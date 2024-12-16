# Project Overview
This is a Django project for a blog application. The project is built using Django 5.1.4 and includes features such as user authentication, post creation, and email sharing.

## Project Structure
The project is structured into the following apps:

- my_site: The main project app, containing settings and configuration.
- blog: The blog app, containing models, views, templates, and URLs for the blog functionality.

## Settings
The project settings are defined in my_site/settings.py. The following settings are notable:

- SECRET_KEY: A secret key for the project, used for security purposes.
- DEBUG: A boolean indicating whether the project is in debug mode.
- ALLOWED_HOSTS: A list of allowed hosts for the project.
- INSTALLED_APPS: A list of installed apps, including the blog app.
- DATABASES: The database configuration, using SQLite as the default database.

## .env File
The .env file contains the following environment variables:

- DATABASE_URL: The URL for the database connection.
- EMAIL_HOST: The host for sending emails.
- EMAIL_PORT: The port for sending emails.
- EMAIL_HOST_USER: The username for sending emails.
- EMAIL_HOST_PASSWORD: The password for sending emails.

## Models
The blog app defines the following models:

- Post: A model representing a blog post, with fields for title, slug, author, body, publish date, and status.
- User: A model representing a user, with fields for username, email, and password.

## Views
The blog app defines the following views:

- PostListView: A view for displaying a list of posts.
- PostDetailView: A view for displaying a single post.
- post_share: A view for sharing a post via email.

## Templates
The blog app defines the following templates:

- blog/base.html: A base template for the blog app.
- blog/list.html: A template for displaying a list of posts.
- blog/detail.html: A template for displaying a single post.
- blog/share.html: A template for sharing a post via email.

## URLs
The blog app defines the following URLs:

- /: The root URL, displaying a list of posts.
- /post/<int:year>/<int:month>/<int:day>/<slug:post>/: A URL for displaying a single post.
- /post/<int:post_id>/share/: A URL for sharing a post via email.

## Forms
The blog app defines the following forms:

- EmailPostForm: A form for sharing a post via email.

## Admin
The blog app defines the following admin classes:

- PostAdmin: An admin class for the Post model.

## Deployment
The project can be deployed using the following steps:

- Install the required dependencies using pip install -r requirements.txt.
- Run the migrations using python manage.py migrate.
- Run the development server using python manage.py runserver.
- Access the project at http://localhost:8000/.
