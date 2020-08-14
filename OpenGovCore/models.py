from django.db import models


# Create your models here.
class States(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"


class Parliamentary_Constituencies(models.Model):
    name = models.CharField(max_length=300)
    constituency_number = models.CharField(max_length=10)
    state = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Parliamentary_Constituency"
        verbose_name_plural = "Parliamentary_Constituencies"


class Assembly_Constituencies(models.Model):
    name = models.CharField(max_length=300)
    constituency_number = models.CharField(max_length=10)
    state = models.ForeignKey(
        States, on_delete=models.CASCADE, verbose_name='State')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Assembly_Constituency"
        verbose_name_plural = "Assembly_Constituencies"
