# Gallery

This python/django web-app was created in order to display my images in a gallery format.Developed during Moringa Core. This is Week 8's Independent Project.
Date: 2nd November 2018
By: Donald Kiplagat

## Description
This web-app allows the user to view teh admin's images while allowing the admin to add the images according with the following attributes: Location and Category.

## Setup/Installation Requirements
* Live site can be accessed from the following link https://gallery-donald.herokuapp.com/
* Pre-configured Admin details are:
Password: halowars54611
Username: donaldkiplagat

### Known Bugs
Copy button comes out of modal in smaller screen sizes.

### Behaviour Driven Development
* The program should return all images on the home page<br>
Given:All images<br>
When: Url is changed to home page<br>
Then: All Images are displayed<br>

* Modal should be displayed when the user clicks on any image and have the image's details<br>
Given:An image<br>
When: User cicks on the image <br>
Then: A modal with the image's details is displayed<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>


### Technologies Used
* Atom was the source code editor of choice.
* Git and Github were used as my local and online repositories respectively.
* Flask was used as the micro-framework
* Heroku was used in deploying the live site
* Gmail was used as the email sender


### Support and contact details
* Contact me through my email: donald.k.kiplagat@gmail.com
* The source code is also contained within the folder containing this ReadMe with comments on the code thus third-party support can be offered.

### License
Moringa School
Copyright (c)2018 **Blog by Yours Truly-Donald Kiplagat**
