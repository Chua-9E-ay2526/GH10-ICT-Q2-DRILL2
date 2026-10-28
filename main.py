from pyscript import display, document

def add_new_guy(e):
    document.getElementById('result').innerHTML = ' '
    student_firstname = document.getElementById('fname').value
    student_lastname = document.getElementById('lname').value
    student_name = str(student_firstname) + " " + str(student_lastname)
    
    Teacher = {'Maria Dela Cruz'}
    G10 = {'John Doe'}
    G11 = {'Jane Doe'}
    G12 = {'Juan Dela Cruz'}

    Club_New_Student = G10 | G11 | G12 | Teacher
    Club_New_Student.add(student_name)

    display(f'The club members are: {Club_New_Student}', target='result')
    display(f'There are {len(Club_New_Student)} members in the club.', target='result')