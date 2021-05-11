function Supprimer(element) {
    var list = document.getElementById('list')
    list.removeChild(element.parentNode)
}
function Ajouter(event) {
    event.preventDefault()
    var list = document.getElementById('list')
    // Recuperation de la valeur du champ
    let addElt = document.getElementById('element').value
    // Creation du li
    let li = document.createElement('li')
    let btn = document.createElement('button')
    btn.setAttribute("onclick", "Supprimer(this)")
    let textBtn = document.createTextNode('Supprimer')
    btn.appendChild(textBtn)
    let text = document.createTextNode(addElt)
    li.appendChild(text)
    li.appendChild(btn)
    list.appendChild(li)
}
formulaire = document.querySelector('form')
formulaire.addEventListener("submit", Ajouter, false);
//comodo

// lorsqu'on cree un element on peut l'ajouter un evenement directement 

// ecouter le click sur le button
// creer les elements button
// Ajouter l'element au Dom
// ecouter le clicl sur l'evement
// retirer les elemets