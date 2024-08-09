import pnms

class Nurse:
    id : int = 0
    name : str = ""
    assignments : int = 0

    def __init__(self,i,n):
        self.id = i
        self.name = n
        self.assignments = 3
        
    def display(self):
        print(f"* ID: {self.id}, Name: {self.name}, Remaining Assignments: {self.assignments}")

    def update_record(self):
        print(" *** Updating Nurse record")
        print("What would you like to update:\n1. Nurse Name\n2. Nurse Assignment")
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            new_name = input("Enter new name: ")
            self.name = new_name
            print("Nurse name updated successfully.")
        elif(choice == 2):
            print("What would you like to update:\n1. Remove Assignment to Particular Patient\n2. Remove All Assignments")
            choice = int(input("Enter your choice: "))
            if(choice == 1):
                print("Nurse is assigned to the following patients: ")
                for patient in pnms.patients:
                    if(patient.nurse_id == self.id):
                        patient.display()
                id = int(input("Enter Patient ID from whom you want to remove assienment: "))
                for patient in pnms.patients:
                    if(id == patient.id):
                        self.assignments += 1
                        patient.nurse_id = 0
                        print(f"Nurse unassigned to patient having ID: {patient.id}.")
                        break
            elif(choice == 2):
                for patient in pnms.patients:
                    if(self.id == patient.nurse_id):
                        patient.nurse_id = 0
                        self.assignments += 1
                print("Nurse Unassigned Successfully.")
            else:
                print("Invalid Choice!")
        else:
            print("Invalid Choice!")

    def delete_record(self):
        record_deleted = False
        print("Unassigning Nurse before deletion: ")
        for patient in pnms.patients:
            if(self.id == patient.nurse_id):
                patient.nurse_id = 0
                print(f"Nurse unassigned to patient having ID: {patient.id}.")
                record_deleted = True
        pnms.nurses[:] = [nurse for nurse in pnms.nurses if nurse != self]
        if record_deleted == False:
            print("Error! Record could not be deleted.")
        else:
            print("Record Deleted Successfully!")