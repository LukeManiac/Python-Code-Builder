import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from subprocess import call as call_command
from platform import system as detect_os
from pyperclip import copy as set_clipboard

class CodeLineManager:
    def __init__(self):
        self.code_lines = []
        self.indentation_level = 0  # To track current indentation level

    def add_line(self, line):
        # Automatically indent if needed
        if self.code_lines and self.code_lines[-1].strip().endswith(":"):
            self.indentation_level += 1

        indented_line = self.indent_line(line, self.indentation_level * 4)
        self.code_lines.append(indented_line)

        if any(i in line for i in ["pass", "continue", "break", "return"]):
            self.indentation_level = max(0, self.indentation_level - 1)

    def add_blank_line(self):
        self.code_lines.append("")

    def rearrange_line(self, index, new_index):
        if 0 <= index < len(self.code_lines) and 0 <= new_index < len(self.code_lines):
            self.code_lines.insert(new_index, self.code_lines.pop(index))

    def edit_line(self, index, new_line):
        if 0 <= index < len(self.code_lines):
            self.code_lines[index] = new_line

    def delete_line(self, index):
        if 0 <= index < len(self.code_lines):
            self.code_lines.pop(index)

    def get_code(self):
        return "\n".join(self.code_lines)

    def indent_line(self, line, indent_level):
        return ' ' * indent_level + line

    def increase_indent(self, index, indent_size=4):
        if 0 <= index < len(self.code_lines):
            self.code_lines[index] = self.indent_line(self.code_lines[index], indent_size)
            self.indentation_level += 1

    def decrease_indent(self, index, indent_size=4):
        if 0 <= index < len(self.code_lines):
            current_indent = len(self.code_lines[index]) - len(self.code_lines[index].lstrip())
            new_indent = max(0, current_indent - indent_size)  # Prevent negative indent
            self.indentation_level = max(0, self.indentation_level - 1)
            self.code_lines[index] = self.indent_line(self.code_lines[index].lstrip(), new_indent)

    def set_indent_size(self, new_indent_size):
        for i in range(len(self.code_lines)):
            self.code_lines[i] = self.indent_line(self.code_lines[i].lstrip(), new_indent_size)


class CodeBuilderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python Code Builder")
        master.minsize(1000, 500)

        self.line_manager = CodeLineManager()
        self.indent_size = 4  # Default indent size
        self.saved = True
        self.current_file = None

        self.frame = tk.Frame(master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.text_area = tk.Text(self.frame, wrap=tk.WORD, height=20, width=60, state=tk.DISABLED)
        self.text_area.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.text_area.bind("<Button-1>", self.prevent_selection)
        self.text_area.bind("<Key>", lambda e: "break")
        self.text_area.bind("<FocusIn>", lambda e: self.text_area.focus_set())

        self.line_numbers = tk.Text(self.frame, bg='lightgrey', state=tk.DISABLED, width=1)  # Set a default width
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.line_numbers.bind("<Button-1>", self.prevent_selection)
        self.line_numbers.bind("<Key>", lambda e: "break")
        self.line_numbers.bind("<FocusIn>", lambda e: self.line_numbers.focus_set())

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10, side=tk.BOTTOM)

        self.auto_indent_var = tk.BooleanVar(value=True)
        self.auto_indent_check = tk.Checkbutton(self.button_frame, text="Auto Indent", variable=self.auto_indent_var)
        self.auto_indent_check.pack(side=tk.TOP)

        self.indent_size_label = tk.Label(self.button_frame, text="Indent Size:")
        self.indent_size_label.pack(side=tk.LEFT, padx=(5, 0))

        self.indent_size_entry = tk.Entry(self.button_frame, width=5)
        self.indent_size_entry.pack(side=tk.LEFT)
        self.indent_size_entry.insert(0, str(self.indent_size))

        self.add_button = tk.Button(self.button_frame, text="Add Line", command=self.add_line)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.blank_line_button = tk.Button(self.button_frame, text="Add Blank Line", command=self.add_blank_line)
        self.blank_line_button.pack(side=tk.LEFT, padx=5)

        self.rearrange_button = tk.Button(self.button_frame, text="Rearrange Line", command=self.rearrange_line)
        self.rearrange_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Line", command=self.edit_line)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Line", command=self.delete_line)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.run_button = tk.Button(self.button_frame, text="Run Code", command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save Code", command=self.save_code)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.copy_button = tk.Button(self.button_frame, text="Copy Code", command=self.copy_code)
        self.copy_button.pack(side=tk.LEFT, padx=5)

        self.new_button = tk.Button(self.button_frame, text="New Code", command=self.new_code)
        self.new_button.pack(side=tk.LEFT, padx=5)

        self.shift_indent_left_button = tk.Button(self.button_frame, text="Shift Indent Left", command=self.shift_indent_left)
        self.shift_indent_left_button.pack(side=tk.LEFT, padx=5)

        self.shift_indent_right_button = tk.Button(self.button_frame, text="Shift Indent Right", command=self.shift_indent_right)
        self.shift_indent_right_button.pack(side=tk.LEFT, padx=5)

        self.text_area.bind("<KeyRelease>", self.update_line_numbers)
        self.text_area.bind("<Configure>", self.update_line_numbers)

        self.update_line_numbers()

    def prevent_selection(self, event):
        return "break"

    def add_line(self):
        line = simpledialog.askstring("Input", "Enter a line of code:")
        if line:
            self.line_manager.add_line(line)
            self.update_text_area()
            self.saved = False

    def add_blank_line(self):
        self.line_manager.add_blank_line()
        self.update_text_area()
        self.saved = False

    def rearrange_line(self):
        index = simpledialog.askinteger("Input", "Enter the index of the line to move (1-based):") - 1
        new_index = simpledialog.askinteger("Input", "Enter the new index for the line (1-based):") - 1
        if index is not None and new_index is not None:
            try:
                self.line_manager.rearrange_line(index, new_index)
                self.update_text_area()
                self.saved = False
            except IndexError:
                messagebox.showerror("Error", "Invalid indices provided.")

    def edit_line(self):
        index = simpledialog.askinteger("Input", "Enter the index of the line to edit (1-based):") - 1
        if index is not None:
            new_line = simpledialog.askstring("Input", "Enter the new line of code:", initialvalue=self.line_manager.code_lines[index])
            if new_line:
                self.line_manager.edit_line(index, new_line)
                self.update_text_area()
                self.saved = False

    def delete_line(self):
        index = simpledialog.askinteger("Input", "Enter the index of the line to delete (1-based):") - 1
        if index is not None:
            try:
                self.line_manager.delete_line(index)
                self.update_text_area()
                self.saved = False
            except IndexError:
                messagebox.showerror("Error", "Invalid index provided.")

    def run_code(self):
        code = self.line_manager.get_code()
        try:
            exec(code)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_code(self):
        if self.current_file is None:
            file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py, *.pyw, *.pyi"), ("Text files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                self.current_file = file_path
        else:
            file_path = self.current_file

        try:
            with open(file_path, 'w') as file:
                file.write(self.line_manager.get_code())

            self.saved = True
        except FileNotFoundError:
            pass

    def copy_code(self):
        set_clipboard(self.line_manager.get_code())
        print("Copied code to clipboard!")

    def new_code(self):
        self.line_manager.code_lines.clear()
        self.update_text_area()

    def shift_indent_right(self):
        index = simpledialog.askinteger("Input", "Enter the line number to shift right (1-based):") - 1
        if index is not None:
            self.line_manager.increase_indent(index, self.indent_size)
            self.update_text_area()

    def shift_indent_left(self):
        index = simpledialog.askinteger("Input", "Enter the line number to shift left (1-based):") - 1
        if index is not None:
            self.line_manager.decrease_indent(index, self.indent_size)
            self.update_text_area()

    def update_text_area(self):
        self.text_area.configure(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.line_manager.get_code())
        self.text_area.configure(state=tk.DISABLED)
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        self.line_numbers.configure(state=tk.NORMAL)
        self.line_numbers.delete(1.0, tk.END)

        # Calculate the maximum number of digits for line numbers
        max_digits = len(str(len(self.line_manager.code_lines)))

        for i, _ in enumerate(self.line_manager.code_lines, start=1):
            self.line_numbers.insert(tk.END, f"{i:>{max_digits}}\n")  # Right-align line numbers

        self.line_numbers.configure(state=tk.DISABLED, width=max_digits)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeBuilderGUI(root)
    root.mainloop()
