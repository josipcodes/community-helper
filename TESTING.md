# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.


| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2F) | ![screenshot](documentation/testing/html/homepage.png) | Pass: No Errors |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/html/login.png) | Pass: No Errors |
| Signup | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/html/signup.png) | Pass: No Errors |
| Open Tasks | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Fopen-tasks%2F) | ![screenshot](documentation/testing/html/open-tasks.png) | Pass: No Errors |

Below pages were validated through a manual input as they required user to be logged in. Code was obtained by selecting **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).

As such, W3C links are purely informational.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Logout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Faccounts%2Flogout%2F) | ![screenshot](documentation/testing/html/logout.png) | Pass: No Errors |
| Display Task | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Fdisplay-task%2F42) | ![screenshot](documentation/testing/html/display-task.png) | Input cannot be a child of anchor, fixed |
| Edit Task | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Fedit-task%2F42) | ![screenshot](documentation/testing/html/edit-task.png) | Section lacks heading, fixed |
| Delete Task | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Fdelete-task%2F42) | ![screenshot](documentation/testing/html/delete-task.png) | Pass: No Errors |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Fprofile%2F) | ![screenshot](documentation/testing/html/profile.png) | Pass: No Errors |
| Own Task list | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Ftask-list%2F) | ![screenshot](documentation/testing/html/task-list.png) | Pass: No Errors |
| New Task | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Fsubmission%2F) | ![screenshot](documentation/testing/html/new-task.png) | Nested form, fixed |
| Ongoing Task | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Fongoing-task%2F74) | ![screenshot](documentation/testing/html/ongoing-task.png) | Pass: No Errors |
| Filter | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2Ffilter%2F) | ![screenshot](documentation/testing/html/filter.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

All errors are coming from Bootstrap:

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcommunity-h3lp3r-3eca282c4ffe.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/testing/css/validation.png) | 1 is not a aspect-ratio value : 1, fixed |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate JS used within `script` elements of HTML documents.

