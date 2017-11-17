#SQL Database
import sqlite3
#For clearing terminal
import os


con = sqlite3.connect("Adressebok.db")
c = con.cursor()


#
def database_check():
    c.execute('''CREATE TABLE IF NOT EXISTS bok
             (Name, PhoneNumber, Address, Email)''')
    con.commit()

print("Adressebok, ver_0.1")


def add_n_ins():
    valg =input(
        "1. Registrering \n" +
        "2. Inspekter \n"
    )
    #Gets inputs from the user with input and commits them in adressebok.db
    if valg == "1":
        #Clear terminal
        os.system("clear")
        #Define the bok VALUES variables and prints details before
        #Asks for the inputs below
        Name = input("Navn: ")
        PhoneNumber = input("Mobilnummer: ")
        Address = input("Adresse: ")
        Email = input("Email: ")
        #Inserting the defined variables into the table
        c.execute('''INSERT INTO bok (Name, PhoneNumber, Address, Email)VALUES(?,?,?,?)''',
                 (Name, PhoneNumber, Address, Email))
        con.commit()
        input("Trykk en tast for å gå videre")
        os.system("clear")
    #Prints the adressebok.db if user inputs "2"
    elif valg == "2":
        os.system("clear")
        #Prints all content in Adressebok.db
        allcontent = c.execute('SELECT * FROM bok').fetchall()
        print(allcontent)
        input("Trykk en tast for å gå videre \n")
        os.system("clear")

#Puts the two functions together as one
def main():
    database_check()
    add_n_ins()

#Starts program anew
Running = True
while Running:
    main()
