from django.db import models

class CatFact(models.Model):
    text = models.TextField()
    fetched_at = models.DateTimeField(auto_now_add=True, db_index=True)  # Add db_index=True to create an index
    user_id = models.CharField(max_length=50) 