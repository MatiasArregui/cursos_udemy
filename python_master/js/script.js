console.log("Hola Mundo")
var nombre = "Matias"; 
let nulo = null;
console.log(typeof nulo)
let noDefinido;
console.log(typeof noDefinido);
let a = 2;
let b = 2;

console.log(a * b)
console.log(a ** 4)
console.log(a + b)
console.log(a - 1 + b)
console.log(++b)
console.log(--a)

let edad = 18;

function verificarEdad(edad){
    if ( edad > 18){
        console.log("Mayor de edad");
    }else if (edad === 18){
        console.log("Mayor de edad con lo justo");
    }else{
        console.log("Menor de edad");
    }
}
verificarEdad(2);

const multiplicar = (a, b) => a*b;
console.log(multiplicar(2,7));