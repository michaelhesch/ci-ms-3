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
  
#### Functional Testing

- Below are descriptions of tests undertaken on the deployed project to ensure expected behaviors of functionality.

- Registration
  - PASSING: E-Mail Address Validation - description
  - PASSING: Password Match Validation - description
  - PASSING: Empty Form Submission Validation - Form does not proceed with posting if required fields are blank.  Tested fields username, first name, last name, and password fields.  Avatar color is pre-selected by default and cannot be de-selected before submitting.
  - PASSING: Duplicate Email Cannot Register - description
  - PASSING: Default Avatar Selected - By default the form is populated with an avatar colour selected, which can be changed by the user but cannot be de-selected entirely, which is the intended behavior.
  - PASSING: Username Regex Validation - Usernames cannot contain spaces or special characters, only upper or lower case letters and numbers.  Confirmed multiple combinations of special characters and spaces in username field are returned as invalid by the form.

- Login
  - PASSING: Username Does Not Exist Validation - Form endpoint will catch mongoengine error response for a username that does not exist in the database and return a flash message to the user indicating the credentials are incorrect, but intentionally does not specify between the username or password being incorrect.  Correct login credentials are validated and result in a successful login.
  - PASSING: Incorrect Password Validation - Password validation functionality works correctly resulting in an incorrect login details flash message to the user.  This intentionally does not specify if the username or password is incorrect.

- Add Photo
  - OPEN: Description max length validation - 
  - OPEN: Title max length validation
  - PASSING: Title, Description, Photo file are required fields - 
  - PASSING: File picker works on mobile devices - Apple iPhone 11, iPad Pro 10.5 - take new photo and upload from library

- Edit Photo
  - OPEN: Description max length validation
  - OPEN: Title max length validation
  - PASSING: Edit Title - Can edit title 
  - PASSING: Edit Description - Can edit description

- Delete Photo
  - PASSING: Delete photo - Delete photo button removes photo from profile and feed
  - PASSING: Delete photo - Delete photo removes photo from Cloudinary library
  - PASSING: Delete photo - Delete photo removes photo entry from MongoDB photos collection

- Like / Unlike Photo
  - PASSING: Like photo updates correctly - Pressing 'like' button on another user's photo increases the like count by one and correctly changes the like button fill color to a solid blue background.
  - PASSING: Un-like photo updates correctly - Pressing 'like' button on another user's photo which has been liked by the current user correctly decreases the like count by one and changes the like button fill color back to the original off-white background.
  - PASSING: Like any user's photo - Pressing 'like' results in the expected behavior on any other user's photo.
  - PASSING: Like/Un-Like own photo -

- Add Comment
  - OPEN: Comment max length validation - Currently known bug exists where form validation is not working as expected.  Max length validation is working on the back-end, preventing comments exceeding the specified maximum length from being submitted to the database, however no warning is displayed to the user on the UI.  When a comment exceeding the maximum length is submitted, the page reloads however no flash message or form validation message is displayed, and no entry is made to the database.
  - PASSING: Empty Comment form submission - Comment form validation for empty comment text field prevents an empty comment from being submitted.
  - PASSING: Add comment on another user's photo - Able to post a new comment on a photo uploaded by another user without any errors.
  - PASSING: Comment sorting on photo - Newly posted comment is displayed at the top of the list of comments, as intended by design.
  - PASSING: Comment displays correct details - Username, date added and comment text are displayed correctly for newly added comment.
  - PASSING: Comment displays correct buttons - Like, Edit and Delete buttons are displayed for a newly added comment posted and owned by the logged in user.
  - PASSING: Comment on own photo - 

- Edit Comment
  - OPEN: Comment max length validation
  - PASSING: Edit button modal - Pressing the 'edit' button on a comment owned by the logged in user opens the edit comment modal, with the existing text populated in the edit field.
  - PASSING: Cancel edit button on modal - Pressing the 'cancel' button closes the modal with no changes applied to the comment.  Same behavior demonstrated for pressing 'X' button to close modal.
  - PASSING: Save changes to comment - Pressing 'save' closes the edit modal and displays the correct flash message to the user, updated text is displayed in the comment matching the text entered during editing.
  - PASSING: Updating comment on another user's photo - Update functions tested above performed without error on a comment added by the current user to another user's photo.
  - PASSING: Edited comment details correct - Edited comment displays the correct username, date added, and newly edited text value.
  - PASSING: Edited comment displays correct buttons - Edited comment displays the Like, Edit, and Delete buttons.
  - PASSING: Edit comment on own photo - 

- Delete Comment:
  - PASSING: Delete modal opens - Pressing the 'delete' button on a comment owned by the logged in user opens the delete comment modal, asking the user to confirm they wish to delete the comment.
  - PASSING: Cancel delete button on modal - Pressing the 'cancel' button closes the delete modal with no change made to the comment.  Same behavior demonstrated for pressing 'X' button to close modal.
  - PASSING: Delete comment - Pressing the 'delete' button on the modal results in the correct flash message being displayed to the user and the comment being deleted.
  - PASSING: Delete comment on own photo - 

