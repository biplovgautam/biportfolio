// Image Gallery Functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize image gallery
    initImageGallery();
});

function initImageGallery() {
    const gallery = document.querySelector('.image-gallery');
    if (!gallery) return;

    const slides = gallery.querySelectorAll('.gallery-slide');
    const thumbnails = gallery.querySelectorAll('.thumbnail');
    let currentSlide = 0;

    // Show initial slide
    showSlide(currentSlide);

    // Add click event to thumbnails
    thumbnails.forEach((thumbnail, index) => {
        thumbnail.addEventListener('click', () => {
            currentSlide = index;
            showSlide(currentSlide);
        });
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            previousSlide();
        } else if (e.key === 'ArrowRight') {
            nextSlide();
        }
    });

    // Auto-play functionality (optional)
    // let autoPlay = setInterval(nextSlide, 5000);

    // Pause auto-play on hover
    gallery.addEventListener('mouseenter', () => {
        // clearInterval(autoPlay);
    });

    gallery.addEventListener('mouseleave', () => {
        // autoPlay = setInterval(nextSlide, 5000);
    });

    function showSlide(index) {
        // Hide all slides
        slides.forEach(slide => slide.classList.remove('active'));
        thumbnails.forEach(thumb => thumb.classList.remove('active'));

        // Show current slide
        if (slides[index]) {
            slides[index].classList.add('active');
        }
        if (thumbnails[index]) {
            thumbnails[index].classList.add('active');
        }
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    function previousSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    }
}

// Smooth scroll for navigation links
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Lazy loading for images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
});

// Add loading states
function addLoadingState() {
    const buttons = document.querySelectorAll('.btn, .quick-link, .card-link');
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.href && !this.href.includes('#')) {
                this.style.opacity = '0.7';
                this.style.pointerEvents = 'none';
                
                setTimeout(() => {
                    this.style.opacity = '1';
                    this.style.pointerEvents = 'auto';
                }, 2000);
            }
        });
    });
}

// Initialize loading states
document.addEventListener('DOMContentLoaded', addLoadingState);
