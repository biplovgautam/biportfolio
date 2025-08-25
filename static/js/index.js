document.addEventListener('DOMContentLoaded', () => {
  // Enhanced text animation for typing effect with smoother transitions
  const text = document.querySelector(".dynamic-text");
  if (text) {
      // Get phrases from data-words attribute if available, otherwise use defaults
      let phrases;
      if (text.dataset.words) {
          phrases = text.dataset.words.split(',').map(phrase => phrase.trim() + ".");
      } else {
          phrases = ["Full Stack Developer.", "AI Enthusiast.", "Web Designer.", "Problem Solver.", "Student."];
      }
      
      // Get wait time from data-wait attribute or default to 1500ms
      const waitTime = parseInt(text.dataset.wait || 1500);
      
      let currentPhrase = 0;
      let currentChar = 0;
      let isDeleting = false;
      let typingSpeed = 100;
      
      function typeEffect() {
          const currentText = phrases[currentPhrase];
          
          if (isDeleting) {
              text.textContent = currentText.substring(0, currentChar - 1);
              currentChar--;
              typingSpeed = 30 + Math.random() * 40; // Variable delete speed for natural feel
          } else {
              text.textContent = currentText.substring(0, currentChar + 1);
              currentChar++;
              typingSpeed = 70 + Math.random() * 50; // Variable typing speed for natural feel
          }
          
          // If word is complete, pause and then delete
          if (!isDeleting && currentChar === currentText.length) {
              isDeleting = true;
              typingSpeed = waitTime || 1500; // Use data-wait attribute or default to 1500ms
              
              // Add a subtle scale effect when complete
              text.style.transform = 'scale(1.03)';
              setTimeout(() => {
                  text.style.transform = 'scale(1)';
              }, 200);
          }
          
          // If deletion is complete, move to next word
          if (isDeleting && currentChar === 0) {
              isDeleting = false;
              currentPhrase = (currentPhrase + 1) % phrases.length;
              
              // Add a subtle fade effect between words
              text.style.opacity = '0.5';
              setTimeout(() => {
                  text.style.opacity = '1';
              }, 200);
          }
          
          setTimeout(typeEffect, typingSpeed);
      }
      
      // Start the typing effect
      setTimeout(typeEffect, 1000); // Small delay for initial appearance
  }
  
  // Enhanced sidebar behavior
  const sidebarNav = document.querySelector('.sidebar');
  const navLinks = document.querySelectorAll('.nav-link');
  
  if (sidebarNav) {
      // Adjust sidebar opacity based on scroll position
      window.addEventListener('scroll', () => {
          const scrollPosition = window.scrollY;
          if (scrollPosition > 300) {
              sidebarNav.style.backgroundColor = `rgba(var(--sidebar-bg-rgb), 0.8)`;
          } else {
              sidebarNav.style.backgroundColor = `rgba(var(--sidebar-bg-rgb), 0.85)`;
          }
      });
      
      // Add hover effect to sidebar
      sidebarNav.addEventListener('mouseenter', () => {
          sidebarNav.style.backgroundColor = `rgba(var(--sidebar-bg-rgb), 1)`;
          sidebarNav.style.boxShadow = '0 5px 25px var(--shadow-color)';
      });
      
      sidebarNav.addEventListener('mouseleave', () => {
          sidebarNav.style.backgroundColor = `rgba(var(--sidebar-bg-rgb), 0.85)`;
          sidebarNav.style.boxShadow = '0 5px 20px var(--shadow-color)';
      });
      
      // Improved smooth scrolling for all sidebar links
      navLinks.forEach(link => {
          link.addEventListener('click', function(e) {
              e.preventDefault();
              
              const targetId = this.getAttribute('href');
              const targetSection = document.querySelector(targetId);
              
              if (targetSection) {
                  // Get height of any fixed headers
                  const offset = 50;
                  const targetPosition = targetSection.offsetTop - offset;
                  
                  // Smooth scroll with easing
                  window.scrollTo({
                      top: targetPosition,
                      behavior: 'smooth'
                  });
                  
                  // Close mobile sidebar if open
                  if (window.innerWidth < 768 && sidebarNav.classList.contains('active')) {
                      sidebarNav.classList.remove('active');
                  }
              }
          });
      });
  }
  
  // Enhanced mobile menu toggle with overlay
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const sidebarOverlay = document.querySelector('.sidebar-overlay');
  
  if (mobileMenuBtn && sidebarNav) {
      // Toggle sidebar and overlay
      mobileMenuBtn.addEventListener('click', () => {
          sidebarNav.classList.toggle('active');
          sidebarOverlay.classList.toggle('active');
          mobileMenuBtn.classList.toggle('active');
          
          // Toggle icon between bars and times
          const icon = mobileMenuBtn.querySelector('i');
          if (icon) {
              if (icon.classList.contains('fa-bars')) {
                  icon.classList.remove('fa-bars');
                  icon.classList.add('fa-times');
              } else {
                  icon.classList.remove('fa-times');
                  icon.classList.add('fa-bars');
              }
          }
      });
      
      // Close sidebar when clicking the overlay
      sidebarOverlay.addEventListener('click', () => {
          sidebarNav.classList.remove('active');
          sidebarOverlay.classList.remove('active');
          mobileMenuBtn.classList.remove('active');
          
          // Reset icon
          const icon = mobileMenuBtn.querySelector('i');
          if (icon) {
              icon.classList.remove('fa-times');
              icon.classList.add('fa-bars');
          }
      });
      
      // Close sidebar when clicking the X in header
      const sidebarHeader = document.querySelector('.sidebar-header');
      if (sidebarHeader) {
          sidebarHeader.addEventListener('click', (e) => {
              // Check if the click is in the right part of the header (close button area)
              if (window.innerWidth <= 768 && e.clientX > sidebarHeader.getBoundingClientRect().width * 0.7) {
                  sidebarNav.classList.remove('active');
                  sidebarOverlay.classList.remove('active');
                  mobileMenuBtn.classList.remove('active');
                  
                  // Reset icon
                  const icon = mobileMenuBtn.querySelector('i');
                  if (icon) {
                      icon.classList.remove('fa-times');
                      icon.classList.add('fa-bars');
                  }
              }
          });
      }
      
      // Close sidebar when clicking navigation links on mobile
      const navLinks = document.querySelectorAll('.sidebar-nav .nav-link');
      navLinks.forEach(link => {
          link.addEventListener('click', () => {
              if (window.innerWidth <= 768) {
                  setTimeout(() => {
                      sidebarNav.classList.remove('active');
                      sidebarOverlay.classList.remove('active');
                      mobileMenuBtn.classList.remove('active');
                      
                      // Reset icon
                      const icon = mobileMenuBtn.querySelector('i');
                      if (icon) {
                          icon.classList.remove('fa-times');
                          icon.classList.add('fa-bars');
                      }
                  }, 300); // Small delay for better UX
              }
          });
      });
  }
  
  // Theme toggle enhancement with dark mode as default
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
      const themeIcon = themeToggle.querySelector('i');
      
      themeToggle.addEventListener('click', () => {
          document.body.classList.toggle('dark-mode');
          
          // Add rotation animation
          themeToggle.style.transform = 'rotate(360deg)';
          setTimeout(() => {
              themeToggle.style.transform = '';
          }, 500);
          
          if (document.body.classList.contains('dark-mode')) {
              themeIcon.className = 'fas fa-sun';
              localStorage.setItem('theme', 'dark');
          } else {
              themeIcon.className = 'fas fa-moon';
              localStorage.setItem('theme', 'light');
          }
      });
      
      // Default to dark mode unless specifically set to light
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme !== 'light') {
          document.body.classList.add('dark-mode');
          themeIcon.className = 'fas fa-sun';
          localStorage.setItem('theme', 'dark');
      }
  }
  
  // Blog image hover effect
  const blogCards = document.querySelectorAll('.blog-card');
  blogCards.forEach(card => {
      card.addEventListener('mouseenter', () => {
          const img = card.querySelector('.blog-image img');
          if (img) {
              img.style.transform = 'scale(1.05)';
          }
      });
      
      card.addEventListener('mouseleave', () => {
          const img = card.querySelector('.blog-image img');
          if (img) {
              img.style.transform = '';
          }
      });
  });
});
