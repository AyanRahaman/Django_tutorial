document.addEventListener("DOMContentLoaded", function () {
    // Mobile menu toggle
    const burger = document.querySelector(".burger");
    const navLinks = document.querySelector(".nav-links");
    
    burger.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });

    // Smooth scrolling for internal links
    const links = document.querySelectorAll("nav ul li a, .btn");
    
    links.forEach(link => {
        link.addEventListener("click", function (e) {
            if (this.hash !== "") {
                e.preventDefault();
                const hash = this.hash;
                document.querySelector(hash).scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });

    // Simple Testimonials Auto-Scroll
    let testimonials = document.querySelectorAll(".testimonial");
    let index = 0;
    function showTestimonial() {
        testimonials.forEach((t, i) => {
            t.style.display = i === index ? "block" : "none";
        });
        index = (index + 1) % testimonials.length;
    }
    setInterval(showTestimonial, 3000);
    showTestimonial();
});