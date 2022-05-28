name="Sai arun kumar"
flight='boing 670'


def printBoardingpass(name, flight):
  name_lenght = len(name)
  first_name=name[0:name_lenght:name_lenght-1]
  boading_pass=first_name+flight
  return boading_pass.upper().replace(" ", "")
  
print(printBoardingpass(name, flight))
