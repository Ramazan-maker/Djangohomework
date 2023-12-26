from django.db import models

class AnotherModel(models.Model):
    field1 = models.CharField(max_length=100, verbose_name='Field 1')
    field2 = models.IntegerField(verbose_name='Field 2')

    def __str__(self):
        return f'{self.field1} - {self.field2}'

    class Meta:
        verbose_name_plural = 'Another Models'
        verbose_name = 'Another Model'