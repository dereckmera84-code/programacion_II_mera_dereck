document.addEventListener("DOMContentLoaded", () => {
const matriz = document.querySelector(".matriz-permisos");
if (!matriz) return;
const casillas = matriz.querySelectorAll("input[type=checkbox]");
const modelos = {
lectura: ["view"],
gestor: ["view", "add", "change"],
todo: ["view", "add", "change", "delete"],
nada: [],
};
const marcar = (acciones) => casillas.forEach((c) => (c.checked = acciones.includes(c.dataset.accion)));
matriz.querySelectorAll("[data-modelo]").forEach((boton) => {
boton.addEventListener("click", () => marcar(modelos[boton.dataset.modelo]));
});
});
