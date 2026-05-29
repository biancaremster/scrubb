// ===== Dynamic hero padding: always clears the header (including logo bleed) =====
function setHeroPadding() {
    const header = document.getElementById('site-header');
    const hero   = document.querySelector('.hero--landing');
    if (!header || !hero) return;

    // getBoundingClientRect().bottom gives the actual rendered bottom edge,
    // including any logo that overflows below the navbar container.
    const headerBottom = header.getBoundingClientRect().bottom;
    const pad = Math.ceil(headerBottom) + 24; // 24px breathing room
    document.documentElement.style.setProperty('--hero-top-pad', pad + 'px');
}

// Run immediately and on every resize
setHeroPadding();
window.addEventListener('resize', setHeroPadding, { passive: true });

document.addEventListener('DOMContentLoaded', () => {
    // Re-run after fonts/images load (logo may shift layout)
    setHeroPadding();
    window.addEventListener('load', setHeroPadding);
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

    if (form && submitBtn) {
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
    }

    // ===== Quote lead form submission =====
    const leadForm = document.getElementById('hero-lead-form');
    if (leadForm) {
        leadForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Create a gorgeous notification toast
            showToast("We will message you back with an estimate or quote promptly!");
            
            leadForm.reset();
        });
    }

    // ===== Toast Notification Helper =====
    function showToast(message) {
        // Check if container exists, otherwise create it
        let container = document.getElementById('toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toast-container';
            document.body.appendChild(container);
        }
        
        const toast = document.createElement('div');
        toast.className = 'toast-box';
        toast.innerHTML = `
            <div class="toast-content">
                <svg class="toast-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                <span class="toast-message">${message}</span>
            </div>
        `;
        
        container.appendChild(toast);
        
        // Trigger transition
        setTimeout(() => {
            toast.classList.add('show');
        }, 10);
        
        // Keep it for 4.5 seconds, then fade out
        setTimeout(() => {
            toast.classList.remove('show');
            toast.classList.add('hide');
            // Remove from DOM after transition completes (800ms)
            setTimeout(() => {
                toast.remove();
            }, 800);
        }, 4500);
    }

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

    // ===== Chat widget toggle =====
    const chatButton    = document.getElementById('chat-button');
    const chatPopup     = document.getElementById('chat-popup');
    const chatClose     = document.getElementById('chat-close');
    const chatIconOpen  = document.getElementById('chat-icon-open');
    const chatIconClose = document.getElementById('chat-icon-close');

    let chatOpen = false;
    let autoShownOnce = false;

    function openChat() {
        chatOpen = true;
        chatPopup.classList.add('chat-popup--visible');
        chatButton.classList.add('is-open');
        chatButton.setAttribute('aria-expanded', 'true');
        chatIconOpen.style.display  = 'none';
        chatIconClose.style.display = 'block';
    }

    function closeChat() {
        chatOpen = false;
        chatPopup.classList.remove('chat-popup--visible');
        chatButton.classList.remove('is-open');
        chatButton.setAttribute('aria-expanded', 'false');
        chatIconOpen.style.display  = 'block';
        chatIconClose.style.display = 'none';
    }

    chatButton.addEventListener('click', () => {
        chatOpen ? closeChat() : openChat();
    });

    chatClose.addEventListener('click', () => closeChat());

    // Auto-show the popup once after 4 seconds (only on desktop/tablets > 768px)
    setTimeout(() => {
        if (window.innerWidth > 768 && !autoShownOnce && !chatOpen) {
            autoShownOnce = true;
            openChat();
            // Auto-dismiss after 8 more seconds if the user ignores it
            setTimeout(() => { if (chatOpen) closeChat(); }, 8000);
        }
    }, 4000);
});
