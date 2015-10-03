var paragraphMinSentences=2,
	paragraphMaxSentences=8,
	sentenceMinWords=3,
	sentenceMaxWords=12,
	minParagraphs=3,
	maxParagraphs=8;

function gimmeLetter(myString){
	var formattedText,
		numParagraphs=randomInRange(minParagraphs, maxParagraphs);
	formattedText='<p>To whom it may concern,</p>';
	myString=sentenceize(myString);
	myString=paragraphize(myString, numParagraphs);
	formattedText+='<p>'+myString.join('</p><p>')+'</p><p>Your friend, Kevin</p>';
	return formattedText;
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
		allSentences=[];
	while(allWords.length>3){
		var sentenceLength=randomInRange(sentenceMinWords, sentenceMaxWords),
			thisSentence=allWords.splice(0, sentenceLength);
		thisSentence=thisSentence.join(" ")+'.';
		thisSentence=thisSentence.charAt(0).toUpperCase()+thisSentence.substring(1);
		allSentences.push(thisSentence);
	}
	return allSentences;
}
function paragraphize(sentences, numParas){
	var paragraphArray=[];
	for(var i=0;i<numParas;i++){
		var numSentences=randomInRange(paragraphMinSentences, paragraphMaxSentences);
		paragraphArray.push(sentences.splice(0, numSentences).join(' '));
	}
	return paragraphArray;
}
