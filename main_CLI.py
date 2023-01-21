from trie import *
import keyboard


def ConvertListToString(myList):
    return "    ".join(myList)


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

print(" ")
key = input("key: ")
print("Click tab !!!")

while True:
    if keyboard.is_pressed("tab"):
        print(" ")
        y = 0
        while y <= len(t.autocomplete(key)):
            print(ConvertListToString(t.autocomplete(key)[y:y+3]))
            y += 3
        break

print(" ")
