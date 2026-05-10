import os
import re

base_dir = "/Users/biancaremster/antigravity projects"
areas_dir = os.path.join(base_dir, "areas")

def expand_area_content(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract area name
    # <h1 class="area-hero-title anim-fade-up">Cleaning Services in<br><em>Zilker</em></h1>
    area_match = re.search(r'Cleaning Services in<br><em>(.*?)</em></h1>', content)
    area_name = area_match.group(1).strip() if area_match else "Austin"

    # Extract Zip
    zip_match = re.search(r'Zip Code (.*?)</p>', content)
    zip_code = zip_match.group(1).strip() if zip_match else ""

    # Remove existing additions if we are re-running
    content = re.sub(r'<section class="area-services">.*?</section>\s*<section class="area-faq">.*?</section>', '', content, flags=re.DOTALL)

    # Section B: Services Offered
    services_html = f"""
        <section class="area-services">
            <div class="container">
                <div class="editorial-header anim-fade-up">
                    <h2 class="section-title">Cleaning Services Offered in<br><em>{area_name}</em></h2>
                    <div class="editorial-line"></div>
                </div>
                <div class="services-grid">
                    <div class="service-item anim-fade-up" style="--delay: 0.1s">
                        <h3>Standard House Cleaning</h3>
                        <p>Perfect for keeping your {area_name} home consistently fresh. Includes dusting, vacuuming, mopping, and sanitizing kitchens and bathrooms.</p>
                    </div>
                    <div class="service-item anim-fade-up" style="--delay: 0.2s">
                        <h3>Deep Cleaning Service</h3>
                        <p>A thorough, top-to-bottom refresh. We focus on baseboards, inside appliances, and all those hard-to-reach spots that need extra care.</p>
                    </div>
                    <div class="service-item anim-fade-up" style="--delay: 0.3s">
                        <h3>Move-In / Move-Out Clean</h3>
                        <p>Moving in or out of {area_name}? We'll ensure the space is pristine for the next occupants or ready for your arrival.</p>
                    </div>
                </div>
            </div>
        </section>
    """

    # Section C: FAQ
    faq_html = f"""
        <section class="area-faq">
            <div class="container">
                <div class="editorial-header editorial-header--center anim-fade-up">
                    <h2 class="section-title">Common Questions About<br><em>{area_name} Cleaning</em></h2>
                    <div class="editorial-line"></div>
                </div>
                <div class="faq-container">
                    <details class="faq-details anim-fade-up" style="--delay: 0.1s">
                        <summary class="faq-summary">How much does house cleaning cost in {area_name}?</summary>
                        <div class="faq-content">
                            Pricing depends on your home's square footage and the type of service. Most {area_name} residents find our standard cleaning ranges from $120–$280.
                        </div>
                    </details>
                    <details class="faq-details anim-fade-up" style="--delay: 0.2s">
                        <summary class="faq-summary">Do you serve all of {zip_code}?</summary>
                        <div class="faq-content">
                            Yes! We cover the entire {area_name} neighborhood and all homes within the {zip_code} area, as well as surrounding neighborhoods.
                        </div>
                    </details>
                    <details class="faq-details anim-fade-up" style="--delay: 0.3s">
                        <summary class="faq-summary">Are your cleaning products safe for pets and kids?</summary>
                        <div class="faq-content">
                            Absolutely. We use eco-friendly, non-toxic products that are plant-derived and safe for your entire family, including pets.
                        </div>
                    </details>
                </div>
            </div>
        </section>
    """

    # Inject after <section class="area-why">...</section>
    pattern = r'(</section>\s*<section class="area-nearby">)'
    if re.search(pattern, content):
        content = re.sub(pattern, rf'{services_html}{faq_html}\1', content)
    else:
        # Fallback: find the last </section> before </main>
        content = content.replace('</main>', f'{services_html}{faq_html}\n</main>')

    with open(filepath, 'w') as f:
        f.write(content)

for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        expand_area_content(os.path.join(areas_dir, filename))

print("Area page content expanded with correct area names.")
