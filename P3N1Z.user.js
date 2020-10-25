// ==UserScript==
// @name         Mein Skript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Disables Instagram Pop-up
// @author       Gnate
// @match        https://www.instagram.com/tg_socalkitties/
// @grant        none
// ==/UserScript==

function changeBody() {
        var body = document.getElementsByTagName("body")[0];
        body.style.overflow = "visible";
    }

changeBody();
