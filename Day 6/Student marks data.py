data={
    'adithya':{'status':True,'Python':95,'Flask':90, 'mysql':85},
    'sudheer':{'status':True,'Python':70,'Flask':75, 'mysql':79},
    'Prudhvi':{'status':True,'Python':50,'Flask':55, 'mysql':59},
    'Teja':{'status':True,'Python':35,'Flask':40, 'mysql':45},
    'Virat':{'status':False,'Python':None,'Flask':None, 'mysql':None}
}
name = input("Enter the student name:")
if name in data:
    if data[name]['status']:
        sum = data[name]['Python'] + data[name]['Flask'] + data[name]['mysql']
        avg = sum / 3
        if avg >= 90:
            print(f"Congratulations {name}, you got an A grade!")
        elif avg >= 80:
            print(f"Good job {name}, you got a B grade.")
        elif avg >= 70:
            print(f"Great effort {name}, you got a C grade.")
        elif avg >= 60:
            print(f"Keep it up {name}, you got a D grade.")
        else:
            print(f"Sorry {name}, you got an F grade.")
