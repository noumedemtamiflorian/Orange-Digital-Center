
const list = document.getElementById('list')
const button = document.querySelector('button')
const form = document.querySelector('form')

form.onsubmit = function (event) {
    event.preventDefault()
    let eltAdd = document.querySelector('input').value
    let li = document.createElement('li')
    li.appendChild(document.createTextNode(eltAdd))
    let btn = document.createElement("button")
    btn.onclick = function (event) {
        list.removeChild(li)
    }
    btn.appendChild(document.createTextNode("Supprimer"))
    li.appendChild(btn)
    list.appendChild(li)
}