from main import Teacher

teacher_total = []

def add_teacher():

    add = str(input('Teacher name: ->')).strip().capitalize()
    add2 = str(input('Teacher subject: ->')).strip().capitalize()
    teacher = Teacher(add,add2)
    teacher = teacher.__str__()
    teacher_total.append(teacher)
