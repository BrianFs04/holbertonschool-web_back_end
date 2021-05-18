const updateStudentGradeByCity = (studentsList, city, newGrades) => (
  studentsList.filter((student) => student.location === city)
    .map((students) => {
      const grade = newGrades.filter((item) => item.studentId === students.id)
        .map((i) => i.grade)[0] || 'N/A';
      return { ...students, grade };
    })
);

export default updateStudentGradeByCity;
