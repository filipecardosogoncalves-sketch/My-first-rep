/*UserName*/
let List=[]
let First_name= prompt("Digite o seu primeiro nome:");
let Secnd_name= prompt("Digite o seu apelido:");

let first= First_name.slice(0,3);
List.push(first)
let second= Secnd_name.slice(0,3);
List.push(second)
let num= prompt("Digite um número de 0 a 100:");
List.push(num)


console.log("O seu username é",List.join(""));

