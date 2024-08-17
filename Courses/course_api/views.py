from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


# Courses -----------------------------------------------------------


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'

# Course Instances -----------------------------------------------------------


class CourseInstanceListView(generics.ListCreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer


class CourseInstanceCreateView(generics.CreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer


class CourseInstanceFilterView(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)


class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return CourseInstance.objects.get(year=year, semester=semester, course__id=course_id)
