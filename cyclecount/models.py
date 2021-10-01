from django.db import models

# Create your models here.

def image_location(instance, filename):
    ext = filename.split('.')[-1]
    return 'U{0}.{1}'.format(instance.bin, ext)

# commented lpn just for convenience and testing
# add it before deployment
class StockModel(models.Model):
    content      = models.TextField(max_length=255, blank=True, verbose_name="Content")
    aile_num     = models.IntegerField(blank=False, verbose_name="Aile")
    level        = models.IntegerField(default = 0, verbose_name="Level")
    bin          = models.CharField(max_length=100, blank=False, verbose_name="Bin")
    # lpn          = models.CharField(max_length=100, blank=False, verbose_name="Barcode")
    last_scan    = models.DateTimeField(auto_now=True, verbose_name="Last Scan")
    first_scan   = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="First Scan")
    image        = models.ImageField(upload_to=image_location, blank=True, verbose_name="Image")
   
    def __str__(self):
        return self.bin