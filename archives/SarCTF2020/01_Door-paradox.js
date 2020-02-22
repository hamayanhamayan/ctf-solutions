var path = document.location.pathname;

let content, vizavi;

var getUser = api('users.checkAuth');
if (getUser.status === 'success') {
    var userId = getUser.response.user_id;
    $("#navlist").append('<li class="nav-item"><a class="nav-link" href="/messages">Messages</a></li>');
    $("#navlist").append('<li class="nav-item"><a class="nav-link" href="/logout">Log out</a></li>');
} else {
    $("#navlist").append('<li class="nav-item"><a class="nav-link" href="/login">Log in</a></li>');
}

switch (true) {
    case path.match(/^(\/|)$/) !== null:
        document.title = 'Home';
        content = '<div class="starter-template">\n' +
            '<h1>РЎommunication is cool...</h1>\n' +
            '<p class="lead" id="content">The safest messenger in the world!</p>\n' +
            '</div>';
        $('#main').html(content);
        break;
    case path.match(/^\/login(\/|)$/) !== null:
        document.title = 'Log in';
        content = '<form>\n' +
            '  <div class="form-group">\n' +
            '    <label for="nickname">Nickname</label>\n' +
            '    <input class="form-control" id="nickname">\n' +
            '  </div>\n' +
            '  <div class="form-group">\n' +
            '    <label for="password">Password</label>\n' +
            '    <input type="password" class="form-control" id="password">\n' +
            '  </div>\n' +
            '  <p onclick="action(\'login\'); return false;" class="btn btn-primary">Log in</p>\n' +
            '</form>';
        $('#main').html(content);
        break;
    case path.match(/^\/logout(\/|)$/) !== null:
        localStorage.clear();
        location = '/';
        break;
    case path.match(/^\/users(\/|)$/) !== null:
        document.title = 'a list of users';
        let users = api('users.getAll',undefined, true);
        text = '<div class="list-group">';
        users.response.forEach(element => text += `<a href="/write/${element.id}" class="list-group-item list-group-item-action">${element.nickname}</a>`);
        text += '</div>';
        $('#main').html(text);
        break;
    case path.match(/^\/write\/(\d+)(\/|)$/) !== null:
        document.title = 'Write';
        content = '<form>\n' +
            '  <div class="form-group">\n' +
            '    <label for="text">Text:</label>\n' +
            '    <textarea class="form-control" id="text" rows="5"></textarea>\n' +
            '  </div>\n' +
            '  <p onclick="action(\'write\'); return false;" class="btn btn-primary">Send</p>\n' +
            '</form>';
        $('#main').html(content);
        break;
    case path.match(/^\/messages(\/|)$/) !== null:
        document.title = 'Messages';
        req = api('messages.getDialogs',undefined, true);
        if (req.response.length !== 0) {
            text = '<div class="list-group">';
            req.response.forEach(element => text += `<a href="/messages/${element.id}" class="list-group-item list-group-item-action">${element.title}</a>`);
            text += '</div>';
        } else {
            text = '<div class="starter-template">\n' +
                '<h1>РЎommunication is cool...</h1>\n' +
                '<p class="lead" id="content">But you haven\'t written to anyone yet!</p>\n' +
                '</div>';
        }
        $('#main').html(text);
        break;
    case path.match(/^\/messages\/(.+)(\/|)$/) !== null:
        let msgFrom;
        document.title = 'Messages';
        req = api('messages.getByDialog', {"user_id": document.location.pathname.match(/^\/messages\/(.+)(\/|)$/)[1]}, true);
        text = '<form>\n' +
            '  <div class="form-group">\n' +
            '    <label for="text">Text:</label>\n' +
            '    <textarea class="form-control" id="text" rows="5"></textarea>\n' +
            '  </div>\n' +
            '  <p onclick="action(\'reply\'); return false;" class="btn btn-primary">Send</p>\n' +
            '</form>';
        text += '<div class="list-group">';
        req.response.messages.forEach(function (message) {
            msgFrom = req.response.members[message.from_member].nickname;
            text += `<li class="list-group-item"><b>${msgFrom}: </b>${message.message}</li>`;
        });
        text += '</div>';
        vizavi = req.response.members.first.id === userId ? req.response.members.second.id : req.response.members.first.id;
        $('#main').html(text);
        break;
    case path.match(/^\/admin(\/|)$/) !== null:
        document.title = 'Admin';
        content = '<form>\n' +
            '  <div class="form-group">\n' +
            '    <label for="password">Password</label>\n' +
            '    <input type="password" class="form-control" id="password">\n' +
            '  </div>\n' +
            '  <p onclick="action(\'adminAuth\'); return false;" class="btn btn-primary">Log in</p>\n' +
            '  <p onclick="action(\'adminRestore\'); return false;" class="btn btn-link">Forgot your password?</p>' +
            '</form>';
        $('#main').html(content);
        break;
    default:
        document.title = 'Page not found';
        alert('Page not found');
        location = '/';
        break;
}

function api(method, params = {}, withAlert = false) {
    params.key = localStorage.access_key;
    let result = JSON.parse($.ajax({
        url: '/api/' + method,
        type: "POST",
        data: params,
        async: false
    }).responseText);
    if (result.status === 'error' && withAlert === true) {
        alert(result.response);
    }
    return result;
}

function action(action) {
    let req;
    switch (action) {
        case 'login':
            req = api('users.logIn', {"nickname": $("#nickname").val(), "password": $("#password").val()}, true);
            if (req.status === 'success') {
                localStorage.setItem('access_key', req.response);
                location = '/';
            }
            break;
        case 'write':
            req = api('messages.send', {
                "user_id": document.location.pathname.match(/^\/write\/(\d+)(\/|)$/)[1],
                "text": $("#text").val()
            }, true);
            if (req.status === 'success') {
                location = '/messages/' + req.response;
            }
            break;
        case 'reply':
            req = api('messages.send', {
                "user_id": vizavi,
                "text": $("#text").val()
            }, true);
            if (req.status === 'success') {
                location = '/messages/' + req.response;
            }
            break;
        case 'adminRestore':
            req = api('admin.restore', undefined, true);
            if (req.status === 'success') {
                while (req.response.need_sms === true) {
                    code = prompt('A six-digit secret code has been sent to your number. Enter the code from SMS:');
                    if (code === null || code === undefined || code === '') {
                        location.reload();
                    } else {
                        req = api('admin.restore', {
                            'hash': req.response.new_hash,
                            'sms_code': code
                        }, true);
                    }
                }
                if (req.response.message) alert(req.response.message);
            }
            break;
        case 'adminAuth':
            req = api('admin.logIn', {"password": $("#password").val()}, true);
            if (req.status === 'success') {
                eval(req.response.code);
            }
            break;
    }
}