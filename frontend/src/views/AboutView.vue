<style>
/*

Template 2106 Soft Landing

http://www.tooplate.com/view/2106-soft-landing
	
*/
 
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400');

body {
  font-family: 'Open Sans', sans-serif;
  overflow-x: hidden;
  background: #f9f9f9;
}



/*---------------------------------------
   TYPOGRAPHY              
-----------------------------------------*/

h1,h2,h3,h4,h5,h6 {
  font-weight: 300;
  line-height: normal;
}

h1 {
  font-size: 3em;
}

h2 {
  color: #353535;
  font-size: 2em;
}

p {
  color: #757575;
  font-size: 14px;
  font-weight: normal;
  line-height: 24px;
}



/*---------------------------------------
   GENERAL               
-----------------------------------------*/

html{
  -webkit-font-smoothing: antialiased;
}

a {
  color: #202020;
  text-decoration: none !important;
}

a,
input, button,
.form-control {
  -webkit-transition: 0.5s;
  transition: 0.5s;
}

a:hover, a:active, a:focus {
  color: #29ca8e;
  outline: none;
}

::-webkit-scrollbar{
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-thumb {
  cursor: pointer;
  background: #202020;
}

.section-title {
  padding-bottom: 40px;
}

section {
  position: relative;
  padding: 100px 0;
}

#contact,
footer {
  background: #ffffff;
  text-align: center;
}

.overlay {
  background: #536976;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #292E49, #536976);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #292E49, #536976); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  opacity: 0.9;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.online-form {
  position: relative;
}

.online-form .form-control {
  border-color: #f0f0f0;
  display: inline-block;
  vertical-align: top;
  border-radius: 50px;
  box-shadow: none;
  height: 50px;
  margin-right: 0.5em;
  padding-left: 15px;
}

.online-form input[type="email"] {
  width: 60%;
}

.online-form button {
  background: #29ca8e;
  border: 0;
  color: #ffffff;
  position: absolute;
  right: 6em;
  width: 25%;
}

.online-form button:hover {
  background: #202020;
  color: #ffffff;
}



/*---------------------------------------
   BUTTONS               
-----------------------------------------*/

.section-btn {
  background: #29ca8e;
  border: 0;
  border-radius: 50px;
  color: #ffffff;
  font-size: 16px;
  font-weight: normal;
  padding: 12px 30px;
  transition: 0.5s 0.2s;
}

.section-btn:hover,
.section-btn:focus {
  background: #202020;
  color: #ffffff;
}



/*---------------------------------------
     PRE LOADER              
-----------------------------------------*/

.preloader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99999;
  display: flex;
  flex-flow: row nowrap;
  justify-content: center;
  align-items: center;
  background: none repeat scroll 0 0 #ffffff;
}

.spinner {
  border: 1px solid transparent;
  border-radius: 3px;
  position: relative;
}

.spinner:before {
  content: '';
  box-sizing: border-box;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 45px;
  height: 45px;
  margin-top: -10px;
  margin-left: -10px;
  border-radius: 50%;
  border: 1px solid #575757;
  border-top-color: #ffffff;
  animation: spinner .9s linear infinite;
}

@-webkit-@keyframes spinner {
  to {transform: rotate(360deg);}
}

@keyframes spinner {
  to {transform: rotate(360deg);}
}



/*---------------------------------------
    MENU              
-----------------------------------------*/

.custom-navbar {
  border: none;
  margin-bottom: 0;
  padding: 25px 0;
}

.custom-navbar .navbar-brand {
  color: #ffffff;
  font-size: 25px;
  font-weight: 500;
  letter-spacing: -1px;
}

.top-nav-collapse {
  background: #ffffff;
}

.custom-navbar .navbar-nav {
  margin-left: 6em;
}

.custom-navbar .nav li a {
  font-size: 16px;
  font-weight: normal;
  color: #f0f0f0;
  padding-right: 22px;
  padding-left: 22px;
}

.custom-navbar .nav li a:hover {
  background: transparent;
  color: #29ca8e;
}

