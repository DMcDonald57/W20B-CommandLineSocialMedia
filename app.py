import dbcreds
import mariadb

conn = mariadb.connect(
            user=dbcreds.user,
            password=dbcreds.password,
            host=dbcreds.host,
            port=dbcreds.port,
            database=dbcreds.database)

cursor = conn.cursor()

print("Welcome Back.\n")
alias = input("Please enter your User Name\n")
password = input("Please enter your Password\n")

def login():
    check = "SELECT id from hackers WHERE alias = %s AND password = %s"
    cursor.execute(check, (alias, password))
    results = cursor.fetchone()
    if results is False:
        print("User not found")
    else:
        id = results[0]
        # print(id)
        print("Welcome Back {}.\n".format(alias))
        print("1. Add a new Exploit")
        print("2. Review your Exploits")
        print("3. See what others have done")
        print("4. Exit\n")

    selection = input("please select:\n")
    return selection

login()