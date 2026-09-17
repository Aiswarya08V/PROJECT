# app.py - Simulates exam evaluation report generation
with open("exam_summary_report.txt", "w") as f:
    f.write("=========================================\n")
    f.write("ONLINE EXAMINATION EVALUATION SUMMARY\n")
    f.write("=========================================\n")
    f.write("Total Students Registered: 350\n")
    f.write("Students Appeared: 342\n")
    f.write("Passed: 310\n")
    f.write("Failed: 32\n")
    f.write("Average Score: 76.5%\n")
    f.write("Report generated successfully.\n")

print("Exam metrics written to exam_summary_report.txt")
