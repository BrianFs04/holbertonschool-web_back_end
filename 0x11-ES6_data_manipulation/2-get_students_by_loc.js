import getListStudents from './0-get_list_students';

const getStudentsByLocation = (studentsList, city) => studentsList.filter((student) => student.location === city);

export default getStudentsByLocation;
