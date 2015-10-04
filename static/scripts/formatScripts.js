var paragraphMinSentences=4,
	paragraphMaxSentences=12,
	sentenceMinWords=4,
	sentenceMaxWords=12,
	lineWordMin=1,
	lineWordMax=7,
	stanzaLineMin=1,
	stanzaLineMax=8;

function gimmeNormal(myString, numParagraphs, numWords){
	numWords=numWords||300000000;
	var formattedText='';
	var mySentences=sentenceize(myString, sentenceMinWords, sentenceMaxWords, numWords);
	if(numParagraphs>1){
		myString=paragraphize(mySentences, numParagraphs);
		formattedText+='<p>'+myString.join('</p><p>')+'</p>';
	}
	else{
		formattedText+='<p>'+mySentences.join(' ')+'</p>';
	}
	return formattedText;
}

function gimmeLetter(myString){
	var formattedText,
		minParagraphs=3,
		maxParagraphs=8,
		numParagraphs=randomInRange(minParagraphs, maxParagraphs);
		
	formattedText='<p>To whom it may concern,</p>';
	myString=sentenceize(myString, sentenceMinWords, sentenceMaxWords);
	myString=paragraphize(myString, numParagraphs);
	formattedText+='<p>'+myString.join('</p><p>')+'</p><p>Your friend,<br>Kevin</p>';
	return formattedText;
}

function gimmeFreeVerse(myString, stanzas){
	var formattedText='',
		myString=sentenceize(myString, lineWordMin, lineWordMax);
		for(var i in myString){
			var str=myString[i];
			myString[i]=str.substring(0, str.length-1);
			if(Math.random()>.95){
				myString[i]+='&mdash;';
			}
		}
		myString=poemize(myString, stanzas);
		formattedText+='<p>'+myString.join('<p><p>')+'.</p>';
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
function sentenceize(string, minWordsinSentence, maxWordsinSentence, maxWords){
	maxWords=maxWords||10000000000;
	var newString='',
		allWords=string.split(" "),
		allSentences=[];
	if(allWords.length>maxWords){
		allWords=allWords.splice(0, maxWords);
	}
	while(allWords.length>3){
		var sentenceLength=randomInRange(minWordsinSentence, maxWordsinSentence);
		sentenceLength=Math.min(sentenceLength, allWords.length);
		var	thisSentence=allWords.splice(0, sentenceLength);
		if(allWords.length<4){
			thisSentence=thisSentence.concat(allWords);
		}
		if(sentenceLength==1){
			sentenceLength=randomInRange(minWordsinSentence, maxWordsinSentence);
		}
		if(sentenceLength>5){
			if(Math.random()>.5){
				var insertionPoint=randomInRange(2, sentenceLength-2);
				if(Math.random()>.2){
					thisSentence[insertionPoint]+=',';
				}
				else{
					if(Math.random()>.5){
						thisSentence[insertionPoint]+=';';
					}
					else{
						thisSentence[insertionPoint]+='&mdash;';
					}
				}
			}
		}
		thisSentence=thisSentence.join(" ")+'.';
		thisSentence=thisSentence.replace("&mdash; ", "&mdash;");
		thisSentence=thisSentence.charAt(0).toUpperCase()+thisSentence.substring(1);
		allSentences.push(thisSentence);
	}
	allSentences=filterWord(allSentences);
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

function poemize(lines, numStanzas){
	var stanzaArray=[];
	for(var i=0;i<numStanzas;i++){
		var numLines=randomInRange(stanzaLineMin, stanzaLineMax);
		var thisStanza=lines.splice(0, numLines);
		thisStanza=thisStanza.join('<br>');
		stanzaArray.push(thisStanza);
	}
	return stanzaArray;
}

function filterWord(myWords){
	for(var word in myWords){
		if(myWords[word].indexOf('http')>0){
			myWords.splice(word, 1);
		}
	}
	return myWords;
}
