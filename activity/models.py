from django.db import models
from django.conf import settings

# Create your models here.

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'activity_period'
