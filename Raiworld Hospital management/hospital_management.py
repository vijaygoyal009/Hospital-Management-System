import mysql.connector as management

# Connect to MySQL
db = management.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital"
)
cursor = db.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS doctor (
                    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
                    doctor_name VARCHAR(255),
                    speciality VARCHAR(255)
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS patient (
                    patient_id INT AUTO_INCREMENT PRIMARY KEY,
                    patient_name VARCHAR(255),
                    gender varchar(10),
                    phone bigint,
                    Disease VARCHAR(255),
                    admit_date varchar(50),
                    discharge_date varchar(50),
                    address VARCHAR(255),
                    doctor_id INT,
                    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS  management_persons (
                    management_person_id INT AUTO_INCREMENT PRIMARY KEY,
                    management_person_name VARCHAR(255),
                    management_person_password VARCHAR(255)
                )''')





# Function to check login credentials
def login(username, password):
    cursor.execute("SELECT * FROM management_persons WHERE management_person_name=%s AND management_person_password=%s", (username, password))
    if cursor.fetchone():
        return True
    else:
        return False



# from prettytable import PrettyTable
from prettytable import PrettyTable
from pwinput import pwinput

def display_data(data, headers):
    table = PrettyTable(headers)
    for row in data:
        table.add_row(row)
    print(table)







#__________________________________________Doctor's Information Functionj_________________________________________________________



# Doctor Menu
def doctor_menu():
    print("Select an option:")
    print("1. Add new doctor")
    print("2. Update doctor data")
    print("3. Access individual doctor data")
    print("4. Access all doctor data")
    print('5. Delete Specific doctor data')
    option = int(input("Enter your choice: "))
    if option == 1:
        new_doctor()
    elif option == 2:
        update_doctor()
    elif option == 3:
        get_doctor_data()
    elif option == 4:
        show_all_doctors()
    elif option == 5:
        delete_doctor()
    else:
        print("Invalid option.")


# Function to add new doctor
def new_doctor():
    name = input("Enter doctor name: ")
    speciality = input("Enter doctor's speciality: ")
    cursor.execute("INSERT INTO doctor (doctor_name, speciality) VALUES (%s, %s)", (name, speciality))
    db.commit()
    print("New doctor added successfully.")
    print("--------------------------------------")



# Function to update doctor data
def update_doctor():
    doctor_id = int(input("Enter doctor ID to update: "))
    name = input("Enter doctor name: ")
    speciality = input("Enter doctor's speciality: ")
    cursor.execute("UPDATE doctor SET doctor_name=%s, speciality=%s WHERE doctor_id=%s", (name, speciality, doctor_id))
    db.commit()
    print("Doctor data updated successfully.")
    print("--------------------------------------")



#Function to access indivual doctor data
def get_doctor_data():
    doctor_id = int(input("Enter doctor id to access data: "))
    cursor.execute("SELECT * FROM doctor WHERE doctor_id=%s", (doctor_id,))
    data = cursor.fetchone()
    if data:
        table = PrettyTable(["doctor_id", "doctor_name", "speciality"])
        table.add_row(data)
        print(table)
    else:
        print("Doctor not found.")
    print("--------------------------------------")


def show_all_doctors():
    cursor.execute("SELECT * FROM doctor")
    data = cursor.fetchall()
    if data:
        print("All Doctors:")
        headers = ["doctor_id", "doctor_name", "speciality"]
        display_data(data, headers)

    else:
        print("No doctor records found.")




def delete_doctor():
    doctor_id = int(input('Enter the ID of the doctor you want to delete :- '))
    cursor.execute('delete from doctor where doctor_id=%s',(doctor_id,))
    db.commit()
    print('Doctor Delete Successfully !!!')



# _____________________________________________Doctor work done___________________________________________________________




# ____________________________________________Patient Function Start_________________________________________________________________________


# Patient Menu
def patient_menu():
    print("Select an option:")
    print("1. Add new patient")
    print("2. Update patient data")
    print("3. Access individual patient data")
    print('4. Access Patient By Admit Date')
    print('5. Access Patinet By Disease')
    print('6. Access All patient data')
    print('7. Delete specific patient')
    option = int(input("Enter your choice: "))
    if option == 1:
        new_patient()
    elif option == 2:
        update_patient_info()
    elif option == 3:
        get_patient_data()
    elif option == 4:
        Access_Patient_By_Admit_Date()
    elif option == 5:
        Access_Patient_By_Disease()
    elif option == 6:
        show_all_patients()
    elif option == 7:
        delete_patient()
        
    else:
        print("Invalid option.")


def new_patient():
    name = input("Enter patient name: ")
    gender = input('Enter patient gender (Male/Female) :- ')
    phone = int(input('Enter patient mobile number :- '))
    Disease = input("Enter patient's Disease: ")
    admit_date = input('Enter admit date (in this format --- (YY-MM-DD)) :- ')
    discharge_date = input('Enter discharge date (in this format --- (YY-MM-DD)) :- ')
    address = input("Enter patient address: ")
    doctor_id = int(input("Enter doctor ID: "))
    cursor.execute("INSERT INTO patient (patient_name,gender,phone, Disease,admit_date,discharge_date, address,doctor_id) VALUES (%s, %s, %s, %s, %s ,%s,%s,%s)", (name,gender,phone,Disease,admit_date,discharge_date,address,doctor_id ))
    db.commit()
    print("New patient added successfully.")
    print("--------------------------------------")



# Function to update patient data
# def update_patient():
#     patient_id = int(input("Enter patient ID to update: "))
    
    
#     name = input("Enter patient name: ")
#     gender = input('Enter patient gender :- ')
#     phone = int('Enter patient phone number :- ')
#     Disease = input("Enter patient's illness: ")
#     admit_date = input('Enter admit date (in this format --- (YY-MM-DD)) :- ')
#     discharge_date = input('Enter discharge date (in this format --- (YY-MM-DD)) :- ')
#     doctor_id = int(input("Enter doctor ID: "))
#     address = input("Enter patient address: ")
#     cursor.execute("UPDATE patient SET patient_name=%s,gender=%s,phone=%s, Disease=%s,admit_date=%s,discharge_date=%s ,address=%s, doctor_id=%s  WHERE patient_id=%s", (name,gender,phone, Disease,  admit_date, discharge_date, address , doctor_id,))
#     db.commit()
#     print("Patient data updated successfully.")



def update_patient_info():
    patient_name = input("Enter the patient's name to update information: ")
    
    print("Select the information you want to update:")
    print("1. Admit date")
    print("2. Disease")
    print("3. Gender")
    print("4. Phone number")
    print("5. Address")
    print("6. Discharge date")

    choice = input("Enter your choice (separate choices by commas for multiple selections): ")
    choices = [int(x.strip()) for x in choice.split(",")]

    update_query = "UPDATE patient SET "
    values = []

    for choice in choices:
        if choice == 1:
            new_admit_date = input("Enter the new admit date ('YYYY-MM-DD'): ")
            update_query += "admit_date = %s, "
            values.append(new_admit_date)
        elif choice == 2:
            new_disease = input("Enter the new disease: ")
            update_query += "disease = %s, "
            values.append(new_disease)
        elif choice == 3:
            new_gender = input("Enter the new gender: ")
            update_query += "gender = %s, "
            values.append(new_gender)
        
        elif choice == 4:
            new_phone = input("Enter the new phone number: ")
            update_query += "phone = %s, "
            values.append(new_phone)
        elif choice == 5:
            new_address = input("Enter the new address: ")
            update_query += "address = %s, "
            values.append(new_address)
        elif choice == 6:
            new_discharge_date = input("Enter the new discharge date ('YYYY-MM-DD'): ")
            update_query += "discharge_date = %s, "
            values.append(new_discharge_date)
        else:
            print("Invalid choice.")

    update_query = update_query.rstrip(", ") + " WHERE patient_name = %s"
    values.append(patient_name)

    cursor.execute(update_query, values)
    db.commit()
    print("Patient information updated successfully.")




def get_patient_data():
    patient_id = int(input("Enter patient ID to access data: "))
    cursor.execute("SELECT * FROM patient WHERE patient_id=%s", (patient_id,))
    data = cursor.fetchone()
    if data:
        table = PrettyTable(["patient_id", "patient_name","gender","phone", "Disease", "admit_date", "discharge_date", "address", "doctor_id"])
        table.add_row(data)
        print(table)
    else:
        print("Patient not found.")



def Access_Patient_By_Admit_Date():
    admin_date = input("Enter the patient's admit date (YY-MM-DD):- ")
    cursor.execute("SELECT * FROM patient WHERE admit_date = %s", (admin_date,))
    data = cursor.fetchall()
    if data:
        table = PrettyTable(["patient_id", "patient_name","gender","phone", "Disease", "admit_date", "discharge_date", "address", "doctor_id"])
        for row in data:
            table.add_row(row)
        print(table)
    else:
        print("No person admitted on this date.")






def Access_Patient_By_Disease():
    Disease = input('Enter Disease :- ')
    cursor.execute('select * from patient where Disease=%s',(Disease,))
    data = cursor.fetchall()
    if data:
        table = PrettyTable(["patient_id", "patient_name","gender","phone","Disease", "admit_date", "discharge_date", "address", "doctor_id"])
        for row in data:
            table.add_row(row)
        print(table)
    else:
        print("No person admitted on this date.")



def show_all_patients():
    cursor.execute("SELECT patient_id,patient_name,gender,phone,Disease,admit_date,discharge_date,address,doctor_name  FROM patient p  join doctor d on p.doctor_id=d.doctor_id ")
    data = cursor.fetchall()
    if data:
        print("All Patients:")
        headers = ["patient_id", "patient_name","gender","phone", "Disease", "admit_date", "discharge_date", "address", "doctor_id"]
        display_data(data, headers)
    else:
        print("No patient records found.")



def delete_patient():
    patient_id = int(input('Enter the ID of the doctor you want to delete :- '))
    cursor.execute('delete from patient where patient_id=%s',(patient_id,))
    db.commit()
    print('patient Delete Successfully !!!')


# -________________________________________________________Patient Function End's_______________________________________________________________________________________________





# ________________________________________________________Management person Function's__________________________________________________________________________________________



def management_menu():
    print("Select an option:")
    print("1. Add new Management person")
    print("2. Update Management person")
    print("3. Show all Management person")
    print("4. Delete Management person")
    option = int(input("Enter your choice: "))
    if option == 1:
        new_management_person()
    elif option == 2:
        update_management_person()
    elif option == 3:
        show_all_management_person()
    elif option == 4:
        delete_management_person()
    else:
        print("Invalid option.")



# Function to add new management person
def new_management_person():
    name = input("Enter management person name: ")
    password = pwinput("Enter management person password: ")
    cursor.execute("INSERT INTO management_persons (management_person_name, management_person_password) VALUES (%s, %s)", (name, password))
    db.commit()
    print("New management person added successfully.")
    print("--------------------------------------")


def update_management_person():
    management_person_id = int(input('Enter management person id :- '))
    management_person_name = input("Enter management person name to update: ")
    management_person_password = input("Enter management person password name: ")
    cursor.execute("update management_persons SET  management_person_name=%s,management_person_password=%s  WHERE management_person_id=%s", (management_person_name,management_person_password,management_person_id))
    db.commit()
    print("management person data updated successfully.")


def delete_management_person():
    management_person_id = int(input('Enter management person id :- '))
    cursor.execute('delete from management_persons where management_person_id=%s',(management_person_id,))
    db.commit()
    print("Management Person Successfully Deleted !!!")



def show_all_management_person():
    cursor.execute("SELECT * FROM management_persons")
    data = cursor.fetchall()
    if data:
        print("All management person:")
        headers = ["management_person_id", "management_person_name", "management_person_password"]
        display_data(data, headers)

    else:
        print("No management person records found.")


# ________________________________________________________Management person Function's__________________________________________________________________________________________



# Main Program
def main():
    username = input("Enter Management Person Name :- ")
    password = pwinput("Enter password: ")
    while True: 
        if login(username, password):
            print("Login Successful.")
            print('Press-1 For Doctor releted information')
            print('Press-2 For Patient releted information')
            print('Press-3 For Management Person releted information')
            print('Press-4 for Exit')
            option = int(input('Enter Your choice :- '))
            if option == 1:
                doctor_menu()
            elif option == 2:
                patient_menu()
            elif option == 3:
                management_menu()
            elif option == 4:
                break
        else:
            print("Access Denied. You are not part of our management.")
            break;
main()



























