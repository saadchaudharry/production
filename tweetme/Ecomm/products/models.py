from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save
from Ecomm.utils import unique_slug_generator

CAT = 'cats'
BIRD = 'birds'
DOG = 'dogs'
ACCESSORIES = 'accessories'
FEATURED = "featured"
fish = "fish"

CATAGORY_CHOICES = [
    (CAT, 'Cat'),
    (DOG, 'Dog'),
    (BIRD, 'Bird'),
    (FEATURED, 'Featured'),
    (fish, 'Fishes'),
    (ACCESSORIES, 'Accessories')
]

# Create your models here.
class Prooductmanger(models.Manager):
    def featured(self):
        return self.get_queryset().filter(catagory="featured")
    def cat(self):
        return self.get_queryset().filter(catagory="cats")
    def dog(self):
        return self.get_queryset().filter(catagory="dogs")
    def bird(self):
        return self.get_queryset().filter(catagory="birds")
    def accessories(self):
        return self.get_queryset().filter(catagory="accessories")
    def fish(self):
        return self.get_queryset().filter(catagory="fish")

    #search
    def search(self,query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)|Q(tag__title__icontains=query)
        return self.filter(lookup)


class Product(models.Model):
    title        =models.CharField(max_length=120)
    image        =models.ImageField(upload_to="productsimg/",null=True)
    slug         =models.SlugField(max_length=120,blank=True,unique=True,null=True)
    description  =models.TextField()
    price        =models.DecimalField(decimal_places=2,max_digits=999999,null=True)
    catagory = models.CharField(max_length=120, choices=CATAGORY_CHOICES, default=CAT)
    objects =Prooductmanger()



    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Products:slug',kwargs={'slug':self.slug})

def Product_slug_pre_save(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(Product_slug_pre_save,sender=Product)





    # FISH = 'fi'
    # CAT = 'ca'
    # BIRD = 'bi'
    # OTHER = 'ot'
    # CATAGORY_CHOICES = [
    #     (FISH, 'Fish'),
    #     (CAT, 'Cat'),
    #     (BIRD, 'Bird'),
    #     (OTHER, 'Other'),
    # ]
    # catagory = models.CharField(max_length=120, choices=CATAGORY_CHOICES, default=FISH)




  # cat          =models.BooleanField(default=False)
  #   dog          =models.BooleanField(default=False)
  #   bird         =models.BooleanField(default=False)
  #   fish         =models.BooleanField(default=False)
  #   featured     =models.BooleanField(default=False)#exotic
  #   accessories  =models.BooleanField(default=False)