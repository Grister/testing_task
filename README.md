# Getting Started

### Installation

Clone the repository
```
git clone https://github.com/Grister/testing_task.git
```
Navigate to the project directory:
```
cd testing_task
```
Switch branch
```
git checkout dev
```
Create .env file in base directory. Example of .env file
```
DJANGO_SECRET_KEY='l^h+1r57ilnvif%!15y42ath^w!$p^_$70+@pra0bb3ga0#t2v'
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_NAME=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

Install [Docker for Desktop](https://docs.docker.com/desktop/install/windows-install/)

Run docker-compose in terminal <br>
Important! You must be in the directory with the docker files
```
docker-compose up
```

At the end  you can stop the containers with the command:
```
docker-compose down
```

Project works on [localhost:8000](http://localhost:8000/)

# Project Features

## User Registration
- Registration works on http://localhost:8000/sign-up/
- Allows users to create an account with username, email, password, and profile photo.
- Email and username uniqueness validation.
- Profile Photo Upload

## Authentication
- Login works on http://localhost:8000/sign-in/
- Allows users to log in with username and password
- Аuthentication is based on Django Session Authentication
- Secure password handling with AbstractBaseUser.

## Posts
### Get Post List
- On main page http://localhost:8000/ user can see all posts and replies.
- The default sorting is by newest. Sorting is also available by oldest, username and email
- The list of posts also supports pagination of 25 objects per page

### Create a new post/reply
- The authenticated user can create a new post or reply other post
- To create a post, you need to fill in the text field, pass the captcha, 
and add attachments (optional). Since the user is already registered, 
there is no need to confirm username or email
- Attachments files can be only JPG, GIF, PNG or TXT. TXT files are only allowed under 100kb,
images in sizes larger than 300x240px are cropped to allowed size
- Text of post supported only `<a>`, `<code>`, `<i>` and `<strong>` html tags. Other tags are deleted from text

### Likes and dislikes

- The authenticated user can like or dislike any post
- If the user has already liked the post, a second click on like will remove the like. 
If the user clicks on dislike, the like will also be removed and the dislike will be added to the post
- On the post card everyone can see the post rating. 
Rating is made up of likes subtract dislikes. Rating can be negative if dislikes more than likes

## Security

- All user inputs are validated to prevent XSS and SQL injection.
- Passwords are encrypted using Django's AbstractBaseUser.
