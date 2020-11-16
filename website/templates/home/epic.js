function renderNew() {
    var newItem = document.createElement("p");
    var textnode = document.createTextNode("Water");
    newItem.appendChild(textnode);

    var list = document.getElementById("monkey");
    list.insertBefore(newItem, list.childNodes[1]);

}