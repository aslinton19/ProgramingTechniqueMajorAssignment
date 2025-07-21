Author: Abbeygail Linton
Date Created: July 20, 2025
Course: ITT103
GitHub Public URL to Code: https://github.com/aslinton19/ProgramingTechniqueMajorAssignment 
Video Presentation Link: https://drive.google.com/file/d/1VhPqojgvixQIAfbTZv2X53uC6BbMOWV1/view?usp=drive_link 
PROGRAM PURPOSE: This Python console-based program is designed as a Hospital Management System. It allows users to register patients and doctors, manage appointments, confirm or cancel bookings, and generate patient bills. The program was built using object-oriented programming (OOP) techniques.
HOW TO RUN THE PROGRAM: In order to run the program, the following steps must be followed:
1. Ensure PyCharm 2025.1.2 is installed on your machine.
2. Save the file using a desired naming convention
3. Open a terminal or command prompt.
4. Navigate to the folder where the file is saved.
5. Run the program
6. Follow the menu options displayed on screen.

PROGRAM FUNCTIONALITY 
The program takes the form of a menu which shows the functions as menu options to choose from. The functions of the program are:
1. Register Patient - Adds a new patient with a, name, age, gender and generates a unique patient identification number.
2. Add Doctor - Registers a new doctor with a name, age, gender, specialty and generates a unique doctor identification number.
3. Book New Appointment - Books an appointment between a patient and doctor with date and time and creates a unique appointment identification number.
4. Confirm Existing Appointment - Confirms a scheduled appointment using its appointment identification number.
5. Cancel Existing Appointment - Cancels an appointment and removes it from the doctor’s schedule.
6. View Patient Profile - Displays patient's details and all past appointments.
7. View Doctor Schedule - Shows all scheduled appointments for a specific doctor.
8. View Patient Bill - Generates a formatted hospital bill based on appointment details and charges.
9. Exit - Ends the program.
Other functions of the program that are not listed as a menu option includes:
* Appointment, patient, and doctor identification numbers are generated using random numbers with respective prefixes APT, PAT and DOC respectively followed by a 5 digit number
* Users are prompted to input specific information to carry out the menu functions and guided through validations to ensure that correct type of information is entered.
* The program includes helpful messages for invalid entries to improve user experience such as displaying error messages.
REQUIRED MODIFICATIONS 
In the future, for further enhancement of the program, the following modifications can be considered: 
* Add a storage feature which saves the patient, doctor and appointment information permanently or until it is removed by the user.
* Implement username and password logins for admin access to enhanced security.
* Add visual interface here the user can interact with buttons, windows etc. to make the system more user friendly 
* Support real-time appointment conflict resolution, for example where a doctor is being double booked for the same date and time, the program can suggest available time or show the available times for the doctor.
ASSUMPTIONS
The following are a list of conditions the program assumes will be true when running properly:
* All ages entered are valid positive integers.
* Gender inputs are limited to specific valid strings (e.g., "Male", "Female", "M", "F").
* Users will follow the correct input format for the date and time which is dd/mm/yyyy and 24hr HH:MM respectively.
* Doctor and patient identification numbers entered for booking already exist in the system.
* Each appointment is uniquely identified by its generated identification number.
* Only one appointment can be booked for a specific doctor and time slot.
* A fixed consultation fee is always applied before any additional charges or discounts.
 LIMITATIONS: 
The following are limitations of the program:
* All data that is created while running the program is lost when the user exits the program.
* No login feature which can be a security risk.
* Appointments cannot be edited or rescheduled once booked, they can only be cancelled.
* The program doesn’t handle multiple appointments for the same patient at the same time.
* The flat rate consultation fee doesn’t reflect real world hospital billing which can be broken down further based on the services used by the patient or the department the patient visits.
* In a world were gender has evolved only a limited list of gender options (male/female) are accepted.
* The appointment date must follow the dd/mm/yyyy format and time in 24-hour HH:MM format and is symbol specific
* No support for editing or rescheduling appointments.
* Data is stored in-memory only; restarting the program clears all data.
* The program assumes all insurance policies cover exactly 20%, which may not be the true in all cases.
“I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT”
