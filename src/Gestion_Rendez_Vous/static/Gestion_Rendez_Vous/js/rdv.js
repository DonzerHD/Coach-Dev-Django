document
    .getElementById("submitButton")
    .addEventListener("click", function () {
        swal("Votre rendez-vous a bien été confirmé!", {
            buttons: {
                confirm: {
                    text: "OK",
                    value: true,
                    visible: true,
                    className: "btn btn-primary",
                    closeModal: true,
                },
            },
        }).then((value) => {
            if (value) {
                window.location.href = "{% url 'accueil' %}";
            }
        });
    });