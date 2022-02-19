# Games R us


### Games R us is an ecommerce web application for customers seeking to purchase gaming stuff online.

This is the fifth and last portfolio project for the Code Institute Diploma in Fullstack Software Development.

Users can create accounts and administrators have full write and delete access to all data. To test an administrator account, 

You can test the card payment functionality without making a purchase. Use card details:

4242 4242 4242 4242 - CVC and 5-number postal code at the end of the card can be any numbers.

### Admin:

* password: Niklas3000
* Username: Admin


You can view the deployed site [Link to Live Website](#)
Github repo [GitHub Repo](#)

# Project Overview
Games R Us is an assignment for the Code Institute Diploma in Full Stack Software Development, but also meant to be applicable in a real world scenario (except for the products being fictional of course).

The focus points for this application are ecommerce, using the Django framework and the ability to go through with a payment for an order.


## Agile Workflow


I have tried to implement the basic Agile strategy, creating issues for my user stories,

As Github is limited with ways to do this, I had my user stories in a seperate file


#User Experience
##Strategy
###Primary Goals
The site owners primary goals are:

* To be able to sell the stores products online

* To have the ability to add, remove or edit products in the store

* To access a customers order, edit and/or remove it if necessary

* To access and keep track of customer information

* To own a website which is easy to use and navigate, for all types of users on all devices.

### A potential customers primary goals are:

* To be able to view details of and purchase any of the available products from the online store.

* To be able to register for an account

* To see an order history in their account

* To be able to edit their account details or remove their account

* To easily navigate the whole website and keep track of all user interactions, for example the products in their cart and how much they are to spend

# Business Model
I have chosen a traditional B2C (Business to Customer without middle person) application, which has a straightforward and user friendly interface. This online store offers no products of their own and relies on the wholesale of branded products. A real world version of the store would list all the retailers it is affiliated with.

The business flow is as follows:

* Games R Us buys products from wholesale retailers or from the manifacturers themselvse

* The website handles selling of products from Games R Us to the end customer, the website user.

The intentions should be obvious and users should know as soon as they enter the site what it offers and how to use it's features.

### Marketing
This site has a Facebook Business page with a link on the page footer. It can be viewed
# (LINK TO FACEBOOK SITE)


### Search Engine Optimisation

I have also done some research on highest searched words in Gaming retailing, and came up with this title and description:

# (img of meta data with search keywords)

# Structure
This website has 11 custom built pages and 16 (not all are used) account operations Django Allauth pages. The navbar at the top of the screen gives users access to the most important pages at all times.


## Pages
### Accessible to all users

* Home - The landing page of the site, with a full screen carousel hero image giving first time visitors a nice welcome

* Products - This is a list of the products when clicking on a category in the navbar, or performing a search

* Product Detail - The dedicated page for a specific product, where users can read a description and perform all given tasks for the product

* Bag - A user purchases an item by adding it to the bag; clicking on it will show all bag items

* Checkout - Here users enter their delivery details and card info to proceed with their order

* Order Confirmation - The page show when a payment has successfully been made, showing the order information

* The Sign In and Sign Up pages

## Accessible to signed in users

### Profile page 

* The users order history, billing and shipping info is here.

#### Sign Out

* Other accounts operations pages such as Change Password or Password reset

* Delete Account - Allows the user to completely remove their account from Games R us

### Accessible to Admin users

* Add Brand or Product - This is where admin users can add new products to the website

* Edit Product - The page for admins to edit or delete products

* Manage products - An overview of all products on the site with edit and remove functionality

## Pages provided by Django
These pages are provided by the Allauth package of the Django framework, but are customised by me to fit in with the rest of the site. Read more about Allauth here

* Sign Up - where users can register for an account on the site

* Sign in - Registered users can log accessing their personal info etc by signing in

* Sign Out - The same goes for signing out

* Various pages for email verification and password reset, etc

## Technical Design
###Code Structure
I have devided the code into apps as per Django best practice, for the different areas of functionality.

* Home - basic functionality for the home page

* Products - all functionality related to the products on the site

* Bag - functionality for the users shopping bag

* Checkout - functionality for the user to go through with the order and payment

* Profiles - functionality regarding the users profile and order data

* User Account - The app in which users can delete their account

### Other Directories and files


* static - css and javascript files

* media - images for the development website (other images are used in the production version)

* gamesrus - project folder containing settings, urls and other configuration files for the whole project

* templates - contains the base template and templates (HTML-files with Django logic) for the Django allauth authentication

* manage.py - the main python project file to get the web application running

* README.md - the document you are reading right now, documentation of the whole project

* custom_storages.py - configuration for storage of media and static files on AWS S3

Enviromental Variables such as API-keys, passwords etc are stored securely in the back end (in the development environment and in the Heroku App settings) so that regular users do not have access to them.

* Procfile - needed for deployment to Heroku to specify commands to be executed by the app on startup

* requirements.txt - a list of dependancies (installed packages) that the project requires for the application to function


## Data Models
The following models have been used to populate the database and for the site to function as it should:

* User - the built in Django User model, facilitates the users basic information

* Category - the category in which the product is placed

* Product - the model for the product itself and its details

* Order - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

* OrderLineItem - a model holding the product information for a single product, binding the product model together with the order

* UserProfile - the model storing the users product and order information

# Img of database schema for models (#)

## Scope - Epics and User Stories
Epic 1: Base functionality and ease of use
As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page

As a user, I can access important links such as home, products, my bag, sign in/out, and my profile by scrolling and/or clicking once, regardless of where on the site * I am, so that i can easily navigate the site

* As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook

* As a user, it is visible if I am signed in or not, so that I am made aware of this

* As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

## Epic 2: Products
* As a user, I can browse a list of products for sale on the site so that I can find the product I seek

* As a user, i can perform a search, so that products matching the search appear in the products list

* As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek

* As a user, I can view the most important details of the product in the product list, such as category, price, rating, and image so that i know most details without having to click on the product

* As a user, i can click the product in the products list so that I can view the products details

## Epic 3: Bag
* As a user, I can add a product to my bag by clicking ’Add to bag’ from the product detail page so that I can purchase the product

* As a user, I can always see the total price of my bag in the navigation bar, so that I know what the total cost will be

* As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart in the order details

* As a user, I can view the products added to my bag by clicking the bag icon or by adding an item to the bag

* As a user, I can update the quantity or remove it completly

## Epic 4: Checkout
* As a user, I can click on Proceed to Checkout, so that I can purchase the items in my bag

* As a logged in user, on the Checkout page, I can choose to save my delivery address to Profile if logged in, so that I can retain it for future orders

* As a user, i can enter my card details on the checkout page, so that I can make the desired purchase

* As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation

## Epic 5: User registration and account
* As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits

* As a user, I am not able to access pages that require authentication if I am not signed in

* As a user, I have to confirm my email address to complete my account registration

* As a logged in user, i can view a My profile page, so that I can view my previous orders, and view and update my delivery and contact details

* As a logged in user, I can add my delivery details to the profile page, so that it is my default delivery address for my order on the checkout page

* As a logged in user, I can choose to delete my account, so that my user account no longer exists


## Epic 6: Site Owner functionality
* As a site owner, I can view an admin page, where I can perform batch editing of model instances on the site including products, categories, orders

* As a site owner, I can add, edit or remove any product on the site

* As a site owner, I can remove any products review on the site
