# ***DocAdvanced***

## 1. Project Information
DocAdvanced is a hospital web app focused on prioritising user-friendly access to healthcare services. This platform enables patients to effortlessly register and request consultations with registered medical professionals. Simultaneously, it empowers doctors to manage appointment requests, confirm scheduled sessions, or cancel them when necessary.

**Project Goal:**
The primary goal of this project is to deliver a clean and intuitive user interface that simplifies the booking and management of medical appointments. This systems is designed for smart interactions between patients and doctors through an organized and accessible digital platform.

**Audience:**
The platform is designed for teenagers and adults who want a fast and simple way to book a consultation with a doctor online.

*DocAdvanced website can be accessed at [Here](https://doc-advanced-c1ddb943acbd.herokuapp.com/).*

# 2. Table of Contents

- [1. Project Information](#1-project-information)
- [2. Table of Contents](#2-table-of-contents)
- [3. User Experience](#3-user-experience)
    - [3.1. Strategy Plan](#31-Strategy-Plan)
        - [3.1.1. The Ideal](#311-the-ideal)
        - [3.1.2. Site Goal](#312-site-goal)
        - [3.1.3. Epics](#313-epics)
        - [3.1.4. User Stories](#314-user-stories)
    - [3.2. Scope Plan](#32-scope-Plan)
        - [3.2.1. Features to Implement](#321-features-to-implement)
    - [3.3. Structure Plan](#33-structure-Plan)
        - [3.3.1. Database Scheme](#331-database-scheme)
        - [3.3.2. Wireframes](#332-wireframes)
        - [3.3.3. Fonts](#333-fonts)
        - [3.3.4. Icons and Images](#334-images-and-icons)
- [4. Features](#4-features)
    - [4.1. Base HTML](#41-base-html)
    - [4.2. Error Pages](#42-error-pages)
    - [4.3. Main Content](#43-main-content)
        - [4.3.1. Landing Page](#431-landing-page)
        - [4.3.2. Authentication and Authorisation](#432-authentication-and-authorisation)
        - [4.3.3. Account Form](#433-account-form)
        - [4.3.4. Account Page](#434-account-page)
        - [4.3.5. Appointments](#435-appointments)
        - [4.3.6. Book Appointment](#436-book-appointments)
        - [4.3.7. Consults](#437-consults)
    - [4.4. Future Features](#44-future-features)
- [5. Testing and Validation](#5-testing-and-validation)
    - [5.1. Testing](#51-testing)
    - [5.2. Validation](#52-validation)
        - [5.2.1. HTML Validation](#521-html-validation)
        - [5.2.2. CSS Validation](#522-css-validation)
        - [5.2.3. JavaScript Validation](#523-javascript-validation)
        - [5.2.4. Python Validation](#524-python-validation)
    - [5.3. Bugs](#53-bugs)
        - [5.3.1. Fixed Bugs](#531-fixed-bugs)
        - [5.3.2. Unfixed Bugs](#532-Unfixed-bugs)
    - [5.4. Accessibility](#54-accessibility)
- [6. Deployment](#6-deployment)
    - [6.1 Heroku Deployment](#61-Heroku-deployment)
- [7. Technologies and Credits](#7-technologies-and-credits)
    - [Technologies Used](#71-technologies-used)
    - [Credits](#72-credits)

# 3. User Experience

## 3.1. Strategy Plan

### 3.1.1. The Ideal
DocAdvanced was made thinking of simplicity and quick consultation booking, easy appointments management. On top of that, the UI was made for easy navigation.

### 3.1.2. Site Goal
- Give user ability to register and log in into the website
- Give user ability to request and manage appointments
- Give user ability to create consultation report( doctor) and read that report (patient)
- Offer user easy navigation through the website

### 3.1.3. Epics
To organize the development process, **10 Epics** were created as part of the project planning strategy. These Epics represent major features or sections of the application. Link to Kanban Board.

Check the Kanban board below

They were added to a [**Kanban Board**](https://github.com/users/Jonatas-01/projects/2/views/1) on the GitHub platform to help manage progress clearly and efficiently. Each Epic was later broken down into smaller tasks called **User Stories**, which made it easier to track and complete specific parts of the project.

### 3.1.4. User Stories
**User Stories** are small parts of an Epic, created to break down tasks and deliver value to the user. A total of **34 User Stories** were written, all from the user’s perspective.

To help define priorities and estimate effort, **labels** and **story points** were added to each task.

**Labels:**
Labels were created using the **MoSCoW technique**, which classifies tasks based on their importance:

- **Must-Have**: Essential features that are critical for the project to work.
- **Should-Have**: Important features, but not critical for core functionality.
- **Could-Have**: Nice-to-have features that can be added if time and resources allow.
- **Won’t-Have**: Features that are not included in the current project scope.

**Story Points:**
Story points are used to estimate the effort needed to complete each User Story. They follow the **Fibonacci sequence** (1, 3, 5, 8, 13), where, **1** means very easy and **13** means very complex or time-consuming.

You can view all the User Stories and their details on the [**Kanban board**](https://github.com/users/Jonatas-01/projects/2/views/1).

## 3.2. Scope Plan
After defining the development and organization strategy, the project scope was created.

### 3.2.1. Features to Implement
- User Authentication: Users can register as either a doctor or a patient, and have the ability to log in and log out securely.
- Personal/Professional Details: After registration, users can fill out a form with their personal details. If the user is a doctor, they also complete a section with their professional information (such as specialty and a brief bio).
- Request Appointments: Patients can request appointments with available doctors. During the request, they can also include notes describing their symptoms or the reason for the consultation.
- Appointment Management: Doctors can confirm appointments by selecting a date and time. Both doctors and patients can cancel or delete appointments at any time before the consultation begins.
- Consultation Handling: Once an appointment is confirmed, the doctor can start the consultation. During the consult, the doctor fills out a form that includes patient intake notes, diagnosis, and a prescription if necessary.
- Consultation Records: After a consultation is completed, both doctors and patients can view the consult details. These records are displayed on the Consults page, ensuring transparency and easy access to medical history.

## 3.3. Structure Plan

### 3.3.1. Database Scheme
Bellow you can see the actual database structure, made in [Lucid Flowchart](https://lucid.app/) platform website.
![Database Schema](/docs/structure-Plan/Database%20ER%20diagram%20(crow's%20foot).png)

### 3.3.2. Wireframes
The wireframes were made to organize the design toughts. Platform used was [Mockflow](https://app.mockflow.com/).

- **Navbar and Footer**: The **Navbar** and **Footer** are displayed on every page of the website to ensure consistent navigation and user experience.
    - The **Navbar** is located at the top of the page. It allows users to easily access the main sections of the site, such as Home, Account, Login, and Register, depending on their authentication status. It adjusts dynamically based on whether the user is logged in and their role (doctor or patient).
    - The **Footer** is placed at the bottom of each page. It provides basic information about the website, such as credits to the developer and links to social media platforms.   

![Navbar and Footer](/docs/wireframes/nav-footer.png)
---

- **Landing Page**: The **Landing Page** is the homepage of the website and the first screen new users will see. It is designed to **welcome visitors**, **explain how the platform works**, and **encourage them to register**. The layout is clean and informative, giving users a quick overview of the site's purpose and how to get started.

![Landing Page](/docs/wireframes/landing-page.png)
---

- **Account Page**: The **Account Page** displays the user's information based on their role:
    - For patients, it shows their personal details.
    - For doctors, it includes both personal and professional information (such as specialty and biography). 

This page also provides an option for users to edit and update their information at any time.

![Account Page](/docs/wireframes/account-page.png)
---

- **Appointment Page**: The **Appointment Page** displays all appointment-related information, including upcoming, pending, and cancelled/rejected appointments.

It provides different functionalities based on the user role:
- **For Patients:**
    - View their appointments.
    - Request a new appointment with a doctor.
    - Edit, cancel, or delete existing appointments before the consultation begins.

![Patient Appointment Page](/docs/wireframes/patient-appointment-page.png)

- **For Doctors:**
    - View incoming appointment requests.
    - Confirm appointments by assigning a date and time.
    - Reject, cancel, or delete appointments as needed.
    - Start consult.

![Doctor Appointment Page](/docs/wireframes/doctor-appointment-page.png)
---

- **Consults Page:** The **Consults Page** displays completed consultations recorded by doctors.
    - **For Patients**
        - View their past consultations and the details filled in by the doctor.
        - Delete consultation records from their view if needed.
![Patient Consult Page](/docs/wireframes/patient-consults-page.png)

    - **For Doctors**
        - View all consultations they have conducted.
        - Edit consultation details, including intake notes, diagnosis, and prescriptions.
![Doctor Consult Page](/docs/wireframes/doctor-consults-page.png)

### 3.3.3. Fonts
The **Google Fonts** platform was used to select typography that balances style and readability. Special attention was given to ensuring that all text is **clear**, **accessible**, and easy to read across different screen

**Fonts used:**
- **Quicksand:** Applied to most of the body text for its clean and modern appearance.
- **Rubik:** Used for headings and titles to provide emphasis and visual hierarchy.

As the developer, I focused on maintaining a consistent and legible design that enhances the overall user experience.

### 3.3.4. Images and Icons
**Images**: One image is used throughout the website, placed on the Landing Page. The image was sourced from [Freepik](https://www.freepik.com/free-vector/hospital-waiting-room-concept-illustration_72631546.htm#fromView=search&page=6&position=15&uuid=19fa2f01-421e-46aa-9279-7097377ddcaa&query=hospital) and is intended to give context and meaning to the platform by visually representing its purpose (healthcare and consultation).

**Icons** were sourced from [Font Awesome](https://fontawesome.com/) and are used throughout the website to enhance visual communication. They help users quickly identify actions and links (e.g., social media, navigation), improving overall usability and design appeal.

# 4. Features
## 4.1. Base HTML
To ensure the navigation bar and footer appear on every page, a reusable template named `base.html` was created. This file is located inside the `templates` folder.

The `base.html` template includes:
- A consistent navbar
- A footer
- Template blocks to load dynamic content
- Links to CSS files and other static resources

**Navigation Bar**
The navigation bar is placed at the top of every page and includes:
- Logo and brand name
- Links to important pages such as Home, Account, Login, and Register
- If the user is not logged in:
    - Links to Register and Login are displayed

![Navbar logged out](/docs/website-features/nav-bar.png)

- If the user is logged in:
    - Links to Account and Log Out are shown, adjusted based on the user’s role

![Navbar logged in](/docs/website-features/nav-bar-logged.png)

- Responsive mobile version

![Navbar Mobile](/docs/website-features/nav-bar-mobile.png)

**Footer**
Footer is placed at the bottom of every page and has:
- Logo and Brand name followed by context paragraph
- Quick links section to all pages
- Contact Information
    - Address
    - Phone
    - Email
- Social media section with link to Facebook, Instagram, X and LinkedIn

![Footer Desktop](/docs/website-features/footer-desktop.png)

Mobile Footer

![Footer Mobile](/docs/website-features/footer-mobile.png)

## 4.2. Error Pages
**Custom error pages** were created to give users a **better understanding** of what went wrong and to provide a quick way to return to the website. Each error page includes a clear message and a button that allows the user to go back to the home page with a single click.

- **403** - Received when user attempts to access a web resource for which they lack the necessary permissions.
- **404** - Encountered when the requested web resource by user is not found on the server.
- **500** - Displayed when the web server encounters an internal error while processing the request.

**403 Page**

![403 Page](/docs/website-features/403-error.png)

**404 Page**

![404 Page](/docs/website-features/404-error.png)

**500 Page**

![500 Page](/docs/website-features/500-error.png)

## 4.3. Main Content
### 4.3.1. Landing Page
**The Landing Page** was built to welcome new users, introduce the company, explain how to use the platform, and encourage visitors to register. Its main purpose is to provide a clear and friendly starting point for anyone visiting the website for the first time.

The landing page includes the following sections:
- **Header:** Provides a brief introduction to the platform, includes an image, and contains buttons to book an appointment or access the account page.
- **Smart Features:** Highlights the key features and benefits of using the service, helping users understand why the platform is valuable.
- **How It Works:** Explains step-by-step how users (patients and doctors) can use the website, from registration to booking and managing appointments.
- **Ready to start?** A call-to-action section that encourages new users to register and begin using the platform

![Landing Page](/docs/website-features/landing-page.png)

### 4.3.2. Authentication and Authorisation
The **authentication system** was implemented to allow users to **register**, **log in**, and **log out** of the website securely.

After successful registration and login, users are **authorized** to access the platform’s features based on their role (patient or doctor). This ensures that only verified users can interact with the appointment and consultation system.
- App: `core`

**Registration Page**
- Template File : /authentication/register.html - extends `base.html`

![Registration](/docs/website-features/registration.png)

**Login Page**
- Template File: /authentication/login.html - extends `base.html`

![Login Page](/docs/website-features/login.png)

**Log out Page**
- Template File: /authentication/logout.html - extends `base.html`

![Log out](/docs/website-features/logout.png)

### 4.3.3. Account Form
After a user successfully registers, they are immediately redirected to fill out their account form. Completing this form is mandatory in order to gain full access to the platform’s services. The form content varies depending on the user's role (patient or doctor).
- App: `account`

**Patient Account Form** 
The patient form collects basic personal and medical information
- Contains personal fields:
    - First name
    - Last name
    - Gender
    - Age
    - Contact Information
- Medical Information:
    - Current Medication
    - Allergies
- Template File: /forms/patient_form.html - extends `base.html`

![Patient Account Form](/docs/website-features/patient-account-form.png)

**Doctor Account Form** 
The doctor form includes personal and professional details:
- Contains personal fields:
    - First name
    - Last name
    - Gender
    - Contact Information
- Professional Details:
    - Specialty
    - About (a short bio or description of their professional background)
- Template File: /forms/doctor_form.html - extends `base.html`

![Doctor Account Form](/docs/website-features/doctor-account-form.png)

### 4.3.4. Account Page
The Account Page allows users to view and manage their personal or professional details. Page displays different information for patients and doctors.

**Patient Account Page** 
Patients can:
- View Personal Details:
    - First Name
    - Last Name
    - Gender
    - Age
    - Contact Information
    - (Optional) Medical details like current medication and allergies
- Edit Information:
    - Update personal or medical details at any time through the "Edit" form.
- Template File: /accounts/patient_details.html - extends `base.html`

![Patient Details](/docs/website-features/patient-account-page.png)

**Doctor Account Page** 
Doctors can:
- View Personal and Professional Details:
    - First Name
    - Last Name
    - Gender
    - Contact Information
    - Specialty
    - About (short bio)
- Edit Information:
    - Update both personal and professional details using the edit form.
- Template File: /accounts/doctor_details.html - extends `base.html`

![Doctor Details](/docs/website-features/doctor-account-page.png)

This page ensures that users always have access to their own data and can keep it up to date as needed.

### 4.3.5. Appointments
**The appointment** system allows patients to request consultations with doctors and enables doctors to manage those requests. It is a central part of the platform’s functionality, offering different features depending on the user role.
**App**: `appointment`

**Patients can:**
- **Request an Appointment:**
    - Choose a doctor from the list.
    - Add optional notes to describe symptoms or reasons for the consultation.
- **Manage Appointments:**
    - View all appointment statuses (Pending, Confirmed, Rejected, Canceled).
    - Edit, cancel, or delete an appointment before it begins.
    - View confirmed appointments with the scheduled date set by the doctor.
- Template File: /patient/appointments_patient_view.html - extends `base.html`

![Patient Appointment1](/docs/website-features/patient-appointment-part1.png)
![Patient Appointment2](/docs/website-features/patient-appointment-part2.png)

**Doctors can:**
- **View Requests:**
    - See all incoming appointment requests from patients.
- **Manage Appointments:**
    - Confirm an appointment by selecting a consultation date and time.
    - Start the confirmed appointments.
    - Reject an appointment if unavailable.
    - Edit a scheduled date if changes are needed.
    - Cancel or delete appointments when appropriate.
- Template File: /doctor/appointment_doctor_view.html - extends `base.html`

![Doctor Appointment](/docs/website-features/doctor-appointments.png)

### 4.3.6. Book Appointments
The **Book Appointments** feature allows **patients** to explore a list of available doctors and request a consultation with just a few clicks. It’s designed to make the process fast, simple, and user-friendly.
**App**: `appointments`

**Patients can:**
- **Browse Available Doctors:**
    - View doctor cards that include name, gender, specialty, contact info, and a short bio.
- **Request an Appointment:**
    - Click the "Book Appointment" button on a selected doctor.
    - Fill out a short form with optional notes describing symptoms or reasons for the visit.
    - Submit the form to send the request to the doctor.
- **View Booking Status:**
    - After submission, the appointment status appears as “Pending” until the doctor responds.

**Doctors can:**
- **View Appointment Requests:**
    - See a list of all incoming appointment requests from patients.
- **Respond to Requests:**
    - Confirm the appointment by selecting a date and time.
    - Reject the request if unavailable or inappropriate.
- Template File: /form/request_appointment.html - extends `base.html`

![Book Appointments](/docs/website-features/book-appointments.png)

This feature connects patients and doctors smoothly, ensuring the appointment workflow begins with ease and clarity.

### 4.3.7. Consults
The **Consults** feature handles everything related to medical consultations after an appointment has been confirmed. It enables **doctors** to record details of the consultation and allows **patients** to view and manage their consultation history
**App**: `consult`

**Doctor Consult Features** 
Doctors can:

- **Start a Consultation:**
    - Available once an appointment is confirmed and scheduled.
    - Access a consultation form linked to the specific patient and appointment.
- **Fill Out Consultation Details:**
    - Patient Intake Notes: Information about the patient’s condition or symptoms.
    - Diagnosis: The doctor’s medical conclusion.
    - Prescription: Medications or treatment plans suggested for the patient.
- **Edit Consultation:**
    - Modify any of the consultation fields after submission, if needed.
- Template File: /consults/start_consult.html - extends `base.html`

![Doctor Consult Form](/docs/website-features/doctor-consult-form.png)

![Doctor Consult Page](/docs/website-features/doctor-consult-page.png)

**Patient Consult Features** 
Patients can:

- **View Consult Records:**
    - Access completed consultations from the Consults Page.
    - See details filled out by the doctor, including notes, diagnosis, and prescriptions.
- **Delete Consults:**
    - Remove consultation records from their view if they choose to.

![Patient Consult Page](/docs/website-features/patient-consult-page.png)

![Patient Consult View](/docs/website-features/patient-consult-view.png)

The **Consults Page** creates a reliable space to **track medical history**, ensuring that both patients and doctors have access to important health records even after the consultation is complete.

### 4.4. Future Features
To continue improving the platform and enhancing the user experience, the following features are planned for future development:

- **Email & SMS Notifications**:
Automatically notify users about appointment confirmations, cancellations, and reminders.
- **Calendar Integration**
Sync confirmed appointments with Google Calendar or Outlook for easier time management.
- **Admin Dashboard**
A backend interface for administrators to manage users, appointments, and platform content.
- **Medical History Archive**
Enable long-term storage and filtering of past consults for easier access to patient records.
- **Search & Filter for Doctors**
Add search functionality and filters by specialty, gender, or availability.
- **Rating & Feedback System**
Allow patients to rate doctors and leave feedback after consultations.

# 5. Testing and Validation
## 5.1. Testing
Both **automated** and **manual** tests were conducted to ensure the functionality and reliability of the application.

- **Automated Testing**: Automated tests were written using Django’s built-in unittest framework. These tests focused on:
    - Models – Validating data structure, relationships, and methods
    - Forms – Ensuring proper field validations and behavior
    - Views – Testing access control, response codes, and redirections
All test files can be found in the tests.py file located within each app. These tests allowed quick verification of core logic and user authorization rules.

- **Manual Testing**: Manual testing was carried out to check:
    - Visual consistency – Ensuring that pages display correctly across devices and screen sizes
    - Navigation – Confirming that links, buttons, and forms work as expected
    - User Flow – Testing real interactions, including registering, logging in, booking appointments, and editing profiles
Manual tests were run in two environments, locally by running python manage.py runserver and on Heroku after deploying the live version of the site

All tests were **completed successfully**, and any bugs discovered during testing were **identified and fixed**.

## 5.2. Validation
### 5.2.1. HTML Validation
- To ensure source code generated from all `*.html` templates is compliant with [W3C standards](https://validator.w3.org/).
- **Method :**
    - Open each page of the project.
    - In Browser : Right click on page background and select View Page Source.
    - Copy and Paste the generated code from browser to validator.
    - See results.
    - Please note this needs to be done for all states of the templates (i.e. Logged In / Logged Out, etc.).

 Check the validation screenshots in [Validation HTML](/docs/validation/validation-html.md).

### 5.2.2. CSS Validation
To ensure the code in style.css is compliant with [W3C standards](https://jigsaw.w3.org/css-validator/).
- **Method :**
    - Open the style.css file
    - Copy and Paste the code from IDE to validator
    - See results

`style.css` file passed the validation test with **NO ERRORS**.

![CSS Validation](/docs/validation/css/css-validation.png)

### 5.2.3. JavaScript Validation
To ensure JavaScript has no error the code in `*.js` are check in [JSHint](https://jshint.com/).
- **Method :**
    - Open the `.js` files
    - Copy and Paste the code from IDE to validator
    - See results

`*.js` file passed the validation test with **NO ERRORS**.

![JS Validation](/docs/validation/js/js-validation.png)

### 5.2.4. Python Validation
We have used [CI Python Linter](https://pep8ci.herokuapp.com/) to check if the matches PEP8 standards, also we add docstring following [PEP257](https://peps.python.org/pep-0257/) instructions.
- **Method :**
    - Open all `*.py` files from all apps
    - Copy and Paste the code from IDE to validator
    - See results

The project was checked for **PEP8 compliance** using the **CI Python Linter**, focusing specifically on the `views.py` files across all apps. These files were selected because they contain logical blocks that can be safely adjusted to meet line-length and formatting rules.

Other files, such as `models.py` and `forms.py`, were not linted in the same way due to long lines that are structurally difficult to break without reducing readability or introducing complexity. However, **PEP 257-compliant** docstrings were added to all Python files.

Check the screenshot from CI Python Linter [validation-python](/docs/validation/validation-python.md).

Aside from a few `messages` lines that exceed the standard character limit and are not practical to break without reducing readability, the files successfully passed the **PEP8 validation** with **NO ERRORS**.

## 5.3. Bugs

### 5.3.1. Fixed Bugs
| ID | Bug Description                                      | Cause                                                       | Fix                                                           | Status  |
|----|-------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------|---------|
| 1  | Consults were not being displayed                     | Parameter was not passed in the view                        | Created the variable and passed it to the template             | ✅ Fixed |
| 2  | Buttons overflowed on desktop view                    | Spacing issue in the layout                                 | Updated layout to display buttons in a vertical column         | ✅ Fixed |
| 3  | Logged-in users could access login/register pages     | No condition to block access for authenticated users        | Added `if` statement to redirect logged-in users               | ✅ Fixed |
| 4  | Feedback messages had no styling                      | No CSS classes applied to Django messages                   | Added message tags in `settings.py` to apply Bootstrap classes | ✅ Fixed |
| 5  | Modals were not displaying unique values per card     | Only one modal was used for all cards                       | Created a modal inside the loop and used `data-` attributes per item| ✅ Fixed |

### 5.3.2. Unfixed Bugs
All known bugs identified during development and testing have been resolved.  
**There are currently no unfixed bugs in the application.**

## 5.4. Accessibility
To ensure that the application is user-friendly and inclusive, an accessibility audit was performed using Lighthouse (Chrome DevTools).
- **Tool Used**: [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- **Mode**: Desktop & Mobile
- **Metric**: Accessibility Score

### Accessibility Highlights:
- All relevant images include **alt text**
- Forms use properly associated **label** elements
- **Color contrast** meets WCAG 2.1 AA standards
- Use of **semantic HTML elements** (`<header>`, `<main>`, `<footer>`, etc.)
- Full support for **keyboard navigation**
- **Focus indicators** are visible on interactive elements

### Fixes & Adjustments:
- Added missing `<label>` tags to form inputs
- Improved button and link text for clarity
- Adjusted focus states and tab order for better keyboard support

Lighthouse Score:
- **Accessibility**: ✅ 93%

A screenshot of the Lighthouse report can be included here: [Lighthouse Accessibility Report](/docs/lighthouse/lighthouse.md)

# 6. Deployment
## 6.1 Heroku Deployment
**Objective:** Deploy the live version of the DocAdvanced platform so that users can interact with the application online.

**Steps:**
1. Create a Heroku Account
    - Register or log in at heroku.com
2. Create a New App
    - Go to Dashboard > New > Create New App
    - Choose a unique name for your application
3. Configure Environment Variables
    - Go to Settings > Reveal Config Vars
    - Copy all key-value pairs from your local `env.py` file
    - Add all required environment variables (e.g., `SECRET_KEY`, `DATABASE_URL`, etc.)
    - Add `PORT` with the value `8000`
    - For testing deployment, add `COLLECTSTATIC` with the value 1
4. Update Django Settings
    - Add your Heroku app domain to the `ALLOWED_HOSTS` list in `settings.py`
5. Create a Procfile
    - In the root directory of your project, create a file named `Procfile`
    - This file should contain: `web: gunicorn <your_project_name>.wsgi`
6. Connect to GitHub
    - In the Deploy tab of your Heroku app, connect your GitHub repository
7. Deploy Your Application
    - Select the appropriate branch (usually `main` or `master`)
    - Click Deploy Branch
8. View Deployment Logs
    - Monitor the logs to ensure the deployment was successful
    - If everything works, you’ll be able to click "View" to open the live application

# 7. Technologies and Credits
## 7.1 Technologies Used
- [Django](https://www.djangoproject.com/) - High-level Python web framework used to build the backend and manage the application's logic, models, and authentication system.
- [Python](https://www.python.org/) - The core programming language used for backend development.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Adds interactivity and dynamic behavior to the frontend.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Structures the content of the web pages.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Styles the HTML content and ensures a responsive and visually appealing design.
- [BootStrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - A CSS framework used to build responsive layouts and styled components quickly.
- [Heroku](https://www.heroku.com/) - Cloud platform used to deploy and host the live version of the application.
- [MockFlow](https://mockflow.com/) - Used for creating wireframes and planning the UI/UX design.
- [Git](https://git-scm.com/) - Version control system used to track code changes during development.
- [GitHub](https://github.com/) - Code hosting platform used for collaboration and deployment integration.
- [VS Code](https://code.visualstudio.com/) - Code editor used throughout the development process.

## 7.2 Credits
- [Google Fonts](https://fonts.google.com/) - used for picking the best typography
- [FreePik](https://freepik.com) - used as images database
- [FlatIcon](https://www.flaticon.com/) - used to get icon to user on browser window
- [FontAwesome](https://fontawesome.com/) - used as icon database
- [Django](https://www.djangoproject.com/) - useful documentation
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - bootstrap documentation for useful information
- [Lucid](https://lucid.app/) - to database schema creation
- [Dribbble](https://dribbble.com/) - for design ideas