from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

# List Courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, "course/course_list.html", {"courses": courses})

# Add Course
def add_course(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        
        Course.objects.create(name=name, description=description)
        return redirect("course_list")
    return render(request, "course/course_form.html")

# Update Course
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.name = request.POST["name"]
        course.description = request.POST["description"]
        # course.duration = request.POST["duration"]
        course.save()
        return redirect("course_list")
    return render(request, "course/course_form.html", {"course": course})

# Delete Course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(request, "course/course_confirm_delete.html", {"course": course})
