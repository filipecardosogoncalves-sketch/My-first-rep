//Exercicio1//
// let nums=[]
// let numsOut=[]
// let count=0

// function createNums() {
//     for(let i=1;i<=90;i++){
//         nums.push([i])
//     }
// }
// createNums()

// function sortNums() {
//     let pos= Math.floor(Math.random()*nums.length)

//     let numOut=num[pos]
//     numOut.push(numOut)
//     nums=nums.filter(i => i!=numOut)
//     count++
//     if(count==90){
//         alert("Os numeros forma todos tirados")
//         nums=[]
//         numsOut=[]
//         count=0
//         createNums()
//     }
// }
// function bingo() {
//     if(count<15){
//         alert("Impossivel")
//     }else{
//         alert("Bingo")
//         nums=[]
//         numsOut=[]
//         count=0
//         createNums()
//     }
// }


//Exercicio2//
// let Lista=[]
// let Negativos=[]
// let Positivos=[]

// for(let i= 0; i<=15;i++){
//    let num= Math.ceil(Math.random()*101);
//    num=num-50
//    Lista.push(num)
//    if(num<0){
//     Negativos.push(num)
//    }else{
//     Positivos.push(num)
//    }
// }
// alert(`A lista continha os números ${Lista.join(",")} com ${Negativos.length} números negativos e ${Positivos.length} positivos.`)
    


//Exercicio3//
// let numeros = [121, 123, 44, 456, 11, 90, 909, 22];
// let capicuas=[]

// for(let i=0; i<numeros.length;i++){
//     let num=String(numeros[i])
//     let inverso= num.split("").reverse().join("")
//     if(num == inverso){
//        console.log("O numero é uma capicua");
//     }else{
//         console.log("O numero não é uma capicua");
//     }
// }


//Exercicio4//
let username= prompt("User Name:")
if(username=="Admin"){
    let password=prompt("Digite a password:")
    if(password=="TheMaster"){
        alert("Bem-vindo!")
    }else if(password=="") {
        alert("Cancelado")
    }else{
        alert("Password errada")
    }
}else if (username==""){
    alert("Cancelado")
}else{
    alert("Username não reconhecido")
}