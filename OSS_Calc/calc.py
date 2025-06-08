import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.history = []

        self.history_frame = tk.LabelFrame(root, text="사록", font=("Arial", 12))
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
            ['sin', 'cos', 'tan', '⌫', 'C'],
            ['π', 'e', '^', '√', 'HIST'],
            ['7', '8', '9', '/', '('],
            ['4', '5', '6', '*', ')'],
            ['1', '2', '3', '-', '='],
            ['0', '.', 'x²', '+', 'log'],
            [ 'DEC→BIN']
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
                
    def show_dec2bin(self):
        converter = tk.Toplevel(self.root)
        converter.title("10진수에서 2진수로")
        converter.geometry("300x200")
        
        self.converter_window = converter

        tk.Label(converter, text="10진수 정수를 입력하세요:").pack(pady=5)
        self.dec_input = tk.Entry(converter, font=("Arial", 14))
        self.dec_input.pack(fill="x", padx=20)

        convert_btn = tk.Button(
            converter,
            text="변환",
            command=self.convert_dec2bin,
            height=1,
            width=10
        )
        convert_btn.pack(pady=10)

        self.bin_result = tk.Label(converter, text="", font=("Arial", 14), fg="blue")
        self.bin_result.pack()

        close_btn = tk.Button(
            converter,
            text="닫다",
            command=converter.destroy,
            height=1,
            width=10
        )
        close_btn.pack(pady=5)

    def convert_dec2bin(self):
        try:
            dec_num = int(self.dec_input.get())
            bin_str = bin(dec_num)[2:]
            
            self.bin_result.config(text=f"2진수: {bin_str}")
            
            self.expression = bin_str
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
            
        except ValueError:
            self.bin_result.config(text="올바른 정수를 입력하십시오！", fg="red")






  
    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == 'HIST':
            self.show_history()
        elif char == '^':
            self.expression += '**'
        elif char == '√':
            self.expression += 'math.sqrt('
        elif char == 'sin':
            self.expression += 'math.sin(math.radians('
        elif char == 'cos':
            self.expression += 'math.cos(math.radians('
        elif char == 'tan':
            self.expression += 'math.tan(math.radians('
        elif char == 'π':
            self.expression += str(math.pi)
        elif char == 'e':
            self.expression += str(math.e)
        elif char == 'x²':
            self.expression += '**2'
        elif char == 'log':
            self.expression += 'math.log10('
        elif char == 'DEC→BIN':
            self.show_dec2bin()
        elif char == '=':
            try:
                result = str(eval(self.expression, {'__builtins__': None}, {'math': math}))
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()