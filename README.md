# 📊 Attendance Tracker

A Flask web application for analyzing student attendance data from CSV files.

## ✨ Features

- Upload CSV files with attendance data (P/A format)
- Calculate attendance percentages for each student
- Determine pass/fail status based on 75% threshold
- Display beautiful summary statistics
- Download processed results as CSV
- Modern, responsive web interface

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open your browser:**
   Navigate to `http://127.0.0.1:5000`

## 📋 CSV Format

Your CSV file should have the following format:
- First column: Student names
- Subsequent columns: Attendance data using 'P' for Present and 'A' for Absent

Example:
```csv
Name,Day1,Day2,Day3,Day4,Day5
John Smith,P,P,A,P,P
Jane Doe,P,P,P,P,A
Mike Johnson,A,P,A,P,A
```

## 📁 Sample Data

Use the included `sample_attendance.csv` file to test the application.

## 🎯 Features

- **Automatic Calculation**: Calculates present days, total days, and percentage
- **Pass/Fail Status**: Students with ≥75% attendance get "PASS" status
- **Summary Statistics**: Shows average attendance and pass rate
- **Download Reports**: Export results as CSV file
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technical Details

- **Framework**: Flask 3.0.0
- **Data Processing**: Python built-in CSV module
- **Frontend**: HTML5, CSS3, JavaScript
- **File Upload**: Secure file handling with validation
- **Compatibility**: Python 3.13+ ready
