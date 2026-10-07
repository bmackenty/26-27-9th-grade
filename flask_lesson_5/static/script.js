const button = document.getElementById("generate-button");
const result = document.getElementById("result");

async function generate() {
    const response = await fetch("/api/generate");
    const data = await response.json();
    result.textContent = data.item;
}

button.addEventListener("click", generate);
