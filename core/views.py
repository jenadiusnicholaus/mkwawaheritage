from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from .models import (
    Chief, HistoricalEvent, TourismSite, Booking,
    Product, ProductCategory, Project, ProjectCategory,
    Newsletter, ContactMessage, Bid
)


def home(request):
    """Homepage with featured content"""
    chiefs = Chief.objects.all()[:2]  # First and current chief
    featured_projects = Project.objects.filter(featured=True, status='ongoing')[:3]
    featured_products = Product.objects.filter(featured=True, status='available')[:6]
    recent_events = HistoricalEvent.objects.all()[:3]
    tourism_sites = TourismSite.objects.filter(is_active=True)[:3]
    
    context = {
        'chiefs': chiefs,
        'featured_projects': featured_projects,
        'featured_products': featured_products,
        'recent_events': recent_events,
        'tourism_sites': tourism_sites,
    }
    return render(request, 'core/home.html', context)


def heritage_view(request):
    """Historical background page"""
    chiefs = Chief.objects.all()
    events = HistoricalEvent.objects.all()
    
    # Filter by chief if specified
    chief_filter = request.GET.get('chief')
    if chief_filter:
        events = events.filter(chief__slug=chief_filter)
    
    context = {
        'chiefs': chiefs,
        'events': events,
    }
    return render(request, 'core/heritage.html', context)


def chief_detail(request, slug):
    """Individual chief detail page"""
    chief = get_object_or_404(Chief, slug=slug)
    events = chief.events.all()
    
    context = {
        'chief': chief,
        'events': events,
    }
    return render(request, 'core/chief_detail.html', context)


def tourism_view(request):
    """Tourism sites listing"""
    sites = TourismSite.objects.filter(is_active=True)
    
    # Filter by type
    site_type = request.GET.get('type')
    if site_type:
        sites = sites.filter(site_type=site_type)
    
    context = {
        'sites': sites,
        'site_types': TourismSite.SITE_TYPES,
    }
    return render(request, 'core/tourism.html', context)


def tourism_detail(request, slug):
    """Individual tourism site detail and booking"""
    site = get_object_or_404(TourismSite, slug=slug, is_active=True)
    
    if request.method == 'POST':
        # Handle booking submission
        visitor_name = request.POST.get('visitor_name')
        visitor_email = request.POST.get('visitor_email')
        visitor_phone = request.POST.get('visitor_phone')
        visitor_type = request.POST.get('visitor_type')
        number_of_visitors = int(request.POST.get('number_of_visitors', 1))
        visit_date = request.POST.get('visit_date')
        visit_time = request.POST.get('visit_time')
        special_requirements = request.POST.get('special_requirements', '')
        
        # Calculate total amount
        if visitor_type == 'local':
            total_amount = site.entry_fee_local * number_of_visitors
        else:
            total_amount = site.entry_fee_foreign * number_of_visitors
        
        booking = Booking.objects.create(
            tourism_site=site,
            visitor_name=visitor_name,
            visitor_email=visitor_email,
            visitor_phone=visitor_phone,
            visitor_type=visitor_type,
            number_of_visitors=number_of_visitors,
            visit_date=visit_date,
            visit_time=visit_time,
            special_requirements=special_requirements,
            total_amount=total_amount,
        )
        
        messages.success(request, f'Booking confirmed! Your reference number is {booking.booking_reference}')
        return redirect('booking_confirmation', reference=booking.booking_reference)
    
    context = {
        'site': site,
    }
    return render(request, 'core/tourism_detail.html', context)


def booking_confirmation(request, reference):
    """Booking confirmation page"""
    booking = get_object_or_404(Booking, booking_reference=reference)
    
    context = {
        'booking': booking,
    }
    return render(request, 'core/booking_confirmation.html', context)


def products_view(request):
    """Products catalog with filtering"""
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    # Filter by type
    product_type = request.GET.get('type')
    if product_type:
        products = products.filter(product_type=product_type)
    
    # Filter by status
    status = request.GET.get('status')
    if status:
        products = products.filter(status=status)
    else:
        products = products.exclude(status='sold')
    
    # Search
    search = request.GET.get('search')
    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(artist_name__icontains=search)
        )
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'product_types': Product.PRODUCT_TYPES,
    }
    return render(request, 'core/products.html', context)


def product_detail(request, slug):
    """Individual product detail with bidding"""
    product = get_object_or_404(Product, slug=slug)
    recent_bids = product.bids.all()[:5]
    
    if request.method == 'POST':
        # Handle bid submission
        bidder_name = request.POST.get('bidder_name')
        bidder_email = request.POST.get('bidder_email')
        bidder_phone = request.POST.get('bidder_phone')
        bid_amount = float(request.POST.get('bid_amount'))
        
        # Validate bid amount
        min_bid = product.current_bid or product.starting_bid or product.price
        if bid_amount > min_bid:
            # Update previous winning bid
            Bid.objects.filter(product=product, is_winning=True).update(is_winning=False)
            
            # Create new bid
            bid = Bid.objects.create(
                product=product,
                bidder_name=bidder_name,
                bidder_email=bidder_email,
                bidder_phone=bidder_phone,
                bid_amount=bid_amount,
                is_winning=True
            )
            
            # Update product current bid
            product.current_bid = bid_amount
            product.status = 'bidding'
            product.save()
            
            messages.success(request, 'Your bid has been placed successfully!')
            return redirect('product_detail', slug=slug)
        else:
            messages.error(request, f'Bid must be higher than ${min_bid}')
    
    context = {
        'product': product,
        'recent_bids': recent_bids,
    }
    return render(request, 'core/product_detail.html', context)


def projects_view(request):
    """Projects showcase page"""
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        projects = projects.filter(category__slug=category_slug)
    
    # Filter by status
    status = request.GET.get('status')
    if status:
        projects = projects.filter(status=status)
    
    context = {
        'projects': projects,
        'categories': categories,
        'status_choices': Project.STATUS_CHOICES,
    }
    return render(request, 'core/projects.html', context)


def project_detail(request, slug):
    """Individual project detail page"""
    project = get_object_or_404(Project, slug=slug)
    
    context = {
        'project': project,
    }
    return render(request, 'core/project_detail.html', context)


def contact_view(request):
    """Contact page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'core/contact.html')


def newsletter_subscribe(request):
    """Newsletter subscription handler"""
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name', '')
        
        newsletter, created = Newsletter.objects.get_or_create(
            email=email,
            defaults={'name': name}
        )
        
        if created:
            messages.success(request, 'Successfully subscribed to our newsletter!')
        else:
            messages.info(request, 'You are already subscribed to our newsletter.')
        
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    return redirect('home')
