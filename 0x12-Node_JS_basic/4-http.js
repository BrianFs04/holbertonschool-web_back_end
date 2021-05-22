const http = require('http');

const app = http.createServer((req, res) => {
  const body = 'Hello Holberton School!';
  res.writeHead(200, { 'Content-Type': 'text/plain' }).end(body);
}).listen(1245);

module.exports = app;
