from django.db import models
from django.urls import reverse
from datetime import date

class Type(models.Model):
    type= models.CharField(unique=True, max_length=50, help_text='Enter a product type (e. g. fruits)')

    def __str__(self):
        return self.type

class Mark(models.Model):
    mark = models.CharField(unique=True, max_length=50, help_text='Enter a mark (e. g. fresh)')

    def __str__(self):
        return self.mark

class Measure(models.Model):
    unit = models.CharField(unique=True, max_length=10, help_text='Enter a unit of measure (e. g. Kg)')

    def __str__(self):
        return self.unit

class Product(models.Model):
    name = models.CharField(max_length=100)
    measure = models.ForeignKey(Measure,on_delete=models.CASCADE)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    mark = models.ForeignKey(Mark,on_delete=models.CASCADE)
    akce = models.BooleanField(default=False)
    description = models.TextField(null=True)
    img = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        output = f"{self.name} (1{self.measure}), "
        output += f"{self.type}, "
        output += f"{self.price} Kč/{self.measure}, "
        output += f"{self.mark}, "
        if (self.akce):
            output += f"AKCE, "
        output += f"{self.description[0:20]}..."
        return output

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        ordering = ["type", "name", "price", "akce"]