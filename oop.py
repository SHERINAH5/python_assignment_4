# #object oriented progamming 
# #it always has classes and objects
# # a class always has propertise/attributes
# #an object takes on the properties of a class

# #syntaxs#1. creating classes
# #cohort class
#classes start with upper case
# class Cohort:
#     name
#     description
#     start_date
#     end_date
#     total_students
#add a constructor foe the cohort class.(read about constructors)
class Cohort:
    def __init__( self, name, description, start_date, end_date, total_students):
        self.name = name
        self.description = description
        self.start_date =start_date
        self.end_date = end_date
        self.total_students = total_students

        #add a method to the class that prints the cohort name, and the total number of students
    def print_cohort_info(self):
        print(f"Cohort Name:{self.name}") 
        print(f"Total Students:{self.total_students}")

        #create a new instaance of the cohort class'
        my_cohort = Cohort( name="Cohort4", description= "Has got the biggest number of students",start_date= "20-08-2024", end_date="20-06-2026", total_students=55) 

        my_cohort.print_cohort_info( )
    
