const bodyE = document.body;
const gNavMaskE = document.querySelector('.gNav-mask');
const gNavBeforeE = document.querySelector('#gNav-beforeE');
const gNavAfterE = document.querySelector('#gNav-afterE');
const gNavE = document.querySelector('.gNav');
const searchCharaInputE = document.querySelector('.searchCharaInput');
const gNavCloseBtn = document.querySelector('.gNav-closeBtn');
const gNavOpenBtn = document.querySelector('.gNav-openBtn');
const eExcludingHeader = document.querySelectorAll('body > *:not(header)');

function gNavOpen() {
bodyE.style.overflow = "hidden";
for(let i = 0; i < eExcludingHeader.length; i++) {
  eExcludingHeader[i].setAttribute("aria-hidden", "true");
}
gNavBeforeE.setAttribute("tabindex", "0");
gNavAfterE.setAttribute("tabindex", "0");
gNavMaskE.classList.add('gNav-mask-appear');
gNavE.classList.add('gNav-open');
gNavCloseBtn.style.display = "block";
window.setTimeout(() => {searchCharaInputE.focus();}, 200)

window.addEventListener('keydown', (e) => {
  if(e.keyCode === 27) {gNavClose();}
});
}

function gNavClose() {
bodyE.removeAttribute('style');
for(let i = 0; i < eExcludingHeader.length; i++) {
  eExcludingHeader[i].setAttribute("aria-hidden", "false");
}
gNavBeforeE.setAttribute("tabindex", "-1");
gNavAfterE.setAttribute("tabindex", "-1");
gNavMaskE.classList.remove('gNav-mask-appear');
gNavE.classList.remove('gNav-open');
gNavCloseBtn.style.display = "none";
gNavOpenBtn.focus();
}

function chgFocus(elem) {document.querySelector(elem).focus();}
