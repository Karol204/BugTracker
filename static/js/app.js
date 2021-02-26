// Funkcja odpowiadajaca za fale przy formularzu logowania i rejestracji
const loginLabels = document.querySelectorAll('.form-control label')

const priorityTypes = document.querySelectorAll('.priorityType')

const formBtn = document.getElementById('hidden-form')

loginLabels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('')
})

// Report bug on popup

const btnShowingBtn = document.querySelector('.btnshowingForm')

btnShowingBtn.addEventListener('click', (e) => {
    formBtn.classList.toggle('inactive')
    btnShowingBtn.classList.toggle('active')
})



function AjaxFormSubmit() {

    let issue_name = document.getElementById('id_issue_name')
    let issue_type = document.getElementById('id_issue_type')
    let project = document.getElementById('id_project')
    let priority = document.getElementById('id_priority')
    let due_date = document.getElementById('id_due_date')
    let description = document.getElementById('id_description')

    let page = "/homePage"
    let info = {'issue_name' : issue_name, 'issue_type' : issue_type, 'project' : project, 'priority' : priority,
    'due_date' : due_date, 'description' : description, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}
    console.log(info)
    $.post(page, info, function () {
        $.success(function (){
            formBtn.innerHTML = '<h1 class="confirmation">Done</h1>'
            setTimeout(hideForm, 2000)
        })
})

function hideForm() {
    formBtn.classList.add('inactive')
}}


// Priority box color

priorityTypes.forEach((e) => {
    if(e.innerHTML === 'Urgent') {
        e.classList.add('urgent')
    } else if(e.innerHTML === 'ASAP'){
        e.classList.add('asap')
    }
})