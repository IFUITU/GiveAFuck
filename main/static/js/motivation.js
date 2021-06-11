let slides;
let ekran = $(window).width();
// console.log(ekran)

// // Enable Carousel Indicators
// $(".item").click(function(){
//   $("#myCarousel").carousel(1);
// });

// // Enable Carousel Controls
// $(".left").click(function(){
//   $("#myCarousel").carousel("prev");
// });

if(ekran <= 449){
  slides = 1;
  let container = $('.c0ntainer');
  container.removeClass('container');
}else if(ekran >= 450 && ekran <= 800){
  slides =  2;
}else{
  slides = 3;
};  


$('.slick-slider').slick({
  slidesToShow: slides,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 1000,
});
// $(".slick-slider").slick({
//   dots:false,
//   slidesToShow: 5,
//   slidesToScroll:1,
//   touchMove:false
// })

// $("label").click(function(){
//   $(this).parent().find("label").css({"background-color": "#78e2fb"});
//   $(this).css({"background-color": "red"});
//   $(this).nextAll().css({"background-color": "red"});
// });
// $(".star label").click(function(){
//   $(this).parent().find("label").css({"color": "#78e2fb"});
//   $(this).css({"color": "red"});
//   $(this).nextAll().css({"color": "red"});
//   $(this).css({"background-color": "transparent"});
//   $(this).nextAll().css({"background-color": "transparent"});
// });


// let dwlink = $('.a[name="dwnlink"]');
// var clicks = 0;
// function dwndlink(){
//   clicks = ++clicks;
//   $('b[name="cnt_dwn"]').text(String(clicks)) ;
  
// };

// let platforms = $('span[name="platform"]');
let g = 0;

$(".p1atf0rm").each(function(){
  let str = $(this).first().text();
  
    if (str == 'Windows'){
      $(this).addClass('icon icon-windows text-primary');
      // icon_plt.addClass('icon icon-windows');
    }
    else if (str == 'Android'){
      $(this).addClass('icon icon-android text-success');
      // icon_plt.addClass('icon icon-android');
    }
    else if (str == "Ubuntu"){
     $(this).addClass('icomoon icon-lightning text-warning');
      // icon_plt.addClass('icomoon icon-lightning');
    }else if (str == "MacOS"){
      $(this).addClass('icomoon icon-apple c888');
      // icon_plt.addClass('icon icon-apple');
    }
    else if(str == 'Xbox360'){
      $(this).addClass('fa fa-times text-success');
      // icon_plt.addClass('icon icon-support');
    }
    else if(str == 'PSP 4' || str=="PSP 5" || str=='PSP 3' || str=="PSP 2"){
      $(this).addClass('fa fa-gamepad csilver');
    }
    else if(str == 'Online'){
      $(this).addClass('fa fa-globe text-light');
    }
    else{
      $(this).addClass('fa fa-child text-warning');
    }
    g+=1

  
  // console.log(str);
  
});







$('.status').each(function(){
  let str = $(this).first().text();
  if (parseInt(str) >= 300  && parseInt(str) < 1000){
    $(this).addClass('over5k');
  }else if (parseInt(str) >= 1000 && parseInt(str) <= 2000){
    $(this).addClass('M6');
  }else if (parseInt(str) > 2000){
    $(this).addClass('over10k');
  }else{
    $(this).addClass('');
  }
  
  // str += $(this).text() + "<br>";
});




//--------------------// AJAX //-------------------------//

  $('a[data-toggle="ajax"]').on('click', function(e){
    // alert($(this).attr('class'));
    let obj = $(this);
    
    // $.post($(this)) //work with post method

    $.get($(this).attr('href'), function(res){
      
      obj.html(res);
    });
    // $.ajax({
    //   method:'GET',
    //   url:$(this).attr('href'),
    //   success:function (res){
    //     // obj.parent().find('.class').html()
    //     obj.html(res);
    //   },
    //   error:function (){
    //     alert("ERROt");
    //   }
    // });
    return false;
  });

  // $('#download_start').on('click', function(e){
  //   let obj = $(this).attr('data-url');
  //   // alert(obj);
  //   window.location.href = obj;
  //   let url = $(this).children().attr('href');
  //   // alert(url);
    
  //   $.get(url, function(res){
  //     console.log(res, "fuckn Res");
  //     $('b[name="cnt_dwn"]').html(res);
  //   });
  //   // return false;
  // });

let dwnd_a = $('.file-size');
if (dwnd_a.text() == 'CommingSoon'){ 
  $('a[aria-disabled="false"]').attr('onclick','return false');
};

let login = $('#login');
let register = $('#register');

$('#onclick-register').on('click', function(e){
  // login.css({"display":"none"});
  $.get('/user/login/', function(response){
    console.log(response);
    $('#myModalJS').html('');
    $('#myModalJS').html(response);
  });
  return false;
}); 




// Img to modal View
// var modal = document.getElementById("imgModal");
// // Get the image and insert it inside the modal - use its "alt" text as a caption
// var img = $('div[data-img="imgToModal"]');
// console.log(img.attr('data-img'));
// var modalImg = document.getElementById("img01");
// var captionText = document.getElementById("caption");
// img.on('click', function(e){
//   console.log('Clicked div');
//   modal.style.display = "block";
//   modalImg.src = $(this).attr('data-url');
//   captionText.innerHTML = "From demo gameplay!";
// });
// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];
// // When the user clicks on <span> (x), close the modal
// span.onclick = function() { 
//   modal.style.display = "none";
// }
////////////////////////////////////

$.ajax({
  url:'/Home/GamesApi/',
  success:function(res){
    // alert(JSON.stringify(res))
  }
})