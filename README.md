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
    - [3.1. Startegy Plane](#31-startegy-plane)
        - [3.1.1. The Ideal](#311-the-ideal)
        - [3.1.2. Site Goal](#312-site-goal)
        - [3.1.3. Epics](#313-epics)
        - [3.1.4. User Stories](#314-user-stories)
    - [3.2. Scope Plan](#32-scope-plane)
        - [3.2.1. Features to Implement](#321-features-to-implement)
    - [3.3. Structure Plan](#33-structure-plane)
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

# 3. User Experience

## 3.1. Startegy Plane

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
**User Stories** are small parts of an Epic, created to break down tasks and deliver value to the user. A total of **29 User Stories** were written, all from the user’s perspective.

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

## 3.2. Scope Plane
After defining the development and organization strategy, the project scope was created.

### 3.2.1. Features to Implement
- User Authentication: Users can register as either a doctor or a patient, and have the ability to log in and log out securely.
- Personal/Professional Details: After registration, users can fill out a form with their personal details. If the user is a doctor, they also complete a section with their professional information (such as specialty and a brief bio).
- Request Appointments: Patients can request appointments with available doctors. During the request, they can also include notes describing their symptoms or the reason for the consultation.
- Appointment Management: Doctors can confirm appointments by selecting a date and time. Both doctors and patients can cancel or delete appointments at any time before the consultation begins.
- Consultation Handling: Once an appointment is confirmed, the doctor can start the consultation. During the consult, the doctor fills out a form that includes patient intake notes, diagnosis, and a prescription if necessary.
- Consultation Records: After a consultation is completed, both doctors and patients can view the consult details. These records are displayed on the Consults page, ensuring transparency and easy access to medical history.

## 3.3. Structure Plane

### 3.3.1. Database Scheme
Bellow you can see the actual database sctructure, made in [Lucid Flowchart](https://lucid.app/) platform website.
![Database Schema](/docs/structure-plane/Database%20ER%20diagram%20(crow's%20foot).png)

### 3.3.2. Wireframes
The wireframes were made to organize the design toughts. Plataform used was [Mockflow](https://app.mockflow.com/).

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
- Professional Detials:
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
