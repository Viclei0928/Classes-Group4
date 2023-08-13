# Class#1 Doctor

class Doctor:
    def __init__(self, doctor_id="", name="", specialization="", working_time="", qualification="", room_number=""):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

    # Implement getters and setters for properties
    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def get_working_time(self):
        return self.working_time

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

# Class#2 Doctor Manager

class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return str(doctor)

    def enter_dr_info(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Doctor Specialization: ")
        working_time = input("Enter Doctor Working Time: ")
        qualification = input("Enter Doctor Qualification: ")
        room_number = input("Enter Doctor Room Number: ")
        return Doctor(doctor_id, name, specialization, working_time, qualification, room_number)

    def read_doctors_file(self):
        try:
            with open("doctors.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    doctor_info = line.strip().split("_")
                    doctor = Doctor(*doctor_info)
                    self.doctors.append(doctor)
        except FileNotFoundError:
            print("No doctors data file found. Starting with an empty list.")

    def search_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same id on the system")

    def search_doctor_by_name(self, doctor_name):
        for doctor in self.doctors:
            if doctor.get_name() == doctor_name:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, doctor):
        print("Doctor Information:")
        print(f"Doctor ID: {doctor.get_doctor_id()}")
        print(f"Name: {doctor.get_name()}")
        print(f"Specialization: {doctor.get_specialization()}")
        print(f"Working Time: {doctor.get_working_time()}")
        print(f"Qualification: {doctor.get_qualification()}")
        print(f"Room Number: {doctor.get_room_number()}")

    def edit_doctor_info(self):
        doctor_id = input("Enter the ID of the doctor you want to edit: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                new_name = input("Enter the new name: ")
                new_specialization = input("Enter the new specialization: ")
                new_working_time = input("Enter the new working time: ")
                new_qualification = input("Enter the new qualification: ")
                new_room_number = input("Enter the new room number: ")
                doctor.set_name(new_name)
                doctor.set_specialization(new_specialization)
                doctor.set_working_time(new_working_time)
                doctor.set_qualification(new_qualification)
                doctor.set_room_number(new_room_number)
                self.write_list_of_doctors_to_file()
                print(f"Doctor whose id is {doctor_id} has been edited.")
                return
        print("Cannot find the doctor with the same id on the system")

    def display_doctors_list(self):
        print("Doctors List:")
        for doctor in self.doctors:
            self.display_doctor_info(doctor)

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        self.write_list_of_doctors_to_file()
        print(f"Doctor whose id is {new_doctor.get_doctor_id()} has been added.")

# Class#3 Patient

class Patient:
    def __init__(self, pid="", name="", disease="", gender="", age=""):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

    # Implement getters and setters for properties
    def get_pid(self):
        return self.pid

    def set_pid(self, new_pid):
        self.pid = new_pid

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_disease(self):
        return self.disease

    def set_disease(self, new_disease):
        self.disease = new_disease

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

# Class 4   
class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        return str(patient)

    def enter_patient_info(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient Gender: ")
        age = input("Enter Patient Age: ")
        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        try:
            with open("patients.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    patient_info = line.strip().split("_")
                    patient = Patient(*patient_info)
                    self.patients.append(patient)
        except FileNotFoundError:
            print("No patients data file found. Starting with an empty list.")

    def search_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                self.display_patient_info(patient)
                return
        print("Can't find the patient with the same id on the system")

    def display_patient_info(self, patient):
        print("Patient Information:")
        print(f"Patient ID: {patient.get_pid()}")
        print(f"Name: {patient.get_name()}")
        print(f"Disease: {patient.get_disease()}")
        print(f"Gender: {patient.get_gender()}")
        print(f"Age: {patient.get_age()}")

    def edit_patient_info_by_id(self):
        patient_id = input("Please enter the id of the patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                new_name = input("Enter the new name: ")
                new_disease = input("Enter the new disease: ")
                new_gender = input("Enter the new gender: ")
                new_age = input("Enter the new age: ")
                patient.set_name(new_name)
                patient.set_disease(new_disease)
                patient.set_gender(new_gender)
                patient.set_age(new_age)
                self.write_list_of_patients_to_file()
                print(f"Patient whose id is {patient_id}has been edited.")
                return
        print("Cannot find the patient with the same id on the system")

    def display_patients_list(self):
        print("Patients List:")
        for patient in self.patients:
            self.display_patient_info(patient)

    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        self.write_list_of_patients_to_file()
        print(f"Patient whose id is {new_patient.get_pid()} has been added")

print("Welcome to Alberta Hospital(AH) Mangement System")
# Class 5
class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            print("\n Select from the following options, or select 3 to stop:")
            print("1. Doctors")
            print("2. Patients")
            print("3. Exit program")

            option = input("Enter your choice (1/2/3): ")

            if option == '1':
                self.display_doctors_submenu()
            elif option == '2':
                self.display_patients_submenu()
            elif option == '3':
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please enter a valid option (1/2/3).")

    def display_doctors_submenu(self):
        while True:
            print("\nDoctors Menu:")
            print("1. Display Doctors List")
            print("2. Search for doctor by ID")
            print("3. Search for doctor by Name")
            print("4. Add Doctor")
            print("5. Edit Doctor info")
            print("6. Back to Main Menu")

            option = input("Enter your choice (1/2/3/4/5/6): ")

            if option == '1':
                self.doctor_manager.display_doctors_list()
            elif option == '2':
                doctor_id = input("Enter the doctor Id:")
                self.doctor_manager.search_doctor_by_id(doctor_id)
            elif option == '3':
                doctor_name = input("Enter the doctor name:")
                self.doctor_manager.search_doctor_by_name(doctor_name)
            elif option == '4':
                self.doctor_manager.add_dr_to_file()
            elif option == '5':
                self.doctor_manager.edit_doctor_info()
            elif option == '6':
                break
            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4/5/6).")

    def display_patients_submenu(self):
        while True:
            print("\nPatients Menu:")
            print("1. Display Patients List")
            print("2. Search for patient by ID")
            print("3. Add Patient")
            print("4. Edit patient info")
            print("5. Back to the Main Menu")

            option = input("Enter your choice (1/2/3/4/5): ")

            if option == '1':
                self.patient_manager.display_patients_list()
            elif option == '2':
                patient_id = input("Enter the patient id:")
                self.patient_manager.search_patient_by_id(patient_id)
            elif option == '3':
                self.patient_manager.add_patient_to_file()
            elif option == '4':
                self.patient_manager.edit_patient_info_by_id()
            elif option == '5':
                break
            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4/5).")


if __name__ == "__main__":
    management_system = Management()
    management_system.display_menu()


