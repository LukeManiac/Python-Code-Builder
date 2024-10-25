import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from pyperclip import copy as set_clipboard

texts = {
    "English": [
        "Python Code Builder",
        "Select Language",
        "Auto Indent",
        "Indent Size:",
        "Add Line",
        "Blank Line",
        "Reorder Line",
        "Edit Line",
        "Delete Line",
        "Run Code",
        "Save Code",
        "Copy Code",
        "New Code",
        "Shift Indent Left",
        "Shift Indent Right",
        "Enter a line of code:",
        "Enter the index of the line to move",
        "Enter the new index for the line",
        "Invalid indices provided.",
        "Enter the index of the line to edit",
        "Enter the new line of code:",
        "Enter the index of the line to delete",
        "Enter the line number to shift left",
        "Enter the line number to shift right"
    ],
    "French": [
        "Python Code Builder",
        "Sélectionner la langue",
        "Auto-retrait",
        "Taille du retrait :",
        "Ajouter une ligne",
        "Ligne vide",
        "Réorganiser la ligne",
        "Modifier la ligne",
        "Supprimer la ligne",
        "Exécuter le code",
        "Enregistrer le code",
        "Copier le code",
        "Nouveau code",
        "Décaler le retrait vers la gauche",
        "Décaler le retrait vers la droite",
        "Entrer une ligne de code :",
        "Entrer l'index de la ligne à déplacer",
        "Entrer le nouvel index pour la ligne",
        "Index non valides fournis.",
        "Entrer l'index de la ligne à modifier",
        "Entrer la nouvelle ligne de code :",
        "Entrer l'index de la ligne à supprimer",
        "Entrer le numéro de ligne à décaler vers la gauche",
        "Entrer le numéro de ligne à décaler vers la droite"
    ],
    "German": [
        "Python Code Builder",
        "Sprache auswählen",
        "Automatischer Einzug",
        "Einzugsgröße:",
        "Zeile hinzufügen",
        "Leere Zeile",
        "Zeile neu anordnen",
        "Zeile bearbeiten",
        "Zeile löschen",
        "Code ausführen",
        "Code speichern",
        "Code kopieren",
        "Neuer Code",
        "Einzug nach links verschieben",
        "Einzug nach rechts verschieben",
        "Codezeile eingeben:",
        "Index der zu verschiebenden Zeile eingeben",
        "Neuen Index für die Zeile eingeben",
        "Ungültige Indizes angegeben.",
        "Index der zu bearbeitenden Zeile eingeben",
        "Neue Codezeile eingeben:",
        "Index der zu löschenden Zeile eingeben",
        "Zeilennummer eingeben, die nach links verschoben werden soll",
        "Zeilennummer eingeben, die nach rechts verschoben werden soll"
    ],
    "Spanish": [
        "Generador de código Python",
        "Seleccionar idioma",
        "Sangría automática",
        "Tamaño de sangría:",
        "Agregar línea",
        "Línea en blanco",
        "Reordenar línea",
        "Editar línea",
        "Eliminar línea",
        "Ejecutar código",
        "Guardar código",
        "Copiar código",
        "Nuevo código",
        "Desplazar sangría a la izquierda",
        "Desplazar sangría a la derecha",
        "Ingresar una línea de código:",
        "Ingresar el índice de la línea que se va a mover",
        "Ingresar el nuevo índice de la línea",
        "Se proporcionaron índices no válidos",
        "Ingresar el índice de la línea que se va a editar",
        "Ingresar la nueva línea de código:",
        "Ingresar el índice de la línea que se va a eliminar",
        "Ingresar el número de línea que se va a desplazar a la izquierda",
        "Ingresar el número de línea que se va a desplazar a la derecha"
    ],
    "Italian": [
        "Python Code Builder",
        "Seleziona lingua",
        "Auto Indent",
        "Dimensione rientro:",
        "Aggiungi riga",
        "Riga vuota",
        "Riordina riga",
        "Modifica riga",
        "Elimina riga",
        "Esegui codice",
        "Salva codice",
        "Copia codice",
        "Nuovo codice",
        "Sposta rientro a sinistra",
        "Sposta rientro a destra",
        "Inserisci una riga di codice:",
        "Inserisci l'indice della riga da spostare",
        "Inserisci il nuovo indice per la riga",
        "Indici forniti non validi.",
        "Inserisci l'indice della riga da modificare",
        "Inserisci la nuova riga di codice:",
        "Inserisci l'indice della riga da eliminare",
        "Inserisci il numero di riga da spostare a sinistra",
        "Inserisci il numero di riga da spostare a destra"
    ],
    "Dutch": [
        "Python Code Builder",
        "Selecteer taal",
        "Automatisch inspringen",
        "Inspringingsgrootte:",
        "Regel toevoegen",
        "Lege regel",
        "Regel opnieuw ordenen",
        "Regel bewerken",
        "Regel verwijderen",
        "Code uitvoeren",
        "Code opslaan",
        "Code kopiëren",
        "Nieuwe code",
        "Inspringing naar links verschuiven",
        "Inspringing naar rechts verschuiven",
        "Voer een regel code in:",
        "Voer de index in van de regel die u wilt verplaatsen",
        "Voer de nieuwe index voor de regel in",
        "Ongeldige indices opgegeven.",
        "Voer de index in van de regel die u wilt bewerken",
        "Voer de nieuwe regel code in:",
        "Voer de index in van de regel die u wilt verwijderen",
        "Voer het regelnummer in dat u naar links wilt verschuiven",
        "Voer het regelnummer in dat u naar rechts wilt verschuiven"
    ],
    "Portuguese": [
        "Python Code Builder",
        "Selecionar idioma",
        "Recuo automático",
        "Tamanho do recuo:",
        "Adicionar linha",
        "Linha em branco",
        "Reordenar linha",
        "Editar linha",
        "Excluir linha",
        "Executar código",
        "Salvar código",
        "Copiar código",
        "Novo código",
        "Deslocar recuo para a esquerda",
        "Deslocar recuo para a direita",
        "Digite uma linha de código:",
        "Digite o índice da linha a ser movida",
        "Digite o novo índice para a linha",
        "Índices inválidos fornecidos.",
        "Digite o índice da linha a ser editada",
        "Digite a nova linha de código:",
        "Digite o índice da linha a ser excluída",
        "Digite o número da linha a ser deslocada para a esquerda",
        "Digite o número da linha a ser deslocada para a direita"
    ],
    "Russian": [
        "Python Code Builder",
        "Выбрать язык",
        "Автоматический отступ",
        "Размер отступа:",
        "Добавить строку",
        "Пустая строка",
        "Изменить порядок строк",
        "Редактировать строку",
        "Удалить строку",
        "Запустить код",
        "Сохранить код",
        "Копировать код",
        "Новый код",
        "Сдвиг отступа влево",
        "Сдвиг отступа вправо",
        "Введите строку кода:",
        "Введите индекс строки для перемещения",
        "Введите новый индекс строки",
        "Предоставлены недопустимые индексы.",
        "Введите индекс строки для редактирования",
        "Введите новую строку кода:",
        "Введите индекс строки для удаления",
        "Введите номер строки для сдвига влево",
        "Введите номер строки для сдвига вправо"
    ],
    "Japanese": [
        "Python コード ビルダー",
        "言語の選択",
        "自動インデント",
        "インデント サイズ:",
        "行の追加",
        "空白行",
        "行の順序変更",
        "行の編集",
        "行の削除",
        "コードの実行",
        "コードを保存",
        "コードのコピー",
        "新しいコード",
        "インデントを左にシフト",
        "インデントを右にシフト",
        "コード行を入力:",
        "移動する行のインデックスを入力",
        "行の新しいインデックスを入力",
        "無効なインデックスが指定されました。",
        "編集する行のインデックスを入力",
        "新しいコード行を入力:",
        "削除する行のインデックスを入力",
        "左にシフトする行番号を入力",
        "右にシフトする行番号を入力"
    ],
    "Chinese (traditional)": [
        "Python 程式碼產生器",
        "選擇語言",
        "自動縮排",
        "縮排尺寸：",
        "新增線路",
        "空行",
        "再訂購線",
        "編輯行",
        "刪除行",
        "運行程式碼",
        "儲存程式碼",
        "複製程式碼",
        "新守則",
        "左移縮進",
        "右移縮進",
        "輸入一行程式碼：",
        "輸入要移動的行的索引",
        "輸入該行的新索引",
        "提供的索引無效。",
        "輸入要編輯的行的索引",
        "輸入新的程式碼行：",
        "輸入要刪除的行的索引",
        "輸入要左移的行號",
        "輸入要右移的行號"
    ],
    "Chinese (simplified)": [
        "Python 代码生成器",
        "选择语言",
        "自动缩进",
        "缩进大小：",
        "添加行",
        "空白行",
        "重新排序行",
        "编辑行",
        "删除行",
        "运行代码",
        "保存代码",
        "复制代码",
        "新代码",
        "左移缩进",
        "右移缩进",
        "输入一行代码：",
        "输入要移动的行的索引",
        "输入行的新索引",
        "提供的索引无效。",
        "输入要编辑的行的索引",
        "输入新代码行：",
        "输入要删除的行的索引",
        "输入要左移的行号",
        "输入要右移的行号"
    ],
    "Korean": [
        "Python 코드 빌더",
        "언어 선택",
        "자동 들여쓰기",
        "들여쓰기 크기:",
        "줄 추가",
        "빈 줄",
        "줄 재정렬",
        "줄 편집",
        "줄 삭제",
        "코드 실행",
        "코드 저장",
        "코드 복사",
        "새 코드",
        "왼쪽으로 들여쓰기",
        "오른쪽으로 들여쓰기",
        "코드 줄을 입력하세요:",
        "이동할 줄의 인덱스를 입력하세요",
        "줄의 새 인덱스를 입력하세요",
        "잘못된 인덱스가 제공되었습니다.",
        "편집할 줄의 인덱스를 입력하세요",
        "새 코드 줄을 입력하세요:",
        "삭제할 줄의 인덱스를 입력하세요",
        "왼쪽으로 이동할 줄 번호를 입력하세요",
        "오른쪽으로 이동할 줄 번호를 입력하세요"
    ]
}
widths = {
    "English":1000,
    "French":1440,
    "German":1380,
    "Spanish":1380,
    "Italian":1240,
    "Dutch":1500,
    "Portuguese":1380,
    "Russian":1420,
    "Japanese":1200,
    "Chinese (traditional)":850,
    "Chinese (simplified)":820,
    "Korean":960
}

