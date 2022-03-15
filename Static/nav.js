function make_divs_appear(index){

        
      document.querySelectorAll(".right-div")[index].style.right = "-7%"
      if(index == 1){
        document.querySelectorAll(".left-div")[index].style.left = "5%"
      }else{
        document.querySelectorAll(".left-div")[index].style.left = "15%"
      }
        
    
}

lastScrollTop = 0


window.addEventListener("scroll" , function(e){
    st = window.pageYOffset || document.documentElement.scrollTop
  
    if(st >= 285 ){
        
        make_divs_appear(0)
        
    }
    if(st >= 710 ){
        
        make_divs_appear(1)
        
    }
    if(st >= 1270){
        make_divs_appear(2)
     
    }
    

    lastScrollTop = st <= 0 ? 0 : st;
})