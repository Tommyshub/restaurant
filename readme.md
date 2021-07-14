# The Greenhouse

### User stories

As a customer of the restaurant i want,

- to order food to be delivered to my door.

- to be able to create an account.

- to be able to store my default delivery information.

- to be able to change my default delivery information.

- be able to view information about the food.

- be able to contact the restaurant to ask about my order.

As a restaurant owner I want,

- to have a menu where my customers can view and order food.

- my customers to be able to create a account.

- to be able to view my customers contact information.

- my customers to be able to update their default delivery information.

- my customers to be able to give tips to the delivery people.

- customers to be able to contact us.

- my customers to be able to view their past order.

- my customers to have a good checkout experience.

- the website to look professional so that my customers feel safe ordering from us.

## Requirements and Expectations

- The home view should be rendered directly when a customer enters the webpage, it would be very embarrassing if I somehow used the base template for this.

- The responsiveness of the website needs to be good.

- The website needs to be secure and look professional so that the customers feel comfortable using their credit cards on it.

- Navigation should be easy to understand.

- Users should get feedback from their actions, for example by a toast message.

- It should be easy to create accounts, for example by using google to signup.

- It should be easy for the users to retrieve lost passwords.

- It should be easy to contact the site owner in case of problems with orders.

## Design

### Wireframes

I used figma to create the wireframes but sadly my computer broke and I lost the original files so the ones included today has been created after the project was done. I did try to create them similar to how I made them from the start but I added things that I knew was there in the finished project, for example the logo.

