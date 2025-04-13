document.addEventListener("DOMContentLoaded", function () {
    /* FUNCIONAMIENTO PARA EL FORMULARIO REGISTRARSE */
    const formRegister = document.querySelector("#registerForm");
    if (formRegister) {
        setupTogglePassword(formRegister, ['#password', '#confirm']);
        // Referencias a los elementos del formulario de registro
        const email = formRegister.querySelector("#email");
        const contraseña = formRegister.querySelector("#password");
        const confirmarContraseña = formRegister.querySelector("#confirm");

        // Evento submit del formulario de registro
        formRegister.addEventListener("submit", function (event) {
            event.preventDefault();
            limpiarErrores(formRegister);
            let isValid = true;

            if (!email.value.trim() || !validarCorreo(email.value)) {
                mostrarError(email, "Ingrese un correo válido.", formRegister);
                isValid = false;
            }
            if (!contraseña.value.trim() || !validarContraseña(contraseña.value)) {
                mostrarError(contraseña, "La contraseña debe tener 6-18 caracteres, incluir una mayúscula y un número.", formRegister);
                isValid = false;
            }
            if (contraseña.value !== confirmarContraseña.value) {
                mostrarError(confirmarContraseña, "Las contraseñas no coinciden.", formRegister);
                isValid = false;
            }
            // Validar que el campo de confirmar contraseña no esté vacío
            if (!confirmarContraseña.value.trim()) {
                mostrarError(confirmarContraseña, "Confirma tu contraseña.", formRegister);
                isValid = false;
            }

            // Si todas las verificaciones son validas, se simula el envío (en este caso mediante redirección)
            if (isValid) {
                // Obtenemos el contenedor para el mensaje de registro
                const registerMessageDiv = document.getElementById("registerMessage");
                registerMessageDiv.innerHTML = '<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                    'Te has registrado correctamente.' +
                    '</div>';
            }
        });
    }

    /* FUNCIONAMIENTO PARA EL FORMULARIO INICIAR SESION */
    const formLogin = document.querySelector("#loginForm");
    if (formLogin) {
        // Referencias a los elementos del formulario de login
        const usuarioLogin = formLogin.querySelector("#username");
        const contraseñaLogin = formLogin.querySelector("#password");

        // Evento para mostrar/ocultar la contraseña
        setupTogglePassword(formLogin, ['#password']);

        // Evento submit del formulario de login
        formLogin.addEventListener("submit", function (event) {
            event.preventDefault();
            limpiarErrores(formLogin);
            let isValid = true;

            if (!usuarioLogin.value.trim()) {
                mostrarError(usuarioLogin, "El usuario o correo es obligatorio.", formLogin);
                isValid = false;
            }
            if (!contraseñaLogin.value.trim()) {
                mostrarError(contraseñaLogin, "La contraseña es obligatoria.", formLogin);
                isValid = false;
            }

            if (isValid) {
                // Definimos las credenciales predefinidas para el administrador
                const usuario = "ADMIN";
                const contraseña = "Admin@12345";

                // Obtenemos el contenedor del mensaje (asegúrate de tenerlo en tu HTML)
                const loginMessageDiv = document.getElementById("loginMessage");

                if (usuarioLogin.value.trim() === usuario && contraseñaLogin.value.trim() === contraseña) {
                    // Mensaje de éxito para el administrador
                    loginMessageDiv.innerHTML = '<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                        'Has iniciado sesión correctamente como administrador.' +
                        '</div>';
                    setTimeout(function () {
                        window.location.href = "paginas/index-admin.html";
                    }, 5000);
                } else {
                    // Mensaje de éxito para usuario normal
                    loginMessageDiv.innerHTML = '<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                        'Has iniciado sesión correctamente.' +
                        '</div>';
                    setTimeout(function () {
                        // Si el formulario no tiene un atributo "action", usamos homeUrl
                        const params = new URLSearchParams(new FormData(formLogin)).toString();
                        const url = formLogin.getAttribute("action") ?
                            formLogin.getAttribute("action") + "?" + params : homeUrl;
                        window.location.href = url;
                    }, 5000);
                }
            }
        });
    }

    /* FUNCIONAMIENTO PARA EL FORMULARIO RECUPERACIÓN DE CONTRASEÑA */
    const formularioContraseña = document.getElementById("recoverForm");
    if (formularioContraseña) {
        formularioContraseña.addEventListener("submit", function (event) {
            event.preventDefault();
            limpiarErrores(formularioContraseña);
            const emailRecuperacion = document.getElementById("recoverEmail");

            if (!emailRecuperacion.value.trim() || !validarCorreo(emailRecuperacion.value)) {
                mostrarError(emailRecuperacion, "Ingrese un correo válido.", formularioContraseña);
                return;
            }

            // Mostramos la alerta de Bootstrap
            const alertaCodigo = document.getElementById("recoverMessage");
            alertaCodigo.innerHTML = '<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                'Código de recuperación enviado a ' + emailRecuperacion.value +
                '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                '</div>';

            formularioContraseña.reset();

            // Ocultar el modal y limpiar el mensaje después de 5 segundos
            setTimeout(function () {
                alertaCodigo.innerHTML = "";
                const recoverModalEl = document.getElementById("recoverPasswordModal");
                const recoverModal = bootstrap.Modal.getInstance(recoverModalEl);
                if (recoverModal) {
                    recoverModal.hide();
                }
            }, 5000);
        });
    }

    /* FUNCIONES COMPARTIDAS */
    function mostrarError(element, message, container) {
        element.classList.add("is-invalid");
        const errorDiv = document.createElement("div");
        errorDiv.classList.add("invalid-feedback");

        // Icono de error
        const iconSpan = document.createElement("span");
        iconSpan.classList.add("error-icon");
        iconSpan.textContent = "!";
        errorDiv.appendChild(iconSpan);
        errorDiv.insertAdjacentText("beforeend", " " + message);

        element.parentNode.insertBefore(errorDiv, element.nextSibling);

        // Listener para quitar el error al ingresar texto
        const clearError = function () {
            element.classList.remove("is-invalid");
            if (errorDiv.parentNode) {
                errorDiv.parentNode.removeChild(errorDiv);
            }
            element.removeEventListener("input", clearError);
        };
        element.addEventListener("input", clearError);
    }

    // Función para limpiar todos los errores dentro de un contenedor (formulario)
    function limpiarErrores(container) {
        container.querySelectorAll(".is-invalid").forEach(el => el.classList.remove("is-invalid"));
        container.querySelectorAll(".invalid-feedback").forEach(el => el.remove());
    }

    // Validación de formato de email
    function validarCorreo(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Validación de contraseña: 6-18 caracteres, al menos una mayúscula y un dígito
    function validarContraseña(password) {
        const regex = /^(?=.*[A-Z])(?=.*\d)[\S]{6,18}$/;
        return regex.test(password);
    }

    // Configuración para mostrar/ocultar contraseña en el formulario de registro y login
    function setupTogglePassword(form, passwordFieldSelectors) {
        // Busca el checkbox dentro del formulario (evita duplicados o conflictos globales)
        const toggle = form.querySelector('#showPassword');
        if (toggle) {
            toggle.addEventListener('change', function () {
                passwordFieldSelectors.forEach(selector => {
                    const field = form.querySelector(selector);
                    if (field) {
                        field.type = this.checked ? 'text' : 'password';
                    }
                });
            });
        }
    }
});