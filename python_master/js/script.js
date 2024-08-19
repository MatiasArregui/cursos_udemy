// console.log("Hola Mundo")
// var nombre = "Matias"; 
// let nulo = null;
// console.log(typeof nulo)
// let noDefinido;
// console.log(typeof noDefinido);
// let a = 2;
// let b = 2;

// console.log(a * b)
// console.log(a ** 4)
// console.log(a + b)
// console.log(a - 1 + b)
// console.log(++b)
// console.log(--a) 

// let edad = 18;

// function verificarEdad(edad){
//     if ( edad > 18){
//         console.log("Mayor de edad");
//     }else if (edad === 18){
//         console.log("Mayor de edad con lo justo");
//     }else{
//         console.log("Menor de edad");
//     }
// }
// verificarEdad(2);

// const multiplicar = (a, b) => a*b;
// console.log(multiplicar(2,7));

// const lista = [1,2,3,4,5];
// console.log(lista)
// lista.push(6);
// console.log(lista)
// lista.forEach((elemento, indice) => {
//     console.log(elemento, indice);
// })

// for(let i = 0; i<5; i++){
//     console.log(i+1);
// }

// let i = 0;
// while(i<=3){
//     console.log(i+1);
//     i +=1;
// }
// do{
//     console.log(i);
// }while(i<=3);

// const h1 = document.getElementById("heading");
// console.log(h1.textContent);
// const ul = document.getElementById("lista");
// console.log(ul.innerHTML);
// console.log(ul.textContent);

// console.log(titulo);
// titulo.style.backgroundColor = "red";
// titulo.classList.add("titulo1");
// titulo.classList.add("titulo2");
// titulo.classList.remove("titulo2");
// const lista = document.querySelectorAll(".list li");
// lista[2].style.color = "red";
// lista[2].style.backgroundColor = "#ffde";
// for(let i = 0; i < lista.length; i++){
//     // lista[i].style.backgroundColor = "#eee";
//     // lista[i].style.color = "red";
//     // lista[i].style.listStyle = "none";
//     lista[i].className = "estilo1 estilo2";
//     lista[i].className +=" estilo3";
// }
// const button = document.querySelector(".btn");

// button.onclink = () => {
//     console.log("hola");
// };
// button.onmouseover = () => {
//     titulo.classList.add("titulo2");
//     titulo.classList.remove("titulo1");
// };
// button.onmouseout = () => {
//     titulo.classList.add("titulo1");
//     titulo.classList.remove("titulo2");
// };
const titulo = document.querySelector(".heading");
const boton = document.querySelector(".btn");
// boton.onclick = () =>{ 
//     console.log("hola mundo");
// };
boton.addEventListener("click", () => {
    titulo.classList.add("titulo2");
});
boton.addEventListener("mouseover", () => {
    titulo.classList.add("titulo1");
});
boton.addEventListener("mouseout", () => {
    titulo.classList.remove("titulo1");
});

const newElemento = document.createElement("li");
const texto = document.createTextNode("4 hola");
newElemento.appendChild(texto);

const lista = document.querySelector(".list");
// lista.appendChild(newElemento);
lista.insertBefore(newElemento, lista.children[1]);
