from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, time, timedelta
from decimal import Decimal
from core.models import (
    Chief, HistoricalEvent, TourismSite, Booking,
    ProductCategory, Product, ProjectCategory, Project,
    Bid, Newsletter, ContactMessage
)
import random


class Command(BaseCommand):
    help = 'Seeds the database with realistic test data for MkwawaHeritage'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            ContactMessage.objects.all().delete()
            Newsletter.objects.all().delete()
            Bid.objects.all().delete()
            Project.objects.all().delete()
            ProjectCategory.objects.all().delete()
            Product.objects.all().delete()
            ProductCategory.objects.all().delete()
            Booking.objects.all().delete()
            TourismSite.objects.all().delete()
            HistoricalEvent.objects.all().delete()
            Chief.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('✓ Existing data cleared'))

        self.stdout.write('Seeding database...\n')

        # Seed Chiefs
        self.stdout.write('Creating Chiefs...')
        chiefs_data = [
            {
                'name': 'Mkwawa Nyinyka',
                'position': 1,
                'reign_start': 1855,
                'reign_end': 1879,
                'biography': 'The founder of the Hehe kingdom, Chief Mkwawa Nyinyka was a visionary leader who unified various clans into a powerful kingdom. He established the capital at Kalenga and laid the foundation for what would become one of East Africa\'s most formidable military powers. His vision and leadership created a unified Hehe identity that persists to this day.',
                'achievements': 'United the Hehe clans, Established Kalenga as capital, Created strong military organization, Developed trade networks with coastal regions',
                'birth_year': 1830,
                'death_year': 1879,
            },
            {
                'name': 'Mkwawa Mtwa Nyinyka',
                'position': 2,
                'reign_start': 1879,
                'reign_end': 1898,
                'biography': 'The most famous of all Hehe chiefs, Chief Mkwawa II was a brilliant military strategist and fierce defender of his people\'s sovereignty. He successfully resisted German colonial forces for nearly two decades, earning respect even from his enemies. His tactical victory at the Battle of Lugalo in 1891, where he defeated a German expedition, is legendary. Symbol of African resistance to colonialism, his skull was returned to Tanzania in 1954 after being taken to Germany.',
                'achievements': 'Defeated German forces at Battle of Lugalo (1891), Maintained independence for 17 years, Established sophisticated intelligence network, Created formidable Hehe military force, Protected trade routes and territorial integrity',
                'birth_year': 1855,
                'death_year': 1898,
            },
            {
                'name': 'Mkwawa Mtengule',
                'position': 3,
                'reign_start': 1898,
                'reign_end': 1926,
                'biography': 'Following the death of his predecessor, Chief Mkwawa Mtengule had the difficult task of leading the Hehe people during the height of German colonial rule. He focused on preserving Hehe culture and traditions while adapting to the new colonial reality. Remembered for his diplomatic skills and cultural preservation efforts during challenging times.',
                'achievements': 'Preserved Hehe cultural traditions during colonial period, Established educational initiatives, Maintained peace while protecting Hehe interests, Promoted agriculture and local crafts',
                'birth_year': 1878,
                'death_year': 1926,
            },
            {
                'name': 'Mkwawa Sapi',
                'position': 4,
                'reign_start': 1926,
                'reign_end': 1957,
                'biography': 'Chief Mkwawa Sapi led during both the late colonial period and the early independence movement. He was an advocate for education and modernization while maintaining Hehe traditions. His reign saw the construction of schools and health facilities in Hehe territory. Pioneer of education and development in the Hehe region.',
                'achievements': 'Built schools and health facilities, Promoted literacy among the Hehe people, Supported the independence movement, Modernized agricultural practices, Strengthened community institutions',
                'birth_year': 1900,
                'death_year': 1957,
            },
            {
                'name': 'Mkwawa Gama',
                'position': 5,
                'reign_start': 1957,
                'reign_end': 1993,
                'biography': 'The fifth and most recent traditional chief, Chief Mkwawa Gama witnessed Tanzania\'s independence and the transformation of traditional leadership roles. He focused on preserving Hehe heritage while supporting national development initiatives. His work in preserving Hehe heritage has made him a cultural icon in modern Tanzania.',
                'achievements': 'Established the Mkwawa Memorial Museum, Documented Hehe history and traditions, Promoted tourism in the region, Supported community development projects, Preserved historical artifacts and sites',
                'birth_year': 1925,
                'death_year': 1993,
            },
        ]

        chiefs = []
        for chief_data in chiefs_data:
            chief = Chief.objects.create(**chief_data)
            chiefs.append(chief)
            self.stdout.write(f'  ✓ Created {chief.name}')

        # Seed Historical Events
        self.stdout.write('\nCreating Historical Events...')
        events_data = [
            {
                'chief': chiefs[0],
                'title': 'Unification of the Hehe Kingdom',
                'date': date(1855, 6, 15),
                'description': 'Chief Mkwawa Nyinyka successfully unified various Hehe clans under one kingdom, establishing Kalenga as the capital. This marked the beginning of the Hehe as a major political force in the region. Foundation of the unified Hehe kingdom.',
            },
            {
                'chief': chiefs[1],
                'title': 'Battle of Lugalo',
                'date': date(1891, 8, 17),
                'description': 'In one of the most significant battles of African resistance, Chief Mkwawa II\'s forces ambushed and decisively defeated a German military expedition led by Emil von Zelewski. Over 300 German soldiers and their allies were killed, and vast amounts of weapons and ammunition were captured. Greatest military victory against German colonialism in East Africa.',
            },
            {
                'chief': chiefs[1],
                'title': 'Construction of Kalenga Fortress',
                'date': date(1894, 3, 10),
                'description': 'Chief Mkwawa ordered the construction of a massive fortress at Kalenga with thick walls and strategic defensive positions. The fortress served as the center of Hehe military operations and administration.',
            },
            {
                'chief': chiefs[1],
                'title': 'Fall of Kalenga',
                'date': date(1894, 10, 30),
                'description': 'After a fierce battle, German forces captured and destroyed the Kalenga fortress. Chief Mkwawa escaped and continued guerrilla warfare for another four years. Beginning of the guerrilla phase of Hehe resistance.',
            },
            {
                'chief': chiefs[1],
                'title': 'Death of Chief Mkwawa',
                'date': date(1898, 7, 19),
                'description': 'Rather than be captured by German forces, Chief Mkwawa chose to take his own life. His head was taken by the Germans as a trophy and sent to Germany, not to be returned until 1954. End of active Hehe resistance, martyrdom for African independence.',
            },
            {
                'chief': chiefs[4],
                'title': 'Establishment of Mkwawa Memorial Museum',
                'date': date(1974, 7, 19),
                'description': 'Chief Mkwawa Gama established the Mkwawa Memorial Museum to preserve the history and artifacts of the Hehe people and honor the legacy of Chief Mkwawa II. Preservation of Hehe cultural heritage for future generations.',
            },
            {
                'chief': chiefs[1],
                'title': 'Return of Mkwawa\'s Skull',
                'date': date(1954, 6, 9),
                'description': 'After decades of diplomatic efforts, the skull of Chief Mkwawa was finally returned from Germany to Tanzania. It was received with great ceremony and laid to rest at the Kalenga memorial. Justice and closure for the Hehe people, symbol of post-colonial reconciliation.',
            },
        ]

        for event_data in events_data:
            event = HistoricalEvent.objects.create(**event_data)
            self.stdout.write(f'  ✓ Created event: {event.title}')

        # Seed Tourism Sites
        self.stdout.write('\nCreating Tourism Sites...')
        tourism_data = [
            {
                'name': 'Mkwawa Memorial Museum',
                'site_type': 'museum',
                'description': 'The Mkwawa Memorial Museum houses an extensive collection of artifacts from the Hehe kingdom, including weapons, traditional clothing, and historical documents. The museum tells the story of Chief Mkwawa II and the Hehe resistance against German colonialism. Guided tours, Gift shop, Parking, Restrooms, Photography allowed. Contact: +255 26 270 2345',
                'location': 'Kalenga Village, Iringa',
                'region': 'Iringa Region',
                'opening_hours': '8:00 AM - 5:00 PM',
                'entry_fee_local': Decimal('5000.00'),
                'entry_fee_foreign': Decimal('10000.00'),
                'capacity': 150,
                'amenities': 'Guided tours, Gift shop, Parking, Restrooms, Photography allowed',
                'is_active': True,
            },
            {
                'name': 'Chief Mkwawa Historical Site',
                'site_type': 'historical_site',
                'description': 'The ruins of the great Kalenga fortress where Chief Mkwawa made his last stand. Visitors can explore the remaining walls and learn about the historic battle that took place here in 1894. Walking trails, Information plaques, Parking, Local guides available. Contact: +255 26 270 2346',
                'location': 'Kalenga, Iringa',
                'region': 'Iringa Region',
                'opening_hours': '7:00 AM - 6:00 PM',
                'entry_fee_local': Decimal('3000.00'),
                'entry_fee_foreign': Decimal('8000.00'),
                'capacity': 200,
                'amenities': 'Walking trails, Information plaques, Parking, Local guides available',
                'is_active': True,
            },
            {
                'name': 'Ruaha National Park Gateway',
                'site_type': 'game_reserve',
                'description': 'Experience wildlife safari in one of Tanzania\'s largest national parks. Home to large populations of elephants, lions, leopards, and over 570 bird species. The park offers stunning landscapes and authentic African wilderness. 4x4 Safari vehicles, Professional guides, Camping sites, Lodges, Restaurant, First aid. Contact: +255 26 270 2888',
                'location': 'Tungamalenga, Iringa Region',
                'region': 'Iringa Region',
                'opening_hours': '6:00 AM - 6:00 PM',
                'entry_fee_local': Decimal('15000.00'),
                'entry_fee_foreign': Decimal('50000.00'),
                'capacity': 500,
                'amenities': '4x4 Safari vehicles, Professional guides, Camping sites, Lodges, Restaurant, First aid',
                'is_active': True,
            },
            {
                'name': 'Isimila Stone Age Site',
                'site_type': 'historical_site',
                'description': 'One of Africa\'s most significant Stone Age archaeological sites. Features ancient stone tools dating back 60,000 years and dramatic rock pillars formed by erosion. Museum, Guided tours, Parking, Picnic area. Contact: +255 26 270 2347',
                'location': 'Isimila, Iringa',
                'region': 'Iringa Region',
                'opening_hours': '8:00 AM - 5:00 PM',
                'entry_fee_local': Decimal('4000.00'),
                'entry_fee_foreign': Decimal('9000.00'),
                'capacity': 100,
                'amenities': 'Museum, Guided tours, Parking, Picnic area',
                'is_active': True,
            },
        ]

        tourism_sites = []
        for site_data in tourism_data:
            site = TourismSite.objects.create(**site_data)
            tourism_sites.append(site)
            self.stdout.write(f'  ✓ Created site: {site.name}')

        # Seed Bookings
        self.stdout.write('\nCreating Bookings...')
        visitor_names = [
            'John Mwangi', 'Sarah Johnson', 'Ahmed Hassan', 'Maria Garcia',
            'David Kimani', 'Emma Williams', 'Michael Omondi', 'Lisa Anderson',
            'James Mutua', 'Anna Schmidt', 'Robert Njoroge', 'Sophie Martin'
        ]

        for i in range(20):
            days_ahead = random.randint(1, 60)
            visitor_type = random.choice(['local', 'foreign'])
            site = random.choice(tourism_sites)
            num_visitors = random.randint(1, 8)
            
            entry_fee = site.entry_fee_local if visitor_type == 'local' else site.entry_fee_foreign
            total = entry_fee * num_visitors
            
            booking = Booking.objects.create(
                tourism_site=site,
                visitor_name=random.choice(visitor_names),
                visitor_email=f'visitor{i}@example.com',
                visitor_phone=f'+25571{random.randint(1000000, 9999999)}',
                visitor_type=visitor_type,
                number_of_visitors=num_visitors,
                visit_date=date.today() + timedelta(days=days_ahead),
                visit_time=time(random.randint(8, 15), random.choice([0, 30])),
                special_requirements='None' if random.random() > 0.3 else 'Need wheelchair access',
                total_amount=total,
                status=random.choice(['pending', 'confirmed', 'confirmed', 'confirmed']),
            )
            if i < 5:
                self.stdout.write(f'  ✓ Created booking: {booking.booking_reference}')

        self.stdout.write(f'  ✓ Created 20 bookings total')

        # Seed Product Categories
        self.stdout.write('\nCreating Product Categories...')
        categories_data = [
            {
                'name': 'Traditional Weapons',
                'description': 'Historical replicas and authentic traditional Hehe weapons',
            },
            {
                'name': 'Beadwork & Jewelry',
                'description': 'Handcrafted traditional Hehe beadwork and jewelry pieces',
            },
            {
                'name': 'Textiles & Clothing',
                'description': 'Traditional Hehe garments and woven textiles',
            },
            {
                'name': 'Pottery & Ceramics',
                'description': 'Handmade pottery and ceramic art pieces',
            },
            {
                'name': 'Wood Carvings',
                'description': 'Intricate wood sculptures and functional wooden items',
            },
            {
                'name': 'Paintings & Art',
                'description': 'Traditional and contemporary African art',
            },
        ]

        product_categories = []
        for cat_data in categories_data:
            category = ProductCategory.objects.create(**cat_data)
            product_categories.append(category)
            self.stdout.write(f'  ✓ Created category: {category.name}')

        # Seed Products
        self.stdout.write('\nCreating Products...')
        products_data = [
            {
                'category': product_categories[0],
                'name': 'Mkwawa\'s Ceremonial Spear Replica',
                'description': 'A faithful replica of Chief Mkwawa\'s ceremonial spear, handcrafted by master artisans using traditional techniques. Made from indigenous hardwood with intricate metalwork.',
                'product_type': 'both',
                'price': Decimal('250000.00'),
                'starting_bid': Decimal('250000.00'),
                'current_bid': Decimal('280000.00'),
                'status': 'bidding',
                'artist_name': 'Master Craftsman Saidi Mlawa',
                'year_created': 2024,
                'dimensions': '180cm x 15cm',
                'materials': 'Hardwood, Iron, Leather',
                'stock_quantity': 5,
                'featured': True,
                'nft_metadata': {'token_id': 'MKWSPEAR001', 'blockchain': 'ethereum'},
            },
            {
                'category': product_categories[1],
                'name': 'Hehe Royal Beaded Necklace',
                'description': 'Traditional beaded necklace worn by Hehe royalty, featuring intricate patterns in traditional colors. Each bead is carefully selected and hand-strung.',
                'product_type': 'physical',
                'price': Decimal('85000.00'),
                'artist_name': 'Mama Neema Kimayu',
                'year_created': 2024,
                'dimensions': '45cm length',
                'materials': 'Glass beads, Cotton thread, Brass clasp',
                'stock_quantity': 12,
                'featured': True,
            },
            {
                'category': product_categories[2],
                'name': 'Warrior\'s Traditional Cloth',
                'description': 'Handwoven cloth featuring traditional Hehe warrior patterns. Used in ceremonies and as traditional attire.',
                'product_type': 'physical',
                'price': Decimal('120000.00'),
                'artist_name': 'Mzee John Mtengule',
                'year_created': 2023,
                'dimensions': '200cm x 150cm',
                'materials': 'Cotton, Natural dyes',
                'stock_quantity': 8,
            },
            {
                'category': product_categories[3],
                'name': 'Ancient Battle Scene Pottery',
                'description': 'Large decorative pot depicting the famous Battle of Lugalo. Hand-painted with natural pigments.',
                'product_type': 'both',
                'price': Decimal('180000.00'),
                'starting_bid': Decimal('180000.00'),
                'status': 'bidding',
                'artist_name': 'Artist Grace Mwakalinga',
                'year_created': 2024,
                'dimensions': '60cm height x 40cm diameter',
                'materials': 'Clay, Natural pigments',
                'stock_quantity': 3,
                'featured': True,
                'nft_metadata': {'token_id': 'MKWPOT001', 'blockchain': 'polygon'},
            },
            {
                'category': product_categories[4],
                'name': 'Chief Mkwawa Portrait Carving',
                'description': 'Detailed wooden portrait of Chief Mkwawa II, carved from a single piece of mahogany by a master carver.',
                'product_type': 'physical',
                'price': Decimal('350000.00'),
                'artist_name': 'Master Carver Daniel Sapi',
                'year_created': 2024,
                'dimensions': '80cm x 50cm x 25cm',
                'materials': 'Mahogany wood',
                'stock_quantity': 2,
                'featured': True,
            },
            {
                'category': product_categories[5],
                'name': 'Kalenga Fortress at Sunset',
                'description': 'Contemporary painting depicting the historic Kalenga fortress during the golden hour. Oil on canvas.',
                'product_type': 'nft',
                'price': Decimal('450000.00'),
                'artist_name': 'Contemporary Artist Maria Ngowi',
                'year_created': 2024,
                'dimensions': '120cm x 90cm',
                'materials': 'Oil on canvas',
                'stock_quantity': 1,
                'featured': True,
                'nft_metadata': {'token_id': 'MKWART001', 'blockchain': 'ethereum'},
            },
            {
                'category': product_categories[1],
                'name': 'Traditional Hehe Bracelet Set',
                'description': 'Set of three matching bracelets with traditional Hehe patterns and colors.',
                'product_type': 'physical',
                'price': Decimal('45000.00'),
                'artist_name': 'Mama Amina Hassani',
                'year_created': 2024,
                'dimensions': 'Adjustable',
                'materials': 'Beads, Leather, Brass',
                'stock_quantity': 20,
            },
            {
                'category': product_categories[4],
                'name': 'Miniature Warrior Figurines Set',
                'description': 'Set of five hand-carved miniature Hehe warrior figurines in battle poses.',
                'product_type': 'physical',
                'price': Decimal('95000.00'),
                'artist_name': 'Carver Joseph Mkwawa',
                'year_created': 2024,
                'dimensions': '15cm height each',
                'materials': 'Ebony wood',
                'stock_quantity': 10,
            },
        ]

        products = []
        for prod_data in products_data:
            product = Product.objects.create(**prod_data)
            products.append(product)
            self.stdout.write(f'  ✓ Created product: {product.name}')

        # Seed Bids
        self.stdout.write('\nCreating Bids...')
        bidding_products = [p for p in products if p.status == 'bidding']
        bidder_names = ['Alice Moshi', 'Bob Kariuki', 'Carol Mwamba', 'Daniel Ouma', 'Eva Kibet']
        
        bid_count = 0
        for product in bidding_products:
            num_bids = random.randint(3, 8)
            current_bid = product.starting_bid if product.starting_bid else product.price
            
            for i in range(num_bids):
                current_bid += Decimal(random.randint(5000, 20000))
                bid = Bid.objects.create(
                    product=product,
                    bidder_name=random.choice(bidder_names),
                    bidder_email=f'bidder{bid_count}@example.com',
                    bidder_phone=f'+25571{random.randint(1000000, 9999999)}',
                    bid_amount=current_bid,
                    is_winning=(i == num_bids - 1),
                )
                bid_count += 1
            
            product.current_bid = current_bid
            product.save()

        self.stdout.write(f'  ✓ Created {bid_count} bids')

        # Seed Project Categories
        self.stdout.write('\nCreating Project Categories...')
        project_categories_data = [
            {
                'name': 'Agriculture & Farming',
                'description': 'Sustainable farming and agricultural development projects',
            },
            {
                'name': 'Water & Irrigation',
                'description': 'Water supply and irrigation infrastructure projects',
            },
            {
                'name': 'Education',
                'description': 'Educational facilities and programs',
            },
            {
                'name': 'Healthcare',
                'description': 'Health clinics and medical service projects',
            },
        ]

        proj_categories = []
        for cat_data in project_categories_data:
            category = ProjectCategory.objects.create(**cat_data)
            proj_categories.append(category)
            self.stdout.write(f'  ✓ Created category: {category.name}')

        # Seed Projects
        self.stdout.write('\nCreating Projects...')
        projects_data = [
            {
                'category': proj_categories[0],
                'title': 'Community Vegetable Farming Initiative',
                'description': 'Large-scale community vegetable farming project providing fresh produce to local markets. Currently growing cabbage, tomatoes, and French beans using modern farming techniques.',
                'objectives': 'Increase food security, Generate income for local farmers, Promote sustainable agriculture, Create employment opportunities',
                'location': 'Kalenga Village, Iringa',
                'start_date': date(2023, 3, 15),
                'end_date': date(2025, 12, 31),
                'budget': Decimal('25000000.00'),
                'progress_percentage': 65,
                'status': 'ongoing',
                'beneficiaries': 250,
                'featured': True,
                'impact_summary': 'Providing fresh vegetables to 250 families and creating 45 direct jobs.',
            },
            {
                'category': proj_categories[1],
                'title': 'Modern Irrigation System Installation',
                'description': 'Installation of a modern drip irrigation system to support year-round farming. The system will serve 50 hectares of farmland and benefit over 100 families.',
                'objectives': 'Enable year-round farming, Improve water efficiency, Increase crop yields, Support climate-resilient agriculture',
                'location': 'Kalenga Area, Iringa',
                'start_date': date(2024, 1, 10),
                'end_date': date(2024, 12, 31),
                'budget': Decimal('45000000.00'),
                'progress_percentage': 45,
                'status': 'ongoing',
                'beneficiaries': 120,
                'featured': True,
                'impact_summary': 'Serving 50 hectares of farmland with efficient irrigation.',
            },
            {
                'category': proj_categories[0],
                'title': 'Fish Farming & Aquaculture Project',
                'description': 'Establishment of fish ponds and aquaculture training center. The project includes 10 fish ponds and a training facility for sustainable fish farming practices.',
                'objectives': 'Provide protein source, Create income opportunities, Train community in aquaculture, Promote sustainable fishing',
                'location': 'Tungamalenga, Iringa',
                'start_date': date(2023, 6, 1),
                'end_date': date(2025, 6, 1),
                'budget': Decimal('35000000.00'),
                'progress_percentage': 70,
                'status': 'ongoing',
                'beneficiaries': 180,
                'featured': True,
                'impact_summary': 'Training 180 families in sustainable fish farming techniques.',
            },
            {
                'category': proj_categories[2],
                'title': 'Mkwawa Heritage Education Center',
                'description': 'Construction of an education center dedicated to teaching Hehe history and culture to young people. Includes classrooms, library, and cultural performance space.',
                'objectives': 'Preserve Hehe culture, Educate youth about heritage, Provide community gathering space, Promote cultural tourism',
                'location': 'Kalenga, Iringa',
                'start_date': date(2023, 9, 1),
                'end_date': date(2025, 8, 31),
                'budget': Decimal('55000000.00'),
                'progress_percentage': 55,
                'status': 'ongoing',
                'beneficiaries': 500,
            },
            {
                'category': proj_categories[3],
                'title': 'Rural Health Clinic Expansion',
                'description': 'Expansion of the Kalenga health clinic to serve more community members. Adding maternity ward and pharmacy.',
                'objectives': 'Improve healthcare access, Add maternity services, Establish pharmacy, Serve more patients',
                'location': 'Kalenga Village, Iringa',
                'start_date': date(2024, 2, 1),
                'end_date': date(2025, 1, 31),
                'budget': Decimal('38000000.00'),
                'progress_percentage': 35,
                'status': 'ongoing',
                'beneficiaries': 800,
            },
            {
                'category': proj_categories[0],
                'title': 'Beekeeping & Honey Production',
                'description': 'Training program and equipment provision for community beekeeping. Successfully established 200 modern beehives.',
                'objectives': 'Generate income through honey sales, Train beekeepers, Promote environmental conservation, Create sustainable livelihoods',
                'location': 'Iringa District',
                'start_date': date(2022, 5, 1),
                'end_date': date(2024, 4, 30),
                'budget': Decimal('15000000.00'),
                'progress_percentage': 100,
                'status': 'completed',
                'beneficiaries': 85,
                'impact_summary': 'Successfully trained 85 beekeepers and established 200 hives.',
            },
        ]

        for proj_data in projects_data:
            project = Project.objects.create(**proj_data)
            self.stdout.write(f'  ✓ Created project: {project.title}')

        # Seed Newsletter Subscribers
        self.stdout.write('\nCreating Newsletter Subscribers...')
        for i in range(50):
            Newsletter.objects.create(
                email=f'subscriber{i}@example.com',
                name=f'Subscriber {i}',
                is_active=random.choice([True, True, True, False]),
            )
        self.stdout.write('  ✓ Created 50 newsletter subscribers')

        # Seed Contact Messages
        self.stdout.write('\nCreating Contact Messages...')
        subjects = [
            'Inquiry about Museum Tours',
            'Booking Question',
            'Product Purchase Inquiry',
            'Partnership Opportunity',
            'Research Request',
            'General Information',
        ]
        
        for i in range(15):
            ContactMessage.objects.create(
                name=random.choice(visitor_names),
                email=f'contact{i}@example.com',
                phone=f'+25571{random.randint(1000000, 9999999)}',
                subject=random.choice(subjects),
                message=f'This is a test message {i} regarding various inquiries about the Mkwawa Heritage site and services.',
                is_read=random.choice([True, False]),
            )
        self.stdout.write('  ✓ Created 15 contact messages')

        self.stdout.write(self.style.SUCCESS('\n✓ Database seeding completed successfully!'))
        self.stdout.write(self.style.SUCCESS('\nSummary:'))
        self.stdout.write(f'  • Chiefs: {Chief.objects.count()}')
        self.stdout.write(f'  • Historical Events: {HistoricalEvent.objects.count()}')
        self.stdout.write(f'  • Tourism Sites: {TourismSite.objects.count()}')
        self.stdout.write(f'  • Bookings: {Booking.objects.count()}')
        self.stdout.write(f'  • Product Categories: {ProductCategory.objects.count()}')
        self.stdout.write(f'  • Products: {Product.objects.count()}')
        self.stdout.write(f'  • Bids: {Bid.objects.count()}')
        self.stdout.write(f'  • Project Categories: {ProjectCategory.objects.count()}')
        self.stdout.write(f'  • Projects: {Project.objects.count()}')
        self.stdout.write(f'  • Newsletter Subscribers: {Newsletter.objects.count()}')
        self.stdout.write(f'  • Contact Messages: {ContactMessage.objects.count()}')
