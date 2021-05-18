const getListStudentsIds = (arrayObjs) => {
  if (Array.isArray(arrayObjs)) {
    return arrayObjs.map((obj) => obj.id);
  }

  return [];
};

export default getListStudentsIds;
