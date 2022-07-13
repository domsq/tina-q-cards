# Tina Q Cards

Tina Q Cards is a website selling bespoke handmade greeting cards for occasions such as birthdays, anniversaries, get well soon and so on. Users are able to browse the selection of cards and purchase any they like the look of. They can also send a message requesting cards to be made to requirements. Users will be able to look at previous orders and update their delivery details if they register an account. Admin users can add, edit and delete products. Non-admin users are also able to add, edit and delete replies to the blog posts (they can only edit and delete replies that belong to them).

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
There is a one-to-many relationship between UserProfile and Order as one user can have many orders associated with them. The UserProfile table also has a one-to-one link with the built-in Django User model (shown here for demonstration purposes) as each user can have only one profile linked to them. The BlogPost table has a one-to-many relationship with Reply, which allows for multiple replies to a particular blog post. There is also a one-to-many relationship between the User model and the Reply table as one user may have many replies.<br><br>

The ContactUs table is standalone with no links to any other tables.<br><br>

The details for each model are as follows:

#### Blog app

- BlogPost<br>
![Image of blogpost model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/blogpost_model.JPG)

- Reply<br>
![Image of reply model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/reply_model.JPG)

#### Checkout app

- Order<br>
![Image of order model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/order_model.JPG)

- OrderLineItem<br>
![Image of orderlineitem model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/orderlineitem_model.JPG)

#### ContactUs app

- ContactUs<br>
![Image of contactus model](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/contactus_model.JPG)

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
Blog overview page:<br>
![Wireframe of mobile blog overview page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_blog_overview.JPG)<br>
Blog detail page:<br>
![Wireframe of mobile blog detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_blog_detail.JPG)<br>
Contact us page:<br>
![Wireframe of mobile contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_contact.JPG)<br>
Add product page:<br>
![Wireframe of mobile add product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_add_product.JPG)<br>
Edit product page:<br>
![Wireframe of mobile edit product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_mobile_edit_product.JPG)<br>
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
Blog overview page:<br>
![Wireframe of tablet blog overview page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_blog_overview.JPG)<br>
Blog detail page:<br>
![Wireframe of tablet blog detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_blog_detail.JPG)<br>
Contact us page:<br>
![Wireframe of tablet contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_contact.JPG)<br>
Add product page:<br>
![Wireframe of tablet add product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_add_product.JPG)<br>
Edit product page:<br>
![Wireframe of tablet edit product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_tablet_edit_product.JPG)<br>
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
Blog overview page:<br>
![Wireframe of desktop blog overview page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_blog_overview.JPG)<br>
Blog detail page:<br>
![Wireframe of desktop blog detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_blog_detail.JPG)<br>
Contact us page:<br>
![Wireframe of desktop contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_contact.JPG)<br>
Add product page:<br>
![Wireframe of desktop add product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_add_product.JPG)<br>
Edit product page:<br>
![Wireframe of desktop edit product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_edit_product.JPG)<br>
404 page:<br>
![Wireframe of desktop 404 page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/wireframe_desktop_404.JPG)<br>

<br>
For the final version of my site, the newsletter signup is on the left instead of the right now in the footer.
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
- As a site user I can reply to the blog posts so that I can express an opinion about them or add a comment 
- As a site user I can edit my replies to the blog posts so that I may update them if needed
- As a site user I can delete any of my replies to the blog posts so that I can remove them if I feel they’re no longer needed
- As a site admin I can manage product categories so that I may add, update or delete them as needed
- As a site admin I can manage products so that I may add, update or delete them as needed
- As a site admin I can manage user accounts so that any required changes to them can be made
- As a site admin I can view created orders so that they may be fulfilled, or amended if needs be
- As a site admin I can view messages submitted via the contact us section so that I may act upon them
- As a site admin I can manage the content on the “Tina's Blog” page so that it can be amended if needed

#### Returning users

- As a returning site user I can have a look whether any new products have been added so that I can decide if I want to buy any
- As a returning site user I can view my user profile (if I registered an account) so that I can see whether my details are still up-to-date and also view previous orders
- As a returning site user I can see whether any new blog posts and associated replies have been added
- As a returning site admin I can see whether any new messages have been submitted so that I can action them accordingly
- As a returning site admin I can look at whether any new orders have been placed so that I can fulfill or amend them as required
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

