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

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."


🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

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
| | When logged out, manually input url leading to a task-deletion page to attempt brute-force entry | Redirection to sign-in page | Pass | ![screenshot](documentation/testing/features/brute-delete-logged-out.gif) | |
| Archive Task | | | | | | 
| | Click on a 'Mark task as finished' button of which you're the owner and has assigned helper | Redirection to own task list, displays success message below the header image | Pass | ![screenshot](documentation/testing/features/archive-task.gif) | |
| | Click on a 'Go back' button | Redirection to the ongoing task | Pass | ![screenshot](documentation/testing/features/archive-go-back.gif) | |
| | Manually input url leading to a task-archiving page for an already archived task you own | Fail | ![screenshot](documentation/testing/features/archive-go-back.gif) | |
| | Manually input url leading to a task-archiving page for a task you own but has no helper | Fail | ![screenshot](documentation/testing/features/archive-go-back.gif) | |
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













| Contact | | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | | |
| | Enter first/last name | Field will accept freeform text | Pass | | |
| | Enter valid email address | Field will only accept email address format | Pass | | |
| | Enter message in textarea | Field will accept freeform text | Pass | | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return | |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## User Story Testing

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/josipcodes/community-helper/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/josipcodes/community-helper/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/josipcodes/community-helper/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/josipcodes/community-helper/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/josipcodes/community-helper/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/josipcodes/community-helper/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/josipcodes/community-helper/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/josipcodes/community-helper/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.