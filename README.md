# E-library_knustob
## E-library is a platform for the KNUST Obuasi Campus

## To Run tailwindcss run the below code in the vs code terminal
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch

Or use ## *npm run build*

## For Scrolling animation, we are using ScrollReveal
<script src="https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js"></script>

##  Also we are usng Alpine.js library to control the navbar
<script defer src="https://unpkg.com/alpinejs@3.10.3/dist/cdn.min.js"></script>

## The Icon pack we are using is from FontAwesome
<script src="https://kit.fontawesome.com/a04dfe1eb8.js" crossorigin="anonymous"></script>


<!-- ICONS -->
home icon <i class="fa-solid fa-house"></i>
news icon <i class="fa-solid fa-newspaper"></i>
library icon <i class="fa-solid fa-book"></i>
location icon <i class="fa-solid fa-location-dot"></i>
videos icon <i class="fa-solid fa-video"></i>
committees icon <i class="fa-solid fa-people-group"></i>
executives icon <i class="fa-solid fa-user"></i>
contact us <i class="fa-solid fa-messages"></i>
calendar<i class="fa-solid fa-calendar-days"></i>
<i class="fa-solid fa-calendar"></i>
time icon <i class="fa-solid fa-clock"></i>
tools <i class="fa-solid fa-toolbox"></i>
<i class="fa-solid fa-rectangle-history"></i>
Download icon -  <i class="fa-solid fa-download"></i>


## Font api
<link href="https://api.fontshare.com/v2/css?f[]=erode@300,500,400&f[]=satoshi@900,700,300,901&display=swap" rel="stylesheet">
font-family: "Erode", "serif"; body-font
font-family: "Satoshi", "sans-serif"; heading font


<link href="https://api.fontshare.com/v2/css?f[]=nunito@600,400&f[]=bebas-neue@400&display=swap" rel="stylesheet">

font-family: "Nunito", "sans-serif"; body-font
font-family: "Bebas Neue", "sans-serif"; heading font

## I Just tried the erode font and it's great next is nunito

## Pre-loader
 <div class="wrapper">
    <div class="loader">
      <img src="../../static/img/src.png" alt="">
    </div>
  </div>


  ## Social media
  facebook -
  twitter - https://twitter.com/ObuasiSrc?t=dUHx0qViCac8meIzdJ0JLg&s=08
  email -
  instagram -
  youtube - 


<!-- Nav bar menu  -->
<div class="flex flex-col lg:flex-row lg:mx-1 lg:space-x-5 lg:mr-5 backdrop-blur-3xl ">
              <a class="src_nav_item" href="#">
                <i class="fa-solid fa-house"></i>
               <span class="nav-icon-text">Home</span>
              </a>
              <a class="src_nav_item" href="#">
                <i class="fa-solid fa-address-card"></i>
                <span class="nav-icon-text">About</span>
              </a>
              <a class="src_nav_item" href="#"><i class="fa-solid fa-newspaper"></i>
              <span class="nav-icon-text">News</span>
              </a>
              <a class="src_nav_item" href="#"><i class="fa-solid fa-book"></i>
                <span class="nav-icon-text">Library</span>
              </a>
              <a class="src_nav_item" href="#"><i class="fa-solid fa-message"></i>
              <span class="nav-icon-text">Contact Us</span>
            </a>
            <a class="src_nav_item" href="#">
              <i class="fa-solid fa-folder"></i>
              <span class="nav-icon-text">Resources</span>
            </a>
            </div>

            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"></svg>