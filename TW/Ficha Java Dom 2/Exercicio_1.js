let text = document.getElementById("content").firstElementChild.textContent
console.log(text)

let select = document.getElementById("mySelect")
select.addEventListener("change", function () {
  console.log("Selecionado:", select.value)
})

let para = document.createElement("p")
let novoNome = document.createTextNode("João II")
para.appendChild(novoNome)

let antigo = document.getElementById("container")
let antigoNome = document.getElementById("p1")
parent.replaceChild(novoNome, antigoNome)

let pai = document.getElementById("container")
let remove = document.getElementById("p1")
pai.removeChild(remove)
