from flask import Flask, request, render_template, redirect, url_for, jsonify
import pandas as pd
import os
import csv
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)

# Define the CSV files
phq9_csv = "phq9.csv"
mood_csv = "user_moods.csv"
mood_categories = ['happy', 'anxious', 'stressed', 'peaceful', 'motivated']

# User database (for simplicity)
database = {'Student': '123', 'Sam': 'abc', 'sasirudh': '1234'}

# Initialize mood CSV if it doesn't exist
def create_mood_csv():
    if not os.path.isfile(mood_csv):
        with open(mood_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Month', 'Year', 'Mood', 'Week Number', 'Day of Week'])  # Write header

# Initialize PHQ9 CSV if it doesn't exist
def create_phq9_csv():
    if not os.path.isfile(phq9_csv):
        headers = ['date', 'time', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total', 'severity', 'mood']
        df = pd.DataFrame(columns=headers)
        df.to_csv(phq9_csv, index=False)

# Helper function to assess PHQ-9 severity
def assess_severity(score):
    if score <= 4:
        return "subclinical"
    elif score <= 9:
        return "mild"
    elif score <= 14:
        return "moderate"
    elif score <= 19:
        return "moderately severe"
    else:
        return "severe"

@app.route('/')
def login_page():
    return render_template("login.html")

@app.route('/form_login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username not in database:
        return render_template('login.html', info='Invalid User')
    elif database[username] != password:
        return render_template('login.html', info='Invalid Password')
    else:
        return redirect(url_for('home', name=username))

@app.route('/home')
def home():
    name = request.args.get('name', 'User')
    df = pd.read_csv('phq9.csv')
    mood = df['mood'].iloc[-1] if 'mood' in df.columns and not df.empty else "No mood rating yet"
    return render_template("home.html", name=name, mood=mood)

# Function to get moods for the current month
def get_moods_for_month(year, month):
    moods_for_month = {}
    with open(mood_csv, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date = row[0]
            row_month = row[1]
            row_year = row[2]
            mood = row[3]

            if row_month == month and row_year == year:
                moods_for_month[date] = mood

    return moods_for_month


# Get week number and day of the week
def get_week_and_day(date, month, year):
    date_str = f'{month} {date}, {year}'
    date_obj = datetime.strptime(date_str, '%B %d, %Y')
    week_number = date_obj.strftime('%U')  # Week number (0-52)
    day_of_week = date_obj.strftime('%A')  # Day of the week (e.g., Monday)
    return week_number, day_of_week

# Update mood in the mood CSV
def update_mood(date, month, year, mood):
    if mood not in mood_categories:
        return "Invalid mood."

    week_number, day_of_week = get_week_and_day(date, month, year)

    data = []
    with open(mood_csv, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    updated = False
    for row in data:
        if row[0] == date and row[1] == month and row[2] == year:
            row[3] = mood
            row[4] = week_number
            row[5] = day_of_week
            updated = True
            break

    if not updated:
        data.append([date, month, year, mood, week_number, day_of_week])

    with open(mood_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return f"Mood for {month} {date}, {year} updated to {mood}."

# Analyze mood trends from the mood CSV
def analyze_mood_trends():
    mood_counts = {mood: 0 for mood in mood_categories}
    month_counts = defaultdict(lambda: {mood: 0 for mood in mood_categories})
    week_counts = defaultdict(lambda: {mood: 0 for mood in mood_categories})
    day_of_week_counts = defaultdict(lambda: {mood: 0 for mood in mood_categories})

    with open(mood_csv, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date = row[0]
            month = row[1]
            year = row[2]
            mood = row[3]
            week_number = row[4]
            day_of_week = row[5]

            if mood in mood_counts:
                mood_counts[mood] += 1

            month_counts[month][mood] += 1
            week_counts[week_number][mood] += 1
            day_of_week_counts[day_of_week][mood] += 1

    return mood_counts, month_counts, week_counts, day_of_week_counts

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        # Save answers and calculate the total score
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        try:
            answers = [int(request.form[f'q{i}']) for i in range(1, 10)]
        except ValueError:
            return "Error: Please provide valid answers for all questions.", 400
        
        total_score = sum(answers) - 9
        severity = assess_severity(total_score)

        # Save to CSV
        df = pd.read_csv(phq9_csv)
        row_to_append = [date, time] + answers + [total_score, severity, None]
        if len(row_to_append) == len(df.columns):
            df.loc[len(df)] = row_to_append
        else:
            return "Error: Mismatched columns in CSV file.", 500

        df.to_csv(phq9_csv, index=False)
        return render_template('results.html', total=total_score, severity=severity)

    return render_template('questionnaire.html')

@app.route('/results')
def display_scores():
    df = pd.read_csv(phq9_csv)
    summary = df[['date', 'time', 'total', 'severity']]
    return render_template('scores.html', tables=[summary.to_html(classes='data')], titles=summary.columns.values)

@app.route('/mood', methods=['GET', 'POST'])
def rate_mood():
    if request.method == 'POST':
        mood_rating = request.form['mood']
        df = pd.read_csv(phq9_csv)

        if not df.empty:
            df.loc[len(df) - 1, 'mood'] = mood_rating
            df.to_csv(phq9_csv, index=False)
            
            # Update mood in mood CSV
            now = datetime.now()
            date = now.strftime("%d")
            month = now.strftime("%B")
            year = now.strftime("%Y")
            update_mood(date, month, year, mood_rating)

        return redirect(url_for('home', name=request.args.get('name', 'User')))

    return render_template('mood_rating.html')
import calendar
from datetime import datetime
import pandas as pd
from flask import request

@app.route('/mood_calendar', methods=['GET', 'POST'])
def mood_calendar():
    # Get the current month and year
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    # Generate a calendar for the current month
    cal = calendar.monthcalendar(current_year, current_month)

    # Read the mood data from the CSV file
    df = pd.read_csv(mood_csv)
    
    # Store moods by day (only keep date and mood)
    mood_by_day = {int(row['Date']): row['Mood'] for index, row in df.iterrows()}

    if request.method == 'POST':
        # Get the selected moods for each day
        selected_moods = request.form.getlist('mood')

        # Update the CSV with the selected moods
        for day, mood in zip(range(1, 32), selected_moods):
            if mood:
                # Check if the day already exists in the CSV
                if day in mood_by_day:
                    # Update existing mood
                    df.loc[df['Date'] == day, 'Mood'] = mood
                else:
                    # Add a new mood entry for the day
                    new_row = {'Date': day, 'Mood': mood}
                    df = df.append(new_row, ignore_index=True)

        # Save the updated moods back to the CSV
        df.to_csv(mood_csv, index=False)

        # Redirect to the same page to show updated mood data
        return redirect(url_for('mood_calendar'))

    return render_template('mood_calendar.html', cal=cal, mood_by_day=mood_by_day, year=current_year, month=current_month)



@app.route('/trend_analysis')
def trend_analysis():
    mood_counts, month_counts, week_counts, day_of_week_counts = analyze_mood_trends()

    return render_template('trend_analysis.html', mood_counts=mood_counts,
                           month_counts=month_counts, week_counts=week_counts,
                           day_of_week_counts=day_of_week_counts)

if __name__ == '__main__':
    create_mood_csv()  # Create mood CSV if it doesn't exist
    create_phq9_csv()  # Create PHQ9 CSV if it doesn't exist
    app.run(debug=True)
