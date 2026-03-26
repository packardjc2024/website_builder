$(document).ready(function() {
    $('#prompt').on('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            $('#chatbot-form').submit(); 
        }
    });
});