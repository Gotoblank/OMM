import json
import os
from pathlib import Path

def findHighestFileNum(filePath, file): #this is specifically for question files
    num = 1
    newestFile = None
    searching = True
    
    while searching: #This while loop searches for the most recent iteration of a file by looking at the '-#' at the end of each file and returns the one with the highest one
        currentFile = str(file) + "-" + str(num) + ".json"
        if currentFile in os.listdir(filePath):
            newestFile = currentFile
            num += 1
        else:
            searching = False
    return newestFile

def editAllJson(): #method for editing all files if needed, currently unused
    filePath = Path('main-omm/database/Code/accounts')
    for file in os.listdir(filePath):
        fullPath = filePath / file
        with open(fullPath, 'r') as f:
            data = json.load(f)
            #if needed to edit all for whatever reason

        with open(fullPath, 'w') as f:
            json.dump(data, f, indent=4)  # Save the updated data back to the file

def editJsonAccountDetails(fileName, newEmail, newPassword, newFirstName, newLastName, newAccountType):
    filePath = Path('main-omm/database/Code/accounts')
    fileName = filePath / f"{fileName}.json"


    if not os.path.exists(fileName):
        print("File does not exist")
    else:

        with open(fileName, 'r') as f:
            data = json.load(f)
            if newEmail != None:
                data['accountDetails']['email'] = newEmail  #Set new email if needed
            if newPassword != None:
                data['accountDetails']['password'] = newPassword  #Set new password if needed
            if newFirstName != None:
                data['accountDetails']['firstName'] = newFirstName  #Set new first name if needed
            if newLastName != None:
                data['accountDetails']['lastName'] = newLastName  #Set new last name if needed
            if newAccountType != None:
                data['accountDetails']['accountType'] = newAccountType  #Set new account type if needed

        with open(fileName, 'w') as f:
            json.dump(data, f, indent=4)  #Save the updated data back to the file

def editJsonAccountStatistics(fileName, newTotalQuestionsAnswered, newTotalQuestionsCorrect, newTotalTestsCompleted, newAverageScore):
    filePath = Path('main-omm/database/Code/accounts')
    fileName = filePath / f"{fileName}.json"

    if not os.path.exists(fileName):
        print("File does not exist")

    else:
        with open(fileName, 'r') as f:
            data = json.load(f)
            if newTotalQuestionsAnswered != None:
                data['statistics']['totalQuestionsAnswered'] = newTotalQuestionsAnswered  #Set new amount of questions answered
            if newTotalQuestionsCorrect != None:
                data['statistics']['totalQuestionsCorrect'] = newTotalQuestionsCorrect  #Set new amount of questions answered correctly
            if newTotalTestsCompleted != None:
                data['statistics']['totalTestsCompleted'] = newTotalTestsCompleted  #Set new amount of total tests completed
            if newAverageScore != None:
                data['statistics']['averageScore'] = newAverageScore  #Update average score

        with open(fileName, 'w') as f:
            json.dump(data, f, indent=4)  # Save the updated data back to the file

