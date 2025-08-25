import { $, $$, getLocalStorage, setLocalStorage } from "js/helper";
import { giscus } from "./giscus";

const KEY_THEME = "site:theme";

const applyTheme = (theme) => {
  const elHtml = document.documentElement;
  if (theme === "dark" || theme === "light") {
    elHtml.dataset.theme = theme;
    giscus(theme);
  } else if (theme === "auto") {
    const systemTheme = window.matchMedia("(prefers-color-scheme: dark)")
      .matches
      ? "dark"
      : "light";
    elHtml.dataset.theme = systemTheme;
    giscus(systemTheme);
  }

  const radio = $(`input[name="theme"][value="${theme}"]`);
  if (radio) radio.checked = true;
  setLocalStorage(KEY_THEME, theme);
};

const optionTheme = () => {
  const selected = $(`input[name="theme"]:checked`);
  if (selected) {
    applyTheme(selected.value);
  }
};

const initTheme = () => {
  const storageTheme = getLocalStorage(KEY_THEME);
  if (!storageTheme) {
    applyTheme("auto");
  } else {
    applyTheme(storageTheme);
  }
};

export const themeHandler = () => {
  initTheme();
  $$('input[name="theme"]').forEach((el) => {
    el.addEventListener("change", optionTheme);
  });
};
