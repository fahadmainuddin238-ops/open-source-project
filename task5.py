import os

# ==========================================
# SECTION 1 — LAUNCH YOUR PROJECT
# ==========================================

project_name = input("Enter project name: ")
project_version = input("Enter project version: ")
project_year = int(input("Enter year started: "))
project_language = input("Enter main language: ")
project_lead = input("Enter project lead name: ")

project = (project_name, project_version, project_year, project_language, project_lead)

print("=" * 42)
print(f" {project[0]} — Open Source Project")
print(f" Project Lead : {project[4]}")
print("=" * 42)

print(f"Name : {project[0]} | Version : {project[1]} | Started : {project[2]}")
print(f"Main Language : {project[3]} | Lead : {project[4]}")
print(f"First 3 fields : {project[0:3]}")
print(f"Language count : {project.count(project[3])} Language index : {project.index(project[3])}")

# project[0] = "test"
# This gives TypeError because tuple values cannot be changed.
# Tuple is suitable because project information is fixed and should stay safe.

contributors = []

for i in range(4):
    print(f"\nEnter contributor {i + 1} information:")
    name = input("Name: ")
    role = input("Role: ")
    language = input("Language: ")
    commits = input("Commits: ")
    country = input("Country: ")

    contributor = {
        "name": name,
        "role": role,
        "language": language,
        "commits": commits,
        "country": country
    }

    contributors.append(contributor)

names = []
for contributor in contributors:
    names.append(contributor["name"])

names.sort()

print("-" * 42)
print(f"Sorted names : {names}")
print(f"Last name : {names[-1]}")
print(f"First two : {names[:2]}")

for contributor in contributors:
    contributor.update({"status": "Active"})

print(f"Contributor 1 status : {contributors[0].get('status')}")

backup = contributors[0].copy()
print(f"Backup : {backup}")

# ==========================================
# SECTION 2 — TRACK AND ANALYSE ISSUES
# ==========================================

issues = []

for i in range(5):
    print(f"\nEnter issue {i + 1} information:")
    issue_id = input("ID: ")
    title = input("Title: ")
    issue_type = input("Type (Bug/Feature): ")
    priority = input("Priority (Critical/High/Medium/Low): ")
    reporter = input("Reporter: ")
    status = input("Status (Open/In Progress/Resolved): ")

    issue = {
        "id": issue_id,
        "title": title,
        "type": issue_type,
        "priority": priority,
        "reporter": reporter,
        "status": status
    }

    issues.append(issue)

open_count = 0
for issue in issues:
    if issue["status"] == "Open":
        open_count += 1

print("-" * 42)
print(f"Open issues : {open_count}")

issues[0]["priority"] = "Critical"
print("First issue → priority updated to Critical.")

print(f"Last two issues : {issues[-2:]}")

reporters = set()
for issue in issues:
    reporters.add(issue["reporter"])

tech_stack = set()
for contributor in contributors:
    tech_stack.add(contributor["language"])

tech_stack.add("TypeScript")
tech_stack.discard("Kotlin")

union_set = reporters.union(tech_stack)
intersection_set = reporters.intersection(tech_stack)
difference_set = reporters.difference(tech_stack)

print("-" * 42)
print(f"reporters : {reporters}")
print(f"tech_stack : {tech_stack}")
print(f"union : {union_set}")
print(f"intersection : {intersection_set}")
print(f"difference : {difference_set}")

priority_set = set()
for issue in issues:
    priority_set.add(issue["priority"])

if "Critical" in priority_set:
    print("Critical present : YES — flag for immediate review.")
else:
    print("Critical present : NO")

priority_count = {}
for issue in issues:
    current_priority = issue["priority"]
    if current_priority in priority_count:
        priority_count[current_priority] += 1
    else:
        priority_count[current_priority] = 1

status_groups = {}
for issue in issues:
    current_status = issue["status"]
    current_title = issue["title"]

    if current_status not in status_groups:
        status_groups[current_status] = []

    status_groups[current_status].append(current_title)

print("-" * 42)
print(f"priority keys : {priority_count.keys()}")
print(f"priority values : {priority_count.values()}")

print("Status Groups:")
for status_name, title_list in status_groups.items():
    print(f"{status_name} : {title_list}")

reporter_count = {}
for issue in issues:
    current_reporter = issue["reporter"]
    if current_reporter in reporter_count:
        reporter_count[current_reporter] += 1
    else:
        reporter_count[current_reporter] = 1

top_reporter = ""
top_reporter_count = 0

for reporter_name, count_value in reporter_count.items():
    if count_value > top_reporter_count:
        top_reporter = reporter_name
        top_reporter_count = count_value

print(f"Top reporter : {top_reporter} ({top_reporter_count} issues)")

removed_type = issues[0].pop("type")
print(f"Removed type : {removed_type}")
print(f"After pop('type') : {issues[0]}")

# ==========================================
# SECTION 3 — SAVE, READ AND REPORT
# ==========================================

folder_name = project[0].lower().replace(" ", "_")

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder created : {folder_name}/")
else:
    print(f"Folder already exists : {folder_name}/")

