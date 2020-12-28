from rest_framework import routers
from . models import Courses
from . serializer import CoursesSerializer
from . viewset import CoursesViewSet


router = routers.DefaultRouter()
router.register('courses', CoursesViewSet)