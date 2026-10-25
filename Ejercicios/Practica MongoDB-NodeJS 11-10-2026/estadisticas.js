globalThis.crypto = require("crypto"); // Libreria requerida segun version de Node.js
const { MongoClient } = require("mongodb");        // cargar la librería
const cliente = new MongoClient("mongodb://127.0.0.1:27017");
 
async function main() {
  try {
    await cliente.connect();                         // conectar
    const libros = cliente.db("biblioteca").collection("libros");
    console.log("conexion correcta");
    //Muestra 1 - numero total de libros
    const total = await libros.countDocuments();
    console.log("Numero total de libros: " + total);
    
    //Muestra 2 - disponibles y prestados     
    const disponibles = await libros.countDocuments({ disponible: true });
    console.log("\n" + "Libros que siguen disponibles:"+ disponibles);
    const prestados = await libros.countDocuments({ disponible: false });
    console.log("Libros que estan prestados:"+ prestados);
    
    // Muestra 3: titulo del libro con mas paginas
    console.log("\n");
    const pagina = await libros.findOne({}, {sort:  { paginas: -1 } });
    if(pagina){
      console.log("libro con mas paginas:" + pagina.titulo);
    }     
 
  } catch (error) {
    console.log("Error: " + error.message);         // si algo falla, lo vemos
  } finally {
    await cliente.close();                           // cerrar siempre la conexión
  }
}
 
main();
