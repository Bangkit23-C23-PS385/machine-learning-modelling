def BodyMassIndex(weight, height):
  height = height/100
  bmi = round(weight / (height**2), 2)

  if bmi < 18.5:
    status  = "Berat badan kurang (underweight)"

  elif bmi < 22.9:
    status = "Berat badan normal (normal weight)"

  elif bmi < 24.9:
    status = "Kelebihan berat badan (overweight)"

  elif bmi < 29.9:
    status = "Obesitas I (obese class I)"

  else :
    status = "Obesitas II (obese class II)"

  return bmi, status