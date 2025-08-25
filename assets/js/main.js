import { fontSizeHandler } from "./module_internal/font-size";
import { sidebarHandler } from "./module_internal/sidebar";
import { tabHandler } from "./module_internal/tab";
import { themeHandler } from "./module_internal/theme";

const main = () => {
  sidebarHandler()
  tabHandler()
  themeHandler()
  fontSizeHandler()
}

document.addEventListener("DOMContentLoaded", main)