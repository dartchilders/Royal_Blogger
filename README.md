# Royal Blogger Blog Site

# Project Overview

**Royal Blogger** will be an blogging application (created with seperate Django and Vue projects) that will allow users to login, create blogs in typed, video and picture formats, edit, delete blog posts as well as logout of the application. Additionally, users will also be able to leave comments and likes on other users' blog posts. Royal Blogger will utilize a variety of frameworks and libraries, including Django, Python, HTML, the GraphQL API and CSS for style.

# Features

Here, we will walk through the application from the user's perspective and list the feautres of the Royal Blogger application.

## User Story 1

"As a **blog poster**, I want **to be able to log into the blog site, write my own blog posts, have the ability to edit and delete them as well as have the ability to upload video blogs and pictures** because **I want to be able to record and share my activities and adventures**."

### Tasks:

- Create main page and allow users to login.
- Create form which allows the user to submit their blog title, post, location and date/time of post.

## User Story 2

"As a **blog reader**, I want **to be able to read other people's blog posts and have the ability to leave comments and likes if I choose** because **I like being able to read and learn about their activities and adventures**."

### Tasks:

- Create input boxes for comments and like buttons on each post.

# Schema (Data Models)
```
Profile:
    user = models.onetoonefield
    bio = models.charfield
    website = models.urlfield
    
Post:
    title = models.charfield
    subtitle = models.charfield
    body = models.textfield
    date_created = models.datetimefield
    date_modified = models.datetimefield
    author = models.foreignkey
    tags = models.manytomanyfield
    
Tag:
    name = models.charfield
    
```
# Schedule

## Week 1
- Create Django project
- Create models
- Get garden hose connected/working properly
- Create pages for login, register, authorized/unauthorized users

## Week 2
- Learn and implement GraphQL API
- Use vue to make front-end work
- Add video and picture upload functionality
- Add basic CSS styling

## Week 3
- Prepare for presentaion
- Finalize CSS styling

# Must Haves/Should Haves and Can Haves

## Must Haves
- Users
- Login/register page
- Funcationality to add/edit/delete/comment on and like blog posts

## Should Haves
- Decent CSS styling
- Garden hose connected/working properly

## Can Haves
- Functionality to upload videos and pictures 
