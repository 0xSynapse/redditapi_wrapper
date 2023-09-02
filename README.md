# Reddit Article Viewer Web Application

This Markdown document outlines the structure and functionality of a simple web application designed to fetch and display articles from a chosen subreddit using the Reddit API. The application consists of a backend created using Python and a frontend built with HTML and JavaScript.

## Backend

The backend of the web application is developed using Python. It utilizes the Reddit API to fetch articles from a chosen subreddit and exposes a REST API endpoint to retrieve the last 10 threads as JSON data.

### Backend Steps:

1. Set up a Python environment with the required dependencies, such as Django for creating the REST API.

2. Use the Reddit API to authenticate and fetch articles from the chosen subreddit.

3. Create a route in the Django application to serve the fetched articles as JSON data.

## Frontend

The frontend of the web application is a simple HTML page with basic styling. It uses JavaScript to fetch data from the backend's REST API endpoint and dynamically display the articles on the page.

### Frontend Steps:

1. Design a basic HTML structure for the web page, including placeholders for the article information.

2. Use JavaScript to fetch data from the backend's REST API endpoint.

3. Dynamically populate the HTML page with the fetched article information.

## Functionality

The web application allows users to view the latest articles from a chosen subreddit. Each article is displayed with the following information: title, author, creation date, and a link to the original thread.

The application is designed to be responsive, ensuring that it functions well on different devices, such as desktops, tablets, and mobile phones.

## How to Run the Application

To run the web application, follow these steps:

1. Clone the repository containing the application code to your local machine.

2. Set up the Python environment by installing the required dependencies using `pip install requirements.txt`.

3. Configure the Reddit API authentication by obtaining the necessary credentials (client ID and secret) and adding them to the backend code.

4. Start the Django backend by running the following command: `python manage.py runserver`.

5. Open the provided URL in a web browser to access the application.

The frontend will display the latest articles from the chosen subreddit, fetching data from the backend's REST API.

## Third-Party Libraries

The application uses the following third-party libraries:

- Django: Used to create the backend and serve the REST API.
- JavaScript Fetch API: Used to make asynchronous requests to the backend API and update the frontend dynamically.
