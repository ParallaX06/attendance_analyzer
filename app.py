from flask import Flask, render_template, request, send_file
import csv
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULT_CSV_PATH = os.path.join(UPLOAD_FOLDER, "attendance_result.csv")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    table_data = None
    summary = {}

    if request.method == "POST":
        file = request.files["csv_file"]
        if file.filename.endswith(".csv"):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Read CSV file and process attendance data
            with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
                
                if len(rows) < 2:  # Need at least header and one data row
                    return render_template("index.html", data=table_data, summary=summary)
                
                headers = rows[0]
                data_rows = rows[1:]
                
                # Calculate attendance for each student
                results = []
                all_percentages = []
                
                for row in data_rows:
                    if len(row) < 2:  # Need at least name and one attendance day
                        continue
                        
                    name = row[0]
                    attendance_data = row[1:]  # Skip name column
                    
                    # Count present days
                    present_count = sum(1 for day in attendance_data if day.upper() == 'P')
                    total_days = len(attendance_data)
                    
                    if total_days > 0:
                        percentage = round((present_count / total_days) * 100, 2)
                        status = "PASS" if percentage >= 75 else "FAIL"
                        
                        results.append({
                            "Name": name,
                            "Present": present_count,
                            "Total": total_days,
                            "Percentage": percentage,
                            "Status": status
                        })
                        
                        all_percentages.append(percentage)
                
                # Save results to CSV
                if results:
                    with open(RESULT_CSV_PATH, 'w', newline='', encoding='utf-8') as result_file:
                        fieldnames = ["Name", "Present", "Total", "Percentage", "Status"]
                        writer = csv.DictWriter(result_file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(results)
                    
                    table_data = results
                    
                    # Calculate summary statistics
                    if all_percentages:
                        avg_percent = round(sum(all_percentages) / len(all_percentages), 2)
                        pass_count = sum(1 for result in results if result["Status"] == "PASS")
                        pass_rate = round((pass_count / len(results)) * 100, 2)
                        
                        summary = {
                            "avg_percent": avg_percent,
                            "pass_rate": pass_rate
                        }

    return render_template("index.html", data=table_data, summary=summary)

@app.route("/download")
def download_report():
    return send_file(RESULT_CSV_PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)