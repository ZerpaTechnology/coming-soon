#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!doctype html>\n<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->\n<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->\n<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class="no-js" lang="">\n<!--<![endif]-->\n\n<head>\n<meta charset="utf-8">\n<meta name="description" content="">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>ZERPATECHNOLOGY - Bootstrap Coming Soon template</title>\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/css/bootstrap.min.css">\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/css/main.css">\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/css/responsive.css">\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">\n<link rel="icon" type="image/png" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/logos/logoZtec.png" />\n</head>\n\n<body>\n\n<!--header section -->\n<section class="banner" role="banner">\n  <div class="banner-area"> \n    <!-- overlay -->\n    <div class="banner-area-gradient"></div>\n    <!-- overlay -->\n    <div class="inner-bg">\n      <div class="container">\n        <div class="col-md-10 col-md-offset-1">\n          <div class="banner-text text-center"> <a class="logo" href="#">ZERPATECHNOLOGY</a>\n            <h1>Coming soon</h1>\n            <!--Countdown -->\n            <div id="countdown"></div>\n            <!--Countdown --> \n            <a href="#subscribes" class="btn">Notify me</a>\n            </p>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n</section>\n<!--header section --> \n<!--intro section -->\n<section id="intro" class="section intro">\n  <div class="container">\n    <div class="row">\n      <div class="col-md-4 col-sm-6">\n        <div class="intro-content">\n          <h1>We'r forward-thinking agency to build amazing digital products.</h1>\n        </div>\n        \n        <!-- intro --> \n      </div>\n      <div class="col-md-7  col-md-offset-1 col-sm-6">\n        <div class="intro-content">\n          <h2>Welcome to ZERPATECHNOLOGY</h2>\n          <p>ZERPATECHNOLOGY is a professional, unique and modern HTML template for a creative agency, portfolio or general business. It can be used as your Coming Soon Page while the main site is under construction.</p>\n        </div>\n        \n        <!-- intro --> \n      </div>\n    </div>\n  </div>\n</section>\n<!--intro section --> \n<!--subscribe section -->\n<section id="subscribes" class="subscribe">\n  <div class="container">\n    <div class="row">\n      <div class="col-sm-12 col-md-5 subscribe-title">\n        <h2>Subscribe now.</h2>\n      </div>\n      \n      <!-- subscribe form -->\n      <div class="col-sm-12 col-md-7 subscribe-form"> \n               \n        <form method="post" action="php/subscribe.php" name="subscribeform" id="subscribeform">\n          <input type="text" name="email" placeholder="Enter your email address to get notified" id="subemail" />\n          <input type="submit" name="send" value="Notify me" id="subsubmit" class="btn2" />\n        </form>\n        \n        <!-- subscribe message -->\n        <div id="mesaj"></div>\n        <!-- subscribe message --> \n      </div>\n      <!-- subscribe form --> \n    </div>\n  </div>\n</section>\n<!--subscribe section --> \n\n<!-- Footer section -->\n<footer class="footer">\n  <div class="container">\n    <div class="row">\n      <div class="footer-col col-md-5">\n        <p>Copyright © 2015 ZERPATECHNOLOGY Inc. All Rights Reserved.</p>\n        <p> Made with <i class="fa fa-heart pulse"></i> by <a href="http://www.designstub.com/">Designstub</a></p>\n      </div>\n      <div class="footer-col col-md-7">\n        <ul class="footer-share">\n          <li><a href="#"><i class="fa fa-facebook"></i></a></li>\n          <li><a href="#"><i class="fa fa-twitter"></i></a></li>\n          <li><a href="#"><i class="fa fa-linkedin"></i></a></li>\n          <li><a href="#"><i class="fa fa-google-plus"></i></a></li>\n        </ul>\n      </div>\n    </div>\n  </div>\n  \n  <!-- footer top --> \n  \n</footer>\n<!-- Footer section --> \n\n<!-- JS files--> \n<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script> \n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/bootstrap.min.js"></script> \n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/jquery.backstretch.min.js"></script> \n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/jquery.countdown.js"></script> \n<script type="text/javascript" src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/jquery.subscribe.js"></script> \n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/main.js"></script>\n</body>\n</html>'''