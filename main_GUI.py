from trie import *
from tkinter import *
from tkinter import ttk


def Search():
    t.autocomplete(Search_Entry.get())

    Search_Combo = ttk.Combobox(window, values=t.autocomplete(Search_Entry.get()))
    Search_Combo.set(Search_Entry.get())
    Search_Combo.pack()


window = Tk()
window.title("Trie")
window.geometry("400x250")

t = Trie()

t.insert("apple")
t.insert("apples")
t.insert("applered")

t.insert("book")
t.insert("bookstore")
t.insert("bookshelf")
t.insert("bookworm")
t.insert("books")
t.insert("booking")
t.insert("booker")

Search_Entry = Entry(window)
Search_Entry.pack()

Search_Btn = Button(window, text="Search", command=Search)
Search_Btn.pack()

window.mainloop()
