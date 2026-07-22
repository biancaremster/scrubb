import os
import re

BASE_DIR = '/Users/macbookprom42025/Paddock/Scrubb'
AREAS_DIR = os.path.join(BASE_DIR, 'areas')

def fix_sitemap():
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace .html in loc tags
    content = re.sub(r'<loc>https://scrubbatx\.com/(.*?)\.html</loc>', r'<loc>https://scrubbatx.com/\1</loc>', content)
    # Ensure referrals has no trailing slash
    content = content.replace('<loc>https://scrubbatx.com/referrals/</loc>', '<loc>https://scrubbatx.com/referrals</loc>')

    # Check for missing main service and faq pages
    missing_urls = [
        ('https://scrubbatx.com/services', '0.9'),
        ('https://scrubbatx.com/standard-house-cleaning', '0.9'),
        ('https://scrubbatx.com/signature-deep-cleaning', '0.9'),
        ('https://scrubbatx.com/faq', '0.8')
    ]

    for url, priority in missing_urls:
        if f'<loc>{url}</loc>' not in content:
            new_entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-05-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>
"""
            # Insert after referrals url block
            if '<loc>https://scrubbatx.com/referrals</loc>' in content:
                content = content.replace(
                    '</url>\n  <url>\n    <loc>https://scrubbatx.com/referrals</loc>',
                    f'</url>\n{new_entry}  <url>\n    <loc>https://scrubbatx.com/referrals</loc>'
                )
            else:
                content = content.replace('</urlset>', f'{new_entry}</urlset>')

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated sitemap.xml")

def fix_index():
    path = os.path.join(BASE_DIR, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update "@type": "LocalBusiness" -> "@type": ["HouseCleaning", "LocalBusiness"]
    content = content.replace('"@type": "LocalBusiness"', '"@type": ["HouseCleaning", "LocalBusiness"]')

    # 2. Add hasOfferCatalog to LocalBusiness schema if not present
    if '"hasOfferCatalog"' not in content:
        offer_catalog_snippet = """      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "House Cleaning Services",
        "itemListElement": [
          {
            "@type": "OfferCatalog",
            "name": "Standard Cleaning Services",
            "itemListElement": [
              {
                "@type": "Offer",
                "itemOffered": {
                  "@type": "Service",
                  "name": "Standard House Cleaning",
                  "description": "Regular maintenance cleaning covering dusting, vacuuming, mopping, kitchen surfaces, and bathroom sanitization."
                }
              }
            ]
          },
          {
            "@type": "OfferCatalog",
            "name": "Deep Cleaning Services",
            "itemListElement": [
              {
                "@type": "Offer",
                "itemOffered": {
                  "@type": "Service",
                  "name": "Signature Deep Cleaning",
                  "description": "Comprehensive top-to-bottom deep clean including baseboards, appliance interiors, and deep grout scrubbing."
                }
              }
            ]
          },
          {
            "@type": "OfferCatalog",
            "name": "Move-Out Cleaning Services",
            "itemListElement": [
              {
                "@type": "Offer",
                "itemOffered": {
                  "@type": "Service",
                  "name": "Apartment Move-Out Cleaning",
                  "description": "Detailed move-out cleaning tailored to fulfill lease requirements and secure security deposit refunds."
                }
              }
            ]
          }
        ]
      },
"""
        content = content.replace('"telephone": "+1-512-962-0744",', f'"telephone": "+1-512-962-0744",\n{offer_catalog_snippet}')

    # 3. Add theme-color if missing
    if 'name="theme-color"' not in content:
        content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                                  '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="theme-color" content="#2c2c2c">')

    # 4. Add og:image dimensions & alt if missing
    if 'og:image:width' not in content:
        og_dims = """    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="Scrubb ATX House Cleaning Services" />"""
        content = content.replace('<meta property="og:image" content="https://i.imgur.com/PSdNNW8.png" />',
                                  '<meta property="og:image" content="https://i.imgur.com/PSdNNW8.png" />\n' + og_dims)

    # 5. Fix internal links to clean URLs
    content = content.replace('href="services.html"', 'href="services"')
    content = content.replace('href="faq.html"', 'href="faq"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")

def fix_faq():
    path = os.path.join(BASE_DIR, 'faq.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean canonical & og:url
    content = content.replace('https://scrubbatx.com/faq.html', 'https://scrubbatx.com/faq')

    # Add theme-color
    if 'name="theme-color"' not in content:
        content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                                  '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="theme-color" content="#2c2c2c">')

    # Add Twitter cards if missing
    if 'name="twitter:card"' not in content:
        twitter_card = """    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Frequently Asked Questions | Scrubb ATX" />
    <meta name="twitter:description" content="Have questions about our cleaning services in Austin? Find answers about pricing, service areas, cleaning products, and booking." />
    <meta name="twitter:image" content="https://i.imgur.com/PSdNNW8.png" />
