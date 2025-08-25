import { $ } from "js/helper";

const scAttr = (el, key, val) => {
  el.setAttribute(key, val);
};

export const giscus = (theme) => {
  const container = $(".discussion");
  if (!container) return;
  container.innerHTML = "";

  const script = document.createElement("script");
  script.src = "https://giscus.app/client.js";

  const data = container.dataset;
  scAttr(script, "data-repo", data.repo);
  scAttr(script, "data-repo-id", data.repoId);
  scAttr(script, "data-category", data.category);
  scAttr(script, "data-category-id", data.categoryId);
  scAttr(script, "data-mapping", data.mapping);
  scAttr(script, "data-strict", data.strict);
  scAttr(script, "data-reactions-enabled", data.reactionsEnabled);
  scAttr(script, "data-emit-metadata", data.emitMetadata);
  scAttr(script, "data-input-position", data.inputPosition);
  scAttr(script, "data-theme", theme);
  scAttr(script, "data-lang", document.documentElement.lang || data.lang);
  script.crossOrigin = "anonymous";
  script.async = true;

  container.appendChild(script);
};