report_path = os.path.join(folder_name, "project_report.txt")
csv_path = os.path.join(folder_name, "issues.csv")

try:
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(f"{'=' * 42}\n")
        file.write(f"{project[0]} — PROJECT REPORT\n")
        file.write(f"{'=' * 42}\n")
        file.write(f"Project Name : {project[0]}\n")
        file.write(f"Version : {project[1]}\n")
        file.write(f"Year Started : {project[2]}\n")
        file.write(f"Main Language : {project[3]}\n")
        file.write(f"Project Lead : {project[4]}\n")
        file.write("\n")

        file.write("CONTRIBUTORS\n")
        file.write(f"{'-' * 42}\n")
        for contributor in contributors:
            file.write(
                f"Name: {contributor['name']}, Role: {contributor['role']}, "
                f"Language: {contributor['language']}, Commits: {contributor['commits']}, "
                f"Country: {contributor['country']}, Status: {contributor['status']}\n"
            )

        file.write("\n")
        file.write("ISSUES\n")
        file.write(f"{'-' * 42}\n")
        for issue in issues:
            file.write(
                f"ID: {issue['id']}, Title: {issue['title']}, Priority: {issue['priority']}, "
                f"Reporter: {issue['reporter']}, Status: {issue['status']}\n"
            )

        file.write("\n")
        file.write("ANALYSIS\n")
        file.write(f"{'-' * 42}\n")
        file.write(f"Total Contributors : {len(contributors)}\n")
        file.write(f"Sorted Names : {names}\n")
        file.write(f"Total Issues : {len(issues)}\n")
        file.write(f"Open Issues : {open_count}\n")
        file.write(f"Reporters : {reporters}\n")
        file.write(f"Tech Stack : {tech_stack}\n")
        file.write(f"Top Reporter : {top_reporter} ({top_reporter_count} issues)\n")
        file.write("Priority Breakdown:\n")
        for priority_name, priority_total in priority_count.items():
            file.write(f"{priority_name} : {priority_total}\n")

    with open(csv_path, "w", encoding="utf-8") as file:
        file.write("id,title,priority,reporter,status\n")
        for issue in issues:
            file.write(
                f"{issue['id']},{issue['title']},{issue['priority']},{issue['reporter']},{issue['status']}\n"
            )

    print(f"Files saved : {os.listdir(folder_name)}")

except IOError:
    print("An IOError happened while writing files.")

try:
    with open(report_path, "r", encoding="utf-8") as file:
        print("\n--- read() ---")
        print(file.read())

    with open(report_path, "r", encoding="utf-8") as file:
        print("--- readline() ---")
        print(f"Line 1 : {file.readline().strip()}")
        print(f"Line 2 : {file.readline().strip()}")

    with open(report_path, "r", encoding="utf-8") as file:
        print("--- readlines() ---")
        all_lines = file.readlines()
        total_lines = len(all_lines)

        important_lines = []
        for line in all_lines:
            if "Critical" in line or "High" in line:
                important_lines.append(line.strip())

        print(f"Total lines : {total_lines}")
        print(f"Critical/High lines : {len(important_lines)}")
        for line in important_lines:
            print(line)

except FileNotFoundError:
    print("File not found while reading.")

# ==========================================
# BONUS PART
# ==========================================

urgent = [issue["title"] for issue in issues if issue["priority"] == "Critical" or issue["priority"] == "High"]

print("-" * 42)
print(f"Urgent issues : {urgent}")
print(f"Urgent issues count : {len(urgent)}")

try:
    with open(report_path, "a", encoding="utf-8") as file:
        file.write("\n")
        file.write("URGENT ISSUES\n")
        file.write(f"{'-' * 42}\n")
        for title in urgent:
            file.write(f"{title}\n")

    with open(report_path, "r", encoding="utf-8") as file:
        appended_lines = file.readlines()
        print("\nLast 6 lines after append:")
        for line in appended_lines[-6:]:
            print(line.strip())

except IOError:
    print("An error happened while appending urgent issues.")
except FileNotFoundError:
    print("Report file not found.")

# ==========================================
# FINAL SUMMARY
# ==========================================

priority_parts = []
for priority_name, priority_total in priority_count.items():
    priority_parts.append(f"{priority_name}:{priority_total}")

priority_summary = " ".join(priority_parts)

print("=" * 42)
print(f" {project[0]} — FINAL SUMMARY")
print("=" * 42)
print(f"Project : {project[0]} Version : {project[1]} Lead : {project[4]}")
print(f"Contributors : {len(contributors)} Names : {names}")
print(f"Tech Stack : {tech_stack}")
print(f"Issues : {len(issues)} Open : {open_count} Reporters : {len(reporters)}")
print(f"Top Reporter : {top_reporter} ({top_reporter_count} issues)")
print(f"{priority_summary}")
print(f"Report : {report_path}")
print(f"CSV : {csv_path}")
print("=" * 42)
print(f"{project[0]} complete. Thank you for contributing to open source!")
print("=" * 42)

