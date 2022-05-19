# Your Blog

## Author

Joylene Kirui

# Description
This  is a personal blogging website where writers can post, edit and delete their blogs. Users who have signed up can view and comment on the blogs that has been posted by a writer.It also displays random quotes to inspire users.
## Live Link
[View Site](https://YourBlog.herokuapp.com)

## User Story

* A user can view the most recent posts.
* View and comment the blog posts on the site.
* Register to be allowed to log in to the application
* A user sees random quotes on the site
* A writer can create a blog from the application and update or delete blogs I have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  ```
2. Move to the folder and install requirements
  ```bash
  cd Blog-Posts
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python manage.py server
  ```
  ```
Open the application on your browser `127.0.0.1:5000`.

## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Contact Information 

If you have any questions or contributions, please email me at [joylinkirui@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Joylene Kirui**