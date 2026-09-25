# Personal Job Application Tracker 💼

A simple, dependency-free CLI tool built in standard Python to organize, track, and analyze software engineering job applications across recruitment stages.

---

## 🎯 Key Features

- **Lifecycle Tracking**: Monitor applications across key stages: `Applied`, `Interview`, `Selected`, `Rejected`.
- **Targeted Filtering**: Search job entries by status or company name.
- **Analytics & Insights**: Generates status distribution metrics and highlights companies currently sitting at the `Interview` phase.
- **Persistent Reports**: Exports a formatted report (`tracker_report.txt`) containing summary dashboards and full application inventories.

---

## 📂 Repository Structure

```text
├── job_tracker.py             # Core CLI script and business logic
├── sample_applications.json   # Seed data containing initial job applications
├── tracker_report.txt         # Auto-generated report output file
├── obstacle_log.md            # Log of bugs, edge cases, and technical solutions
└── README.md                  # Project overview and documentation
