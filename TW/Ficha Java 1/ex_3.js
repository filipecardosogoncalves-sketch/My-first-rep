let peso = prompt("Digite o seu peso(kg)")
let altura = prompt("Digite a sua altura(m)")
let IMC = peso / (altura * altura)

if (IMC<18.5){
    alert("Classificação: Magreza")
}else if(18.5<=IMC<=24.9){
    alert("Classificação: Normal")
}else if(25<=IMC<=29.9){
    alert("Classificação: Sobrepeso")
}else if( 30<=IMC<=34.9){
    alert("Classificação: Obesidade grau I")
}else if(35<=IMC<=39.9){
    alert("Classificação: Obesidade grau II")
}else{
    alert("Classificação: Obesidade grau III")
}
        