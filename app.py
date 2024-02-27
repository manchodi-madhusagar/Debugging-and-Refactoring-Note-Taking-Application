from flask import Flask, render_template, request, redirect  

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index.html", notes=notes)

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    if 0 <= index < len(notes):
        del notes[index]
    return redirect('/')

@app.route('/delete/all', methods=["POST"])
def delete_all():
    notes.clear()
    return redirect('/')

@app.route('/print_notes')
def print_notes():
    return render_template("print_notes.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)