"""
        content = content.replace('<!-- Open Graph -->', twitter_card + '\n    <!-- Open Graph -->')

    # Add FAQPage Schema if missing
    if 'FAQPage' not in content:
        faq_schema = """
    <!-- FAQ Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How much does house cleaning cost in Austin?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pricing is based on the square footage of your home and the type of cleaning needed. Standard cleanings typically range from $140 to $260. Deep cleanings and move-out cleanings are priced higher due to the extra time and detail required. Contact us for a free estimate!"
          }
        },
        {
          "@type": "Question",
          "name": "What is included in a standard clean?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our standard clean covers all main living areas, including dusting reachable surfaces, vacuuming/mopping floors, cleaning kitchen counters and appliance exteriors, and sanitizing bathrooms."
          }
        },
        {
          "@type": "Question",
          "name": "What makes the \\\"Signature Deep Clean\\\" different?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The Signature Deep Clean includes everything in a standard clean plus hand-wiping baseboards, cleaning inside the microwave and oven, dusting ceiling fans/light fixtures, and deep scrubbing all tile grout and shower areas."
          }
        },
        {
          "@type": "Question",
          "name": "Are your cleaners background-checked and insured?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Every Scrubb ATX professional is background-checked, bonded, and fully insured for your peace of mind. We take the security of your home very seriously."
          }
        },
        {
          "@type": "Question",
          "name": "Are your cleaning products safe for pets and children?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Absolutely. We use non-toxic, eco-friendly cleaning agents that are safe for pets, children, and the environment while still being incredibly effective."
          }
        },
        {
          "@type": "Question",
          "name": "How far in advance do I need to book?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We typically recommend booking 3-7 days in advance, but we often have same-week availability. For move-out cleanings, booking 2 weeks in advance is recommended during peak moving seasons in Austin."
          }
        },
        {
          "@type": "Question",
          "name": "Do I need to be home during the cleaning?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No, you do not need to be home. Most of our clients provide a key or entry code. If you prefer to be home, that's fine too!"
          }
        },
        {
          "@type": "Question",
          "name": "What is your air conditioning (A/C) policy during hot months?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Air conditioning must be turned on and running at a comfortable temperature during hot summer months while our cleaning team is working in your home. Working in unconditioned high temperatures poses safety risks for our staff and impairs cleaning performance."
          }
        },
        {
          "@type": "Question",
          "name": "What is your cancellation policy?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We require at least two days (48 hours) prior notice for any cancellations or rescheduling. If you cancel or reschedule less than two days before your scheduled appointment, we will keep your deposit."
          }
        }
      ]
    }
    </script>
"""
        content = content.replace('</head>', faq_schema + '\n</head>')

    # Fix NAP phone in footer
    content = content.replace('(512) 555-0123', '(512) 962-0744')
    content = content.replace('+15125550123', '+15129620744')

    # Fix internal links
    content = content.replace('href="index.html#about"', 'href="/#about"')
    content = content.replace('href="index.html#service-areas"', 'href="/#service-areas"')
    content = content.replace('href="index.html#contact"', 'href="/#contact"')
    content = content.replace('href="index.html#booking"', 'href="/#booking"')
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="services.html"', 'href="services"')
    content = content.replace('href="standard-house-cleaning.html"', 'href="standard-house-cleaning"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated faq.html")

def fix_services():
    path = os.path.join(BASE_DIR, 'services.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean canonical & og:url
    content = content.replace('https://scrubbatx.com/services.html', 'https://scrubbatx.com/services')

    # Add theme-color
    if 'name="theme-color"' not in content:
        content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                                  '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="theme-color" content="#2c2c2c">')

    # Add Twitter cards if missing
    if 'name="twitter:card"' not in content:
        twitter_card = """    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Cleaning Services in Austin, TX | Scrubb ATX" />
    <meta name="twitter:description" content="Explore our professional cleaning services in Austin, TX. We offer standard cleaning, deep cleaning, and move-in/out cleaning." />
    <meta name="twitter:image" content="https://i.imgur.com/PSdNNW8.png" />
