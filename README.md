# Password Strength Checker

A clean, lightweight desktop application built with **Python** and **CustomTkinter** that evaluates password strength and provides instant color-coded feedback.

Developed by **Sukhmandeep Singh** ([TechWithSukhman](https://github.com)).

## Features

- **Modern CustomTkinter GUI:** Built with a responsive desktop interface (`500x400`).
- **System Theme Sync:** Automatically adapts to your operating system's **Light** or **Dark** mode.
- **Instant Color-Coded Results:** Displays **Strong password** in bold green and **Weak password** in bold red.
- **5-Point Security Validation:** Checks passwords against core security criteria:
  - Minimum length of **8 characters**
  - At least one **lowercase letter** (`a-z`)
  - At least one **uppercase letter** (`A-Z`)
  - At least one **numeric digit** (`0-9`)
  - At least one **special symbol** (`!@#$%^&*`, etc.)

## Prerequisites

- **Python 3.8+**
- **CustomTkinter**

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PasswordStrenthChecker.git
   cd PasswordStrenthChecker
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # On Linux/macOS
   # .venv\Scripts\activate         # On Windows
   ```

3. **Install CustomTkinter:**
   ```bash
   pip install customtkinter
   ```

## Usage

Run the application from your terminal:

```bash
python gui.py
```
*(Replace `gui.py` with your script's filename if different.)*

1. Enter your password into the text field.
2. Click **Check** to see whether your password is **Strong** or **Weak**.

## Author

**Sukhmandeep Singh** (TechWithSukhman)

## License

This project is open-source and available under the [MIT License](LICENSE).
