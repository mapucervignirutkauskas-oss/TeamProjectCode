Milestone 1 – University Program

How to run

Make sure these files are in the same folder:

main Python file
`course_catalog.csv`
`university_data.csv`

Then run:

```
python your_program_file.py
```

The program loads all courses and students from the CSV files, creates the appropriate objects, enrolls students in their listed courses with their corresponding grades, and then prints the fully populated dictionaries to show that the data was loaded and linked correctly.
---

How to Test

You can add print statements at the bottom of the file to test things like:

```
print(u_files.get_student("STU00001").calculate_gpa())
print(u_files.get_course_enrollment("CSE2050"))
```

This lets you check GPA calculations and course enrollment counts.
