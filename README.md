# Flask User Registration

A simple Flask web app with a registration form for a user's full name, city, and phone number. Submitting the form displays the entered details on a confirmation page.

## Features

- Responsive registration and confirmation pages
- Required name, city, and phone fields
- Tailwind CSS styling loaded from its CDN

> **Note:** This is a demonstration project. Submitted details are displayed on the confirmation page but are not saved to a database.

## Requirements

- Python 3.9 or later
- pip

## Run locally

1. Clone the repository and open its folder:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install Flask:

   ```bash
   python -m pip install "Flask>=3.1,<4.0"
   ```

4. Start the app:

   ```bash
   python app.py
   ```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project structure

```text
.
├── app.py
└── templates/
    ├── confirmation.html
    └── register.html
```

## Routes

| Method | Path      | Description                         |
|--------|-----------|-------------------------------------|
| GET    | `/`       | Displays the registration form      |
| POST   | `/submit` | Displays the submitted information  |
