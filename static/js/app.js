
// Funkcja odpowiadajaca za fale przy formularzu logowania i rejestracji
const loginLabels = document.querySelectorAll('.form-control label')

loginLabels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('')
})