.custom-navbar .navbar-nav > li > a:hover,
.custom-navbar .navbar-nav > li > a:focus {
  background-color: transparent;
}

.custom-navbar .nav li.active > a {
  background-color: transparent;
  color: #29ca8e;
}

.custom-navbar .navbar-toggle {
  border: none;
  padding-top: 10px;
}

.custom-navbar .navbar-toggle {
  background-color: transparent;
}

.custom-navbar .navbar-toggle .icon-bar {
  background: #29ca8e;
  border-color: transparent;
}

@media(min-width:768px) {
  .custom-navbar {
    border-bottom: 0;
    background: 0 0; 
  }

  .custom-navbar.top-nav-collapse {
    background: #ffffff;
    -webkit-box-shadow: 0 1px 30px rgba(0, 0, 0, 0.1);
    -moz-box-shadow: 0 1px 30px rgba(0, 0, 0, 0.1);
    box-shadow: 0 1px 30px rgba(0, 0, 0, 0.1);
    padding: 10px 0;
  }

  .top-nav-collapse .navbar-brand {
    color: #252525;
  }

  .top-nav-collapse .nav li a {
    color: #575757;
  }

  .top-nav-collapse .nav .section-btn a {
    color: #ffffff;
  }
}



/*---------------------------------------
    HOME          
-----------------------------------------*/

#home {
  background: url('../../../2106_soft_landing/images/home-bg.jpg') no-repeat center center;
  background-size: cover;
  vertical-align: middle;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  min-height: 100vh;
  position: relative;
  padding-top: 12em;
  text-align: center;
}

#home h1 {
  color: #ffffff;
  margin-top: 10px;
  margin-bottom: 40px;
}

.home-info {
  margin-top: 7em;
}

.home-info h3 {
  color: #f0f0f0;
  font-size: 11px;
  font-weight: bold;
  letter-spacing: 4px;
  text-transform: uppercase;
  margin: 10px 0;
}



/*---------------------------------------
    FEATURE              
-----------------------------------------*/

#feature {
  background: #ffffff;
}

#feature .nav-tabs {
  border-bottom: 0;
}

#feature .nav>li>a {
  padding: 8px 0;
}

#feature .nav-tabs>li>a {
  color: #999999;
  font-size: 18px;
  border: 0;
  border-bottom: 3px solid transparent;
  border-radius: 0;
  margin-right: 35px;
}

#feature .nav-tabs>li.active>a, 
#feature .nav-tabs>li.active>a:focus, 
#feature .nav-tabs>li.active>a:hover {
  background: transparent;
  color: #202020;
  border-bottom: 3px solid #29ca8e;
}

#feature .nav>li>a:focus, 
#feature .nav>li>a:hover {
  background: transparent;
  border-bottom: 3px solid #29ca8e;
  color: #202020;
}

#feature .tab-content {
  margin-top: 50px;
}

.tab-pane-item {
  margin: 20px 0;
}

.tab-pane-item h2 {
  margin: 0 0 5px 0;
}

.feature-image {
  position: absolute;
  bottom: -27em;
}



/*---------------------------------------
    ABOUT              
-----------------------------------------*/

#about .col-md-4 {
  margin: 0;
  padding: 0;
}

.team-thumb {
  background: #ffffff;
  position: relative;
  overflow: hidden;
}

.team-thumb-up:after {
  display: block;
  margin: 0 auto;
  position: absolute;
  top: -15px;
  right: 0;
  left: 0;
  content: "";
  width: 0;
  height: 0;
  border-right: 15px solid transparent;
  border-left: 15px solid transparent;
  border-bottom: 15px solid #ffffff;
}

.team-thumb-down:after {
  display: block;
  margin: 0 auto;
  position: absolute;
  bottom: -15px;
  right: 0;
  left: 0;
  content: "";
  width: 0;
  height: 0;
  border-right: 15px solid transparent;
  border-left: 15px solid transparent;
  border-top: 15px solid #ffffff;
}

