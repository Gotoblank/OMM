import createJsonFile
import editJsonFile


#Calling function to create filename
createJsonFile.createAccountJson(
                        "test@gmail.com",
                        "password",
                        "testing",
                        "testerton",
                        3
                        )


createJsonFile.createQuestionJson(
                        "Simple Math", #title
                        "What is 2+2", #question text
                        ["Math", "Simple", "Test Tag"], #tags
                        None, #image path (if exists)
                        "3", #answer text 1
                        "22", #answer text 2
                        "4", #answer text 3
                        "15", #answer text 4
                        "2", #answer text 5
                        False, #is answer 1 correct
                        False, #is answer 2 correct
                        True, #is answer 3 correct
                        False, #is answer 4 correct
                        False, #is answer 5 correct
                        )

createJsonFile.createQuestionJson(
                        "Test Question", #title
                        "True or False: Is Water Wet?", #question text
                        ["The Truth"], #tags
                        None, #image path (if exists)
                        "True", #answer text 1
                        "False", #answer text 2
                        None, #answer text 3
                        None, #answer text 4
                        None, #answer text 5
                        False, #is answer 1 correct
                        True, #is answer 2 correct
                        None, #is answer 3 correct
                        None, #is answer 4 correct
                        None, #is answer 5 correct
                        )

editJsonFile.editJsonAccountDetails(
                        "N8JWPZAO83",
                        "TestingEmail@gmail.com",
                        "newTestPassword",
                        "new First Name",
                        "Last Name Test",
                        2
                        )

editJsonFile.editJsonAccountStatistics(
                        "N8JWPZAO83",
                        5,
                        3,
                        2,
                        80)

editJsonFile.editJsonQuestion(
                        "P5H7RX1JNP",
                        None,
                        "What is 6 + 4?",
                        None,
                        None,
                        False,
                        "15",
                        "10",
                        "46",
                        True,
                        "18",
                        True,
                        None,
                        False,
                        [False, True, False, False, None],
                        2,
                        1,
                        10
                        )