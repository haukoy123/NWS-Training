function getData() {
    const http = request('GET', '/api/v1/employees')
    http.onreadystatechange = function() {
        if (http.readyState == 4 && http.status == 200) {
            const data = JSON.parse(http.responseText);
            showData(data);
        }
    }

    function showData(data) {
        document.getElementById('empl').innerHTML = '<tr>' +
            '<th></th>' +
            '<th>Name</th>' +
            '<th>Phone</th>' +
            '<th>Email</th>' +
            '<th>Address</th>' +
            '<th>Gender</th>' +
            '<th>Team</th>' +
            '<th></th>' +
            '</tr>';
        console.log(data['data'])
        console.log(empl)
        let employees = data['data']['results']
        for (let i in employees) {
            var tr = document.createElement('tr');
            let html = '<td>' + (parseInt(i) + 1) + '</td>' +
                '<td>' + employees[i]['name'] + '</td>' +
                '<td>' + employees[i]['phone'] + '</td>' +
                '<td>' + employees[i]['email'] + '</td>' +
                '<td>' + employees[i]['address'] + '</td>' +
                '<td>' + employees[i]['gender'] + '</td>' +
                '<td>' + employees[i]['team'] + '</td>' +
                '<td>' +
                '<input type="submit" value="delete" onclick="deleteEmployees(' + employees[i]["id"] + ')">' +
                '<input type="submit" value="edit" onclick="getEmployees(' + employees[i]["id"] + ')">' +
                '</td>';
            // var html = `
            //     <td>${parseInt(i) + 1}</td>
            // `
            tr.innerHTML = html;
            document.getElementById('empl').appendChild(tr);
        }
    }
}
getData()

function createEmployees() {
    const data = inputData();
    const http = request('POST', '/api/v1/employees', JSON.stringify(data))
    http.onreadystatechange = function() {
        if (http.readyState == 4) {
            getData();
        }
    }
}

function deleteEmployees(id) {
    const http = request('DELETE', '/api/v1/employees/' + id)
    http.onreadystatechange = function() {
        if (http.readyState === 4) {
            getData();
        }
    }
}

function getEmployees(id) {
    const http = request('GET', '/api/v1/employees/' + id)
    http.onreadystatechange = function() {
        if (http.readyState == 4) {
            const data = JSON.parse(http.responseText);
            editEmployees(data)
        }
    }
}


let idToEdit

function editEmployees(data) {
    idToEdit = data['data']['id']
    var account = document.getElementsByClassName('account')
    for (let i = 0; i < account.length; i++) {
        account[i].value = data['data']['account'][account[i].name]
    }

    var infor = document.getElementsByClassName('infor');
    for (let j = 0; j < infor.length; j++) {
        if (infor[j].name == 'gender') {
            if (infor[j].value == data['data'][infor[j].name]) {
                infor[j].checked = true;
            }
        } else {
            infor[j].value = data['data'][infor[j].name];
        }
    }
}


function inputData() {
    var elements = document.getElementsByClassName('account');
    var account = new Object();
    for (var i = 0; i < elements.length; i++) {
        account[elements[i].name] = elements[i].value;
    }

    var infor = document.getElementsByClassName('infor');
    var data = new Object();
    for (var j = 0; j < infor.length; j++) {
        data[infor[j].name] = infor[j].value;
    }
    account['permission'] = 2;
    data['account'] = account;
    return data
}


function updateEmployees() {
    const data = inputData();
    const http = request('PUT', '/api/v1/employees/' + idToEdit, JSON.stringify(data))
    http.onreadystatechange = function() {
        if (http.readyState == 4) {
            getData();
        }
    }
}

function request(method, path, data) {
    var http = new XMLHttpRequest();
    http.open(method, 'http://localhost:8000' + path, true);
    http.setRequestHeader('Content-Type', 'application/json');
    http.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjU5NjNmZjEwLTk3ZmMtNDY1OC1hZTczLTUzYjlmNTkxYTAxMSIsImV4cCI6MTY0MDM0MDg4OCwiaWF0IjoxNjM1MTU2ODg4fQ.WeGZ4_sZc2sBdMjFGUGCANhW7Vdz71YLksCGPRWb2ck');
    http.send(data);
    return http;
}

