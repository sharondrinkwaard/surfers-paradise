

# Introduction

Surfers Paradise, a surfschool located in Queensland, Australia. A warm climate, beautiful nature and the best waves.

Everyone who has ever wanted to try surfing, don't wait any longer! Take a look at this project and book your first surfing lesson. 

My goal for this project is to make it very easy for all users and visitors to make a booking for a surf lesson of choice. Being able to keep track of all bookings when logged in, update them if needed, or even to delete a booking.

Also that all necessary information is provided, like all contact information, what is included in a lesson and what times the lessons are everyday.

View my repository <strong>[here](https://github.com/sharondrinkwaard/surfers-paradise)</strong>

View the live application <strong>[here](https://surfers-paradise.herokuapp.com/)</strong>

![Mockup Screenshot](/static/images/mockup.png)

## Features
---
 ### Navigation

  - Navigationbar
  - Toggler

 ### Header

  - Image on every page
  - Header text 
  - Button directing to another page

 ### Info Section

  - On the home page
  - Informs the user about the different lessons available

 ### Booking form

  - Displays the main booking model from models.py  
  - Several fields are hidden for the user and are automatically generated and filled in before saving the form.

 ### Bookings overview

  - Displays all bookings made by the authenticated user
  - Bookings from other users are not shown
  - Option to edit the booking
  - Option to delte the booking
  - Before deletion, an alert pops up which requires input from the user, to confirm deletion of the selected booking.
  - Button to create another booking, which directs to the Booking form 

 ### Register

  - Allows the user to create an account
  - Account keeps track of all bookings

 ### Login

  - Gives the user the opportunity to log in

 ### Logout

  - Gives the user the opportunity to log out
  - Asks for confirmation before logging out

 ### Footer

  - Copyright

## Features Left To Implement
---

- I would like to add a contact page with a map incl location
- I would like to add reviews
- I would like to add more images
- I would like to add more information about what is included in the surfing lessons
- I would like to add blogposts/news
- I would like to add a calender with all the events going on
- I would like to implement a django message after the user made, edited or deleted a booking.
- I would like to finish up the 'Forget password' page
- On the home page I would like to add pictures of the lessons of choice, and make these into a link, which would direct to a page with the specific information.
- On the overview page, if there are no bookings made yet, I would like to add a message saying "You haven't made a booking yet".

- I want to prevent the following things when making a booking:
    - Make booking in the past
    - Make more than 6 bookings at the same date and time (max p per lesson is 6)
- I want to implement this when making a booking:
    - Send an automated email confirmation with the booking details

## Design
---

For the visual view of the web application, I used [WireFrame](https://mockflow.com) from Mockflow

![Wireframe1](/static/images/wireframe-1.png)
![Wireframe2](/static/images/wireframe-2.png)
![Wireframe3](/static/images/wireframe-3.png)
![Wireframe4](/static/images/wireframe-4.png)


## Planning
---
For planning this project I used a kanban board with user stories. Those are labeled with Must, Could or Should have. So it was easy to have an overview and keep track of how far the development was going.

![Kanban Board](/static/images/kanban-board.png)

When starting to set up the models.py, I created an Entity Relationship Diagram in Word.

![Entity Relationship Diagram](/static/images/ERD.png)

## Testing
---

### Validators
- No errors returned when passing through the <strong>[HTML Validator](https://validator.w3.org/nu/)</strong>.

- No errors returned when passing through the <strong>[CSS validator](https://jigsaw.w3.org/css-validator/)</strong>

- No errors but some warnings returned when passing through the <strong>[Python validator](https://extendsclass.com/python-tester.html)</strong>
As PEP8 Online is not available anymore (at least in my country) I chose this other python validator. 
The warnings it sometimes returned were not errors but simply the use of another style guide. I decided to stick to the PEP8, because I prefer this style and ignore the warnings.

- Below you can find the Lighthouse report.
  ![Lighthouse report](/static/images/lighthouse.png)


### Manual Testing - Python & JavaScript

- I tested it the project displays well in Chrome and Microsoft Edge.

- I tested if all hovers work correctly. I confirm that they indeed do by hovering over all of them.

- I confirm that this design is responsive, functions well and looks good on all standard media devices, desktop, tablet and mobile phone. I tested this by using DevTools in the Chrome browser. 

- I confirm that there are no errors or bugs in the console while using DevTools in the browswer. I tested this by opening and refreshing the websiste several times while keeping DevTools open.

- I tested if all images are being displayed correctly from Cloudinary. Previously the images were not loading. Now they do and I confirm that they indeed are all being displayed. I tested this by loading every page several times to see if the images are being displayed. 

- I confirm that the messages/alerts (JavaScript)
 are working. I tested this by logging in and out several times. Each time a messages was being displayed at the top of the page. I also checked that the message would dissappear on it's own.
- I confirm that all user stories are implemented and are fullfilled. 

Below I placed my testing sheet where all tests I have done are mentioned and the results are being displayed.

![Testing sheet](/static/images/testing_sheet_1.png)
![Testing sheet](/static/images/testing_sheet_2.png)
![Testing sheet](/static/images/testing_sheet_3.png)



## Bugs
---

### Solved bugs

  - When displaying the form on the booking page, the user could choose under which name to make a booking. So the form was displaying all the existing users in a dropdown option. Instead of just the authenticated user.
  I solved this by 
  ```
    current_user = request.user
    queryset = Booking.objects.filter(posted_by=current_user)
  ```
  - When displaying the form, I wanted to hide several model fields from the user. Those fiels were required so had to be filled in. I implemented this code by requesting the 'posted_by' field from the user and save the form afterwards.
  ```
   if form.is_valid():
      booking = form.save(commit=False)
      booking.posted_by = request.user
      booking.save()
      return redirect('overview')
  ```
  - When deploying to Heroku, all my images didn't load. I figured out this was because it is asking for another image.url than given. 
  In Cloudinary the style.css file is up to date, but when deploying to Heroku I would get an error about the collectstatic. I solved the error by linking my stylesheet with the direct Cloudinary url instead of a file path and then deploying with the config var: DISABLE_COLLECTSTATIC = 1.

### Unsolved bugs

- When deploying to heroku, my css file doesn't load.
- A user can now still make bookings in the past.
- When the user is not logged in and tries to make a booking, an server error occurs. This is because the hidden forms cannot be generated if the user is not authenticated.



## Libraries & Technologies
---
- Django DateTime
- Django Allauth
- Summernote
- Gunicorn
- Bootstrap
- Cloudinary
- Heroku
- Django Messages

## Deployment
---
1. Log in to Heroku or create an account.
2. Then, click the button labelled New from the dashboard in the top right corner and from the drop-down menu select Create New App. You must enter a unique app name.
3. Next, select your region.
4. Click on the Create App button.
5. The next page you will see is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars.
6. Click Reveal Config Vars and enter PORT into the Key box and 8000 into the Value box and click the Add button.
7. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
8. The Buildpacks must be in the correct order. If not, click and drag them to move into the correct order.
9. Scroll to the top of the page and now choose the Deploy tab.
10. Select Github as the deployment method.
11. Confirm you want to connect to GitHub.
12. Search for the repository name and click the connect button.
13. Scroll to the bottom of the deploy page and select preferred deployment type:
- Click either <strong>Enable Automatic Deploys</strong> for automatic deployment when you push updates to Github.

- Select the correct branch for deployment from the drop-down menu and click <strong>Deploy Branch</strong> for manual deployment.


## Credits
---

- [Medium](https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f) - for reminding me of the markdown codes
- [Google Translate](https://translate.google.com) - for helping me translate from Dutch to English
- [GeeksForGeeks](https://geeksforgeeks.org) - for helping me understand Django Models
- [Pexels](https://pexels.com) - for the images 
- [Flexbox Froggy](https://flexboxfroggy.com/) - to help me postition divs


 ### Acknowledgments

 - My mentor Daisy for guiding me
 - Tutor support for helping me solve the bugs mentioned above
 - Code Institute 
 