def editJsonQuestion(fileName, newTitle, newQuestionText, newTags, newImagePath, allowImagePath, newAnswerOneText, newAnswerTwoText, newAnswerThreeText, allowAnswerThree, newAnswerFourText, allowAnswerFour, newAnswerFiveText, allowAnswerFive, newIsCorrect):
    filePath = Path('main-omm/database/Code/questions')
    baseFile = filePath / f"{fileName}-1.json"

    if not os.path.exists(baseFile): #make sure one file exists atleast
        print("File does not exist")

    else:
        fileName = findHighestFileNum(filePath, fileName) #find most recent version
        print(fileName + " is most recent")
        with open(filePath / fileName, 'r') as f:
            data = json.load(f)

            if newTitle != None:
                data['questionDetails']['title'] = newTitle  #Sets new question title if needed
            if newQuestionText != None:
                data['questionDetails']['questionText'] = newQuestionText  #Sets new question text if needed
            if newTags != None:
                data['questionDetails']['tags'] = newTags  #Sets new tags if needed
            if data['questionDetails']['imagePath'] == None and allowImagePath: #if image doesnt exist but you want to add one
                data['questionDetails']['imagePath'] = newImagePath  
            elif data['questionDetails']['imagePath'] != None and not allowImagePath: #if image exists but want to remove it
                data['questionDetails']['imagePath'] = None 
            elif data['questionDetails']['imagePath'] != None and allowImagePath: # if image exists but want to update it
                data['questionDetails']['imagePath'] = newImagePath

            data['questionDetails']['questionVersion'] += 1  #Question is being updated, so add 1 to question version

            if newAnswerOneText != None:
                data['answers']['answerOneText'] = newAnswerOneText  # Edit the 'answerOneText' field
            if newAnswerTwoText != None:
                data['answers']['answerTwoText'] = newAnswerTwoText  # Edit the 'answerOneTwo' field

            if data['answers']['answerThreeText'] == None and allowAnswerThree: #Same as image but instead for answer 3
                data['answers']['answerThreeText'] = newAnswerThreeText  
            elif data['answers']['answerThreeText'] != None and not allowAnswerThree:
                data['answers']['answerThreeText'] = None 
            elif data['answers']['answerThreeText'] != None and allowAnswerThree:
                data['answers']['answerThreeText'] = newAnswerThreeText

            if data['answers']['answerFourText'] == None and allowAnswerFour: #Same as image but instead for answer 4
                data['answers']['answerFourText'] = newAnswerFourText
            elif data['answers']['answerFourText'] != None and not allowAnswerFour:
                data['answers']['answerFourText'] = None 
            elif data['answers']['answerFourText'] != None and allowAnswerFour:
                data['answers']['answerFourText'] = newAnswerFourText

            if data['answers']['answerFiveText'] == None and allowAnswerFive: #Same as image but instead for answer 5
                data['answers']['answerFiveText'] = newAnswerFiveText 
            elif data['answers']['answerFiveText'] != None and not allowAnswerFive:
                data['answers']['answerFiveText'] = None
            elif data['answers']['answerFiveText'] != None and allowAnswerFour:
                data['answers']['answerFiveText'] = newAnswerFiveText

            if newIsCorrect != None:
                data['answers']['isCorrect'] = newIsCorrect  #Edit which answers are correct

            newFileName = fileName[:-6] + str(data['questionDetails']['questionVersion']) + ".json"

        with open(filePath / newFileName, 'w') as f:
            json.dump(data, f, indent=4)  # Save the updated data back to the file

def editJsonQuestionStatistics(fileName, newTotalTimesAnswered, newTotalTimesAnsweredCorrect, newTotalTimeSpentOnQuestion):

    filePath = Path('main-omm/database/Code/questions')
    baseFile = filePath / f"{fileName}-1.json"

    if not os.path.exists(baseFile): #make sure one file exists atleast
        print("File does not exist")

    else:
        fileName = findHighestFileNum(filePath, fileName) #find most recent version
        print(fileName + " is most recent")
        with open(filePath / fileName, 'r') as f:
            data = json.load(f)
        
            if newTotalTimesAnswered != None:
                data['statistics']['totalTimesAnswered'] = newTotalTimesAnswered  #Update total times question has been answered
            if newTotalTimesAnsweredCorrect != None:
                data['statistics']['totalTimesAnsweredCorrect'] = newTotalTimesAnsweredCorrect  #Update total times question has been correctly answered
            if newTotalTimeSpentOnQuestion != None:
                data['statistics']['totalTimeSpentOnQuestion'] = newTotalTimeSpentOnQuestion  #Update total time spent on question

        with open(filePath / fileName, 'w') as f:
            json.dump(data, f, indent=4)  # Save the updated data back to the file
