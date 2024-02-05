# Created by: Chinmay Jain
# Dated: 5 February 2024

"""
Writing application software for the holidays:
reasons for holidays in [university, school, any education centre etc]
[Illness,tour,function,family issues, accidents]
"""

# Basic requirements for writting the application

user_name = str(input("Enter your name: "))

user_class = str(input("Enter your class/semester + stream(if any): "))

user_id = str(input("Enter your unique id: "))

current_date = str(input("Enter the current date: "))

last_day_of_the_leave = str(input("Enter the last day of the leave: "))

number_of_days_for_leave = str(input("Enter the number of leave days: "))

user_education_centre = str(input("Enter your education centre name: "))

authority_name = str(
    input("Enter the name of the authority of which we have to write the application: ")
)

subject = str(input("Enter subject of the application: "))

salutation = "Dear Sir/Madam"

application_type = str(
    input(
        "Please choose the application choice:\n1.Illness\n2.Function\n3.Accident\n4.Family issues\n5.Tour\n"
    )
)

# Writing the application in the file:  named "leave_application"

with open("leave_application.txt", "w") as file:

    file.write(
        f"To,\n{authority_name};\nDated: {current_date};\nSubject: {subject}.\n{salutation},\nWith due regards I want to notify you that I am {user_name}, studying in {user_class} of your {user_education_centre} I need a leave for {number_of_days_for_leave} because {subject}\nKindly grant me leave from {current_date} to {last_day_of_the_leave}. So that I can visit to required place as soon as possible.\nThanking You\nYour's sincerely\n{user_name}\nStudent ID:({user_id})"
    )
