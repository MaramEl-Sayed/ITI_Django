from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views import View
from .models import Trainee
from .forms import TraineeForm

# List all trainees
class TraineeListView(ListView):
    model=Trainee
    template_name="trainee/trainee_list.html"
    context_object_name="trainees"

# # Create a new trainee
class TraineeCreateView(View):
    template_name="trainee/trainee_form.html"

    def get(self,request):
        form =TraineeForm()
        return render(request, self.template_name,{"form":form})
    def post(self,request):
        form =TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("trainee_list")
        return render(request, self.template_name,{"form":form})

# # Update a Trainee
class TraineeUpdateView(View):
    template_name="trainee/trainee_form.html"

    def get(self,request,pk):
        trainee=get_object_or_404(Trainee,id=pk)
        form=TraineeForm(instance=trainee)
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,pk):
        trainee=get_object_or_404(Trainee,id=pk)
        form=TraineeForm(request.POST,instance=trainee)
        if form.is_valid():
            form.save()
            return redirect("trainee_list")
        return render(request,self.template_name,{"form":form})
    
# # Delete Trainee
class TraineeDeleteView(DeleteView):
    model=Trainee
    template_name="trainee/confirm_delete.html"
    success_url=reverse_lazy("trainee_list")

# # trainee show details
class TraineeDetailView(DetailView):
    model=Trainee
    template_name="trainee/trainee_detail.html"
    context_object_name="trainee"
    
#################################################
# # function Based
# # list trainees

# def trainee_list(request):
#     trainees = Trainee.objects.select_related("course").all() 
#     return render(request, "trainee/trainee_list.html", {"trainees": trainees})

# # Add a new trainee
# def add_trainee(request):
#     if request.method == "POST":
#         form = TraineeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("trainee_list")
#     else:
#         form = TraineeForm()
#     return render(request, "trainee/trainee_form.html", {"form": form})

# # Update an existing trainee
# def update_trainee(request, trainee_id):
#     trainee = get_object_or_404(Trainee, id=trainee_id)
#     if request.method == "POST":
#         form = TraineeForm(request.POST, instance=trainee)
#         if form.is_valid():
#             form.save()
#             return redirect("trainee_list")
#     else:
#         form = TraineeForm(instance=trainee)
#     return render(request, "trainee/trainee_form.html", {"form": form})

# # Delete a trainee
# def delete_trainee(request, trainee_id):
#     trainee = get_object_or_404(Trainee, id=trainee_id)
#     if request.method == "POST":
#         trainee.delete()
#         return redirect("trainee_list")
#     return render(request, "trainee/confirm_delete.html", {"trainee": trainee})
