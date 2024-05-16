CS50 WEB PROGRAMMING FINAL PROJECT: ABHINAV PANGARIA
Github - 18Abhinav07
edx- abhinavpangaria

The project video is here: https://youtu.be/Ywty40NmCso

## Distinctiveness and Complexity

My project is a sophisticated and comprehensive integration of various concepts learned throughout the CS50 course, combined with practical application for an institution that requires an entry management system.

    Unique Integration: Unlike typical projects like social media apps or e-commerce websites, my project stands out by combining elements from different domains. It's not just about creating a standalone application but integrating it into a real-world scenario, such as entry management for a college. This integration adds a layer of practicality and relevance to my project.

    Complexity in Functionality: My project has a range of functionalities, from user authentication to real-time updates using APIs and JavaScript. This complexity is further heightened by the inclusion of multiple user groups with different permissions, such as entry officers and admins. Each functionality, like creating users or managing student details, adds depth to the application, making it more robust and versatile.

    Responsive Design: Ensuring responsiveness across different devices adds another layer of complexity. By utilizing frameworks like Bootstrap and media queries, I am not only addressing the aesthetic aspect but also enhancing user experience across various screen sizes, which is crucial for modern web applications.

    Scalability and Security: Mentioning scalability implies that my project is designed to accommodate growth and handle increasing demands. This scalability, combined with security considerations, such as managing user permissions and data protection, adds another dimension of complexity. Building a system that can evolve and maintain integrity over time is a significant challenge in itself.

The Entry Management System was chosen by me as it had all the aspects of integrating the topics that I have learned in the CS50 course. From the knowledge of basic pages and rendering from the search project, the CRUD theory and implementation from the wiki project, the Javascript and in-depth url calls and multiple views from project commerce, the API calls from mail project and further use of API, javascript and django in network project.

My project is distinct and complex as it is not an e-commerce platform and neither a chat/social media app, It is an entirely different project that includes authentication, authorization, creation of multiple kinds of users, distinguished user pages and dashboards, sophesticated use of django to develop the backend and also I used MySql to be the backend database provider.

There are real time updates with API calls and subsequent JSON data transfers.

Now, the django and javascript are part of the backend implementations, I have spent considerable amount of time working on the responsiveness and overall appearnance of the webapp. I have used Bootstrap as a CSS framework and maintained the site to be one of a very good user experience.

  Structure:
  -- Home Page (with some video text for style)
  -- Home Page (split-screen that contains the login for guard and admins)
  -- Admin Dashboard--> {Student} / {Users} / {Others}
     --> The admin dashboard has functionality to create all kinds of users.
     --> The Others containes all the non institute based entries and records.
  -- Student Dashboard:
     --> Create new srudents / delete students.
     --> Get all the details about the students and modify student details and records.
     --> Get real-time updates on the details of the students, a pie chart analytics that is made usign javascript.

The project involves use of three mdoels and a default User model thus advancing its complexity from the other projects.
I have implemented various API' and javascript to make the webapp fast and responsive.
There are multiple user types and login methods so authentcation complexity is a notch above the course projects.
Overall the size and usability of the project makes it distinct and complex.

## File and Implementation:

Implemented using Django, Javascript, HTML, CSS, Bootstrap, MYSQL
All the HTML files are inside the templates folder.
Follows all the standard django construct.

Here is an overview of all the files in the project.

### models.py

    INSTITUTE_ADMITTED Model:
    This table holds records of students who have been officially admitted to the institute. It includes data such as the student's name, roll number, reason for admission, permission status, contact phone number, batch/year, branch/department, and vehicle number if applicable. This data is crucial for managing and tracking the admission status of students within the institute.

    NON_INSTITUTE_ADMITTED Model:
    This table stores information about individuals who are not officially admitted to the institute but have visited its premises for various reasons. It records details such as the person's name, reason for visit, contact phone number, and vehicle number if provided. This data helps in monitoring external visits and maintaining security protocols within the institute.

    STUDENTS_DATA Model:
    This table contains essential information about students enrolled in the institute. It includes details such as the student's roll number (serving as the primary key), name, room number, contact phone number, email address, batch/year, and branch/department. This data serves as a comprehensive student database for administrative purposes, academic tracking, and communication within the institute.


1. **INSTITUTE_ADMITTED** Model:
   - This model represents the data related to students admitted to the institute.
   - `created_at` is a CharField that stores the date and time when the record was created.
   - `name` is a CharField that stores the name of the student (up to 50 characters).
   - `roll_no` is an IntegerField that stores the roll number of the student.
   - `reason` is a CharField that stores the reason for the student's admission (up to 100 characters).
   - `permission` is a CharField that stores whether the student has permission or not (up to 10 characters).
   - `phone` is a CharField that stores the student's phone number (up to 10 characters).
   - `batch` is a CharField that stores the batch or year of the student (up to 15 characters).
   - `branch` is a CharField that stores the branch or department of the student (up to 10 characters).
   - `vehicle_no` is a CharField that stores the vehicle number of the student (up to 10 characters).

