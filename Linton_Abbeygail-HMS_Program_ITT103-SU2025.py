#import required libraries
import random
from datetime import datetime

#creating a function that will create id numbers for the patients, doctors and appointment with prefixes PAT, DOC & APT
#respectively
def generate_id(prefix):
    return prefix + str(random.randint(10000,99999))

#creating a function that will check if the time is available in the doctors schedule
def is_time_available(schedule, date, time):
    return (date, time) not in schedule


#creating the parent class Person which represents a person with the attributes name, gender and age
#Person is a super class

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

#creating a method to view person information
    def display_info(self):
        print(f"Name           : {self.name}")
        print(f"Gender         : {self.gender}")
        print(f"Age            : {self.age}")


#creating the class Patient which is a subclass of the Person parent class
#Patient class has added attributes patient ID and appointment list

class Patient(Person):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.patient_id = generate_id("PAT")
        self.appointment_list = []

#creating a method that allows the user to book a patient's appointment
    def book_appointment(self, appointment):
        self.appointment_list.append(appointment)

#creating a method that allows the user to view the patient's profile as well as to see if the patient has a previous
#appointment
    def profile_view(self):
        print("\n**Patient Profile Details**")
        self.display_info()
        print(f"Patient ID#      : {self.patient_id}")
        print("Appointments     : ")
        if self.appointment_list:
            for appt in self.appointment_list: #showing previous appointments
                print(f"Appointment ID: {appt.appointment_id} - Dr. {appt.doctor.name} - Date: {appt.date} at {appt.time}")
        else:
            print(f"No Previous Appointments. Please Book an Appointment") #shown where the patient has no previous
            # appointment at the hospital

#creating the class Doctor which is a subclass of the parent class Person
#Doctor class has added attributes doctor id, specialty and schedule

class Doctor(Person):
    def __init__(self, name, age, gender, specialty):
        super().__init__(name, age, gender)

        self.doctor_id = generate_id("DOC")
        self.specialty = specialty
        self.schedule = []

#creating a method that allows the user to check doctors availability
    def is_available (self, date, time):
        return is_time_available(self.schedule, date, time)

#creating a method that allows the user to view the doctors full schedule
    def view_schedule(self):
        print(f"\nDr. {self.name}'s schedule is:")
        if self.schedule:
            for date,time in self.schedule:
                print(f"{date} at {time}") #shows the appointments on the doctor's scheduled
        else:
            print("No Appointment Found") #shown when the doctor has no scheduled appointment

#creating class for appointment scheduling which has the attributes appointment ID, patient, doctor, date, time and status
class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.appointment_id = generate_id("APT")
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Appointment Confirmed!!"

#creating a method that allows a user to confirm and appointment and view the appointment ID
    def confirm(self):
        print(f"\nAppointment with ID {self.appointment_id} is confirmed")

#creating a method that allows the user to cancel an appointment
    def cancel(self):
        self.status = "Appointment is Cancelled"
        print(f"\nAppointment with id {self.appointment_id} is successfully cancelled")

#creating class for the hospital system with attributes patients, doctors and appoints
#the class controls the adding of patients and doctors, booking or cancelling of appointments as well as to generate a hospital bill

class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

#creating a method that allows the user to add a patient to the hospital system database
    def add_patient(self, name, gender, age):
        try:
            age = int(age) #only accepting integers greater than zero for the age input
            if age <=0:
                raise ValueError
        except ValueError:
            print("Invalid Entry. Please Enter a Valid Age")
            return

        if gender.upper() not in ["male", "female", "m", "f", "Male", "Female", "M", "F", "MALE", 'FEMALE']: #only
            # accepting entries from the list for gender input
            print("Invalid Gender. Please retry")
            return

        patient = Patient(name, age, gender.capitalize())
        self.patients[patient.patient_id] = patient
        print(f"\nPatient Successfully Added to Database, Patient ID: {patient.patient_id}")
        print(f"")

