function get(id) {
  return(document.getElementById(id));
}

function getClass(name) {
  return(document.getElementsByClassName(name));
}

blocks = getClass("ModuleStyleWrapper__wrapper");
currentBlock = blocks[blocks.length - 1].contents;
document.write(currentBlock);
