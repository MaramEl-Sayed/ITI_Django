from django.urls import path,include
from .views import *
from .api.views import *
from rest_framework import routers

router=routers.SimpleRouter()
router.register(r'API',CourseModelViewSet)


urlpatterns = [
    path("", course_list, name="course_list"),
    path("add/", add_course, name="add_course"),
    path("update/<int:course_id>/", update_course, name="update_course"),
    path("delete/<int:course_id>/", delete_course, name="delete_course"),
    path('API/',Course_List_Create.as_view()),
    path('API/<int:id>/',Course_get_update_delete.as_view()),
    path('API/generic/',Course_List_Create_Generic.as_view()),
    path('API/generic/<pk>/',Course_get_update_delete_Generic.as_view()),
    # path('',include(router.urls)),

]