#creating a method that allows the user to add a doctor to the hospital system database
    def add_doctor(self, name, age, gender, specialty):
        try:
            age = int(age)  #only accepting integers greater than zero for the age input
            if age <=0:
                raise ValueError
        except ValueError:
            print("Invalid Entry. Please Enter a Valid Age")
            return
        # only accepting entries from the list for gender input
        if gender not in ["male", "female", "m", "f", "Male", "Female", "M", "F", "MALE", 'FEMALE']:
            print("Invalid Gender. Please retry")
            return
        doctor = Doctor(name, age, gender.capitalize(), specialty)
        self.doctors[doctor.doctor_id] = doctor
        print(f"\nDoctor Successfully Added to Database, Doctor ID: {doctor.doctor_id}")

#creating a method that allows the user to add an appointment to the hospital system database
    def appointment_booking(self, patient, doctor, date, time):
        while True: #loops until a valid patient or doctor id is entered and if the doctor is also available
            patient = self.patients.get(patient)
            doctor = self.doctors.get(doctor)

            if not patient or not doctor: #error handle when and unrecognized patient or doctor id is entered when booking an appointment
                print("Invalid Patient or Doctor Id")
                return

            if not doctor.is_available(date, time): #checking to see whether the doctor is available for the date and time of an appointment
                print("Doctor is not available, Please choose a different doctor.")
                return
            else:
                break
        appointment = Appointment(patient, doctor, date, time)
        self.appointments[appointment.appointment_id] = appointment
        patient.book_appointment(appointment)
        doctor.schedule.append((date, time))
        appointment.confirm()

#creating a method that allows the user to confirm an appointment in the hospital system database
    def confirm_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            appointment.confirm()
        else:
            print("Appointment not found, Retry")

