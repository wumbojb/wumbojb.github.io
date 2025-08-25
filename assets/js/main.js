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
  const btnsClass = document.querySelectorAll(".tab-control__btn");

  btns.forEach((btn) => {
    const targetId = btn.getAttribute("data-tab");
    const tabPane = document.getElementById(targetId);
    const activeBtn = document.querySelector(`.tab-control__btn[data-tab="${targetId}"]`);

    btn.addEventListener("click", () => {
      btnsClass.forEach((e) => e.classList.remove("tab-control__btn--is-active"));
      activeBtn.classList.add("tab-control__btn--is-active");
      
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
