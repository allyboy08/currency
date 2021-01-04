from tkinter import  *
import requests

root=Tk()
root.title("Currency Convertor")
root.geometry("300x600")

class CurrencyConvertor():
    def __init__(self,url):
        self.response= requests.get(url).json()
        self.currency = self.response['rates']




root.mainloop()