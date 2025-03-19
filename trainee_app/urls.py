from django.urls import path
from .views import *
from .api.views import *

urlpatterns = [
    path("", TraineeListView.as_view(), name="trainee_list"),  
    path("add/", TraineeCreateView.as_view(), name="add_trainee"),  
    path("update/<int:pk>/", TraineeUpdateView.as_view(), name="update_trainee"),  
    path("delete/<int:pk>/", TraineeDeleteView.as_view(), name="delete_trainee"), 
    path("detail/<int:pk>/", TraineeDetailView.as_view(), name="trainee_detail"),  
    path("list/", getAll),
    path("list/<id>/",getbyid_update_delete)
]


##############################################################################
# from .views import trainee_list, add_trainee, update_trainee, delete_trainee
# urlpatterns = [
#     path("", trainee_list, name="trainee_list"),  # List all trainees
#     path("add/", add_trainee, name="add_trainee"),  # Add a new trainee
#     path("update/<int:trainee_id>/", update_trainee, name="update_trainee"),  # Update trainee
#     path("delete/<int:trainee_id>/", delete_trainee, name="delete_trainee"),  # Delete trainee
# ]
