# [COMMUNITY HELPER](https://community-h3lp3r-3eca282c4ffe.herokuapp.com)

Need a hand? Have two? Or...at least one?

Let us try this again...have you ever played Stardew Valley and never got tired of bringing Willy 5 albacores in 2 days?

Well, in that case, our Community Helper is just the right thing for you.

If you need help with something, or if you can help someone, why not do it?

Simply post a task, or accept one, and you're ready to go!

![screenshot](documentation/readme/amiresponsive.png)


## UX

### Colour Scheme

Colour scheme was kept simple, with dominant dark green being used for text on otherwise white background.

- `#286638` used for primary text.

### Typography

We have used `Poppins` and `Montserrat` fonts throughout the website to create, both, familiarity using the similarities of the fonts, but also distinction between different types of text.

Their combination shows a kind of strict playfulness that fits perfectly with what we are trying to achieve.

- [Poppins](https://fonts.google.com/specimen/Poppins) was used for the headers.

- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout on the homepage.

## User Stories

### New Site Users

- As a user, I can read about the website goal so that I can decide if I want to sign up.
- As a potential user, I can view how many users/requests the website has so that I know if it's a real deal before signing up.
- As a user, I can register so that I can accepted or post tasks/requests.
- As a user, I can categorize my request so that I can receive help quicker.
- As a user, I can choose a deadline of my request so that I don't receive help when not needed.
- As a user, I can only choose future date for a deadline so that I don't accidentally choose a past date.
- As a user, I can submit a request so that I can receive help from the community.
- As a user, I can browse through requests so that I find a suitable one.
- As a user, I can navigate through pages of requests so that I can find a suitable one in order to accept it.
- As a user, I can see the correct date of task creation/editing so that I know when the last change was made.
- As a user, I can accept someone's request so that I can help the community.

### Mobile Users

- As a mobile user, I can click a 'go back up' button so that I can return to the top of the page instantly and not have to scroll.
- As a user using a smaller desktop screen, I can clearly see the mission statement so that I know what the page is about.

### Returning Site Users

- As a user, I can instantly recognise the Community Helper tab by it's favicon so that I avoid unnecessary clicks.
- As a user, I can login so that I can check on the progress of my task/request or accept a task/request.
- As a user, I can log out from the site so that I don't jeopardize my or someone else's information.
- As a user, I can ensure my own privacy with login being required for any sensitive areas of the website so that I can be at easy with my information and information of others.
- As a user, I can filter through requests so that I save time while looking for a suitable one.
- As a user, I can see the location of the owner so that I can decide if I want to open the task to read more about it and accept it.
- As a user, I can open an active request so that I can view it in full and decide if I want to accept it.
- As a user, I can see the same information when filtering as I would in a general task list so that I don't have to unnecessarily open all tasks to find out if they have an end date and their location.
- As a user, I can clearly see when I'm logged in so that I know to logout when necessary.
- As a user, I can navigate to a page with my active requests so that I can update them or be reminded of what needs doing.
- As a user who submitted the request, I can mark it as done so that I can keep better track of my requests.
- As a submitter/helper, I can comment on the request so that I can request an update/info.
- As a user, I can see that the comment form is visually similar to the task form so that I don't break the illusion of the brand.
- As a user who published a task, I can edit it so that I provide up to date information to a future helper.
- As a user who published a task, I can delete it so that I don't clog request list with something that is outdated/unneccessary.
- As a user, I can confirm that I want to delete my request so that I don't do it on accident.
- As a user, I can confirm that I want to mark a task as closed so that I don't do it accidentally.
- As a user, I can enter relevant information in my profile so that I don't have to repeat myself later on.
- As a user, I can see a notification that I've opened a page that doesn't exist so that I can navigate to where I actually wanted to go.

### Site Admin

- As an administrator, I can access admin panel so that I can monitor my page and edit necessary items.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
We've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
  - ![screenshot](documentation/readme/wireframes/mobile-homepage.png)

Create a Request
  - ![screenshot](documentation/readme/wireframes/mobile-make-a-request.png)

Ongoing Request
  - ![screenshot](documentation/readme/wireframes/mobile-ongoing-request.png)

Request List
  - ![screenshot](documentation/readme/wireframes/mobile-request-list.png)

Open Request
  - ![screenshot](documentation/readme/wireframes/mobile-specific-request.png)

</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Home
  - ![screenshot](documentation/readme/wireframes/desktop-homepage.png)

Create a Request
  - ![screenshot](documentation/readme/wireframes/desktop-make-a-request.png)

Ongoing Request
  - ![screenshot](documentation/readme/wireframes/desktop-ongoing-request.png)

Request List
  - ![screenshot](documentation/readme/wireframes/desktop-request-list.png)

Open Request
  - ![screenshot](documentation/readme/wireframes/desktop-specific-request.png)

</details>

### Deviation from the Wireframes

- Footer was originally planned as a constant feature present across all pages, however, as it only serves the purpose of validating the website for newer users, we have decided to remove it in order to maximise space.
- Subheading (Need a hand? Give a hand) was ommited to preserve a cleaner look.
- Special Instructions/directions were streamlined into user profile to prevent repetition.
- Mobile version of the request list is only slightly different, in order to maximise space.
- Mobile version of the homepage does not have fontawesome icons in order to maximise space - they are, however, available for the desktop users.
- Private messages, as noted within the wireframes, were not a part of the MVP, however, comment section was added to the ongoing tasks to compensate.

## Features

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you should go over the different parts of your project,
and describe each in a sentence or so.

You will need to explain what value each of the features provides for the user,
focusing on who this website is for, what it is that they want to achieve,
and how your project is the best way to help them achieve these things.

For some/all of your features, you may choose to reference the specific project files that implement them.

IMPORTANT: Remember to always include a screenshot of each individual feature!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Existing Features

- **Navbar**

    - Responsive navbar adjusts to the user's screen and maximises space saved all while allowing user to have everything available in up to two clicks.

![screenshot](documentation/readme/features/navbar.png)

- **Footer**

    - Footer displays the number of available tasks, successfully resolved tasks and a total number of users.
    - This is validating the website for a future user, all the while making current users' feel like they're contributing.

![screenshot](documentation/readme/features/footer.png)

- **Homepage**

    - Homepage allows the future user to understand the goal of the website.

![screenshot](documentation/readme/features/homepage.png)

- **Login confirmation**

    - Login confirmation allows users to know which account they are currently using, to ensure they don't mix up their accounts.

![screenshot](documentation/readme/features/login-confirm.png)

- **Task List**

    - Clicking on `Browse Requests` opens up a list of currently available tasks sorted from oldest to the newest.
    - Available tasks display title, 150 characters of user's request, as well as task category, deadline (when applicable) and location.

![screenshot](documentation/readme/features/open-tasks.png)

- **New Task**

    - User can create their own task. Should they forget to enter value in mandatory fields, they will be reminded. 
    - If user already created their profile, it will be auto-filled, but available for changes during task-creation.

![screenshot](documentation/readme/features/new-task.png)

- **User Profile**

    - Clicking on `Profile`, followed by `Your Profile`, user can create or update their profile.
    - This way, the user won't necessarily need to input all their details whenever they need to  create a task.
    - If user updates their profile after creating a task, the change will be visible on the already-created task(s).

![screenshot](documentation/readme/features/profile.png)

- **Own tasks**

    - Clicking on `Profile`, followed by `Check Requests`, user has access to all open tasks they have created or are helping on.
    - These tasks are separated into `Tasks you created` and `Tasks you are helping on` sections.

![screenshot](documentation/readme/features/own-tasks.png)

- **Pagination**

    - When browsing tasks, user can navigate between multiple pages easily in order to find a suitable task.

![screenshot](documentation/readme/features/pagination.png)

- **Task Filtering**

    - In order to facilitate quicker task-hunt, we have developed filtering option based on the task category.

![screenshot](documentation/readme/features/task-filtering.png)

- **Back To Top button**

    - When there are more than three filtered tasks on a smaller screen, back to top button is displayed.
    - Same feature is available when user is reviewing their own tasks, regardless of their number.

![screenshot](documentation/readme/features/back-to-top.png)

- **Edit Task**

    - Owner can update their task as long as there is no helper associated with it.
    - Date of update will be displayed from now on, however, task will remain sorted by the creation time to not punish the user for making changes.

![screenshot](documentation/readme/features/edit-task.gif)

- **Delete Task**

    - Owner can delete their task as long as there is no helper associated with it.

![screenshot](documentation/readme/features/delete-task.gif)

- **Ongoing task**

    - Task that has a helper but has not been archived yet is considered an ongoing one.
    - Owner and helper are the only ones with access to it, as it displays user's profile details.

![screenshot](documentation/readme/features/ongoing-task.png)

- **Comment**

    - Owner and helper can comment on a task. Along the comment, they can see when the comment was made.

![screenshot](documentation/readme/features/comment.gif)

- **Archive Task**

    - Once the task is done, owner can archive it.
    - This task is then counted in the footer under successful requests.

![screenshot](documentation/readme/features/archive-task.gif)

- **Accept a task**

    - User who is not task owner can accept a task. 
    - This way they get access to full task details and can communicate with the owner.

![screenshot](documentation/readme/features/accept-task.png)

- **Title for feature #3**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/readme/features/profile.png)

- **Title for feature #1**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/readme/features/profile.png)

- **Title for feature #2**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/readme/features/profile.png)

- **Title for feature #3**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/readme/features/profile.png)

- **Title for feature #1**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/readme/features/profile.png)

- **Title for feature #2**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/readme/features/profile.png)

- **Title for feature #3**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/readme/features/profile.png)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Repeat as necessary for as many features as your site contains.

Hint: the more, the merrier!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Future Features

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Do you have additional ideas that you'd like to include on your project in the future?
Fantastic! List them here!
It's always great to have plans for future improvements!
Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- Title for future feature #1
    - Any additional notes about this feature.
- Title for future feature #2
    - Any additional notes about this feature.
- Title for future feature #3
    - Any additional notes about this feature.

## Tools & Technologies Used

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you should explain the various tools and technologies used to develop the project.
Make sure to put a link (where applicable) to the source, and explain what each was used for.
Some examples have been provided, but this is just a sample only, your project might've used others.
Feel free to delete any unused items below as necessary.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Codeanywhere](https://codeanywhere.com) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Materialize](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [SQLAlchemy](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Using your defined models (one example below), create an ERD with the relationships identified.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

```python
class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

A couple recommendations for building free ERDs:
- [Draw.io](https://draw.io)
- [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

![screenshot](documentation/erd.png)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Using Markdown formatting to represent an example ERD table using the Product model above:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- Table: **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | category | ForeignKey | FK to **Category** model |
    | | sku | CharField | |
    | | name | CharField | |
    | | description | TextField | |
    | | has_sizes | BooleanField | |
    | | price | DecimalField | |
    | | rating | DecimalField | |
    | | image_url | URLField | |
    | | image | ImageField | |

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/josipcodes/community-helper/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Consider adding a basic screenshot of your Projects Board.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/josipcodes/community-helper/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Consider adding a screenshot of your Open and Closed Issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- [Open Issues](https://github.com/josipcodes/community-helper/issues)

    ![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/josipcodes/community-helper/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**IMPORTANT:**

- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️
- ⚠️ DO NOT update the environment variables to your own! These should NOT be included in this file; just demo values! ⚠️

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

The live deployed application can be found deployed on [Heroku](https://community-h3lp3r-3eca282c4ffe.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: community-helper).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/josipcodes/community-helper) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/josipcodes/community-helper.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/josipcodes/community-helper)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/josipcodes/community-helper)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Credits

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Content

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project, especially when self-doubt kicked in.