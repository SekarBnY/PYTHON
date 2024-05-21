import tkinter
from tkinter import ttk, messagebox
from datetime import datetime

def clear_item():
    quantity_spinbox.delete(0, tkinter.END)
    quantity_spinbox.insert(0, "1")
    item_combobox.set("")
    price_label.config(text="")

def add_item(item_prices):
    quantity = int(quantity_spinbox.get())
    item = item_combobox.get()
    if item in item_prices:
        price = item_prices[item]
        line_total = quantity * price
        invoice_item = [quantity, item, price, line_total]

        tree.insert('', 'end', values=invoice_item)
        clear_item()
        update_totals()
    else:
        messagebox.showerror("Error", "Please select a valid item")

def new_invoice():
    name_entry.delete(0, tkinter.END)
    type_of_customer_combobox.set("")
    phone_number_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    update_totals()

def update_totals():
    total = sum(tree.item(child)['values'][3] for child in tree.get_children())
    initial_total_entry.delete(0, tkinter.END)
    initial_total_entry.insert(0, f"IDR {total:.2f}")
    tax = total * 0.1
    tax_entry.delete(0, tkinter.END)
    tax_entry.insert(0, f"IDR {tax:.2f}")
    grand_total = total + tax
    grand_total_entry.delete(0, tkinter.END)
    grand_total_entry.insert(0, f"IDR {grand_total:.2f}")

def check_entries():
    user = name_entry.get()
    type_of_customer = type_of_customer_combobox.get()
    phone_number = phone_number_entry.get()

    if not user:
        messagebox.showerror("Error", "Please fill in your name")
        return False
    if not type_of_customer:
        messagebox.showerror("Error", "Please fill in your type of customer")
        return False
    if not phone_number:
        messagebox.showerror("Error", "Please fill in your phone number")
        return False
    if not phone_number.isdigit():
        messagebox.showerror("Error", "Phone number must be a number")
        phone_number_entry.delete(0, tkinter.END)
        return False
    return True

def update_price(event):
    selected_item = item_combobox.get()
    price = item_prices.get(selected_item, 0)
    price_label.config(text=f"IDR {price:.2f}")

window = tkinter.Tk()
window.title("Invoice Generator by Sekar Bestari Nindita Yasmin (21120123130072)")
window.configure(background="white")

frame = tkinter.Frame(window, background="white")
frame.pack(padx=25, pady=25)

name_label = tkinter.Label(frame, text="Name")
name_label.grid(row=0, column=0)
name_entry = tkinter.Entry(frame)
name_entry.grid(row=1, column=0)

type_of_customer_label = tkinter.Label(frame, text="Type of customer")
type_of_customer_label.grid(row=0, column=1)
type_of_customer_combobox = ttk.Combobox(frame, values=('First time', 'Regular'))
type_of_customer_combobox.grid(row=1, column=1)

phone_number_label = tkinter.Label(frame, text="Phone Number")
phone_number_label.grid(row=0, column=2)
phone_number_entry = tkinter.Entry(frame)
phone_number_entry.grid(row=1, column=2)

quantity_label = tkinter.Label(frame, text="Quantity")
quantity_label.grid(row=2, column=0)
quantity_spinbox = tkinter.Spinbox(frame, from_=1, to=250)
quantity_spinbox.grid(row=3, column=0)

item_prices = {
    "Bundle jelata 1": 20,
    "Bundle jelata 2": 25,
    "Bundle jelata 3": 30,
    "Bundle reguler 1": 40,
    "Bundle reguler 2": 50,
    "Bundle reguler 3": 60,
    "Bundle ratu 1": 75,
    "Bundle ratu 2": 95,
    "Bundle ratu 3": 125,
}

item_label = tkinter.Label(frame, text="Item")
item_label.grid(row=2, column=1)
item_combobox = ttk.Combobox(frame, values=list(item_prices.keys()))
item_combobox.grid(row=3, column=1)
item_combobox.bind("<<ComboboxSelected>>", update_price)

price_label_text = tkinter.Label(frame, text="Price")
price_label_text.grid(row=2, column=2)
price_label = tkinter.Label(frame, text="")
price_label.grid(row=3, column=2)

add_item_button = tkinter.Button(frame, text="Add item", command=lambda: (check_entries() and add_item(item_prices)))
add_item_button.grid(row=4, column=1, pady=5)

columns = ('quantity', 'item', 'price', 'total')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('quantity', text="Quantity")
tree.heading('item', text="Item")
tree.heading('price', text="Price")
tree.heading('total', text="Total")
tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

initial_total_label = tkinter.Label(frame, text="Initial Total")
initial_total_label.grid(row=6, column=1, sticky="news", padx=20, pady=10)
initial_total_entry = tkinter.Entry(frame)
initial_total_entry.grid(row=6, column=2, sticky="news", padx=20, pady=10)

tax_label = tkinter.Label(frame, text="Tax")
tax_label.grid(row=7, column=1, sticky="news", padx=20, pady=5)
tax_entry = tkinter.Entry(frame)
tax_entry.grid(row=7, column=2, sticky="news", padx=20, pady=5)

grand_total_label = tkinter.Label(frame, text="Grand Total")
grand_total_label.grid(row=9, column=1, sticky="news", padx=20, pady=5)
grand_total_entry = tkinter.Entry(frame)
grand_total_entry.grid(row=9, column=2, sticky="news", padx=20, pady=5)

save_invoice_button = tkinter.Button(frame, text="Generate Invoice")
save_invoice_button.grid(row=10, column=0, columnspan=3, sticky="news", pady=5, padx=20)
new_invoice_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_invoice_button.grid(row=11, column=0, columnspan=3, sticky="news", padx=20, pady=5)

window.mainloop()