There is a blog overview page showing all blog posts at a glance:

![Image of blog overview page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/blog.JPG)<br>

Clicking on a particular blog post takes you to its detail page:

![Image of blog detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/blog_detail1.JPG)<br>

Logged in users can also post a reply to a blog post using the inline form for this:

![Image of blog detail page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/blog_detail2.JPG)<br>

Editing a blog reply is done via the same form:

![Image of blog reply edit page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/blog_reply_edit.JPG)<br>

Deleting a blog reply triggers the following confirmation page:

![Image of delete blog reply confirmation page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/delete_reply.JPG)<br>

There is a contact us page with a form to be filled out should a user wish to submit a message to the site admin:

![Image of contact us page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/contact_us.JPG)<br>

For admin users, there is a page to add new products:

![Image of add product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/add_product.JPG)<br>

Admin users can also edit products:

![Image of edit product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/edit_product.JPG)<br>

Deleting a product triggers the following confirmation page:

![Image of delete product confirmation page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/delete_product.JPG)<br>


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
    - Actual: From the basket page, you can click "Secure Checkout" to be taken to the checkout page (see above image for "Secure Checkout" button location)
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
- As a site user I can reply to the blog posts so that I can express an opinion about them or add a comment
    - Expected: There will be a form to submit a reply when viewing a blog post
    - Actual: On the blog post detail page, there is an inline form below the post that logged in users can use to post a reply
    ![Image of blog reply form](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/blog_detail2.JPG)<br>
- As a site user I can edit my replies to the blog posts so that I may update them if needed
    - Expected: There will be a function to edit an existing reply
    - Actual: On the blog post detail page, if the user clicks "Edit" on one of their replies, the inline form below the post is used for editing the reply
    ![Image of blog reply edit](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/blog_reply_edit.JPG)<br>
- As a site user I can delete any of my replies to the blog posts so that I can remove them if I feel they’re no longer needed
    - Expected: There will be a function to delete a reply
    - Actual: On the blog post detail page, if the user clicks "Delete" on one of their replies, they are shown a confirmation screen regarding the reply deletion
    ![Image of blog reply delete confirmation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/delete_reply.JPG)<br>
- As a site admin I can manage product categories so that I may add, update or delete them as needed
    - Expected: There will be an admin view where I can see the configured categories
    - Actual: Navigating to the admin page, which has a link visible to admin users from the "Account" dropdown, allows managing of the categories
    ![Image of category management page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/testing/manage_categories.JPG)<br>
- As a site admin I can manage products so that I may add, update or delete them as needed
    - Expected: There will be functionality to manage products
    - Actual: 
        - Adding products: From the "Account" dropdown, I can click "Product Management" as a logged in admin user to add a new product
        ![Image of add product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/add_product.JPG)<br>
        - Updating products: From either the product overview or product detail pages, I can click "Edit" on a product as a logged in admin user to update it
        ![Image of edit product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/edit_product.JPG)<br>
        - Deleting products: From either the product overview or product detail pages, I can click "Delete" on a product as a logged in admin user to delete it
        ![Image of delete product page](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/features/delete_product.JPG)<br>
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

During the development of my application, I encountered the following bugs which I managed to resolve in each case:

