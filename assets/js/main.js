const sidebarHandler = () => {
  document.querySelectorAll("[data-sidebar]").forEach((btn) => {
    const targetId = btn.getAttribute("data-sidebar");

    btn.addEventListener("click", () => {
      document.getElementById(targetId).classList.toggle("sidebar--is-active");
    });
  });
};

document.addEventListener("DOMContentLoaded", ()=>{
  sidebarHandler()
})