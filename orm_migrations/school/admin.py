from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'display_teachers']
    list_filter = ['group', 'teachers']
    filter_horizontal = ['teachers']  # Удобный интерфейс для выбора учителей

    def display_teachers(self, obj):
        return ", ".join([f"{teacher.name} ({teacher.subject})" for teacher in obj.teachers.all()])

    display_teachers.short_description = 'Учителя'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'students_count']
    list_filter = ['subject']

    def students_count(self, obj):
        return obj.students.count()

    students_count.short_description = 'Количество учеников'