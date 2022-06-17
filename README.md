# Tina Q Cards

Tina Q Cards is a website selling bespoke handmade greeting cards for occasions such as birthdays, anniversaries, get well soon and so on. Users are able to browse the selection of cards and purchase any they like the look of. They can also send a message requesting cards to be made to requirements. Users will be able to look at previous orders and update their delivery details if they register an account. 

![Image of application pages on different screen sizes](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/am_i_responsive.JPG)<br>

[Link to deployed site](https://tina-q-cards.herokuapp.com/)

## UX

### Imagery

 My application features a simple background image showing some texture on the homepage. The other images present are those for the products. I also make use of Font Awesome icons for some additional visual flourish.

### Typography

The fonts used in my application are "Corben" for any heading type text and "Montserrat" for any remaining content. These come from Google Fonts. 

### Colour scheme

The colour scheme is based around darker pink and red colours (#AB274F, #CA9FB5, #A16484) with a very dark purple colour used for certain backgrounds and also for some button elements (#54424B). The palette for this was determined using [mycolor.space](https://mycolor.space/?hex=%23AB274F&sub=1) and is known as the "Neighbor Palette":

![Image of colour palette](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/colour_palette.JPG)<br>

The colour #AB274F has also been used for certain button elements and for various headings. It is the primary colour for the site with the other colours used to support it. 

### Schema

The schema overview for my application is as below:

![Image of schema overview](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/schema.JPG)<br>

As seen above, the Category table has a one-to-many link with Product as one category can contain many products.
The Order table has a one-to-many link with OrderLineItem, as one order can contain many line items. There is also a one-to-many link between Product and OrderLineItem as the same product can appear in many line items on different orders.<br><br>
There is a one-to-many relationship between UserProfile and Order as one user can have many orders associated with them. The UserProfile table also has a one-to-one link with the built-in Django User model (shown here for demonstration purposes) as each user can have only one profile linked to them.
The ContactUs, WelcomeMessage and BlogPost tables are standalone with no links to any other tables. 

The details for each model are as follows:

#### Blog app

- BlogPost<br>
![Image of blogpost model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/blogpost_model.JPG)

#### Checkout app

- Order<br>
![Image of order model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/order_model.JPG)

- OrderLineItem<br>
![Image of orderlineitem model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/orderlineitem_model.JPG)

#### ContactUs app

- ContactUs<br>
![Image of contactus model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/contactus_model.JPG)

#### Home app

- WelcomeMessage<br>
![Image of welcomemessage model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/welcomemessage_model.JPG)

#### Products app

- Category<br>
![Image of category model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/category_model.JPG)

- Product<br>
![Image of product model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/product_model.JPG)

#### Profiles app

- UserProfile<br>
![Image of userprofile model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/userprofile_model.JPG)

### Business Model

The business model used for my application is B2C. The reason I chose this is because the products I will be selling are aimed at consumers and not businesses. The product selection and checkout flow allow for quick and straightforward purchases, which is not something you would use in a B2B environment. 

### Marketing Strategy

In terms of the marketing strategy choices employed for my application, I have made use of the following:<br>

- Social media advertising, due to it being a no cost option and potentially able to reach many users
- Email advertising due to the relative simplicity of creating newsletters or offers for potential and existing customers
- SEO and looking to rank well in searches on Google to aid visibility of my application

### Facebook Business Page

The Facebook Business Page created for my project is as follows and makes use of the same imagery and logo. It is also linked to in the footer of my application.

Home page:<br>
![Wireframe of FB home page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/fb_page1.JPG)<br>

Info:<br>
![Wireframe of FB info details](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/fb_page2.JPG)<br>

Photos:<br>
![Wireframe of FB photo page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/fb_page3.JPG)<br>

Community:<br>
![Wireframe of FB community page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/fb_page4.JPG)<br>

### Wireframes

The wireframes for my website are as follows:

#### Mobile

Homepage:<br>
![Wireframe of mobile homepage](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_home_1.JPG)<br>
Homepage with expanded menu:<br>
![Wireframe of mobile homepage with expanded menu](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_home_2.JPG)<br>
Products page:<br>
![Wireframe of mobile products page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_products.JPG)<br>
Product detail page:<br>
![Wireframe of mobile product detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_product_detail.JPG)<br>
Basket page:<br>
![Wireframe of mobile basket page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_basket.JPG)<br>
Checkout page:<br>
![Wireframe of mobile checkout page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_checkout.JPG)<br>
Checkout confirmation page:<br>
![Wireframe of mobile checkout confirmation page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_checkout_confirm.JPG)<br>
User profile page:<br>
![Wireframe of mobile user profile page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_profile.JPG)<br>
About us page:<br>
![Wireframe of mobile about us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_about.JPG)<br>
Contact us page:<br>
![Wireframe of mobile contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_contact.JPG)<br>
404 page:<br>
![Wireframe of mobile 404 page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_404.JPG)<br>

#### Tablet

Homepage:<br>
![Wireframe of tablet homepage](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_home_1.JPG)<br>
Homepage with expanded menu:<br>
![Wireframe of tablet homepage with expanded menu](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_home_2.JPG)<br>
Products page:<br>
![Wireframe of tablet products page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_products.JPG)<br>
Product detail page:<br>
![Wireframe of tablet product detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_product_detail.JPG)<br>
Basket page:<br>
![Wireframe of tablet basket page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_basket.JPG)<br>
Checkout page:<br>
![Wireframe of tablet checkout page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_checkout.JPG)<br>
Checkout confirmation page:<br>
![Wireframe of tablet checkout confirmation page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_checkout_confirm.JPG)<br>
User profile page:<br>
![Wireframe of tablet user profile page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_profile.JPG)<br>
About us page:<br>
![Wireframe of tablet about us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_about.JPG)<br>
Contact us page:<br>
![Wireframe of tablet contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_contact.JPG)<br>
404 page:<br>
![Wireframe of tablet 404 page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_404.JPG)<br>

#### Desktop

Homepage:<br>
![Wireframe of desktop homepage](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_home.JPG)<br>
Products page:<br>
![Wireframe of desktop products page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_products.JPG)<br>
Product detail page:<br>
![Wireframe of desktop product detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_product_detail.JPG)<br>
Basket page:<br>
![Wireframe of desktop basket page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_basket.JPG)<br>
Checkout page:<br>
![Wireframe of desktop checkout page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_checkout.JPG)<br>
Checkout confirmation page:<br>
![Wireframe of desktop checkout confirmation page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_checkout_confirm.JPG)<br>
User profile page:<br>
![Wireframe of desktop user profile page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_profile.JPG)<br>
About us page:<br>
![Wireframe of desktop about us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_about.JPG)<br>
Contact us page:<br>
![Wireframe of desktop contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_contact.JPG)<br>
404 page:<br>
![Wireframe of desktop 404 page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_404.JPG)<br>

<br>
The final version of my site has a link for "Tina's Blog" instead of "About Us" in the main navigation element, this change was made following some discussion with my mentor. Also, in the footer, the newsletter signup is on the left instead of the right now. 
<br>
<br>

### User Stories

#### New users

- As a site user I can browse through products so that I can decide what I may be interested in buying
- As a site user I can look at product details so that I can decide whether I would like to buy it
- As a site user I can search for products so that I have another way of looking for items
- As a site user I can sort products on criteria such as category or price so that I have a method of ordering the products as I prefer
- As a site user I can add products I want to purchase to a basket so that I may then decide whether to purchase them or not
- As a site user I can view the contents of my shopping basket so that I can make any adjustments to it
- As a site user I can perform a checkout on my shopping basket so that I can create an order
- As a site user I can register an account so that I can make use of features reserved for registered users
- As a site user I can log in so that I can use features reserved for registered users
- As a site user I can log out so that my account remains secure if I were to visit the site from a shared PC
- As a site user I can view a profile for my user account so that I can see my order history and also make any adjustments to the details kept on record for me
- As a site user I can submit a message to admin so that any feedback or issues I’m having can be raised with them
- As a site admin I can manage product categories so that I may add, update or delete them as needed
- As a site admin I can manage products so that I may add, update or delete them as needed
- As a site admin I can manage user accounts so that any required changes to them can be made
- As a site admin I can view created orders so that they may be fulfilled, or amended if needs be
- As a site admin I can view messages submitted via the contact us section so that I may act upon them
- As a site admin I can manage the welcome message text that displays on the Homepage so that I can update it if required
- As a site admin I can manage the content on the “Tina's Blog” page so that it can be amended if needed

#### Returning users

- As a returning site user I can have a look whether any new products have been added so that I can decide if I want to buy any
- As a returning site user I can view my user profile (if I registered an account) so that I can see whether my details are still up-to-date and also view previous orders
- As a returning site admin I can see whether any new messages have been submitted so that I can action them accordingly
- As a returning site admin I can look at whether any new orders have been placed so that I can fulfill or amend them as required
- As a returning site admin I can update the welcome message text so that any changes to it can be made
- As a returning site admin I can update the "Tina's Blog" page content so that any required changes to it are reflected

#### Frequent users

- As per returning users

## Features

### Existing Features

The application features a fixed header containing a nav element which is responsive and collapes for narrower viewports; you would see a "hamburger" icon to the left of the nav element, with the nav links below that, if viewed on a smaller screen. The links for account related activities are under the "Account" dropdown. You can search the products from the search box in the header and see whether you have anything in your basket:

![Image of header](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/header.JPG)<br>

The homepage features a welcome message and also a button to start browsing the products:

![Image of homepage](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/homepage.JPG)<br>

There is a footer containing a newsletter signup form and also links to social media pages and the privacy policy:

![Image of footer](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/footer.JPG)<br>

There is a login page:

![Image of login page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/login.JPG)<br>

There is also a logout page:

![Image of logout page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/logout.JPG)<br>

For unregistered users, there is a registration page:

![Image of sign up page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/signup.JPG)<br>

The products overview page shows all products and also has the function to sort them accordingly:

![Image of products page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/products.JPG)<br>

Clicking on a product will take you to the detail page for that item where a required quantity can be added to the basket:

![Image of product detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/product_detail.JPG)<br>

There is a notification system showing messages following user initiated actions such as adding an item to the basket, etc:

![Image of notification](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/toast.JPG)<br>

There is a view of the basket so that its contents can be adjusted if needed:

![Image of basket page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/basket.JPG)<br>

When going to checkout from the basket view, a checkout form and preview of the basket can be seen:

![Image of checkout page 1](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/checkout1.JPG)<br>
![Image of checkout page 2](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/checkout2.JPG)<br>

Completing checkout successfully shows a confirmation screen for this:

![Image of checkout complete page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/checkout_success.JPG)<br>

For registered users, there is a profile view showing default delivery information and past orders:

![Image of profile page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/profile.JPG)<br>

Clicking on an order from the profile view shows its details:

![Image of order history page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/past_order_details.JPG)<br>

There is a blog page:

![Image of blog page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/blog.JPG)<br>

And finally a contact us page with a form to be filled out should a user wish to submit a message to the site admin:

![Image of contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/contact_us.JPG)<br>


### Features Left to Implement

- Implement a stock system so product quantities could be managed
- Have a loyalty discount scheme where codes can be used to reduce the cost of some items
- A method of reducing prices of items in bulk for sale type events

## Technologies Used

### Languages

- HTML - Required for the render templates
- CSS - Used to provide required custom styling for the templates
- JavaScript - Used to provide custom code to automate certain tasks in the templates
- Python - The language that the Django framework is based on

### Libraries

- Bootstrap - Used for various components in the templates as follows:
    - Navbar - For navigation element
    - Card - For the display of certain elements    
    - Grid - To configure layout of page elements
    - CSS - Used for element styling
    - JavaScript - Used for automation of components
    - Toasts - Used to provide notifications to the user
- Stripe - Used to provide payment functionality
- Google Fonts - Where fonts were sourced from
- Font Awesome - Icons used to provide additional visual flourish

### Frameworks

- Django - Full stack framework used to build this application

### Platforms

- GitHub - Where code repository resides with Git version control
- Gitpod - IDE used for development with Git version control
- Heroku - Where the deployed application is served from
- AWS S3 - Where media and static files are stored for the deployed application
- Stripe - Used to provide payment functionality
- Mailchimp - Used to provide the newsletter sign up functionality

### Services

- [Mycolor.space](https://mycolor.space/) - Used for deciding on colour palette
- [favicon.io](https://favicon.io/favicon-generator/) - Used to generate favicon  
- [TinyPNG](https://tinypng.com/) - Used for optimisation of image file sizes
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/#wizard) - Where the privacy policy was generated from

### Software

- GIMP 2.10.30 - Used for the creation of the logo 

## Testing

- As a site user I can browse through products so that I can decide what I may be interested in buying
    - Expected: There will be a products page that I can look through
    - Actual: Browsing to the products page of the site shows all products at a glance
    ![Image of products page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/products.JPG)<br>
- As a site user I can look at product details so that I can decide whether I would like to buy it
    - Expected: Clicking on a product will show more details about it
    - Actual: There is a detail page for each product, which opens when you click on the item
    ![Image of product detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/product_detail.JPG)<br>
- As a site user I can search for products so that I have another way of looking for items
    - Expected: The site will have some sort of search function to allow searching of products
    - Actual: From the header, there is a search box where product searches can be entered
    ![Image of header](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/header.JPG)<br>
- As a site user I can sort products on criteria such as category or price so that I have a method of ordering the products as I prefer
    - Expected: When viewing the products page, there will be some way to sort products by different criteria
    - Actual: On the products overview page, there is a "Sort" box at the top right that allows sorting
    ![Image of products page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/products.JPG)<br>
- As a site user I can add products I want to purchase to a basket so that I may then decide whether to purchase them or not
    - Expected: The website will have some sort of basket function
    - Actual: When viewing a product detail page, there are buttons to add a required quantity to the basket
    ![Image of product detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/product_detail.JPG)<br>
- As a site user I can view the contents of my shopping basket so that I can make any adjustments to it
    - Expected: There will be a method to view the shopping basket
    - Actual: Clicking on the basket icon in the header takes you to the basket page
    ![Image of basket page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/basket.JPG)<br>
- As a site user I can perform a checkout on my shopping basket so that I can create an order
    - Expected: There should be a button to allow checkout of a basket
    - Actual: From the basket page, you can click "Secure Checkout" to be taken to the checkout page
    ![Image of checkout page 1](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/checkout1.JPG)<br>
    ![Image of checkout page 2](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/checkout2.JPG)<br>
- As a site user I can register an account so that I can make use of features reserved for registered users
    - Expected: There will be a link to a sign up page
    - Actual: As an anonymous user, clicking on "Account" in the header provides a link to a sign up page
    ![Image of sign up page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/signup.JPG)<br>
- As a site user I can log in so that I can use features reserved for registered users
    - Expected: There should be a link to log into the site
    - Actual: From the "Account" dropdown in the header, there is a log in link
    ![Image of login page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/login.JPG)<br>
- As a site user I can log out so that my account remains secure if I were to visit the site from a shared PC
    - Expected: I should be able to log out of the site with a button of some sort
    - Actual: As a logged in user, there is a link to log out under the "Account" dropdown
    ![Image of logout page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/logout.JPG)<br>
- As a site user I can view a profile for my user account so that I can see my order history and also make any adjustments to the details kept on record for me
    - Expected: I should be able to, as a logged in user, navigate to a profile page
    - Actual: From the "Account" dropdown, there is a link to a profile page visible to logged in users
    ![Image of profile page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/profile.JPG)<br>
- As a site user I can submit a message to admin so that any feedback or issues I’m having can be raised with them
    - Expected: There should be a page to submit a message 
    - Actual: From the "Contact Us" link, there is a form to allow sending of messages to site admin
    ![Image of contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/contact_us.JPG)<br>
- As a site admin I can manage product categories so that I may add, update or delete them as needed
    - Expected: There will be an admin view where I can see the configured categories
    - Actual: Navigating to the admin page, which has a link visible to admin users from the "Account" dropdown, allows managing of the categories
    ![Image of category management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_categories.JPG)<br>
- As a site admin I can manage products so that I may add, update or delete them as needed
    - Expected: I will be able to view product management from the admin view
    - Actual: From the admin page, I can select to manage the products
    ![Image of product management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_products.JPG)<br>
- As a site admin I can manage user accounts so that any required changes to them can be made
    - Expected: The admin view should have a way to manage users
    - Actual: From the admin page, clicking on "Users" allows management of them
    ![Image of user management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_users.JPG)<br>
- As a site admin I can view created orders so that they may be fulfilled, or amended if needs be
    - Expected: There will be an admin view to see any submitted orders
    - Actual: From the admin page, clicking on "Orders" allows you to view them
    ![Image of order management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_orders.JPG)<br>
- As a site admin I can view messages submitted via the contact us section so that I may act upon them
    - Expected: I should be able to view submitted messages from an admin view
    - Actual: Clicking on "Contact Us" from the admin page allows viewing of submitted messages
    ![Image of message management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_messages.JPG)<br>
- As a site admin I can manage the welcome message text that displays on the Homepage so that I can update it if required
    - Expected: There will be a way to view the welcome message text
    - Actual: From the admin page, clicking on "WelcomeMessage" allows for this functionality
    ![Image of welcome message management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_welcomemessage.JPG)<br>
- As a site admin I can manage the content on the “Tina's Blog” page so that it can be amended if needed
    - Expected: The admin view will have a way to manage content for the blog page
    - Actual: Navigating to "Blog posts" allows management of this content
    ![Image of blog management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_blog.JPG)<br>

The application has been tested using the Chrome, Edge and Firefox browsers at full width on a 1080p and 4K monitor, as well as a Samsung Galaxy S20 FE 5G handset. The following emulated device sizes were checked:<br>
<br>

- Chrome \ Edge
    - Galaxy S5
    - Pixel 2 XL
    - iPhone 6/7/8
    - iPhone X
    - iPad
    - iPad Pro
- Firefox
    - Galaxy S10/S10+
    - Galaxy S20 Ultra
    - iPad
    - iPhone 11 Pro
    - iPhone 12/13 +
    - iPhone SE 2nd gen

The application behaved as expected at the different viewport widths. While it functions as expected on a 4K monitor, it is optimised for screens 1080p and lower. 

### Bugs


### Validator testing


## Deployment

### Initial deployment

- Gitpod
    - Create new repository from CI template
    - Install Django and required dependencies into Gitpod workspace
    - Create new Django project called "tina_q_cards"
    - Create procfile as required
    - Run "pip3 freeze --local > requirements.txt" to update requirements file
- Heroku
    - Log into Heroku 
    - Create new app called "tina-q-cards"
    - Add a PostgreSQL "hobby" database as resource
    - Configure "DISABLE_COLLECTSTATIC = 1" in Config Vars
    - Configure "SECRET_KEY" variable in Config Vars
- Gitpod
    - Create env.py file and add database path from Heroku
    - Add secret key to env.py
    - Configure database path and secret key in settings.py to be read from environment variables
    - Perform commit and push to GitHub
    - Also push commit to Heroku, this will trigger deployment, await completion 

### Final deployment


## Credits 

### Content


### Media


### Acknowledgements

