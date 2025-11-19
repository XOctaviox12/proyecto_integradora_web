document.addEventListener("DOMContentLoaded", () => {
  const bg = document.getElementById("bg-anim");

  // Cachea valores para NO recalcular layout 100 veces
  const maxW = window.innerWidth;
  const maxH = window.innerHeight;

  // Creamos un fragmento para insertar TODO de golpe (optimización real)
  const fragment = document.createDocumentFragment();

  for (let i = 0; i < 100; i++) {
    const star = document.createElement("div");
    star.classList.add("star");

    const size = Math.random() * 3;
    const top = Math.random() * maxH;
    const left = Math.random() * maxW;
    const duration = 2 + Math.random() * 3;

    // En lugar de cambiar estilos uno por uno → 1 solo reflow
    star.style.cssText = `
      width: ${size}px;
      height: ${size}px;
      top: ${top}px;
      left: ${left}px;
      animation-duration: ${duration}s;
      position: absolute;
    `;

    fragment.appendChild(star);
  }

  // Insertamos todo al DOM de una sola vez
  bg.appendChild(fragment);
});
