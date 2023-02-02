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
        results[0]
        print("Nice to see you {}.\n".format(alias))
        print("1. Add a new Exploit")
        print("2. Review your Exploits")
        print("3. See what others have done")
        print("4. Exit\n")

    selection = input("please select:\n")
    return selection


def prompt():
    while True:
        selection = 0
        try:          
            selection = int(prompt())
        except ValueError:
            print("Not a number")
            continue
        if selection == 1:
            input("Enter your recent Exploit")
            cursor.execute("CALL add_content")
        # elif selection == 2:
        #     print_exploits()
        # elif selection == 3:
        #     pass
        elif selection ==4:
            print("All done")
            break
        else: 
            print("invalid selection")

    # def add_exploit():
    #     content = input("Enter your recent Exploit")
    #     return content
    #     cursor.execute("INSERT INTO exploits (content) VALUES ('content','user_id')")


login()
prompt()