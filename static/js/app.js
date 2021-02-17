
// Funkcja odpowiadajaca za fale przy formularzu logowania i rejestracji
const loginLabels = document.querySelectorAll('.form-control label')

const priorityTypes = document.querySelectorAll('.priorityType')

loginLabels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('')
})

console.log(priorityTypes)

priorityTypes.forEach((e) => {
    console.log(e.innerHTML)
    if(e.innerHTML === 'Urgent') {
        e.classList.add('urgent')
    } else if(e.innerHTML === 'ASAP'){
        e.classList.add('asap')
    }
})