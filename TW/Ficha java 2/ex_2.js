/*Exercicio primo*/

let num = prompt("Digite um número:")
let count= 0
function primo(num) {
    for ( let i=1; i<=num;i++){
          if(num%i==0){
            count++
            }
    }
    if (count==2){
        alert("O número é primo");
    }else{
        alert("O número não é primo");
    }
}