const formulario = document.getElementById("producto-form");
const tabla = document.getElementById("tabla-productos");
const mensaje = document.getElementById("mensaje");
const productoId = document.getElementById("producto-id");
const nombre = document.getElementById("nombre");
const precio = document.getElementById("precio");
const categoria = document.getElementById("categoria");
const stock = document.getElementById("stock");
const tituloFormulario = document.getElementById("titulo-formulario");
const btnGuardar = document.getElementById("btn-guardar");
const btnCancelar = document.getElementById("btn-cancelar");
const btnRecargar = document.getElementById("btn-recargar");

async function cargarProductos() {
    try {
        const respuesta = await fetch("/api/productos");
        const productos = await respuesta.json();
        tabla.innerHTML = "";
        productos.forEach(producto => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${producto.id}</td>
                <td>${producto.nombre}</td>
                <td>$${producto.precio.toLocaleString("es-CL")}</td>
                <td>${producto.categoria}</td>
                <td>${producto.stock}</td>
                <td>
                    <button class="editar" onclick='editarProducto(${JSON.stringify(producto)})'>Editar</button>
                    <button class="eliminar" onclick="eliminarProducto(${producto.id})">Eliminar</button>
                </td>`;
            tabla.appendChild(fila);
        });
    } catch (error) {
        mostrarMensaje("No se pudo cargar la lista.", true);
    }
}

formulario.addEventListener("submit", async function(evento) {
    evento.preventDefault();
    const datos = {
        nombre: nombre.value.trim(),
        precio: Number(precio.value),
        categoria: categoria.value.trim(),
        stock: Number(stock.value)
    };
    const id = productoId.value;
    try {
        let respuesta;
        if (id) {
            respuesta = await fetch(`/api/productos/${id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(datos)
            });
        } else {
            respuesta = await fetch("/api/productos", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(datos)
            });
        }
        const resultado = await respuesta.json();
        if (!respuesta.ok) throw new Error(resultado.detail || "Ocurrió un error.");
        mostrarMensaje(id ? "Producto actualizado correctamente." : "Producto creado correctamente.");
        limpiarFormulario();
        await cargarProductos();
    } catch (error) {
        mostrarMensaje(error.message, true);
    }
});

function editarProducto(producto) {
    productoId.value = producto.id;
    nombre.value = producto.nombre;
    precio.value = producto.precio;
    categoria.value = producto.categoria;
    stock.value = producto.stock;
    tituloFormulario.textContent = "Editar producto";
    btnGuardar.textContent = "Actualizar producto";
    btnCancelar.classList.remove("oculto");
    window.scrollTo({ top: 0, behavior: "smooth" });
}

async function eliminarProducto(id) {
    if (!confirm("¿Está seguro de que desea eliminar este producto?")) return;
    try {
        const respuesta = await fetch(`/api/productos/${id}`, { method: "DELETE" });
        const resultado = await respuesta.json();
        if (!respuesta.ok) throw new Error(resultado.detail || "Ocurrió un error.");
        mostrarMensaje(resultado.mensaje);
        await cargarProductos();
    } catch (error) {
        mostrarMensaje(error.message, true);
    }
}

function limpiarFormulario() {
    formulario.reset();
    productoId.value = "";
    tituloFormulario.textContent = "Agregar producto";
    btnGuardar.textContent = "Guardar producto";
    btnCancelar.classList.add("oculto");
}

function mostrarMensaje(texto, error = false) {
    mensaje.textContent = texto;
    mensaje.style.color = error ? "#dc2626" : "#16a34a";
    setTimeout(() => { mensaje.textContent = ""; }, 3000);
}

btnCancelar.addEventListener("click", limpiarFormulario);
btnRecargar.addEventListener("click", cargarProductos);
cargarProductos();
