function calcularIMC() {
    //entrada
    let peso = Number(document.getElementById("peso").value);
    let altura = parseFloat(document.getElementById("altura").value);
    //processamento
    let calculoIMC = peso/(altura*altura);
    //saída
    document.getElementById("resultado").textContent = "Seu IMC é: " + calculoIMC.toFixed(2);
    if (calculoIMC < 18.5) {
        document.getElementById("classificacao").textContent = "Você está na faixa de baixo peso"}
    else if (calculoIMC > 18.5 && calculoIMC < 25){
        document.getElementById("classificacao").textContent = "Você está na faixa normal de peso"}
    else {
        document.getElementById("classificacao").textContent = "Você está na faixa de sobrepeso"}
}