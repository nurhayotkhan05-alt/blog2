with open("login.txt","r",encoding='utf-8') as f:
    logins = f.read()



print(logins.replace("@","_2026@"))