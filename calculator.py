# File:    calculator.py
# Date:   9/3/2020
# Description:
#   This program calculates the Blood Alcohol Content of a person. The user is prompted to input their age, weight, gender, how many drinks they have had, and how much time has elapsed since they started drinking. Upon input, they are returned an approximate BAC.

# Constants for BAC calculation
MALE_METABOLIC_RATE = 0.68
FEMALE_METABOLIC_RATE = 0.55
# Number required to convert pounds to grams
POUNDS_TO_GRAMS = 454
# Standard US average of alcohol content in 1 drink, measured in grams
GRAMS_OF_ALCOHOL_PER_DRINK = 14
LEGAL_BAC_LIMIT = 0.08
RATE_OF_BAC_DECAY = 0.015
QUIT = "q"

def main():

  print("Welcome to the BoozeBot 3000! I'm here to calculate your Blood Alcohol Content. To properly calculate your BAC, I'll need information from you. ")

# Prompt user for gender so that the loop can begin
  gender = input("\n Are you male or female? Please enter M for male or F for female, or q to quit: ")

  while gender != QUIT:

    alcoholConsumed = int(input("\n Enter the number of drinks you've had: "))
    weight = int(input("\n Enter your weight in pounds: "))
    elapsedTime = int(input("\n Enter the number of hours that you have been drinking: "))

    weight = weight * POUNDS_TO_GRAMS # Convert weight to grams

    # Set the appropriate metabolic rate based upon gender
    if gender == "M" or gender == "m":
      weight = weight * MALE_METABOLIC_RATE
    elif gender == "F" or gender == "f":
      weight = weight * FEMALE_METABOLIC_RATE

    alcoholConsumed = alcoholConsumed * GRAMS_OF_ALCOHOL_PER_DRINK # Convert drinks to measure pure alcohol in grams

    bloodAlcohol = alcoholConsumed / weight # calculate raw BAC
    bloodAlcohol = bloodAlcohol * 100 # convert blood alcohol from raw number to a percentage
    bloodAlcohol = float(bloodAlcohol - (elapsedTime * RATE_OF_BAC_DECAY)) # account for drop in BAC based on time elapsed

    print("\n Your approximate Blood Alcohol Content is: " + str(bloodAlcohol))

    if bloodAlcohol > LEGAL_BAC_LIMIT:
      print("\n You should not drive. \n")
    elif (bloodAlcohol > 0 ) and (bloodAlcohol< LEGAL_BAC_LIMIT):
      print("\n You still shouldn't drive, but it's not illegal. \n")

    gender = input("If you'd like to continue, enter the gender of the next person, or enter \"q\" to quit: ") # get input on gender again to continue the loop, or exit the loop and quit

  print("\n Thanks for using the BoozeBot 3000, be safe out there!")

main()

exit