- Like / Unlike Comment:
  - PASSING: Liking comment updates correctly - Pressing 'like' on a comment correctly updates the like count by increasing by one and changes the like button fill color to a solid blue background.
  - PASSING: Un-liking comment updates correctly - Pressing 'like' on a comment that the current user has already liked updates the like count by decreasing by one and changes the like button fill color back to the original off-white background.
  - PASSING: Ability to like any comment - Pressing 'like' results in the expected behavior on any other user's comment.
  - PASSING: Can like/un-like own comments on own photo - 

- Edit User Profile
  - OPEN: About me max length validation
  - PASSING: About Me displays correct text - After adding text to the About Me field, this correctly displays existing data
  - PASSING: Avatar Color displays correct selection - Avatar will display the correct color based on setting captured at registration or after editing.
  - PASSING: Edit Profile Go Back button works - Clicking 'go back' button returns user to the profile page
  - PASSING: Edit Profile Save Changes button updates profile - Clicking 'save changes' returns user to the profile page with updates applied

- Explore Feed
  - PASSING: Like icon display - Like icon on photo feed correctly displays blue icon if photo has been liked by the current user, and gray icon if it has not been liked.
  - PASSING: Photo card details correct - Photo cards in feed correctly display photo, photo title and total likes count.
  - PASSING: Clicking photo opens correct details page - Clicking on a photo in the feed redirects the user to the correct photo's details page.

- User Profile & Feed
  - PASSING: Add Photo button redirects correctly - Pressing the 'add photo' button redirects user to the upload photo page.
  - PASSING: Edit Profile button redirects correctly - Pressing the 'edit profile' button redirects the user to the correct profile edit page.
  - PASSING: Like Icon displays correctly - Like icon in the profile photo feed correctly displays a blue icon if the photo was liked by the photo owner, and a gray icon if it has not.
  - PASSING: Photo details correctly displayed on card - The photo, title, description, likes count and date added are all correctly displayed on the photo feed card.
  - PASSING: Clicking photo opens correct details page - Clicking on a photo in the profile photo feed redirects the user to the correct photo's details page.

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Story Testing

1. I want to understand the service the website provides before registering.

2. I want to create a new user account and be able to log in.

3. I want to easily interact with content posted by other users on the site by adding 'likes' or comments.

4. I want to easily add my own photos to the platform for other users to interact with.

#### Returning Visitor Story Testing

1. I want to easily log in to my account and access my profile.

2. I want to be able to quickly access and explore the main photo feed content.

3. I want to be able to manage the content I add to the platform - including editing or deleting my photos, comments and likes.

#### Site Owner Story Testing

1. I want to provide a streamlined registration and login experience.
  
2. I want to provide a fun and interactive experience for the user.

3. I want to encourage the user to return back to the platform to see and interact with new content.

4. I want to allow users to manage their content - adding, editing and deleting as they desire.

### Further Testing

#### Responsiveness

- All pages were tested for responsiveness and any visible bugs using Google Chrome developer tools to emulate the viewing size across all standard device sizes offered.  Media queries have been implemented in the CSS of the site to adjust various attributes as necessary to improve the viewing experience on small screen sizes, such as scaling social media icon sizes and adjusting button styling to remain easily usable.  In addition site rendering on very high resolutions (such as "4K" or 2160p) were checked to ensure consistent performance as expected.
  
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

- Please note that while efforts to coprrect some defects indicated in these results are due to issues found in external dependencies, such as MDBootstrap's CSS for example, or other faults that are beyond the scope of this project to remedy.

### Issues Encountered in Development

- [Resolved] "None" response from WTForms process_data()
- An important component of the user experience for the site is pre-populating edit fields with the existing data, so that when a user clicks 'edit', they are able to see the values they have already entered.  This applies to photo descriptions and comments in particular.
  - When attempting to render the edit modal for these features, WTForms would not return any existing value, despite multiple approaches to apply the existing database values to the form fields.  
  - A solution was found using a WTForms method called process_data(), which is passed a data object as its only argument, that resulted in existing form data rendering in the form correctly.  This method was applied in the Jinja template code for the form fields - both a StringField input field a TextAreaField textarea.
  - When using this appraoch, for reasons still unknown, process_data() returned an additional value of " None ", which was injected in-between the label field and the input field below.  Hours of troubleshooting and discussion with my mentor did not result in a solution, so a work-around was crafted.
  - This problem was solved by setting up the necessary input fields in HTML directly, and setting the default values using Jinja to access the existing data values.

- [Resolved] Masonry layout rendering

- When implementing the Masonry layout, using the Masonry JS plugin compatible with MDB / Bootstrap v5, a serious rendering issue was encountered on initial loading of a photo page.
- Due to the Masonry layout being applied to the div structure before the image files were fully loaded, the image cards would render stacked to the top of the viewable area, and overlapping each other.  Refreshing the page would result in the correct layout rendering, as Masonry could correctly set the size attributes of the divs with the image files loaded.
- After extensive investigation, a solution was found using JavaScript to initialize Masonry after all page content was loaded, so that the layout will be applied correctly every time the page is viewed.
- This solution is credited to [this codepen example](https://codepen.io/desandro/pen/MwJoZQ) and was adapted for use in this project.

- [Open] x

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

### Heroku Deployment - TBU

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
