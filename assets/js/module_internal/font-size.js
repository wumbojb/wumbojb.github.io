import { $, $$, getLocalStorage, setLocalStorage } from "js/helper";

const KEY_FONT_SIZE = "site:font-size";

const applyFontSize = (size) => {
  const elHtml = document.documentElement;
  elHtml.style.setProperty("--md-font-default", `${size}px`);
  const radio = $(`input[name="font-size"][value="${size}"]`);
  if (radio) radio.checked = true;
  setLocalStorage(KEY_FONT_SIZE, size);
};

const optionFontSize = () => {
  const selected = $(`input[name="font-size"]:checked`);
  if (selected) {
    applyFontSize(selected.value);
  }
};

const initFontSize = () => {
  const storageSize = getLocalStorage(KEY_FONT_SIZE);
  if (!storageSize) {
    applyFontSize(14);
  } else {
    applyFontSize(storageSize);
  }
};

export const fontSizeHandler = () => {
  initFontSize();
  $$('input[name="font-size"]').forEach((el) => {
    el.addEventListener("change", optionFontSize);
  });
};
