/*Avaliação escolar*/ 

function avaliacao() {
    let num = Math.ceil(Math.random() * 20);
    if (0<=num<=9){
        return alert(`O estudante teve ${num} valores, resultando em Negativa`);
    } else if(10<=num<=13){
        return alert(`O estudante teve ${num} valores, resultando em Tem de ir a Prova Oral`);
    } else if(14<=num<=17){
        return alert(`O estudante teve ${num} valores, resultando em Positiva`);
    } else if(18<=num<=20){
        return alert(`O estudante teve ${num} valores, resultando em Excelente`);
    } else{
        return alert("Valor inválido");
    }
}