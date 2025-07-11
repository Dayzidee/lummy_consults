// Main JavaScript file for Lummy Consults

// Initialize when DOM is fully loaded
window.addEventListener('DOMContentLoaded', function() {
    // Initialize scroll animations
    initScrollAnimations();
    
    // Initialize form handlers
    initFormHandlers();
    
    // Initialize other interactive elements
    initInteractiveElements();
});

// Scroll animations using ScrollReveal
function initScrollAnimations() {
    if (typeof ScrollReveal !== 'undefined') {
        ScrollReveal().reveal('.hero-section', {
            duration: 1000,
            origin: 'top',
            distance: '100px',
            delay: 200
        });
        
        ScrollReveal().reveal('.service-card', {
            duration: 800,
            origin: 'bottom',
            distance: '50px',
            delay: 200,
            interval: 200
        });
        
        ScrollReveal().reveal('.about-text', {
            duration: 1000,
            origin: 'left',
            distance: '100px',
            delay: 300
        });
        
        ScrollReveal().reveal('.about-image', {
            duration: 1000,
            origin: 'right',
            distance: '100px',
            delay: 300
        });
        
        ScrollReveal().reveal('.testimonial-card', {
            duration: 800,
            origin: 'bottom',
            distance: '30px',
            delay: 100,
            interval: 200
        });
        
        ScrollReveal().reveal('.contact-section', {
            duration: 1000,
            origin: 'bottom',
            distance: '80px',
            delay: 200
        });
    }
}

// Form handlers
function initFormHandlers() {
    // Contact form handler
    const contactForm = document.querySelector('.contact-form form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            handleContactForm(this);
        });
    }
    
    // Add form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
            }
        });
    });
}

// Contact form submission
function handleContactForm(form) {
    const formData = new FormData(form);
    const name = formData.get('name');
    const email = formData.get('email');
    const message = formData.get('message');
    
    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;
    
    // Simulate form submission (replace with actual API call)
    setTimeout(() => {
        alert(`Thank you ${name}! Your message has been sent successfully.`);
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }, 1000);
}

// Form validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            showError(input, 'This field is required');
            isValid = false;
        } else {
            clearError(input);
        }
        
        // Email validation
        if (input.type === 'email' && input.value.trim()) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(input.value)) {
                showError(input, 'Please enter a valid email address');
                isValid = false;
            }
        }
    });
    
    return isValid;
}

// Show error message
function showError(input, message) {
    clearError(input);
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    errorDiv.style.color = 'red';
    errorDiv.style.fontSize = '14px';
    errorDiv.style.marginTop = '5px';
    input.parentNode.appendChild(errorDiv);
    input.style.borderColor = 'red';
}

// Clear error message
function clearError(input) {
    const errorDiv = input.parentNode.querySelector('.error-message');
    if (errorDiv) {
        errorDiv.remove();
    }
    input.style.borderColor = '';
}

// Initialize interactive elements
function initInteractiveElements() {
    // Smooth scrolling for anchor links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add hover effects to service cards
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Add loading animation for buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.type !== 'submit') {
                this.style.transform = 'scale(0.98)';
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 100);
            }
        });
    });
    
    // Add parallax effect to hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            heroSection.style.transform = `translateY(${rate}px)`;
        });
    }
    
    // Add counting animation to stats
    const stats = document.querySelectorAll('.stat h3');
    const animateStats = () => {
        stats.forEach(stat => {
            const target = parseInt(stat.textContent.replace('+', ''));
            let current = 0;
            const increment = target / 100;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                stat.textContent = Math.floor(current) + '+';
            }, 20);
        });
    };
    
    // Trigger stats animation when in view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                observer.unobserve(entry.target);
            }
        });
    });
    
    const aboutSection = document.querySelector('.about-section');
    if (aboutSection) {
        observer.observe(aboutSection);
    }
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add loading overlay
function showLoading() {
    const overlay = document.createElement('div');
    overlay.id = 'loading-overlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    `;
    overlay.innerHTML = '<div style="color: white; font-size: 20px;">Loading...</div>';
    document.body.appendChild(overlay);
}

function hideLoading() {
    const overlay = document.getElementById('loading-overlay');
    if (overlay) {
        overlay.remove();
    }
}

// Export functions for global use
window.LummyConsults = {
    showLoading,
    hideLoading,
    validateForm,
    debounce
};

