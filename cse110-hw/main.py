"""
Autho: Ethan James Walker

Purpose: Display Text to the Screen
"""

import email
from tkinter import LAST


print("Please enter the following information:")

first_name = input("What is your First name? ")
last_name = input("what is your Last name? ")
email_address = input("what is your Email Address? ")
phone_number = input("what is your phone number? ")
job_title = input("what is your job Title? ")
Id = input("what is your ID number? ")

print("The ID Card is:")
print()
print("-"*32)
print(f"{first_name}, {last_name}")
print(f"{job_title}")
print(f"ID: {Id}")
print()
print(f"{email_address}")
print(f"{phone_number}")
print("-"*32)