| File | Screenshot | Notes |
| --- | --- | --- |
| edit_task.html | ![screenshot](documentation/testing/js/validation.png) | Pass: No Errors |
| create_task.html | ![screenshot](documentation/testing/js/validation.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Board admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/josipcodes/community-helper/main/board/admin.py) | ![screenshot](documentation/testing/python/board-admin.png) | Pass: No Errors |
| Board forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/josipcodes/community-helper/main/board/forms.py) | ![screenshot](documentation/testing/python/board-forms.png) | Pass: No Errors |
| Board models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/josipcodes/community-helper/main/board/models.py) | ![screenshot](documentation/testing/python/board-models.png) | Pass: No Errors |
| Board urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/josipcodes/community-helper/main/board/urls.py) | ![screenshot](documentation/testing/python/board-urls.png) | Pass: No Errors |
| Board views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/josipcodes/community-helper/main/board/views.py) | ![screenshot](documentation/testing/python/board-views.png) | Pass: No Errors |
| Community Helper settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/josipcodes/community-helper/main/communityhelper/settings.py) | ![screenshot](documentation/testing/python/communityhelper-settings.png) | Pass: No Errors |
| Community Helper urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/josipcodes/community-helper/main/communityhelper/urls.py) | ![screenshot](documentation/testing/python/communityhelper-urls.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

Browsers used:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Brave](https://brave.com/download)

| Browser | Home | Task List | New Task | Profile | Own Tasks | Edit Task | Show Task | Ongoing Task | Login | 404 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/compatibility/chrome/homepage.png) | ![screenshot](documentation/testing/compatibility/chrome/task-list.png) | ![screenshot](documentation/testing/compatibility/chrome/new-task.png) | ![screenshot](documentation/testing/compatibility/chrome/profile.png) | ![screenshot](documentation/testing/compatibility/chrome/own-tasks.png) | ![screenshot](documentation/testing/compatibility/chrome/edit-task.png) | ![screenshot](documentation/testing/compatibility/chrome/show-task.png) | ![screenshot](documentation/testing/compatibility/chrome/ongoing-task.png) | ![screenshot](documentation/testing/compatibility/chrome/login.png) | ![screenshot](documentation/testing/compatibility/chrome/404.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/compatibility/firefox/homepage.png) | ![screenshot](documentation/testing/compatibility/firefox/task-list.png) | ![screenshot](documentation/testing/compatibility/firefox/new-task.png) | ![screenshot](documentation/testing/compatibility/firefox/profile.png) | ![screenshot](documentation/testing/compatibility/firefox/own-tasks.png) | ![screenshot](documentation/testing/compatibility/firefox/edit-task.png) | ![screenshot](documentation/testing/compatibility/firefox/show-task.png) | ![screenshot](documentation/testing/compatibility/firefox/ongoing-task.png) | ![screenshot](documentation/testing/compatibility/firefox/login.png) | ![screenshot](documentation/testing/compatibility/firefox/404.png) | Works as expected |
| Brave | ![screenshot](documentation/testing/compatibility/brave/homepage.png) | ![screenshot](documentation/testing/compatibility/brave/task-list.png) | ![screenshot](documentation/testing/compatibility/brave/new-task.png) | ![screenshot](documentation/testing/compatibility/brave/profile.png) | ![screenshot](documentation/testing/compatibility/brave/own-tasks.png) | ![screenshot](documentation/testing/compatibility/brave/edit-task.png) | ![screenshot](documentation/testing/compatibility/brave/show-task.png) | ![screenshot](documentation/testing/compatibility/brave/ongoing-task.png) | ![screenshot](documentation/testing/compatibility/brave/login.png) | ![screenshot](documentation/testing/compatibility/brave/404.png) | Works as expected |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | New Task | Own Tasks | Show Task | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/responsiveness/samsung/homepage.png) | ![screenshot](documentation/testing/responsiveness/samsung/new-task.png) | ![screenshot](documentation/testing/responsiveness/samsung/own-tasks.png) | ![screenshot](documentation/testing/responsiveness/samsung/show-task.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/responsiveness/surface/homepage.png) | ![screenshot](documentation/testing/responsiveness/surface/new-task.png) | ![screenshot](documentation/testing/responsiveness/surface/own-tasks.png) | ![screenshot](documentation/testing/responsiveness/surface/show-task.png) | Works as expected |
| Desktop | ![screenshot](documentation/testing/responsiveness/desktop/homepage.png) | ![screenshot](documentation/testing/responsiveness/desktop/new-task.png) | ![screenshot](documentation/testing/responsiveness/desktop/own-tasks.png) | ![screenshot](documentation/testing/responsiveness/desktop/show-task.png) | Works as expected |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Homepage | ![screenshot](documentation//testing/lighthouse/mobile-homepage.png) | ![screenshot](documentation//testing/lighthouse/desktop-homepage.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Signup | ![screenshot](documentation//testing/lighthouse/mobile-signup.png) | ![screenshot](documentation//testing/lighthouse/desktop-signup.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Login | ![screenshot](documentation//testing/lighthouse/mobile-login.png) | ![screenshot](documentation//testing/lighthouse/desktop-login.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Logout | ![screenshot](documentation//testing/lighthouse/mobile-logout.png) | ![screenshot](documentation//testing/lighthouse/desktop-logout.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Browse Tasks | ![screenshot](documentation//testing/lighthouse/mobile-browse.png) | ![screenshot](documentation//testing/lighthouse/desktop-browse.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Create a Task | ![screenshot](documentation//testing/lighthouse/mobile-create.png) | ![screenshot](documentation//testing/lighthouse/desktop-create.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Profile | ![screenshot](documentation//testing/lighthouse/mobile-profile.png) | ![screenshot](documentation//testing/lighthouse/desktop-profile.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Own Tasks | ![screenshot](documentation//testing/lighthouse/mobile-own.png) | ![screenshot](documentation//testing/lighthouse/desktop-own.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Show Task | ![screenshot](documentation//testing/lighthouse/mobile-show.png) | ![screenshot](documentation//testing/lighthouse/desktop-show.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Ongoing task | ![screenshot](documentation//testing/lighthouse/mobile-ongoing.png) | ![screenshot](documentation//testing/lighthouse/desktop-ongoing.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Edit Task | ![screenshot](documentation//testing/lighthouse/mobile-edit.png) | ![screenshot](documentation//testing/lighthouse/desktop-edit.png) | Render-blocking resources, image sizing, unused CSS, JS |
| Delete Task | ![screenshot](documentation//testing/lighthouse/mobile-delete.png) | ![screenshot](documentation//testing/lighthouse/desktop-delete.png) | Render-blocking resources, image sizing, unused CSS, JS |

To note, during Lighthouse Audit, Lighthouse was providing bingo-like numbers with their values changing significantly between each audit of the same page.

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Screenshot | Comments |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Click on Logo | Redirection to Home page | Pass | ![screenshot](documentation/testing/features/logo.gif) | |
| | Click on Register | Redirection to signup page | Pass | ![screenshot](documentation/testing/features/register.gif) | |
| | Click on Login | Redirection to login page | Pass | ![screenshot](documentation/testing/features/login.gif) | |
| | Click on Browse Requests | Redirection to task list | Pass | ![screenshot](documentation/testing/features/browse.gif) | |
| | Create a task | Updates Open requests in footer, adds a success message below the header image | Pass | ![screenshot](documentation/testing/features/new-task-footer.gif) | |
| | Archive Task | Updates Successful requests in footer | Pass | ![screenshot](documentation/testing/features/successful-task-footer.gif) | |
| | Create a User | Updates Friends in footer | Pass | ![screenshot](documentation/testing/features/new-user.gif) | |
| | Delete a Task | Updates Open requests in footer, adds a success message below the header image | Pass | ![screenshot](documentation/testing/features/deleted-task-footer.gif) | |
| | Delete a User | Updates Open and Successful requests, Friends | Pass | ![screenshot](documentation/testing/features/deleted-user-footer.gif) | |
| | Click on Your Profile | Redirection to the profile | Pass | ![screenshot](documentation/testing/features/open-profile.gif) | |
| | Click on Check Requests | Redirection to own task list | Pass | ![screenshot](documentation/testing/features/check-requests.gif) | |
| | Click on Logout | Redirection to sign-out page | Pass | ![screenshot](documentation/testing/features/sign-out.gif) | |
| Signup | | | | | | 
| | Enter a password without a username | Prompt user to enter a username | Pass | ![screenshot](documentation/testing/features/signup.gif) | |
| | Enter an existing username | Notify user that the username is taken | Pass | ![screenshot](documentation/testing/features/signup.gif) | |
| | Enter an invalid username | Notify user about invalid characters | Pass | ![screenshot](documentation/testing/features/signup.gif) | |
| | Enter an invalid email address | Prompt user to enter a valid email address | Pass | ![screenshot](documentation/testing/features/signup.gif) | |
| | Enter an invalid password | Prompt user to enter a valid password | Pass | ![screenshot](documentation/testing/features/signup.gif) | |
| | Create an account with/out email address | Create account, redirection to homepage, success message displayed below the header image | Pass | ![screenshot](documentation/testing/features/signup.gif) | |
| | Click on Sign-in | Redirection to login page | Pass | ![screenshot](documentation/testing/features/signup-sign-in.gif) | |
|Sign In | | | | | | 
| | Input password without a username | Prompt user to enter a username | Pass | ![screenshot](documentation/testing/features/sign-in.gif) | |
| | Input a username and invalid password | Notify user that the details aren't correct | Pass | ![screenshot](documentation/testing/features/sign-in.gif) | |
| | Input correct login details | Log user in, redirection to homepage, display success message below the header image | Pass | ![screenshot](documentation/testing/features/sign-in.gif) | |
| | Click on Sign up | Redirection to signup page | Pass | ![screenshot](documentation/testing/features/sign-in-signup.gif) | |
| Sign Out | | | | | | 
| | Click on Sign Out button | User is signed out, redirection to the homepage, success message is displayed below header image | Pass | ![screenshot](documentation/testing/features/signed-out.gif) | |
| Browse Requests | | | | | | 
| | Click on a task | Redirection to the task display | Pass | ![screenshot](documentation/testing/features/open-task.gif) | |
| | Click on the Filter button | Redirection to task filtering | Pass | ![screenshot](documentation/testing/features/filter-button.gif) | |
| | Click on a different page number | Redirection to another page of task list | Pass | ![screenshot](documentation/testing/features/pagination.gif) | |
| | Click on a task when logged out | Redirection to login | Pass | ![screenshot](documentation/testing/features/login-redirect.gif) | |
| | Task in the list has a deadline | Deadline is displayed | Pass | ![screenshot](documentation/testing/features/browse-dates.png) | |
| | Task in the list doesn't have a deadline | Deadline isn't displayed | Pass | ![screenshot](documentation/testing/features/browse-dates.png) | |
| Profile | | | | | | 
| | When user has no profile, submit empty form | Prompt user to input value into the first empty field | Pass | ![screenshot](documentation/testing/features/profile.gif) | |
| | When user has no profile, submit form with any fields being empty | Prompt user to input value into the first empty field | Pass | ![screenshot](documentation/testing/features/profile.gif) | |
| | Add value to each field and submit form | Reloads the page, adds success message below the header image | Pass | ![screenshot](documentation/testing/features/profile.gif) | We have not enforced minimum character value, nor rules regarding certain fields not being allowed to have numberical values entered as some users might not want to add their private details |
| | When user has an existing profile, update fields to not contain value |  Prompt user to input value into the first empty field | Pass | ![screenshot](documentation/testing/features/update-profile.gif) | |
| | Update all values | Reloads the page, adds success message below the header image | Pass | ![screenshot](documentation/testing/features/update-profile.gif) | |
| | When logged out, add /profile to the url to attempt brute-force entry | Redirection to login page | Pass | ![screenshot](documentation/testing/features/brute-profile.png) | |
| Filter Task | | | | | | 
| | Click filter without choosing a category | Displays a warning message | Pass | ![screenshot](documentation/testing/features/filter.gif) | |
| | Click filter after choosing a valid category | Renders available tasks in the filtered category | Pass | ![screenshot](documentation/testing/features/filter.gif) | |
| | Click filter after choosing a category without any tasks | Renders a notification stating there are no tasks in a chosen category | Pass | ![screenshot](documentation/testing/features/filter.gif) | |
| | Click on a filtered task | Redirection to the task display | Pass | ![screenshot](documentation/testing/features/filter-task.gif) | |
| | Filter categories for one with more than 3 tasks | Displays a 'Back to Top' button | Pass | ![screenshot](documentation/testing/features/filter-back-to-top.gif) | Use screen equal to or less than 767px wide |
| | Filter categories for one with equal to or less than 3 tasks | Doesn't display a 'Back to Top' button | Pass | ![screenshot](documentation/testing/features/filter-back-to-top.gif) | Use screen equal to or less than 767px wide |
| | Click 'Back To Top' button | Takes user to the top of the page | Pass | ![screenshot](documentation/testing/features/filter-back-to-top.gif) | Use screen equal to or less than 767px wide |
| | When logged out, manually input url leading to a filter to attempt brute-force entry | Redirection to login page | Pass | ![screenshot](documentation/testing/features/brute-filter.gif) | |
| Own Tasks | | | | | | 
| | Click on a task you've created | Redirection to the task page | Pass | ![screenshot](documentation/testing/features/own-task-open.gif) | If the task has a helper, it is considered ongoing task, otherwise we're rendering display-task page |
| | Click on a task you're helping on | Redirection to ongoing task page | Pass | ![screenshot](documentation/testing/features/own-task-open.gif) | |
| | Use screen equal to or less than 767px wide when you have some tasks you are working on | Display 'Back To Top' button | Pass | ![screenshot](documentation/testing/features/own-back-to-top.gif) | |
| | Use screen wider than 767px when you have some tasks you are working on | Doesn't display 'Back To Top' button | Pass | ![screenshot](documentation/testing/features/own-back-to-top.gif) | |
| | Click 'Back To Top' button | Takes user to the top of the page | Pass | ![screenshot](documentation/testing/features/own-back-to-top.gif) | Use screen equal to or less than 767px wide |
| | When you're not working on any tasks, click on 'Check Requests' | Displays notes stating there are no tasks in the list | Pass | ![screenshot](documentation/testing/features/own-none.png) | |
| | When you're not working on any tasks, and in own task-list, click on "we're here for you" | Redirection to submission | Pass | ![screenshot](documentation/testing/features/own-none-links.gif) | |
| | When you're not working on any tasks, and in own task-list, click on "here you go" | Redirection to general task list | Pass | ![screenshot](documentation/testing/features/own-none-links.gif) | |
| | When not logged in, input a url taking you to the own task list | Redirection to login | Pass | ![screenshot](documentation/testing/features/brute-own.gif) | |
| Task Display | | | | | | 
| | Click on a task in 'Browse Requests' which you are not an owner of | Displays task with 'Accept a Task' button | Pass | ![screenshot](documentation/testing/features/display-tasks.gif) | |
| | Click on a task in 'Browse Requests' which you are an owner of | Displays task with 'Edit' and 'Delete' buttons | Pass | ![screenshot](documentation/testing/features/display-tasks.gif) | |
| | Click on a task in 'Browse Requests' which you are not an owner of, then click 'Accept' button | Redirection to homepage, success message displayed below the header image | Pass | ![screenshot](documentation/testing/features/display-tasks-buttons.gif) | Secondary verification is available in the own task list where user can see they are now a helper on said task |
| | Click on a task in 'Browse Requests' which you are an owner of, then click 'Edit' button | Redirection to edit-task page | Pass | ![screenshot](documentation/testing/features/display-tasks-buttons.gif) | |
| | Click on a task in 'Browse Requests' which you are an owner of, then click 'Delete' button | Redirection to delete-task page | Pass | ![screenshot](documentation/testing/features/display-tasks-buttons.gif) | |
| | When logged out, manually input url leading to a display-task to attempt brute-force entry | Redirection to sign-in page | Pass | ![screenshot](documentation/testing/features/brute-display-logged-out.gif) | |
| Create Task | | | | | | 
| | With a new account, leave each field blank and click submit | Prompts user to enter information into required fields (all except Deadline) | Pass | ![screenshot](documentation/testing/features/create-task-profile.gif) | |
| | Click submit after entering valid info | Redirection to own tasks with task being visible there, success message displays below header image | Pass | ![screenshot](documentation/testing/features/create-task-profile.gif) | |
| | With existing profile, add task information and change profile information before clicking Submit | Creates task, updates profile, success message displays below header image | Pass | ![screenshot](documentation/testing/features/create-task-update-profile.gif) |Profile update is visible by Location in the task, or in the Profile |
| | Input valid data when creating a task, but set date to a past date manually | Prompts user to enter a valid date | Pass | ![screenshot](documentation/testing/features/create-task-dates.gif) | |
| | Manually enter an url taking you to the submission page | Redirection to login | Pass | ![screenshot](documentation/testing/features/brute-submission.gif) | |
| Edit Task | | | | | | 
| | Leave Title, Description or Category empty and click Update button | Prompt user to input value | Pass | ![screenshot](documentation/testing/features/edit-task-fields.gif) | |
| | Set a deadline to a past date manually and click Update button | Prompt user to input a current or future date | Pass | ![screenshot](documentation/testing/features/edit-task-fields.gif) | |
| | Input new valid data into all fields and click Update button | Edits the task, displays success message below the header image, redirection to task display with new data visible. Date and time of update displays within the task. | Pass | ![screenshot](documentation/testing/features/edit-task-fields.gif) | |
| | Clear deadline date and click Update button | Edits the task, displays success message below the header image, redirection to task display with new data visible. Date and time of update displays within the task. | Pass | ![screenshot](documentation/testing/features/clear-date.gif) | |
| | Manually input url leading to a task-editing page for a task you're a helper on, to attempt brute-force entry | Redirection to own task list, warning message displays below the header image | Pass | ![screenshot](documentation/testing/features/brute-edit-task.gif) | |
| | Manually input url leading to a task-editing page for a task which is not yours nor has a helper assigned, to attempt brute-force entry | Redirection to own task list, warning message displays below the header image | Pass | ![screenshot](documentation/testing/features/brute-edit-task.gif) | |
| | When logged out, manually input url leading to a task-editing page to attempt brute-force entry | Redirection to sign-in page | Pass | ![screenshot](documentation/testing/features/brute-edit-task.gif) | |
| Delete Task | | | | | | 
| | Click on 'I am sure, delete it' button | Redirection to the own task list, success message displays below the header image, task is no longer available in the own task section | Pass | ![screenshot](documentation/testing/features/own-task-deleted.gif) | |
| | Manually input url leading to a task-deletion page for a task you're a helper on, to attempt brute-force entry | Redirection to own task list, warning message displays below the header image | Pass | ![screenshot](documentation/testing/features/brute-helper-deleting-task.gif) | |
| | Manually input url leading to a task-deletion page for a task which is not yours nor has a helper assigned, to attempt brute-force entry | Redirection to own task list, warning message displays below the header image | Pass | ![screenshot](documentation/testing/features/brute-delete-task.gif) | |
| | Manually input url leading to a task-deletion page for a task which you've previously archived, to attempt brute-force entry | Redirection to own task list, warning message displays below the header image | Pass | ![screenshot](documentation/testing/features/brute-delete-archived.gif) | |
| | When logged out, manually input url leading to a task-deletion page to attempt brute-force entry | Redirection to sign-in page | Pass | ![screenshot](documentation/testing/features/brute-delete-logged-out.gif) | |
| Archive Task | | | | | | 
| | Click on a 'Mark task as finished' button of which you're the owner and has assigned helper | Redirection to own task list, displays success message below the header image | Pass | ![screenshot](documentation/testing/features/archive-task.gif) | |
| | Click on a 'Go back' button | Redirection to the ongoing task | Pass | ![screenshot](documentation/testing/features/archive-go-back.gif) | |
| | Manually input url leading to a task-archiving page for an already archived task you own | Redirection to own task list, warning message displays below the header image | Fail | ![screenshot](documentation/testing/features/archive-fix.gif) | added a task.status condition in archive_task view, passed after the fix |
| | Manually input url leading to a task-archiving page for a task you own but has no helper | Redirection to own task list, warning message displays below the header image | Fail | ![screenshot](documentation/testing/features/archive-fix.gif) | added a task.status condition in archive_task view, passed after the fix |
| | Manually input url leading to a task-archiving page you are a helper on, to attempt brute-force entry | Redirection to own task list, warning message displays below the header image | Pass | ![screenshot](documentation/testing/features/brute-archive.gif) | |
| | Manually input url leading to a task-archiving page you are not associated with, to attempt brute-force entry | Redirection to own task list, warning message displays below the header image | Pass | ![screenshot](documentation/testing/features/brute-archive.gif) | |
| | When logged out, manually input url leading to a task-archiving page to attempt brute-force entry | Redirection to sign-in page | Pass | ![screenshot](documentation/testing/features/brute-archive.gif) | |
| Ongoing Task | | | | | | 
| | Input a comment and click Comment | Reloads the page, displays a comment below the Comment button, displays a success message below the header image. | Pass | ![screenshot](documentation/testing/features/ongoing-comment.gif) | |
| | Open a task which you are an owner of and has a helper | 'Mark Task as Done' button is displayed | Pass | ![screenshot](documentation/testing/features/ongoing-comment.gif) | |
| | Open a task which you are an owner of and has a helper, click 'Mark Task as Done' | Redirection to archive task page | Pass | ![screenshot](documentation/testing/features/ongoing-done.gif) | |
| | Open a task which you are an owner of or a helper on, and task has both | Owner's location is displayed | Pass | ![screenshot](documentation/testing/features/ongoing-details.gif) | |
| | Open a task which you are a helper on, and task has both | 'Mark Task as Done' button is not displayed | Pass | ![screenshot](documentation/testing/features/ongoing-details.gif) | |
| | Manually input a url taking you to an ongoing task that you are not participating on | Redirection to own task list with warning message displayed below the header image | Pass | ![screenshot](documentation/testing/features/brute-ongoing.gif) | |
| | Manually input a url taking you to an ongoing task when logged out | Redirection to login | Pass | ![screenshot](documentation/testing/features/brute-ongoing-logged-out.gif) | |
| | Manually input a url taking you to an ongoing task which you previously marked as archived | Redirection to own task list, warning message displayed below the header image | Pass | ![screenshot](documentation/testing/features/brute-ongoing-archived.gif) | |
| | Open a task from 'Browse Requests' and replace 'display' in url with 'ongoing' | Redirection to own task list, warning message displayed below the header image | Pass | ![screenshot](documentation/testing/features/brute-display-ongoing.gif) | |

## User Story Testing

### New Site Users

| User Story | Screenshot |
| --- | --- |
| As a user, I can read about the website goal so that I can decide if I want to sign up. | ![screenshot](documentation/readme/features/homepage.png) |
| As a potential user, I can view how many users/requests the website has so that I know if it's a real deal before signing up. | ![screenshot](documentation/readme/features/footer.png) |
| As a user, I can register so that I can accept or post tasks/requests. | ![screenshot](documentation/testing/features/sign-in.gif) |
| As a user, I can categorize my request so that I can receive help quicker. | ![screenshot](documentation/testing/features/create-task-update-profile.gif) |
| As a user, I can choose a deadline of my request so that I don't receive help when not needed. | ![screenshot](documentation/testing/features/create-task-dates.gif) |
| As a user, I can only choose future date for a deadline so that I don't accidentally choose a past date. | ![screenshot](documentation/testing/features/create-task-dates.gif) |
| As a user, I can submit a request so that I can receive help from the community. | ![screenshot](documentation/testing/features/create-task-update-profile.gif) |
| As a user, I can browse through requests so that I find a suitable one. | ![screenshot](documentation/testing/features/browse.gif) |
| As a user, I can navigate through pages of requests so that I can find a suitable one in order to accept it. | ![screenshot](documentation/testing/features/pagination.gif) |
| As a user, I can see the correct date of task creation/editing so that I know when the last change was made. | ![screenshot](documentation/testing/features/edit-task-fields.gif) |
| As a user, I can accept someone's request so that I can help the community. | ![screenshot](documentation/testing/features/display-tasks-buttons.gif) |

### Mobile Users

| User Story | Screenshot |
| --- | --- |
| As a mobile user, I can click a 'go back up' button so that I can return to the top of the page instantly and not have to scroll. | ![screenshot](documentation/testing/features/own-back-to-top.gif) |
| As a user using a smaller desktop screen, I can clearly see the mission statement so that I know what the page is about. | ![screenshot](documentation/testing/features/mission-statement.png) |

### Returning Site Users

| User Story | Screenshot |
| --- | --- |
| As a user, I can instantly recognise the Community Helper tab by it's favicon so that I avoid unnecessary clicks. | ![screenshot](documentation/readme/features/favicon.png) |
| As a user, I can login so that I can check on the progress of my task/request or accept a task/request. | ![screenshot](documentation/testing/features/sign-in.gif) |
| As a user, I can log out from the site so that I don't jeopardize my or someone else's information. | ![screenshot](documentation/testing/features/signed-out.gif) |
| As a user, I can ensure my own privacy with login being required for any sensitive areas of the website so that I can be at ease with my information and information of others. | ![screenshot](documentation/testing/features/brute-display-logged-out.gif) |
| As a user, I can filter through requests so that I save time while looking for a suitable one. | ![screenshot](documentation/testing/features/filter.gif) |
| As a user, I can see the location of the owner so that I can decide if I want to open the task to read more about it and accept it. | ![screenshot](documentation/testing/features/display-tasks.gif) |
| As a user, I can open an active request so that I can view it in full and decide if I want to accept it. | ![screenshot](documentation/testing/features/display-tasks.gif) |
| As a user, I can see the same information when filtering as I would in a general task list so that I don't have to unnecessarily open all tasks to find out if they have an end date and their location. | ![screenshot](documentation/testing/features/filter.gif) |
| As a user, I can clearly see when I'm logged in so that I know to logout when necessary. | ![screenshot](documentation/readme/features/login-confirm.png) |
| As a user, I can navigate to a page with my active requests so that I can update them or be reminded of what needs doing. | ![screenshot](documentation/testing/features/check-requests.gif) |
| As a user who submitted the request, I can mark it as done so that I can keep better track of my requests. | ![screenshot](documentation/testing/features/archive-task.gif) |
| As a submitter/helper, I can comment on the request so that I can request an update/info. | ![screenshot](documentation/testing/features/ongoing-comment.gif) |
| As a user, I can see that the comment form is visually similar to the task form so that I don't break the illusion of the brand. | ![screenshot](documentation/testing/features/ongoing-comment.gif) |
| As a user who published a task, I can edit it so that I provide up to date information to a future helper. | ![screenshot](documentation/testing/features/edit-task-fields.gif) |
| As a user who published a task, I can delete it so that I don't clog request list with something that is outdated/unneccessary. | ![screenshot](documentation/testing/features/own-task-deleted.gif) |
| As a user, I can confirm that I want to delete my request so that I don't do it on accident. | ![screenshot](documentation/testing/features/own-task-deleted.gif) |
| As a user, I can confirm that I want to mark a task as closed so that I don't do it accidentally. | ![screenshot](documentation/testing/features/archive-task.gif) |
| As a user, I can enter relevant information in my profile so that I don't have to repeat myself later on. | ![screenshot](documentation/testing/features/profile.gif) |
| As a user, I can see a notification that I've opened a page that doesn't exist so that I can navigate to where I actually wanted to go. | ![screenshot](documentation/readme/features/404.png) |

### Site Admin

| User Story | Screenshot |
| --- | --- |
| As an administrator, I can access admin panel so that I can monitor my page and edit necessary items. | ![screenshot](documentation/readme/features/admin.png) |

## Bugs

- Contents of a comment remain in the form after it has been published.

[Documented bug](https://github.com/josipcodes/community-helper/issues/43)
    
    - To fix this, I have added an empty `form` into the `context`, however, this fix was refactored later on.

- `Pagination` is displayed over content.

[Documented bug](https://github.com/josipcodes/community-helper/issues/37)

    - To fix this, I have removed `fixed-bottom class` from the pagination `div`.

- `Footer` covers content on <=575px width.

[Documented bug](https://github.com/josipcodes/community-helper/issues/33)

    - To fix this, I have added `footer margin` using `CSS`.

- Styling changes when user is logged in or logged out.

[Documented bug](https://github.com/josipcodes/community-helper/issues/29)

    - To fix this, I have created a class `task-link` and associted it with existing CSS rule regarding link display.

- Navbar links change position when user is logged in or logged out.

[Documented bug](https://github.com/josipcodes/community-helper/issues/28)

    - To fix this, I have removed `me-auto class` from the affected `ul`.

- Overflow x when user opens the dropdown menu.

[Documented bug](https://github.com/josipcodes/community-helper/issues/22)
[Related user story](https://github.com/josipcodes/community-helper/issues/21)

    - To present a true Agile approach, this bug was prioritised due to existence of a user story which presented a type of fix. As such, we have included a template which confirms user's username when logged in, depending on their screen size.

```
    {% include "login_confirm.html" %}

    <span class="brand-color">
        Logged in as {{ user.username }}
    </span>
```

### GitHub **Issues**

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/josipcodes/community-helper/issues?q=label%3Abug+is%3Aclosed).

## Unfixed Bugs

There are no remaining bugs that I am aware of.