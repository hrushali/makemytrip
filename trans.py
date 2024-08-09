from tkinter import Tk, Label, Entry, Button, StringVar, Scrollbar, Text, OptionMenu, END
import json
import random

class TranslationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.transactions = []
        self.allow = True

        self.balance = Label(master, text="Balance:")
        self.balance.grid(row=0, column=0, padx=10, pady=10)

        self.money_plus = Label(master, text="Income:")
        self.money_plus.grid(row=0, column=1, padx=10, pady=10)

        self.money_minus = Label(master, text="Expense:")
        self.money_minus.grid(row=0, column=2, padx=10, pady=10)

        self.list = Text(master, height=6, width=40, wrap='word')
        self.list.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.scrollbar = Scrollbar(master, command=self.list.yview)
        self.scrollbar.grid(row=2, column=4, sticky='nsew')

        self.list['yscrollcommand'] = self.scrollbar.set

        self.text = Entry(master)
        self.text.grid(row=3, column=0, padx=10, pady=10)

        self.amount = Entry(master)
        self.amount.grid(row=3, column=1, padx=10, pady=10)

        self.form = Button(master, text="Add Expense", command=self.add_transaction)
        self.form.grid(row=3, column=2, padx=10, pady=10)

        self.clear_button = Button(master, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=3, column=3, padx=10, pady=10)

        self.exit_button = Button(master, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=4, column=2, pady=10)

        self.load_transactions()

    def generate_id(self):
        return random.randint(1, 1000000000)

    def add_transaction(self):
        if self.text.get().strip() == '' or self.amount.get().strip() == '':
            print('Please add text and amount')
        else:
            transaction = {
                'id': self.generate_id(),
                'text': self.text.get(),
                'amount': float(self.amount.get())
            }

            self.transactions.append(transaction)
            self.add_transaction_dom(transaction)
            self.update_values()
            self.update_local_storage()
            self.text.delete(0, END)
            self.amount.delete(0, END)

    def add_transaction_dom(self, transaction):
        sign = "-" if transaction['amount'] < 0 else "+"
        item = f"{transaction['text']} {sign}{abs(transaction['amount'])}\n"
        self.list.insert(END, item)

    def update_values(self):
        amounts = [transaction['amount'] for transaction in self.transactions]
        total = round(sum(amounts), 2)
        income = round(sum(filter(lambda x: x > 0, amounts)), 2)
        expense = round(abs(sum(filter(lambda x: x < 0, amounts))), 2)

        self.balance.config(text=f"Balance: ${total}")
        self.money_plus.config(text=f"Income: ${income}")
        self.money_minus.config(text=f"Expense: ${expense}")

    def clear_fields(self):
        self.text.delete(0, END)
        self.amount.delete(0, END)
        self.allow = True

    def update_local_storage(self):
        with open('transactions.json', 'w') as file:
            json.dump(self.transactions, file)

    def load_transactions(self):
        try:
            with open('transactions.json', 'r') as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            pass

        for transaction in self.transactions:
            self.add_transaction_dom(transaction)

        self.update_values()

if __name__ == "__main__":
    root = Tk()
    app = TranslationApp(root)
    root.mainloop()
