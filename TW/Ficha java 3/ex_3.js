/*Contando vogais*/

let texto= prompt("Digite uma frase:")

let a=0, e=0, i=0, o=0, u=0;

frase = texto.toLowerCase();

for (let i = 0; i < frase.length; i++){
    let letra = frase.charAt(i);
    if(letra=="a"){
        a++
    }else if(letra=="e"){
        e++
    }else if(letra=="i"){
        i++
    }else if(letra=="o"){
        o++
    }else if(letra=="u"){
        u++
    }
}   

alert(`A:${a},E:${e},I:${i},O:${o},U:${u}`)