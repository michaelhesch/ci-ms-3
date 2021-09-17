<a id="top"></a>

# Milestone Project Three - "Out of Office"

![Am I Responsive Image - Placeholder](#)

## Project Overview

 The purpose of Out of Office is to provide users with a platform for sharing their favourite photos from their holidays, and interacting with other user's holiday photos.  The site provides users with the ability to create an account, log in, and then easily share their photos, view other photos, as well as manage the photos they have uploaded to the platform.  The user can also leave "likes" and comments on any photo uploaded to the platform.

- This is a full-stack web application built with Material Design Bootstrap, a Python back-end utilizing the Flask micro-framework, a MongoDB NoSQL database, Cloudinary 

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

- The page color scheme is based on the [Material Design Bootstrap colour theme](https://mdbootstrap.com/docs/standard/content-styles/colors/).

- Background color is "bg-light" (#FBFBFB), a soft off-white.  

- Highlight color is "crimson" (#E60023) found on the site logo and favicon.  

- Button call to action color is MDB "Primary" (#1266F1), used for important buttons and icons.

- The full palette containing all colors used in the site can be found [here.](https://mdbootstrap.com/docs/standard/content-styles/colors/#section-full-palette)

#### Typography

- The font used throughout the site is the Google Font 'Roboto'.  This font is included with MDB and font weights are assigned by MDB, more information on typography can be found [here.](https://mdbootstrap.com/docs/standard/content-styles/typography/#section-introduction)

- A sample of the Roboto typography from [Google Fonts](https://fonts.google.com/specimen/Roboto)

#### Imagery

- x.
- x.

### Wireframes

- Mobile Wireframes - [View](#)

- Tablet Wireframes - [View](#)

- Desktop Wireframes - [View](#)

#### Deviations from wireframe designs

- During development some changes were made to the final design that is deployed vs. the wireframes above:

  - TBU.

## Data Models

### Database Models

- The database for the site contains three collections: User, Photo and Comment.

- User

  - Contains details of the user and their account, including username, first name, last name, email address, password hash, about me text, avatar color and avatar color ID value for each user.
  - Contains an automatically generated unique ObjectId value which is used to interact with user data and serves as a reference field.

- Photo

  - Contains the identifying details for each photo including it's title, description, user who uploaded the photo, the time and date it was added, the secure Cloudinary URL for the photo, the Cloudinary public ID of the photo, number of likes, and the users who have liked the photo.
  - Contains an automatically generated unique ObjectId value used to interact with the photo and serves as a reference field.
  - Users who have liked a photo are stored as an array of ObjectIds, allowing for easy mapping between Photos and Users.

- Comment

  - Contains the identifying details for each comment, including the user who added the comment, the date and time the comment was added, the photo the comment was added to, the text content of the comment, number of likes, and the users who liked the comment.
  - Contains an automatically generated unique ObjectId value used to interact with the comment and serves as a reference field.
  - The user who added the comment is caputred using their user ObjectId, and is a reference field tied to the User collection.
  - The photo which the comment was added to is captured using its ObjectId, and is a reference field tied to the Photo collection.
  - Users who have liked the comment are stoerd as an array of ObjectIds, allowing for easy mapping between Comments and Users.

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

### Cloudinary Implementation

- This project uses Cloudinary to both manage user photo file uploads but also as a cloud hosting provider for the images displayed on the app.  Cloudinary's API also provides several very useful features that improve performance of the deployed site.
- Cloudinary also offers a range of third party add-ons that further enhance the functionality provided by Cloudinary itself.  For this project, I have enabled the Amazon Rekognition AI Moderation add-on, which provides automatic artificial intelligence-based content moderation limiting a range of inapproprite content from being posted to the deployed site.  You can read moreabout this add-on [here.](https://cloudinary.com/documentation/aws_rekognition_ai_moderation_addon)

#### Cloudinary Upload and Transformation Configuration

- Each image uploaded to the site undergoes a series of transformations to improve site performance and optimize storage space used.  These settings include:
  - Allowing Cloudinary to automatically determine the best quality settings to optimize file size while maintaining viewability.
  - Setting max height and width to 1920 x 1080px
  - Automatically cropping images while maintaining their original aspect ratio to fit this size requirement.
  - Automatically moderating content uploaded to the site with Amazon Rekognition.
- To provide essential defensive programming measures, the file types allowed both in the image upload input field as well as those accepted by Cloudinary for this project are restricted to JPG, JPEG and PNG files.

## Features

### All Pages

- Clear and concise page design, including an easy to use and responsive navigation bar and a subdued colour scheme.

- Highly contrasting logo icon on the menu bar and site favicon to draw user's attention.

- Social media links on the navbar as well as easily identifiable social media link buttons on the footer.

### Landing Page (Logged Out)

- Clear and centrally located information card describing what the site is and who it is for.

- Strongly styled call to action buttons for Login and Register to draw user's attention.

### Login Page

- Straightforward Log In card free of clutter and a strong call to action button for logging in.

- Additional link to registration page for a new user who could potentially land on the log in page without an account.

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

- There are several features that I would like to incorporate to enhance the site in the future that unfortunately could not be added for this version:
  - Photo Category & Location - in the future I would like to incorporate a category and location attribute for the photos, which would allow users to specify the type of photo they are adding as well as where it was taken.  This would also allow for additional enhancements such as filtering to be performed on the Explore feed page.
  - User account password reset - secure password resets for users who forget their password, or need to reset it for any reason, would be useful.
  - User account deletion - the ability for a user to entirely delete their account (not just the content they have added) would be beneficial to include.
  - Admin view - inclusion of a super user account which will allow for direct intervention if manual content moderation is required.
  - User follows / account views - allow users to follow each other's accounts directly and view another user's account and photos.
  - User profile photo feed enhancements - allow sorting and/or filtering of user's own photo feed to over-ride the default sort of oldest to newest.
  - Comment pagination - add in vertical collapsing/pagination of comments once many comments are added to a photo to prevent unweidly scrolling in an image details page.

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
1. [Favicon.io](https://favicon.io)
    - Favicon.io was used to generate the Favicons used for the browser tab as well as the navbar logo for the site.
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
1. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the site and provides cloud hosting for the live version of the site.
1. [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/)
    - Code snippets were referenced for styling various elements of the site, and organization of the social media links footer section.

## Testing - TBU

### Detailed testing information can be found in the testing file, [located here.](documentation/TESTING.md)

## Deployment - TBU

### Deployment Requirements

- The following accounts and software packages are required to deploy a clone of this project.  All can be obtained free of charge from the respective providers.

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

### Working With A Local Clone

1. Setup all dependencies:
   1. Change directory to the location of the local clone.
   2. Create a new Python virtual environment to ensure no conflicts occur with locally installed Python packages.  This is done with the command "python3 -m venv venv" (if needed install the Python virtual environment package with "pip install virtualenv")
   3. Launch your virtual environment with ".\venv\Scripts\activate" (on Windows, syntax will differ for other operating systems)
   4. Install all necessary dependencies for this project as specified in the requirements.txt file with the command "pip install -r requirements.txt"

2. Ensure you have a MongoDB database set up (see MongoDB Database Setup section above).
   1. Create the following collections: comment, user, and photo.

3. Configure local enviornment variables
   1. There are multiple ways to achieve this, however for this project I used an env.py file added to .gitignore - this is critically important to avoid exposing sensitive configuration data!
   2. Configure your env.py file as follows:

        ```python
            import os

            # Flask environment variables
            os.environ.setdefault("IP", "0.0.0.0")
            os.environ.setdefault("PORT", "5000")
            os.environ.setdefault("SECRET_KEY", "[your_secret_key]")
            # MongoDB environment variables
            os.environ.setdefault("MONGO_URI", "[your_mongo_uri]")
            os.environ.setdefault("MONGO_DB", "[your_db_name]")
            # Cloudinary environment variables
            os.environ.setdefault("CLOUD_NAME", "[your_cloud_name]")
            os.environ.setdefault("API_KEY", "[your_api_key]")
            os.environ.setdefault("API_SECRET", "[your_api_secretkey]")
        ```

### Heroku Deployment

Heroku deployment is fast and efficient once the project is properly configured.  Heroku needs the requirements.txt and Procfile files included in the repository for this project to deploy the application to a live environment.

If the Procfile was not cloned, this can easily be created from the terminal on Windows using "echo web: gunicorn run:app >Procfile".  Be sure to do this in the project's root directory.

The project was deployed to Heroku using the following steps, which can be followed for a local clone:

1. Log in to your Heroku account, then create a new app with a unique name.
2. For the deployment method, select GitHub, then select "Connect to GitHub".
3. After you have connected to the repository for the cloned app, you need to configure the Heroku environment variables.
4. Open the "Settings" menu and click the "Reveal Config Vars" button to view the environment variables.
5. Add all necessary variable and value pairs exactly as used in the locan environment variables file.
6. Return to the "Deploy" tab and click "Deploy Branch" (unless you opted to enable automatic deployments)
7. After the deployment process has completed, you can view your live application by clicking "View App", or navigating to the name of your app with .herokuapp.com added.

## Credits - TBU

### Code

- [Material Design Bootstrap Documentation](https://mdbootstrap.com/) : Code snippets taken from the offical MDBootstrap reference materials were used to create the layout of the site, including various text and image cards, the navigation bar, as well as utilizing the styling from MDB including the colour palette and Google Font family.

- [Python Flask Tutorial: Full-Featured Web App](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) : A multi-part YouTube coding tutorial which was referenced extensively for guidance on package structure, blueprints, object model creation and other key features of the application.  Code in this project may follow similar logical flow or format but all efforts were taken to create unique versions of these concepts.

- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) : A multi-part tutorial on Flask which was also referenced extensively for guidance on web form creation, pagination, user profiles and avatars, as well as deployment to Heroku with Gunicorn.  Again code in this project may follow similar logical flow or format but all efforts were taken to create unique solutions based on these concepts.

- [MongoEngine User Guide](https://docs.mongoengine.org/guide/index.html) : The MongoEngine guide document was referenced extensively to create the correct data queries for the MongoDB database used in this project, as the tutorials above both use SQL databases.  

- [Flask-Login User Guide](https://flask-login.readthedocs.io/en/latest/) : The Flask Login documentation was used to configure the LoginManager class used to manage user sessions in the project.  In particular, settings used for this project such setting session_protection to strong for enhanced local cookie security and reducing the default sesion timeout via PERMANENT_SESSION_LIFETIME to 12 hours (from c.31 days) were identified in this documentation.

- [WTForms Crash Course](https://wtforms.readthedocs.io/en/2.3.x/crash_course/) : The WTForms crash course was used (in addition to the general WTForms documentation) to create the object models for Users, Photos, Comments and Categories, generate the corresponding forms (in each packages respective forms.py file), valdiate form data, configure forms for enhanced security and finally generate the form element HTML in template files.

- [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/) : Code snippets were referenced from the Task Manager mini-project, as well as the guide for configuring the MongoDB database and Heroku deployment.

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
