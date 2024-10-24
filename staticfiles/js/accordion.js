var acc = document.getElementsByClassName("faq__item__header");
var i;

for(i=0; i< acc.length; i++){
    acc[i].addEventListener("click", function(){
        this.classList.toggle("active");

        var faq__item__content = this.nextElementSibling;
        // if (faq__item__content.style.display === "block") {
        //     faq__item__content.style.display = "none";
        // } else {
        //     faq__item__content.style.display = "block";
        // }
        if (faq__item__content.style.maxHeight){
            faq__item__content.style.maxHeight = null;
        } else{
            faq__item__content.style.maxHeight = faq__item__content .scrollHeight + "px"
        }
    }
);
}