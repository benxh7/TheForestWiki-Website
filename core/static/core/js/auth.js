document.addEventListener("DOMContentLoaded", function () {
    /* FUNCIONAMIENTO PARA EL FORMULARIO REGISTRARSE */
    const formularioRegistro = document.querySelector("#registerModal form");
    if (formularioRegistro) {
        const nombreCompleto = formularioRegistro.querySelector("#nombre-completo");
        const nombreUsuario = formularioRegistro.querySelector("#nombre-usuario");
        const email = formularioRegistro.querySelector("#correo");
        const fechaNacimiento = formularioRegistro.querySelector("#fecha-nacimiento");
        const direccion = formularioRegistro.querySelector("#direccion");
        const contraseña = formularioRegistro.querySelector("#contraseña");
        const confirmarContraseña = formularioRegistro.querySelector("#confirmar");
        const limpiarBtn = formularioRegistro.querySelector("#limpiarBtn");

        // Botón para limpiar el formulario y remover mensajes de error
        if (limpiarBtn) {
            limpiarBtn.addEventListener("click", function () {
                // Limpiamos el formulario y removemos los mensajes de error de los campos
                formularioRegistro.querySelectorAll(".is-invalid").forEach(el => el.classList.remove("is-invalid"));
                formularioRegistro.querySelectorAll(".invalid-feedback").forEach(el => el.remove());
                // Limpiamos los campos del formulario
                nombreCompleto.value = "";
                nombreUsuario.value = "";
                email.value = "";
                fechaNacimiento.value = "";
                direccion.value = "";
                contraseña.value = "";
                confirmarContraseña.value = "";
                // Reiniciamos el formulario
                formularioRegistro.reset();
                limpiarErrores(formularioRegistro);
            });
        }

        // Evento submit del formulario de registro
        formularioRegistro.addEventListener("submit", function (event) {
            event.preventDefault();
            limpiarErrores(formularioRegistro);
            let isValid = true;

            // Lista de verificacio de cada campo
            if (!nombreCompleto.value.trim()) {
                mostrarError(nombreCompleto, "El nombre completo es obligatorio.", formularioRegistro);
                isValid = false;
            }
            if (!nombreUsuario.value.trim()) {
                mostrarError(nombreUsuario, "El nombre de usuario es obligatorio.", formularioRegistro);
                isValid = false;
            }
            if (!email.value.trim() || !validarCorreo(email.value)) {
                mostrarError(email, "Ingrese un correo válido.", formularioRegistro);
                isValid = false;
            }
            if (!fechaNacimiento.value || !validarEdad(fechaNacimiento.value)) {
                mostrarError(fechaNacimiento, "Debe tener al menos 13 años.", formularioRegistro);
                isValid = false;
            }
            // Este campo como se decia en la semana 2 es opcional
            if (!contraseña.value.trim() || !validarContraseña(contraseña.value)) {
                mostrarError(contraseña, "La contraseña debe tener 6-18 caracteres, incluir una mayúscula y un número.", formularioRegistro);
                isValid = false;
            }
            if (contraseña.value !== confirmarContraseña.value) {
                mostrarError(confirmarContraseña, "Las contraseñas no coinciden.", formularioRegistro);
                isValid = false;
            }

            // Si todas las verificaciones son validas, se simula el envío (en este caso mediante redirección)
            if (isValid) {
                const params = new URLSearchParams(new FormData(formularioRegistro)).toString();
                const url = (formularioRegistro.getAttribute("action") || "#") + "?" + params;
                window.location.href = url;
            }
        });
    }

    /* FUNCIONAMIENTO PARA EL FORMULARIO INICIAR SESION */
    const formularioLogin = document.querySelector("#loginForm");
    if (formularioLogin) {
        // Referencias a los elementos del formulario de login
        const usuarioLogin = formularioLogin.querySelector("#username");
        const contraseñaLogin = formularioLogin.querySelector("#password");
        
        // Evento para mostrar/ocultar la contraseña
        const showPasswordCheckbox = document.getElementById('showPassword');
        if (showPasswordCheckbox) {
            showPasswordCheckbox.addEventListener('change', function() {
                contraseñaLogin.type = this.checked ? 'text' : 'password';
            });
        }
        
        // Evento submit del formulario de login
        formularioLogin.addEventListener("submit", function (event) {
            event.preventDefault();
            limpiarErrores(formularioLogin);
            let isValid = true;

            if (!usuarioLogin.value.trim()) {
                mostrarError(usuarioLogin, "El usuario o correo es obligatorio.", formularioLogin);
                isValid = false;
            }
            if (!contraseñaLogin.value.trim()) {
                mostrarError(contraseñaLogin, "La contraseña es obligatoria.", formularioLogin);
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
                        const params = new URLSearchParams(new FormData(formularioLogin)).toString();
                        const url = formularioLogin.getAttribute("action") ? 
                                    formularioLogin.getAttribute("action") + "?" + params : homeUrl;
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

    // Validación de edad (al menos 13 años)
    function validarEdad(fecha) {
        const birthDate = new Date(fecha);
        const today = new Date();
        let age = today.getFullYear() - birthDate.getFullYear();
        const m = today.getMonth() - birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age >= 13;
    }

    // Validación de contraseña: 6-18 caracteres, al menos una mayúscula y un dígito
    function validarContraseña(password) {
        const regex = /^(?=.*[A-Z])(?=.*\d)[\S]{6,18}$/;
        return regex.test(password);
    }

    // Ventana de añadir juego
    let submitTriggered = false;

    const formAñadirJuego = document.getElementById("formAñadirJuego");
    if (formAñadirJuego) {
        formAñadirJuego.addEventListener("submit", function (e) {
            e.preventDefault();
            // Obtener valores y eliminar espacios en blanco
            const titulo = document.getElementById("tituloJuego").value.trim();
            const descripcion = document.getElementById("descripcionJuego").value.trim();
            const precio = document.getElementById("precioJuego").value.trim();
            const stock = document.getElementById("stockJuego").value.trim();

            // Verificar que ningún campo esté vacío
            if (titulo === "" || descripcion === "" || precio === "" || stock === "") {
                document.getElementById("alertaJuego").innerHTML =
                    '<div class="alert alert-danger alert-dismissible fade show" role="alert">' +
                    'Por favor, complete todos los campos para publicar el juego.' +
                    '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                    '</div>';
                return;
            }

            // Si todos los campos tienen datos, se considera que se publicó el juego
            submitTriggered = true;
            document.getElementById("alertaJuego").innerHTML =
                '<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                'Juego publicado exitosamente.' +
                '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                '</div>';
            // Limpiar el formulario (esto disparará el evento reset)
            this.reset();
        });

        // Evento reset para mostrar mensaje al eliminar datos manualmente
        formAñadirJuego.addEventListener("reset", function (e) {
            // Si el reset es producto del submit, no mostramos el mensaje de "eliminar"
            if (submitTriggered) {
                submitTriggered = false;
                return;
            }
            document.getElementById("alertaJuego").innerHTML =
                '<div class="alert alert-warning alert-dismissible fade show" role="alert">' +
                'Los datos han sido eliminados.' +
                '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                '</div>';
        });
    }

    // Ventana de editar juego
    let submitTriggeredEditar = false;
    const formEditarJuego = document.getElementById("formEditarJuego");
    if (formEditarJuego) {
        formEditarJuego.addEventListener("submit", function (e) {
            e.preventDefault();
            // Obtenemos los valores de los campos de edicion y eliminamos los espacios en blanco
            const juegoSeleccionado = document.getElementById("juegoSeleccionado").value;
            const tituloEd = document.getElementById("tituloJuegoEd").value.trim();
            const descripcionEd = document.getElementById("descripcionJuegoEd").value.trim();
            const precioEd = document.getElementById("precioJuegoEd").value.trim();
            const stockEd = document.getElementById("stockJuegoEd").value.trim();

            // Validamos que hayamos seleccionado un juego y que todos los campos tengan datos
            if (
                !juegoSeleccionado ||
                tituloEd === "" ||
                descripcionEd === "" ||
                precioEd === "" ||
                stockEd === ""
            ) {
                document.getElementById("alertaEditar").innerHTML =
                    '<div class="alert alert-danger alert-dismissible fade show" role="alert">' +
                    'Por favor, seleccione un juego y complete todos los campos para editar.' +
                    '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                    '</div>';
                return;
            }

            // Si la validacion es correcta, se muestra el mensaje
            submitTriggeredEditar = true;
            document.getElementById("alertaEditar").innerHTML =
                '<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                'Cambios guardados exitosamente.' +
                '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                '</div>';
            // Limpiar el formulario
            this.reset();
        });

        // Evento reset para el formulario de edicion
        formEditarJuego.addEventListener("reset", function (e) {
            if (submitTriggeredEditar) {
                submitTriggeredEditar = false;
                return;
            }
            document.getElementById("alertaEditar").innerHTML =
                '<div class="alert alert-warning alert-dismissible fade show" role="alert">' +
                'Los datos han sido eliminados.' +
                '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
                '</div>';
        });
    }
});