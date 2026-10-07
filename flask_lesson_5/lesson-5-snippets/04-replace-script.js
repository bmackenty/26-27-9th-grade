const form = document.getElementById("generator-form");
const button = document.getElementById("generate-button");
const result = document.getElementById("result");
const nicknameInput = document.getElementById("nickname");
const themeInput = document.getElementById("theme");
const resultCard = document.getElementById("result-card");
const themeBadge = document.getElementById("theme-badge");

async function generate(event) {
    // Keep the form from navigating to another page.
    event.preventDefault();

    // Read values from the controls. trim removes spaces at the ends.
    const nickname = nicknameInput.value.trim();
    const theme = themeInput.value;
    const themeLabel = themeInput.options[themeInput.selectedIndex].text;

    // HTML required blocks an empty field; this also catches spaces alone.
    if (nickname === "") {
        result.textContent = "Please enter an invented nickname.";
        nicknameInput.focus();
        return;
    }

    button.disabled = true;
    result.textContent = "Forging your item...";

    // This request sends NO nickname or theme to Python.
    try {
        const response = await fetch("/api/generate");
        if (!response.ok) {
            throw new Error("The server could not generate an item.");
        }
        const data = await response.json();

        // These lines personalise the result entirely in the browser.
        resultCard.dataset.theme = theme;
        themeBadge.textContent = themeLabel.toUpperCase();
        result.textContent = `${nickname}, your item is: ${data.item}`;
    } catch (error) {
        result.textContent = "Could not reach the generator. Check Flask and try again.";
        console.error(error);
    } finally {
        button.disabled = false;
    }
}

// Listen for the form submission, including submission with the Enter key.
form.addEventListener("submit", generate);

