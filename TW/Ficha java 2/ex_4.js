/*Número aleatorio*/

let numeroAleatorio = Math.ceil(Math.random() * 10);
let guess = +prompt(`1ª tentativa:`);

if (guess==numeroAleatorio) {
    alert("Parabens, acertaste na primeira tentativa");    
} else{
    let tentativa=2
    while (guess !== numeroAleatorio) {
        guess = +prompt(`${tentativa}ª tentativa:`);
        tentativa++;
    }
    alert(`Acertaste na ${tentativa - 1}ª tentativa!`);
}



