import pnms

class Patient:
    id : int = 0
    name : str = ""
    nurse_id : int = 0

    def __init__(self,i,n):
        self.id = i
        self.name = n
        self.nurse_id = 0
    
    def display(self):
        if(self.nurse_id == 0):
            print(f"* ID: {self.id}, Name: {self.name}, Nurse ID: Not Assigned")
        else:
            print(f"* ID: {self.id}, Name: {self.name}, Nurse ID: {self.nurse_id}")
    
    def update_record(self):
        print(" *** Updating Patient record")
        print("What would you like to update:\n1. Patient Name\n2. Assigned Nurse")
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            new_name = input("Enter new name: ")
            self.name = new_name
            print("Patient name updated successfully.")
        elif(choice == 2):
            print("What would you like to update:\n1. Assign Another Nurse\n2. Remove Current Assigned Nurse")
            choice = int(input("Enter your choice: "))
            if(choice == 1):
                print("Following are the nurses which can be replaced: ")
                for nurse in pnms.nurses:
                    if(nurse.id != self.nurse_id):
                        nurse.display()
                    else:
                        nurse.assignments += 1
                id = int(input("Enter Nurse ID which you would like to assign: "))
                for nurse in pnms.nurses:
                    if(id == nurse.id):
                        self.nurse_id = id
                        nurse.assignments -= 1
                        print("New Nurse Assigned Successfully.")
                        break
            elif(choice == 2):
                for nurse in pnms.nurses:
                    if(self.nurse_id == nurse.id):
                        self.nurse_id = 0
                        nurse.assignments += 1
                        print("Nurse Unassigned Successfully.")
                        break
            else:
                print("Invalid Choice!")
        else:
            print("Invalid Choice!")
    
    def delete_record(self):
        record_deleted = False
        for nurse in pnms.nurses:
            if(self.nurse_id == nurse.id):
                nurse.assignments += 1
                print("Nurse unassigned before deletion.")
                pnms.patients[:] = [patient for patient in pnms.patients if patient != self]
                print("Record Deleted Successfully!")
                record_deleted = True
                break
        if record_deleted == False:
            print("Error! Record could not be deleted!")