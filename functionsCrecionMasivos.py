
def recorrerDF (df):

    for index, row in df.iterrows():
        userName = row['nombres']
        userLastName = row['apellidos']
        userId = row['CC']
        birthDate = row['fechaNacimiento']
        channel = row['canal']
        region = row['regional']
        company = row['empresa']
        email = row['correo']
        position = row['cargo']
        
        print(userName)
        print(userLastName)
        print(userId)
        print(birthDate)
        print(channel)
        print(region)
        print(company)
        print(email)
        print(position)
        
def userID():
    return '1015465005'
    
def userPass():
    return 'Con31415*'