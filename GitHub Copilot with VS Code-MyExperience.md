# Using GitHub Copilot with VS Code: Experience and Reflections

For this project, I leveraged **GitHub Copilot** within **Visual Studio Code** to rapidly develop a Python calculator application with a graphical user interface. Copilot provided intelligent code suggestions, boilerplate code, and even UI layout ideas, which significantly accelerated the initial development process. I was able to iterate quickly, adding features like dark/light mode and a number pad layout with minimal manual coding.

---

## Challenges Faced

- **UI Customization:**  
    Copilot’s suggestions for Tkinter UI were sometimes generic. I needed to manually adjust widget placements and color schemes to achieve a polished, modern look, especially for dark mode.

- **State Management:**  
    Ensuring that theme toggling updated all UI elements correctly required careful review and some manual debugging, as Copilot’s suggestions didn’t always cover every widget.

- **Refactoring:**  
    As requirements changed (e.g., removing the debug button), I had to ensure Copilot’s edits didn’t leave behind unused code or references.

---

## How I Resolved Them

- Used Copilot’s code completions as a starting point, then customized and refactored the code to fit my needs.
- Frequently ran and tested the application in VS Code, using the integrated terminal and debugger to catch and fix UI or logic issues.
- When Copilot’s suggestions were incomplete, I supplemented them with my own research and manual edits, ensuring the final product met all requirements.

---

**Overall**, Copilot and VS Code together made the development process faster and more efficient, while still allowing for full control and customization when needed.