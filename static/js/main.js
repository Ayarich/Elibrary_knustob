/*=============== SCROLL REVEAL ANIMATION ===============*/
// window.sr = ScrollReveal({ reset: true });
const sr = ScrollReveal({
  origin: 'top',
  distance: '30px',
  duration: 800,
//    reset: true
}
);
sr.reveal(`.committee_description, .committee_name, .committee_members_container`, { interval: 300, delay: 500, })

sr.reveal(` .circles_container, .tl-container`, {
  origin: "bottom",
 

}); 
sr.reveal(`.executive_name, .executive_position`, {
  interval: 400,
  origin: "left",  delay:300,

});

// sr.reveal(``, {
//   delay: 100,   reset: false
 
// });