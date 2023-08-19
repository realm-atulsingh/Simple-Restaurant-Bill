import tkinter as tk
from tkinter import messagebox


class RestaurantBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanpur Restaurant")
        
        self.menu = {
            "Burger": 5.0,
            "Pizza": 8.0,
            "Pasta": 7.0,
            "Salad": 4.0,
            "Soda": 1.5,
        }
        
        self.order = {}
        self.total_price = tk.DoubleVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(side="left", padx=10, pady=10)
        
        self.order_frame = tk.Frame(self.root)
        self.order_frame.pack(side="right", padx=10, pady=10)
        
        self.total_frame = tk.Frame(self.root)
        self.total_frame.pack(side="bottom", padx=10, pady=10)
        
        self.total_label = tk.Label(self.total_frame, text="Total:")
        self.total_label.pack(side="left")
        
        self.total_amount_label = tk.Label(self.total_frame, textvariable=self.total_price)
        self.total_amount_label.pack(side="left")
        
        for item in self.menu:
            button = tk.Button(self.menu_frame, text=f"{item} (${self.menu[item]:.2f})", command=lambda i=item: self.add_to_order(i))
            button.pack(fill="x", padx=5, pady=5)
        
        self.order_label = tk.Label(self.order_frame, text="Your Order:")
        self.order_label.pack()
        
        self.submit_button = tk.Button(self.order_frame, text="Submit Order", command=self.submit_order)
        self.submit_button.pack(pady=10)
        
    def add_to_order(self, item):
        if item in self.order:
            self.order[item] += 1
        else:
            self.order[item] = 1
        
        messagebox.showinfo("Added to Order", f"{item} added to your order!")
    
    def submit_order(self):
        if not self.order:
            messagebox.showwarning("Empty Order", "Your order is empty!")
            return
        
        total = 0
        order_summary = ""
        
        for item, quantity in self.order.items():
            price = self.menu[item]
            total += price * quantity
            order_summary += f"{item} x{quantity} = ${price * quantity:.2f}\n"
        
        order_summary += "\nTotal: ${:.2f}".format(total)
        
        self.total_price.set(total)
        self.order_label.config(text="Your Order:")
        
        messagebox.showinfo("Order Summary", order_summary)
        
        self.order = {}  # Clear the order
        
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantBillingSystem(root)
    root.mainloop()
