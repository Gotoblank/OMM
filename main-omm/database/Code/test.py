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
                        "YTJZ4L1OQ3",
                        "NewTestingEmail@gmail.com",
                        "newTestPassword",
                        "new First Name",
                        "Last Name Test",
                        2
                        )

editJsonFile.editJsonAccountStatistics(
                        "YTJZ4L1OQ3",
                        5,
                        3,
                        2,
                        80)

editJsonFile.editJsonQuestion(
                        "4RRB9BFVLS",
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
                        [False, True, False, False, None]
                        )

editJsonFile.editJsonQuestionStatistics(
                        "4RRB9BFVLS",
                        2,
                        1,
                        10
                        )