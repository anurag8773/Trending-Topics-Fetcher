# Trending Topics Fetcher

This project fetches the latest trending topics from a specified platform (e.g., Twitter/X) using Selenium, stores the results in a MongoDB database, and allows a frontend (HTML) to interact with the backend (Flask) to display the results.

## Project Structure

- **Backend (Flask API)**: A Python Flask application that scrapes trending topics using Selenium and stores the results in MongoDB.
- **Frontend (HTML)**: A simple HTML page with a button that triggers the backend to fetch trending topics and displays the results.

## Features

- **Trending Topics Fetching**: Scrapes trending topics from the specified platform.
- **Data Storage**: Stores the trending topics, timestamp, and IP address in MongoDB.
- **Simple Frontend**: Provides a button to trigger the backend script and display results.
- **CORS Handling**: Allows the frontend and backend to interact seamlessly using `flask-cors`.

## Technologies Used

- **Backend**: Flask, Python, Selenium, Flask-CORS, MongoDB
- **Frontend**: HTML, JavaScript
- **Web Scraping**: Selenium WebDriver

## Installation & Setup

### 1. Set up the Backend

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/trending-topics-fetcher.git
   cd trending-topics-fetcher
2. Install the required dependencies:
   pip install flask flask-cors pymongo selenium

3. MongoDB Setup:
  Make sure MongoDB is installed locally or use a cloud-based MongoDB service like MongoDB Atlas.
  Create a database named twitter_trends and a collection named trending_topics to store the data.

4.Modify MongoDB URI:
  In the app.py file, update the MONGO_URI to match your MongoDB setup:

  Copy code
    MONGO_URI = "mongodb://localhost:27017"  # Local MongoDB URI
    # Or for MongoDB Atlas
    MONGO_URI = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>"

5. Run the Flask Backend:
  python scrape.py
  The backend will start running on http://127.0.0.1:5000.

### 2. Set up the Frontend
  Create an index.html file with the following code:

  Open the index.html file in your browser. Clicking the "Click here to run the script" button will trigger the backend to fetch trending topics and display the results.

  Usage
  Run the Backend: Start the Flask API by running the following command in the backend directory:

  python scrape.py
  Open the Frontend: Open the index.html file in your browser.

  Click the Button: Click the button on the frontend to run the script. The backend will fetch trending topics and display the results on the frontend.

Expected Output
Once the button is clicked, the frontend will display the following:

A list of the top 5 trending topics.
The timestamp of when the script finishes execution.
The IP address used for the request.
A JSON extract of the MongoDB record containing the fetched data.
Example Output:

csharp
Copy code
These are the most happening topics as on 2024-12-25 15:00:00
- Trend 1
- Trend 2
- Trend 3
- Trend 4
- Trend 5

The IP address used for this query was 192.168.1.1.

Here’s a JSON extract of this record from the MongoDB:
{
    "_id": "123456789",
    "trend1": "Trend 1",
    "trend2": "Trend 2",
    "trend3": "Trend 3",
    "trend4": "Trend 4",
    "trend5": "Trend 5",
    "date_time": "2024-12-25 15:00:00",
    "ip_address": "192.168.1.1"
}


Troubleshooting
  CORS Issues: If you encounter CORS errors when trying to fetch data, ensure that flask-cors is properly installed and configured in the Flask app. You can use CORS(app) to allow all origins or specify an         allowed origin.

  MongoDB Connection: Ensure MongoDB is running and accessible. If using MongoDB Atlas, verify your URI and network settings.

  Selenium Issues: If Selenium doesn't fetch the data correctly, check the XPath and the HTML structure of the page being scraped. The script may need adjustments if the structure changes.


Acknowledgments
  Selenium: For web scraping the trending topics from platforms like Twitter/X.
  Flask: For creating the backend API.
  MongoDB: For storing the trending topics data.
