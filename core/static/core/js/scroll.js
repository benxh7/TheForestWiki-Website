/* Animacion para los textos del body al hacer scroll */
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.animate-up');

    // Creamos un array de umbrales de 0 a 1 en pasos de 0.01
    const thresholds = Array.from({ length: 101 }, (_, i) => i / 100);

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Aquí calculamos la transformación en función del intersectionRatio
            const ratio = entry.intersectionRatio;
            const minScale = 0.8;
            const scale = minScale + (1 - minScale) * ratio;
            const translateY = 50 * (1 - ratio);
            const opacity = ratio;

            entry.target.style.transform = `translateY(${translateY}px) scale(${scale})`;
            entry.target.style.opacity = opacity;
        });
    }, {
        threshold: Array.from({ length: 101 }, (_, i) => i / 100),
        rootMargin: "-100px 0px 0px 0px" // Ajusta este valor según la altura de la navbar
    });

    // Observamos cada elemento que tenga la clase .animate-up
    animatedElements.forEach(el => observer.observe(el));
});

/* Animacion para las categorias de la pagina */
const boxes = document.querySelectorAll('.box');

window.addEventListener('scroll', checkBoxes);
checkBoxes();
function checkBoxes() {
    const triggerBottom = window.innerHeight / 5 * 4; // Ajusta este valor según sea necesario
    boxes.forEach((box, idx) => {
        const boxTop = box.getBoundingClientRect().top;

        if (boxTop < triggerBottom) {
            box.classList.add('show');
        } else {
            box.classList.remove('show');
        }
    });
}