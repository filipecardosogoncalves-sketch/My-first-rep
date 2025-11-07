/*UserName*/

let First_name= prompt("Digite o seu primeiro nome:");
let Secnd_name= prompt("Digite o seu apelido:");
let num= prompt("Digite um número de 0 a 100:");
List.push(num);
let List=[];

let first= First_name.slice(0,3);
List.push(first);
let second= Secnd_name.slice(0,3);
List.push(second);

alert(List.join(""));
