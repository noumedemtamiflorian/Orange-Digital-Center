const form = document.querySelector('form')
var prenom = document.getElementById('prenom')
var prix_unitaire = document.getElementById('prix_unitaire')
var quantite = document.getElementById('quantite')
var prix_total = document.getElementById('prix_total')


prix_unitaire.onchange = (event) => {
    event.preventDefault()
    let Pu = event.target.value
    if (parseInt(Pu) < 0) {
        alert("Entrer un entier positif")
        Pu = event.target.value = 0
    }
    prix_total.value = Pu * quantite.value

}
quantite.onchange = (event) => {
    event.preventDefault()
    let Qte = event.target.value
    if (parseInt(Qte) < 0) {
        alert("Entrer un entier positif")
        Qte = event.target.value = 0
    }
    prix_total.value = Qte * prix_unitaire.value
}

form.onsubmit = () => {
    alert(`Merci Mr ${prenom.value}  d’avoir choisit notre magasin. Vous avez commandé 
    ${quantite.value} produit(s) dont le prix unitaire est de ${prix_unitaire.value} 
    pour un prix total de ${prix_total.value}`)
}