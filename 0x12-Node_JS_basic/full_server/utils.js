import fs from 'fs';

const readDatabase = (file) => new Promise((resolve, reject) => {
  fs.readFile(file, 'UTF-8', (err, data) => {
    if (err) {
      reject(Error('Cannot load the database'));
      return;
    }
    const columns = data.split('\r\n').slice(1, data.length);
    const fields = {};
    for (const rows of columns) {
      const row = rows.split(',');
      if (!fields[row[3]] && row[3]) {
        fields[row[3]] = [];
      }
      if (row[0]) {
        fields[row[3]].push(row[0]);
      }
    }
    resolve(fields);
  });
});

export default readDatabase;
