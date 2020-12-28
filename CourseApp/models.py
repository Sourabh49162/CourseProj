from django.db import models

# Create your models here.

my_choices = (
    ("0", "DEACTIVE"),
    ("1", "ACTIVE")
)


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=1,choices=my_choices, default="1")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


