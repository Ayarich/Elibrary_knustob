/*=============== SCROLL REVEAL ANIMATION ===============*/
// window.sr = ScrollReveal({ reset: true });
const sr = ScrollReveal({
  origin: 'top',
  distance: '30px',
  duration: 800,
//    reset: true
}
);
sr.reveal(` .committee_description, .committee_name, .committee_members_container`, { interval: 300, delay: 500, })

sr.reveal(` .circles_container, .tl-container`, {
  origin: "bottom",

}); 
// sr.reveal(`.features,.p-box,.hero,.title,.about-description`, {
//   interval: 100,
//   origin: "left",reset: false

// });

// sr.reveal(``, {
//   delay: 100,   reset: false
 
// });