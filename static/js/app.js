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


$(".btn-add-issue").click(function (){


    let issue_name = document.getElementById('id_issue_name').value
    let issue_type = document.getElementById('id_issue_type').value
    let project = document.getElementById('id_project').value
    let priority = document.getElementById('id_priority').value
    let due_date = document.getElementById('id_due_date').value
    let description = document.getElementById('id_description').value
    let doc = document.getElementById('id_attachment')

    if(issue_name == "") {
        $("#result").text('Please Enter Name')
    } else if(issue_type == "") {
        $("#result").text('Please Select Type')
    }else if(project == "") {
        $("#result").text('Please Select Project')
    }else if(priority == "") {
        $("#result").text('Please Select Priority')
    }else if(due_date == "") {
        $("#result").text('Please Enter Date')
    }else if(description == "") {
        $("#result").text('Please Enter Description')
    } else {
            $.ajax({
        url: '/homePage',
        type: 'POST',
        data: {
        issue_name: issue_name,
        issue_type: issue_type,
        project: project,
        priority: priority,
        due_date: due_date,
        description: description,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
    }
    }).done(function(response) {
        $("#result").text(response['errorMessage'])
    }).fail(function () {
        $("#result").text(response['errorMessage'])
    })
    }


})

// Priority box color

    priorityTypes.forEach((e) => {
        if (e.innerHTML === 'Urgent') {
            e.classList.add('urgent')
        } else if (e.innerHTML === 'ASAP') {
            e.classList.add('asap')
        }
    })


