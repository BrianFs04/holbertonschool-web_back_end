import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response, file) {
    readDatabase(file)
      .then((fields) => {
        const msg = [];
        msg.push('This is the list of our students');
        for (const [key, values] of Object.entries(fields)) {
          msg.push(`Number of students in ${key}: ${values.length}. List: ${values.join(', ')}`);
        }
        response.status(200).send(`${msg.join('\n')}`);
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response, file) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
    }
    readDatabase(file)
      .then((fields) => {
        const studentsList = fields[major];
        response.status(200).send(`List: ${studentsList.join(', ')}`);
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }
}
