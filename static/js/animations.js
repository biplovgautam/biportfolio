// Animation handling for the portfolio - optimized for performance
document.addEventListener('DOMContentLoaded', () => {
    // Initialize core components with performance checks
    if (document.getElementById('blobPath')) {
        // Only initialize blob animation if the element exists
        animateBlob();
    }
    
    // Use requestAnimationFrame for smoother animations
    requestAnimationFrame(() => {
        // Initialize Intersection Observer for scroll animations
        initIntersectionObserver();
        
        // Initialize staggered animations
        initScrollAnimations();
    });
});

// Enhanced blob animation for profile image
function animateBlob() {
    const blob = document.getElementById('blobPath');
    if (!blob) return;
    
    // Random points generator with smooth transitions
    const getRandomPoint = (min, max) => {
        return Math.random() * (max - min) + min;
    };
    
    // Create morphing blob path
    const createBlobPath = () => {
        // Create complex morphing shape with multiple points
        const numPoints = 8; 
        const angleStep = (Math.PI * 2) / numPoints;
        const radiusMin = 0.4;
        const radiusMax = 0.6;
        
        let points = [];
        
        for (let i = 0; i < numPoints; i++) {
            const angle = i * angleStep;
            const radius = getRandomPoint(radiusMin, radiusMax);
            
            const x = 0.5 + radius * Math.cos(angle);
            const y = 0.5 + radius * Math.sin(angle);
            
            points.push({ x, y });
        }
        
        // Create SVG path
        let path = `M${points[0].x},${points[0].y}`;
        
        for (let i = 1; i < points.length; i++) {
            // Use cubic bezier curves for smoother transitions
            const prevPoint = points[i - 1];
            const currentPoint = points[i];
            
            const cpX1 = prevPoint.x + (currentPoint.x - prevPoint.x) * 0.5;
            const cpY1 = prevPoint.y;
            const cpX2 = currentPoint.x - (currentPoint.x - prevPoint.x) * 0.5;
            const cpY2 = currentPoint.y;
            
            path += ` C${cpX1},${cpY1} ${cpX2},${cpY2} ${currentPoint.x},${currentPoint.y}`;
        }
        
        // Close the path with a smooth curve back to the first point
        const firstPoint = points[0];
        const lastPoint = points[points.length - 1];
        
        const cpX1 = lastPoint.x + (firstPoint.x - lastPoint.x) * 0.5;
        const cpY1 = lastPoint.y;
        const cpX2 = firstPoint.x - (firstPoint.x - lastPoint.x) * 0.5;
        const cpY2 = firstPoint.y;
        
        path += ` C${cpX1},${cpY1} ${cpX2},${cpY2} ${firstPoint.x},${firstPoint.y}`;
        path += ' Z';
        
        return path;
    };
    
    // Generate multiple random paths for animation
    const paths = [];
    for (let i = 0; i < 6; i++) {
        paths.push(createBlobPath());
    }
    
    // Add original circle path at start and end for smoother loop
    paths.unshift('M0.5,1 C0.776,1,1,0.776,1,0.5 C1,0.224,0.776,0,0.5,0 C0.224,0,0,0.224,0,0.5 C0,0.776,0.224,1,0.5,1 Z');
    paths.push('M0.5,1 C0.776,1,1,0.776,1,0.5 C1,0.224,0.776,0,0.5,0 C0.224,0,0,0.224,0,0.5 C0,0.776,0.224,1,0.5,1 Z');
    
    // Update animation values
    const pathsString = paths.join(';');
    blob.setAttribute('d', paths[0]);
    
    // Create keySplines for smoother animation
    const keySplines = Array(paths.length - 1).fill('0.42 0 0.58 1').join(';');
    
    // Set animation attributes
    const animate = blob.querySelector('animate') || document.createElementNS('http://www.w3.org/2000/svg', 'animate');
    animate.setAttribute('attributeName', 'd');
    animate.setAttribute('dur', '20000ms');
    animate.setAttribute('repeatCount', 'indefinite');
    animate.setAttribute('calcMode', 'spline');
    animate.setAttribute('keySplines', keySplines);
    animate.setAttribute('values', pathsString);
    
    if (!blob.querySelector('animate')) {
        blob.appendChild(animate);
    }
}

// Initialize intersection observer for section animations
function initIntersectionObserver() {
    const sections = document.querySelectorAll('.section');
    const staggerItems = document.querySelectorAll('.stagger-item');
    const fadeElements = document.querySelectorAll('.fade-in-up, .fade-in-left, .fade-in-right');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    // Observer for sections
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Animate children with staggered delay
                const childElements = entry.target.querySelectorAll('.animate-on-scroll');
                childElements.forEach((el, i) => {
                    setTimeout(() => {
                        el.classList.add('visible');
                    }, 100 + (i * 120));
                });
                
                sectionObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observer for staggered items
    const staggerObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Initialize styles
                if (!entry.target.style.transform) {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateY(30px) scale(0.95)';
                    entry.target.style.transition = 'all 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
                }
                
                setTimeout(() => {
                    entry.target.classList.add('stagger-visible');
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0) scale(1)';
                }, 150 + (index * 100));
                
                staggerObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observer for fade animations
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, 100);
                
                fadeObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Apply observers
    sections.forEach(section => sectionObserver.observe(section));
    staggerItems.forEach(item => staggerObserver.observe(item));
    fadeElements.forEach(element => fadeObserver.observe(element));
}

// Optimized scroll animations with better performance
function initScrollAnimations() {
    // Elements that should animate when scrolled into view - using one selector for better performance
    const animatedElements = document.querySelectorAll(
        '.fade-in-up, .fade-in-left, .fade-in-right, .section-header, ' + 
        '.project-card, .skill-card, .certification-card, .volunteer-card, ' +
        '.timeline-item, .blog-card, .stagger-item'
    );
    
    // Exit early if no elements to animate
    if (!animatedElements.length) return;
    
    // Configure the observer with optimized options
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Check if element is in viewport
            if (entry.isIntersecting) {
                // Simplify by just adding animated class
                entry.target.classList.add('animated');
                
                // Special handling for image animations
                if (entry.target.classList.contains('blog-card') || 
                    entry.target.classList.contains('project-card')) {
                    const img = entry.target.querySelector('img');
                    if (img) {
                        // Use requestAnimationFrame for smoother animation
                        requestAnimationFrame(() => {
                            img.style.transform = 'scale(1.02)';
                            setTimeout(() => {
                                img.style.transform = '';
                            }, 300);
                        });
                    }
                }
                
                // Stop observing once animated for performance
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15, // Slightly higher threshold for better timing
        rootMargin: '0px 0px -30px 0px' // Trigger a bit earlier
    });
    
    // Observe all animated elements
    animatedElements.forEach(el => {
        observer.observe(el);
    });
    
    // Special handling for staggered elements in containers
    const staggerContainers = document.querySelectorAll('.skills-container, .projects-container, .certifications-container, .volunteering-container, .blogs-container');
    
    staggerContainers.forEach(container => {
        const staggerObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const items = entry.target.querySelectorAll('.stagger-item');
                    
                    items.forEach((item, index) => {
                        // Stagger the animation of items inside a container
                        setTimeout(() => {
                            item.classList.add('animated');
                        }, 100 + (index * 100));
                    });
                    
                    staggerObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        staggerObserver.observe(container);
    });
}
