maths_marks = int(input("marks in maths: "))
science_marks = int(input("marks in science: "))
english_marks = int(input("marks in english: "))
total_marks = maths_marks + science_marks + english_marks
print(f"Total marks: {total_marks}")
average_marks = total_marks/3
print(f"Average marks: {average_marks}")
percentage = (total_marks/300)*100
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
else:
    print("Fail")