"""
        content = content.replace('<!-- Open Graph -->', twitter_card + '\n    <!-- Open Graph -->')

    # Add Service & Breadcrumb schema if missing
    if 'BreadcrumbList' not in content:
        services_schema = """
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://scrubbatx.com/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://scrubbatx.com/services"}
      ]
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "Cleaning Services",
      "serviceType": "House Cleaning",
      "provider": {
        "@type": "HouseCleaning",
        "name": "Scrubb ATX",
        "url": "https://scrubbatx.com/",
        "telephone": "+1-512-962-0744"
      },
      "areaServed": {"@type": "City", "name": "Austin", "addressRegion": "TX"}
    }
    </script>
"""
        content = content.replace('</head>', services_schema + '\n</head>')

    # Fix NAP phone in footer
    content = content.replace('(512) 555-0123', '(512) 962-0744')
    content = content.replace('+15125550123', '+15129620744')
    content = content.replace('tel:5125550123', 'tel:+15129620744')

    # Fix internal links
    content = content.replace('href="index.html#about"', 'href="/#about"')
    content = content.replace('href="index.html#service-areas"', 'href="/#service-areas"')
    content = content.replace('href="index.html#contact"', 'href="/#contact"')
    content = content.replace('href="index.html#booking"', 'href="/#booking"')
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="faq.html"', 'href="faq"')
    content = content.replace('href="standard-house-cleaning.html"', 'href="standard-house-cleaning"')
    content = content.replace('href="signature-deep-cleaning.html"', 'href="signature-deep-cleaning"')
    content = content.replace('href="apartment-move-out-cleaning.html"', 'href="apartment-move-out-cleaning"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated services.html")

def fix_service_detail_page(filename, title, desc, path_slug):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean canonical & og:url
    content = content.replace(f'https://scrubbatx.com/{filename}', f'https://scrubbatx.com/{path_slug}')

    # Add theme-color
    if 'name="theme-color"' not in content:
        content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                                  '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="theme-color" content="#2c2c2c">')

    # Add Twitter cards if missing
    if 'name="twitter:card"' not in content:
        twitter_card = f"""    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{desc}" />
    <meta name="twitter:image" content="https://i.imgur.com/PSdNNW8.png" />
"""
        content = content.replace('<!-- Open Graph -->', twitter_card + '\n    <!-- Open Graph -->')

    # Add Service & Breadcrumb schema if missing
    if 'BreadcrumbList' not in content:
        detail_schema = f"""
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://scrubbatx.com/"}},
        {{"@type": "ListItem", "position": 2, "name": "Services", "item": "https://scrubbatx.com/services"}},
        {{"@type": "ListItem", "position": 3, "name": "{title.split('|')[0].strip()}", "item": "https://scrubbatx.com/{path_slug}"}}
      ]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "{title.split('|')[0].strip()}",
      "serviceType": "House Cleaning",
      "provider": {{
        "@type": "HouseCleaning",
        "name": "Scrubb ATX",
        "url": "https://scrubbatx.com/",
        "telephone": "+1-512-962-0744"
      }},
      "areaServed": {{"@type": "City", "name": "Austin", "addressRegion": "TX"}}
    }}
    </script>