.team-info {
  position: relative;
  padding: 40px;
}

.team-info h2 {margin: 0;}

.team-info small {
  display: block;
  font-size: 18px;
  margin: 5px 0 10px 0;
}

.team-thumb img {
  width: 100%;
}



/*---------------------------------------
    TESTIMONIAL           
-----------------------------------------*/

#testimonial {
  background: #ffffff;
}

#testimonial .col-md-6 {
  margin: 0;
  padding: 0;
}

#testimonial .section-title {
  padding-bottom: 0;
}

#testimonial h1 {
  color: #ffffff;
}

.testimonial-image {
  background: url('../../../2106_soft_landing/images/testimonial-image.jpg') no-repeat center center;
  background-size: cover;
  width: 100%;
  height: 65vh;
}

.testimonial-info {
  background: #202020;
  padding: 60px;
  height: 65vh;
}

.testimonial-info h3 {
  color: #d9d9d9;
  font-style: italic;
  margin-top: 5px;
}

.testimonial-info .item {
  display: block;
  width: 100%;
}

.testimonial-item {
  margin: 20px 0;
}

.owl-carousel .owl-item img,
.testimonial-item img,
.testimonial-item h4 {
  color: #d9d9d9;
  display: inline-block;
  vertical-align: top;
}

.owl-carousel .owl-item img,
.testimonial-item img {
  border: 3px solid #ffffff;
  border-radius: 100px;
  width: 60px;
  height: 60px;
  margin-right: 10px;
}



/*---------------------------------------
    PRICING             
-----------------------------------------*/

#about .section-title,
#pricing .section-title {
  text-align: center;
}

#pricing .col-md-4 {
  margin: 0;
  padding: 0;
}

#pricing .col-md-4:last-child .pricing-thumb {
  border-right: 0;
}

.pricing-thumb {
  background: #ffffff;
  border-right: 2px solid #f0f0f0;
  padding: 20px 40px;
}

.pricing-title {
  padding-bottom: 5px;
}

.pricing-info {
  border-top: 2px solid #f0f0f0;
  border-bottom: 2px solid #f0f0f0;
}

.pricing-info,
.pricing-bottom {
  padding: 20px 0;
}

.pricing-info p {
  font-size: 16px;
}

.pricing-bottom {
  position: relative;
}

.pricing-bottom span {
  font-size: 20px;
}

.pricing-btn {
  position: absolute;
  top: 15px;
  right: 0;
  display: inline-block;
}



/*---------------------------------------
    CONTACT             
-----------------------------------------*/

#contact-form .col-md-12,
#contact-form .col-md-4 {
  padding-left: 0;
}

#contact-form .form-control {
  background: transparent;
  border: 0;
  border-bottom: 3px solid #f0f0f0;
  border-radius: 0;
  box-shadow: none;
  margin: 10px 0;
}

#contact-form .form-control:focus {
  border-bottom-color: #202020;
}

#contact-form input {
  height: 50px;
}

#contact-form input[type='submit'] {
  background: #202020;
  border-radius: 50px;
  border: 0;
  color: #ffffff;
}

#contact-form input[type='submit']:hover {
  background: #29ca8e;
  color: #ffffff;
}



/*---------------------------------------
   FOOTER              
-----------------------------------------*/

footer {
  padding-bottom: 80px;
}

.copyright-text p {
  margin: 5px;
}



/*---------------------------------------
   SOCIAL ICON              
-----------------------------------------*/

.social-icon {
  position: relative;
  padding: 0;
  margin: 0;
}

.social-icon li {
  display: inline-block;
  list-style: none;
}

.social-icon li a {
  border-radius: 50px;
  color: #202020;
  font-size: 15px;
  width: 35px;
  height: 35px;
  line-height: 35px;
  text-decoration: none;
  text-align: center;
  position: relative;
  margin: 5px 5px 5px 0;
}

.social-icon li a:hover {
  background: #536976;
  color: #ffffff;
}



/*---------------------------------------
   RESPONSIVE STYLES              
-----------------------------------------*/

