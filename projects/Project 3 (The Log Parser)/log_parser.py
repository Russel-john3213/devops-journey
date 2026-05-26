# 1. Open the server.log file in read mode ('r')
error_counter = 0
with open("server.log", "r") as log_file:
    # 2. Use a loop to iterate through every single line in the file
    for line in log_file:
        if "ERROR" in line:
            error_counter += 1
            print(line.strip())

print(f"Total errors found: {error_counter}")

with open("incident_report.txt", "w") as report_file:
    report_file.write(f"Total errors found: {error_counter}\n")
    report_file.write("detailed log\n")
    with open("server.log", "r") as log_file: 
        for line in log_file:
            if "ERROR" in line:
                report_file.write(line.strip() + "\n")