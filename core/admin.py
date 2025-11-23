from django.contrib import admin
from .models import (
    Chief, HistoricalEvent, TourismSite, Booking,
    ProductCategory, Product, Bid, ProjectCategory,
    Project, Newsletter, ContactMessage
)


@admin.register(Chief)
class ChiefAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'reign_start', 'reign_end']
    list_filter = ['position']
    search_fields = ['name', 'biography']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['position']


@admin.register(HistoricalEvent)
class HistoricalEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'chief', 'created_at']
    list_filter = ['date', 'chief']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'


@admin.register(TourismSite)
class TourismSiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'site_type', 'region', 'entry_fee_local', 'is_active']
    list_filter = ['site_type', 'is_active', 'region']
    search_fields = ['name', 'description', 'location']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'site_type', 'description', 'slug')
        }),
        ('Location', {
            'fields': ('location', 'region')
        }),
        ('Pricing & Capacity', {
            'fields': ('entry_fee_local', 'entry_fee_foreign', 'capacity', 'opening_hours')
        }),
        ('Additional Info', {
            'fields': ('amenities', 'image', 'gallery_images', 'is_active')
        }),
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_reference', 'visitor_name', 'tourism_site', 'visit_date', 'status', 'total_amount']
    list_filter = ['status', 'visitor_type', 'visit_date', 'tourism_site']
    search_fields = ['booking_reference', 'visitor_name', 'visitor_email']
    date_hierarchy = 'visit_date'
    readonly_fields = ['booking_reference', 'created_at', 'updated_at']
    fieldsets = (
        ('Booking Details', {
            'fields': ('booking_reference', 'tourism_site', 'visit_date', 'visit_time', 'status')
        }),
        ('Visitor Information', {
            'fields': ('visitor_name', 'visitor_email', 'visitor_phone', 'visitor_type', 'number_of_visitors')
        }),
        ('Additional', {
            'fields': ('special_requirements', 'total_amount', 'created_at', 'updated_at')
        }),
    )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'product_type', 'price', 'status', 'featured', 'created_at']
    list_filter = ['product_type', 'status', 'category', 'featured']
    search_fields = ['name', 'description', 'artist_name']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description', 'slug')
        }),
        ('Product Details', {
            'fields': ('product_type', 'artist_name', 'year_created', 'dimensions', 'materials')
        }),
        ('Pricing', {
            'fields': ('price', 'starting_bid', 'current_bid', 'status', 'stock_quantity')
        }),
        ('Media', {
            'fields': ('image', 'gallery_images', 'nft_metadata')
        }),
        ('Settings', {
            'fields': ('featured',)
        }),
    )


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['product', 'bidder_name', 'bid_amount', 'is_winning', 'created_at']
    list_filter = ['is_winning', 'created_at']
    search_fields = ['bidder_name', 'bidder_email', 'product__name']
    readonly_fields = ['created_at']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'start_date', 'progress_percentage', 'featured']
    list_filter = ['status', 'category', 'featured', 'start_date']
    search_fields = ['title', 'description', 'location']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'start_date'
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'description', 'objectives', 'slug')
        }),
        ('Timeline & Location', {
            'fields': ('start_date', 'end_date', 'location', 'status', 'progress_percentage')
        }),
        ('Budget & Impact', {
            'fields': ('budget', 'beneficiaries', 'impact_summary', 'partners')
        }),
        ('Media', {
            'fields': ('image', 'gallery_images', 'featured')
        }),
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_active', 'subscribed_at']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email', 'name']
    readonly_fields = ['subscribed_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
