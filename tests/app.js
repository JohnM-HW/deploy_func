const admin = require('firebase-admin');
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;


// Get a reference to the Firestore database
const db = admin.firestore();

// Retrieve and display data from the "deployments" collection
db.collection('deployments')
  .get()
  .then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
      console.log(`Document ID: ${doc.id}`);
      console.log(`Data:`, doc.data());
      console.log('---');
    });
  })
  .catch((error) => {
    console.error('Error retrieving data:', error);
  });


const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
// Initialize the Firebase Admin SDK
// const serviceAccount = require('./path/to/serviceAccountKey.json');
// admin.initializeApp({
//   credential: admin.credential.cert(serviceAccount)
// });