@media only screen and (max-width: 1200px) {

  .custom-navbar .navbar-nav {
    margin-left: 3em;
  }

  .home-info {
    margin-top: 0;
  }
}


@media only screen and (max-width: 992px) {

  section {
    padding: 60px 0;
  }

  .custom-navbar .navbar-nav {
    margin-left: 0;
  }

  .custom-navbar .nav li a {
    font-size: 14px;
    padding-right: 15px;
    padding-left: 15px;
  }

  #feature .nav-tabs>li>a {
    font-size: 16px;
    margin-right: 20px;
  }

  .feature-image {
    bottom: -24em;
  }

  .pricing-thumb {
    margin-bottom: 30px;
  }

  footer {
    padding-bottom: 40px;
  }
}


@media screen and (max-width: 767px) {

  .section-title {
    padding-bottom: 20px;
  }

  .custom-navbar {
    background: #ffffff;
    -webkit-box-shadow: 0 1px 30px rgba(0, 0, 0, 0.1);
    -moz-box-shadow: 0 1px 30px rgba(0, 0, 0, 0.1);
    box-shadow: 0 1px 30px rgba(0, 0, 0, 0.1);
    padding: 10px 0;
    text-align: center;
  }

  .custom-navbar .nav li a {
    line-height: normal;
    padding: 5px;
  }

  .custom-navbar .navbar-brand,
  .top-nav-collapse .navbar-brand {
    color: #202020;
    font-weight: normal;
  }

  .custom-navbar .nav li a,
  .top-nav-collapse .nav li a {
    color: #656565;
  }

  .feature-image {
    position: relative;
    bottom: 0;
  }

  #about .col-md-4:nth-child(3n) .team-thumb {
    display: flex;
    -webkit-box-orient: vertical;
    flex-direction: column-reverse;
    -webkit-flex-direction: column-reverse;
    -ms-flex-direction: column-reverse;
  }

  .team-thumb-down:after {
    top: -15px;
    bottom: inherit;
    border-top: inherit;
    border-bottom: 15px solid #ffffff;
  }

  .testimonial-image,
  .testimonial-info {
    height: 85vh;
  }

  .testimonial-info {
    padding: 30px;
  }
}


@media screen and (max-width: 480px) {

  .online-form input[type="email"],
  .online-form .form-control {
    width: 85%;
  }

  .online-form .form-control {
    display: block;
    margin: 20px auto;
  }

  .online-form button {
    position: relative;
    right: 0;
  }

  .testimonial-image,
  .testimonial-info {
    height: 65vh;
  }
}

</style>

<template>
<body>

<!-- PRE LOADER
<section class="preloader">
     <div class="spinner">

          <span class="spinner-rotate"></span>
          
     </div>
</section> -->


<!-- MENU -->
<section class="navbar custom-navbar navbar-fixed-top" role="navigation">
     <div class="container">

          <div class="navbar-header">
               <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon icon-bar"></span>
                    <span class="icon icon-bar"></span>
                    <span class="icon icon-bar"></span>
               </button>

               <!-- lOGO TEXT HERE -->
               <a href="index.html" class="navbar-brand">Soft Landing</a>
          </div>

          <!-- MENU LINKS -->
          <div class="collapse navbar-collapse">
               <ul class="nav navbar-nav">
                    <li><a href="#home" class="smoothScroll">Home</a></li>
                    <li><a href="#feature" class="smoothScroll">Features</a></li>
                    <li><a href="#about" class="smoothScroll">About us</a></li>
                    <li><a href="#pricing" class="smoothScroll">Pricing</a></li>
                    <li><a href="#contact" class="smoothScroll">Contact</a></li>
               </ul>
               <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">Say hello - <span>info@soft.co</span></a></li>
               </ul>
          </div>

     </div>
</section>


