# README for SAMJAY DATA DRIVEN MENTAL HEALTH DIAGNOSIS WITH DASHBOARD IN MOBILE PHONE - BY Alpha Coders.

## Overview
This is a Flask-based web application for tracking user moods and assessing mental health using the PHQ-9 questionnaire. The application includes user authentication, mood rating, PHQ-9 scoring, trend analysis, and a calendar-based interface for viewing and updating moods.

---

## Features
1. **User Authentication**  
   - Login functionality with predefined users stored in a simple dictionary.
     ![login page](https://github.com/user-attachments/assets/cc926d92-457f-4c49-92bb-209af9935068)
     

![Home page](https://github.com/user-attachments/assets/0e5e0a8a-7621-4f55-a802-18d57b0c7a4a)

2. **PHQ-9 Questionnaire**  
   - A form-based interface to complete the PHQ-9 depression assessment.
   - Automatic calculation of severity levels based on scores.
     ![PHQ9](https://github.com/user-attachments/assets/33e0aed2-1e05-4b7f-b7f1-3f396a451489)


3. **Mood Tracking**  
   - Daily mood ratings stored in a CSV file.
   - Visualization of mood trends over time (month, week, day).
     ![rating](https://github.com/user-attachments/assets/04bd341b-9785-47bd-aa2a-f43297904f73)


4. **Mood Calendar**  
   - A calendar view to display and update moods for each day of the current month.
     
     ![mood calendar](https://github.com/user-attachments/assets/fb0b0c22-6609-4732-af15-834123fc6b62)


5. **Trend Analysis**  
   - Aggregated statistics for mood trends by month, week, and day of the week.
  

![fccae660-579c-4928-a554-944c01a75c1c](https://github.com/user-attachments/assets/a7ef58b6-8f41-4afe-bd11-c9f2bd09e9ac)

6. **Data Storage**  
   - All data is stored locally in CSV files: `phq9.csv` and `user_moods.csv`.
     ![data stored](https://github.com/user-attachments/assets/75a7be45-bfe6-4329-9ab6-03027bc940a7)

7. **Dashboard**
   -Comprehensive Mental Health Tracking: Seamlessly journal your thoughts and emotions while accessing a dynamic dashboard to view your progress and insights, available across both mobile and desktop for anytime, anywhere convenience.
   
**desktop**

![Screenshot 2025-01-22 000901](https://github.com/user-attachments/assets/4ee684c5-b23f-4a3c-b655-ff66e95a16bd)

   
7. **Mobile access**
   ![mobile viz](https://github.com/user-attachments/assets/ee4ec0c0-55a1-4b63-956f-3aa4c1e04f82)
   
9. **Journaling app**
   -Capture your thoughts and emotions effortlessly with a built-in journaling feature, complemented by a dynamic dashboard to track your mental health journey. Accessible on both mobile and desktop for ultimate flexibility
   
11. **Mobile access**
   
![WhatsApp Image 2025-01-21 at 11 31 53 PM](https://github.com/user-attachments/assets/1abb5d1a-b7ab-46f1-b9b5-94c8f1e1a0c7)

12. **desktop access**
![journaling in desktop](https://github.com/user-attachments/assets/0065fb69-dbce-4f8e-ae00-b476a1e3b926)




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


