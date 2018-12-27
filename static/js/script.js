function queren(is_modify) {


    var station=$("#stationname").val();
    var data = {"station": station};
    $.ajax({
        type: "GET",
        url: "/busstation",
        data: data,
        success: function(data){
            $('body').html(data)
        }

    });

}

function queren2(is_modify) {


    var number=$("#busname").val();
    var data = {"number": number};
    $.ajax({
        type: "GET",
        url: "/busnumber",
        data: data,
        success: function(data){
           $('body').html(data)
        }
    });

}