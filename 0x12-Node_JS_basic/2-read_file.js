const fs = require('fs');

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, { encoding: 'utf8' }).split('\r\n');
    const columns = data.slice(1, data.length);
    let count = 0;
    const fields = {};
    for (const rows of columns) {
      if (rows) count += 1;
      const row = rows.split(',');
      if (!fields[row[3]]) {
        fields[row[3]] = [];
      }
      if (row[0]) fields[row[3]].push(row[0]);
    }
    console.log(`Number of students: ${count}`);
    for (const [key, values] of Object.entries(fields)) {
      if (key && values.length) {
        console.log(`Number of students in ${key}: ${values.length}. List: ${values.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
