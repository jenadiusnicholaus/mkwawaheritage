from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Chief(models.Model):
    """Model for Chief Mkwawa lineage from 1st to 5th"""
    CHIEF_POSITIONS = [
        (1, 'First Chief'),
        (2, 'Second Chief'),
        (3, 'Third Chief'),
        (4, 'Fourth Chief'),
        (5, 'Fifth Chief'),
    ]
    
    name = models.CharField(max_length=200)
    position = models.IntegerField(choices=CHIEF_POSITIONS, unique=True)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    reign_start = models.IntegerField()
    reign_end = models.IntegerField(null=True, blank=True)
    biography = models.TextField()
    achievements = models.TextField()
    image = models.ImageField(upload_to='chiefs/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Chiefs'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Chief {self.name} - {self.get_position_display()}"


class HistoricalEvent(models.Model):
    """Historical events related to the Mkwawa heritage"""
    title = models.CharField(max_length=300)
    date = models.DateField()
    description = models.TextField()
    chief = models.ForeignKey(Chief, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')
    image = models.ImageField(upload_to='historical/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class TourismSite(models.Model):
    """Tourism locations including museum and game reserve"""
    SITE_TYPES = [
        ('museum', 'Museum'),
        ('game_reserve', 'Game Reserve'),
        ('cultural_site', 'Cultural Site'),
        ('historical_site', 'Historical Site'),
    ]
    
    name = models.CharField(max_length=200)
    site_type = models.CharField(max_length=20, choices=SITE_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=300)
    region = models.CharField(max_length=100, default='Southern Highlands')
    opening_hours = models.CharField(max_length=200)
    entry_fee_local = models.DecimalField(max_digits=10, decimal_places=2)
    entry_fee_foreign = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(help_text='Maximum visitors per day')
    amenities = models.TextField(help_text='Available facilities and services')
    image = models.ImageField(upload_to='tourism/', null=True, blank=True)
    gallery_images = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.get_site_type_display()}"


class Booking(models.Model):
    """Booking system for tourism sites"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    tourism_site = models.ForeignKey(TourismSite, on_delete=models.CASCADE, related_name='bookings')
    visitor_name = models.CharField(max_length=200)
    visitor_email = models.EmailField()
    visitor_phone = models.CharField(max_length=20)
    visitor_type = models.CharField(max_length=20, choices=[('local', 'Local'), ('foreign', 'Foreign')])
    number_of_visitors = models.IntegerField(validators=[MinValueValidator(1)])
    visit_date = models.DateField()
    visit_time = models.TimeField()
    special_requirements = models.TextField(blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booking_reference = models.CharField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.booking_reference:
            import uuid
            self.booking_reference = f"MKW{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.booking_reference} - {self.visitor_name}"


class ProductCategory(models.Model):
    """Categories for arts, crafts, and products"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Product Categories'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Arts, crafts, and products available as NFT or physical items"""
    PRODUCT_TYPES = [
        ('nft', 'NFT'),
        ('physical', 'Physical Product'),
        ('both', 'Both NFT & Physical'),
    ]
    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('bidding', 'Open for Bidding'),
        ('reserved', 'Reserved'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='products')
    description = models.TextField()
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    artist_name = models.CharField(max_length=200)
    dimensions = models.CharField(max_length=100, blank=True)
    materials = models.CharField(max_length=200, blank=True)
    year_created = models.IntegerField(null=True, blank=True)
    stock_quantity = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    gallery_images = models.JSONField(default=list, blank=True)
    nft_metadata = models.JSONField(default=dict, blank=True, help_text='NFT specific metadata')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Bid(models.Model):
    """Bidding system for products"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bids')
    bidder_name = models.CharField(max_length=200)
    bidder_email = models.EmailField()
    bidder_phone = models.CharField(max_length=20)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_winning = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-bid_amount', '-created_at']
    
    def __str__(self):
        return f"{self.bidder_name} - ${self.bid_amount} on {self.product.name}"


class ProjectCategory(models.Model):
    """Categories for projects"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Icon class name')
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Project Categories'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """Community projects: aquaculture, horticulture, irrigation"""
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('suspended', 'Suspended'),
    ]
    
    title = models.CharField(max_length=300)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, related_name='projects')
    description = models.TextField()
    objectives = models.TextField()
    location = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    beneficiaries = models.IntegerField(help_text='Number of people benefiting')
    progress_percentage = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    impact_summary = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    gallery_images = models.JSONField(default=list, blank=True)
    partners = models.TextField(blank=True, help_text='Partner organizations')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Newsletter(models.Model):
    """Newsletter subscription"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
