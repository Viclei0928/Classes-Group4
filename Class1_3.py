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
        print("Can't find the doctor...")

    def search_doctor_by_name(self, doctor_name):
        for doctor in self.doctors:
            if doctor.get_name() == doctor_name:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor...")

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
                print("Doctor information has been edited.")
                return
        print("Cannot find the doctor...")

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
        print("New doctor has been added.")

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

