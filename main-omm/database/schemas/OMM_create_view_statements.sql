CREATE VIEW vw_attempted_question_tags_correct_count AS 
select T.users_id,
sum((case when (T.dtype = 'Category') then 1 else 0 end)) AS Category,
sum((case when (T.dtype = 'Body region') then 1 else 0 end)) AS `Body region`,
sum((case when (T.dtype = 'Treatment techniques') then 1 else 0 end)) AS `Treatment techniques`
from (select distinct a.users_ID, q.question_ID, t.dtype
	from attempt a 
	join attempt_answer an on an.attempt_ID = a.attempt_ID
	join question q on q.question_ID = an.question_ID
	join tag_question tq on tq.question_ID = q.question_ID
	join tag t on t.tag_ID = tq.tag_ID
	where an.is_correct = true) AS T
group by T.users_id;

CREATE VIEW vw_attempted_question_tags_count AS 
select T.users_id,
sum((case when (T.dtype = 'Category') then 1 else 0 end)) AS Category,
sum((case when (T.dtype = 'Body region') then 1 else 0 end)) AS `Body region`,
sum((case when (T.dtype = 'Treatment techniques') then 1 else 0 end)) AS `Treatment techniques`
from (select distinct a.users_ID, q.question_ID, t.dtype
	from attempt a 
	join attempt_answer an on an.attempt_ID = a.attempt_ID
	join question q on q.question_ID = an.question_ID
	join tag_question tq on tq.question_ID = q.question_ID
	join tag t on t.tag_ID = tq.tag_ID) AS T
group by T.users_id;

CREATE VIEW vw_question_tags_count AS SELECT
sum((case when (t.dtype = 'Category') then 1 else 0 end)) AS Category,
sum((case when (t.dtype = 'Body region') then 1 else 0 end)) AS `Body region`,
sum((case when (t.dtype = 'Treatment techniques') then 1 else 0 end)) AS `Treatment techniques`
from tag_question tq
join tag t on t.tag_ID = tq.tag_ID;

CREATE VIEW vw_test_info_for_attempt AS
SELECT t.test_ID, GROUP_CONCAT(DISTINCT q.question_ID SEPARATOR ',')
FROM question q
JOIN question_answer qa ON qa.question_ID = q.question_ID
JOIN answer a ON a.answer_ID = qa.answer_ID
JOIN test_question tq ON tq.question_id = q.question_ID
JOIN test t ON t.test_ID = tq.test_id
GROUP BY t.test_ID;