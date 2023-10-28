import requests
import tkinter as tk
from tkinter import ttk
def convertCurrency(fromCurrency,to_currency,amount):
    if len(fromCurrency) != 3 or len(to_currency) != 3:
        return "Invalid currency \ncode(s)"
    fromCurrency,to_currency = fromCurrency.upper(),to_currency.upper()
    
    if not amount.isnumeric() or int(amount) < 0:
        return "Invalid amount"
    amount = float(amount)

    try:
        response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={fromCurrency}&to={to_currency}")
        # Website doesn't need an api key and is free to use but has limited currencies
        #print(f"\n{response.status_code}\n) # 200 means success 
        data = response.json()
        #print(f"\n{data}\n) 
        amount = int(amount) if amount.is_integer() else amount # if amount is an integer, convert to int, else leave as float
        convertedAmount = data['rates'][to_currency] # get the conversion rate from the data (print data to see dictionary structure)
        #return f"{amount} {fromCurrency} is equal to {convertedAmount} {to_currency}"
    except:
        return "API error or \ninvalid currency \ncode(s)"
    return f"{convertedAmount} {to_currency}"

class App():
    def __init__(self):
        self.root = tk.Tk() # create the root window which will hold everything
        self.root.title("Currency Converter")
        self.root.geometry("350x250")
        self.mainframe = tk.Frame(self.root) 
        self.mainframe.pack(fill='both',expand = True)

        self.text = ttk.Label(self.mainframe,text = "Currency Converter",font=("Helvetica", 22))
        self.text.grid(row=0,column=0)

        self.baseLabel = ttk.Label(self.mainframe,text="From")
        self.baseLabel.grid(row=1,column=0)
        self.base = ttk.Entry(self.mainframe)
        self.base.grid(row=2,column=0,pady=10)# sticky="nsew"

        self.toLabel = ttk.Label(self.mainframe,text="To")
        self.toLabel.grid(row=3,column=0)
        self.newValue = ttk.Entry(self.mainframe)
        self.newValue.grid(row=4,column=0)#,pady=10)

        self.amountLabel = ttk.Label(self.mainframe,text="Amount")
        self.amountLabel.grid(row=5,column=0)
        self.amount = ttk.Entry(self.mainframe)
        self.amount.grid(row=6,column=0)

        self.convertButton = ttk.Button(self.mainframe,text="Convert",command=self.returnValue)
        self.convertButton.grid(row=8,column=0,pady=10)

        self.resultLabel = ttk.Label(self.mainframe,text="0")
        self.resultLabel.grid(row=4,column=1)

        self.root.mainloop() # start the mainloop (opens the window)
        return
    
    def returnValue(self):
        self.resultLabel.config(text= convertCurrency(self.base.get(),self.newValue.get(),self.amount.get()))
        return
        

if __name__ == "__main__":
    App()