"""
        content = content.replace('</head>', detail_schema + '\n</head>')

    # Fix NAP phone in footer
    content = content.replace('(512) 555-0123', '(512) 962-0744')
    content = content.replace('+15125550123', '+15129620744')

    # Fix internal links
    content = content.replace('href="index.html#about"', 'href="/#about"')
    content = content.replace('href="index.html#service-areas"', 'href="/#service-areas"')
    content = content.replace('href="index.html#contact"', 'href="/#contact"')
    content = content.replace('href="index.html#booking"', 'href="/#booking"')
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="services.html"', 'href="services"')
    content = content.replace('href="faq.html"', 'href="faq"')
    content = content.replace('href="standard-house-cleaning.html"', 'href="standard-house-cleaning"')
    content = content.replace('href="signature-deep-cleaning.html"', 'href="signature-deep-cleaning"')
    content = content.replace('href="apartment-move-out-cleaning.html"', 'href="apartment-move-out-cleaning"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

def fix_referrals():
    path = os.path.join(BASE_DIR, 'referrals', 'index.html')
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove trailing slash from canonical & og:url to match vercel.json trailingSlash: false
    content = content.replace('https://scrubbatx.com/referrals/', 'https://scrubbatx.com/referrals')

    # Add theme-color
    if 'name="theme-color"' not in content:
        content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                                  '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="theme-color" content="#2c2c2c">')

    # Fix NAP phone
    content = content.replace('(512) 555-0123', '(512) 962-0744')
    content = content.replace('+15125550123', '+15129620744')

    # Fix internal nav links
    content = content.replace('href="../index.html#about"', 'href="/#about"')
    content = content.replace('href="../index.html#service-areas"', 'href="/#service-areas"')
    content = content.replace('href="../index.html#contact"', 'href="/#contact"')
    content = content.replace('href="../index.html#booking"', 'href="/#booking"')
    content = content.replace('href="../index.html"', 'href="/"')
    content = content.replace('href="../services.html"', 'href="/services"')
    content = content.replace('href="../faq.html"', 'href="/faq"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated referrals/index.html")

def fix_area_pages():
    for f_name in os.listdir(AREAS_DIR):
        if not f_name.endswith('.html'):
            continue
        path = os.path.join(AREAS_DIR, f_name)
        slug = f_name.replace('.html', '')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean canonical & og:url
        content = content.replace(f'https://scrubbatx.com/areas/{f_name}', f'https://scrubbatx.com/areas/{slug}')

        # Add theme-color
        if 'name="theme-color"' not in content:
            content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                                      '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="theme-color" content="#2c2c2c">')

        # Clean duplicate preloads in head
        content = re.sub(r'(\s*<!-- Preloads -->\s*<link rel="preload" href="\.\./logo\.png" as="image">\s*<link rel="preload" href="\.\./styles\.css" as="style">\s*){2,}',
                         r'\n    <!-- Preloads -->\n    <link rel="preload" href="../logo.png" as="image">\n    <link rel="preload" href="../styles.css" as="style">\n',
                         content)

        # Fix NAP phone
        content = content.replace('(512) 555-0123', '(512) 962-0744')
        content = content.replace('+15125550123', '+15129620744')

        # Fix internal links
        content = content.replace('href="../index.html#about"', 'href="/#about"')
        content = content.replace('href="../index.html#service-areas"', 'href="/#service-areas"')
        content = content.replace('href="../index.html#contact"', 'href="/#contact"')
        content = content.replace('href="../index.html#booking"', 'href="/#booking"')
        content = content.replace('href="../index.html"', 'href="/"')
        content = content.replace('href="../services.html"', 'href="/services"')
        content = content.replace('href="../faq.html"', 'href="/faq"')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    print("Updated 42 area pages")

if __name__ == '__main__':
    fix_sitemap()
    fix_index()
    fix_faq()
    fix_services()
    fix_service_detail_page('standard-house-cleaning.html',
                            'Standard House Cleaning Services in Austin, TX | Scrubb ATX',
                            'Keep your home fresh and tidy with our standard house cleaning services in Austin, TX. Vetted cleaners, eco-friendly products, and recurring schedules available.',
                            'standard-house-cleaning')
    fix_service_detail_page('signature-deep-cleaning.html',
                            'Signature Deep Cleaning Services in Austin, TX | Scrubb ATX',
                            'Transform your space with our signature deep cleaning services in Austin, TX. Detailed baseboard wiping, grout scrub, interior windows, and complete sanitation.',
                            'signature-deep-cleaning')
    fix_service_detail_page('apartment-move-out-cleaning.html',
                            'Apartment Move-Out Cleaning Services in Austin, TX | Scrubb ATX',
                            'Get your deposit back with our specialized apartment move-out cleaning services in Austin, TX. Thorough, efficient, and guaranteed to leave your place spotless.',
                            'apartment-move-out-cleaning')
    fix_referrals()
    fix_area_pages()
    print("SEO updates completed successfully!")
