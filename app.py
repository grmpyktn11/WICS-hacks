from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "img"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'  

@app.route('/entry', methods=["POST", "GET"]) 
def postPage():
    if request.method == 'POST':
        postUser = request.form.get("name", "No name provided")
        postLocationName = request.form.get("location", "No location provided")
        postContent = request.form.get("content", "No content provided")
        postHashtag = request.form.get("hashtag", "No hashtag provided")
        file = request.files.get("file")

        postFilepath = "No file uploaded"  # Default file path if no file is uploaded

        if file and file.filename:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            postFilepath = filepath

        print("user: " + postUser)
        print("location: " + postLocationName)
        print("content: " + postContent)
        print(postHashtag)
        print("file: " + postFilepath)


    return render_template("entry.html")

@app.route('/img/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
