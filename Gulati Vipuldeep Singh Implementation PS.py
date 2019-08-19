#Vipuldeep Singh Gulati
#jc497971
import random                                  #to use random function in the code
def main():
    welCome = validateUsername("Welcome to the Calorie Intake Assistant, my name is Cal. What is your name?")
    ynConsent = getPersonalinformation(welCome)
    if ynConsent.upper() == "Y":               #upper() converts user input into capital letter
        print("Great username, let’s start! What is your gender? Enter M for male or F for female")
        mfGender = getGender()
        ageFactor = validateNumber("What is your age in years?")
        weightFactor = validateNumber("What is your current weight in Kg")
        heightFactor = validateNumber("What is your height in cm")
        RDCI = getRdcicalculator(mfGender, weightFactor, heightFactor, ageFactor)
        ADCI = getCaloriecount(RDCI)
        finalResult = round(ADCI / RDCI) * 100
        considerFeedback(finalResult, welCome)
        print("Goodbye and good luck!")
    else:
        print("That's alright, goodbye", welCome)

def validateUsername(prompt):
    #This function is used to validate whether the name of the user is not null and all the charachters in a string (name) are alphabets
    name = input(prompt)
    while len(name) < 1 or (name.isalpha() != True):
        if len(name) < 1:             #len(name) will check whether the length of the name is not less than 1, if it is incase then askagainMessage will be shown
            askagainMessage = "Don't be shy. Please enter your name."
        elif name.isalpha() != True:  #isalpha() is used to check whether all the charachters/alphabets in a string are alphabets or not
            askagainMessage = "It is unlikely your name is " + name + "! Please enter your name."
        name = input(askagainMessage)
    return name

def getPersonalinformation(welcome):
    #getPersonalinformation function ask for consent of the user to further move forward with the assistance.
    #The answer is returned.
    print("Hi", welcome, "! To properly assist you, we will need some personal information such as age, gender, weight and height. Do you want to continue? Enter Y for yes or N for no.")
    answer = input()
    while answer.upper() not in ["N", "Y"]:
        answer = input("I am sorry, I cannot understand. To properly assist you, we will need some personal information such as age, gender, weight and height. Do you want to continue? Enter Y for yes or N for no.")
    return answer.upper()

def getGender():
    #gets "m" or "f" as input from the user and validates till the input is correct
    #returns gender
    gender = input()
    while gender.upper() not in ["M", "F"]:                #upper() function is used to take input "m" or "f" and convert it in capital letters if it is in small letters
        gender = input("I'm sorry, I cannot understand. What is your gender? Enter M for male or F for female")
    return gender.upper()

def validateNumber(prompt):
    #validateNumber validates for ageFactor, weightFactor, heightFactor
    #doesn't returns the value till it is coorect.
    value = input(prompt)
    while len(value) == 0 or (float(value) <= 0):
        if len(value) == 0:
            print("I'm sorry, I cannot understand. Please enter again.")
        elif float(value) <= 0:
            print("I'm sorry, I cannot understand. Please enter positive number.")
    return float(value)

def getRdcicalculator(mfGender, weightFactor, heightFactor, ageFactor):
    #getRdcicalculator takes mfGender, weightFactor, heightFactor, ageFactor as parameters
    # and calculates rdci and returns rDci
    if mfGender == "M":
        rDci = (10*weightFactor)+(6.25*heightFactor)-(5*ageFactor)+5        #Miffin - St Jeor Formula for caluclating rdci for men.
    else:
        rDci = (10*weightFactor)+(6.25*heightFactor)-(5*ageFactor)-161      #Miffin - St Jeor Formula for caluclating rdci for women.
    return rDci

def getCaloriecount(RDCI):
    #getCaloriecount takes RDCI as parameter
    #asks user for their intake 7 times, generates random temptations, shows result with and without temptations for 7 days
    #calculates adci and returns aDci
    print(" ")                                             #Just used to make running of code more readable.
    totalCalCulation = 0
    for dayNo in range(1, 8):                              #for loop used because I now it will run for 7 days (definite loop)
        calCulation = 0
        option = input("Day" + str(dayNo) + ": Were your meals (1) very unhealthy,(2) unhealthy,(3) healthy, or (4) very healthy? Enter the corresponding number")
        while option not in ["1", "2", "3", "4"]:
            option = input("Please enter valid number")    #Will ask again if the user puts other options than "1","2","3","4"
        if (option == "1"):
            calCulation = RDCI * 1.5
        elif (option == "2"):
            calCulation = RDCI * 1.2
        elif (option == "3"):
            calCulation = RDCI
        elif (option == "4"):
            calCulation = RDCI * 0.8
        hasTemptation = random.randint(0, 1)              #random will generate random number between 0 or 1 every time it runs loop. If 0 then it will directly show result without temptations
        if (hasTemptation == 1):
            randTemptation = random.randrange(7)          #random.randrange returns a randomly selected element from range 1 to 7.
            temptationItems = ["chocolate", "chips", "ice-cream", "fast-food", "fizzy drink", "party cake", "popcorn"]
            temptation = temptationItems[randTemptation]  #tempatationItem will be known by the index, which item it is.
            if temptation == "chocolate":                 # calorievalue accordingly to the item will be added.
                calorieValue = 250
            elif temptation == "chips":
                calorieValue = 550
            elif temptation == "ice-cream":
                calorieValue = 207
            elif temptation == "fast-food":
                calorieValue = 350
            elif temptation == "fizzy drink":
                calorieValue = 180
            elif temptation == "party cake":
                calorieValue = 257
            elif temptation == "popcorn":
                calorieValue = 375
            print(calCulation, "calories for day", dayNo, ". Also , it looks like this day you've been tempted with", temptation, "and", calorieValue, "is added")
            print(" ")                                     #Just used to make running of code more readable.
            calCulation = calCulation + calorieValue       #calorie value according to the temptation is added.
        else:
            print(calCulation, "calories for day", dayNo, ".")  #if temptation is 0 this result will be displayed which is without temptation
            print(" ")                                     #Just used to make running of code more readable.
        totalCalCulation = totalCalCulation + calCulation
    aDci= round(totalCalCulation/7)                               #adci is calculated and round function is used to round off the value that will be obtained.
    print("During the last 7 days you had an intake of", totalCalCulation, "calories, meaning a daily average of", aDci, "calories")  #this will display total calories and adci
    return aDci

def considerFeedback(finalResult, welCome):
                                                           #considerFeedback function will provide feedback to the user on the basis of finalResult that is calculated.
    print(" ")                                             #Just used to make running of code more readable.
    print("Thank you,", welCome, "! I’m computing your results…")
    if finalResult < 90:
        print(welCome, ", your daily calorie intake is lower than the recommended with", 100 - finalResult, "%.")
        print("This rhythm will make you lose weight, just make sure your meals contain all nutritional value needed.")
        print("It’s recommended that you do not fall under the healthy weight and that you keep a balanced lifestyle.")
    elif(finalResult >= 90) and (finalResult <= 110):
        print(welCome, ", your daily calorie intake is close to the recommended one!")
        print("You have a balanced healthy lifestyle,")
        print("well done!")
    else:
        print(welCome, ", your daily calorie intake is higher than the recommended with", finalResult - 100, "%.")
        print("This rhythm will make you gain weight which will lead to health concerns.")
        print("It’s recommended that you either lower your calorie intake, either exercise more!")
        print("Careful with those temptations!")

main()