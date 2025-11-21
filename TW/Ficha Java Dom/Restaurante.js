let Lista = []
let Menu = document.querySelectorAll("li")//Vai imprimir cada elemnto no console//
for(let i = 0; i<Menu.length;i++){
    console.log(Menu[i].innerHTML)
    Lista.push(Menu[i].innerHTML)
}


let botao = document.querySelector("button");
botao.addEventListener("click", function() {
    let novoPrato = prompt("Digite o nome do novo prato:");
    if(novoPrato){
        let novaLinha= document.createElement("li");//Criar nova linha//
        let texto = document.createTextNode(novoPrato);//Criar um texto com o pormpt//
        novaLinha.appendChild(texto);//Adicionar o texto á linha//
        document.querySelector("ul").appendChild(novaLinha);//Adicionar a linha à lista//
    }
});

let titulo = document.querySelector("h1");

titulo.addEventListener("mouseover", function() {
    titulo.style.color = "blue";//Ao passar por cima mudar a cor do titulo para azul//
});
titulo.addEventListener("mouseout", function() {
    titulo.style.color = "";//Voltar a cor original//
});