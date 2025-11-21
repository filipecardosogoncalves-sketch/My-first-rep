let List=[]
let numberS

function number(nums) {
    console.log(nums)
    numberS=nums
}
function Soma(number) {
    List.push(number)
}
function Result(number){
    if(numberS>0){
        List.push(number)
    }
    let soma = List.reduce((a, b) => a + b)
    console.log("Resultado da soma: " + soma);
    List = []
}

