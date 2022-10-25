from parser import downloading, autorisation
#from parser import naming_moving
from tkinter import *

def clicked():
        quantity = int(number.get())
        url = 'https://www.pinterest.com/'

        try:
            autorisation(url=url)

        except:
            print("Ошибка в процессе авторизации")

        downloading(index=quantity, quantity=0)


#       except:
#            naming_moving()

#        try:
#            naming_moving()

#        except:
#            print("Ошибка в процессе именования или перемещения")



window = Tk()
window.title("PaPin")
window.resizable(False, False)
window.geometry("450x100+300+300")

lbl = Label(window, text="Изображений скачать: ", font=("Sylfaen", 20)).grid(column=0, row=0)

lbl2 = Label(window, text=f"Загрузилось %", font=("Sylfaen", 15)).grid(column=1, row=1)

btn = Button(window, text="----------------  Начать  ----------------", font=("Sylfaen", 10), height=1, width=33, command=clicked).grid(column=0, row=1)

number = IntVar()

entr = Entry(window, textvariable=number).grid(column=1, row=0)

window.mainloop()
