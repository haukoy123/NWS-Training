// $('#btn').click(function() {
//     console.log('hello')
// })

// function ajax(config) {
//     const result = 'abcd'
//     if (readyState === 4) {
//         const callback = config.success
//         callback(result)
//     }
// }

// function showEmp (result) {
//     console.log(result)
//     console.log('finish')
// }

// function funny (result) {
//     showEmp(result)
// }

// showEmp(result)
// funny(result)


$('input[name="email"]').on('change', function(e) {
    $element = $(this);
    const email = $element.val()
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        $('#vldEmail').remove();
    } else {
        $('#mess').append($('<label></label>').attr('id', 'vldEmail').css('color', 'red').text('Sai Email'))
    }
});


$('input').focus(function() {
    $(this).css("background-color", "yellow");
});
$('input').blur(function() {
    $(this).css("background-color", "#bff7f4");
});

$('button').hover(function() {
    $(this).css({
        'width': '100px',
        'height': '30px',
        'border-radius': '5px',
        'background': 'chartreuse'
    })
}, function() {
    $(this).css({
        'width': '65px',
        'height': '25px',
        'border-radius': '5px',
        'background': '#e8e8e8',
    })
})

function request(method, path, callback, data) {
    $.ajax({
        url: "http://localhost:8000" + path,
        type: method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjU5NjNmZjEwLTk3ZmMtNDY1OC1hZTczLTUzYjlmNTkxYTAxMSIsImV4cCI6MTY0MDM0MDg4OCwiaWF0IjoxNjM1MTU2ODg4fQ.WeGZ4_sZc2sBdMjFGUGCANhW7Vdz71YLksCGPRWb2ck'
        },
        data: data,
        success: callback,
        error: badResponse
    });
}


function badResponse(error) {
    $('.error').remove()
    let accountError = error.responseJSON.data.account
    let inforError = error.responseJSON.data
    delete inforError.account
    $.extend(inforError, accountError)
        // for (let i in inforError) {
        //     for (let j of inforError[i]) {
        //         // console.log($('input[name=' + i + '').parent())
        //         $('input[name="' + i + '"]').parent().append($('<br>').addClass('error')).append($('<label></lable>').addClass('error').css('color', 'red').text(j))
        //     }
        // }

    inforError.forEach((errors, i) => {
        errors.forEach((error, j) => {
            $(`input[name="${i}"]`)
                .parent()
                .append($('<br>')
                    .addClass('error'))
                .append($('<label></lable>')
                    .addClass('error')
                    .css('color', 'red')
                    .text(j));
        })
    })
}


function getData() {
    request('get', '/api/v1/employees', showEmployees)
}

getData()

function getUserInput() {
    const $elements = $('.account');
    const account = new Object();
    $elements.each(function() {
        const $element = $(this)
        account[$element.attr('name')] = $element.val();
    })

    // account['permission'] = 2;
    account.permission = 2;

    // const attr = 'permission';
    // account[attr] = 2;

    // account['some-thing'] = 2

    // console.log(account);

    const $infor = $('.infor');
    const data = new Object();
    $infor.each(function() {
        const $element = $(this)
        if ($element.attr('name') === 'gender') {
            if ($element.prop('checked')) {
                data[$element.attr('name')] = $element.val();
            }
        } else {
            data[$element.attr('name')] = $element.val();
        }
    })

    if (data.date_birth === '') {
        delete data.date_birth;
    }
    // console.log(data.date_birth)
    data['account'] = account
    data['email'] = account['email']
    return data
}

function createEmployees() {
    const data = getUserInput()
    request('post', '/api/v1/employees', showEmployees, JSON.stringify(data))
}

function showEmployees(data) {
    let employees;
    console.log(data)
    if (data.data.results == null) {
        employees = []
        employees.push(data.data)
    } else {
        employees = data.data.results
    }

    let $rankLast, $rankList = $('.rank');
    if ($rankList.length === 0) {
        $rankLast = 0;
    } else {
        $rankLast = parseInt($('.rank').last().text());
    }
    for (let i in employees) {
        $rankLast++;
        const $rank = $('<td></td>').addClass('rank').text($rankLast)
        const $name = $('<td></td>').text(employees[i]['name'])
        const $phone = $('<td></td>').text(employees[i]['phone'])
        const $email = $('<td></td>').text(employees[i]['email'])
        const $address = $('<td></td>').text(employees[i]['address'])
        const $gender = $('<td></td>').text(employees[i]['gender'])
        const $team = $('<td></td>').text(employees[i]['team'])
        const $submit = $('<td></td>').append($('<input>').attr({ 'type': 'submit', 'onclick': 'delEmployees(' + employees[i]['id'] + ')' }).val('delete'))
            .append($('<input>').attr({ 'type': 'submit', 'onclick': 'editEmployees(' + employees[i]['id'] + ')' }).val('edit'))
        const $tr = $('<tr></tr>').append($rank, $name, $phone, $email, $address, $gender, $team, $submit);
        $('#empl').append($tr);
    }
}

function delEmployees(id) {
    if (confirm("Bạn muốn xóa nhân viên này?")) {
        $('#empl > tr').remove()
        request('delete', '/api/v1/employees/' + id, getData);
    }
}

let idToEdit

function getEmp(data) {
    data = data.data
    idToEdit = data.id

    // console.log(idToEdit)
    const $account = $('.account')
    const $infor = $('.infor')
    $account.each(function() {
        const $element = $(this)
        $element.val(data.account[$element.attr('name')])
    })

    $infor.each(function() {
        const $element = $(this)
        if ($element.attr('name') === 'gender') {
            if ($element.val() === data.gender) {
                $element.attr('checked', 'true')
            }
        } else {
            $element.val(data[$element.attr('name')])
        }
    });
    // console.log(data)
}

function editEmployees(id) {
    request('get', '/api/v1/employees/' + id, getEmp)
}

function updateEmployees() {
    $('#table-header > tr').remove()
    const data = getUserInput()
    request('put', '/api/v1/employees/' + idToEdit, getData, JSON.stringify(data))
}

