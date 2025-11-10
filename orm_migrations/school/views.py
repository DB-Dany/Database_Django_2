from django.shortcuts import render
from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    # Получаем студентов с упорядочиванием по группе
    # и предзагружаем связанных учителей для оптимизации
    students = Student.objects.order_by('group').prefetch_related('teachers')

    context = {
        'object_list': students  # передаем в контекст под ключом object_list
    }

    return render(request, template, context)