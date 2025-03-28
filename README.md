# ***DocAdvanced***

## 1. Project Information
DocAdvanced is a hospital web app focused on prioritising user-friendly access to healthcare services. This platform enables patients to effortlessly register and request consultations with registered medical professionals. Simultaneously, it empowers doctors to manage appointment requests, confirm scheduled sessions, or cancel them when necessary.

**Project Goal:**
The primary goal of this project is to deliver a clean and intuitive user interface that simplifies the booking and management of medical appointments. This systems is designed for smart interactions between patients and doctors through an organized and accessible digital platform.

**Audience:**
The platform is designed for teenagers and adults who want a fast and simple way to book a consultation with a doctor online.

*DocAdvanced website can be accessed at [Here](https://doc-advanced-c1ddb943acbd.herokuapp.com/).*

# 2. Table of Contents

- [1. Project Information]()
- [2. Table of Contents]()
- [3. User Experience]()
    - [3.1. Startegy Plane]()
        - [3.1.1. The Ideal]()
        - [3.1.2. Site Goal]()
        - [3.1.3. Epics]()
        - [3.1.4. User Stories]()
    - []()
- []()

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

### 3.2.1. Features Implemented
- User Authentication: Users can register as either a doctor or a patient, and have the ability to log in and log out securely.
- Personal/Professional Details: After registration, users can fill out a form with their personal details. If the user is a doctor, they also complete a section with their professional information (such as specialty and a brief bio).
- Request Appointments: Patients can request appointments with available doctors. During the request, they can also include notes describing their symptoms or the reason for the consultation.
- Appointment Management: Doctors can confirm appointments by selecting a date and time. Both doctors and patients can cancel or delete appointments at any time before the consultation begins.
- Consultation Handling: Once an appointment is confirmed, the doctor can start the consultation. During the consult, the doctor fills out a form that includes patient intake notes, diagnosis, and a prescription if necessary.
- Consultation Records: After a consultation is completed, both doctors and patients can view the consult details. These records are displayed on the Consults page, ensuring transparency and easy access to medical history.

## 3.3. Structure Plane

### 3.3.1 Database Scheme
Bellow you can see the actual database sctructure, made in [Lucid Flowchart](https://lucid.app/) platform website.
![Database Schema](/docs/structure-plane/Database%20ER%20diagram%20(crow's%20foot).png)

### 3.3.2 Wireframes
The wireframes were made to organize the design toughts. Plataform used was [Mockflow](https://app.mockflow.com/).

- **Navbar and Footer**: The **Navbar** and **Footer** are displayed on every page of the website to ensure consistent navigation and user experience.
    - The **Navbar** is located at the top of the page. It allows users to easily access the main sections of the site, such as Home, Account, Login, and Register, depending on their authentication status. It adjusts dynamically based on whether the user is logged in and their role (doctor or patient).
    - The **Footer** is placed at the bottom of each page. It provides basic information about the website, such as credits to the developer and links to social media platforms.
![Navbar and Footer](/docs/wireframes/nav-footer.png)

