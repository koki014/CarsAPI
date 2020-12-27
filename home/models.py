from django.db import models

class Car(models.Model):
    FUEL_CHOICE = [
        ('B','Benzin'),
        ('D','Dizel'),
        ('Q','Qaz'),
    ]

    #information
    model = models.CharField('model', max_length=50)
    title = models.CharField('adi', max_length=20)
    fuel = models.CharField('yanacaq novu:', max_length=10, choices=FUEL_CHOICE)
    is_new = models.BooleanField('tezedir', default=False)
    image = models.ImageField('sekil', upload_to='car_images', blank=True, null=True)
    image_url = models.CharField('sekil url', max_length=255, blank=True, null=True)

    #moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'car'
        verbose_name = 'masin'
        verbose_name_plural = 'masinlar'

        
    def __str__(self):
        return self.model





