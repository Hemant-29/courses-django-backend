from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("Server running at port - 8000")


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


class CourseInstanceDetailView(generics.GenericAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return CourseInstance.objects.filter(year=year, semester=semester, course__id=course_id)

    def get(self, request, *args, **kwargs):
        instances = self.get_queryset()
        if instances.exists():
            serializer = self.get_serializer(instances, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        instances = self.get_queryset()
        if instances.exists():
            instances.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
