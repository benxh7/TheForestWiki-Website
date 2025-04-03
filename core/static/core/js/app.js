const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;
const slideInterval = 5000; // 5 segundos

function showSlide(index) {
    // Actializamos los slides del slider
    slides.forEach((slide, i) => {
        slide.classList.toggle('active', i === index);
    });
    // Actualizamos los botones del slider
    dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
    });
    currentSlide = index;
}

function nextSlide() {
    let nextIndex = (currentSlide + 1) % slides.length;
    showSlide(nextIndex);
}

function prevSlide() {
    let prevIndex = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(prevIndex);
}

// slider automatico
let autoSlide = setInterval(nextSlide, slideInterval);

// Permite cambiar de slide al hacer clic en algun boton
dots.forEach(dot => {
    dot.addEventListener('click', () => {
        clearInterval(autoSlide); // Opcional: reinicia el intervalo al cambiar manualmente
        showSlide(parseInt(dot.getAttribute('data-index')));
        autoSlide = setInterval(nextSlide, slideInterval);
    });
});

// Navegacion con flechas
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

prevButton.addEventListener('click', () => {
    clearInterval(autoSlide);
    prevSlide();
    autoSlide = setInterval(nextSlide, slideInterval);
});

nextButton.addEventListener('click', () => {
    clearInterval(autoSlide);
    nextSlide();
    autoSlide = setInterval(nextSlide, slideInterval);
});