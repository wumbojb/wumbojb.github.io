const sidebarHandler = () => {
  document.querySelectorAll("[data-sidebar]").forEach((btn) => {
    const targetId = btn.getAttribute("data-sidebar");

    btn.addEventListener("click", () => {
      document.getElementById(targetId).classList.toggle("sidebar--is-active");
    });
  });
};

const tabHandler = () => {
  const btns = document.querySelectorAll("[data-tab]");

  btns.forEach((btn) => {
    const targetId = btn.getAttribute("data-tab");
    const tabPane = document.getElementById(targetId);

    btn.addEventListener("click", () => {
      document
        .querySelectorAll(".tab-pane")
        .forEach((e) => e.classList.remove("tab-pane--is-active"));
      tabPane.classList.add("tab-pane--is-active");
    });
  });
};

document.addEventListener("DOMContentLoaded", () => {
  sidebarHandler();
  tabHandler();
});
