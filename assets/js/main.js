import { handlerCopyCode } from "./module_internal/copy-code";
import { fontSizeHandler } from "./module_internal/font-size";
import { linkPreviewHandler } from "./module_internal/preview-link";
import { searchHandler } from "./module_internal/search";
import { sidebarHandler } from "./module_internal/sidebar";
import { tabHandler } from "./module_internal/tab";
import { themeHandler } from "./module_internal/theme";

const main = () => {
  sidebarHandler();
  tabHandler();
  themeHandler();
  fontSizeHandler();
  searchHandler();
  handlerCopyCode();
  linkPreviewHandler();
};

document.addEventListener("DOMContentLoaded", main);
