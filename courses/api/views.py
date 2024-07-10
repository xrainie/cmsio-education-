from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer, CourseSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# class EnrollCourseView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({"enrolled": True})


@action(
    detail=True,
    methods=["POST"],
    authentication_classes=[BasicAuthentication],
    permission__classes=[IsAuthenticated],
)
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({"enrolled": True})