<!-- FEATURE -->
<section id="home" data-stellar-background-ratio="0.5">
     <div class="overlay"></div>
     <div class="container">
          <div class="row">

               <div class="col-md-offset-3 col-md-6 col-sm-12">
                    <div class="home-info">
                         <h3>professional landing page</h3>
                         <h1>We help you manage your website successfully!</h1>
                         <form action="" method="get" class="online-form">
                              <input type="email" name="email" class="form-control" placeholder="Enter your email" required="">
                              <button type="submit" class="form-control">Get started</button>
                         </form>
                    </div>
               </div>

          </div>
     </div>
</section>


<!-- FEATURE -->
<section id="feature" data-stellar-background-ratio="0.5">
     <div class="container">
          <div class="row">

               <div class="col-md-12 col-sm-12">
                    <div class="section-title">
                         <h1>What you get</h1>
                    </div>
               </div>

               <div class="col-md-6 col-sm-6">
                    <ul class="nav nav-tabs" role="tablist">
                         <li class="active"><a href="#tab01" aria-controls="tab01" role="tab" data-toggle="tab">Responsive</a></li>

                         <li><a href="#tab02" aria-controls="tab02" role="tab" data-toggle="tab">Mobile</a></li>

                         <li><a href="#tab03" aria-controls="tab03" role="tab" data-toggle="tab">Support</a></li>
                    </ul>

                    <div class="tab-content">
                         <div class="tab-pane active" id="tab01" role="tabpanel">
                              <div class="tab-pane-item">
                                   <h2>Minimal Design</h2>
                                   <p>Nam feugiat a ante sollicitudin luctus. Quisque eget placerat massa. Ut quis ligula ornare, pellentesque velit eget, vestibulum est. Donec pretium tristique elit eget sodales. Pellentesque posuere.</p>
                              </div>
                              <div class="tab-pane-item">
                                   <h2>Easy to use</h2>
                                   <p>Aliquam massa massa, consectetur non mattis fringilla, sodales ac turpis. Morbi ac felis sagittis, faucibus mauris vitae, placerat mauris.</p>
                              </div>
                         </div>


                         <div class="tab-pane" id="tab02" role="tabpanel">
                              <div class="tab-pane-item">
                                   <h2>Compatible Browsers</h2>
                                   <p>Nam maximus elit a metus luctus, a faucibus magna mattis. Ut malesuada viverra iaculis. Nunc euismod sit amet neque a tincidunt.</p>
                              </div>
                              <div class="tab-pane-item">
                                   <h2>User Friendly</h2>
                                   <p>Maecenas maximus velit lorem, quis pharetra turpis fringilla id. Vestibulum tempor facilisis efficitur. Sed nec nisi sit amet nibh pellentesque elementum.</p>
                              </div>
                              <div class="tab-pane-item">
                                   <h2>HTML5 & CSS3</h2>
                                   <p>In viverra ipsum ornare sapien rhoncus ullamcorper. Vivamus vitae risus ac mi vehicula sagittis. Nulla dictum magna sit amet pharetra aliquam.</p>
                              </div>
                         </div>

                         <div class="tab-pane" id="tab03" role="tabpanel">
                              <div class="tab-pane-item">
                                   <h2>Quick Support</h2>
                                   <p>Mauris rutrum est at fringilla pulvinar. Nam ligula urna, lobortis non scelerisque vel, molestie eu massa. Nullam mattis elit at tortor accumsan.</p>
                              </div>
                              <div class="tab-pane-item">
                                   <h2>Managed Stuffs</h2>
                                   <p>Quisque ullamcorper sem quis sapien cursus efficitur. Sed id sodales ipsum. Morbi eleifend tempus erat sit amet vehicula. Nulla at posuere tellus, non mattis erat. Nulla id massa gravida.</p>
                              </div>
                         </div>
                    </div>

               </div>

               <div class="col-md-6 col-sm-6">
                    <div class="feature-image">
                         <img src="../../2106_soft_landing/images/feature-mockup.png" class="img-responsive" alt="Thin Laptop">                             
                    </div>
               </div>

          </div>
     </div>
</section>


