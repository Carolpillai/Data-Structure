import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return " <- ".join(reversed(self.items)) if self.items else "Stack is empty"


class StackGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hello Kitty Stack GUI")
        master.geometry("400x400")
        master.configure(bg="#ffe6f0")

        self.stack = Stack()

        # Entry to push item
        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Buttons
        self.push_button = tk.Button(master, text="Push", command=self.push_item, bg="#ff99cc", font=("Arial", 12), width=20, height=2)
        self.push_button.pack(pady=5)

        self.pop_button = tk.Button(master, text="Pop", command=self.pop_item, bg="#ffccff", font=("Arial", 12), width=20, height=2)
        self.pop_button.pack(pady=5)

        self.peek_button = tk.Button(master, text="Peek", command=self.peek_item, bg="#ccffff", font=("Arial", 12), width=20, height=2)
        self.peek_button.pack(pady=5)

        self.empty_button = tk.Button(master, text="Is Empty?", command=self.check_empty, bg="#ffffcc", font=("Arial", 12), width=20, height=2)
        self.empty_button.pack(pady=5)

        self.size_button = tk.Button(master, text="Size", command=self.check_size, bg="#d5ccff", font=("Arial", 12), width=20, height=2)
        self.size_button.pack(pady=5)

        # Display Stack
        self.stack_label = tk.Label(master, text="Current Stack: Stack is empty", bg="#ffe6f0", font=("Arial", 12), wraplength=300, justify="center")
        self.stack_label.pack(pady=20)

    def update_display(self):
        self.stack_label.config(text=f"[Kuromi] Current Stack: {str(self.stack)}")

    def push_item(self):
        item = self.entry.get()
        if item:
            self.stack.push(item)
            messagebox.showinfo("Hello Kitty", f"[Hello Kitty] {item} has been pushed onto the stack.")
            self.entry.delete(0, tk.END)
            self.update_display()

    def pop_item(self):
        try:
            item = self.stack.pop()
            messagebox.showinfo("Badtz-Maru", f"[Badtz-Maru] {item} has been popped from the stack.")
            self.update_display()
        except IndexError as e:
            messagebox.showerror("Error", f"[Keroppi] {str(e)}")

    def peek_item(self):
        try:
            item = self.stack.peek()
            messagebox.showinfo("My Melody", f"[My Melody] Top item is: {item}")
        except IndexError as e:
            messagebox.showerror("Error", f"[Keroppi] {str(e)}")

    def check_empty(self):
        result = "Yes" if self.stack.is_empty() else "No"
        messagebox.showinfo("Kuromi", f"[Kuromi] Is the stack empty? {result}")

    def check_size(self):
        messagebox.showinfo("Cinnamoroll", f"[Cinnamoroll] Size of the stack: {self.stack.size()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()

