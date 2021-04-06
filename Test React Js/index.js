
function change() {
    var prix_unitaire = document.getElementById('prix_unitaire').value;
    var quantite = document.getElementById('quantite').value;
    if (parseInt(prix_unitaire) != NaN && parseInt(prix_unitaire) < 0) {
        alert("le prix unitaite doit etre un nombre positif")
    }
    if (parseInt(quantite) != NaN && parseInt(quantite) < 0) {
        alert("Entrer une valuer positif")
    }
    var Prix_total = document.getElementById('prix_total').value = prix_unitaire * quantite;
}

function envoyer() {
    var prix_unitaire = document.getElementById('prix_unitaire').value;
    var prenom = document.getElementById('prenom').value;
    var quantite = document.getElementById('quantite').value;
    var total = prix_unitaire * quantite
    alert(`Merci Mr ${prenom} d'avoir chosit notre magasin. Vous avez commande ${quantite} produit(s) dont le prix unitaire est de ${prix_unitaire} pour un prix total de ${total}`)
}