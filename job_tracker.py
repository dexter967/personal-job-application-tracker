"""
Personal Job Application Tracker
--------------------------------
A CLI tool to track job applications across various interview stages,
generate summary metrics, update application progress, and persist
records and reports to external text/JSON files.
"""

from datetime import datetime
import json
import os

VALID_STATUSES = ["Applied", "Interview", "Selected", "Rejected"]


# ==========================================
# Step 1: Data Initialization & Storage
# ==========================================

def load_applications(file_path="sample_applications.json"):
    """Loads application records from a JSON file or provides default sample data."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Fallback initial dataset
    return [
        {"id": "APP-101", "company": "Google", "role": "Software Engineer", "status": "Interview", "applied_date": "2026-08-15"},
        {"id": "APP-102", "company": "Microsoft", "role": "Backend Developer", "status": "Applied", "applied_date": "2026-08-20"},
        {"id": "APP-103", "company": "Amazon", "role": "Cloud Architect", "status": "Rejected", "applied_date": "2026-07-10"},
        {"id": "APP-104", "company": "Meta", "role": "Frontend Engineer", "status": "Interview", "applied_date": "2026-08-28"},
        {"id": "APP-105", "company": "Apple", "role": "iOS Developer", "status": "Selected", "applied_date": "2026-06-01"},
        {"id": "APP-106", "company": "Netflix", "role": "Systems Engineer", "status": "Applied", "applied_date": "2026-09-01"},
        {"id": "APP-107", "company": "Stripe", "role": "Full Stack Engineer", "status": "Interview", "applied_date": "2026-09-05"},
    ]


# ==========================================
# Step 2: Core Functions
# ==========================================

def add_application(applications, company, role, status="Applied", applied_date=None):
    """Adds a new job application to the tracking list."""
    if status not in VALID_STATUSES:
        print(f"❌ Invalid status '{status}'. Must be one of: {', '.join(VALID_STATUSES)}")
        return False

    if not applied_date:
        applied_date = datetime.now().strftime("%Y-%m-%d")

    app_id = f"APP-{len(applications) + 101}"
    new_app = {
        "id": app_id,
        "company": company,
        "role": role,
        "status": status,
        "applied_date": applied_date,
    }
    applications.append(new_app)
    print(f"✅ Application for {role} at {company} added successfully! (ID: {app_id})")
    return True


def search_applications(applications, query_type, value):
    """Searches applications by company name or application status."""
    val = value.strip().lower()
    results = []

    for app in applications:
        if query_type == "status" and app["status"].lower() == val:
            results.append(app)
        elif query_type == "company" and val in app["company"].lower():
            results.append(app)

    if not results:
        print(f"🔍 No applications found for {query_type}: '{value}'")
        return []

    print(f"\n--- Search Results for {query_type.upper()}: '{value}' ---")
    for app in results:
        print(f"[{app['id']}] {app['company']} — {app['role']} | Status: {app['status']} | Date: {app['applied_date']}")
    return results


def update_status(applications, app_id, new_status):
    """Updates the recruitment status of a specific application."""
    if new_status not in VALID_STATUSES:
        print(f"❌ Invalid status '{new_status}'. Allowed values: {', '.join(VALID_STATUSES)}")
        return False

    for app in applications:
        if app["id"].upper() == app_id.upper():
            old_status = app["status"]
            app["status"] = new_status
            print(f"✅ Updated {app['company']} ({app['role']}): '{old_status}' ➔ '{new_status}'")
            return True

    print(f"❌ Error: Application ID '{app_id}' not found.")
    return False


# ==========================================
# Step 3: Analytics & Summary Generation
# ==========================================

def generate_summary(applications):
    """Calculates status distribution metrics and extracts active interviews."""
    total_apps = len(applications)
    status_counts = {status: 0 for status in VALID_STATUSES}
    interview_stage_apps = []

    for app in applications:
        status = app.get("status", "Applied")
        if status in status_counts:
            status_counts[status] += 1
        
        if status == "Interview":
            interview_stage_apps.append((app["company"], app["role"], app["applied_date"]))

    return {
        "total": total_apps,
        "status_counts": status_counts,
        "interview_stage": interview_stage_apps,
    }


def print_summary(summary):
    """Prints formatted summary analytics to standard output."""
    print("\n" + "=" * 45)
    print("      JOB APPLICATION TRACKER SUMMARY")
    print("=" * 45)
    print(f"Total Applications Tracked : {summary['total']}")
    print("-" * 45)
    for status, count in summary["status_counts"].items():
        percentage = (count / summary["total"] * 100) if summary["total"] > 0 else 0
        print(f"  • {status:<12}: {count:>2} ({percentage:.1f}%)")
    print("-" * 45)

    print(f"\n🎯 Active Interview Stage ({len(summary['interview_stage'])}):")
    if not summary["interview_stage"]:
        print("  None currently active.")
    else:
        for company, role, date in summary["interview_stage"]:
            print(f"  • {company} — {role} (Applied: {date})")
    print("=" * 45 + "\n")


# ==========================================
# Step 4: Persist Records to Text File
# ==========================================

def save_tracker_report(applications, filename="tracker_report.txt"):
    """Saves complete application inventory and summary dashboard to a text file."""
    summary = generate_summary(applications)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=====================================================\n")
        f.write("         PERSONAL JOB APPLICATION TRACKER REPORT    \n")
        f.write(f"         Generated on: {timestamp}\n")
        f.write("=====================================================\n\n")

        # Section 1: Executive Dashboard
        f.write("📊 EXECUTIVE SUMMARY\n")
        f.write("-" * 53 + "\n")
        f.write(f"Total Applications Submitted : {summary['total']}\n")
        for status, count in summary["status_counts"].items():
            pct = (count / summary["total"] * 100) if summary["total"] > 0 else 0
            f.write(f"  - {status:<10}: {count:>2} ({pct:.1f}%)\n")
        f.write("\n")

        # Section 2: Active Interviews Focus
        f.write("🎯 CURRENT INTERVIEW STAGE ROLES\n")
        f.write("-" * 53 + "\n")
        if summary["interview_stage"]:
            for company, role, date in summary["interview_stage"]:
                f.write(f"  • Company : {company}\n")
                f.write(f"    Role    : {role}\n")
                f.write(f"    Applied : {date}\n")
                f.write("-" * 30 + "\n")
        else:
            f.write("  No active interviews at this time.\n")
        f.write("\n")

        # Section 3: Detailed Inventory Log
        f.write("📋 FULL APPLICATION INVENTORY\n")
        f.write("-" * 53 + "\n")
        f.write(f"{'ID':<8} | {'Company':<15} | {'Role':<20} | {'Status':<10} | {'Date':<10}\n")
        f.write("-" * 75 + "\n")
        for app in applications:
            f.write(
                f"{app['id']:<8} | {app['company'][:15]:<15} | "
                f"{app['role'][:20]:<20} | {app['status']:<10} | {app['applied_date']:<10}\n"
            )

        f.write("\n=====================================================\n")
        f.write("End of Report\n")

    print(f"💾 Application tracker report saved to '{filename}'.")


# ==========================================
# Main CLI Application Loop
# ==========================================

def main():
    applications = load_applications()

    while True:
        print("\n" + "=" * 35)
        print("   JOB APPLICATION TRACKER CLI")
        print("=" * 35)
        print("1. View Full Tracker")
        print("2. Search Applications")
        print("3. Add New Application")
        print("4. Update Application Status")
        print("5. Generate & View Summary")
        print("6. Export Report & Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            print(f"\n{'ID':<8} | {'Company':<15} | {'Role':<22} | {'Status':<10} | {'Date':<10}")
            print("-" * 72)
            for app in applications:
                print(f"{app['id']:<8} | {app['company']:<15} | {app['role']:<22} | {app['status']:<10} | {app['applied_date']:<10}")
        elif choice == "2":
            q_type = input("Search by (company/status): ").strip().lower()
            if q_type in ["company", "status"]:
                val = input(f"Enter {q_type} term: ")
                search_applications(applications, q_type, val)
            else:
                print("❌ Choice must be either 'company' or 'status'.")
        elif choice == "3":
            company = input("Company Name: ")
            role = input("Role Title: ")
            status = input("Initial Status (Applied/Interview/Selected/Rejected) [default: Applied]: ").strip()
            status = status if status else "Applied"
            add_application(applications, company, role, status)
        elif choice == "4":
            app_id = input("Enter Application ID (e.g. APP-101): ").strip()
            new_status = input("Enter New Status (Applied/Interview/Selected/Rejected): ").strip()
            update_status(applications, app_id, new_status)
        elif choice == "5":
            summary = generate_summary(applications)
            print_summary(summary)
        elif choice == "6":
            save_tracker_report(applications)
            print("Exiting Tracker. Best of luck with the job search!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
