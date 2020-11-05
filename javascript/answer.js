function get(id) {
  return(document.getElementById(id));
}

function pause(milliseconds) {
  setTimeout(function(){;},milliseconds);
}

function myFunction() {
  var copyText = document.getElementById("myInput");
  copyText.select();
  document.execCommand("copy");
  alert("Copied the text: " + copyText.value);
}

function getClass(name) {
  return(document.getElementsByClassName(name));
}

while(true) {
  button = getClass("PrimaryButtonTypes_medium__3jJgQ")[0]
  buttonStatus = getClass("Button_iconTextWrapper__2AVyk")[1].children[0].innerHTML;
  //console.log(buttonStatus);
	if(buttonStatus == "Continue" || buttonStatus == "Start learning") {
    button.click();
  } else {
    blocks = getClass("SessionItemEntranceTransitionWrapper");
    currentBlock = blocks[blocks.length - 1];
    type = currentBlock.children[0].className;
    if(type == "withModuleStyle_wrapper__5MQZf") { // Hidden word from list
      blurredItems = currentBlock.getElementsByClassName("BlurredWord__word BlurredWord__word--blurred")
      for(var i = 0;i < blurredItems.length;i++) {
        blurredItem = blurredItems[i].children[0].innerHTML;
        console.log(blurredItem);
        currentBlock.getElementsByClassName("List__WordInput__input")[0].value = blurredItem+'\n';
        pause(1000);
      }
    }
  }
  break;
}