<!-- ABOUT -->
<section id="about" data-stellar-background-ratio="0.5">
     <div class="container">
          <div class="row">

               <div class="col-md-offset-3 col-md-6 col-sm-12">
                    <div class="section-title">
                         <h1>Professional Team for you</h1>
                    </div>
               </div>

               <div class="col-md-4 col-sm-4">
                    <div class="team-thumb">
                         <img src="../../2106_soft_landing/images/team-image1.jpg" class="img-responsive" alt="Andrew Orange">
                         <div class="team-info team-thumb-up">
                              <h2>Andrew Orange</h2>
                              <small>Art Director</small>
                              <p>Lorem ipsum dolor sit amet, consectetur adipisicing eiusmod tempor incididunt ut labore et dolore magna.</p>
                         </div>
                    </div>
               </div>

               <div class="col-md-4 col-sm-4">
                    <div class="team-thumb">
                         <div class="team-info team-thumb-down">
                              <h2>Catherine Soft</h2>
                              <small>Senior Manager</small>
                              <p>Lorem ipsum dolor sit amet, consectetur adipisicing eiusmod tempor incididunt ut labore et dolore magna.</p>
                         </div>
                         <img src="../../2106_soft_landing/images/team-image2.jpg" class="img-responsive" alt="Catherine Soft">
                    </div>
               </div>

               <div class="col-md-4 col-sm-4">
                    <div class="team-thumb">
                         <img src="../../2106_soft_landing/images/team-image3.jpg" class="img-responsive" alt="Jack Wilson">
                         <div class="team-info team-thumb-up">
                              <h2>Jack Wilson</h2>
                              <small>CEO / Founder</small>
                              <p>Lorem ipsum dolor sit amet, consectetur adipisicing eiusmod tempor incididunt ut labore et dolore magna.</p>
                         </div>
                    </div>
               </div>
               
          </div>
     </div>
</section>


<!-- TESTIMONIAL -->
<section id="testimonial" data-stellar-background-ratio="0.5">
     <div class="container">
          <div class="row">

               <div class="col-md-6 col-sm-12">
                    <div class="testimonial-image"></div>
               </div>

               <div class="col-md-6 col-sm-12">
                    <div class="testimonial-info">
                         
                         <div class="section-title">
                              <h1>What People Say</h1>
                         </div>

                         <div class="owl-carousel owl-theme">
                              <div class="item">
                                   <h3>Vestibulum tempor facilisis efficitur. Sed nec nisi sit amet nibh pellentesque elementum. In viverra ipsum ornare sapien rhoncus ullamcorper.</h3>
                                   <div class="testimonial-item">
                                        <img src="../../2106_soft_landing/images/tst-image1.jpg" class="img-responsive" alt="Michael">
                                        <h4>Michael</h4>
                                   </div>
                              </div>

                              <div class="item">
                                   <h3>Donec pretium tristique elit eget sodales. Pellentesque posuere, nunc id interdum venenatis, leo odio cursus sapien, ac malesuada nisl libero eget urna.</h3>
                                   <div class="testimonial-item">
                                        <img src="../../2106_soft_landing/images/tst-image2.jpg" class="img-responsive" alt="Sofia">
                                        <h4>Sofia</h4>
                                   </div>
                              </div>

                              <div class="item">
                                   <h3>Lorem ipsum dolor sit amet, consectetur adipisicing eiusmod tempor incididunt ut labore et dolore magna.</h3>
                                   <div class="testimonial-item">
                                        <img src="../../2106_soft_landing/images/tst-image3.jpg" class="img-responsive" alt="Monica">
                                        <h4>Monica</h4>
                                   </div>
                              </div>
                         </div>

                    </div>
               </div>
               
          </div>
     </div>
</section>


