from django.db import models

# Create your models here.
from django.utils import timezone


class TodayTrend(models.Model):
    rank = models.IntegerField()
    url = models.CharField(max_length=2000)
    desc = models.TextField()
    language = models.CharField(max_length=250)
    star_count = models.IntegerField()
    fork_count = models.IntegerField()
    today_star_count = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.created_at) + ' | ' + str(self.today_star_count) + ' | ' + str(self.rank) + ' | ' + self.url

    class Meta:
        ordering = ['-pk']