# The Greenhouse

### User stories

As a customer of the resturant i want,

- to order food to be delivered to my door.

- to be able to create an account.

- to be able to store my default delivery information.

- to be able to change my default delivery information.

- be able to view information about the food.

- be able to contact the resturant to ask about my order.

As a resturant owner I want,

- to have a menu where my customers can view and order food.

- my customers to be able to create a account.

- to be able to view my customers contact information.

- my customers to be able to update their default delivery information.

- my customers to be able to give tips to the delivery people.

- customers to be able to contant us.

- my customers to be able to view their past order.

- my customers to have a good checkout experience.

- the website to look professional so that my customers feel save ordering from us.

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML)

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Tools & frameworks

- [Django](<https://en.wikipedia.org/wiki/Django_(web_framework)>)

- [Materialize CSS](https://materializecss.com/)

- [Git](https://git-scm.com/)

- [Google Fonts](https://fonts.google.com/)

## Testing

### Bandit -a tool designed to find common security issues in Python code.

[You can find out more about bandit here](https://github.com/PyCQA/bandit)

I used this automated tool to check if there were any security issues in my code. It scanned 1491 lines of code and found no security issues.

### Django Testing

I wrote tested some of my code with the buil-in django testing framework. I focused on the checkout app when I wrote me tests but I intend to add more in the future.

- I tested the forms by making sure that the form cannot be submitted without the required fields.

- I tested so that the urls resolves as expected.

### Forms

- Default delivery information form

The first form I tested was the change default delivery information form, and I realized that this form can be submitted when it is empty and therefore set the default delivery information to an empty string.

I fixed this by setting blank to false on all fields except the street address 2 field.

I also checked that everything was updated as expected when submitting a valid form by going to the checkout form and looking at the delivery information.

- Contact form

First thing I checked was to submit a blank form and that does not work.

I tried to submit the form without a valid email address and this did not work either.

I also tried to submit a valid form and I checked my email adress to confirm that I the received the email and that it was formatted as expected.

- Bag forms

The first thing I tested here was to update and remove items and that worked as expected.

One problem I noticed is that the input field for the form for giving tips does not show until the button is pressed and it warns that the form needs to be filled out. I have no idea how to fix this and I cannot find any information about it online so that is something I intend to ask my mentor about before submitting this project.

### Buttons and links

I manually looked at every button and link on the page and I could not find any the did not work as expected.

### Developer console

While looking in the console I visited every page in my app and I clicked all the buttons.

First issue I noticed was a warning about missing favicon, I solved this by making a copy of my vegan logo and using that as a favicon and linking to it in the base template.
