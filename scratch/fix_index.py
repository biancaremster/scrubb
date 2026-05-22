import os

filepath = '/Users/biancaremster/antigravity projects/index.html'

with open(filepath, 'r') as f:
    content = f.read()

# 1. Hero text formatting
old_hero = '''                    <h1 class="hero-title hero-title--landing anim-fade-up" style="--delay: 0.1s">
                        Austin's Premier Cleaning Service — Transform Your Space from Chaos to Clean
                    </h1>
                    
                    <p class="hero-body hero-body--landing anim-fade-up" style="--delay: 0.2s">
                        Professional cleaning services in Austin, TX. <strong>Let us handle the chores for your home or business.</strong>
                    </p>'''

new_hero = '''                    <h1 class="hero-title hero-title--landing anim-fade-up" style="--delay: 0.1s">
                        Austin's Premier Cleaning Service<br>
                        <span class="hero-title-accent">— Transform Your Space</span><br>
                        from Chaos to Clean.
                    </h1>
                    
                    <p class="hero-body hero-body--landing anim-fade-up" style="--delay: 0.2s">
                        Professional cleaning services in Austin, TX.<br>
                        <strong>Let us handle the chores for your home or business.</strong>
                    </p>'''
content = content.replace(old_hero, new_hero)

# 2. Remove bg decorations in #about
old_about = '''        <section id="about" class="about">
            <div class="bg-decoration bg-decoration--dots" style="top: 10%; right: 5%; width: 400px; height: 400px; opacity: 0.5;" aria-hidden="true"></div>
            <div class="bg-decoration bg-decoration--circle" style="bottom: -150px; left: -150px; width: 500px; height: 500px;" aria-hidden="true"></div>
            <div class="container">'''
new_about = '''        <section id="about" class="about">
            <div class="container">'''
content = content.replace(old_about, new_about)

# 3. Fix duplicate FAQ
old_faq = '''                            <li><a href="faq.html">FAQ</a></li>
                            <li><a href="#">FAQ</a></li>'''
new_faq = '''                            <li><a href="faq.html">FAQ</a></li>'''
content = content.replace(old_faq, new_faq)

# 4. Phone numbers
content = content.replace('(512) 555-0123', '(512) 962-0744')
content = content.replace('tel:+15125550123', 'tel:+15129620744')
content = content.replace('"+1-512-555-0123"', '"+1-512-962-0744"')

# 5. Form wrapper in #contact
old_form = '''                <div class="contact-form-wrapper anim-fade-up" style="--delay: 0.2s">
                    <form class="lead-form" action="#" method="POST" onsubmit="event.preventDefault(); alert('Form submitted!');">
                        <div class="form-row">
                            <div class="form-group">
                                <label class="form-label" for="contact-name">First Name</label>
                                <input type="text" id="contact-name" class="form-input" placeholder="Your name" required>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="contact-phone">Phone Number</label>
                                <input type="tel" id="contact-phone" class="form-input" placeholder="(512) 000-0000" required>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="contact-email">Email Address</label>
                            <input type="email" id="contact-email" class="form-input" placeholder="you@example.com">
                        </div>
                        <button type="submit" class="btn btn--primary btn--full btn--submit">Get My Free Quote</button>
                    </form>
                </div>'''

new_form = '''                <div class="contact-form-wrapper anim-fade-up" style="--delay: 0.2s">
                    <div class="contact-form-card hero-form-card">
                        <form class="lead-form" action="#" method="POST" onsubmit="event.preventDefault(); alert('Form submitted!');">
                            <div class="form-row">
                                <div class="form-group">
                                    <label class="lead-label" for="contact-name">First Name <span class="required">*</span></label>
                                    <input type="text" id="contact-name" class="lead-input form-input" placeholder="Your name" required>
                                </div>
                                <div class="form-group">
                                    <label class="lead-label" for="contact-phone">Phone Number <span class="required">*</span></label>
                                    <input type="tel" id="contact-phone" class="lead-input form-input" placeholder="(512) 000-0000" required>
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="lead-label" for="contact-email">Email Address</label>
                                <input type="email" id="contact-email" class="lead-input form-input" placeholder="you@example.com">
                            </div>
                            <button type="submit" class="btn btn--primary btn--full btn--submit">Get My Free Quote</button>
                        </form>
                    </div>
                </div>'''
content = content.replace(old_form, new_form)

with open(filepath, 'w') as f:
    f.write(content)
print("Updated index.html safely.")
