<a id="top"></a>

# Milestone Project Three - "Out of Office"

![Am I Responsive Image - Placeholder](#)

## Project Overview

 The purpose of Out of Office is to provide users with a platform for sharing their favourite photos from their holidays, and interacting with other user's holiday photos.  The site provides users with the ability to create an account, log in, and then easily share their photos, view other photos, as well as manage the photos they have uploaded to the platform.  The user can also leave "likes" and comments on any photo uploaded to the platform.

- This is a full-stack web application built with Material Design Bootstrap, a Python back-end utilizing the Flask micro-framework, a MongoDB NoSQL database, 

[View the live project here.](https://ci-ms-3-mh.herokuapp.com/)

---

## Table of Contents

1. [User Experience](#test1)
    1. [User Stories](#test1a)
    2. [Design](#test)
2. [Data Models](#test2)
    1. [Database Models](#test)
    2. [MongoDB Database Setup](#test)
3. [Features](#test3)
    1. [Test](#test)
4. [Technologies Used](#test)
    1. [Programming Languages](#test)
    2. [Frameworks, Libraries & Programs](#test)
5. [Testing](#test3)
    1. [Test](#test)
6. [Deployment](#test3)
    1. [Requirements](#test)
    2. [Making a Local Clone](#test)
    3. [Heroku Deployment](#test)
7. [Credits](#test3)
    1. [Code](#test)
    2. [Content](#test)
    3. [Media](#test)
    4. [Acknowledgements](#test)

## User Experience (UX) - TBU

### User stories

#### First Time Visitor Goals

- As a first time visitor

  - I want to understand the service the website provides before registering.

  - I want to create a new user account and be able to log in.

  - I want to easily interact with content posted by other users on the site by adding 'likes' or comments.

  - I want to easily add my own photos to the platform for other users to interact with.

#### Returning Visitor Goals

- As a returning visitor

  - I want to easily log in to my account and access my profile.

  - I want to be able to quickly access and explore the main photo feed content.

  - I want to be able to manage the content I add to the platform - including editing or deleting my photos, comments and likes.

#### Site Owner Goals

- As the site owner

  - I want to provide a streamlined registration and login experience.
  
  - I want to provide a fun and interactive experience for the user.

  - I want to encourage the user to return back to the platform to see and interact with new content.

  - I want to allow users to manage their content - adding, editing and deleting as they desire.

### Design - TBU

#### Colour Scheme

- The page color scheme is based on x.

- Background color  .  

- Highlight color .  

- Button call to action color.

- The full palette containing all colors used in the site can be found [here.](#)

#### Typography

- The font used throughout the site is the Google Font 'x'.

- A sample of the X typography from [Google Fonts](#):

  ![TBU](#)

#### Imagery

- x.
- x.

### Wireframes

- Mobile Wireframes - [View](#)

- Tablet Wireframes - [View](#)

- Desktop Wireframes - [View](#)

#### Deviations from wireframe designs

- During development some small changes were made to the final design that is deployed vs. the wireframes above:

  - TBU.

## Data Models

### Database Models

- The database for the site contains four collections: User, Photo, Comment and Category.

- User

  - Contains details of the user and their account, including username, first name, last name, email address, password hash, about me text, avatar color and avatar color ID value for each user.
  - Contains an automatically generated unique ObjectId value which is used to interact with user data and serves as a reference field.

- Photo

  - Contains the identifying details for each photo including it's category name, title, description, user who uploaded the photo, the time and date it was added, the secure Cloudinary URL for the photo, the Cloudinary public ID of the photo, number of likes, and the users who have liked the photo.
  - Contains an automatically generated unique ObjectId value used to interact with the photo and serves as a reference field.
  - Category name is a reference field tied to the Category collection and set when a user uploads a photo.
  - Users who have liked a photo are stored as an array of ObjectIds, allowing for easy mapping between Photos and Users.

- Comment

  - Contains the identifying details for each comment, including the user who added the comment, the date and time the comment was added, the photo the comment was added to, the text content of the comment, number of likes, and the users who liked the comment.
  - Contains an automatically generated unique ObjectId value used to interact with the comment and serves as a reference field.
  - The user who added the comment is caputred using their user ObjectId, and is a reference field tied to the User collection.
  - The photo which the comment was added to is captured using its ObjectId, and is a reference field tied to the Photo collection.
  - Users who have liked the comment are stoerd as an array of ObjectIds, allowing for easy mapping between Comments and Users.

- Category

  - Contains the names of categories which can be selected from when a user adds a new photo to the platform.
  - Contains an automatically generated unique ObjectId value used to interact with the category and serves as a reference field.

### Database Schema Diagram

![database schema diagram]()

### MongoDB Database Setup

- This project uses MongoDB as it's database solution.  The setup process for creating the database follows the general guidelines provided by the Code Institute Full-Stack program's Task Manager mini-project.  An outline of the steps needed to re-create the database from the beginning are as follows:

  - Log in to MongoDB (or create a free account if needed)
  - Create new shared cluster with Amazon AWS as the cloud provider
  - Select region closest to you (in this project, region is Ireland)
  - Under cluster tier, select M0 free cluster tier
  - Additional Settings can be left as default
  - Select desired cluster name
  - Wait for cluster to be provisioned, then click 'Connect'
  - Select 'Python 3.6 or later' and copy the connection string provided
  - Set necessary environment variables in Python environment, both local git-ignored configuration and Heroku deployment environment

## Features

### All Pages

- Clear and concise page design, including a simple and responsive navigation bar and a subdued colour scheme.

- Social media links on the navbar as well as easily identifiable social media link buttons on the footer.

### Landing Page (Logged Out)

- Tbu.

### Login Page

- Tbu.

### Registration Page

- Tbu.

### Explore Page

- Tbu.

### Add Photo Page

- Tbu.

### Profile Page

- Tbu.

### Edit Content Views

- Edit Profile
- Edit Photo
- Edit Comment

### Delete Conntent Views

- Delete Photo
- Delete Comment

### Future Improvements

- Future release features

## Technologies Used

### Programming Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python 3.9.6](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - The Flask micro-framework for Python was used to build the back-end for the site.  In addition to the main Flask framework, several Flask extensions were used as well, including:
        - [MongoEngine](https://docs.mongoengine.org/): Mongoengine is an Object-Document Mapper for Python and MongoDB and was used to interact with the databse in this project.
        - [Login](https://flask-login.readthedocs.io/en/latest/): The LoginManager class was used to handle permissions and manage sessions for users.
        - [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/): Werkzeug was used to generate and check user password hash values used during registration and login.
        - [WTForms](https://flask-wtf.readthedocs.io/en/0.15.x/): WTForms was used to provide forms for the various user input components of the page, as well as providing CSRF protection.
        - [Gunicorn](https://docs.gunicorn.org/en/stable/): Gunicorn "Green Unicorn" was used as the web server for the production deployment on Heroku and is more robust than the Flask development server.
1. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - The Jinja templating engine was used throughout the site to enable template-based delivery of the front end content.
1. [MongoDB](https://www.mongodb.com/)
    - MongoDB was used as the database provider, providing a fast and efficient NoSQL database solution for this project.
1. [Cloudinary](https://cloudinary.com/)
    - Cloudinary proivdes the image upload, transformation and cloud hosting services needed for the site to function properly.  In addition, I have enabled a Cloudinary add-on called Rekognition AI Moderation by Amazon which provides automatic content moderation and protection against inappropriate content using deep learning algorithms.
1. [Material Design Bootstrap (MDB)](https://mdbootstrap.com/)
    - Material Design for Bootstrap v5 was used to add responsiveness and provide a simplified grid construction method.  MDB also provided access to many standardized components with a clean design which served as building blocks for many elements of the site.
1. [Masonry](https://masonry.desandro.com/)
    - Masonry layout was used to render the photo cards to create a unique visual style in the 'Explore' and 'Profile' pages.  This is achieved using a combination of JavaScript and CSS properties applied to the container for the photo sections.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts are included with MBD, and this project uses the Roboto font family throughout the site.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome icons are included with MDB, and this project uses the provided icons to provide simple, user-friendly ways to interact with different aspects of the site's functionality.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the design wireframes used to outline the webpage before development.
1. [dbdiagram.io](https://dbdiagram.io/home)
    - This tool was used to create the database schema visualization found in the Database Model & Schema section above.
1. [GIMP:](https://www.gimp.org/)
    - GIMP (GNU Image Manipulation Program) is a free and open source image editor, used to resize and adjust the images used on the site for better performance.
1. [Visual Stuido Code:](https://code.visualstudio.com/)
    - Visual Stuido code was used as the desktop development IDE for the project, managing the code and assets for the page during development.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Windows command prompt/terminal interface to commit and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from the local development machine using Git.
1. [Heroku](https://id.heroku.com/login)
    - Heroku was used to deploy the site and provides hosting for the live version of the site.
1. [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/)
    - Code snippets were referenced for styling various elements of the site, and organization of the social media links footer section.

## Testing - TBU

### Code Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.  Results of those checks are documented in PDFs included in the project repository and can be accessed by following the links below.

- [W3C Markup Validator](https://validator.w3.org/nu/)
  - [x Results](#)
    - No warnings or errors returned.
  - [x Results](#)
    - No warnings or errors returned.

- [W3C CSS Validator - Jigsaw](https://jigsaw.w3.org/css-validator/)
  - [Style.css Results](#)
    - No warnings or errors returned.

- [Pycharm](https://jshint.com/) - Pycharm was used to check Python code for PEP8 compliance.
  
#### JSHint Warning: Three undefined variables

1. X


#### JSHint Warning: Four Unused variables

1. X

### Function Testing

The site contains X functions which are used to implement the dynamic functionality of the page in various ways.  During development and upon completion of the project, testing was undertaken to ensure these functions are behaving as designed.

Each function was tested with the extensive use of ```console.log()```, often in multiple places within the same function, to confirm that the expected behavior was happening through each step of the function as well as at the end result.  This testing was essential to the development of this site, as several functions take in parameters from others, so confirming the output of each function was correct was All ```console.log()```s have been removed from the deployed project.

During the development process when functions were not working as expected or intended, the debugger in the Chrome Developer Tools was used to set break points and step through functions to troubleshoot and resolve issues.  This was very helpful in identifying where an issue was being created.

After deploying the site, additional checks were performed to ensure all functions are behaving as expected by selecting every option and clicking every button on the site, particularly on the map generation page.  This included selecting options and clicking items out of the normal logical order to make sure that no bugs exist in the deployed version of the site.

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Story Testing

1. I want to learn about the service offered by Mappy and how it can help plan my trip.
    1. The landing page provides a clear description of what is offered by the service centered in the page upon loading. [View Screenshot](#)

2. I want to easily access the map making tool without any confusing steps.
    1. The "Build your map" button is presented in the the middle of the page and is clearly defined from the background and surrounding content. [View Screenshot](#g)

3. I want to learn valuable information about potential destinations from the map making tool.
    1. The map making tool allows quick and easy access to city information by displaying it immediately when a map is generated.  Details about each city are easy to access by clicking one button. [View Screenshot](#)

#### Returning Visitor Story Testing

1. I want to be able to quickly return to the map making tool.
    1. The "Build your map" button launches the map creation tool in one click from the landing page, allowing a returning user to very easily access the tool.  Alternatively this page can be bookmarked and accessed directly by a returning user. [View Screenshot](#)

2. I want to easily generate new maps to meet my needs.
    1. Once on the map creation page, new maps can be generated with one click of the "create your travel map" button at the top of the page.  This can be done until the user obtains a combination they are satisfied with. [View Screenshot](#)

3. I want to see different results each time I generate a new map.
    1. Results are randomized each time a new map is generated, so new results will be returned each time a user generates a map. [View Screenshot](#)

#### Site Owner Story Testing

1. I want to create incentive for user's to interact with the map making tool.
    1. The free, easy to use service provided by Mappy to help users improve their travel experiences creates incentive to use the site.

1. I want to provide a pleasant and easy to use to the user experience.
    1. The subdued color palette, clean design aesthetic and easy to use navigation controls provide this to the user.

1. I want to provide value to the user through the information provided in the service.
    1. Details about each city included as well as points of interest across multiple categories for each city provide users with valuable insights into new cities.

1. I want the user to want to come back to use the map making tool in the future.
    1. The ability to get new results quickly and easily with the map generation tool provides users with incentive to return to plan their future travel around Ireland.

### Further Testing

#### Responsiveness

- All pages were tested for responsiveness and any visible bugs using Google Chrome developer tools to emulate the viewing size across all standard device sizes offered.  Media queries have been implemented in the CSS of the site to adjust various attributes as necessary to improve the viewing experience on small screen sizes, such as scaling social media icon sizes and adjusting button styling to remain easily usable.
  
  Device Screen Sizes Tested

  ![Devices Tested](#)

- In addition, all pages on the site were tested for correct behavior on a 27" desktop monitor, a 15.1" laptop monitor, an iPhone 11 and a 10.5" iPad Pro.  The pages scale and respond as expected for a normal user experience across these viewing sizes & devices.

#### Lighthouse

- The Lighthouse tool within Chrome Developer tools was used to generate performance scores and identify areas for improvement in both mobile and desktop views of the page.  Results of this scoring can be viewed via the links below:

1. Mobile Scores:
    1. [x](#)
    1. [x](#)
1. Desktop Scores:
    1. [x](#)
    1. [x](#)

- Please note that while efforts to coprrect some defects indicated in these results are due to issues found in external dependencies, such as Bootstrap's CSS, the Mapbox library, the HTTP version configured in the GitHub Pages server that the site is deployed on, etc. or other faults that are beyond the scope of this project to remedy.

### Issues Encountered in Development

- [Resolved] x

- x
  - x
  - x

- [Open] x

    -[Partial Solution] x

    ```javascript

    ```

- [Open] x


## Deployment - TBU

### Deployment Requirements

1. GitHub Account
2. MongoDB Account
3. Heroku Account
4. Python 3.9.6

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/michaelhesch/ci-ms-3/)
2. Under the repository name, click "Code", then select the clipboard icon under "Clone with HTTPS" to copy the link.
3. Open Git Bash
4. Change the current working directory to the location where you want the cloned directory.
5. Type `git clone`, and then paste the URL you copied in Step 2 in place of the URL in quotes below.

    ```git

    # git clone "https://github.com/YOUR-USERNAME/YOUR-REPOSITORY"
    
    ```

6. Press Enter. Your local clone will be created.

    ```git
    
    # git clone "https://github.com/YOUR-USERNAME/YOUR-REPOSITORY"
    > Cloning into `Test-Clone`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    
    ```

[Click Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to visit GitHub Help for more detailed explanations of the cloning process.

### Heroku Deployment

The project was deployed to Heroku using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/michaelhesch/ci-ms-3/)
2. From the Repository menu, select "Settings" at the far right of the menu bar.
3. Scroll down the Settings page and select the "Pages" option.
4. Under "Source", click the dropdown and select "Main" to select the main branch of the project.  Press "save".
5. The page will automatically refresh.
6. The site has now been published and GitHub will display the [link](https://michaelhesch.github.io/ci-ms-3/) in a green box.

## Credits - TBU

### Code

- [Material Design Bootstrap Documentation](https://mdbootstrap.com/) : Code snippets taken from the offical MDBootstrap reference materials were used to create the layout of the site, including various text and image cards, the navigation bar, as well as utilizing the styling from MDB including the colour palette and Google Font family.

- [Python Flask Tutorial: Full-Featured Web App](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) : A multi-part YouTube coding tutorial which was referenced extensively for guidance on package structure, blueprints, object model creation and other key features of the application.  Code in this project may follow similar logical flow or format but all efforts were taken to create unique versions of these concepts.

- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) : A multi-part tutorial on Flask which was also referenced extensively for guidance on web form creation, pagination, user profiles and avatars, as well as deployment to Heroku with Gunicorn.  Again code in this project may follow similar logical flow or format but all efforts were taken to create unique solutions based on these concepts.

- [MongoEngine User Guide](https://docs.mongoengine.org/guide/index.html) : The MongoEngine guide document was referenced extensively to create the correct data queries for the MongoDB database used in this project, as the tutorials above both use SQL databases.  

- [Flask-Login User Guide](https://flask-login.readthedocs.io/en/latest/) : The Flask Login documentation was used to configure the LoginManager class used to manage user sessions in the project.  In particular, settings used for this project such setting session_protection to strong for enhanced local cookie security and reducing the default sesion timeout via PERMANENT_SESSION_LIFETIME to 12 hours (from c.31 days) were identified in this documentation.

- [WTForms Crash Course](https://wtforms.readthedocs.io/en/2.3.x/crash_course/) : The WTForms crash course was used (in addition to the general WTForms documentation) to create the object models for Users, Photos, Comments and Categories, generate the corresponding forms (in each packages respective forms.py file), valdiate form data, configure forms for enhanced security and finally generate the form element HTML in template files.

- [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/) : Code snippets were referenced from the Task Manager mini-project, as well as the guide for configuring the MongoDB database.

- [README Template](https://github.com/Code-Institute-Solutions/SampleREADME) : Template for the README.md file for this project was sourced from Code Institute.


### Content

- All static text content (such as landing page text and page descritiptions) was written by the developer.  In addition, demonstration user accounts were created to populate image and comment data to the site for demo purposes, written by the developer.

- All other user content, such as photos, photo descriptions, user profile details, and photo comments added are created by the respective user who added them.

### Media

- Images uploaded by the developer for demonstration purposes were sourced externally from searching for 'travel' on royalty free images sites [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/).

- Additional images may be provided by users from their own image libraries, no copyright or ownership is implied by displaying these images.

### Acknowledgements

- My Code Institute Mentor Aaron for helpful feedback on my ideas prior to development and guidance throughout the project.

[Return to the Top](#top)
