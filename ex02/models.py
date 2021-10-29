from django.db import models

# Create your models here.
class Record(models.Model):
	content = models.TextField(null=False, blank=True)
	published = models.DateTimeField(auto_now_add=True, db_index=True)