2. **NON_INSTITUTE_ADMITTED** Model:
   - This model represents the data related to people who are not admitted to the institute but have visited the premises.
   - `created_at` is a CharField that stores the date and time when the record was created.
   - `name` is a CharField that stores the name of the person (up to 50 characters).
   - `reason` is a CharField that stores the reason for the person's visit (up to 100 characters).
   - `phone` is a CharField that stores the person's phone number (up to 10 characters).
   - `vehicle_no` is a CharField that stores the vehicle number of the person (up to 10 characters).

3. **STUDENTS_DATA** Model:
   - This model represents the basic data of students enrolled in the institute.
   - `roll_no` is an IntegerField that stores the roll number of the student and serves as the primary key for this model.
   - `name` is a CharField that stores the name of the student (up to 50 characters).
   - `room_no` is an IntegerField that stores the room number of the student.
   - `phone` is a CharField that stores the student's phone number (up to 10 characters).
   - `email` is an EmailField that stores the student's email address.
   - `batch` is a CharField that stores the batch or year of the student (up to 15 characters).
   - `branch` is a CharField that stores the branch or department of the student (up to 10 characters).

### forms.py

This file contains several Django form classes that are used to handle user input and interact with the database models. Forms include user creation forms, student creation forms, entry forms etc. The form structures are as follows:

1. **SignUpForm**:
   - This form inherits from `UserCreationForm` and is used for user registration.
   - It includes fields for `email`, `first_name`, `last_name`, `group` (a choice field to select a user group), `username`, `password1`, and `password2`.
   - It customizes the appearance and behavior of various form fields using HTML attributes and help text.

2. **AddNIPDetailsForm**:
   - This form is a ModelForm that corresponds to the `NON_INSTITUTE_ADMITTED` model.
   - It includes fields for `vehicle_no`, `reason`, `name`, `phone`, and `created_at`.
   - The `created_at` field is automatically populated with the current date and time.
   - This form is likely used to create records for visitors who are not part of the institute.

3. **AddInstituteAdmittedDetailsForm**:
   - This form is a ModelForm that corresponds to the `INSTITUTE_ADMITTED` model.
   - It includes fields for `created_at`, `name`, `roll_no`, `reason`, `permission`, `phone`, `vehicle_no`, `batch` (a choice field), and `branch` (a choice field).
   - The `created_at` field is automatically populated with the current date and time.
   - This form is likely used to create records for students admitted to the institute.

4. **AddStudentDetailsForm**:
   - This form is a ModelForm that corresponds to the `STUDENTS_DATA` model.
   - It includes fields for `name`, `roll_no`, `email`, `room_no`, `phone`, `batch` (a choice field), and `branch` (a choice field).
   - This form is likely used to create or update student records in the database.

5. **UpdateStudentForm**:
   - This form is a ModelForm that corresponds to the `STUDENTS_DATA` model.
   - It includes only the `roll_no` field, which is used to retrieve the student record for updating.
   - This form is likely used in conjunction with another form or view to update student details.

Overall, these forms provide a way to handle user input for various operations related to student management, visitor tracking, and user registration. They interact with the corresponding database models and facilitate data entry, validation, and submission.

### urls.py

This file defines the URL patterns for a Django application using the `path` function from `django.urls`. Here's an explanation of each URL pattern:

1. `path('', views.home, name='home')`: This maps the root URL (`''`) to the `home` view function. The `name='home'` part provides a way to refer to this URL pattern from other parts of the application.

2. `path('login_user/<str:user_group>/', views.login_user, name='login_user')`: This maps the URL `login_user/` followed by a string parameter `user_group` to the `login_user` view function. The `name='login_user'` part provides a way to refer to this URL pattern.

3. `path('logout_user/', views.logout_user, name='logout_user')`: This maps the URL `logout_user/` to the `logout_user` view function.

4. `path('upload_image/<str:user>/', views.upload_image, name='upload_image')`: This maps the URL `upload_image/` followed by a string parameter `user` to the `upload_image` view function.

5. `path('add_non_record/', views.add_non_record, name='add_non_record')`: This maps the URL `add_non_record/` to the `add_non_record` view function.

6. `path('add_student_record/', views.add_student_record, name='add_student_record')`: This maps the URL `add_student_record/` to the `add_student_record` view function.

7. `path('new_user/', views.new_user, name='new_user')`: This maps the URL `new_user/` to the `new_user` view function.

8. `path('register/', views.register, name='register')`: This maps the URL `register/` to the `register` view function.