[Mobile Wireframe](https://github.com/Tommyshub/restaurant/blob/main/static/wireframes/thegreenhouse-mobile-wireframe.fig.fig)

[Desktop Wireframe](https://github.com/Tommyshub/restaurant/blob/main/static/wireframes/thegreenhouse-desktop-wireframe.fig)

[Mobil Wireframe Image](https://github.com/Tommyshub/restaurant/blob/main/static/wireframes/mobile-wireframe.png)

[Desktop Wireframe Image](https://github.com/Tommyshub/restaurant/blob/main/static/wireframes/desktop-wireframe.png)

### Choice of project and design

I decided to create a project that I thought was a bit easier to create and I took something that was a bit similar to the Boutique Ado project.
I did this because I knew I would not have too much time to create this and I wanted to make sure I had time enought to finish what I started.

I did not like how the navbar from the materialize css framework looks or functions so I decided to create one from scratch, I think it worked out pretty well but it did take longer then I originally expected.

I also decided to keep the rest of the design fairly simple because I often question my taste and spend a lot of time obsessing over small things.

I think that the it worked out prettty well with the gray navbar and a white background but with a little bit of color added in terms of the logo and buttons.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

## Tools & frameworks

- [Django](<https://en.wikipedia.org/wiki/Django_(web_framework)>)

- [Materialize CSS](https://materializecss.com/)

- [Git](https://git-scm.com/)

- [Google Fonts](https://fonts.google.com/)

## Testing

## Testing User Stories from User Experience (UX) Section

Some of the wants of the restaurant owner is the same as the customers wants so I will not go over them twice here.

Customer wants:

1. Can the customers order food to be delivered to their door?

Yes, the customers are able to order food if they register for an account at the greenhouse. The MENU/ORDER tab in the navigation bar and the shopping cart icon makes it clear for the users that they can order food to be delivered.

2. Can the customers create an account?

Yes, this is made clear by having login and registration links in the navbar, but also by requiring the users to either login or register for an account if they want to do things such as adding menu items to their shopping cart.

The authentication system was created with help of django allauth and I made it easier for the users to signup for an account with google.

3. Can the users store their default delivery information?

Yes, they can do this by checking the box for "save this delivery information to my profile" during the checkout process or they can go to their profile and manually add it before creating an order. They can also change the delivery information on their profile if needed.

4. Can the users view information about the orders they have made?

Yes, the customers will receive a confirmation email when an order is created and they can also view past order on their profile at any time.

5. Can the users contact the restaurant to ask about their order?

Yes, at the bottom of the home / index page there's a question if the users wants to contact the restaurant with a link to the contact page.

Restaurant owners wants:

1. Is there a place for the users to give tips to the delivery people?

No, I decided to change this to be coupon codes instead.

2. Can the users apply coupon codes?

Yes, if the user have access to a coupon code they can use this during the checkout process, it is valid for one time use and used coupon codes will be stored and associated with the person who used it. The restaurant owner can create, modify and delete coupon codes in the admin panel.

3. Will the customers have a good checkout experience?

Yes, the checkout experience should be pretty straightforward for the users and I have found no bugs during the checkout process as of yet.

4. Is the website secure and professional looking?

Yes, the website looks professional and it is secure, there were some issues before with users being able to visit pages they shouldn't be able to without being logged in, but this have been fixed now.

The order information text can use some improvement to make it look more professional and this is something I intend to fix in the future, but what's there is fine for now.

Requirements and Expectations:

1. Is the home view rendered directly when the user enters the website?

Yes.

2. Is the responsiveness of the website good?

Yes, this have been tested both manually and with online tools.

3. Is the navigation easy to understand?

Yes, I think that the layout and naming of links makes it easy for the users to understand how to navigate the website and this is made even clearer with toast messages down in the right corner of the page.

4. Is feedback given to the users?

Yes, most actions done by the users will give them feedback via toast messages or order confirmations.

5. Is it easy for the users to retrieve lost passwords?

Yes, this is built-in to the allauth authentication system and I have tested it so that it works as expected.

## Bandit -a tool designed to find common security issues in Python code.

[You can find out more about bandit here](https://github.com/PyCQA/bandit)

I used this automated tool to check if there were any security issues in my code. It scanned 1491 lines of code and found no security issues.

## Migrating to PostgreSQL from Sqlite3

This part was a real headache for me and I spent more than a week trying to figure out what was wrong, even asking people for help without avail.

I tried everything I could think of and at the end it was something really simple that I feel I should have figured out sooner.

PostgreSQL did not understand my query when I wrote in lowercase letters and Sqlite3 did, so all I needed to do to fix this was to change how I query the database.

## Bug Testing

- User inputs:

I found several issues here with some forms not being validated at all by django because I did not ask if the form is valid in the view, but also that the users were able to use invalid an invalid email address.

I fixed some of these issues with the built in validators for email addresses and images, but for other fields like for example the address, name, city fields I created a custom validation file that I put in the profile app. This makes it so that I can validate for each type of field and create a message for the specific input.

I have noticed a bug in the checkout app in regards to the field specific messages. They do not work because I am unable to render the form without breaking the field for stripe payments, so I have to redirect the users if there's an error for now. The users still gets a message saying that the input is not valid but they will not get the error message for the specific input that is wrong.

I have tried a few things to fix this, for example overriding the default is valid function. But as of now I have not been able to figure out how to fix this.

- Navigation and Security:

I had a few issues here with the users for example being able to view order information without actually being logged in to their account. I have fixed all of these issues by requiring users to be logged in to view certain pages, or even being a super user to view some.

I applied those limitations in both the template itself but also in the python code to make sure it is as secure as possible.

- Crud:

I had some issues here with for example users being able to upload files in the image field in the form for posting blogs, with emails not being sent and with the coupons codes not being applied correctly. I also found an issue with the quantity not being updated in the bag, this was due to the fact that I somehow had removed the buttons and only used the ones rendered by default in the form and they did not have the right settings. I fixed this by adding the buttons and setting the visibility to hidden in the css.

I do not find anymore errors when going through the website now and I tried every crud operation every several times in different ways to confirm this.

- Admin account:

In order to make sure that there are no issues with the admin account that is going to be used for the assessment I tried logging in to it and testing so that it worked as expected. I also asked a friend to login and see so there's no problems.

- Developer console:

One issue I noticed was a warning about missing favicon, I solved this by making a copy of my vegan logo and using that as a favicon and linking to it in the base template.

- Testing done after setting debug to false:

I started by testing all the forms, trying to change to invalid input to check if the validations work as expected and they do except for the bug I write about above here. Then I tried to submit the forms with valid data, sending emails, posting blog posts and creating orders with coupon codes. I did not find any issues there.

I also tried login in to accounts, resetting passwords, creating new accounts without any issues. I also tried updating and removing bag items without any problems.

I checked all the links and tried to get access to pages that I should not have access to without being logged in or an administrator and all of the protections here was working and I could not get access to anything that I shouldn't.

I logged into stripe to verify that everything works there and I checked that the payment intents had succeeded and that there was no errors with the webhooks.

I scanned all the python files one more time to check if I had any pep8 formatting errors but it was all fine.

When scanning my html templates for problem I encountered a problem at the accounts/login path, the validator says "No li element in scope but a li end tag seen." but this is a problem that comes from the allauth package and it is not in the code in the actual login.html template.

I found no other errors when scanning my templates. I scanned both with manual input and directly with the rendered html on the paths I could.
I ignored problems regarding bad values due to the jinja syntax.

## Known Bugs

### Form validation on checkout page

The form validation for the checkout form does not give a field specific error. This is due to the fact that I cannot render the checkout page with the form without breaking the stripe payment part, so I redirect instead. Form is still marked as invalid and the user will get a message saying it's invalid.

### Ending li tag in the login template

There's a end tag for an li element that is being rendered by the allauth package that I am unable to remove at the accounts/login page.

### Images in the blog form

This is not a bug exactly, but I noticed at the last night before submitting the project that it's sadly not possible to upload images to the deployed version of the site. The reason for this is that when I worked at the project and tried using s3 bucket, the free tier went out in less then a week and I had to change to static file hosting with whitenoise. This was perfectly fine for the project as it was back then and I did not consider it at all when creating the blog page.

My temporary solution for this is to upload [this](https://github.com/Tommyshub/restaurant/blob/main/static/images/blog-images.zip) zip file that contains images that I have already uploaded but deleted the blog posts from. All of these images will work to check so that the image form works on the blog page.

I realize that this solution isn't perfect and that it would have been far better to use something like digital ocean or cloudinary to host my images but I did not want to change that and risk not getting it to work properly this close before the submission deadline.

My hope is that the assessor will have some leniency for this mistake seeing that the function works fine other than the fact that I used static file hosting.

## Responsiveness

- Navbar

One problem with my navbar is that the pop out menu is not perfectly aligned in height on some screen sizes. I solved this by setting media queries for the height and changing the viewport settings in my css.

The navbar also starts to look a bit funky on sizes under 300pixels width but after doing some research I decided that it is not necessary to support screen sizes below 300 pixels in width so I left this as it is.

- Menu

I found no real issues with the responsiveness here but I did not like how the category names looked at smaller screen sizes and it also looked a bit weird when the categories had icons.

I fixed this by changing the headings to small text and put it under the icons instead.

- Contact

No issues.

- Account

No issue.

- Bag

In the bag I found that the keep shopping and secure checkout buttons where too close on small screen sizes and I fixed this by adding a class with margin-top on both of them. I needed to do that on both so that the height of the buttons matched on large screen sizes.

- Checkout

I had the same issues as in the bag but with the complete order and adjust bag buttons, and I fixed them in the same way.

## Formatting and Validation

### Prettier

I used the prettier extension for vscode to format the html, this worked great but one issue I had was that it did not format the jinja code. I googled how to best solve this and I could chose between either adding a comment saying prettier ignore to make the formatter ignore the jinja code, or just add normal comments. I did a mix between both but I mainly used normal comments.

### Pep8

For python I used the cornflakes-linter which is a wrapper for flake8. This also worked really good and it did most of the formatting for me, but I did notice a few issues when I checked my python files online. It seems that the cornflakes-linter missed a few lines that were too long and it also missed whitespace in some places.

[This tool](http://pep8online.com/) is what I used to double check if I had missed any pep8 issues and I fixed all that I could find.

### HTML

Validating the html was a bit problematic because the tool warned alot about the jinja code and it was a bit hard to see the real issues but this should be right now as far as I can tell.

One example of this problem is that it warned me about a stray doctype declaration in the base template, but as far as I can tell this is just because the jinja code is on the line before.

## Visualization of my database

[database diagram](https://github.com/Tommyshub/restaurant/blob/main/static/images/database_diagram.png)

## Deployment

Steps to take in order to run this website locally:

1. Clone or download this repository, unzip it and then open that folder in your favorite editor.

2. Rename the dummy_env file to only env.py, uncomment the import os statement and save it.

3. Add a secret key for the application, this can be any key you want but I recommend that you google for a secret key generator and use a generated key.

4. Register for a account on [stripe](https://stripe.com/) and get your public key, secret key and wh secret and add them to the env file.

5. Connect your email, in this case gmail in the env settings. You can find more information on how to do this [here](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab). You could also use any email provider you want to but then you need to change the configuration for the email provider in the settings.py file.

6. Add google OAuth credentials to your env file, you can find more information on how to get OAuth credentials [here](https://developers.google.com/identity/protocols/oauth2) you can also connect other providers and you can find more information about that [here](https://django-allauth.readthedocs.io/en/latest/providers.html)

7. You need to get a PostgreSQL database and connect it to the env file. You could install this on your own system or use a service provider. I would suggest you google for the option the fits you best and add the credentials from what ever you choose in the env file. You also need to migrate the database, you can do this by opening a terminal, navigating to the project folder and type:

- python manage.py makemigrations

- python manage.py migrate

8. Sign-up for an account at [EmailJS](https://www.emailjs.com/) and create a new template. It will have access to the subject, from_name, from_email and message variables and you can style this template how ever you want. You also need to connect to a new email service. You then need to add your service id and template id to the sendEmail.js file. You can find that file in the static js folder in the contact app. Last step here is to replace the existing browser integration settings in the base.html template with the ones you can find [here](https://dashboard.emailjs.com/admin/integration/browser). You can find the base.html file in the templates folder at the root of this application.

9. Last step is to navigate to the project folder in your terminal and type "python manage.py runserver" and open the url in your browser.

There are many options for you if you wish to deploy the site to your own domain, but I would recommend using Digital Ocean. You can find out more on how to deploy a Django application to Digital Ocean [here](https://www.digitalocean.com/community/tutorials/how-to-deploy-django-to-app-platform).

## Acknowledgments and Credits

I would like to make it clear that I referenced and used a lot of what we learned during the Boutique Ado project when creating this, especially when it came to connecting to the stripe payments system.

I got a little bit help from the tutor support and an acquaintance when creating the coupon codes. I had problems figuring out how to subtract the discount from the total in the context processor, so I got advised to add the discount to the settings.py file and I also got advice how to best check for used coupons.

### Images

I got all the images from and I would like to thank these people for making them available for the public to use.

- Deryn Macey
- Taylor Kiser
- Jordan Nix
- Irene Kredenets
- Fabio Alves
- Luis Gonzalez
- Adalia Botha

## Coupon Codes for Testing

I considered adding the coupon codes to the confirmation email but I decided not to because I felt that it was less of a risk
that they would be missed if I added them here instead.

Here are two codes that can be used for testing:

Code20 and Institute21

## Changes made after the 4th of July 2021

### Coupon Codes

Here I had a problem with the users not being given the right feedback after applying coupon codes, to fix this I added the discount to the
checkout model and made sure the discount and new total will be displayed correctly everywhere. I also made sure to set the discount back to zero after it was applied so that the users can't use the coupon code twice before the session is emptied.

When testing the new changes I encountered a problem, both the discount and the total could be set to zero if the user tried to refresh the checkout success page so to fix this I am now redirecting the users to the order history page instead.

This made the message that the users are viewing a past order when clicking on the order history link a bit awkward so I decided to remove that message. I figured that it should be clear to the user that it is a past order either way, because of the date in the order information but also because of the navigation actions.

To test so that this works as expected I made several orders with different items and I applied the discount codes to check that it worked correctly. I also made a few orders without discount directly after to insure that the discount was gone from the session.

### Contact Page

I moved the contact page to the bottom of the homepage instead. I changed from using the built-in send mail from django to emailjs. This presented a problem with the messaging from the django view not working anymore because I needed the emailjs javascript file function to return false. I tried writing the javascript function asynchronous instead but I never got it to work good, so my solution at the end was to handle the messages for emails directly via the javascript instead.

### Blog Page

I built the blog page so that the restaurant can post news and updates on what is going on there and also so that they can post coupon codes if they have any deals at the moment. This is a page that I envision not only restaurant owners would use, but also the restaurant workers. Therefore I decided to build out an admin panel in the template so that the restaurant workers with the right access can create a blog post from there. I think that it would make sense to have a different type of user other than superusers to get access to that part of the page, since that is the user that have access to the admin panel, but for now and for testing purposes I decided to leave it for the normal superuser class.

### Form Validation

Contact Form:

The only validation I did on the contact form is to validate the email and require fields to be filled in. I did not see any use for any more validation here.

Blog Form:

The only validation I did on the blog form is to require the fields to be filled in and to make sure that no one can upload anything other than a image file. This was done by default on the image field so all I had to do is to ask if the form is valid.

Bag Form:

I did not do much of validation on the bag form other than that the coupon codes needs to be unique and I put a max length of twelve. I think this should be enough since the coupons can only be used once and they need to match what's in the database to work.

Profile Form:

The profile form required much more validation so I created a validators.py file where I validate most of the fields in the contact form. I do this by matching the value of the form towards a regex filter. Much of the filtering is the same but I created one for almost each individual field so that I can attach a error message for that exact field. I also use the built in email validator from django on the email field.

Checkout Form:

I am doing the same validation for the checkout form as for the profile form and I am importing the custom validator from the profile app to use on the checkout form.
