import { $$, byId } from "../helper";

export const sidebarHandler = () => {
  $$("[data-sidebar]").forEach((btn) => {
    btn.addEventListener("click", () => {
      byId("sidebar").classList.toggle("sidebar--is-active");
    });
  });
};