- While trying to adjust the nav links colour, I had forgotten to specifically target the "a" elements.
- The header logo wouldn't initially display when using src="{{ MEDIA_URL }}tqc-logo.png", this was due to the context processor "'django.template.context_processors.media'," not being present. Adding this corrected the issue.
- The logo on the mobile nav header wouldn't display initially, this was due to me adjusting the path on the main header but not the mobile one. Once set to src="{{ MEDIA_URL }}tqc-logo.png", this worked as expected. 
- When configuring the basket page to show product images, this would crash if a product had no image associated. This was corrected using an if statement to check for a product image and if none, display a "noimage" image instead. 
- When configuring the remove from basket functionality, I was getting a "CSRF token missing or invalid" error. This was due to my having put the associated JS into a separate file, turns out to be able to read the CSRF token, the script code needed to be directly in the template instead. 
- I had an issue where when browsing to the homepage, the Django messaging system was picking up and displaying the homepage welcome title and displaying it. This was due to my referencing “messages” to display the contents of the WelcomeMessage model. The fix was to rather display the text directly in the index.html template and remove the context from the “home” view.
- When configuring the checkout template, for the basket preview section, I mistakenly used the url “product_detail” which doesn’t exist and so got an error. Changing this to “product_details”, which does exist, fixed the issue.
- When defining the “update_total” method in the Order model, where I referenced the key [‘lineitem_total_sum’], this caused a key error. This needed to be set to [‘lineitem_total__sum’].
- While testing the Stripe webhook functionality in Gitpod, I initially was getting 401 errors and it didn’t seem to be reaching my test server. I needed to set port 8000 to public. 
- When trying to update my Order table to use the django-country field, the migration for this failed as I had existing orders that weren’t using a valid 2 digit code. Removing these orders (which were only test ones) allowed the migrate operation to complete successfully.
- My checkout wasn’t initially working once I’d deployed, this was because I’d forgotten to set the “STRIPE_PUBLIC_KEY”, “STRIPE_SECRET_KEY” and “STRIPE_WH_SECRET” environment variables on Heroku. 
- When configuring the profiles app, I had to temporarily adjust the signal for profile creation to create a profile for my user. Upon testing, and before setting the signal back to what it should be, I was getting errors about the user profile already existing (this was due to the signal trying to create a new profile regardless). Once the signal was reset to what it should be, the error was resolved.
- If you scroll all the way down on the products page, getting right to the bottom of the footer, the BTT button wouldn't work. Adding z-index of 1 fixed this.
- When configuring Summernote for the body field on the BlogPost model admin view, I forgot to add the URLs to the base URL file, resulting in a “Not found” error. Correctly adding the URLs to the base URL file fixed this.
- When configuring the blog overview template, the posts weren’t displaying as I intended, namely side by side on larger screens. This was due to me having put the containing div for the posts outside the for loop for generating the posts, rather than inside it. 
- When creating the blog detail page, which shows all related replies, I was initially getting an error regarding "‘RelatedManager’ object is not iterable" when trying to render the replies. This was due to my having referenced the associated replies in the view as "replies = post.blog_replies" instead of "replies = post.blog_replies.all()"

### Validator testing

- HTML
    - Home page:<br>
    ![Image of home page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/homepage_validate.JPG)<br>
    - Products page:<br>
    ![Image of product page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/products_validate.JPG)<br>
    - Product detail page:<br>
    ![Image of product detail page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/product_detail_validate.JPG)<br>
    The error noted is due to my having to use the "linebreaks" filter on the item description to allow it to display correctly.
    - Basket page:<br>
    ![Image of basket page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/basket_validate.JPG)<br>
    The error noted here is due to the fact that the basket page has a mobile view and one for larger screens, for this to work the required code 
    (which is in an include file) appears twice in the DOM.
    - Checkout page:<br>
    ![Image of checkout page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/checkout_validate.JPG)<br>
    The warning noted here is due to the structure of the overlay spinner, which appears while checkout is processing.
    - Checkout complete page:<br>
    ![Image of checkout complete page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/checkout_success_validate.JPG)<br>
    - Profile page:<br>
    ![Image of profile page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/profile_validate.JPG)<br>
    - Blog overview page:<br>
    ![Image of blog overview page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/blog_overview_validate.JPG)<br>
    - Blog detail page:<br>
    ![Image of blog detail page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/blog_detail_validate.JPG)<br>
    The error noted relates to my using Summernote to edit the body text in the admin view.
    - Blog reply delete page:<br>
    ![Image of blog reply delete page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/delete_reply_validate.JPG)<br>
    - Contact Us page:<br>
    ![Image of contact us page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/contact_us_validate.JPG)<br>
    - Add Product page:<br>
    ![Image of add product page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/add_product_validate.JPG)<br>
    - Edit Product page:<br>
    ![Image of edit product page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/edit_product_validate.JPG)<br>
    - Delete Product page:<br>
    ![Image of delete product page validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/html/delete_product_validate.JPG)<br>

