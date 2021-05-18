const getStudentIdsSum = (studentsList) => (
  studentsList.reduce((total, student) => total + student.id, 0)
);

export default getStudentIdsSum;
