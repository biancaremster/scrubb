document.addEventListener('DOMContentLoaded', () => {
    // ===== Intersection Observer for scroll animations =====
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.anim-fade-up, .anim-fade-in-right').forEach(el => observer.observe(el));

    // ===== Header scroll effect =====
    const header = document.getElementById('site-header');
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;
        if (currentScroll > 60) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
        lastScroll = currentScroll;
    }, { passive: true });

    // ===== Mobile navigation toggle =====
    const mobileToggle = document.getElementById('mobile-toggle');
    const mobileNav = document.getElementById('mobile-nav');

    mobileToggle.addEventListener('click', () => {
        const isActive = mobileToggle.classList.toggle('active');
        mobileNav.classList.toggle('active');
        mobileToggle.setAttribute('aria-expanded', isActive);
        document.body.style.overflow = isActive ? 'hidden' : '';
    });

    // Close mobile nav on link click
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.addEventListener('click', () => {
            mobileToggle.classList.remove('active');
            mobileNav.classList.remove('active');
            mobileToggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        });
    });

    // ===== Smooth scroll for anchor links =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                e.preventDefault();
                const offset = 80;
                const top = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });

    // ===== Contact form feedback =====
    const form = document.getElementById('contact-form');
    const submitBtn = document.getElementById('contact-submit');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Sent! We\'ll be in touch ✓';
        submitBtn.style.background = '#8fa4c4';
        submitBtn.disabled = true;
        setTimeout(() => {
            submitBtn.textContent = originalText;
            submitBtn.style.background = '';
            submitBtn.disabled = false;
            form.reset();
        }, 3000);
    });

    // ===== Subtle parallax on hero decorations =====
    const heroCircle = document.querySelector('.hero-decoration--circle');
    const heroDots = document.querySelector('.hero-decoration--dots');

    if (heroCircle && heroDots) {
        window.addEventListener('mousemove', (e) => {
            const x = (e.clientX / window.innerWidth - 0.5) * 2;
            const y = (e.clientY / window.innerHeight - 0.5) * 2;
            heroCircle.style.transform = `translate(${x * 15}px, ${y * 15}px)`;
            heroDots.style.transform = `translate(${x * -10}px, ${y * -10}px)`;
        }, { passive: true });
    }
});
