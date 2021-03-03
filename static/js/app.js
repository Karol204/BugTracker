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
    let status = document.getElementById('id_status').value

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
    } else if(status == "") {
        $("#result").text('Please Enter status')
    }
    else {
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
        status: status,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
    }
    }).done(function(response) {
        $("#result").text(response['errorMessage'])
    }).fail(function (response) {
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


$(document).on("dblclick", ".editable", function (){
    let select = "<select class='input-data form-control' name=\"status\" id=\"id_status\">\n" +
        "  <option value=\"New\">New</option>\n" +
        "\n" +
        "  <option value=\"In Progress\">In Progress</option>\n" +
        "\n" +
        "  <option value=\"Done\">Done</option>\n" +
        "\n" +
        "</select>"
    $(this).html(select)
    $(this).removeClass("editable")
        })

$(document).on("blur", ".input-data", function ()  {
    let value = $(this).val()
    let td = $(this).parent("td")
    $(this).remove();
    td.html(value)
    td.addClass("editable")
    sendToServer(td.data("id"), value)
})

$(document).on("keypress", ".input-data", function (e)  {
    let key = e.keyCode
    if(key == 13) {
         let value = $(this).val()
        let td = $(this).parent("td")
        $(this).remove();
        td.html(value)
        td.addClass("editable")
        sendToServer(td.data("id"), value)

    }
})

function sendToServer(id, value) {
    $.ajax({
        url: '/updateStatus',
        type: 'POST',
        data: {
            id: id,
            value: value,
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value

        },
    }).done(function (response){
        console.log('success')
    }).fail(function (response){
        console.log('error')
    })
}
