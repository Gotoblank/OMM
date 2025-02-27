USE omm;

-- users table
CREATE TABLE IF NOT EXISTS users (
	users_ID int NOT NULL AUTO_INCREMENT,
    dtype VARCHAR(25),
    first_name VARCHAR(25) DEFAULT NULL,
    last_name VARCHAR(25) DEFAULT NULL,
    email VARCHAR(50) DEFAULT NULL,
    pass VARCHAR(255) DEFAULT NULL,
    last_login DATE DEFAULT NULL,
    PRIMARY KEY (users_ID)
    );
    
-- student table
CREATE TABLE IF NOT EXISTS student (
	users_ID int NOT NULL,
    PRIMARY KEY (users_ID),
	CONSTRAINT fk_student_users FOREIGN KEY (users_ID) REFERENCES users 
    (users_ID) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
-- faculty table
 CREATE TABLE IF NOT EXISTS faculty (
	users_ID int NOT NULL,
    PRIMARY KEY (users_ID),
	CONSTRAINT fk_faculty_users FOREIGN KEY (users_ID) REFERENCES users 
    (users_ID) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
-- test table
CREATE TABLE IF NOT EXISTS test (
	test_ID int NOT NULL AUTO_INCREMENT,
    users_ID int DEFAULT NULL,
	test_name varchar(50),
	is_tutor_mode BOOLEAN,
	is_time_mode BOOLEAN,
    create_date DATE,
    time_limit INT,
    PRIMARY KEY (test_ID),
    CONSTRAINT fk_test_student FOREIGN KEY (users_ID) REFERENCES student
    (users_ID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- question table
CREATE TABLE IF NOT EXISTS question (
	question_ID int NOT NULL AUTO_INCREMENT,
    users_ID int DEFAULT NULL,
    question_text MEDIUMTEXT,
    example_text MEDIUMTEXT,
    is_active BOOLEAN,
    PRIMARY KEY (question_ID),
    CONSTRAINT fk_quesiton_faculty FOREIGN KEY (users_ID) REFERENCES faculty
    (users_ID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- answer 
CREATE TABLE IF NOT EXISTS answer (
	answer_ID int NOT NULL AUTO_INCREMENT,
    answer_text VARCHAR(150),
    PRIMARY KEY (answer_ID)
    );
  
-- question and answer bridge table
CREATE TABLE IF NOT EXISTS question_answer (
	question_answer_ID int NOT NULL AUTO_INCREMENT,
    question_ID int DEFAULT NULL,
    answer_ID int DEFAULT NULL,
    is_correct BOOLEAN,
    PRIMARY KEY (question_answer_id),
    CONSTRAINT fk_question_answer_question FOREIGN KEY (question_ID) REFERENCES question
    (question_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_question_answer_answer FOREIGN KEY (answer_ID) REFERENCES answer
    (answer_ID) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
-- test and question bridge table
CREATE TABLE IF NOT EXISTS test_question (
	test_question_id int NOT NULL AUTO_INCREMENT,
    test_id int,
    question_id int,
	question_number int,
    PRIMARY KEY (test_question_id),
    CONSTRAINT fk_test_question_test FOREIGN KEY (test_ID) REFERENCES test
    (test_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_test_question_question FOREIGN KEY (question_ID) REFERENCES question
    (question_ID) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- attempt table
CREATE TABLE IF NOT EXISTS attempt (
	attempt_id int NOT NULL AUTO_INCREMENT,
    users_id int,
    test_id int,
    score FLOAT,
    attempt_date DATE,
    is_complete BOOLEAN,
    time_taken INT,
	attempt_number int,
    PRIMARY KEY (attempt_id),
    CONSTRAINT attempt_student FOREIGN KEY (users_id) REFERENCES student
    (users_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT attempt_test FOREIGN KEY (test_id) REFERENCES test
    (test_id) ON DELETE CASCADE ON UPDATE CASCADE
	);
   
-- attempt answer table
CREATE TABLE IF NOT EXISTS attempt_answer (
	attempt_answer_id int NOT NULL AUTO_INCREMENT,
	attempt_id int,
	question_id int,
	answer_id int,
	is_correct BOOLEAN,
	question_number int,
	PRIMARY KEY (attempt_answer_id),
	CONSTRAINT attempt_answer_attempt FOREIGN KEY (attempt_id) REFERENCES attempt
    (attempt_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT attempt_answer_question FOREIGN KEY (question_id) REFERENCES question
    (question_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT attempt_answer_answer FOREIGN KEY (answer_id) REFERENCES answer
    (answer_id) ON DELETE CASCADE ON UPDATE CASCADE
	);
        
-- edits question table bridges faculty and question
CREATE TABLE IF NOT EXISTS edits_question (
	edits_question_id int NOT NULL AUTO_INCREMENT,
	users_id int,
	question_id int,
	PRIMARY KEY (edits_question_id),
	CONSTRAINT edits_question_faculty FOREIGN KEY (users_id) REFERENCES faculty
	(users_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT edits_question_question FOREIGN KEY (question_id) REFERENCES question
	(question_id) ON DELETE CASCADE ON UPDATE CASCADE
	);
        
-- flagged table bridges student and question
CREATE TABLE IF NOT EXISTS flagged_question (
	flagged_question_id int NOT NULL AUTO_INCREMENT,
	users_id int,
	question_id int,
	PRIMARY KEY (flagged_question_id),
	CONSTRAINT flagged_question_student FOREIGN KEY (users_id) REFERENCES student
	(users_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT flagged_question_question FOREIGN KEY (question_id) REFERENCES question
	(question_id) ON DELETE CASCADE ON UPDATE CASCADE
	);

CREATE TABLE tag (
  tag_ID int NOT NULL AUTO_INCREMENT,
  dtype varchar(25) DEFAULT NULL,
  tag_name varchar(75) DEFAULT NULL,
  PRIMARY KEY (tag_ID)
);

CREATE TABLE tag_question (
  tag_question_ID int NOT NULL AUTO_INCREMENT,
  tag_ID int DEFAULT NULL,
  question_ID int DEFAULT NULL,
  PRIMARY KEY (tag_question_ID),
  CONSTRAINT fk_tag_question_question FOREIGN KEY (question_ID) REFERENCES question (question_ID) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_tag_question_tag FOREIGN KEY (tag_ID) REFERENCES tag (tag_ID) ON DELETE CASCADE ON UPDATE CASCADE
);