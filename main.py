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
        "Enter the line number to shift right",
        "Copied to clipboard!",
        "Paste Code",
        "Clipboard is empty. Nothing to paste.",
        "Failed to access clipboard."
    ],
    "French": [
        "Générateur de code Python",
        "Sélectionner la langue",
        "Indentation automatique",
        "Taille de l'indentation :",
        "Ajouter une ligne",
        "Ligne vide",
        "Réorganiser la ligne",
        "Modifier la ligne",
        "Supprimer la ligne",
        "Exécuter le code",
        "Enregistrer le code",
        "Copier le code",
        "Nouveau code",
        "Diminuer l'indentation",
        "Augmenter l'indentation",
        "Entrez une ligne de code :",
        "Entrez l'index de la ligne à déplacer",
        "Entrez le nouvel index de la ligne",
        "Indices fournis non valides.",
        "Entrez l'index de la ligne à modifier",
        "Entrez la nouvelle ligne de code :",
        "Entrez l'index de la ligne à supprimer",
        "Entrez le numéro de la ligne à décaler à gauche",
        "Entrez le numéro de la ligne à décaler à droite",
        "Copié dans le presse-papiers !",
        "Coller le code",
        "Presse-papiers vide. Rien à coller.",
        "Échec d'accès au presse-papiers."
    ],
    "German": [
        "Python-Code-Generator",
        "Sprache auswählen",
        "Automatische Einrückung",
        "Einrückungsgröße:",
        "Zeile hinzufügen",
        "Leere Zeile",
        "Zeile neu anordnen",
        "Zeile bearbeiten",
        "Zeile löschen",
        "Code ausführen",
        "Code speichern",
        "Code kopieren",
        "Neuer Code",
        "Einrückung nach links verschieben",
        "Einrückung nach rechts verschieben",
        "Geben Sie eine Codezeile ein:",
        "Geben Sie den Index der zu verschiebenden Zeile ein",
        "Geben Sie den neuen Index für die Zeile ein",
        "Ungültige Indizes angegeben.",
        "Geben Sie den Index der zu bearbeitenden Zeile ein",
        "Geben Sie die neue Codezeile ein:",
        "Geben Sie den Index der zu löschenden Zeile ein",
        "Geben Sie die Zeilennummer zum Verschieben nach links ein",
        "Geben Sie die Zeilennummer zum Verschieben nach rechts ein",
        "In die Zwischenablage kopiert!",
        "Code einfügen",
        "Zwischenablage ist leer. Nichts zum Einfügen.",
        "Fehler beim Zugriff auf die Zwischenablage."
    ],
    "Spanish": [
        "Generador de código Python",
        "Seleccionar idioma",
        "Indentación automática",
        "Tamaño de la indentación:",
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
        "Introduce una línea de código:",
        "Introduce el índice de la línea a mover",
        "Introduce el nuevo índice para la línea",
        "Índices no válidos.",
        "Introduce el índice de la línea a editar",
        "Introduce la nueva línea de código:",
        "Introduce el índice de la línea a eliminar",
        "Introduce el número de línea para desplazar a la izquierda",
        "Introduce el número de línea para desplazar a la derecha",
        "¡Copiado al portapapeles!",
        "Pegar código",
        "Portapapeles vacío. Nada que pegar.",
        "Error al acceder al portapapeles."
    ],
    "Italian": [
        "Generatore di codice Python",
        "Seleziona lingua",
        "Indentazione automatica",
        "Dimensione dell'indentazione:",
        "Aggiungi riga",
        "Riga vuota",
        "Riordina riga",
        "Modifica riga",
        "Elimina riga",
        "Esegui codice",
        "Salva codice",
        "Copia codice",
        "Nuovo codice",
        "Riduci indentazione",
        "Aumenta indentazione",
        "Inserisci una riga di codice:",
        "Inserisci l'indice della riga da spostare",
        "Inserisci il nuovo indice per la riga",
        "Indici non validi.",
        "Inserisci l'indice della riga da modificare",
        "Inserisci la nuova riga di codice:",
        "Inserisci l'indice della riga da eliminare",
        "Inserisci il numero della riga per spostarla a sinistra",
        "Inserisci il numero della riga per spostarla a destra",
        "Copiato negli appunti!",
        "Incolla codice",
        "Appunti vuoti. Niente da incollare.",
        "Impossibile accedere agli appunti."
    ],
    "Dutch": [
        "Python Code Bouwer",
        "Selecteer taal",
        "Automatisch inspringen",
        "Inspringgrootte:",
        "Regel toevoegen",
        "Lege regel",
        "Regel herschikken",
        "Regel bewerken",
        "Regel verwijderen",
        "Code uitvoeren",
        "Code opslaan",
        "Code kopiëren",
        "Nieuwe code",
        "Inspringing naar links verschuiven",
        "Inspringing naar rechts verschuiven",
        "Voer een regel code in:",
        "Voer de index van de te verplaatsen regel in",
        "Voer de nieuwe index voor de regel in",
        "Ongeldige indexen opgegeven.",
        "Voer de index van de te bewerken regel in",
        "Voer de nieuwe code regel in:",
        "Voer de index van de te verwijderen regel in",
        "Voer het regelnummer in om naar links te verschuiven",
        "Voer het regelnummer in om naar rechts te verschuiven",
        "Gekopieerd naar klembord!",
        "Code plakken",
        "Klembord is leeg. Niets om te plakken.",
        "Kon geen toegang krijgen tot het klembord."
    ],
    "Portuguese": [
        "Construtor de Código Python",
        "Selecionar idioma",
        "Indentação automática",
        "Tamanho da indentação:",
        "Adicionar linha",
        "Linha em branco",
        "Reordenar linha",
        "Editar linha",
        "Excluir linha",
        "Executar código",
        "Salvar código",
        "Copiar código",
        "Novo código",
        "Deslocar indentação para a esquerda",
        "Deslocar indentação para a direita",
        "Insira uma linha de código:",
        "Insira o índice da linha a ser movida",
        "Insira o novo índice para a linha",
        "Índices inválidos.",
        "Insira o índice da linha a ser editada",
        "Insira a nova linha de código:",
        "Insira o índice da linha a ser excluída",
        "Insira o número da linha para deslocar para a esquerda",
        "Insira o número da linha para deslocar para a direita",
        "Copiado para a área de transferência!",
        "Colar código",
        "Área de transferência vazia. Nada para colar.",
        "Falha ao acessar a área de transferência."
    ],
    "Russian": [
        "Генератор кода Python",
        "Выберите язык",
        "Автоматический отступ",
        "Размер отступа:",
        "Добавить строку",
        "Пустая строка",
        "Изменить порядок строки",
        "Редактировать строку",
        "Удалить строку",
        "Выполнить код",
        "Сохранить код",
        "Копировать код",
        "Новый код",
        "Сдвинуть отступ влево",
        "Сдвинуть отступ вправо",
        "Введите строку кода:",
        "Введите индекс строки для перемещения",
        "Введите новый индекс для строки",
        "Предоставлены неверные индексы.",
        "Введите индекс строки для редактирования",
        "Введите новую строку кода:",
        "Введите индекс строки для удаления",
        "Введите номер строки для сдвига влево",
        "Введите номер строки для сдвига вправо",
        "Скопировано в буфер обмена!",
        "Вставить код",
        "Буфер обмена пуст. Нечего вставлять.",
        "Не удалось получить доступ к буферу обмена."
    ],
    "Japanese": [
        "Pythonコードビルダー",
        "言語を選択",
        "自動インデント",
        "インデントのサイズ：",
        "行を追加",
        "空行",
        "行の並び替え",
        "行を編集",
        "行を削除",
        "コードを実行",
        "コードを保存",
        "コードをコピー",
        "新しいコード",
        "インデントを左にシフト",
        "インデントを右にシフト",
        "コード行を入力してください：",
        "移動する行のインデックスを入力",
        "行の新しいインデックスを入力",
        "無効なインデックスが指定されました。",
        "編集する行のインデックスを入力",
        "新しいコード行を入力してください：",
        "削除する行のインデックスを入力",
        "左にシフトする行番号を入力",
        "右にシフトする行番号を入力",
        "クリップボードにコピーされました！",
        "コードを貼り付け",
        "クリップボードが空です。貼り付けるものがありません。",
        "クリップボードへのアクセスに失敗しました。"
    ],
    "Chinese (traditional)": [
        "Python 程式碼生成器",
        "選擇語言",
        "自動縮排",
        "縮排大小：",
        "新增行",
        "空行",
        "重新排序行",
        "編輯行",
        "刪除行",
        "執行程式碼",
        "儲存程式碼",
        "複製程式碼",
        "新程式碼",
        "縮排向左移動",
        "縮排向右移動",
        "輸入一行程式碼：",
        "輸入要移動的行索引",
        "輸入該行的新索引",
        "提供的索引無效。",
        "輸入要編輯的行索引",
        "輸入新的程式碼行：",
        "輸入要刪除的行索引",
        "輸入要向左移動的行號",
        "輸入要向右移動的行號",
        "已複製到剪貼簿！",
        "貼上程式碼",
        "剪貼簿為空。無可貼上內容。",
        "無法訪問剪貼簿。"
    ],
    "Chinese (simplified)": [
        "Python 代码生成器",
        "选择语言",
        "自动缩进",
        "缩进大小：",
        "添加行",
        "空行",
        "重新排序行",
        "编辑行",
        "删除行",
        "运行代码",
        "保存代码",
        "复制代码",
        "新代码",
        "缩进左移",
        "缩进右移",
        "输入一行代码：",
        "输入要移动的行索引",
        "输入该行的新索引",
        "提供的索引无效。",
        "输入要编辑的行索引",
        "输入新的代码行：",
        "输入要删除的行索引",
        "输入要左移的行号",
        "输入要右移的行号",
        "已复制到剪贴板！",
        "粘贴代码",
        "剪贴板为空。没有可粘贴的内容。",
        "无法访问剪贴板。"
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
        "들여쓰기 왼쪽으로 이동",
        "들여쓰기 오른쪽으로 이동",
        "코드 한 줄 입력:",
        "이동할 줄의 인덱스 입력",
        "줄의 새 인덱스 입력",
        "유효하지 않은 인덱스입니다.",
        "편집할 줄의 인덱스 입력",
        "새 코드 줄 입력:",
        "삭제할 줄의 인덱스 입력",
        "왼쪽으로 이동할 줄 번호 입력",
        "오른쪽으로 이동할 줄 번호 입력",
        "클립보드에 복사됨!",
        "코드 붙여넣기",
        "클립보드가 비어 있습니다. 붙여넣을 내용이 없습니다.",
        "클립보드 접근에 실패했습니다."
    ]
}
widths = {
    "English": 1080,
    "French": 1500,
    "German": 1540,
    "Spanish": 1500,
    "Italian": 1360,
    "Dutch": 1530,
    "Portuguese": 1550,
    "Russian": 1560,
    "Japanese": 1320,
    "Chinese (traditional)": 1000,
    "Chinese (simplified)": 900,
    "Korean": 1100
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

        if line in ["pass", "continue", "break", "return"]:
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
        self.current_file = None

        # Create a frame for the text area and line numbers
        self.frame = tk.Frame(master)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Create a vertical scrollbar
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure scrollbar
        self.scrollbar.config(command=self.yscroll)

        # Create a horizontal scrollbar
        self.scrollbar2 = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        self.scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure scrollbar
        self.scrollbar2.config(command=self.xscroll)

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
        self.text_area = tk.Text(self.frame, height=20, width=60, xscrollcommand=self.scrollbar2.set, yscrollcommand=self.scrollbar.set, state=tk.NORMAL, wrap="none")
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

        self.paste_button = tk.Button(self.button_frame, text=self.text_list[25], command=self.paste_code)
        self.paste_button.pack(side=tk.LEFT, padx=5)

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

    def add_blank_line(self):
        self.line_manager.add_blank_line()
        self.update_text_area()

    def rearrange_line(self):
        try:
            index = simpledialog.askinteger("Input", f"{self.text_list[16]} (1-{len(self.line_manager.code_lines)}):") - 1
            try:
                new_index = simpledialog.askinteger("Input", f"{self.text_list[17]} (1-{len(self.line_manager.code_lines)}):") - 1
                if index is not None and new_index is not None:
                    try:
                        self.line_manager.rearrange_line(index, new_index)
                        self.update_text_area()
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
        except:
            pass

    def delete_line(self):
        try:
            index = simpledialog.askinteger("Input", f"{self.text_list[21]} (1-{len(self.line_manager.code_lines)}):") - 1
            if index is not None:
                try:
                    self.line_manager.delete_line(index)
                    self.update_text_area()
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
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py, *.pyw, *.pyi"), ("Text files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.line_manager.get_code())
            except FileNotFoundError:
                pass

    def copy_code(self):
        set_clipboard(self.line_manager.get_code())
        print(self.text_list[24])

    def new_code(self):
        self.line_manager.code_lines.clear()
        self.update_text_area()

    def paste_code(self):
        try:
            clipboard_text = self.master.clipboard_get()  # Get clipboard content
            if clipboard_text:  # Check if clipboard is not empty
                lines = clipboard_text.splitlines()  # Split clipboard text by lines
                for line in lines:
                    self.line_manager.add_line(line)  # Add each line from clipboard
                self.update_text_area()  # Refresh text area
            else:
                messagebox.showinfo("Clipboard Empty", self.text_list[26])
        except tk.TclError:
            messagebox.showerror("Error", self.text_list[27])

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
        self.text_area.configure(xscrollcommand=self.scrollbar2.set, yscrollcommand=self.scrollbar.set)
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        self.line_numbers.configure(state=tk.NORMAL)
        self.line_numbers.delete(1.0, tk.END)

        # Calculate the width of the line number area
        max_digits = len(str(len(self.line_manager.code_lines)))  # Adjust width for the total lines

        for i in range(1, len(self.line_manager.code_lines) + 1):
            self.line_numbers.insert(tk.END, f"{i:>{max_digits}}\n")  # Right-align line numbers

        self.line_numbers.configure(state=tk.DISABLED, width=max_digits)

    def xscroll(self, *args):
        self.text_area.xview(*args)
        self.line_numbers.xview(*args)

    def yscroll(self, *args):
        self.text_area.yview(*args)
        self.line_numbers.yview(*args)

if __name__ == "__main__":
    LanguageMenu()
