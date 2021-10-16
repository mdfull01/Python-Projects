from django.db import models


# create djangoClasses class and attributes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=100, default='')
    CourseNumber = models.IntegerField(null=False)
    InstructorName = models.CharField(max_length=75, default='')
    Duration = models.FloatField()

    # assign model manager to objects
    objects = models.Manager()

    # when queried it will list title instead of index number
    def __str__(self):
        return self.Title
