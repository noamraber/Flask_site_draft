$(document).ready(function() {
    $('#type_of_movement').on('input', function() {
        let type = $(this).val();
        $('#movement_value').text(type);
        
        $.ajax({
            url: '/update_ESP32_sys_movement',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({type: type}),
            success: function(response) {
                console.log('ESP sys movement updated:', response.ESP32_sys_movement);
            }
        });
    });
});
