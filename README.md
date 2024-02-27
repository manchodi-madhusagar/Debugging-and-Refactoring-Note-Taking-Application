
# Debugging and Refactoring Note Taking Application

## Overview
This repository contains a note-taking application built with Flask that requires debugging and refactoring. The application allows users to create, view, and delete notes. The goal of this project is to identify and fix existing bugs, as well as refactor the codebase to improve maintainability and performance.

## Features
- Create new notes with a title and content.
- View existing notes.
- Delete notes.

## Bugs Identified
1. **Missing Form Method and Action:**
   - The form in the HTML file lacks the method and action attributes.
   - Fix: Update the form element to include the method as POST and the action as the home route ("/").

2. **Incorrect Method to Retrieve Form Data:**
   - In the Flask application, `request.args.get("note")` is used to get the note from the request, which is incorrect as it's used for query parameters.
   - Fix: Replace `request.args.get("note")` with `request.form.get("note")` to properly retrieve form data.

3. **Route Restriction to POST Requests:**
   - The route in the Flask application only allows POST requests.
   - Fix: Modify the route to allow both GET and POST requests.

## Refactoring Goals
1. Improve code readability by using meaningful variable names and comments.
2. Implement proper error handling to gracefully handle exceptions.
3. Modularize the codebase into smaller, reusable functions.
4. Optimize database queries for improved performance.
5. Implement data validation to prevent injection attacks and ensure data integrity.

## Getting Started
To run the application locally, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Access the application in your web browser at `http://localhost:5000`.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

