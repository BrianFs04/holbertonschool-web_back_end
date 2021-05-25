import fs from 'fs';

const readDatabase = async (file) => {
  try {
    const data = await fs.promises.readFile(file, { encoding: 'utf8' });
    const columns = data.split('\n').slice(1, data.length);
    const fields = {};
    for (const rows of columns) {
      const row = rows.split(',');
      if (!fields[row[3]] && row[3]) {
        fields[row[3]] = [];
      }
      if (row[0]) fields[row[3]].push(row[0]);
    }
    return fields;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

export default readDatabase;
