# MkwawaHeritage.com - Professional Website

A comprehensive Django-based website for MkwawaHeritage, celebrating the legacy of Chief Mkwawa and the Southern Highlands community.

## Features

### 1. **Historical Heritage Section**
- Complete lineage of Chief Mkwawa (1st to 5th)
- Detailed biographies and achievements
- Timeline of historical events
- Rich multimedia content

### 2. **Tourism & Booking System**
- Museum booking system
- Game reserve reservations
- Cultural site visits
- Online booking with instant confirmation
- Automated booking reference generation
- Price calculator for local and foreign visitors

### 3. **Arts & Crafts Marketplace**
- Product catalog with categories
- NFT and physical product support
- Bidding system for auctions
- Advanced filtering and search
- Artist profiles
- Product galleries

### 4. **Community Projects**
- Aquaculture projects
- Horticulture initiatives
- Irrigation activities
- Project progress tracking
- Impact statistics
- Partner information

### 5. **Contact & Communication**
- Contact form
- Newsletter subscription
- Social media integration
- Location information

## Technology Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Styling**: Custom CSS with CSS Variables
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Playfair Display, Poppins)

## Project Structure

```
mkwawaheritage/
├── core/                      # Main application
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # URL routing
│   ├── admin.py              # Admin configuration
│   ├── static/               # Static files
│   │   ├── css/
│   │   │   └── style.css     # Main stylesheet
│   │   ├── js/
│   │   │   └── main.js       # JavaScript functions
│   │   ├── historical/       # Historical images
│   │   ├── products/         # Product images
│   │   └── projects/         # Project images
│   └── migrations/           # Database migrations
├── settings/                  # Project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI configuration
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   └── core/                 # App templates
├── media/                     # User-uploaded files
├── env/                       # Virtual environment
├── manage.py                  # Django management script
└── db.sqlite3                # Database file
```

## Models

### Chief
- Complete information about each Chief Mkwawa
- Biography, achievements, reign period
- Images and related events

### HistoricalEvent
- Significant events in heritage history
- Dates, descriptions, related chiefs

### TourismSite
- Museums, game reserves, cultural sites
- Pricing, capacity, opening hours
- Location and amenities

### Booking
- Tourism site reservations
- Visitor information
- Payment tracking
- Status management

### Product
- Arts and crafts items
- NFT and physical product support
- Pricing and bidding
- Artist information

### Project
- Community development projects
- Progress tracking
- Budget and impact metrics
- Partner information

## Setup Instructions

### 1. Navigate to Project Directory
```bash
cd /Users/mac/development/python_projects/mkwawaheritage
```

### 2. Activate Virtual Environment
```bash
source env/bin/activate
```

### 3. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

### 5. Access the Website
- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Admin Panel

Access the admin panel at `/admin/` to manage:
- Chiefs and historical events
- Tourism sites and bookings
- Products and categories
- Projects and categories
- Newsletter subscriptions
- Contact messages

## Features Breakdown

### Homepage
- Hero section with call-to-action
- Featured chiefs introduction
- Tourism sites preview
- Products showcase
- Projects highlights
- Historical timeline
- Newsletter signup

### Heritage Page
- Complete chiefs timeline
- Detailed biographies
- Historical events
- Filtering by chief

### Tourism & Booking
- Site listings with filters
- Detailed site information
- Online booking form
- Price calculator
- Booking confirmation

### Products Catalog
- Grid layout with images
- Category filtering
- Type filtering (NFT/Physical)
- Search functionality
- Bidding system
- Product details

### Projects Showcase
- Project grid with status
- Category filtering
- Progress tracking
- Impact statistics
- Partner information

### Contact Page
- Contact form
- Location information
- Office hours
- Social media links

## Design Features

### Professional UI/UX
- Modern, clean design
- Responsive layout (mobile-friendly)
- Smooth animations and transitions
- Intuitive navigation
- Accessible color scheme
- Professional typography

### Color Scheme
- Primary: #8B4513 (Saddle Brown)
- Secondary: #D2691E (Chocolate)
- Accent: #FFD700 (Gold)
- Dark: #2C1810
- Light: #F5E6D3

### Interactive Elements
- Mobile menu toggle
- Auto-hiding alerts
- Smooth scrolling
- Image hover effects
- Progress bar animations
- Filter animations
- Form validation

## Next Steps

1. **Add Content**: Use the admin panel to add:
   - Chiefs information (1st to 5th)
   - Historical events
   - Tourism sites
   - Products and categories
   - Projects

2. **Upload Images**: Add images for:
   - Chiefs
   - Historical events
   - Tourism sites
   - Products
   - Projects

3. **Configure Email**: Set up email backend for:
   - Booking confirmations
   - Contact form notifications
   - Newsletter system

4. **Payment Integration**: Integrate payment gateway for:
   - Tourism bookings
   - Product purchases

5. **NFT Integration**: Connect to blockchain for:
   - NFT minting
   - NFT trading

6. **Production Deployment**:
   - Configure production settings
   - Set up PostgreSQL database
   - Configure static file serving
   - Set up domain and SSL

## Dependencies

- Django 5.2.8
- Pillow 12.0.0 (for image handling)
- sqlparse 0.5.3 (SQL formatting)

## License

© 2025 MkwawaHeritage.com. All rights reserved.

## Support

For support or inquiries:
- Email: info@mkwawaheritage.com
- Phone: +255 123 456 789

---

**Built with pride for the preservation and celebration of Chief Mkwawa's legacy.**
# mkwawaheritage
