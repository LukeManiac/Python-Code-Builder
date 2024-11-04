Code Line Manager
Welcome to the Code Line Manager! This is a simple GUI application I built using Tkinter in Python to help manage lines of code. With this application, I can add, edit, delete, rearrange, and manage indentation levels for my code effortlessly. It also includes features such as saving and pasting code, managing line numbers, and changing the application's language.

Overview of Features:
• CodeLineManager
• Purpose: This class manages a list of code lines, tracks indentation, and provides methods for manipulating the code lines.
• Key Methods:
◦ add_line: I can add a new line, with automatic indentation management.
◦ add_blank_line: This allows me to easily insert an empty line.
◦ rearrange_line: I can move a line from one index to another with this method.
◦ edit_line: I can update a specific line when needed.
◦ delete_line: This method lets me remove a line by index.
◦ get_code: I can retrieve the full code as a string.
◦ indent_line: Adds indentation to a line based on my preferences.
◦ increase_indent and decrease_indent: These methods help me adjust the indentation of specific lines.
◦ set_indent_size: I can adjust the indentation size for all lines.

• LanguageMenu
• Purpose: This class provides a language selection interface for the application.
• Key Methods:
◦ update_select_button: Updates the button text based on the selected language.
◦ set_language: Initializes the main application window with the language I select.

• CodeBuilderGUI
• Purpose: This is the main GUI where I can input and manage my code lines.
• Components:
◦ A text area for entering code.
◦ A display for line numbers.
◦ Buttons for various actions like add, delete, edit, etc.
◦ Checkboxes and entries for managing features like automatic indentation.
• Key Methods:
◦ Various methods for interacting with the GUI components (e.g., add_line, edit_line, update_text_area).
◦ run_code: Executes the code I entered in the text area.
◦ Clipboard functions for copying and pasting my code.

Potential Improvements
While I'm proud of this application, I see room for enhancement:

• Error Handling: I plan to improve error handling to provide more user-friendly messages, especially for invalid inputs.
• File Management: I would like to implement an "Open" feature to load existing code files into the text area and include type checks when saving/loading files.
• Indentation Management: Customizing the size of indentation dynamically would be beneficial, along with automatic adjustments based on code structure.
• Text Editing Features: I aim to add undo/redo functionality for better text management and implement syntax highlighting for an improved coding experience.
• User Interface Enhancements: I'm looking to enhance the layout and design for better usability and add tooltips or help documentation.
• Language Support: I want to expand language support by using a robust translation management system and potentially add support for more programming languages.

Getting Started
• To run this application, ensure you have Tkinter installed and properly set up in your Python environment. You can start the GUI by executing the script directly.

If you have any questions or need assistance with specific functionalities, feel free to reach out!
