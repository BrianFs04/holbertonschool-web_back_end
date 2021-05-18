import getListStudents from './0-get_list_students';

const getStudentsByLocation = () => getListStudents().filter((student) => student.location === 'San Francisco');

export default getStudentsByLocation;
