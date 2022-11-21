  # NOTE: 
I would like to inform you that this is my 4th portfolio project.
I havent fully finished this project yet. Unfortunately due to circumstances I am not able to deliver this project, finished, on the scheduled time. I submitted it knowing I wouldnt get a passing grade, and will continue this project whenever I can.
Thank you for understanding!

MOCKUP PICTURE

# Introduction
Surfers Paradise, a surfschool located in Queensland, Australia. A warm climate, beautiful nature and the best waves.

My goal for this project is to make it very easy for all users and visitors to make a booking for a surf lesson of choice. Being able to keep track of all bookings when logged in, update them if needed, or even to delete a booking.
Also that all necessary information is provided, like all contact information, what is included in a lesson and what times the lessons are everyday.

View my repository here - LINK
View the live application here- LINK

## Features
 #### Navigation
  - Navigationbar
  - Toggler
 #### Header
  - Image on every page
  - Header text 
  - Button directing to another page
 #### Info Section
  - On the home page
  - Informs the user about the different lessons available
 #### Booking form
  - Displays the main booking model from models.py  
  - Several fields are hidden for the user and are automatically generated and filled in before saving the form.
 #### Bookings overview
  - Displays all bookings made by the authenticated user
  - Bookings from other users are not shown
  - Option to edit the booking
  - Option to delte the booking
  - Before deletion, an alert pops up which requires input from the user, to confirm deletion of the selected booking.
  - Button to create another booking, which directs to the Booking form 
 #### Register
  - Allows the user to create an account
  - Account keeps track of all bookings
 #### Login
  - Gives the user the opportunity to log in
 #### Logout
  - Gives the user the opportunity to log out
  - Asks for confirmation before logging out
 #### Footer
  - Copyright
  - Social Media links (WORKING ON THIS)


### Features Left To Implement
- I would like to finish this readme file
- I would like to add a contact page with a map incl location
- I would like to add reviews
- I would like to add more images
- I would like to add more information about what is included in the surfing lessons
- I would like to add blogposts/news
- I would like to add a calender with all the events going on
- I would like to implement a django message after the user made, edited or deleted a booking.
- I would like to finish up the 'Forget password' page
- On the home page I would like to add pictures of the lessons of choice, and make these into a link, which would direct to a page with the specific information.

- I want to prevent the following things when making a booking:
    - Make booking in the past
    - Make more than 6 bookings at the same date and time (max p per lesson is 6)
- I want to implement this when making a booking:
    - Send an automated email confirmation with the booking details

## Testing
 - validator testing
    - html
    - js
    - css
    - python

  - lighthouse screenshot

## Bugs
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

### Unsolved bugs
- When deploying to heroku, my css file doesn't load.
- A user can now still make bookings in the past



libraries
technologies
deployment

## Credits
- [Medium](https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f) - for reminding me of the markdown codes
- [Google Translate](https://translate.google.com) - for helping me translate from Dutch to English
- [Stackoverflow]
- [w3schools]
- [GeeksForGeeks]
- [Pexels](https://pexels.com) - for the images 
- [Flexbox Froggy](https://flexboxfroggy.com/) - to help me postition divs


 ### Acknowledgments
 - My mentor Daisy for guiding me
 - Tutor support for helping me solve bugs mentioned above
 - Code Institute 
 