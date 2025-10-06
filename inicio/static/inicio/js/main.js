document.addEventListener("DOMContentLoaded", () => {
  const bg = document.getElementById("bg-anim");

  // Crear estrellas dinámicamente
  for (let i = 0; i < 100; i++) {
    const star = document.createElement("div");
    star.classList.add("star");
    star.style.width = star.style.height = Math.random() * 3 + "px";
    star.style.top = Math.random() * window.innerHeight + "px";
    star.style.left = Math.random() * window.innerWidth + "px";
    star.style.animationDuration = 2 + Math.random() * 3 + "s";
    bg.appendChild(star);
  }
});