9. `path('student_management/', views.student_management, name='student_management')`: This maps the URL `student_management/` to the `student_management` view function.

10. `path('update_student/', views.update_student, name='update_student')`: This maps the URL `update_student/` to the `update_student` view function.

11. `path('new_student/', views.new_student, name='new_student')`: This maps the URL `new_student/` to the `new_student` view function.

12. `path('add_student_details/', views.add_student_details, name='add_student_details')`: This maps the URL `add_student_details/` to the `add_student_details` view function.

13. `path('get_students_data/', views.get_students_data, name='get_students_data')`: This maps the URL `get_students_data/` to the `get_students_data` view function.

14. `path('filter_student_records/', views.filter_student_records, name='filter_student_records')`: This maps the URL `filter_student_records/` to the `filter_student_records` view function.

15. `path('get_details/', views.get_details, name='get_details')`: This maps the URL `get_details/` to the `get_details` view function.

16. `path('check/', views.check, name='check')`: This maps the URL `check/` to the `check` view function.

17. `path('update_student_details/', views.update_student_details, name='update_student_details')`: This maps the URL `update_student_details/` to the `update_student_details` view function.

18. `path('delete_student/', views.delete_student, name='delete_student')`: This maps the URL `delete_student/` to the `delete_student` view function.

19. `path('check_r/', views.check_r, name='check_r')`: This maps the URL `check_r/` to the `check_r` view function.

20. `path('confirm_delete/', views.confirm_delete, name='confirm_delete')`: This maps the URL `confirm_delete/` to the `confirm_delete` view function.

21. `path('analytics/', views.analytics, name='analytics')`: This maps the URL `analytics/` to the `analytics` view function.

22. `path('chart_data/', views.chart_data, name='chart_data')`: This maps the URL `chart_data/` to the `chart_data` view function.

These URL patterns define the mapping between URLs and the corresponding view functions in the `views.py` file. When a user accesses a particular URL, Django will execute the associated view function and generate a response based on the logic defined in that function.

### views.py

This file consists of the view mapping to the URL's:

1. `home(request)`:
   - This function renders the `home.html` template, which is likely the homepage of the application.
   - It prints the current date and time to the console using `datetime.datetime.now()`.

2. `login_user(request, user_group)`:
   - This function handles user authentication and login.
   - If the request method is POST, it tries to authenticate the user with the provided username and password.
   - If the authentication is successful, it checks the user's group membership (admin or guard).
   - If the user belongs to the admin group, it logs them in and renders the `admin.html` template.
   - If the user belongs to the guard group, it logs them in and renders the `guard.html` template, passing two form instances (`AddInstituteAdmittedDetailsForm` and `AddNIPDetailsForm`).
   - If the user doesn't belong to either group, it displays an error message and redirects to the home page.
   - If the request method is not POST, it renders the `login.html` template with the user_group context variable.

3. `upload_image(request, user)`:
   - This function handles image upload and processing.
   - If the request method is POST and an image file is provided, it saves the image file as "temp.jpg" in the "test/" directory.
   - If the user is a "guard", it attempts to retrieve student details based on the roll number obtained from the image (commented out code). It then creates a new `INSTITUTE_ADMITTED` object with the student details and renders the `guard.html` template with the new object and forms.
   - If the user is an "admin", it retrieves the `INSTITUTE_ADMITTED` entries for the roll number obtained from the image and renders the `students_data.html` template with the retrieved entries.
   - If the request method is not POST or no image is provided, it renders the `guard.html` template with the forms.

4. `add_student_record(request)`:
   - This function handles adding a new student record to the `INSTITUTE_ADMITTED` model.
   - If the user is authenticated and the request method is POST, it creates an instance of `AddInstituteAdmittedDetailsForm` with the submitted data.
   - If the form is valid, it saves the form data to the database and redirects back to the same view.
   - If the request method is not POST, it renders the `guard.html` template with the `AddInstituteAdmittedDetailsForm` and `AddNIPDetailsForm` instances.

5. `add_non_record(request)`:
   - This function handles adding a new record to the `NON_INSTITUTE_ADMITTED` model.
   - If the user is authenticated and the request method is POST, it creates an instance of `AddNIPDetailsForm` with the submitted data.
   - If the form is valid, it saves the form data to the database and redirects back to the same view.
   - If the request method is not POST, it renders the `guard.html` template with the `AddInstituteAdmittedDetailsForm` and `AddNIPDetailsForm` instances.

6. `new_user(request)`:
   - This function renders the `register.html` template with an instance of the `SignUpForm` if the user is authenticated.
   - If the user is not authenticated, it displays a success message and redirects to the home page.

