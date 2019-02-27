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
  button = getClass("PrimaryButton medium")[0]
  buttonStatus = getClass("PrimaryButton__iconTextWrapper")[0].children[0].innerHTML;
  if(buttonStatus == "Continue" || buttonStatus == "Start Learning") {
    button.click();
  } else {
    blocks = getClass("ModuleStyleWrapper__wrapper");
    currentBlock = blocks[blocks.length - 1];
    type = currentBlock.children[0].className;
    if(type == "ModuleFeedbackWrapper") { // Hidden word from list
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
