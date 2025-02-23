# Import necessary modules from Flask and Python libraries
from flask import Flask, render_template, request, send_from_directory
import os
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Set up the folder for storing uploaded images
UPLOAD_FOLDER = "img"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the 'img' folder exists
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  # Store the folder path in the app configuration

# Route for the home page (index page)
@app.route('/')
def hello():
    # Render the 'home.html' template when the user accesses the root URL
    return render_template("home.html") 

@app.route('/enterPost', methods=["POST", "GET"]) 
def enterPost():
    if request.method == 'POST':
        # Extract form data from the POST request (i.e., name, location, content, and file)
        postUser = request.form.get("name", "No name provided")  # Default value if no name is entered
        postLocationName = request.form.get("location", "No location provided")  # Default location if none entered
        postContent = request.form.get("content", "No content provided")  # Default content if none entered
        file = request.files.get("file")  # Get the uploaded file

        # Set a default file path in case no file is uploaded
        postFilepath = "No file uploaded"  

        # If a file is uploaded, save it in the 'img' folder
        if file and file.filename:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)  # Save the file to the specified path
            postFilepath = filepath.replace("\\",'/') # Update the file path with the actual file location

        # For debugging, print the details of the post
        print("user: " + postUser)
        print("location: " + postLocationName)
        print("content: " + postContent)
        print("file: " + postFilepath)

        # Connect to the database and insert the new post
        connection = sqlite3.connect('post.db')
        cursor = connection.cursor()

        # Insert the new post into the post table
        cursor.execute('''
            INSERT INTO post (username, picture, content, locationname) 
            VALUES (?, ?, ?, ?)
        ''', (postUser, postFilepath, postContent, postLocationName))

        # Commit the transaction and close the connection
        connection.commit()
        connection.close()

    # Render the 'entry.html' template after the post submission
    return render_template("entry.html")

@app.route('/explore')
def explore():
    # Connect to the SQLite database 'post.db'
    connection = sqlite3.connect('post.db')
    cursor = connection.cursor()
    
    # Query the database to fetch posts along with location details (joined from location table)
    cursor.execute('''
        SELECT post.username, post.picture, post.content, post.locationname, location.address, location.uva, location.cville
        FROM post
        JOIN location ON post.locationname = location.name
    ''')
    
    # Fetch all the results from the query
    posts = cursor.fetchall()
    
    # Close the database connection after fetching the data
    connection.close()
    
    # Format the database results into a list of dictionaries for easier access in the template
    posts_data = [{
        'username': post[0],
        'picture': post[1],
        'content': post[2],
        'locationname': post[3],
        'address': post[4],
        'uva': post[5],
        'cville': post[6]
    } for post in posts]

    # Render the 'explore.html' template and pass the posts data to the template
    return render_template("explore.html", posts=posts_data)


# Route to serve the uploaded images (allows displaying images on the web page)
@app.route('/<filename>')
def uploaded_file(filename):
    # Send the requested file from the 'img' folder
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Run the app in debug mode for development (restarts the server automatically on code changes)
if __name__ == '__main__':
    app.run(debug=True)