class CodeLineManager:
    def __init__(self):
        self.code_lines = []
        self.indentation_level = 0  # To track current indentation level

    def add_line(self, line):
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
            new_indent = max(0, current_indent - indent_size)
            self.indentation_level = max(0, self.indentation_level - 1)
            self.code_lines[index] = self.indent_line(self.code_lines[index].lstrip(), new_indent)

    def set_indent_size(self, new_indent_size):
        for i in range(len(self.code_lines)):
            self.code_lines[i] = self.indent_line(self.code_lines[i].lstrip(), new_indent_size)

class LanguageMenu:
    def __init__(self):
        self.applanguage = None
        self.language_menu = tk.Tk()
        self.language_menu.title("Select Language")
        self.language_menu.resizable(False, False)
        self.language_menu.minsize(200, 100)
        self.language_menu.geometry("200x100")

        # Language dropdown menu
        self.languages = ["English", "French", "German", "Spanish", "Italian", "Dutch", "Portuguese", "Russian", "Japanese", "Chinese (traditional)", "Chinese (simplified)", "Korean"]

        self.selected_language = tk.StringVar(value=self.languages[0])
        self.language_dropdown = tk.OptionMenu(self.language_menu, self.selected_language, *self.languages, command=self.update_select_button)
        self.language_dropdown.pack(pady=10)

        # Select Language button
        self.select_button = tk.Button(self.language_menu, text="Select Language", command=self.set_language)
        self.select_button.pack(pady=10)

        self.language_menu.mainloop()

    def update_select_button(self, language):
        self.button_text = texts[language]
        self.select_button.configure(text=self.button_text[1])

    def set_language(self):
        self.applanguage = self.selected_language.get()
        self.language_menu.destroy()
        root = tk.Tk()
        root.minsize(widths[self.applanguage], 500)
        root.geometry(f"{widths[self.applanguage]}x500")
        app = CodeBuilderGUI(root, self.applanguage)
        root.mainloop()

