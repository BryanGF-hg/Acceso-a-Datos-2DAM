globalThis.crypto = require("crypto"); // Libreria requerida segun version de Node.js
const { MongoClient } = require("mongodb");        // cargar la librería
const cliente = new MongoClient("mongodb://127.0.0.1:27017");
 
async function main() {
  try {
    await cliente.connect();                         // conectar
    const libros = cliente.db("biblioteca").collection("libros");
    console.log("Conexion correcta");
    const resultado = await libros.insertOne({ titulo: "Nada", autora: "Carmen Laforet", anyo: 1945, genero: "novela", paginas: 288, disponible: true, ejemplar: 1 });
    console.log("Esto es la insercion usada:" + resultado.insertedId.toString());
 
    // Buscar el libro recién insertado por título
    const libroGuardado = await libros.findOne({ titulo: "Nada" });
    console.log("Libro encontrado:", libroGuardado);
 
  } catch (error) {
    console.log("Error: " + error.message);         // si algo falla, lo vemos
  } finally {
    await cliente.close();                           // cerrar siempre la conexión
  }
}
 
main();
