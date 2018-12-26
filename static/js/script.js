function queren(is_modify) {


    var station=$("#stationname").val();
    alert("username++"+station);
    var data = {"station": "临江大道"};
    $.ajax({
        type: "GET",
        url: "/busstation",
        data: data,
        success: function(data){
            location.reload();
        }
    });

}

function queren2(is_modify) {


    var station=$("#stationname").val();
    alert("username++"+station);
    var data = {"station": "临江大道"};
    $.ajax({
        type: "GET",
        url: "/busstation",
        data: data,
        success: function(data){
            location.reload();
        }
    });

}