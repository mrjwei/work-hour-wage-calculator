from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime

class WorkHourWageCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Time Calculator")
        self.total_rows = 4

        # Hourly wage input
        Label(self.root, text="Hourly Wage:").grid(row=0, column=0, columnspan=2, sticky=W)
        self.wage_entry = Entry(self.root)
        self.wage_entry.grid(row=1, column=0, columnspan=2, sticky='we')

        Label(self.root, text='Start:').grid(row=2, column=0, sticky=W)
        Label(self.root, text='End:').grid(row=2, column=1, sticky=W)

        start_time_entry = Entry(self.root)
        start_time_entry.grid(row=3, column=0)

        end_time_entry = Entry(self.root)
        end_time_entry.grid(row=3, column=1)

        self.groups = [(start_time_entry, end_time_entry)]

        # Add button to add more time groups
        self.add_button = Button(self.root, text="+ Add", command=self.add_time_group)
        self.add_button.grid(row=self.total_rows, column=0, columnspan=2, sticky='we')

        # Go button
        self.go_button = Button(self.root, text="Go", command=self.calculate_wages)
        self.go_button.grid(row=0, column=2)
        # Quit button
        self.quit_button = Button(self.root, text="Quit", command=lambda: self.root.quit())
        self.quit_button.grid(row=0, column=3)

        # Result label
        self.result_label = Label(self.root, text="")
        self.result_label.grid(row=1, column=2, columnspan=2)

    def add_time_group(self):
        label_row = self.total_rows
        entry_row = label_row + 1

        Label(self.root, text='Start:').grid(row=label_row, column=0, sticky=W)
        Label(self.root, text='End:').grid(row=label_row, column=1, sticky=W)

        start_time_entry = Entry(self.root)
        start_time_entry.grid(row=entry_row, column=0)

        end_time_entry = Entry(self.root)
        end_time_entry.grid(row=entry_row, column=1)

        self.total_rows += 2
        self.add_button.grid(row=self.total_rows, column=0, columnspan=2, sticky='we')
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
    app = WorkHourWageCalculator(root)
    root.mainloop()
