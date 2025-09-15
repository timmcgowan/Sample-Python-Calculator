import tkinter as tk
from tkinter import messagebox


# Calculator class with a traditional calculator UI (number pad and operation buttons)

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.geometry("320x470")
        self.resizable(False, False)
        self.expression = ""  # Stores the current input expression
        self.mode = 'light'  # Current theme mode
        self.colors = {
            'light': {
                'bg': '#f0f0f0', 'fg': '#000', 'button_bg': '#fff', 'button_fg': '#000', 'display_bg': '#fff', 'display_fg': '#000', 'special_bg': '#e0e0e0', 'special_fg': '#000'
            },
            'dark': {
                'bg': '#181818', 'fg': '#fff', 'button_bg': "#000000", 'button_fg': "#000000", 'display_bg': '#101214', 'display_fg': '#00ff99', 'special_bg': '#2d333b', 'special_fg': "#000000"
            }
        }
        self.widgets = []  # Store widgets for theme switching
        self.button_texts = [  # Store original button texts for toggling
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]
        self.create_widgets()
        self.apply_theme()


    def create_widgets(self):
        # Display for showing the current expression/result
        self.display_var = tk.StringVar()
        self.display = tk.Entry(self, textvariable=self.display_var, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right', state='readonly')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")
        self.widgets.append(self.display)

        # Button layout for a traditional calculator

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        self.button_refs = []  # Store button references for theme switching
        self.button_objs = []  # Store button objects for text update
        for idx, btn in enumerate(buttons):
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            action = self.create_action(text)
            b = tk.Button(self, text=text, width=5, height=2, font=("Arial", 16), command=action)
            b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)
            self.widgets.append(b)
            self.button_refs.append((b, text))
            self.button_objs.append(b)

        # Theme toggle button
        self.theme_btn = tk.Button(self, text="Toggle Dark/Light", font=("Arial", 12), command=self.toggle_theme)
        self.theme_btn.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=10, pady=8)
        self.widgets.append(self.theme_btn)

        # Configure grid weights for resizing
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def apply_theme(self):
        """Apply the current theme colors and update button text for all widgets."""
        c = self.colors[self.mode]
        self.configure(bg=c['bg'])
        self.display.configure(readonlybackground=c['display_bg'], fg=c['display_fg'], bg=c['display_bg'])
        # Update button text and color
        for idx, (b, text) in enumerate(self.button_refs):
            # Always update text (future-proof for mode-specific text)
            b.configure(text=self.button_texts[idx])
            # All buttons use special_bg/fg in dark mode for best contrast
            if self.mode == 'dark':
                if text in {'/', '*', '-', '+', '=', 'C', 'Debug'}:
                    b.configure(bg=c['special_bg'], fg=c['special_fg'], activebackground=c['special_bg'])
                else:
                    b.configure(bg=c['button_bg'], fg=c['button_fg'], activebackground=c['button_bg'])
            else:
                if text in {'/', '*', '-', '+', '=', 'C', 'Debug'}:
                    b.configure(bg=c['special_bg'], fg=c['special_fg'], activebackground=c['special_bg'])
                else:
                    b.configure(bg=c['button_bg'], fg=c['button_fg'], activebackground=c['button_bg'])
        self.theme_btn.configure(bg=c['special_bg'], fg=c['special_fg'], activebackground=c['special_bg'])
        # Optionally, update theme button text to show current mode
        self.theme_btn.configure(text=f"Switch to {'Light' if self.mode == 'dark' else 'Dark'} Mode")

    def toggle_theme(self):
        """Switch between dark and light mode."""
        self.mode = 'dark' if self.mode == 'light' else 'light'
        self.apply_theme()

    def create_action(self, char):
        """Return the appropriate function for each button."""
        if char == 'C':
            return self.clear
        elif char == '=':
            return self.calculate
        else:
            return lambda: self.append_char(char)

    def append_char(self, char):
        """Append a character (number/operator) to the expression."""
        self.expression += str(char)
        self.display_var.set(self.expression)

    def clear(self):
        """Clear the current expression."""
        self.expression = ""
        self.display_var.set("")

    def calculate(self):
        """Evaluate the expression and display the result. Handles errors gracefully."""
        try:
            # Evaluate the expression safely
            result = eval(self.expression)
            self.display_var.set(str(result))
            self.expression = str(result)  # Allow chaining calculations
        except ZeroDivisionError:
            self.display_var.set("Error: Div by 0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""



# Entry point for the calculator app
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
