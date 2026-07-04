from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

students = [
    {'name': 'John', 'age': 20, 'grade': 'A'},
    {'name': 'Jane', 'age': 22, 'grade': 'B'},
    {'name': 'Bob', 'age': 21, 'grade': 'C'},
    {'name': 'Alice', 'age': 23, 'grade': 'A'},
]
def student_detail(request,id):
    student = students[id]
    message = f"This is the student detail page for {student.get('name')}, \
    Age: {student.get('age')}, Grade: {student.get('grade')}"
    return HttpResponse(message)
