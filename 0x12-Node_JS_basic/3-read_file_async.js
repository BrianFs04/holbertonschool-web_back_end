const fs = require('fs');

const countStudents = async (path) => {
  try {
    const data = await fs.promises.readFile(path, { encoding: 'utf8' });
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
      if (row[0]) fields[row[3]].push(row[0]);
    }
    console.log(`Number of students: ${count}`);
    msg.push(`Number of students: ${count}`);
    for (const [key, values] of Object.entries(fields)) {
      if (key) {
        console.log(`Number of students in ${key}: ${values.length}. List: ${values.join(', ')}`);
        msg.push(`Number of students in ${key}: ${values.length}. List: ${values.join(', ')}`);
      }
    }
    return msg.join('\n');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
