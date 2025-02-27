holy this code can be really confusing at first glance but i promise its not too bad, gonna go over each class and their methods in detail
so its easy to understand (there will still be documentation in each file so its not only this), also methods are not going to be listed in
order but more about how important they are.

createJsonFile.py

createAccountJson(email, password, firstName, lastName, accountType)

This method is pretty self explanitory, creating a json file for an account.
first, the path where the files will be stored is defined, then a random file name
is created. it calls a method to get a randomly generated file name, to which the returned
string would be used as the accounts ID. then it starts to get all the data associated with
new account being made. there are two sections for account json files, "accountDetails" for
details about the current account, and "statistics" to store the personal statistics for the account.

The data stored in "account details" goes as follows

    "email" - String - The email set for the account - initialized to paramater "email"
    "password" - String - The Password set for the account - initialized to paramater "password"
    "firstName" - String - The first name set for the account - initialized to paramater "firstName"
    "lastName" - String - The last name set for the account - initialized to paramater "lastName"
    "accountType" - Int - This number determines which account type it should be. 0 - Student, 1 - Faculty, 2 - Admin - initialized to paramater "accountType"
    "ID" - String - This is set by default to be the name of the account (The random letters and numbers generated before)

The data stored in "statistics" goes as follows

    "totalQuestionsAnswered" - Int - The total numbers of questions answered on the account - initialized to 0
    "totalQuestionsCorrect" - Int - The total number of questions answered correctly on account - initialized to 0
    "totalTestsCompleted" - Int - The total number of tests completed on the account - initialized to 0
    "averageScore" - Int - The average score for all the tests taken on the account - initialized to 0

After all these ar definied and intialized, the json file is created.


createQuestionJson(title, questionText, tags, imagePath, answer1, answer2, answer3, answer4, answer5, isCorrect1, isCorrect2, isCorrect3, isCorrect4, isCorrect5):

