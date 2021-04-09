
const list = document.querySelector('ul')
const button = document.querySelector('button')
const form = document.querySelector('form')

form.onsubmit = function (event) {
    // Bloquer la redirection du formulaire
    event.preventDefault()
    // Recuperation du produit
    let produit = document.querySelector('input').value
    // Creation de la liste a ajouter
    let li = document.createElement('li')
    li.appendChild(document.createTextNode(produit))
    // Creation du boutton supprimer
    let btn = document.createElement("button")
    btn.appendChild(document.createTextNode("Supprimer"))
    li.appendChild(btn)
    // Attachement de l'evenement onclick au boutton cree
    btn.onclick = function (event) {
        list.removeChild(li)
    }
    // Ajout du li a la liste
    list.appendChild(li)
    // Vidage du formulaire
    document.querySelector('input').value = ""
}