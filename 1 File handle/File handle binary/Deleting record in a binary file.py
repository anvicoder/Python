import pickle

def bdelete():
    # Opening the file in binary read mode and loading the data
    with open("studrec.dat", "rb") as F:
        stud = pickle.load(F)
        print(stud)

    # Deleting the Roll no. entered by user
    rno = int(input("Enter the Roll no. to be deleted: "))
    rec = [i for i in stud if i[0] != rno]
    
    # Writing the updated data back to the file in binary write mode
    with open("studrec.dat", "wb") as F:
        pickle.dump(rec, F)

bdelete()

