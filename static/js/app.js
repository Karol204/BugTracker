// Funkcja odpowiadajaca za fale przy formularzu logowania i rejestracji
const loginLabels = document.querySelectorAll('.form-control label')

const priorityTypes = document.querySelectorAll('.priorityType')

const IssueDetailBtn = document.querySelectorAll('.title')

console.log(IssueDetailBtn)
loginLabels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('')
})

// Issue description

IssueDetailBtn.forEach((e) => {
    e.addEventListener('click', showIssueDetail)
})

function showIssueDetail() {
    this.classList.toggle('inactive')

}

// Priority box color

priorityTypes.forEach((e) => {
    console.log(e.innerHTML)
    if(e.innerHTML === 'Urgent') {
        e.classList.add('urgent')
    } else if(e.innerHTML === 'ASAP'){
        e.classList.add('asap')
    }
})