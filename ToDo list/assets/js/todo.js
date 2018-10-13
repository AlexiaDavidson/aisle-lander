//Crosses out completed tasks
$("ul").on("click", "li", function() {
	$(this).toggleClass("done");
});

//Deletes tasks
$("ul").on("click", "span", function(event){
	$(this).parent().fadeOut(500, function(){
		$(this).remove();
	})
	event.stopPropagation();//Prevents event listener from firing for parent elements
});

//Aceepts new task
$("input").keypress(function(event){
	if (event.which === 13) {
		var todoText = $("input").val();
		$("ul").append("<li><span><i class='fa fa-trash' aria-hidden='true'></i></span> "+todoText+"</li>");
		$("input").val("");
	}
});

//Makes text input bar visible
$(".fa-plus-square").click(function(){
	$("input").fadeToggle();
});