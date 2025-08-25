import { sidebarHandler } from "./module_internal/sidebar";
import { tabHandler } from "./module_internal/tab";

const main = () => {
  sidebarHandler()
  tabHandler()
}

document.addEventListener("DOMContentLoaded", main)