class CodeBuilderGUI:
    def __init__(self, master, applanguage):
        self.master = master
        self.text_list = texts[applanguage]
        self.master.title(self.text_list[0])

        # Store the application language (you can use it later for UI text translations if needed)
        self.applanguage = applanguage

        self.line_manager = CodeLineManager()
        self.indent_size = 4
        self.saved = True
        self.current_file = None

        # Create a frame for the text area and line numbers
        self.frame = tk.Frame(master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Create a vertical scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure scrollbar
        self.scrollbar.config(command=self.on_scroll)

        # Create line numbers text widget
        self.line_numbers = tk.Text(self.frame, bg='lightgrey', state=tk.DISABLED, width=1, height=20)
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.line_numbers.bind("<Button-1>", self.prevent_selection)
        self.line_numbers.bind("<Key>", lambda e: "break")
        self.line_numbers.bind("<FocusIn>", lambda e: self.line_numbers.focus_set())

        # Prevent scrolling with mouse wheel/trackpad
        self.line_numbers.bind("<MouseWheel>", lambda e: "break")  # For Windows
        self.line_numbers.bind("<Button-4>", lambda e: "break")    # For Linux
        self.line_numbers.bind("<Button-5>", lambda e: "break")    # For Linux

        # Create text area
        self.text_area = tk.Text(self.frame, wrap=tk.WORD, height=20, width=60, yscrollcommand=self.scrollbar.set, state=tk.NORMAL)
        self.text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.text_area.bind("<Button-1>", self.prevent_selection)
        self.text_area.bind("<Key>", lambda e: "break")
        self.text_area.bind("<FocusIn>", lambda e: self.text_area.focus_set())

        # Prevent scrolling with mouse wheel/trackpad
        self.text_area.bind("<MouseWheel>", lambda e: "break")  # For Windows
        self.text_area.bind("<Button-4>", lambda e: "break")    # For Linux
        self.text_area.bind("<Button-5>", lambda e: "break")    # For Linux

        # Button frame
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10, side=tk.BOTTOM)

        self.auto_indent_var = tk.BooleanVar(value=True)
        self.auto_indent_check = tk.Checkbutton(self.button_frame, text=self.text_list[2], variable=self.auto_indent_var)
        self.auto_indent_check.pack(side=tk.TOP)

        self.indent_size_label = tk.Label(self.button_frame, text=self.text_list[3])
        self.indent_size_label.pack(side=tk.LEFT, padx=(5, 0))

        self.indent_size_entry = tk.Entry(self.button_frame, width=5)
        self.indent_size_entry.pack(side=tk.LEFT)
        self.indent_size_entry.insert(0, str(self.indent_size))

        self.add_button = tk.Button(self.button_frame, text=self.text_list[4], command=self.add_line)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.blank_line_button = tk.Button(self.button_frame, text=self.text_list[5], command=self.add_blank_line)
        self.blank_line_button.pack(side=tk.LEFT, padx=5)

        self.rearrange_button = tk.Button(self.button_frame, text=self.text_list[6], command=self.rearrange_line)
        self.rearrange_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.button_frame, text=self.text_list[7], command=self.edit_line)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text=self.text_list[8], command=self.delete_line)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.run_button = tk.Button(self.button_frame, text=self.text_list[9], command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text=self.text_list[10], command=self.save_code)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.copy_button = tk.Button(self.button_frame, text=self.text_list[11], command=self.copy_code)
        self.copy_button.pack(side=tk.LEFT, padx=5)

        self.new_button = tk.Button(self.button_frame, text=self.text_list[12], command=self.new_code)
        self.new_button.pack(side=tk.LEFT, padx=5)

        self.shift_indent_left_button = tk.Button(self.button_frame, text=self.text_list[13], command=self.shift_indent_left)
        self.shift_indent_left_button.pack(side=tk.LEFT, padx=5)

        self.shift_indent_right_button = tk.Button(self.button_frame, text=self.text_list[14], command=self.shift_indent_right)
        self.shift_indent_right_button.pack(side=tk.LEFT, padx=5)

        self.text_area.bind("<KeyRelease>", self.update_line_numbers)
        self.text_area.bind("<Configure>", self.update_line_numbers)

        self.update_line_numbers()

    def prevent_selection(self, event):
        return "break"

    def add_line(self):
        line = simpledialog.askstring("Input", self.text_list[15])
        if line:
            self.line_manager.add_line(line)
            self.update_text_area()
            self.saved = False

    def add_blank_line(self):
        self.line_manager.add_blank_line()
        self.update_text_area()
        self.saved = False

    def rearrange_line(self):
        try:
            index = simpledialog.askinteger("Input", f"{self.text_list[16]} (1-{len(self.line_manager.code_lines)}):") - 1
            try:
                new_index = simpledialog.askinteger("Input", f"{self.text_list[17]} (1-{len(self.line_manager.code_lines)}):") - 1
                if index is not None and new_index is not None:
                    try:
                        self.line_manager.rearrange_line(index, new_index)
                        self.update_text_area()
                        self.saved = False
                    except IndexError:
                        messagebox.showerror("Error", self.text_list[18])
            except:
                pass
        except:
            pass

    def edit_line(self):
        try:
            index = simpledialog.askinteger("Input", f"Enter the index of the line to edit (1-{len(self.line_manager.code_lines)}):") - 1
            if index is not None:
                new_line = simpledialog.askstring("Input", self.text_list[20], initialvalue=self.line_manager.code_lines[index])
                if new_line:
                    self.line_manager.edit_line(index, new_line)
                    self.update_text_area()
                    self.saved = False
        except:
            pass

    def delete_line(self):
        try:
            index = simpledialog.askinteger("Input", f"{self.text_list[21]} (1-{len(self.line_manager.code_lines)}):") - 1
            if index is not None:
                try:
                    self.line_manager.delete_line(index)
                    self.update_text_area()
                    self.saved = False
                except IndexError:
                    messagebox.showerror("Error", self.text_list[18])
        except:
            pass

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

    def shift_indent_left(self):
        try:
            index = simpledialog.askinteger("Input", f"{self.text_list[22]} (1-{len(self.line_manager.code_lines)}):") - 1
            if index is not None:
                self.line_manager.decrease_indent(index, self.indent_size)
                self.update_text_area()
        except:
            pass

    def shift_indent_right(self):
        try:
            index = simpledialog.askinteger("Input", f"{self.text_list[23]} (1-{len(self.line_manager.code_lines)}):") - 1
            if index is not None:
                self.line_manager.increase_indent(index, self.indent_size)
                self.update_text_area()
        except:
            pass

    def update_text_area(self):
        self.text_area.configure(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.line_manager.get_code())
        self.text_area.configure(state=tk.DISABLED)
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        self.line_numbers.configure(state=tk.NORMAL)
        self.line_numbers.delete(1.0, tk.END)

        max_digits = len(str(len(self.line_manager.code_lines)))

        for i, _ in enumerate(self.line_manager.code_lines, start=1):
            self.line_numbers.insert(tk.END, f"{i:>{max_digits}}\n")

        self.line_numbers.configure(state=tk.DISABLED, width=max_digits)

    def on_scroll(self, *args):
        self.text_area.yview(*args)
        self.line_numbers.yview(*args)

if __name__ == "__main__":
    LanguageMenu()
