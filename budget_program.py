import tkinter as tk
from tkinter import ttk, messagebox
import csv


class BudgetingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Weekly Budgeting")

        self.messagebox = messagebox

        # Create and arrange the widgets for entering expenditure
        expenditure_frame = tk.LabelFrame(window, text="Weekly Expenditure")
        expenditure_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.expenditure_category_label = tk.Label(expenditure_frame, text="Expenditure Category:")
        self.expenditure_category_label.grid(row=0, column=0, padx=5, pady=5)
        self.expenditure_category_var = tk.StringVar()
        self.expenditure_category_combobox = ttk.Combobox(expenditure_frame, textvariable=self.expenditure_category_var,
                                                          values=[
                                                              "Groceries", "Takeaways", "Entertainment", "Phone",
                                                              "Power", "Music", "Fuel", "Medical", "Savings",
                                                              "Rent", "Gym"
                                                          ])
        self.expenditure_category_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.expenditure_amount_label = tk.Label(expenditure_frame, text="Amount:")
        self.expenditure_amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.expenditure_amount_entry = tk.Entry(expenditure_frame)
        self.expenditure_amount_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create a button to save the expenditure data to the CSV file
        save_expenditure_button = tk.Button(expenditure_frame, text="Save Expenditure Data",
                                            command=self.save_expenditure_data)
        save_expenditure_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # ... (create other expenditure entry widgets)

        # Create and arrange the widgets for entering income
        income_frame = tk.LabelFrame(window, text="Weekly Income")
        income_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.income_category_label = tk.Label(income_frame, text="Income Category:")
        self.income_category_label.grid(row=0, column=0, padx=5, pady=5)
        self.income_category_var = tk.StringVar()
        self.income_category_combobox = ttk.Combobox(income_frame, textvariable=self.income_category_var,
                                                     values=[
                                                         "Student Living Payments", "Jobless Income",
                                                         "Job income", "Debt Repayments"
                                                     ])
        self.income_category_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.income_amount_label = tk.Label(income_frame, text="Amount:")
        self.income_amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.income_amount_entry = tk.Entry(income_frame)
        self.income_amount_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create a button to save the income data to the CSV file
        save_income_button = tk.Button(income_frame, text="Save Income Data", command=self.save_income_data)
        save_income_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # ... (create other income entry widgets)

    @staticmethod
    def save_data_to_csv(data):
        with open("budget.csv", mode="a", newline="") as file:  # Append mode to add to the existing file
            writer = csv.writer(file)
            for category, items in data.items():
                writer.writerow([category])
                for item, value in items.items():
                    writer.writerow([item, value])
                writer.writerow([])

            messagebox.showinfo("Data Saved", "Data has been successfully saved to budget.csv.")

    def save_expenditure_data(self):
        data = {
            "Weekly Expenditure": {
                "Expenditure Category": self.expenditure_category_var.get(),
                "Amount": self.expenditure_amount_entry.get(),
            }
        }
        self.save_data_to_csv(data)

    def save_income_data(self):
        data = {
            "Weekly Income": {
                "Income Category": self.income_category_var.get(),
                "Amount": self.income_amount_entry.get(),
            }
        }
        self.save_data_to_csv(data)


def main():
    window = tk.Tk()
    app = BudgetingApp(window)
    window.mainloop()


if __name__ == "__main__":

    main()
