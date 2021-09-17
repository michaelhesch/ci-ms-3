<a id="top"></a>

# Testing

[Return to Readme](/README.md)

## Table of Contents

1. [Code Validation](#test1)
2. [Functional Testing](#test2)
3. [Testing User Stories](#test3)
4. [Responsiveness](#test)
5. [Lighthouse](#test3)
6. [Issues & Bugs](#test3)

### Code Validation

The W3C Markup Validator, W3C CSS Validator, PEP8 Online and PyCharm were used to validate every page of the project to ensure there were no outstanding syntax errors in the project.  Results of those checks are documented in PDFs included in the project repository and can be accessed by following the links below.

- [W3C Markup Validator](https://validator.w3.org/nu/)
  - Due to the use of the Jinja templating language, each HTML file will produce warnings and errors when validating using the W3C Markup validator.  However, every page on the site was checked by inserting its respective code into the base.html template directly in the W3C validator, and the warnings/errors returned for each page were reviewed to ensure only Jinja related errors were returned.
  - Upon review of each page, no outside errors remain in the project that are not due to Jinja templating syntax.

- [W3C CSS Validator - Jigsaw](https://jigsaw.w3.org/css-validator/)
  - [Style.css Results](documentation/validation/MS3-CSS-Validation.pdf)
    - No warnings or errors returned when validating style.css content directly.
    - Note: multiple warnings are returned if validation is run on the deployed app due to dependencies such as Bootstrap.

- [PEP8 Online](http://pep8online.com/) - PEP8 Online is a web-based PEP8 code format compliance checker which was used to check each Python file in this app for PEP8 compliance.
  - Warnings returned for the app sub-package "__init__.py" files due to the need to import the routes package at the bottom of the file rather than the top, after the package blueprint is created.  Without this configuration the app will not work as it is not able to initalize any of the routes which depend upon the respective blueprints.  PyCharm does not produce any error or warning for this configuration.

- [PyCharm](https://www.jetbrains.com/pycharm/) - Pycharm Python IDE was used as an additional double-check on all Python code for PEP8 compliance after checking each file with PEP8 Online.
  
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
  - PASSING: Pagination working as expected - 

- User Profile & Feed
  - PASSING: Add Photo button redirects correctly - Pressing the 'add photo' button redirects user to the upload photo page.
  - PASSING: Edit Profile button redirects correctly - Pressing the 'edit profile' button redirects the user to the correct profile edit page.
  - PASSING: Like Icon displays correctly - Like icon in the profile photo feed correctly displays a blue icon if the photo was liked by the photo owner, and a gray icon if it has not.
  - PASSING: Photo details correctly displayed on card - The photo, title, description, likes count and date added are all correctly displayed on the photo feed card.
  - PASSING: Clicking photo opens correct details page - Clicking on a photo in the profile photo feed redirects the user to the correct photo's details page.
  - PASSING: Pagination working as expected - 

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

### Responsiveness

- All pages were tested for responsiveness and any visible bugs using Google Chrome developer tools to emulate the viewing size across all standard device sizes offered.  Media queries have been implemented in the CSS of the site to adjust various attributes as necessary to improve the viewing experience on small screen sizes, such as scaling social media icon sizes and adjusting button styling to remain easily usable.  In addition site rendering on very high resolutions (such as "4K" or 2160p) were checked to ensure consistent performance as expected.
  
  Device Screen Sizes Tested

  ![Devices Tested](#)

- In addition, all pages on the site were tested for correct behavior on a 27" desktop monitor, a 15.1" laptop monitor, an iPhone 11 and a 10.5" iPad Pro.  The pages scale and respond as expected for a normal user experience across these viewing sizes & devices.

### Lighthouse

- The Lighthouse tool within Chrome Developer tools was used to generate performance scores and identify areas for improvement in both mobile and desktop views of the page.  Results of this scoring can be viewed via the links below:

1. Mobile Scores:
    1. [x](#)
    1. [x](#)
1. Desktop Scores:
    1. [x](#)
    1. [x](#)

- Please note that while efforts to coprrect some defects indicated in these results are due to issues found in external dependencies, such as MDBootstrap's CSS for example, or other faults that are beyond the scope of this project to remedy.

### Issues & Bugs Encountered in Development

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

[Return to the Top](#top)
