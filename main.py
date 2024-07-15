from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class WorkTimeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Time Calculator")

        self.groups = []
        self.add_time_group()

        # Add button to add more time groups
        self.add_button = Button(root, text="+", command=self.add_time_group)
        self.add_button.grid(row=0, column=2)

        # Hourly wage input
        Label(root, text="Hourly Wage:").grid(row=0, column=3)
        self.wage_entry = Entry(root)
        self.wage_entry.grid(row=0, column=4)

        # Go button
        self.go_button = Button(root, text="Go", command=self.calculate_wages)
        self.go_button.grid(row=0, column=5)

        # Result label
        self.result_label = Label(root, text="")
        self.result_label.grid(row=1, column=0, columnspan=6)

    def add_time_group(self):
        row = len(self.groups) + 1
        start_time_entry = Entry(self.root)
        start_time_entry.grid(row=row, column=0)

        end_time_entry = Entry(self.root)
        end_time_entry.grid(row=row, column=1)

        self.groups.append((start_time_entry, end_time_entry))

    def calculate_wages(self):
        total_minutes = 0
        try:
            for start_time_entry, end_time_entry in self.groups:
                start_time = datetime.strptime(start_time_entry.get(), "%H:%M")
                end_time = datetime.strptime(end_time_entry.get(), "%H:%M")
                diff = (end_time - start_time).seconds / 60
                total_minutes += diff

            hourly_wage = float(self.wage_entry.get())
            total_hours = total_minutes / 60
            total_wages = total_hours * hourly_wage

            self.result_label.config(text=f"Total Minutes: {total_minutes:.2f}, Total Wages: ${total_wages:.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid times in HH:MM format and a numeric hourly wage.")

if __name__ == "__main__":
    root = Tk()
    app = WorkTimeCalculator(root)
    root.mainloop()
