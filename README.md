  # NOTE: 
I would like to inform you that this is my 4th portfolio project.
I havent fully finished this project yet. Unfortunately due to circumstances I am not able to deliver this project, finished, on the scheduled time. I submitted it knowing I would probably not get a passing grade, I will continue this project whenever I can.
Thank you for understanding!

HERE COMES A MOCKUP PICTURE

# Introduction

Surfers Paradise, a surfschool located in Queensland, Australia. A warm climate, beautiful nature and the best waves.

My goal for this project is to make it very easy for all users and visitors to make a booking for a surf lesson of choice. Being able to keep track of all bookings when logged in, update them if needed, or even to delete a booking.

Also that all necessary information is provided, like all contact information, what is included in a lesson and what times the lessons are everyday.




View my repository [here](https://github.com/sharondrinkwaard/surfers-paradise)

View the live application [here](https://surfers-paradise.herokuapp.com/)

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

 - validator testing
    - html
    - js
    - css
    - python

  - lighthouse screenshot

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
 