# probiz

## Milestone Project 4 - Full Stack Development

* probiz is a fictional business consulting website that allows users to  book a service.
  
* This is my Milestone Project 4 submission for Code Institute's Diploma in Web Application Development course. Probiz is built using Django full-stack framework and uses a Relational Database. Technologies used include HTML, CSS, Javascript, Python.
  
## Live Project


[View the live project here.](https://probizz-bd3dbf6d99f9.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/Mahsak89/probiz)

# Table of Contents

## Contents

- [probiz](#probiz)
  - [Milestone Project 4 - Full Stack Development](#milestone-project-4---full-stack-development)
  - [Live Project](#live-project)
  - [Repository](#repository)
- [Table of Contents](#table-of-contents)
  - [Contents](#contents)
- [User Experience](#user-experience)
  - [User stories](#user-stories)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
- [Wireframes](#wireframes)
- [Features](#features)
  - [All Pages](#all-pages)
    - [Header \& Navigation](#header--navigation)
    - [Footer](#footer)
    - [Messages](#messages)
  - [Homepage](#homepage)
  - [All booking and editbooking Page](#booking,editbooking)
  - [Authentification Pages](#authentification-pages)
  - [User Profile Page](#user panel-page)
- [Future Features](#future-features)
- [Data Model](#data-model)
  - [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks \& Libraries](#frameworks--libraries)
  - [Storage \& Hosting](#storage--hosting)
  - [IDE \& Version Control](#ide--version-control)
  - [Other Tools](#other-tools)
  - [Testing \& Code Validation](#testing--code-validation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Code](#code)
    - [Code Institute:](#code-institute)
    - [Django:](#django)
    - [Bootstrap:](#bootstrap)
    - [Stack Overflow:](#stack-overflow)
    - [W3Schools:](#w3schools)
    - [GeeksForGeeks:](#geeksforgeeks)
    - [Youtube:](#youtube)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)


# User Experience

## User stories

| User Story ID | As a/an | I want to be able to... | So that I can... |
| --- | ----------- | ----------- | ----------- |
 | Registration and User Accounts |
| 1 |  admin | see members list | I can know the statistics of my website users |
 | 2 |  Site User | signin or signout to my account | I can book an appointment and Access my personal info |
 | 3 |  Site User  |register an account | Have a personal account and be able to see my profile |
 | 4 | Site User  | access my user profile | i can see, edit and delete my appointment |
  | booking|
 | 5 |  admin | see users' appointment lists | I can visit edit and delete appointments |
 | 6 | admin | search between user's appointment lists | I can find the user appointments I want to |
 | 7 |  admin | filter between users' appointment lists | I can access the user appointments I want to |
 | 8 | site user  |  select between the service choices | I can reserve my needed service |
 | 9 | Site User | select between the available date | I can reserve my needed service |
 | 10 | Site User | select between the time choices | I can reserve my needed service |
 | 11 | Site User | edit my booking appointment |  I can choose between updated date available and appropriate service |
 | 12 | Site User | edit my booking appointment |  I can choose a new time that is available |
 | 13 | Site User | book an appointment  | I can receive professional advice for my business |
 

 
## Design



### Colour Scheme

 --brand: #592E83;
 --dark: #092032;
 --body: #516171;
 --border: rgba(0, 0, 0, 0.08);
 --shadow: 0px 6px 30px rgba(0, 0, 0, 0.08);

### Typography

* I used Barlow font  Designed by Jeremy Tribby and if it doesnt work it will use sans-serif font


  
# Wireframes

* [View my wireframes in PDF form here](#docs/README/wireframes/wireframes.pdf).
# Features

## All Pages

- Responsive design
- Semantic HTML
- Custom CSS to give the website a cohesive and user-friendly appearance

### Header & Navigation

- Website H1 Heading
- Navigation, including links to:
  - account Options (register/ login/ logout/ userpanel)
  - online booking

### Footer

- copy write 
- written moto

### Messages

- Success message
- Info message
- Error message

## Homepage

- header
- about us
- service
- milestone
- 'Call to action' bookingonline button
- pexels Images

## booking,editbooking 
- consist of s simple form
  

## Authentification Pages
- Register/ Log In/ Log Out
- Features largely provided by Django allauth

## User pannel Page
- Default information form
- booking history
- Users must be logged in
- Users can only access their own User Profile
- delete and edit their booking


# Future Features

## Reviews Pages

### Users can view all their reviews

* Users must be logged in
* Users can only access their own reviews

## Add/ Edit/ Delete Reviews

### Add Review Page

* Edit Review Page
* Delete Review
* Users must be logged in
* Users can only access their own reviews



# Data Model



## Database Schema

The following Data models were used:

- user - stores information for each holiday let
- booking - stores information about Listing category

This diagram outlines each model's fields and illustrates the relationship between the models:

<h2 align="center"><img src="docs/README/db-schema.png"></h2>

# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
## Frameworks & Libraries

- [Django](https://www.djangoproject.com/)
  - This website is built using Django, a high-level Python web framework. Lonely House features multiple apps with model, view and template layers. I have also used Django to provide an admin view, create forms and test my website. Further features used include [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) for user authentification, Pillow for uploading images, and Crispy Forms.

## Frameworks & Libraries

- [jQuery](https://jquery.com/)
  - I used jQuery to add functionality to Bootstrap components and within my scripts.

- [Bootstrap 5](https://getbootstrap.com/) 
  - I used bootstrap throughout the site to make it responsive. The website uses Bootstrap's Containers, Grid System, Flexbox and Spacing utilities. I sourced code from the Bootstrap documentation when building the Navbar, Image Carousels, Cards and Buttons.

- [Google Fonts](https://fonts.google.com/)
  - Fonts are imported from google fonts.

## Storage & Hosting

- [Heroku](https://id.heroku.com/login)
  - Heroku is the deployment source I used for this project.

- [Github](https://github.com/)
  - Github was used to create and store the project repository.

* [Cloudinary](https://cloudinary.com/)
  - cloudinary is used to host and store static files and media.

- [ElephantSQL](https://www.elephantsql.com/)
  - ElephantSQL is used to host the website's PostgreSQL database.

## IDE & Version Control

- [Git](https://git-scm.com/)
  - Git was used as a version control in the terminal.

* [codeanywhere](https://app.codeanywhere.com/)
  * codeanywhere was used to create my files and where I wrote the code.

## Other Tools



- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome's Dev Tools were used while building the project to test responsiveness and for debugging.
- [pexels](https://www.pexels.com/)
  - Unsplash was used to source the website imagery.

- [ChatGPT](https://openai.com/blog/chatgpt/)
  - OpenAI's ChatGPT was used in part to generate servicess for business consulting.

## Testing & Code Validation

The following tools were used for testing and code validation. You can see results in the Testing section of this README.

- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

- [Coverage](https://coverage.readthedocs.io/en/7.0.1/)

- [Python Linting on Gitpod]

- [Chrome Screen Reader](https://chrome.google.com/webstore/detail/screen-reader/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en)

# Testing

- Please refer [here](docs/TESTING.md) for more information on testing of the Lonely House website

# Deployment

- Please refer [here](docs/DEPLOYMENT.md) for more information on the deployment of the Lonely House website

# Credits

## Code

### Code Institute:
  - I sourced the framework for this project from the Code Institute Boutique Ado walkthrough. I have customised my website wherever possible. My checkout, Stripe payments, webhooks and email verification are very similar to the walkthrough as I desired to focus more on making my website fit for my users goals, rather than adding any further checkout or payment functionality.

### Django:
  - I referred to the Django documentation whilst building my project. I found articles on [testing](https://docs.djangoproject.com/en/4.1/topics/testing/) and [making database queries](https://docs.djangoproject.com/en/4.1/topics/db/queries/) particularly useful.

### Bootstrap:
  - I have used Bootstrap classes throughout my project, including for layout utilities and cards. I sourced code from the Bootstrap documentation when building the navbar, image carousels, and dropdowns. These were sourced through the [Bootstrap documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)


### Stack Overflow: 
  

### W3Schools

### GeeksForGeeks

### Youtube [youtube](https://www.youtube.com/watch?v=CTrVDi3tt8o&t=366s/)
  -  I used this tutorial for djago-authentication
## Content

- [ChatGPT]
## Media
- I used Pexels for all my images
## Acknowledgements
- Thank you to the Code Institute London Community for their encouragement and technical support.

- Thank you to the tutors and staff at Code Institute for their support.
- I used help to write my readme file from lounly house

Please note this is a personal project. This website is purely for the sake of the developer's portfolio and not for public consumption.
Mahsa Khoshnoud, 2023.