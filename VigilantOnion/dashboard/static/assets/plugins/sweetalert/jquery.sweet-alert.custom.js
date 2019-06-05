
!function($) {
    "use strict";

    var SweetAlert = function() {};

    SweetAlert.prototype.init = function() {


    // Mensagem de Sucesso Detalhes do Usuario
    $('#detalhes-usuario-sucesso').click(function(){
        swal("Good job!", "The changes were successful, if you typed something wrong, do not worry, you can make as many changes as you want.", "success")
    });

    //Mensagem de Erro detalhes do Usuário
    $('#detalhes-usuario-erro').click(function(){
        swal({
            title: "Oops, something went wrong.",
            text: "It seems that some information that you fill in one or more fields is incorrect or does not go into the pattern so that everything works fine.",
            type: "warning",
            confirmButtonColor: "#DD6B55",
            closeOnConfirm: true
        });
    });

    // Mensagem criação de usuário
    $('#criar-usuario-sucesso').click(function(){
        swal("Success!", "The information you have entered now has been successfully registered.", "success")
    });

    //Mensagem de Erro Login
    $('#login-usuario-erro').click(function(){
        swal({
            title: "Oops, something went wrong.",
            text: "It looks like the username or password you are typing is not correct, please check the fields and try again.",
            type: "warning",
            confirmButtonColor: "#DD6B55",
            closeOnConfirm: true
        });
    });

    //Mensagem de Usuário Cliente
    $('#erro-usuario-cliente').click(function(){
        swal({
            title: "Oops, something went wrong.",
            text: "It looks like you're a user who belongs to the client group, that is, you can only have access to your company's information. If you believe this message should not appear to you, please contact your administrator.",
            type: "warning",
            confirmButtonColor: "#DD6B55",
            closeOnConfirm: true
        });
    });

    //Mensagem de erro Deletar usuário
    $('#delete-usuario-erro').click(function(){
        swal({
            title: "Oops, something went wrong.",
            text: "Something very strange happened when we tried to delete this user, try again.",
            type: "warning",
            confirmButtonColor: "#DD6B55",
            closeOnConfirm: true
        });
    });

    //Mensagem de sucesso Deletar usuário
    $('#delete-usuario-sucesso').click(function(){
        swal("Sucess!", "The user has been deleted.", "success")
    });

    //Mensagem de sucesso Criar Cliente
    $('#criar-cliente-sucesso').click(function(){
        swal("Sucesso!", "Congratulations the client has just been registered in our system, go to Clients / All Clients and make sure it is already appearing on the list.", "success")
    })

    //Mensagem de erro criar cliente
    $('#erro-cliente-cliente').click(function(){
        swal({
            title: "Oops, something went wrong.",
            text: "Oh no, something does not go the way it should, check the fields and try again.",
            type: "warning",
            confirmButtonColor: "#DD6B55",
            closeOnConfirm: true
        });
    });
    //Erro de acesso
    $('#usuario-sem-acesso').click(function(){
        swal({
            title: "Oops, something went wrong.",
            text: "Oh no, it looks like your user is not allowed to access this page. If you believe this is incorrect, please contact your system administrator.",
            type: "warning",
            confirmButtonColor: "#DD6B55",
            closeOnConfirm: true
        });
    });





    },
    //init
    $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
function($) {
    "use strict";
    $.SweetAlert.init()
}(window.jQuery);
