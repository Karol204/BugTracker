// Funkcja odpowiadajaca za fale przy formularzu logowania i rejestracji
const loginLabels = document.querySelectorAll('.form-control label')
const priorityTypes = document.querySelectorAll('.priorityType')
const formBtn = document.getElementById('hidden-form')
const btnShowingBtn = document.querySelector('.btnshowingForm')
const priorityCheck = document.getElementById('priority')

loginLabels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('')
})

// Report bug on popup


if(btnShowingBtn !== null){
    btnShowingBtn.addEventListener('click', (e) => {
    formBtn.classList.toggle('inactive')
    btnShowingBtn.classList.toggle('active')
})
}



$(".btdn-add-issue").click(function (e){
    e.preventDefault()

    let issue_name = document.getElementById('id_issue_name').value
    let issue_type = document.getElementById('id_issue_type').value
    let project = document.getElementById('id_project').value
    let priority = document.getElementById('id_priority').value
    let due_date = document.getElementById('id_due_date').value
    let description = document.getElementById('id_description').value
    let att = document.getElementById('id_attachment').value

    if(issue_name == "") {
        $("#result").text('Please Enter Name')
    } else if(issue_type == "") {
        $("#result").text('Please Select Type')
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
        priority: priority,
        due_date: due_date,
        description: description,
        project:project,
        att:att,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value}
    }).done(function() {
        $("#result").text('Successfully added')
    }).fail(function (response) {
        $("#result").text('Something went wrong')
    })
    }
})



function screenWidthCheck () {
    if (innerWidth >= 600) {
        $('.btnshowingForm').removeClass('mobile-display-none')
    }
}


// Priority box color

    priorityTypes.forEach((e) => {
        if (e.innerHTML === 'Urgent') {
            e.classList.add('urgent')
        } else if (e.innerHTML === 'ASAP') {
            e.classList.add('asap')
        }
    })


$(document).on("click", ".editable", function (){
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


window.addEventListener('resize', screenWidthCheck())

// priorityCheckFunc()
screenWidthCheck()

let form1 = $('#form1')
let form2 = $('#form2')
let form3 = $('#form3')


let next1 = $('#next1')
let next2 = $('#next2')

let back1 = $('#back1')
let back2 = $('#back2')

let progress = $('#progress')

next1.on('click', function () {

    let issue_name = document.getElementById('id_issue_name').value
    let issue_type = document.getElementById('id_issue_type').value
    let description = document.getElementById('id_description').value

    if (issue_name == "") {
        $("#result").text('Please Enter Name')
    } else if (issue_type == "") {
        $("#result").text('Please Select Type')
    } else if (description == "") {
        $("#result").text('Please Enter Description')
    } else {

        form1.css('left', -450)
        form2.css('left', 40)
        progress.css('width', 240)
    }
})

back1.on('click', function (){

        form1.css('left', 40)
        form2.css('left', 450)
        progress.css('width', 120)
})

next2.on('click', function (){
     let due_date = document.getElementById('id_due_date').value

    if(due_date == "") {
         $("#result").text('Please Enter Date')
    } else {
        form2.css('left', -450)
        form3.css('left', 40)
        progress.css('width', 360)
    }
})

back2.on('click', function (){
    form2.css('left', 40)
    form3.css('left', 450)
    progress.css('width', 240)
})


function sendProfile(e) {
    e.preventDefault()

    let userId = document.getElementById('formBtn').dataset.id
    let firstName = document.getElementById('id_first_name').value
    let lastName = document.getElementById('id_last_name').value
    let position = document.getElementById('id_position').value

    let profilePic = document.getElementById('id_profil_pic').value


    if (firstName == "") {
        $("#result").text('Please Enter First Name')
    } else if (lastName == "") {
        $("#result").text('Please Enter Last Name')
    } else if (position == "") {
        $("#result").text('Please Select Position')
    } else {
        $.ajax({
            url: `/profil/${userId}`,
            type: 'POST',
            dataType: "json",
            data: {
                firstName: firstName,
                lastName: lastName,
                position: position,
                profilePic: profilePic,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        }).done(function() {
                $("#result").text(response['errorMessage'])
            }).fail(function (response) {
                $("#result").text(response['errorMessage'])
        })
    }
}
