(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });


    // Progress Bar
    $('.pg-bar').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Calender
    $('#calender').datetimepicker({
        inline: true,
        format: 'L'
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
        nav : false
    });


    // Worldwide Sales Chart
    var ctx1 = $("#worldwide-sales").get(0).getContext("2d");
    var myChart1 = new Chart(ctx1, {
        type: "bar",
        data: {
            labels: get_data(0),
            datasets: [{
                    label: "Total Employee",
                    data: get_data(2),
                    backgroundColor: "#2a3954"
                },
                {
                    label: "Present Count",
                    data: get_data(4),
                    backgroundColor: "#0be8b0"
                },
                {
                    label: "Absentism",
                    data: get_data(3),
                    backgroundColor: "#f33e53"
                },

            ]
            },
        options: {
            responsive: true
        }
    });


    // Salse & Revenue Chart
    var ctx2 = $("#salse-revenue").get(0).getContext("2d");
    var myChart2 = new Chart(ctx2, {
        type: "line",
        data: {
            labels: get_data(0),
            datasets: [{
                    label: "Total Employee",
                    data: get_data(2),
                    backgroundColor: "rgba(0, 156, 255, .5)",
                    fill: true
                },
                {
                    label: "Present Count",
                    data: get_data(4),
                    backgroundColor: "rgba(0,255,138,0.3)",
                    fill: true
                },
                {
                    label: "Absentism",
                    data: get_data(3),
                    backgroundColor: "rgb(255,2,61)",
                    fill: true
                }
            ]
            },
        options: {
            responsive: true
        }
    });
    


    // Single Line Chart
    var ctx3 = $("#line-chart").get(0).getContext("2d");
    var myChart3 = new Chart(ctx3, {
        type: "line",
        data: {
            labels: [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
            datasets: [{
                label: "Salse",
                fill: false,
                backgroundColor: "rgba(0, 156, 255, .3)",
                data: [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15]
            }]
        },
        options: {
            responsive: true
        }
    });


    // Single Bar Chart
    var ctx4 = $("#bar-chart").get(0).getContext("2d");
    var myChart4 = new Chart(ctx4, {
        type: "bar",
        data: {
            labels: ["Italy", "France", "Spain", "USA", "Argentina"],
            datasets: [{
                backgroundColor: [
                    "rgba(0, 156, 255, .7)",
                    "rgba(0, 156, 255, .6)",
                    "rgba(0, 156, 255, .5)",
                    "rgba(0, 156, 255, .4)",
                    "rgba(0, 156, 255, .3)"
                ],
                data: [55, 49, 44, 24, 15]
            }]
        },
        options: {
            responsive: true
        }
    });


    // Pie Chart
    var ctx5 = $("#pie-chart").get(0).getContext("2d");
    var myChart5 = new Chart(ctx5, {
        type: "pie",
        data: {
            labels: ["Italy", "France", "Spain", "USA", "Argentina"],
            datasets: [{
                backgroundColor: [
                    "rgba(0, 156, 255, .7)",
                    "rgba(0, 156, 255, .6)",
                    "rgba(0, 156, 255, .5)",
                    "rgba(0, 156, 255, .4)",
                    "rgba(0, 156, 255, .3)"
                ],
                data: [55, 49, 44, 24, 15]
            }]
        },
        options: {
            responsive: true
        }
    });


    // Doughnut Chart
    var ctx6 = $("#doughnut-chart").get(0).getContext("2d");
    var myChart6 = new Chart(ctx6, {
        type: "doughnut",
        data: {
            labels: ["Italy", "France", "Spain", "USA", "Argentina"],
            datasets: [{
                backgroundColor: [
                    "rgba(0, 156, 255, .7)",
                    "rgba(0, 156, 255, .6)",
                    "rgba(0, 156, 255, .5)",
                    "rgba(0, 156, 255, .4)",
                    "rgba(0, 156, 255, .3)"
                ],
                data: [55, 49, 44, 24, 15]
            }]
        },
        options: {
            responsive: true
        }
    });

    
})(jQuery);


function get_data(n){
    let res=[]
    if (n==1){
        let preleave_person =document.getElementById("preleave_person").innerText;
        preleave_person=preleave_person.slice(1,-1).split(",")
        for(i=0;i<preleave_person.length;i++){
            res.push(parseInt(preleave_person[i]))
        }
        console.log(res)
        return res
    }else if (n==0) {
        let dates = document.getElementById("dates").innerText;
        dates = dates.slice(1, -1).split(",")
        for (i = 0; i < dates.length; i+=3) {
            res.push(dates[i+2].replace(')','')+"/"+dates[i+1])
        }
        console.log(res)
        return res
    }else if(n==2){
        let total_person =document.getElementById("total_person").innerText;
        console.log(total_person)
        total_person=total_person.slice(1,-1).split(",")
        for(i=0;i<total_person.length;i++){
            res.push(parseInt(total_person[i]))
        }
        //console.log(res)
        return res
    }else if(n==3){
        let late_person =document.getElementById("late_person").innerText;
        late_person=late_person.slice(1,-1).split(",")
        for(i=0;i<late_person.length;i++){
            res.push(parseInt(late_person[i]))
        }
        console.log(res)
        return res
    }else if(n==4) {
        let present_count = document.getElementById("present_count").innerText;
        present_count = present_count.slice(1, -1).split(",")
        for (i = 0; i < present_count.length; i++) {
            res.push(parseInt(present_count[i]))
        }
        console.log(res)
        return res

    }

}

