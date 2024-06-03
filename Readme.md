# Movie Library Web Application

This is a Django-based movie library web application with user authentication, movie search, and playlist functionality. Users can sign up, log in, search for movies using the OMDB API, and create lists of movies (similar to YouTube playlists). Lists can be public or private.

## Features

1. **User Authentication**:
   - Sign In / Sign Up functionality.
   - Secure login and registration process.

2. **Home Screen**:
   - Search option to find movies using the OMDB API.
   - Display movie details.
   - Add movies to personalized lists.

3. **Movie Lists**:
   - Users can create and manage multiple lists of movies.
   - Lists can be marked as public or private.
   - Public lists can be shared with anyone via a link.
   - Private lists are visible only to the creator.

## Application Links

- [Hosted Application](#) (Replace this with your hosted application link)
- [Source Code Repository](#) (Replace this with the link to your code repository, e.g., GitHub)

## Local Setup Instructions

To run this application locally, follow these steps:

### Prerequisites

- Python 3.x
- Django
- pip (Python package installer)

### Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Server**:
    ```bash
    python manage.py runserver
    ```

### Access the Application

- Home Page (Login/Register): [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Successful Login (Movie Search and Add to Playlist): [http://127.0.0.1:8000/success/](http://127.0.0.1:8000/success/)
- User Playlist: [http://127.0.0.1:8000/playlist/](http://127.0.0.1:8000/playlist/)

## OMDB API Setup

This application uses the OMDB API to search for movies. You need to obtain an API key from [OMDB API](http://www.omdbapi.com/apikey.aspx) and add it to your environment variables.

1. **Obtain an API Key**:
    - Go to [OMDB API](http://www.omdbapi.com/apikey.aspx) and sign up to get your API key.

2. **Add the API Key to Environment Variables**:
    ```bash
    export OMDB_API_KEY='your_api_key'  # On Windows use `set OMDB_API_KEY='your_api_key'`
    ```

## Project Structure

- `movie_library/`: Main project directory.
- `users/`: Django app for user authentication.
- `movies/`: Django app for movie search and playlist management.
- `templates/`: HTML templates for the application.
- `static/`: Static files (CSS, JavaScript, images).
- `requirements.txt`: List of dependencies.

## Deployment

This application can be hosted on platforms like Netlify, Vercel, Heroku, etc. Please follow their respective documentation for deployment instructions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [OMDB API](http://www.omdbapi.com/)

## Contact

For any inquiries or feedback, please contact [Your Name] at [Your Email].

