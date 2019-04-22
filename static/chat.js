var socket = io.connect('http://' + document.domain + ':' + location.port);
      socket.on( 'connect', function() {
        socket.emit( 'my event', {
          data: 'User Connected'
        } )
        var form = $( 'form' ).on( 'submit', function( e ) {
          e.preventDefault()
          let user_name = $( '#username' ).text()
          let user_input = $( 'input.message' ).val()
          socket.emit( 'my event', {
            user_name : user_name,
            message : user_input
          } )
          $( 'input.message' ).val( '' ).focus()
        } )
      } )
      socket.on('response_message', function( msg ) {
        console.log( msg )
        if( typeof msg.user_name !== 'undefined' ) {

          // $( 'div.message_holder' ).append( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
          $('#messagesTextArea').append(msg.timestamp+'\n')
          $('#messagesTextArea').append(msg.user_name+': ' + msg.message+'\n')
        }
      })