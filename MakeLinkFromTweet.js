function makeLink(text) {
  var expression = /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;
 var regex = new RegExp(expression);

  console.log(text.match(regex))
	if (text.match(regex) )
 {
   text = text.replace(text.match(regex), "<a href='"+text.match(regex)+"'>"+text.match(regex)+"</a>")
 } else {
   console.log("No match");
 }
console.log(text)
return text
}
