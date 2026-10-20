from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Student
from .forms import StudentForm

# CREATE Operation
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(
        request,
        'registration/student_form.html',
        {'form': form}
    )

# READ Operation
def student_list(request):
    students = Student.objects.all()
    return render(
        request,
        'registration/student_list.html',
        {'students': students}
    )

    # UPDATE Operation
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            instance=student
        )
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'student': student
        }
    )

# DELETE Operation
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(
        request,
        'registration/student_confirm_delete.html',
        {'student': student}
    )

def student_dashboard(request):
    students = Student.objects.all()
    total_students = students.count()

    program_summary = (
        students
        .values('program')
        .annotate(total=Count('id'))
        .order_by('program')
    )

    # ✅ NEW: Calculate students grouped by Year Level
    year_summary = (
        students
        .values('year_level')
        .annotate(total=Count('id'))
        .order_by('year_level')
    )

    return render(
        request,
        'registration/student_dashboard.html',
        {
            'total_students': total_students,
            'program_summary': program_summary,
            'year_summary': year_summary,  # ✅ NEW: Pass to template
        }
    )