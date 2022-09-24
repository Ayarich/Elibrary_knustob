/*=============== SCROLL REVEAL ANIMATION ===============*/
window.sr = ScrollReveal({ reset: true });
const sr = ScrollReveal({
  origin: 'top',
  distance: '60px',
  duration: 800,
  
   reset: true
}
);
sr.reveal(` .committee_description, .committee_name`, { interval: 300, delay: 300, })
// sr.reveal(``, {
//   delay: 100,   reset: false
 
// });
sr.reveal(`.committee_members_container, .tl-container`, {
  origin: "left",

}); 
// sr.reveal(`.features,.p-box,.hero,.title,.about-description`, {
//   interval: 100,
//   origin: "left",reset: false

// });
