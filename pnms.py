import Patients
import Nurses

patients : list = []
nurses : list = []

## [id, patientid, nurseid]
## create a separate environment and install the package in it
## activate the env and run your app there
## use enum for any static/hardcoded string/digit

def checking_id(id, array_selection):
    if array_selection == 1:
        # Patient Array
        for patient in patients:
            if int(patient.id) == id:
                print("\nPatient Id Already Exists! Enter Again.")
                return False
    else:
        # Nurse Array
        for nurse in nurses:
            if int(nurse.id) == id:
                print("Nurse Id Already Exists! Enter Again.")
                print("")
                return False
    return True

def id_validation(id,array_selection):
    valid_id = id
    is_valid = False
    while not is_valid:
        if all(c.isdigit() for c in valid_id):
            valid_id = int(valid_id)
            is_valid = checking_id(valid_id,array_selection)
            if(not is_valid):
                valid_id = input("\nEnter New ID: ")
        else:
            print("\nInvalid Id! Enter only numbers.")
            valid_id = input("\nEnter New ID: ")
    return valid_id

def validate_name(name):
    valid_name = name
    is_valid = False
    while not is_valid:
        if all(c.isalpha() or c.isspace() for c in valid_name):
            is_valid = True
        else:
            print("\nInvalid Name! Enter only alphabets.")
            valid_name = input("Enter Name Again: ")
    return valid_name


def register_patient():
    print("\n*** Patient Registration ***")
    id = input("Enter ID: ")
    id = id_validation(id,1)
    name = input("Enter Name: ")
    name = validate_name(name)
    patients.append(Patients.Patient(id,name))
    print("Patient Registered Successfully.")

def register_nurse():
    print("\n*** Nurse Registration ***")
    id = input("Enter ID: ")
    id = id_validation(id,2)
    name = input("Enter Name: ")
    name = validate_name(name)
    nurses.append(Nurses.Nurse(id,name))
    print("Nurse Registered Successfully.")

def display_records():
    print("\n*** Displaying Records ***")
    print("\nFollowing are the records regarding patients:")
    for patient in patients:
        patient.display()
    print("\nFollowing are the records regarding nurses: ")
    for nurse in nurses:
        nurse.display()

def patient_nurse_assignment():
    assignment_confirmed = False
    print("\n*** Patient/Nurse Registration ***")
    print("Following are the nurses that can be assigned:")
    for nurse in  nurses:
        if(nurse.assignments != 0):
            print(f"* ID: {nurse.id}, Name: {nurse.name}, Remaining Assignments: {nurse.assignments}")
    print("Following are the patients whom no nurse is assigned:")
    for patient in patients:
        if(patient.nurse_id == 0):
            print(f"* ID: {patient.id}, Name: {patient.name}, Nurse ID: Not Assigned")
    p_id = int(input("\nEnter Patient ID whom nurse will be assigned: "))
    for patient in patients:
        if(p_id == patient.id):
            n_id = int(input("\nEnter Nurse ID you want to assign: "))
            for nurse in nurses:
                if(n_id == nurse.id):
                    nurse.assignments -= 1
                    patient.nurse_id = nurse.id
                    print("Assignment Successful!")
                    assignment_confirmed = True
                    break
            break
    if assignment_confirmed == False:
        print("Error! Assignment Unsuccessful.")


def update_records():
    print("\n*** Update Record ***")
    print("\nWhose record would you like to update: ")
    print("1. Patient\n2. Nurse")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        id = int(input("Enter Patient ID you want to update: "))
        for patient in patients:
            if(id == patient.id):
                patient.update_record()
                break
    elif(choice == 2):
        id = int(input("Enter Nurse ID you want to update: "))
        for nurse in nurses:
            if(id == nurse.id):
                nurse.update_record()
                break
    else:
        print("Invalid Choice!")

def delete_records():
    print("\n*** Delete Record ***")
    print("\nWhich record would you like to delete: ")
    print("1. Patient\n2. Nurse")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        id = int(input("Enter Patient ID you want to delete: "))
        for patient in patients:
            if(id == patient.id):
                patient.delete_record()
                break
    elif(choice == 2):
        id = int(input("Enter Nurse ID you want to delete: "))
        for nurse in nurses:
            if(id == nurse.id):
                nurse.delete_record()
                break
    else:
        print("Invalid Choice!")


def main():
    print("*** Patient/Nurse Management System ***")
    choice = "0"
    
    while choice != "7":
        print()
        print("1. Register Patient")
        print("2. Register Nurse")
        print("3. Assign Nurse to Patient")
        print("4. View Records")
        print("5. Update Records")
        print("6. Delete Records")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_patient()
        elif choice == "2":
            register_nurse()
        elif choice == "3":
            patient_nurse_assignment()
        elif choice == "4":
            display_records()
        elif choice == "5":
            update_records()
        elif choice == "6":
            delete_records()
        elif choice == "7":
            print("Exiting!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()