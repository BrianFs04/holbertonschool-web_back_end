const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'UTF-8', (err, data) => {
    if (err) {
      reject(Error('Cannot load the database'));
      return;
    }
    const columns = data.split('\n').slice(1, data.length);
    let count = 0;
    const fields = {};
    const msg = [];
    for (const rows of columns) {
      if (rows) count += 1;
      const row = rows.split(',');
      if (!fields[row[3]] && row[3]) {
        fields[row[3]] = [];
      }
      if (row[0]) {
        fields[row[3]].push(row[0]);
      }
    }
    msg.push(`Number of students: ${count}`);
    for (const [key, values] of Object.entries(fields)) {
      msg.push(`Number of students in ${key}: ${values.length}. List: ${values.join(', ')}`);
    }
    console.log(msg.join('\n'));
    resolve(msg.join('\n'));
  });
});

module.exports = countStudents;
