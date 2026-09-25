# Personal Job Application Tracker 💼

A simple, dependency-free CLI tool built in standard Python to organize, track, and analyze software engineering job applications across recruitment stages.

---

## 🎯 Key Features

- **Lifecycle Tracking**: Monitor applications across key stages: `Applied`, `Interview`, `Selected`, `Rejected`.
- **Targeted Filtering**: Search job entries by status or company name.
- **Analytics & Insights**: Generates status distribution metrics and highlights companies currently sitting at the `Interview` phase.
- **Persistent Reports**: Exports a formatted report (`tracker_report.txt`) containing summary dashboards and full application inventories.

---

## 🛠️ Core Functions Reference

The system is built around dedicated, single-responsibility functions in `job_tracker.py`:

| Function | Signature | Description |
| :--- | :--- | :--- |
| **`load_applications`** | `load_applications(file_path)` | Loads existing application records from a JSON file. Falls back to a seed dataset if the file is missing. |
| **`add_application`** | `add_application(applications, company, role, status, applied_date)` | Validates status input, generates a unique ID (`APP-xxx`), and appends a new application record to the tracker. |
| **`search_applications`**| `search_applications(applications, query_type, value)` | Filters applications by `company` name or `status` (case-insensitive) and prints matching results. |
| **`update_status`** | `update_status(applications, app_id, new_status)` | Updates an existing application's status stage after validating against allowed status values. |
| **`generate_summary`** | `generate_summary(applications)` | Calculates status distribution counts, percentage breakdowns, and extracts active `Interview` stage roles. |
| **`save_tracker_report`** | `save_tracker_report(applications, filename)` | Exports an executive summary dashboard and fixed-width tabular log to `tracker_report.txt`. |

---

## 📂 Repository Structure

```text
├── job_tracker.py             # Core CLI script and business logic
├── sample_applications.json   # Seed data containing initial job applications
├── tracker_report.txt         # Auto-generated report output file
├── obstacle_log.md            # Log of bugs, edge cases, and technical solutions
└── README.md                  # Project overview and documentation
