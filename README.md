# README for Flask Mood and PHQ-9 Tracker Application

## Overview
This is a Flask-based web application for tracking user moods and assessing mental health using the PHQ-9 questionnaire. The application includes user authentication, mood rating, PHQ-9 scoring, trend analysis, and a calendar-based interface for viewing and updating moods.

---

## Features
1. **User Authentication**  
   - Login functionality with predefined users stored in a simple dictionary.

2. **PHQ-9 Questionnaire**  
   - A form-based interface to complete the PHQ-9 depression assessment.
   - Automatic calculation of severity levels based on scores.

3. **Mood Tracking**  
   - Daily mood ratings stored in a CSV file.
   - Visualization of mood trends over time (month, week, day).

4. **Mood Calendar**  
   - A calendar view to display and update moods for each day of the current month.

5. **Trend Analysis**  
   - Aggregated statistics for mood trends by month, week, and day of the week.

6. **Data Storage**  
   - All data is stored locally in CSV files: `phq9.csv` and `user_moods.csv`.

---

## File Structure
- **app.py**: The main Flask application.
- **Templates**: Contains HTML files for the application:
  - `login.html`: Login page.
  - `home.html`: Home page displaying the latest mood.
  - `questionnaire.html`: PHQ-9 questionnaire form.
  - `results.html`: Displays the PHQ-9 score and severity.
  - `scores.html`: Summary of past PHQ-9 results.
  - `mood_rating.html`: Interface for rating mood.
  - `mood_calendar.html`: Calendar view for daily moods.
  - `trend_analysis.html`: Visualizations of mood trends.

---

## Dependencies
- Python 3.x
- Flask
- Pandas
- Calendar (built-in)
- datetime (built-in)

---

## Setup
1. **Clone or download the repository.**
2. **Install required Python libraries:**
   ```bash
   pip install flask pandas
   ```
3. **Ensure the CSV files exist or are created automatically on the first run.**
   - `phq9.csv`: Stores PHQ-9 responses and scores.
   - `user_moods.csv`: Stores daily mood ratings.

4. **Run the application:**
   ```bash
   python app.py
   ```
   The application will run locally at `http://127.0.0.1:5000`.

---

## Usage
1. **Login**
   - Use the predefined credentials in the `database` dictionary:
     ```python
     database = {'Student': '123', 'Sam': 'abc', 'sasirudh': '1234'}
     ```
2. **Navigate to the Home Page**
   - View the latest mood or proceed to other functionalities.
3. **Complete the PHQ-9 Questionnaire**
   - Fill in the form to calculate and save your PHQ-9 score.
4. **Rate Your Mood**
   - Use the mood rating interface to log your current mood.
5. **View and Update Moods in the Calendar**
   - Use the calendar to review or update moods for specific days.
6. **Analyze Trends**
   - Visit the trend analysis page to view mood statistics over time.

---

## CSV Data Format
1. **`phq9.csv`:**
   - Columns: `date, time, q1-q9, total, severity, mood`
   - Stores individual PHQ-9 responses and associated scores.

2. **`user_moods.csv`:**
   - Columns: `Date, Month, Year, Mood, Week Number, Day of Week`
   - Tracks daily mood ratings and associated metadata.

---

## Development Notes
- **Debug Mode**: Enabled by default for easier development (`app.run(debug=True)`).
- **Customization**: Add more mood categories by updating the `mood_categories` list.
- **Security**: Consider integrating a database like SQLite or MySQL for production use.

---

## License
This project is provided "as-is" for educational purposes.


