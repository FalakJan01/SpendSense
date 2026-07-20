import csv

def export_csv(transactions):

    with open("report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Type", "Category", "Amount", "Date"])

        for item in transactions:

            writer.writerow([
                item["type"],
                item["category"],
                item["amount"],
                item["date"]
            ])

    print("CSV Exported Successfully!")