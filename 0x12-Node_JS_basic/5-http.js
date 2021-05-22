const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const data = await countStudents(process.argv[2]);
      res.end(`This is the list of students\n${data}`);
    } catch (err) {
      res.end(err.message);
    }
    res.end();
  }
}).listen(1245);

module.exports = app;
