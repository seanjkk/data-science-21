# Data Normalization and Entity-Relationship Diagramming

## Original Data Set

### Original Table

The following table, representing students' grades in courses at a university, is already in [first normal form](https://knowledge.kitchen/A_Simple_Guide_to_Five_Normal_Forms_in_Relational_Database_Theory#FIRST_NORMAL_FORM) (1NF) - all records have the same number of fields, and there is only one value per field.

| assignment_id | student_id | due_date | professor | assignment_topic                | classroom | grade | relevant_reading    | professor_email   |
| :------------ | :--------- | :------- | :-------- | :------------------------------ | :-------- | :---- | :------------------ | :---------------- |
| 1             | 1          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 80    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 2             | 7          | 18.11.21 | Logston   | Single table queries            | 60FA 314  | 25    | Dümmlers Chapter 11 | e.logston@foo.edu |
| 1             | 4          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 75    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 5             | 2          | 05.05.21 | Logston   | Python and pandas               | 60FA 314  | 92    | Dümmlers Chapter 14 | e.logston@foo.edu |
| 4             | 2          | 04.07.21 | Nevarez   | Spreadsheet aggregate functions | WWH 201   | 65    | Zehnder Page 87     | i.nevarez@foo.edu |
| ...           | ...        | ...      | ...       | ...                             | ...       | ...   | ...                 | ...               |

## Assumptions

This data represents information about students' grades in courses at a university. The dependencies reflect the reality of how courses work in most universities.

- each course can be taught by multiple professors in different sections
- each professor might teach multiple sections of the same course
- each section meets in a specific classroom with a specific professor
- professors give assignments, with specific due dates
- a professor might give the same assignment to different sections of the same course, but with different due dates
- professors give readings to help with the assignments
- students complete assignments and receive a grade

### 4NF Compliance

This data set is not 4NF compliant:

1. It is not 2NF compliant because there are non-key fields that are facts of only a subset of the whole key.
    * ie. assignment_topic is only a fact about assignment_id and not student_id
2. It is not 3NF compliant as there are non-key fields that are facts about other non-key fields
    * ie. professor_email is a fact about professor

## My Tables and ER Diagram
### My Updated Tables
| <ins>assignment_id</ins>| <ins>student_id</ins> | grade |
| :------------ | :--------- | :------- |
| ...           | ...        | ...      |

| <ins>assignment_id</ins>| <ins>section_id</ins> | due_date |
| :------------ | :--------- | :------- |
| ...           | ...        | ...      |

| <ins>assignment_id</ins>| assignment_topic | relevant_reading |
| :------------ | :--------- | :------- |
| ...           | ...        | ...      |

| <ins>section_id</ins>| professor | classroom |
| :------------ | :--------- | :------- |
| ...           | ...        | ...      |

| <ins>professor</ins>| professor_email |
| :------------ | :--------- |
| ...           | ...        |

### My ER Diagram

![ER Diagram](images/er_diagram.svg)

### Details

- I created a new key called section_id, as the due_date was dependent and different for each section (and not by professor) according to the assumptions
- I split the data into multiple tables, so that every non-key field is a fact about the key field
    * grade is a fact based on both <ins>assignment_id</ins> and <ins>student_id</ins>
    * due_date is a fact based on both <ins>assignment_id</ins> and <ins>section_id</ins>
    * assignment_topic and relevant_readings are facts based on only <ins>assignment_id</ins>
    * professor and classroom are facts based on only <ins>section_id</ins>
    * professor_email is a fact based on only <ins>professor</ins>
- I have also separated the facts into multiple tables so that there aren't two multi-valued facts in one table, so the tables are 1NF, 2NF, 3NF and 4NF compliant
