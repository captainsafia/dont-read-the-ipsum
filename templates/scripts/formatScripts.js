var paragraphMinSentences=2,
	paragraphMaxSentences=8,
	sentenceMinWords=3,
	sentenceMaxWords=12;

function gimmeLetter(myString){
	var formattedText,
		paragraphArray,
		numParagraphs=Math.floor(Math.random()*(4))+4;
	formattedText+='<p>To whom it may concern,</p>';
	myString=sentenceize(myString);
		console.log(myString);
	for(var i=0;i<numParagraphs;i++){
		
		//var numWordsinParagraph=randomInRange(paragraphMinWords, paragraphMaxWords),
			//stringPortion=trim_words(myString, numWordsinParagraph);
		//myString=myString.substring(stringPortion.length, myString.length);
	}
}

function trim_words(theString, numWords) {
    expString = theString.split(/\s+/,numWords);
    theNewString=expString.join(" ");
    return theNewString;
}
function randomInRange(min, max){
	return Math.floor(Math.random()*(max-min)+min);
}
function sentenceize(string){
	var newString='',
		allWords=string.split(" "),
		allSentences;
	while(allWords.length>3){
		var sentenceLength=randomInRange(sentenceMinWords, sentenceMaxWords),
			thisSentence=allWords.splice(0, sentenceLength);
		newString+=thisSentence.join(" ");
		newString+='. ';
	}
	return newString;
}
function paragraphize(sentences){

}
