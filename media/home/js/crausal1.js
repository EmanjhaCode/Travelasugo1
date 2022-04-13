 $(document).ready(function() {
              var owl = $('.owl-carousel');
              owl.owlCarousel({
                margin: 30,
                nav: true,
                loop: true,
                responsive: {
                  0: {
                    items: 1
                  },
                  600: {
                    items: 2
                  },
				   1000:{
				     items:4,
					 loop:false
				  },
                }
              })
            })
