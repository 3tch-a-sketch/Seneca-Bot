function get(id) {
  return(document.getElementById(id));
}

function getClass(name) {
  return(document.getElementsByClassName(name));
}

blocks = getClass("ModuleStyleWrapper__wrapper");
currentBlock = blocks[blocks.length - 1];
type = currentBlock.children[0].className;

if(type == "ModuleFeedbackWrapper") { // Hidden word from list
  blurredItems = currentBlock.getElementsByClassName("BlurredWord__word BlurredWord__word--blurred")
  for(i = 0; i < blurredItems)
  blurredItem = [0].children[0].innerHTML;
}
