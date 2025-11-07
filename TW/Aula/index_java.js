/*let num = 50

while(num <= 55){
    num++
    console.log(num);
}
*/
/*let cond= false

let arr = [1, 5, 2, 11, 23]

for(let i =0; i<arr.length; i++){
    if(arr[i]%2==0)
        console.log('O número');
        
}*/

function teste() {
     return("Olá")
}

let msg = teste()
console.log(msg);


function add(n1, n2 = 3) {
  let sum = n1 + n2
  return sum
}
console.log(add(3))
console.log(add(3, 4))

/*function testarRest(...params) {
    console.log(params);
}

testarRest(5,"Sofia",true)*/

let soma = (a) => 10 + a
console.log(soma(2));


