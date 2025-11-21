function euromilhoes() {
    let numeros = [];
    let estrelas = [];

    while (numeros.length < 5) {
        let num = Math.ceil(Math.random() * 50);
        if(!numeros.includes(num)){
            numeros.push(num)
        }
    }
    while (estrelas.length < 2) {
        let estrela = Math.ceil(Math.random() * 12);
        estrelas.push(estrela)
    }

    console.log("Números: " + numeros.join(", "));
    console.log("Estrelas: " + estrelas.join(", "));
}
euromilhoes();