<!-- PRICING -->
<section id="pricing" data-stellar-background-ratio="0.5">
     <div class="container">
          <div class="row">

               <div class="col-md-12 col-sm-12">
                    <div class="section-title">
                         <h1>Choose any plan</h1>
                    </div>
               </div>

               <div class="col-md-4 col-sm-6">
                    <div class="pricing-thumb">
                        <div class="pricing-title">
                             <h2>Student</h2>
                        </div>
                        <div class="pricing-info">
                              <p>20 Responsive Designs</p>
                              <p>10 Dashboards</p>
                              <p>1 TB Storage</p>
                              <p>6 TB Bandwidth</p>
                              <p>24-hour Support</p>
                        </div>
                        <div class="pricing-bottom">
                              <span class="pricing-dollar">$200/mo</span>
                              <a href="#" class="section-btn pricing-btn">Register now</a>
                        </div>
                    </div>
               </div>

               <div class="col-md-4 col-sm-6">
                    <div class="pricing-thumb">
                        <div class="pricing-title">
                             <h2>Business</h2>
                        </div>
                        <div class="pricing-info">
                              <p>50 Responsive Designs</p>
                              <p>30 Dashboards</p>
                              <p>2 TB Storage</p>
                              <p>12 TB Bandwidth</p>
                              <p>15-minute Support</p>
                        </div>
                        <div class="pricing-bottom">
                              <span class="pricing-dollar">$350/mo</span>
                              <a href="#" class="section-btn pricing-btn">Register now</a>
                        </div>
                    </div>
               </div>

               <div class="col-md-4 col-sm-6">
                    <div class="pricing-thumb">
                        <div class="pricing-title">
                             <h2>Professional</h2>
                        </div>
                        <div class="pricing-info">
                              <p>100 Responsive Designs</p>
                              <p>60 Dashboards</p>
                              <p>5 TB Storage</p>
                              <p>25 TB Bandwidth</p>
                              <p>1-minute Support</p>
                        </div>
                        <div class="pricing-bottom">
                              <span class="pricing-dollar">$550/mo</span>
                              <a href="#" class="section-btn pricing-btn">Register now</a>
                        </div>
                    </div>
               </div>
               
          </div>
     </div>
</section>   


<!-- CONTACT -->
<section id="contact" data-stellar-background-ratio="0.5">
     <div class="container">
          <div class="row">

               <div class="col-md-offset-1 col-md-10 col-sm-12">
                    <form id="contact-form" role="form" action="" method="post">
                         <div class="section-title">
                              <h1>Say hello to us</h1>
                         </div>

                         <div class="col-md-4 col-sm-4">
                              <input type="text" class="form-control" placeholder="Full name" name="name" required="">
                         </div>
                         <div class="col-md-4 col-sm-4">
                              <input type="email" class="form-control" placeholder="Email address" name="email" required="">
                         </div>
                         <div class="col-md-4 col-sm-4">
                              <input type="submit" class="form-control" name="send message" value="Send Message">
                         </div>
                         <div class="col-md-12 col-sm-12">
                              <textarea class="form-control" rows="8" placeholder="Your message" name="message" required=""></textarea>
                         </div>
                    </form>
               </div>

          </div>
     </div>
</section>       


<!-- FOOTER -->
<footer id="footer" data-stellar-background-ratio="0.5">
     <div class="container">
          <div class="row">

               <div class="copyright-text col-md-12 col-sm-12">
                    <div class="col-md-6 col-sm-6">
                         <p>Copyright &copy; 2018 Company Name - Design:
                   <a rel="nofollow" href="http://tooplate.com">Tooplate</a></p>
                    </div>

                    <div class="col-md-6 col-sm-6">
                         <ul class="social-icon">
                              <li><a href="#" class="fa fa-facebook-square" attr="facebook icon"></a></li>
                              <li><a href="#" class="fa fa-twitter"></a></li>
                              <li><a href="#" class="fa fa-instagram"></a></li>
                         </ul>
                    </div>
               </div>

          </div>
     </div>
</footer>


<!-- SCRIPTS
<script src="js/jquery.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/jquery.stellar.min.js"></script>
<script src="js/owl.carousel.min.js"></script>
<script src="js/smoothscroll.js"></script>
<script src="js/custom.js"></script> -->

</body>
</template>

