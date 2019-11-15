/*
Project name:       Hauslr
File name:          Custom JS
*/

"use strict";


jQuery(window).on("load", function() { // makes sure the whole site is loaded
    jQuery('#preloader').delay(350).hide('slow'); // will fade out the white DIV that covers the website.
    jQuery('body').addClass('page-loaded'); // will fade out the white DIV that covers the website.
    jQuery('.amaezi-page-loader').delay(350).hide('slow'); // will fade out the white DIV that covers the website.
});  


jQuery( document ).ready(function() {
    "use strict";

    /* 
    ###############################################
    BOOKING SUPER PLACEHOLDERS
    ############################################### 
    */
    //Add Super placeholder text for booking email field
    if (jQuery( "#contactEmail" ).length) {
        superplaceholder({
            el: contactEmail,
            sentences: [ 'Type in your email', 'Eg. hello@fundraising.tld' ],
            options: {
                loop: true,
                letterDelay: 30
            }
        })
    }
    //Add Super placeholder text for booking date field
    if (jQuery( "#contactPhone" ).length) {
        superplaceholder({
            el: contactPhone,
            sentences: [ 'Type in your phone', 'Eg. 345-3451-345' ],
            options: {
                loop: true,
                letterDelay: 30
            }
        })
    }
    //Add Super placeholder text for booking name field
    if (jQuery( "#contactName" ).length) {
        superplaceholder({
            el: contactName,
            sentences: [ 'Type in your full name', 'Eg. Marco Pollo' ],
            options: {
                loop: true,
                letterDelay: 30
            }
        })
    }


    /* 
    ###############################################
    SLIDING MENU
    ############################################### 
    */
    jQuery('.sliding-menu').removeClass('hidden');


    /* 
    ###############################################
    Begin: Food Menu
    ############################################### 
    */
    var Menu = (function() {
        var $container = jQuery( '#menu-container' ),                       
            $cover = $container.find( 'div.menu-cover' ),
            $middle = $container.find( 'div.menu-middle' ),
            $right = $container.find( 'div.menu-right' ),
            $details = $container.find( 'a.viewdetails' ),

            init = function() {

                initEvents();

            },
            initEvents = function() {

                $details.on( 'click', function( event ) {

                    $container.removeClass( 'menu-in' ).children( 'div.food-modal' ).remove();
                    viewDetails( jQuery( this ) );
                    return false;

                } );
                
            },
            viewDetails = function( recipe ) {

                var title = recipe.text(),
                    img = recipe.data( 'thumb' ),
                    description = recipe.parent().next().text(),
                    url = recipe.attr( 'href' );

                var $modal = jQuery( '<div class="food-modal"><div class="rm-thumb" style="background-image: url(' + img + ')"></div><h5>' + title + '</h5><p>' + description + '</p><a href="' + url + '">See the recipe</a><span class="rm-close-modal">x</span></div>' );

                $modal.appendTo( $container );

                var h = $modal.outerHeight( true );
                $modal.css( 'margin-top', -h / 2 );

                setTimeout( function() {

                    $container.addClass( 'menu-in rm-nodelay' );

                    $modal.find( 'span.rm-close-modal' ).on( 'click', function() {

                        $container.removeClass( 'menu-in' );

                    } );
                
                }, 0 );

            };

        return { init : init };

    })();
    /*End: Food Menu */



    /* 
    ###############################################
    Video YT Header
    ############################################### 
    */
    /*Begin: Video YT */
    function mobilecheck() {
        var check = false;
        (function(a){if(/(android|ipad|playbook|silk|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))check = true})(navigator.userAgent||navigator.vendor||window.opera);
        return check;
    }
    if ( !mobilecheck() ) {
        jQuery(".player").mb_YTPlayer({
            onReady: function(){
                jQuery('.sound').removeClass('hidden');
                jQuery( ".sound" ).on( "click", function(evt) {
                    evt.preventDefault();
                    if(jQuery('.sound').hasClass('off')){
                        jQuery('.sound').removeClass('off');
                        jQuery('.player').unmuteYTPVolume();
                        jQuery('.sound').addClass('on');
                        jQuery('.title').fadeOut();
                        jQuery('.travelogue-icon-sound').removeClass('fa-volume-off');
                        jQuery('.travelogue-icon-sound').addClass('fa-volume-up');
                    }else{
                        if(jQuery('.sound').hasClass('on')){
                            jQuery('.sound').removeClass('on');
                            jQuery('.player').muteYTPVolume();    
                            jQuery('.sound').addClass('off');
                            jQuery('.title').fadeIn();
                            jQuery('.travelogue-icon-sound').removeClass('fa-volume-up');
                            jQuery('.travelogue-icon-sound').addClass('fa-volume-off');
                        }
                    }           
                });
            }
        });
        jQuery('.player').on("YTPStart",function(){
           jQuery('.youtube-video').animate({opacity: 1}, 5000,function(){});
        });
    }
    /*End: Video YT */



    /* 
    ###############################################
    Bootstrap tooltip
    ############################################### 
    */
    /*Begin: tooltip */
    jQuery(function () {
        jQuery('[data-toggle="tooltip"]').tooltip()
    })
    /*End: tooltip */


    /* 
    ###############################################
    Swipebox Gallery
    ############################################### 
    */
    /*Begin: Swipebox */
    if (jQuery( ".swipebox" ).length) {
        jQuery( '.swipebox' ).swipebox();
    }
    /*End: Swipebox */


    /* 
    ###############################################
    SLIDERS
    ############################################### 
    */
    /*Begin: Header subtitle slider*/
    jQuery(".header-banners-slider").owlCarousel({
        navigation      : false, // Show next and prev buttons
        pagination      : false,
        autoPlay        : true,
        slideSpeed      : 2000,
        paginationSpeed : 2000,
        transitionStyle : "fade",
        singleItem      : true
    });

    /*Begin: Header subtitle slider*/
    jQuery(".photo-slider").owlCarousel({
        navigation      : false, // Show next and prev buttons
        pagination      : true,
        autoPlay        : true,
        slideSpeed      : 800,
        paginationSpeed : 800,
        transitionStyle : "fadeUp",
        singleItem      : true
    });

    /*Begin: testimonials slider*/
    jQuery(".testimonials_slider").owlCarousel({
        navigation      : false, // Show next and prev buttons
        pagination      : false,
        items           : 2,
        slideSpeed      : 800,
        paginationSpeed : 800,
    });
    /*Begin: instagram slider*/
    jQuery(".instagram_slider").owlCarousel({
        navigation      : false, // Show next and prev buttons
        pagination      : false,
        autoPlay        : true,
        slideSpeed      : 100,
        paginationSpeed : 100,
        transitionStyle : "fadeUp",
        items           : 4
    });

    /* 
    ###############################################
    TOGGLE MENUS
    ############################################### 
    */
    var accordionsMenu = jQuery('.theme-accordion-menu');
    if( accordionsMenu.length > 0 ) {
        
        accordionsMenu.each(function(){
            var accordion = jQuery(this);
            //detect change in the input[type="checkbox"] value
            accordion.on('change', 'input[type="checkbox"]', function(){
                var checkbox = jQuery(this);
                ( checkbox.prop('checked') ) ? checkbox.siblings('ul').attr('style', 'display:none;').slideDown(300) : checkbox.siblings('ul').attr('style', 'display:block;').slideUp(300);
            });
        });
    }



    /* 
    ###############################################
    Mailchimp subscribe form
    ############################################### 
    */
    jQuery('.subscribe').ketchup().submit(function(evt) {
        evt.preventDefault();
        if (jQuery(this).ketchup('isValid')) {
            var action = jQuery(this).attr('action');

            jQuery.ajax({
                url: action,
                type: 'POST',
                data: {
                    email: jQuery('.address').val()
                },
                success: function(data){
                    jQuery('#result').html(data).css('color', '#35cf76');
                },
                error: function() {
                    jQuery('.result').html('Sorry, an error occurred.').css('color', '#e74c3c');
                }
            });
        }else{
            jQuery('.result').html('Invalid email address.').css('color', '#e74c3c');
        }
        return false;
    });
    //End: MailChimp JS


    /* 
    ###############################################
    One Page Scrolling
    ############################################### 
    */
    jQuery(function(){
      jQuery.scrollIt({
          upKey:        38,         // key code to navigate to the next section
          downKey:      40,         // key code to navigate to the previous section
          easing:       'linear',   // the easing function for animation
          scrollTime:   1000,       // how long (in ms) the animation takes
          activeClass:  'active',   // class given to the active nav element
          onPageChange: null,       // function(pageIndex) that is called when page is changed
          topOffset:    -60         // offste (in px) for fixed top navigation
        });
    });



    /* 
    ###############################################
    LOVE POST - GALLERY
    ############################################### 
    */
    jQuery( ".love-post .fa-heart-o" ).on( "click", function() {
        jQuery(this).parent('.love-post').find('.fa-heart').fadeIn('slow');
    });
    jQuery( ".love-post .fa-heart" ).on( "click", function() {
        jQuery(this).parent('.love-post').find('.fa-heart').fadeOut('slow');
    });
    //End: LOVE POST FEATURE


    /* 
    ###############################################
    Smooth scrolling js
    ############################################### 
    */
    jQuery( 'a[href*="#"]:not([href="#"])' ).on( "click", function() {
        if (location.pathname.replace(/^\//,'') === this.pathname.replace(/^\//,'') && location.hostname === this.hostname) {
            var target = jQuery(this.hash);
            target = target.length ? target : jQuery('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                jQuery('html,body').animate({
                scrollTop: target.offset().top
            }, 1500);
            return false;
            }
        }
    });
    jQuery(window).scroll(function() {    
        var scroll = jQuery(window).scrollTop();

         //>=, not <=
        if (scroll >= 1000) {
            //clearHeader, not clearheader - caps H
            jQuery(".amaezi-top").addClass("is-visible");
        }
    });
    //End: Smooth scrolling js



    /* 
    ###############################################
    Validate and Submit contact form via Ajax
    ############################################### 
    */
    jQuery(".make-reservation").validate({
        //Ajax validation rules
        rules: {
            book_name: {
                required: true,
                minlength: 2
            },
            book_email: {
                required: true,
                email: true
            },
            book_phone: {
                required: true,
                minlength: 8
            },
            book_date: {
                required: true
            },
            book_time: {
                required: true
            },
            book_persons: {
                required: true
            }
        },
        //Ajax validation messages
        messages: {
            book_name: {
                required: "Please enter a name",
                minlength: "Your name must consist of at least 2 characters"
            },
            email: "Please enter a valid email address",
            book_phone: {
                required: "Please enter a message",
                minlength: "Your message must consist of at least 8 characters"
            },
            book_date: {
                required: "Please enter a date"
            },
            book_time: {
                required: "Please select an hour"
            },
            book_persons: {
                required: "Please select no. of persons"
            }
        },
        //Submit via Ajax Form
        submitHandler: function() {
            jQuery('.make-reservation').ajaxSubmit();
            jQuery('.success-message').fadeIn('slow');
        }
    });
    //End: Validate and Submit contact form via Ajax






    /* 
    ###############################################
    mb_YTPlayer js
    ############################################### 
    */
    if ( jQuery( ".youtube-player" ).length ) {
        if ( !mobilecheck() ) {
            jQuery(".youtube-player").mb_YTPlayer({
                onReady: function(){
                    jQuery('.sound').removeClass('hidden');
                    jQuery( ".sound" ).on( "click", function(evt) {
                        evt.preventDefault();
                        if(jQuery('.sound').hasClass('off')){
                            jQuery('.sound').removeClass('off');
                            jQuery('.player').unmuteYTPVolume();
                            jQuery('.sound').addClass('on');
                            jQuery('.title').fadeOut();
                            jQuery('.icon-sound').removeClass('fa-volume-off');
                            jQuery('.icon-sound').addClass('fa-volume-up');
                        }else{
                            if(jQuery('.sound').hasClass('on')){
                                jQuery('.sound').removeClass('on');
                                jQuery('.player').muteYTPVolume();    
                                jQuery('.sound').addClass('off');
                                jQuery('.title').fadeIn();
                                jQuery('.icon-sound').removeClass('fa-volume-up');
                                jQuery('.icon-sound').addClass('fa-volume-off');
                            }
                        }
                    });
                }
            });
            jQuery('.youtube-player').on("YTPStart",function(){
               jQuery('.youtube-video').animate({opacity: 1}, 5000,function(){});
            });
        }
    }
    //End: mb_YTPlayer js



    //open navigation clicking the menu icon
    jQuery('.cd-nav-trigger').on('click', function(event){
        event.preventDefault();
        toggleNav(true);
    });
    //close the navigation
    jQuery('.cd-close-nav, .cd-overlay').on('click', function(event){
        event.preventDefault();
        toggleNav(false);
    });

    function toggleNav(bool) {
        jQuery('.cd-nav-container, .cd-overlay').toggleClass('is-visible', bool);
        jQuery('main').toggleClass('scale-down', bool);
    }
    //End: Menu NAV


    /* Animate */
    jQuery('.animateIn').animateIn();
    
});
