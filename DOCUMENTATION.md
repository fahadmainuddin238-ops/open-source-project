# 📘 Project Documentation

## 🧩 Overview

This project is a **Python CLI-based Open Source Project Manager**.
It simulates real-world open-source workflows including contributors, issues, and reporting.

---

## 🏗️ Project Structure

The program is divided into **4 main sections**:

---

## 🔹 SECTION 1 — Project & Contributors

### Project Data

Stored using a **tuple**:

* Name
* Version
* Year
* Language
* Project Lead

➡️ Tuple is used because data is **immutable (safe & fixed)**

---

### Contributors

Each contributor is stored as a **dictionary**:

```python
{
  "name": "",
  "role": "",
  "language": "",
  "commits": "",
  "country": ""
}
```

Features:

* Stored in a list
* Sorted by name
* Status added dynamically (`Active`)
* Backup copy created

---

## 🔹 SECTION 2 — Issue Tracking & Analysis

Each issue is stored as:

```python
{
  "id": "",
  "title": "",
  "type": "",
  "priority": "",
  "reporter": "",
  "status": ""
}
```

---

### 📊 Analysis Performed

* Count of open issues
* Priority update (first issue → Critical)
* Last two issues extraction
* Unique reporters using **set**
* Tech stack extraction from contributors

---

### ⚙️ Set Operations

* Union → reporters + tech stack
* Intersection → common elements
* Difference → unique reporters

---

### 📈 Advanced Analysis

* Priority count dictionary
* Status grouping (Open / In Progress / Resolved)
* Top reporter detection
* Removal of issue field using `.pop()`

---

## 🔹 SECTION 3 — File Handling

### Folder Creation

```
project_name/
```

---

### Files Generated

#### 1. `project_report.txt`

Contains:

* Project details
* Contributor list
* Issues list
* Analysis summary

#### 2. `issues.csv`

```
id,title,priority,reporter,status
```

---

### File Operations Used

* `write()` → save data
* `read()` → full file
* `readline()` → line by line
* `readlines()` → list of lines
* `append()` → add urgent issues

---

## 🔹 BONUS — Urgent Issues

* Extract issues with:

  * Critical
  * High priority

Stored and appended to report file.

---

## 🔚 FINAL SUMMARY OUTPUT

Displays:

* Project info
* Contributor count
* Tech stack
* Issue stats
* Top reporter
* File paths

---

## 🧠 Key Learning Outcomes

* Data Structures (Tuple, List, Dict, Set)
* File Handling in Python
* CLI-based input/output
* Real-world project simulation
* Basic analytics logic

---

## ⚠️ Limitations

* No database (data not persistent after run)
* No input validation
* Fixed number of contributors/issues
* CLI only (no UI)

---

## 🚀 Future Improvements

* Add database (SQLite)
* Convert to Web App (Flask / React)
* Add authentication system
* Dynamic input sizes
* API integration

---

This project is ideal for beginners learning Python and open-source workflows.
