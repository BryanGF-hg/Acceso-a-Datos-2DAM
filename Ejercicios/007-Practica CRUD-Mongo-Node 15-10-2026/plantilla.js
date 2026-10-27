const { MongoClient } = require("mongodb");
const cliente = new MongoClient("mongodb://127.0.0.1:27017");
 
async function main() {
  try {
    await cliente.connect();
    const contactos = cliente.db("agenda").collection("contactos");
 
    // ===== AQUÍ VA EL CÓDIGO DE CADA EJERCICIO =====
 
  } catch (error) {
    console.log("Error: " + error.message);
  } finally {
    await cliente.close();
  }
}
 
main();
