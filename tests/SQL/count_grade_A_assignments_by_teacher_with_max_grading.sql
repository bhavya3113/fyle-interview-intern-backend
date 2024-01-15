-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH grades_of_teachers AS (
    SELECT teacher_id, COUNT(*) as cnt_grades
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
),
maxigrades AS (
    SELECT teacher_id
    FROM grades_of_teachers
    ORDER BY cnt_grades DESC
    LIMIT 1
)
SELECT teacher_id, COUNT(*)
FROM assignments
WHERE teacher_id = (SELECT teacher_id FROM maxigrades)
AND grade = 'A';