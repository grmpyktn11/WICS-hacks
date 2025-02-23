# Import necessary modules from Flask and Python libraries
from flask import Flask, render_template, request, send_from_directory, session, jsonify, redirect
import os
import sqlite3

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session storage, ensures data security

# Set up the folder for storing uploaded images
UPLOAD_FOLDER = "img"  # Folder where images will be uploaded and stored
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the 'img' folder if it doesn't exist
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  # Store the folder path in the app configuration

# Route for the home page (index page)
@app.route('/')
def hello():
    # When the user visits the root URL ('/'), render and show the 'home.html' page
    return render_template("home.html") 

# Route to allow users to submit a new post
@app.route('/enterPost', methods=["POST", "GET"]) 
def enterPost():
    if request.method == 'POST':
        # Extract form data (user inputs) from the POST request
        postUser = request.form.get("name", "No name provided")  # Default name if none entered
        postLocationName = request.form.get("location", "No location provided")  # Default location if none entered
        postContent = request.form.get("content", "No content provided")  # Default content if none entered
        file = request.files.get("file")  # Get the uploaded file from the form

        postFilepath = "No file uploaded"  # Default file path if no file is uploaded

        # If a file is uploaded, save it to the 'img' folder
        if file and file.filename:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)  # Create a full path for the file
            file.save(filepath)  # Save the uploaded file to the specified path
            postFilepath = filepath.replace("\\",'/')  # Update the file path with the actual location

        # Print post data to the console for debugging (optional for backend developers)
        print("user: " + postUser)
        print("location: " + postLocationName)
        print("content: " + postContent)
        print("file: " + postFilepath)

        # Connect to the database and insert the new post data
        connection = sqlite3.connect('post.db')
        cursor = connection.cursor()

        # Insert the new post data into the 'post' table in the database
        cursor.execute('''
            INSERT INTO post (username, picture, content, locationname) 
            VALUES (?, ?, ?, ?)
        ''', (postUser, postFilepath, postContent, postLocationName))

        # Commit the transaction and close the database connection
        connection.commit()
        connection.close()

    # Render and show the 'entry.html' page after the post submission
    return render_template("entry.html")

# Route to explore posts, show them on the map or feed
@app.route('/explore')
def explore():
    # Connect to the database and fetch the posts data
    connection = sqlite3.connect('post.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT post.username, post.picture, post.content, post.locationname, location.address, location.uva, location.cville
        FROM post
        JOIN location ON post.locationname = location.name
    ''')
    posts = cursor.fetchall()  # Fetch all the posts from the database
    connection.close()

    # Create a list of dictionaries with post data to display in the front-end
    posts_data = [{
        'username': post[0],
        'picture': post[1],
        'content': post[2],
        'locationname': post[3],
        'address': post[4],
        'uva': post[5],
        'cville': post[6]
    } for post in posts]

    # Get the itinerary data from the session (this stores user activity across pages)
    itinerary = session.get('itinerary', [])

    # Render and show the 'explore.html' page, passing the posts data and itinerary
    return render_template("explore.html", posts=posts_data, itinerary=itinerary)

# Route to add a post to the itinerary (session data)
@app.route('/add_to_itinerary', methods=['POST'])
def add_to_itinerary():
    data = request.json  # Get the incoming JSON data
    location = data.get('location', 'Unknown')  # Get the location
    username = data.get('username', 'Unknown')  # Get the username

    # Connect to the database and get bus information for the location
    connection = sqlite3.connect('post.db')
    cursor = connection.cursor()
    cursor.execute("SELECT uva, cville FROM location WHERE name = ?", (location,))
    result = cursor.fetchone()
    connection.close()

    # If location info exists, get bus details; otherwise, set default values
    if result:
        uva, cville = result
    else:
        uva, cville = "No bus info", "No bus info"

    # Initialize itinerary in the session if it doesn't exist
    if 'itinerary' not in session:
        session['itinerary'] = []

    # Add the current post to the itinerary stored in the session
    session['itinerary'].append({'location': location, 'username': username, 'uva': uva, 'cville': cville})
    session.modified = True  # Ensure changes to the session are saved

    # Create the HTML to display the updated itinerary
    itinerary_html = "".join(
        f"<p>{item['location']} - {item['username']}<br><strong>Bus: </strong>{item['uva']}, {item['cville']}</p>"
        for item in session['itinerary']
    )

    # Return the updated itinerary HTML to the front-end (can be used in a dynamic web page update)
    return jsonify(html=itinerary_html)

# Route to clear the itinerary (reset session data)
@app.route('/clear_itinerary', methods=['POST'])
def clear_itinerary():
    session.clear()  # Clear all data from the session, including itinerary
    return redirect('/explore')  # Redirect back to the 'explore' page

# Route to serve the uploaded images (allows displaying images on the web page)
@app.route('/<filename>')
def uploaded_file(filename):
    # This route serves images from the 'img' folder, enabling them to be displayed in the front-end
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Run the app in debug mode for development (restarts the server automatically on code changes)
if __name__ == '__main__':
    app.run(debug=True)