# creating a method that allows the user to cancel an appointment in the hospital system database
    def cancel_appointment(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        if appointment:
            if (appointment.date, appointment.time) in appointment.doctor.schedule:
                appointment.doctor.schedule.remove((appointment.date, appointment.time))
            appointment.cancel()
            del self.appointments[appointment_id]
        else:
            print("Appointment not found, Retry")

#creating a method that allows the user to generate a bill from an appointment in the hospital system database and manually enter additional charges
    def generate_bill(self, appointment_id):
        appointment = self.appointments.get(appointment_id)
        hospital_name = "Linton Memorial Hospital"
        hospital_address = "123 Abbey Street, Kingston"
        hospital_tel = "876-512-3454"
        hospital_email = "linmemorial@hospital.com"
        consultation_fee = 3000

        if not appointment:
            print("\n No Appointment Found")
            return
        else:
            print("\n*******************************************************")
            print(f"{hospital_name}")
            print(f"{hospital_address}")
            print(f"{hospital_email}")
            print(f"{hospital_tel}")
            print("\n*******************************************************")
            print("")
            print("")
            print("Billing Detail:")
            print(f"\nAppointment ID: {appointment_id}")
            print("\n*******************************************************")
            print(f"\nConsultation Fee: ${consultation_fee}JMD")
            try:
                add_charge = float(input("Additional Charges (Lab/Rx):         "))
            except ValueError:
                print('Invalid input, No Additional Charge')
                add_charge = 0.00
            print("\n******************************************************************")

            total = consultation_fee + add_charge
            insurance = input("Does Patients have Health Insurance? (Yes/NO): ") #adding an insurance discount if the patient has insurance
            if insurance == "yes" or insurance == "YES" or insurance == "y" or insurance == "Yes":
                insurance = total * 0.20
            else:
                insurance = 0.00
            discount = 0.00
            if total >= 5000: #adding discount to a patient's bill if the total is over $5000
                discount = total * 0.05
            adj_total = total - insurance - discount
            #all balances are rounded to 2 decimal places
            print(f"\nTotal           :                           ${total:.2f}JMD")
            print(f"Insurance (20%) :                           ${insurance:.2f}JMD")
            print(f"Discount (5%)   :                           ${discount:.2f}JMD")
            print("\n******************************************************************")
            print(f"\nFINAL BILL      :                           ${adj_total:.2f}JMD")
            print("\n******************************************************************")
            print(f"\n Thank you for Choosing {hospital_name}! COME AGAIN NEXT TIME!!!")
            print("\n******************************************************************")

#MAIN PROGRAM LOOP
#this section displays the hospital systems main menu which the user will choose from the options listed

def main():
    hospital = HospitalSystem()
    hospital_name= "Lin's Memorial Hospital"

    while True:
        print(f"\nWelcome to {hospital_name}!!!!! Management System. What would you like to do?")
        print("\n1. Register Patient")
        print("2. Add Doctor")
        print("3. Book New Appointment")
        print("4. Confirm Existing Appointment")
        print("5. Cancel Existing Appointment")
        print("6. View Patient Profile")
        print("7. View Doctor Schedule")
        print("8. View Patient Bill")
        print("9. Exit")

        option = input("\nChoose Number: ").strip()

        if option == "1": #user chose to register a patient
            name = input("Patient Name: ").strip()
            age = input("Age: ").strip()
            gender = input("Gender (Male/Female): ").strip()
            hospital.add_patient(name, age, gender) #user calls for the add patient method in the hospital system and
            # stores the information in the respective attributes

        elif option == "2": #user chose to register a doctor
            name = input("Doctor Name: ").strip()
            age = input("Age: ").strip()
            gender = input("Gender (Male/Female): ").strip()
            specialty = input("Specialty: ")
            hospital.add_doctor(name, age, gender, specialty) #user calls for the add doctor method in the hospital
            # system and stores the information in the respective attributes

        elif option == "3": #user chose to book an appointment
            pid = input("Patient ID: ").strip()
            did = input("Doctor ID: ").strip()
            date_input = input("Date (dd/mm/yy: ").strip()
            time_input = input("Time (00:00): ").strip()

            # error handling to ensure that the date & time are entered in the correct format where it loops until
            # the correct format is entered
            while True:
                try:
                    datetime.strptime(date_input, "%d/%/%y") #error handling to ensure that the date & time are
                    #in the correct format
                    datetime.strptime(time_input, "%H:%M")
                except ValueError:
                    print("Invalid date or time format. Use dd/mm/yy and 24hr HH:MM format")
                    continue
                hospital.appointment_booking(pid, did, date_input,time_input)  # user calls for the add appointment
                #booking method in the hospital system and stores the information in the respective attributes
                break

        elif option == "4":  # user chose to confirm an appointment
            appt_id = input("Enter Appointment ID: ")
            hospital.confirm_appointment(appt_id) #user calls for the confirm appointment method in the hospital system
            #that confirms an existing appointment

        elif option =="5": #user chose to cancel an appointment
            appt_id = input("Enter Appointment ID: ").strip()
            hospital.cancel_appointment(appt_id) #user calls for the cancel appointment method in the hospital system that cancels an existing appointment

        elif option == "6": #user chose to view a patient's profile
            pid = input("Enter Patient ID:")
            patient = hospital.patients.get(pid)
            if patient:
                patient.profile_view() #user calls for the profile view method in the patient class that displays a patient's information
            else:
                print("Patient not found!!") #error handling if the patient id is not recognized

        elif option == "7": #user chose to view a doctor's schedule
            did = input("Doctor ID: ").strip()
            doctor = hospital.doctors.get(did)
            if doctor:
                doctor.view_schedule() #user calls for the view schedule method in the doctor class that displays a patient's information
            else:
                print("Doctor schedule not found!!") #error handling if the doctor id is not recognized

        elif option == "8": #user chose to generate a bill for an appointment
            appt_id = input("Appointment ID: ").strip()
            hospital.generate_bill(appt_id) #user calls for the generate bill method in the hospital system that shows
            #a formatted bill from an existing appointment

        elif option =="9": #user is exiting hospital system
            print("Good Bye")
            break
        else:
            print("Option Not found. Enter Valid Menu Option") #error handling if the option chosen is not a valid menu option

if __name__ == "__main__":
    main()










