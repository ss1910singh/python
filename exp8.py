#Satish Singh-22AD1003
import tkinter as tk
from tkinter import messagebox
import csv
import os

class AddressBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Address Book")

        # Entry fields
        tk.Label(master, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(master, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(master, text="Email:").grid(row=2, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.file_path = "address_book.csv"
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Phone', 'Email'])

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, phone, email])
            messagebox.showinfo("Success", "Contact added successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

def main():
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
