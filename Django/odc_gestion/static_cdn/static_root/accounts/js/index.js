labels = document.querySelectorAll('label')

for (let i = 0; i < labels.length; i++) {
    labels[i].classList.add("form-group")
}

inputs = document.querySelectorAll('input')

for (let i = 0; i < inputs.length; i++) {
    inputs[i].classList.add("form-control")
}