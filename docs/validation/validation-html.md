# **Landing page:**

![Landing page HTML](/docs/validation/html/landing-page-validation-html.png)

# **Patient Account:**

![Patient account HTML Validation](/docs/validation/html/patient-account-html.png)

# **Doctor Acoount:**

![Doctor account HTML Validation](/docs/validation/html/doctor-account-html.png)

# **Patient Appointment**

![Patient appointment HTML Validation](/docs/validation/html/patient-appointments-html.png)

# **Doctor Appointment**

![Doctor appointment HTML Validation](/docs/validation/html/doctor-appointments-html.png)

In the doctor appointments page, the datetime value retrieved from the database does not match the local time format. This issue was identified during testing.

However, after evaluating potential solutions, it was decided not to alter the datetime format, as changes could conflict with the expected format of the HTML `<input type="datetime-local">` field. This input type requires a specific format (YYYY-MM-DDTHH:MM), and any formatting inconsistency could lead to errors or prevent the form from functioning correctly.

The current format ensures compatibility with form inputs and avoids breaking functionality during date/time selection and editing.

# **Consults Page**

![Consults HTML Validation](/docs/validation/html/consults-page-html.png)

