from flask import Flask, render_template, request, redirect, url_for, session,make_response
import os


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure secret key

def get_notes():
    if 'notes' not in session:
        session['notes'] = []
    return session['notes']

@app.route('/', methods=["GET", "POST"])
def index():
    notes = get_notes()
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
        session['notes'] = notes  # Update session with new notes
        # Redirect to the same route after adding the note
        return redirect(url_for('index'))
    return render_template("index.html", notes=notes, enumerate=enumerate)

@app.route('/edit/<int:index>', methods=["GET", "POST"])
def edit(index):
    notes = get_notes()
    if request.method == "POST":
        new_note = request.form.get("note")
        if 0 <= index < len(notes):
            notes[index] = new_note
            session['notes'] = notes  # Update session with edited notes
            return redirect(url_for('index'))
    if 0 <= index < len(notes):
        return render_template("edit_note.html", index=index, note=notes[index])
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    notes = get_notes()
    if 0 <= index < len(notes):
        del notes[index]
        session['notes'] = notes  # Update session with updated notes
    return redirect('/')

@app.route('/delete/all', methods=["POST"])
def delete_all():
    session.pop('notes', None)  # Clear notes from session
    return redirect('/')

@app.route('/print_notes')
def print_notes():
    notes = get_notes()
    # Create a temporary text file
    temp_file_path = 'temp_notes.txt'
    with open(temp_file_path, 'w') as file:
        for note in notes:
            file.write(note + '\n')
    # Serve the file as a downloadable attachment
    response = make_response(open(temp_file_path).read())
    response.headers['Content-Disposition'] = 'attachment; filename=notes.txt'
    # Remove the temporary file
    os.remove(temp_file_path)
    return response
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
