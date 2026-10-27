globalThis.crypto = require("crypto"); // Libreria requerida segun version de Node.js
const { MongoClient } = require("mongodb");        // cargar la librería
const cliente = new MongoClient("mongodb://127.0.0.1:27017");
 
async function main() {
  try {
    await cliente.connect();                         // conectar
    const libros = cliente.db("biblioteca").collection("libros");
    console.log("Conexion correcta");
    const lista = await libros.find().sort({ anio: 1 }).toArray();
    for (const libro of lista) {
      console.log(libro.titulo);
    }      
 
  } catch (error) {
    console.log("Error: " + error.message);         // si algo falla, lo vemos
  } finally {
    await cliente.close();                           // cerrar siempre la conexión
  }
}
 
main();
