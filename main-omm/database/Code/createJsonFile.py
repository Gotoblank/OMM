# SWE Team 6:
# Joseph
# File: createJsonFile.py
# Purpose: To create any json files relating towards questions or accounts
# Last edited: 02/24/2025
import json
import secrets
import string
from pathlib import Path

def generateRandomFileName(length, path, isQuestionFile): #Generates a random file name to not allow duplicates
    alphabet = string.ascii_uppercase + string.digits #What should be in alphabet

    searching = True    
    while searching == True: #This while loop keeps looping until it finds a unique file name
        if isQuestionFile:
            fileName = ''.join(secrets.choice(alphabet) for i in range(length)) + "-1.json"
        else: 
            fileName = ''.join(secrets.choice(alphabet) for i in range(length)) + ".json"
        if not (path / fileName).exists():
            searching = False
        else: 
            print("dup file name")
    return fileName

def createFile(data, folderPath, fileName): #Creating actual .json file
    file = json.dumps(data, indent=4)
    
    with open(folderPath / fileName, "w") as outfile:
        outfile.write(file)

def createAccountJson(email, password, firstName, lastName, accountType):

    path = Path('main-omm/database/Code/accounts') #Should be filepath to where accounts are stored
    fileName = generateRandomFileName(10, path, False) #creates filename
    ID = fileName[:-5] #creates ID based on substring of filename (removes .json)

    data = {

        "accountDetails": { #This section stores all of the account details for said account
                "email": email, #email associated with account
                "password": password, #password associated with account
                "firstName": firstName, #first name of user
                "lastName": lastName, #last name of user
                "accountType": accountType, #account type
                "ID" : ID #ID is randomly generated, same as file name
        },

        "statistics": #This section stores all of the account statistics
            {
                "totalQuestionsAnswered": 0, #should start at 0 but would be modified later
                "totalQuestionsCorrect": 0,
                "totalTestsCompleted": 0,
                "averageScore": 0

                #category questions, body region questions, treatment technique question
            }
    }
    createFile(data, path, fileName)

def createQuestionJson(title, questionText, tags, imagePath, answer1, answer2, answer3, answer4, answer5, isCorrect1, isCorrect2, isCorrect3, isCorrect4, isCorrect5):

    path = Path('main-omm/database/Code/questions') #Should be filepath to where questions are stored
    fileName = generateRandomFileName(10, path, True) #creates filename
    ID = fileName[:-7] #creates ID based on substring of filename (removes .json)

    if answer3 == None: #extra protection to make sure nothing can be messed up, might be removed later and moved somewhere else
            isCorrect3 = None
    if answer4 == None:
            isCorrect4 = None
    if answer5 == None:
            isCorrect5 = None

    data = {

        "questionDetails": { #This stores all the details for the questions
                "title": title, #Qustion title
                "questionText": questionText, #The question text (actual question for students to answer)
                "tags": tags, #Tags for the question
                "ID": ID, #ID is randomly generated, same as file name
                "questionVersion": 1, #Question version
                "imagePath": imagePath, #Path for image if exists
        },
        
        "answers": #This stores the data for the answers
            {
                "answerOneText": answer1, #Answer 1
                "answerTwoText": answer2, #Answer 2
                "answerThreeText": answer3, #Answer 3
                "answerFourText": answer4, #Answer 4
                "answerFiveText": answer5, #Answer 5
                "isCorrect": [isCorrect1, isCorrect2, isCorrect3, isCorrect4, isCorrect5] #True or false for each question (Leftmost is answer 1 rightmost is answer 5)
            },

        "statistics": #Stores all of the data for the specific question's statistics
            {
                "totalTimesAnswered": 0, #should start at 0 but would be modified later
                "totalTimesAnsweredCorrect": 0,
                "totalTimeSpentOnQuestion": 0
            }
    }           #Average per answer choice, 

    createFile(data, path, fileName)