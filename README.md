# Milestone Project Three - TBD

## THIS PROJECT IS A WORK IN PROGRESS
### Expected completion: 16 Septebmer, 2021
Please check back for the fully functional "production" version of the project, including the detailed Readme documentation.
The current work-in-progress version of the live application can be viewed [here.](https://ci-ms-3-mh.herokuapp.com/auth/login)

This is a full stack web application featuring a back-end developed using Python and the Flask micro framework, featuring additional technologies such as Cloudinary, and a responsive design built with Material Design Bootstrap.
---

![Am I Responsive Image - Placeholder](#)

## TBU
 The purpose of #### is to provide users with a custom generated map of cities to visit in Ireland, along with selected points of interest for each city.  The tool will generate a randomized list of cities including two, three or four primary destinations as results, based on the user's selection.  The user can then drill down into each destination to view a list of selected points of interest, which they can then filter by 'cateogry' to further refine their trip.

[View the live project here.](#)

---

## User Experience (UX) - TBU

### User stories

#### First Time Visitor Goals

- As a first time visitor

  - I want to x.

  - I want to x.

  - I want to x.

#### Returning Visitor Goals

- As a returning visitor

  - I want to x.

  - I want to x.

  - I want to x.

#### Administrator Goals

- As the site administrator

  - I want to x.

  - I want to x.

  - I want to x.

#### Site Owner Goals

- As the site owner

  - I want to x.

  - I want to x.

  - I want to x.

  - I want the x.

### Design - TBU

#### Colour Scheme

- The page color scheme is based on subdued green, gray-green and orange tones.  The theme is meant to reference variatiosn of the colors of the Irish flag.

- A light neutral gray-green background color [#F6F5F3] was selected to create a clean and simple backdrop which would not distract from the content of the page.  

- Orange [#B55224] was used as the highlight color only to clearly draw the user's attention to a hover over or click on a clickable selection.  

- Shades of green were employed for the navigation bar [#3C503D], the footer [#3C503D], button backgrounds [#BACBBB] and content containers [#E2E9E2].

- Primary colour palette selected for the site from [Coolors](https://coolors.co/):

    ![Colour Palette](#)

- The full palette containing all colors used in the site can be found [here.](documentation/MappyPalette.pdf)

#### Typography

- The font used throughout the site is the Google Font 'Open Sans' which is a clean and simple font style that is easy to read across font sizes.  This font was selected to further build a clean and simple aesthetic across the content on the site.  Sans-serif serves as the backup to Open Sans if it fails to load.

- A sample of the Open Sans typography from [Google Fonts](#):

  ![OpenSans](#)

#### Imagery

- The landing page is largely text based, but features a distinct image carousel which displays a series of images of cities included in the Mappy generation database.  This aims draw the user's attention and create excitement for visiting cities included when using the tool.
- The map generation page utilizes a stacked arrangement for the primary map and secondary map, which is not displayed until the user engages with the top map.  A plain map of Ireland is displayed upon loading the map page to draw the user's attention and encourage them to engage with the tool.

### Wireframes

- Mobile Wireframes - [View](#)

- Tablet Wireframes - [View](#)

- Desktop Wireframes - [View](#)

#### Deviations from wireframe designs

- During development some small changes were made to the final design that is deployed vs. the wireframes above:

  - Removal of the "Print Map" button & associated feature.  This was removed to reduce complexity for the initial release of the page, this may be added in through a future update.

  - Addition of coloured "tile" background to hold the map output and map drilldown output content.  This was added to give some additional visual focus to the main content a user will interact with on the page, and to distinguish the maps and associated details from the background of the site.

  - Added headings to the top map section and the details map below, which is updated dynamically to show the name of the city a user has selected.

## Features

- All Pages

  - Clear and concise page design, including a simple and responsive navigation bar.

  - A sticky footer with easy to identify social media links.

- Landing Page

  - Easy to read overview of the functionality provided by Mappy.

  - Image carousel with enticing images of different cities in Ireland.

  - Distinct button on the landing page to launch the map creation tool.

- Map Creation Tool Page

  - Clear and uncluttered layout with simple to use controls.

  - Easy to read maps and clearly identifiable details on points of interest.

  - Randomized results which display new data each time a map is generated.

  - Easy to filter points of interest data to show only a specific type of attraction to the user.

## Technologies Used - TBU

### Programming Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](#)

### Frameworks, Libraries & Programs Used

1. [Flask](#)
    - x.
1. [MongoDB](#)
    - x
1. [Bootstrap 5.0.1](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    - Bootstrap was used to add responsiveness and provide a simplified grid construction method.  In addition I utilized Bootstrap to create a sticky footer bar and image carousel for the site's landing page.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Open Sans' font into the style.css file which is used as the default on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add a visual identifier icon for the type of point of interest for the maps page, and for the social media links found in the footer of all pages.
1. [Coolors:](https://coolors.co/)
    - Used Coolors to select the color palette for the page.  Selected color palette can be viewed [here](https://github.com/michaelhesch/ci-ms-2/tree/master/documentation/MappyPalette.pdf).
1. [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/)
    - Code snippets were referenced for styling various elements of the site, and organization of the social media links footer section.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the design wireframes used to outline the webpage before development.
1. [GIMP:](https://www.gimp.org/)
    - GIMP (GNU Image Manipulation Program) is a free and open source image editor, used to resize and adjust the images used on the site for better performance.
1. [Visual Stuido Code:](https://code.visualstudio.com/)
    - Visual Stuido code was used as the desktop development IDE for the project, managing the code and assets for the page during development.
1. [JSHint / JSHint Plugin:](https://jshint.com/about/)
    - The JSHint website was used to validate the JavaScript code.  In addition, the JSHint VS Code plugin was utilized throughout the development process to help catch typographic errors and other potential issues as code was being written.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Windows command prompt/terminal interface to commit and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from the local development machine using Git, as well as host the page using GitHub Pages.

## Testing - TBU

### Code Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.  Results of those checks are documented in PDFs included in the project repository and can be accessed by following the links below.

- [W3C Markup Validator](https://validator.w3.org/nu/)
  - [Index.html Results](#)
    - No warnings or errors returned.
  - [Map.html Results](#)
    - No warnings or errors returned.

- [W3C CSS Validator - Jigsaw](https://jigsaw.w3.org/css-validator/)
  - [Style.css Results](#)
    - No warnings or errors returned.

- [JSHint JavaScript Validator](https://jshint.com/) - JSHint web version produces warnings when validating the code, while the IDE plug-in version of JSHint used during development returns no outstanding warnings.  This difference is due to the web version lacking the full context of references to outside files, functions called from HTML, etc.  During testing no unexpected behavior or bugs have been detected related to these warnings.  Descriptions of the outstanding warnings can be found below:
  
#### JSHint Warning: Three undefined variables

1. X

2. X
3. X

#### JSHint Warning: Four Unused variables

1. X

2. X

3. X

4. X

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
    1. [Home Page](#)
    1. [Map Generation Page](#)
1. Desktop Scores:
    1. [Home Page](#)
    1. [Map Generation Page](#)

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

### Heroku 

The project was deployed to Heroku using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/michaelhesch/ci-ms-3/)
2. From the Repository menu, select "Settings" at the far right of the menu bar.
3. Scroll down the Settings page and select the "Pages" option.
4. Under "Source", click the dropdown and select "Main" to select the main branch of the project.  Press "save".
5. The page will automatically refresh.
6. The site has now been published and GitHub will display the [link](https://michaelhesch.github.io/ci-ms-3/) in a green box.

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

## Credits - TBU

### Code

- [Code Institute Full-Stack Developer Course](https://www.codeinstitute.net/) : Code snippets were referenced for styling various elements of the site, and organization of the social media links footer section.

- [README Template](https://github.com/Code-Institute-Solutions/SampleREADME) : Template for the README.md file for this project was sourced from Code Institute.

- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/components/carousel/) : Code snippets taken from the offical Bootstrap reference materials to create the image carousel featured on the landing page for the site.

- [w3schools.com - Bootstrap:](https://www.w3schools.com/bootstrap4/default.asp) : Referenced w3schools materials on JavaScript to review & learn more about certain JavaScript function methods (array filtering, for example).  Also utilized to review additional documentation on CSS as well as Bootstrap features, in addition to the Bootstrap documentation.

- [X](#) : x


### Content

- All text content excluding city and location information was written by the developer.  

- City and points of interest descriptions were sourced from Wikipedia or Google Maps location descriptions.

- Map locations and points of interest were selected by the developer for demonstration purposes.  In a real-world scenario this data would be returned in a JSON response from a data service.

### Media

- All Images were sourced externally, from Wikipedia or are royalty free images from Pixabay.  Specific image credits below:

- Landing page carousel image credits:

    1. x

### Acknowledgements

- My Code Institute Mentor Aaron for helpful feedback on my ideas prior to development and guidance throughout the project.
