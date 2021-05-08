from django.db import models

technology_used_choice=(
		('python','Python'),
		('php','PHP'),
		('java','JAVA'),
		('flutter','flutter')
	)

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='image/')
	description = models.TextField()
	technology_used = models.CharField(max_length=50, choices=technology_used_choice)

	def __str__(self):
		return self.title