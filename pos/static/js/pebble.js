    var time = 18000;
    if ($(window).width() <= 600){
        test = 20000;
    }

    // Slideshow on product homepages
    $('#quotes').carousel({
        interval: time
    });


    // Customize twitter feed
    var hideTwitterAttempts = 0;
      function hideTwitterBoxElements() {
        setTimeout( function() {
          if ( $('[id*=twitter]').length ) {
          $('[id*=twitter]').each( function(){
              var ibody = $(this).contents().find( 'body' );

              if ( ibody.find( '.timeline .stream .h-feed li.tweet' ).length ) {

              $(this).width(400);

              ibody.find( '.customisable-border' ).css( 'border', 0 );
              ibody.find( 'ol.h-feed' ).css( 'border-radius', '6px' );
              ibody.find( 'li.tweet' ).css( 'border-bottom', '1px dotted #FFFFFF' ); //theme: tweets: color:
              ibody.find( 'li.tweet' ).css( 'color', '#333333' ); //theme: tweets: color:

              ibody.find( '.customisable:link' ).css( 'color', '#4ABAC2' ); //theme: tweets: links:
              ibody.find( '.follow-button' ).css( 'visibility', 'hidden' ); //hide reply, retweet, favorite images

              ibody.find( '.avatar' ).css( 'display', 'none' ); //hide avatar
              ibody.find( 'li.tweet' ).css( 'padding', '12px 10px' ); //tweet padding
              ibody.find( 'li.tweet' ).css( 'border-bottom', '1px solid #666666' ); //tweet padding


              ibody.find( '.p-nickname' ).css( 'font-size', 0 ); //hide @name of tweet
              ibody.find( '.p-nickname' ).css( 'visibility', 'hidden' ); //hide @name of tweet

              // ibody.find( '.footer' ).css( 'min-height', 0 ); //hide reply, retweet, favorite images
              ibody.find( '.footer' ).css( 'height', 30 ); //hide reply, retweet, favorite images
              ibody.find( '.timeline-footer').hide();

              ibody.find( 'h1.summary' ).replaceWith( '<h1 class="summary"><a class="customisable-highlight" title="Pebble on twitter" href="https://twitter.com/mypebble" style="color: #333333;">Pebble on Twitter @mypebble</a></h1>' ); //replace Tweets text at top
              ibody.find( '.p-name' ).css( 'color', '#4ABAC2' ); //theme: tweets: links:
              }
              else {
                  $(this).hide();
              }
          });
          }
          hideTwitterAttempts++;
          if ( hideTwitterAttempts < 3 ) {
              hideTwitterBoxElements();
          }
      }, 1500);
  }
  // somewhere in your code after html page load
  hideTwitterBoxElements();




//eventbrite


$(document).ready(function(){
  Eventbrite({'app_key': "XMDORQYW6PZWGZPVZX"}, function(eb){
    eb.organizer_list_events( {'id': 6834479797, 'statuses': "live, started"}, function( response ){
      var event_list_html = eb.utils.eventList( response, eb.utils.eventListRow );
      $("#event-list").html(event_list_html);
    });
  });
});