- CSS
    - Base.css file:<br>
    ![Image of base.css validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/css/base_css_validate.JPG)<br>
    - Checkout.css file:<br>
    ![Image of checkout.css validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/css/checkout_css_validate.JPG)<br>
    - Profile.css file:<br>
    ![Image of profile.css validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/css/profile_css_validate.JPG)<br>

- JS
    - Quantity-input-script.js file:<br>
    ![Image of quantity-input-script.js validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/js/quantity_script_validate.JPG)<br>
    - Sort-selection.js file:<br>
    ![Image of sort-selction.js validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/js/sort_selector_validate.JPG)<br>
    - Stripe-elements.js file:<br>
    ![Image of stripe-elements.js validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/js/stripe_elements_js_validate.JPG)<br>
    - Update-remove.js file:<br>
    ![Image of update-remove.js validation](https://raw.githubusercontent.com/domsq/tina-q-cards/master/screenshots/validation/js/update_remove_js_validate.JPG)<br>

- Python
  - Please see below flake8 validation for the python files in my project. There are 3 warnings and 1 error, I was unable to correct the error without affecting functionality.<br>

    ./checkout/apps.py:9:9: F401 'checkout.signals' imported but unused<br>
    ./checkout/webhooks.py:24:5: F841 local variable 'e' is assigned to but never used<br>
    ./checkout/webhooks.py:27:5: F841 local variable 'e' is assigned to but never used<br>
    ./checkout/webhooks.py:39:80: E501 line too long (86 > 79 characters)<br>

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
- Heroku
    - Perform deployment on portal, await completion 

### Final deployment

- Gitpod
    - Ensure all required files up-to-date and that application is working
    - Run "pip3 freeze --local > requirements.txt" to update requirements file
    - Ensure "DEBUG = False" set in settings.py
    - Perform commit and push to GitHub
- Heroku
    - Under "tina-q-cards" app, browse to Config Vars
    - Remove the value "DISABLE_COLLECTSTATIC = 1" from Config Vars
    - Add new Config Vars entries for the following with appropriate values:
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY
        - EMAIL_HOST_PASS
        - EMAIL_HOST_USER
        - STRIPE_PUBLIC_KEY
        - STRIPE_SECRET_KEY
        - STRIPE_WH_SECRET
        - USE_AWS 
    - Browse to Deploy and run deployment
    - Wait for confirmation that app has deployed

## Credits 

### Content

All content, apart from the background image for the homepage, was created by the developer (with help from my wife, who assisted me with the colour scheme, logo and product images as we thought it would be nice to be able to showcase some of her handmade cards). Also, the Facebook business page was created by her some time back (although inactive) but repurposed for this project with her permission. The Instagram page linked to in the footer was already active and in use. 

### Media

Background image from [unsplash.com](https://unsplash.com/photos/nipbRVoEp18?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)

### Acknowledgements

In addition to the content from the LMS, and in particular the Boutique Ado walkthrough project which provided me with guidance and inspiration for my project, I made use of the following resources:

- https://www.youtube.com/watch?v=VADHdoPwKtw&t=134s
- https://docs.djangoproject.com/en/4.0/ref/settings/
- https://stackoverflow.com/questions/3346230/wrap-long-lines-in-python
- https://docs.djangoproject.com/en/4.0/ref/views/#the-404-page-not-found-view
- https://github.com/summernote/django-summernote
- https://stackoverflow.com/questions/10270891/newline-in-models-textfield-not-rendered-in-template

As always, many thanks to my mentor Akshat Garg for his invaluable advice and guidance. Earlier on in the design of my application, I had a model called "WelcomeMessage" for the homepage introduction text and also what is now "Tina's Blog" was originally going to be called "About Us". I removed "WelcomeMessage" and adjusted "About Us" to "Tina's Blog" following some discussion with Akshat.<br>
<br>
I'd also like to acknowledge the Code Institute Slack community, who helped me whenever I had a query about my project or something related. Thanks guys!