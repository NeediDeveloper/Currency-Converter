import requests
import tkinter as tk
from tkinter import ttk

BASE_URL = "https://openexchangerates.org/api/latest.json"
API_KEY = "3cfa82aabe004459b9bd1e6a2125dcba"# Replace with yuor API key
BASE_CURRENCY = "USD"

def Fetch_Exchange_Rates(base_currency=BASE_CURRENCY):
    url = f"{BASE_URL}?app_id={API_KEY}&base{BASE_CURRENCY}"
    response = requests.get(url)
    Data = response.json()
    return Data["rates"]

def Currency_Converter(Amount, From_Currency, To_Currency, rates):
    From_Rate = rates.get(From_Currency)
    To_Rate = rates.get(To_Currency)
    converted_amount = (Amount / From_Rate ) * To_Rate
    return converted_amount
    
def Convert():
    try:
        Amount = float(AmountEntry.get())
        From_Currency = FromCombo.get()
        To_Currency = ToCombo.get()
        
        Converted = Currency_Converter(Amount, From_Currency, To_Currency, Rates)
        ResultLabel.config(text=f"{Amount} {From_Currency} is equals to {Converted:.2f} {To_Currency}")
    except:
        ResultLabel.config(text="Please Enter a Valid Amount")

Rates = Fetch_Exchange_Rates()
CurrencyOptions = sorted(Rates.keys())

window = tk.Tk()
window.geometry("330x320")
window.title("Currency Converter")
window.configure(bg="#2b2b2b")


FirtsLabel = tk.Label(window, text="Currency converter", fg="#F3F3F3", bg="#2b2b2b", font=("STENCIL",20))
FirtsLabel.place(x=15, y=15)

AmountLabel = tk.Label(window, text="Amount", fg="#F3F3F3", bg="#2b2b2b", font=("Century",17))
AmountLabel.place(x=20, y=70)

AmountEntry = tk.Entry(window, fg="#F3F3F3", bg="#363636", font=("Century",12))
AmountEntry.place(height=25, width=150, x=160, y=74)

FromLabel = tk.Label(window, text="From Currency", fg="#F3F3F3", bg="#2b2b2b", font=("Century",14))
FromLabel.place(x=20, y=130)

FromCombo = ttk.Combobox(window, values=CurrencyOptions, state="readonly")
FromCombo.place(height=25, width=110, x=180, y=134)
FromCombo.set(BASE_CURRENCY)

ToLabel = tk.Label(window, text="To Currency", fg="#F3F3F3", bg="#2b2b2b", font=("Century",14))
ToLabel.place(x=20, y=170)

ToCombo = ttk.Combobox(window, values=CurrencyOptions , state="readonly")
ToCombo.place(height=25, width=110, x=180, y=174)
ToCombo.set("PKR")

ConvertButton = tk.Button(window, text="Convert", bg="#383838", fg="#F3F3F3", command=Convert, font=("Century",13), activebackground="#1a1a1a", relief="raised")
ConvertButton.place(height=30, width=120, x=100, y=230)

ResultLabel = tk.Label(window, text="", fg="#F3F3F3", bg="#2b2b2b", font=("Century",10))
ResultLabel.place(x=80, y=280)

window.mainloop()