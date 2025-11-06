#Homework - Personalized Birthday Wishes

recipient_name = str(input("What is your name? "))
year_of_birth = int(input("What is your birth year? "))
age = 2025 - year_of_birth
message = "Enjoy the day with your loved ones and collect great memories that will last forever."
sender_name = "Javier"

print(f"{recipient_name}, let's celebrate your {age} years of awesomeness! \n"
      f"Wishing you a day filled with joy and laughter as you turn {age}! \n"
      f"{message} \n"
      f"With love and best wishes, \n"
      f"{sender_name}")