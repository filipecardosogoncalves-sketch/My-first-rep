let Lista=[]

function Add_alimento() {
    let alimento = prompt("Digite um alimento:")
    if(!Lista.includes(alimento)){
        Lista.push(alimento)
    }else{
        alert("Este alimento já existe na lista")
    }
}
function Remove_alimento() {
    let rem_alimento = prompt("Digite um alimento para remover:")
    if(Lista.includes(rem_alimento)){
        Lista=Lista.filter(i => i!= rem_alimento)
    }else{
        alert("Este alimento não existe na lista")
    }
}
function Verify_list() {
    if (Lista.length === 0) {
        alert("A lista está vazia.")
    } else {
        alert("Lista de compras: " + Lista.join(","))
    }
}
