from django.db import models

# Create your models here.

class ToDo(models.Model):
  added_time=models.DateTimeField()
  todo=models.CharField(max_length=200)
  def __str__(self):
        return '{}'.format(self.todo)

  class Meta:
        verbose_name_plural = 'ToDos'

