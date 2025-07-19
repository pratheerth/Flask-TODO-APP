# Flask TODO Application

## Introduction

This project is a simple web based **To‑Do list** built with [Flask](https://flask.palletsprojects.com/) and [TinyDB](https://tinydb.readthedocs.io/). It allows you to create tasks, mark them as complete, update the title and delete them. The data is stored in a small JSON file (`db.json`), making it lightweight and easy to run locally.

## Project Structure

```
Flask-TODO-APP/
├── app.py             # Flask application and route definitions
├── templates/
│   └── index.html     # Main page template
├── db.json            # TinyDB database file
├── screenshot/        # Images showing the app in action
└── README.md
```

### Components

- **app.py** – Contains the Flask application. Routes include:
  - `/` – Display all tasks.
  - `/add` – Add a new task via POST form submission.
  - `/update` – Update an existing task title.
  - `/delete/<id>` – Remove a task from the database.
  - `/complete/<id>` – Mark a task as completed.
- **templates/index.html** – Front-end page built with W3.CSS. It lists current tasks and contains forms/buttons to add, edit, complete or delete them.
- **db.json** – TinyDB file used to persist todo items. The database is automatically created when the app runs.
- **screenshot/** – Sample screenshots of the user interface.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-user/Flask-TODO-APP.git
   cd Flask-TODO-APP
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask tinydb
   ```

   These packages are the only requirements for running the app.

## Running the Application

Run the Flask development server directly with:

```bash
python app.py
```

By default the server runs on `http://127.0.0.1:5000/`. Open this URL in your browser and you will see the main To‑Do list interface.

## Using the Application

1. **Add a task** – Use the input box at the top of the list and press the `+` button.
2. **Mark complete** – Click the checkmark next to a task to mark it finished. Completed tasks appear with a green background.
3. **Edit a task** – Click the pencil icon to bring up the popup editor, then submit the form to update the title.
4. **Delete a task** – Click the trash icon to remove a task from the list.

Screenshots in the `screenshot` folder provide visual examples of these actions.

## Notes

- The database is stored in `db.json` in the project root. Clearing this file will reset the app’s state.
- The app runs with `debug=True` inside `app.py`, so it will automatically reload when you modify the code during development.

Enjoy building your own simple task manager with Flask!
