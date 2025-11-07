let operação = prompt(" Qual opção deseja fazer: ")
let n1 = Number(prompt("Digite um número "))
let n2 = Number(prompt("Digite outro número menor que o anterior"))
let soma = n1 + n2 
let sub= n1 - n2
let multi = n1 * n2
let div= n1 / n2

if(operação === "S"){
    alert(n1 + "+" + n2 + "="+soma)
}else if (operacao === "Sub") {
    alert(n1 + "-" + n2 + "="+ sub)
} else if (operacao === "M") {
    alert(n1 + "x" + n2 + "="+ multi)
} else if (operacao === "D") {
    alert(n1 + "/" + n2 + "="+ div)
} else {
    alert("Operação inválida.")
}