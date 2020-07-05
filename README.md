# F1 Memory Game

![Site Preview](...)

---

## [Project Repository](https://github.com/filleben/F1Dictionary)

## [Deployed Site](https://f1-dictionary.herokuapp.com/)

---

This project is designed for new and casual Formula One fans. The goal of the project is to help improve the understanding of the sport by defining some of the sports most commonly used terms, the project will display the terms in categories based on where they are in the alphabet, user will be able to add new definitions aswell as editing existing definitions if needed.

## Table of Contents

- <a href="#ux">UX</a>
- <a href="#features">Features</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

<span id="ux"></span>

## UX

### User Goals

I expect that the majority of the users will fall into the following criteria:

- Be a Formula One Fan.
- A user with very little Formula One knowledge looking to learn.
- A user with lots of Formula One knowledge looking to update and add new definitions to the site.

### User Stories

- As a user, I want the site to be simple to use and visually appealing.
- As a user, I want the the definitions to be sorted in categories.
- As a user, I want to be able to update any incorrect definitions.
- As a user, I want to be able to add more definitions to the site.
- As a user, I want to be able to quickly find the information I am looking for.

### Wireframes

[Here](https://github.com/filleben/F1Dictionary/tree/master/wireframes) are the designs I made for the site.

The wireframes were made using [Balsamiq](https://balsamiq.cloud)

### Design Choices

- **Font**: I wanted the project to look as professional as possible so decided to use a copy of the official Formula One font sourced from [Here](https://www.ffonts.net/Formula1-Display-Regular.font.download).

- **Colours**: I wanted the project to look like a product from Formula One so with this in mind I used the same colour scheme used on the [Official Site](https://www.formula1.com/). I used white (Hex: '#ffffff' RGB: 'rgb(255, 255, 255)') as the background and navbar font colour, red (Hex: '#ff0000' RGB: 'rgb(255, 0, 0)') for the navbar and block-divder elements and then black (Hex: '#000000' RGB: 'rgb(0, 0, 0)') for the body text.

<span id="features"></span>

## Features

- **Navigation bar**: Allows the user to navigate to all the pages of the site, consistent throughout the site. Links in the navbar change depending on if the user is logged in or not.
- **User Registration and Authenication**: Users have to make a account and be logged into the site in order to unlock the ability to add, edit and delete definitions.
- **Definitons Grouped by Category**: Home page displays all the different categories of definition which can be expanded on click to reveal the records in that category.
- **Add Definition**: Logged in users and add definitions to the database.
- **Edit Definitions**: Logged in users can edit existing definitions in the database and update them.
- **Delete Definitions**: Logged in users can delete definitions from the database.
- **Login Checks**: CRUD pages will only be viewable if a user is logged in.
- **404 Page**: Provides users with a message if they have entered a incorrect URL or clicked a incorrect link, gives the user the option to return to the home page.


### Features Left to Implement

- Search bar on the home page allowing users to simply search for a definition instead of manually finding it.
- Add a undo button in the event of accidental data deletion by the user.
- Futher user authentication, users only allowed to change data they have entered themsleves into the database.


<span id="testing"></span>

## Testing

### Testing Tools

#### I used the following tools and devices to test the website in several different scenarios. 

- [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools)
  - The project used **Firefox Developer Tools** to test responsiveness, styles, and different layouts throughout development. This also allowed the site to be tested on several other [mobile devices](https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode).

##### Devices I Physically Tested With. 

- [Samsung Note 10+](https://en.wikipedia.org/wiki/Samsung_Galaxy_Note_10)
  - The project used a **Samsung Note 10+** to test the site on a mobile device.

- [HP Envy x360 13](https://www.amazon.co.uk/HP-13-ar0001na-Touch-Screen-Convertible-Laptop/dp/B07V3J1H3V)
  - The project used an **HP Envy x360 13** to test the site on both a 13-inch laptop and a tablet.

##### Devices Simulated With In Firefox Dev Tools. 

- [Samsung Galaxy S9/S9+](https://en.wikipedia.org/wiki/Samsung_Galaxy_S9)

- [iPhone 6/7/8](https://en.wikipedia.org/wiki/IPhone_6)

- [iPhone X](https://en.wikipedia.org/wiki/IPhone_X)

- [iPad](https://en.wikipedia.org/wiki/IPad)


I used the following web browsers on both desktop (Windows) and mobile (Android) where available.

- [Mozilla Firefox](https://www.mozilla.org/en-GB/)
  - Desktop Version: 76.0.1 Mobile Version: 75.0.0-beta.6

- [Google Chrome](https://www.google.com/chrome/)
  - Desktop Version: 81.0.4044.138 Mobile Version: 81.0.4044.138

- [Opera](https://www.opera.com/)
  - Desktop Version: 68.0.3618.99

- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
  - Desktop Version: 44.18362.449.0

The project was run through both [HTML Validation](https://validator.w3.org/) and [CSS Validation](https://jigsaw.w3.org/css-validator) with no errors found.