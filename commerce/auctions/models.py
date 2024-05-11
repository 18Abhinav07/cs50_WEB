from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    # Define fields for auction listing model
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    image_url = models.URLField(null = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    favoured = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_favoured", blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.current_bid = self.starting_bid
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('auction_view', kwargs={"pk": self.pk})
    

class Bid(models.Model):
    # Define fields for bid model
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.bid_amount} bid on {self.listing} by {self.bidder}"

class Comment(models.Model):
    # Define fields for comment model
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.commenter} comment on {self.listing}"
    
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('category_listings', kwargs={'slug': self.slug})
