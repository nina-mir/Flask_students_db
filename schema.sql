DROP TABLE IF EXISTS students;

-- (a) Student ID, (b) first name, (c) last name, (d) email, (e) mailing address, and (f) GPA.

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    pronouns TEXT NOT NULL DEFAULT "They/Them/Theirs",
    email TEXT, 
    mail_add TEXT, 
    gpa TEXT NOT NULL DEFAULT "N/A"
);
