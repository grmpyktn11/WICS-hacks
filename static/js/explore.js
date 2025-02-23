// JavaScript function to add a post to the user's itinerary
function addToItinerary(location, username, uva, cville) {
    // Send a POST request with JSON data (location, username, and bus info) to the server
    fetch('/add_to_itinerary', {
        method: 'POST',
        body: JSON.stringify({ location: location, username: username, uva: uva, cville: cville }),  // Sending data in the request body
        headers: { 'Content-Type': 'application/json' }  // Indicating the request content type is JSON
    })
    .then(response => response.json())  // Handle the server's response, expecting JSON
    .then(data => {
        // Update the 'itinerary' section with the new HTML returned from the server
        document.getElementById("itinerary").innerHTML = data.html;
    });
}