$(document).ready(function(){
	// $("selector").eventListener(function9(){result})
	$("#firsta,#firstc, #firstb, #secondb, #secondc, #secondd, #thirda, #thirdc, #thirdd, #fourtha, #fiftha, #fifthb, #sixthd, #sevenc, #eightha").click(function(){
		console.log('correct'); 
		// what happens when firstb is clicked
		$("#response").html('<p class="correct-answer">Correct!</p>');
	})

	$("#firstd, #seconda, #thirdb, #fourthb, #fourthc, #fourthd, #fifthc, #fifthd, #sixtha, #sixthb, #sixthc, #sevena, #sevenb, #sevend, #eighthb, #eighthc, #eighthd").click(function(){
		$('#response').html('<p class="incorrect">Incorrect, try again!</p>');
	})
	
})