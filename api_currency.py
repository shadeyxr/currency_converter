import requests
import tkinter as tk
from tkinter import messagebox

BASE_URL = 'http://api.exchangerate.host/convert'
API_KEY = 'dd7b5794cde5da51661a3dd60996b9a1'

def exchange_currencies():
    value = value_entry.get()
    response = requests.get(BASE_URL,params={'access_key':API_KEY, 'from':selected_option_from.get(),'to':selected_option_to.get(),'amount':value})
    result = response.json()
    if response.status_code == 200:
        messagebox.showinfo('result', message=(result['result'],selected_option_to.get()))

currency_request= requests.get('https://api.exchangerate.host/list', params={'access_key':API_KEY, })
currency_abreviations = currency_request.json()
options = []

for i in currency_abreviations['currencies']:
    options.append(i)




root = tk.Tk()
root.title('Exchange rate conversion')
root.geometry('300x200')


selected_option_from = tk.StringVar(value=options[0])
selected_option_to = tk.StringVar(value=options[0])

wrapper = tk.Frame(root)
wrapper.pack(expand=True,fill='both')


container = tk.Frame(wrapper)
container.place(relx=0.5,rely=0.5,anchor='center')


tk.Label(container, text="From:").grid(row=0, column=0,padx=5,pady=5)
dropdown = tk.OptionMenu(container,selected_option_from, *options)
dropdown.grid(row=1,column=0,padx=5,pady=5)

tk.Label(container, text="To:").grid(row=0,column=1,padx=5,pady=5)
dropdown = tk.OptionMenu(container,selected_option_to, *options)
dropdown.grid(row=1,column=1,padx=5,pady=5)

tk.Label(container, text="Enter value:").grid(row=2, column=0, padx=5, pady=5,columnspan=2)
value_entry = tk.Entry(container)
value_entry.grid(row=3, column=0, padx=10, pady=5,columnspan=2)

tk.Button(container, text='Exchange', command=exchange_currencies).grid(row=4, column=0,columnspan=2, pady=10)

root.mainloop()

