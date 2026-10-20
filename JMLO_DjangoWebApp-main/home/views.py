from django.shortcuts import render

def dynamic_form(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        program = request.POST.get("program")
        context = {
            "student_name": student_name,
            "program": program
        }
        return render(
            request,
            "home/welcome.html",
            context
        )
    return render(
        request,
        "home/dynamic_form.html"
    )