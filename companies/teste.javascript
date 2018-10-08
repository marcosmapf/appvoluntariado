let user_data = {
    "trading_name": "Vulpi",
    "company_sector": "RHTec",
    "company_location": "Belo Horizonte",
    "phone": "31998717317",
    "email": "atendimento@vulpi.com.br",
    "website": "https://vulpi.com.br/",
    "description": "Tenha acesso às melhores vagas para desenvolvedores e programadores"
}

let path = "http://localhost:8000/v1/companies"
let method = "POST"

post(path, user_data, method);

function post(path, params, method) {
    method = method || "post";

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}