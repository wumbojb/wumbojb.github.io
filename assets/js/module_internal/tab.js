import { $, $$, byId } from "js/helper";

export const tabHandler = () => {
  $$("[data-tab]").forEach((btn) => {
    const targetId = btn.getAttribute("data-tab");

    btn.addEventListener("click", () => {
      $$(".tab-control__btn").forEach((e) => {
        e.classList.remove("tab-control__btn--is-active");
      });
      $(`.tab-control__btn[data-tab="${targetId}"]`).classList.add(
        "tab-control__btn--is-active",
      );

      $$(".tab-pane").forEach((e) => {
        e.classList.remove("tab-pane--is-active");
      });
      byId(targetId).classList.add("tab-pane--is-active");
    });
  });
};
