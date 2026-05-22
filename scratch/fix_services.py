import os

filepath = '/Users/biancaremster/antigravity projects/services.html'

with open(filepath, 'r') as f:
    content = f.read()

# Update Styles
old_styles = '''    <style>
        .page-hero { padding: 160px 0 80px; background: var(--charcoal); color: var(--cream); text-align: center; }
        .page-title { font-family: var(--font-display); font-size: 3.5rem; margin-bottom: 20px; }
        .page-subtitle { font-size: 1.2rem; opacity: 0.8; max-width: 600px; margin: 0 auto; }
        .services-section { padding: 80px 0; }
        .service-detail-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; margin-top: 60px; }
        .service-detail-card { padding: 40px; background: white; border-radius: 20px; border: 1px solid var(--border); transition: all 0.3s ease; }
        .service-detail-card:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.05); border-color: var(--pink-light); }
        .service-icon { font-size: 2.5rem; margin-bottom: 20px; }
        .service-detail-card h2 { font-family: var(--font-display); font-size: 1.8rem; margin-bottom: 16px; }
        .service-detail-card p { color: var(--slate); line-height: 1.7; margin-bottom: 24px; }
        .service-features { list-style: none; padding: 0; }
        .service-features li { padding: 8px 0; display: flex; align-items: center; gap: 10px; font-size: 0.95rem; color: var(--slate); }
        .service-features li::before { content: '✓'; color: var(--conversion); font-weight: bold; }
    </style>'''

new_styles = '''    <style>
        .page-hero { padding: 160px 0 80px; background: var(--blue-pale); color: var(--charcoal); text-align: center; border-bottom: 2px solid var(--charcoal); }
        .page-title { font-family: var(--font-display); font-size: 3.5rem; margin-bottom: 20px; }
        .page-subtitle { font-size: 1.2rem; color: var(--slate); max-width: 600px; margin: 0 auto; }
        .services-section { padding: 80px 0; }
        
        .service-detail-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; margin-top: 60px; }
        .service-detail-card { padding: 40px; background: white; border-radius: 4px; border: 2px solid var(--charcoal); box-shadow: 8px 8px 0px rgba(44,44,44,1); transition: all 0.3s ease; }
        .service-detail-card:hover { transform: translateY(-5px); box-shadow: 12px 12px 0px var(--pink); }
        
        .service-icon { 
            display: inline-flex; align-items: center; justify-content: center;
            width: 80px; height: 80px; margin-bottom: 24px;
            background: var(--pink-pale); border-radius: 50%;
            border: 2px solid var(--charcoal); box-shadow: 4px 4px 0px rgba(44,44,44,1);
            color: var(--pink); transition: all 0.3s var(--ease);
        }
        .service-detail-card:hover .service-icon { transform: rotate(-10deg) scale(1.1); box-shadow: 6px 6px 0px var(--charcoal); background: white; }
        .service-icon svg { width: 40px; height: 40px; }
        
        .service-detail-card h2 { font-family: var(--font-display); font-size: 1.8rem; margin-bottom: 16px; color: var(--charcoal); }
        .service-detail-card p { color: var(--slate); line-height: 1.7; margin-bottom: 24px; }
        
        .service-features { list-style: none; padding: 0; }
        .service-features li { padding: 8px 0; display: flex; align-items: center; gap: 10px; font-size: 0.95rem; color: var(--charcoal); font-weight: 500; }
        .service-features li::before { content: '★'; color: var(--pink); font-size: 1.1rem; }
        
        @media (max-width: 768px) {
            .service-detail-grid { grid-template-columns: 1fr; }
        }

        .services-cta { padding: 100px 0; }
        .services-cta-inner { background: var(--pink); padding: 80px 40px; border: 2px solid var(--charcoal); box-shadow: 12px 12px 0px rgba(44,44,44,1); border-radius: 4px; text-align: center; }
        .services-cta-title { font-family: var(--font-display); font-size: 3.5rem; color: var(--charcoal); margin-bottom: 20px; line-height: 1.1; }
        .services-cta-title em { font-family: var(--font-accent); color: var(--cream); font-style: italic; }
        .services-cta-body { font-size: 1.2rem; color: var(--charcoal); margin-bottom: 40px; font-weight: 500; }
        .services-cta-actions { display: flex; justify-content: center; gap: 20px; }
        .services-cta .btn--ghost { border-color: var(--charcoal); color: var(--charcoal); }
        .services-cta .btn--ghost:hover { background: var(--charcoal); color: var(--cream); box-shadow: 4px 4px 0px rgba(44,44,44,1); }
        .services-cta .btn--primary { background: var(--charcoal); color: var(--cream); border-color: var(--charcoal); }
        .services-cta .btn--primary:hover { background: var(--cream); color: var(--charcoal); box-shadow: 4px 4px 0px rgba(44,44,44,1); }
        
        @media (max-width: 600px) {
            .services-cta-actions { flex-direction: column; }
        }
    </style>'''

content = content.replace(old_styles, new_styles)

# Update CTA Section
old_cta = '''        <section class="area-cta" style="background: var(--warm-white); color: var(--charcoal); padding: 100px 0;">
            <div class="container">
                <div class="area-cta-inner">
                    <h2 class="area-cta-title" style="color: var(--charcoal);">Ready for a<br><em>Sparkling Space?</em></h2>
                    <p class="area-cta-body" style="color: var(--slate);">Get your free, no-obligation quote today. We'll respond within 2 hours.</p>
                    <div class="area-cta-actions">
                        <a href="index.html#contact" class="btn btn--primary">Get a Free Quote →</a>
                        <a href="tel:5125550123" class="btn btn--ghost" style="color: var(--charcoal); border-color: var(--border);">Or Call (512) 555-0123</a>
                    </div>
                </div>
            </div>
        </section>'''

new_cta = '''        <section class="services-cta">
            <div class="container">
                <div class="services-cta-inner">
                    <h2 class="services-cta-title">Ready for a<br><em>Sparkling Space?</em></h2>
                    <p class="services-cta-body">Get your free, no-obligation quote today. We'll respond within 2 hours.</p>
                    <div class="services-cta-actions">
                        <a href="index.html#contact" class="btn btn--primary">Get a Free Quote →</a>
                        <a href="tel:+15129620744" class="btn btn--ghost">Or Call (512) 962-0744</a>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old_cta, new_cta)

with open(filepath, 'w') as f:
    f.write(content)
print("Updated services.html")
