const getStudentsByLocation = (studentsList, city) => (
  studentsList.filter((student) => student.location === city)
);

export default getStudentsByLocation;
