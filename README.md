# Password Strength Checker

A clean, modern desktop application built with **Python** and **CustomTkinter** that evaluates password strength and provides instant, actionable feedback.

Developed by **Sukhmandeep Singh** ([TechWithSukhman](https://github.com)).

## Features

- **Modern CustomTkinter UI:** Responsive desktop window (`500x400`) with automatic **System Light/Dark Mode** support.
- **Instant Color-Coded Status:** Displays **Strong password** in bold green and **Weak password** in bold red.
- **Helpful Password Tips:** Automatically displays improvement tips and an example format whenever a weak password is detected.
- **Empty Input Validation:** Shows a pop-up warning alert if the user submits an empty field.
- **Keyboard Friendly:** Supports pressing the **Enter** key or clicking the **Check** button to evaluate passwords.
- **5-Point Security Validation:** Checks passwords against standard complexity rules:
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
   git clone https://github.com/PasswordStrengthChecker.git
   cd PasswordStrengthChecker
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # On Linux/macOS
   # .venv\Scripts\activate         # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install customtkinter
   ```

## Usage

Run the application from your terminal:

```bash
python main.py
```

1. Type a password into the input field.
2. Press **Enter** or click **Check** to view the strength result and improvement tips.

## Author

**Sukhmandeep Singh** ([TechWithSukhman](https://github.com))

## License

This project is open-source and available under the [MIT License](LICENSE).
