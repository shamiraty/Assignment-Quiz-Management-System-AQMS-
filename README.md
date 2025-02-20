## **ASSIGNMENT & QUIZ MANAGEMENT SYSTEM (AQMS) DOCUMENTATION**
## **INFORMATION SYSTEMS DEVELOPMENT & MANAGEMENT**
![1](https://github.com/user-attachments/assets/ff3f6bb8-257e-43cf-a127-08663ff4cb5b)

## Contact Information

- **Location**: Dodoma, Tanzania
- **Email**: [sashashamsia@gmail.com](mailto:sashashamsia@gmail.com)
- **WhatsApp**: [+255675839840](https://wa.me/255675839840)
- **Youtube**: [Videos](https://www.youtube.com/channel/UCjepDdFYKzVHFiOhsiVVffQ)
- **Live Demo**: [Demo](https://collegeforce.pythonanywhere.com/)

## Admin Login Credentials

To access the admin panel, use the following login credentials:

- **Username**: `admin@college300.co.tz`
- **Password**: `demo1234`

| **Testing Data for Modules** | **Value** |
|------------------------------|-----------|
| **Modules** | Discover Assignments and Quizzes HTML page, Create Group Members HTML page |
| **Academic Year** | 2025-2026 |
| **Year of Study** | Year 1 |
| **Stream** | Evening Classes |
| **Level** | Bachelor Degree |
| **Programme** | Management Practice [2025-2026 Evening] |

## 1. Introduction

The **Assignment & Quiz Management System (AQMS)** is a comprehensive web-based platform designed to streamline the management of academic assignments and quizzes within educational institutions. The system serves both instructors and students, providing a seamless experience for uploading, managing, and tracking academic materials such as assignments and quizzes. Instructors can upload tasks, manage courses, and student data, while students can easily access materials, participate in group assignments, and track deadlines. The system ensures efficiency, fairness, and real-time analytics by automating manual processes that were previously prone to errors and inefficiency.

---

## 2. Problem Statement

Currently, the management of assignments and quizzes in educational institutions involves manual processes, which present a number of challenges:
- **Time-Consuming Processes**: Instructors find it difficult to distribute assignments or quizzes across multiple programs or years, which consumes a lot of time.
- **Biased Group Formation**: Manual group creation often leads to inconsistencies and dissatisfaction among students as some groups may have imbalanced workloads or skill sets.
- **Deadline Tracking Issues**: Students frequently miss deadlines due to the absence of a centralized and automated reminder system.
- **Limited Analytics**: Educational institutions lack detailed insights into assignment distribution by program, course, or department.
- **File Management Issues**: Physical or email-based submissions are prone to data loss, lack of organization, and versioning issues, leading to confusion and inefficiencies.

---

## 3. Importance of the Project

The **Assignment & Quiz Management System (AQMS)** aims to address these challenges through automation and centralized management. The key benefits of the system include:
- **Centralized Assignment and Quiz Uploads**: Instructors can upload assignments and quizzes along with deadlines, files, and rich-text questions, making it easier for students to access.
- **Automated Group Formation**: The system generates randomized groups for assignments to ensure fairness and eliminate biases.
- **Deadline Alerts**: The platform notifies students of upcoming deadlines with color-coded tables for overdue tasks, ensuring timely submissions.
- **Comprehensive Analytics Dashboard**: Instructors and administrators can view analytics on the distribution of assignments and quizzes across different programs and courses.
- **Secure File Management**: The system offers secure file uploads with proper access control, reducing the risks of data loss and disorganization.
- **Flexible Filtering**: Students can filter assignments and quizzes by program, academic year, year of study, courses, etc., making navigation easier and more efficient.

---

## 4. Main Objective

The main objective of the AQMS is to develop a digital platform that automates the distribution and tracking of assignments and quizzes, simplifies group formation for collaborative tasks, and provides real-time analytics. This platform aims to improve transparency, streamline academic workflows, and enhance the educational experience for both students and instructors.

---

## 5. Specific Objectives

The system aims to accomplish the following specific objectives:
1. **Instructor Modules**:
   - Upload assignments and quizzes with specific deadlines, files, and questions.
   - Manage programs, courses, and student registrations.
   - View analytics on assignment and quiz distribution across different programs.
2. **Student Modules**:
   - Filter assignments and quizzes based on program, academic year, year of study, and courses.
   - Generate randomized groups to ensure fairness in collaborative assignments.
   - Download materials, view deadlines, and track the progress of their tasks.
3. **System Features**:
   - A responsive user interface with role-based access control (instructors vs. students).
   - Ability to export group data to CSV/PDF for record-keeping.
   - Color-coded alerts for upcoming and overdue tasks to help students manage deadlines effectively.

---

## 6. Methodology

### Technologies Used
- **Backend**:
  - **Django**: A Python web framework used for implementing the MVC architecture to manage backend logic and database interactions.
  - **SQL-LITE**: A relational database used to manage data related to programs, students, assignments, and quizzes.
  
- **Frontend**:
  - **Bootstrap**: A front-end framework used to create responsive designs and improve the user experience.
  - **jQuery/Select2**: Libraries used for dynamic dropdowns and interactions within the user interface.
  - **DataTables**: A plug-in for displaying and exporting tables, making data presentation more interactive.

- **Additional Tools**:
  - **CKEditor**: A rich text editor used for creating detailed questions for assignments and quizzes.
  - **Django Admin**: Used by instructors to manage the platform through an easy-to-use interface.

- **Security**:
  - Role-based access control (RBAC) ensures that only authorized users (instructors vs. students) can perform certain actions, like uploading assignments or accessing analytics.
  - **Django FileField**: Used to manage secure file uploads and limit access based on user roles.


## 7. System Roles

The system involves two main roles: **Instructor** and **Student**, each with distinct responsibilities. Below is a summary of their tasks and capabilities within the platform:

| **Role**     | **Responsibilities**                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------|
| **Instructor** | - Uploads assignments and quizzes to a specific program, with deadlines and files.                                           |
|              | - Adds, edits, or deletes assignments and quizzes as required.                                                              |
|              | - Manages the creation and maintenance of programs, academic years, courses, students, streams, and departments.             |
|              | - Can view the analytics related to the assignments and quizzes for their program(s).                                      |
| **Student**   | - Searches for assignments or quizzes by program, academic year, year of study, or course.                                |
|              | - Generates random groups for collaborative assignments to ensure unbiased group formation.                                 |
|              | - Can see analytics on the number of assignments and quizzes assigned to each program they are enrolled in.                |

---
## 7. Group Generation

To ensure that the group creation process is fair and unbiased, students are randomly assigned to groups. The randomization process eliminates any subjective preferences or biases in grouping. This feature ensures equal distribution of students across groups, providing a fair environment for group assignments.

### Group Generation Algorithm

To ensure that students are distributed into groups in a fair and unbiased manner, the following algorithm is used:
```python
students = list(Student.objects.filter(...))  # Apply necessary filters
random.shuffle(students)
groups = [[] for _ in range(group_count)]
for index, student in enumerate(students):
    groups[index % group_count].append(student)
```
## 8. Methodology

### Functionality References

8.1. **Assignment & Quiz Upload and Management**:
   - **Instructors** are able to upload, update, or delete assignments and quizzes associated with specific programs, academic years, and courses. This functionality ensures that the latest academic materials are always available for students, and instructors can modify content as required.

8.2. **Random Group Formation**:
   - The **system** automatically generates student groups for assignments or quizzes to ensure that groups are balanced and free of biases. This ensures that no group is unfairly composed of stronger or weaker students based on subjective decisions.

8.3. **Analytics and Tracking**:
   - The system provides detailed analytics for **instructors** on the total number of assignments and quizzes assigned to students, allowing instructors to monitor the workload distribution across various programs and courses.

8.4. **Deadline Management and Alerts**:
   - The platform automatically alerts **students** and **instructors** of upcoming deadlines. This functionality ensures that assignments and quizzes are submitted on time, and no student misses any due dates.

8.5. **Search and Filter for Assignments**:
   - **Students** can filter assignments and quizzes by their program, academic year, and course, ensuring that they can easily find the materials relevant to their current study.

---

## 9. Conclusion

The **Assignment & Quiz Management System (AQMS)** provides a streamlined, efficient solution to many of the challenges faced in educational institutions when managing academic tasks. By automating the distribution of assignments and quizzes, ensuring fairness in group formation, and providing real-time analytics, AQMS enhances the academic experience for both instructors and students. The system’s role-based access control, file management capabilities, and deadline tracking features ensure a secure and user-friendly environment for managing academic materials.

---

## 10. References

1. **Smith, J.** (2019). *Automating Group Creation in Academic Systems*. Journal of Educational Technology, 13(4), 45-58.  
2. **Brown, A.** (2020). *Effective Deadline Management for Student Success*. Journal of Online Education, 22(1), 78-89.  
3. **Johnson, R. & Lee, P.** (2018). *Managing Academic Workload with Online Systems*. International Journal of Educational Management, 15(3), 101-113.  
4. **Williams, L.** (2021). *Analyzing Assignment Distribution in Higher Education*. Academic Analytics Journal, 19(2), 44-50.  
5. **Chang, Y.** (2022). *Fairness in Group Assignments in Education*. Journal of Educational Research, 30(2), 61-72.  


