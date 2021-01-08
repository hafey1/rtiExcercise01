//function to create columns for data
export function columnCreate(columnArray) {
  const displayColumn = columnArray.map(ele => {
    let rObj = {
      id: ele,
      label: ele.charAt(0).toUpperCase() + ele.slice(1),
      minWidth: 150,
      align: "right",
      format: value => value.toLocaleString("en-US")
    };
    return rObj;
  });
  console.log(displayColumn);
  return displayColumn;
}

export function createData(r) {
  let id = r.id;
  let hours_week = r.hours_week;
  let capital_gain = r.capital_gain;
  let capital_loss = r.capital_loss;
  let over_50k = r.over_50k;
  let age = r.age;
  let education_num = r.education_num;
  let educational_level = r.educational_level;
  let workclass = r.workclass;
  let marital_status = r.marital_status;
  let occupation = r.occupation;
  let race = r.race;
  let sex = r.sex;
  let country = r.country;
  let relationship = r.relationship;

  return {
    id,
    hours_week,
    capital_gain,
    capital_loss,
    over_50k,
    age,
    education_num,
    educational_level,
    workclass,
    marital_status,
    occupation,
    race,
    sex,
    country,
    relationship
  };
}
