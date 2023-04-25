from django.http import HttpResponse
from faker import Faker

from .models import Student

fake = Faker()


def generate_student(request):
    if request.method == 'GET':

        student = Student.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=fake.random_int(min=17, max=24)
        )

        return HttpResponse(f"ID нового студента  {student.id}")
    else:
        return HttpResponse("Invalid request method")


def generate_students(request):
    if request.method == 'GET':
        count = request.GET.get('count', 0)

        try:
            count = int(count)
            if count < 1 or count > 100:
                raise ValueError("Invalid count value")
        except ValueError as e:
            return HttpResponse(f"Invalid count parameter: {str(e)}")

        for i in range(count):
            Student.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.random_int(min=17, max=24)
            )

        return HttpResponse(f"{count} студентів було створено")
    else:
        return HttpResponse("Invalid request method")
