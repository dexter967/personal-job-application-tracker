# Obstacle Log: Personal Job Application Tracker

This document details technical challenges encountered during the development of the Personal Job Application Tracker and explains how they were resolved.

---

### Obstacle 1: Case Sensitivity and Formatting Bottlenecks in Search & Updates
* **Issue:** User queries like searching for status `"interview"` or updating ID `"app-101"` failed to match records due to exact case comparisons against stored strings (`"Interview"`, `"APP-101"`).
* **Resolution:** Normalized user inputs using `.strip().lower()` (or `.upper()` for application IDs) before evaluating conditional statements across `search_applications()` and `update_status()`.

---

### Obstacle 2: Flexible Dynamic Status Analytics
* **Issue:** Hardcoding status counters in `generate_summary()` caused missed entries when unexpected or custom statuses were encountered.
* **Resolution:** Created a central global variable `VALID_STATUSES = ["Applied", "Interview", "Selected", "Rejected"]` and initialized dictionary keys dynamically. Enforced validation during input so invalid status strings are rejected early.

---

### Obstacle 3: Output Alignment in Text Reports
* **Issue:** Long role titles or company names distorted column alignment in the text file output, breaking tabular formatting.
* **Resolution:** Used string slicing combined with Python format specifiers (e.g., `{app['role'][:20]:<20}`) to truncate overly long strings to guaranteed maximum lengths while padded to uniform column widths.
