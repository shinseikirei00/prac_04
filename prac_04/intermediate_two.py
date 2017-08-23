usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("Enter username"))
while username not in usernames:
    print("Access Denied")
    username = str(input("Enter username"))

print("Access Granted")