7. `register(request)`:
   - This function handles user registration.
   - If the request method is POST, it creates an instance of `SignUpForm` with the submitted data.
   - If the form is valid, it creates a new user, sets their password, saves the user, and assigns them to the specified group.
   - It displays a success message and redirects to the `new_user` view.
   - If the request method is not POST, it renders the `register.html` template with the `SignUpForm` instance.

8. `get_students_data(request)`:
   - This function retrieves student data from the `INSTITUTE_ADMITTED` model, grouped by batch year.
   - It renders the `students_data.html` template with the retrieved data.

9. `filter_student_records(request)`:
   - This function handles filtering student records based on name, roll number, batch, and branch.
   - If the request method is POST, it retrieves the filter criteria from the submitted form data.
   - It queries the `INSTITUTE_ADMITTED` model based on the provided filter criteria and stores the results in separate variables.
   - It renders the `students_data.html` template with the filtered data and the filter criteria.
   - If the request method is not POST, it redirects to the `get_students_data` view.

10. `get_details(request)`:
    - This function retrieves all records from the `NON_INSTITUTE_ADMITTED` model.
    - It renders the `details.html` template with the retrieved data.

11. `student_management(request)`:
    - This function renders the `admin_choice.html` template if the user is authenticated.
    - If the user is not authenticated, it displays a success message and redirects to the home page.

12. `new_student(request)`:
    - This function renders the `student_management.html` template with an instance of the `AddStudentDetailsForm` if the user is authenticated.
    - If the user is not authenticated, it displays a success message and redirects to the home page.

13. `add_student_details(request)`:
    - This function handles adding a new student to the `STUDENTS_DATA` model.
    - If the user is authenticated and the request method is POST, it creates an instance of `AddStudentDetailsForm` with the submitted data.
    - If the form is valid, it saves the form data to the database, displays a success message, and redirects to the `new_student` view.
    - If the form is not valid, it displays an error message and redirects to the `new_student` view.
    - If the request method is not POST, it renders the `student_management.html` template with the `AddStudentDetailsForm` instance.

14. `update_student(request)`:
    - This function renders the `roll.html` template with an instance of the `UpdateStudentForm` if the user is authenticated.
    - If the user is not authenticated, it displays a success message and redirects to the home page.

15. `check(request)`:
    - This function handles retrieving a student's details based on their roll number for updating.
    - If the request method is POST, it retrieves the roll number from the submitted form data.
    - If the roll number is provided, it retrieves the corresponding `STUDENTS_DATA` entries and renders the `update_student.html` template with the retrieved entries, roll number, and an instance of `AddStudentDetailsForm`.
    - If the roll number is not provided, it displays an error message and redirects to the `update_student` view.
    - If the request method is not POST, it renders the `roll.html` template with an instance of `UpdateStudentForm`.

16. `update_student_details(request)`:
    - This function handles updating a student's details in the `STUDENTS_DATA` model.
    - If the user is authenticated and the request method is POST, it retrieves the submitted data (name, email, phone, room number, batch, branch) and the roll number.
    - It retrieves the existing student object from the database based on the roll number and updates the object's fields with the submitted data.
    - It saves the updated object to the database, displays a success message, and renders the `update_student.html` template with the updated student data.
    - If the request method is not POST, it renders the `update_student.html` template with an instance of `UpdateStudentForm`.

17. `delete_student(request)`:
    - This function renders the `roll_d.html` template with an instance of `UpdateStudentForm` if the user is authenticated.
    - If the user is not authenticated, it displays a success message and redirects to the home page.

18. `check_r(request)`:
    - This function handles retrieving a student's details based on their roll number for deleting.
    - If the request method is POST, it retrieves the roll number from the submitted form data.
    - If the roll number is provided, it retrieves the corresponding `STUDENTS_DATA` and `INSTITUTE_ADMITTED` entries and renders the `delete.html` template with the retrieved entries and roll number.
    - If the roll number is not provided, it displays an error message and redirects to the `delete_student` view.


### templates
    This folder contains all the HTML files and instead of using a dedicated javascript or css file, I have implemented the javascript API and styles from css in the needed respective HTML files inside the template folder.

### Database
    Normally all the projects used sqlite3 as the database but I have used MySql at it inlined with my college course on databases.

## Comments

This project involves all the major functionality that Django provides with multiple table addition, authorisation, authentication, forms etc. I also involved an additional face recognition system to identify and make record on the basis of photographs. It involves using a face recognition model from github, so we need to have that model, all the functionality has been made for that. The site took ample amount of time to make to implement the logic and beautify.

## Working

Install all the requirements from the requirements.txt file.
We need Django and mysqlclient for the working.
In the database_inti.py file I have defined the code for the intialisation of the sql database and if the database gets stuck run this file to initialise the new database.

This file has the username and password for the Mysql database.
Apply all the migrations.
