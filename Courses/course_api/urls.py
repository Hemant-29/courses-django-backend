from django.urls import path
from .views import CourseListCreateView, CourseDetailView, CourseInstanceListView, CourseInstanceCreateView, CourseInstanceFilterView, CourseInstanceDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:id>/', CourseDetailView.as_view(), name='course-detail'),

    path('instances/', CourseInstanceListView.as_view(),
         name='course-instance-list'),

    path('instances/', CourseInstanceCreateView.as_view(),
         name='course-instance-create'),
    path('instances/<int:year>/<int:semester>/',
         CourseInstanceFilterView.as_view(), name='course-instance-filter'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/',
         CourseInstanceDetailView.as_view(), name='course-instance-detail'),
]
