import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
	self.history = []

        self.history_frame = tk.LabelFrame(root, text="历史记录", font=("Arial", 12))
        self.history_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.history_list = tk.Listbox(
            self.history_frame, 
            height=5, 
            font=("Arial", 12),
            selectbackground="#a6a6a6"
        )
        self.history_list.pack(fill="both", expand=True, padx=5, pady=5)
        self.history_list.bind("<Double-Button-1>", self.use_history)

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/', '⌫'],
            ['4', '5', '6', '*', 'C'],
            ['1', '2', '3', '-', 'HIST'],
            ['0', '.', '(', '+', ')'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == 'HIST':
            self.show_history()
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.history.append(f"{self.expression} = {result}")
                self.history_list.insert(0, f"{self.expression} = {result}")
                self.expression = result
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
    def use_history(self, event):
        selected = self.history_list.get(self.history_list.curselection())
        expr = selected.split(' = ')[0]
        self.expression = expr
        self.update_display()
    
    def show_history(self):
        if not self.history:
            messagebox.showinfo("사록", "사록 없음")
        else:
            messagebox.showinfo(
                "사록", 
                "\n".join(f"{i+1}. {item}" for i, item in enumerate(self.history)))
