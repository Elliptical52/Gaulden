import os, msvcrt, shutil, sys
sys.dont_write_bytecode = True
from root.system.env import reach
os.system('cls')
print('• Requirements imported')
###############
print('System initialized. Boot? (Y/N):', end='', flush=True)
###############
key = None
while not key in (b'y', b'n', b'Y', b'N'): key = msvcrt.getch()
if key == b'n': quit()
###############
cd = 'root/home'
###############
os.system('cls')
print('╔═════════╦═══════════╦══════════════════════╗')
print('║ Gaulden ║ Indev 0.1 ║ `open help` for help ║')
print('╚═════════╩═══════════╩══════════════════════╝')
###############
def tree(dir : str, lvl : int, limit : int):
    if lvl == limit:
        return
    if lvl == 1: print(f'🗀  {dir}')
    for item in os.listdir(dir):
        if os.path.isfile(f'{dir}/{item}'):
            print(f'{'    ' * lvl}🗎  {item}')
        else:
            print(f'{'    ' * lvl}🗀  {item}')
            tree(f'{dir}/{item}', lvl+1, limit)
            
    
###############
while True:
    command = input(f'{cd} ~$').strip().split(' ')
    length = len(command)
    match command[0]:
        case 'var':
            if length == 1:
                print('File env.txt (root/system/env/env.txt):')
                print('╔══════════════════════════════════════════════════╗')
                with open('root/system/env/env.txt') as file:
                    text = file.read()
                    for line in text.split('\n'):
                        print('║ ' + line + (' ' * (49-len(line))) + '║')
                    file.close()
                print('╚══════════════════════════════════════════════════╝')
            elif length == 2:
                print(reach.read('V', command[1]))
            elif length > 2:
                match command[1]:
                    case 'read':
                        print(reach.read('V', command[2]))
                    case 'write':
                        reach.read('V', command[2], command[3])
                        print(f"Wrote '{command[3]}' to variable '{command[2]}'")
        case 'clear'|'cls':
            os.system('cls')
            print('╔═════════╦═══════════╦══════════════════════╗')
            print('║ Gaulden ║ Indev 0.1 ║ `open help` for help ║')
            print('╚═════════╩═══════════╩══════════════════════╝')
        case 'cd':
            if length == 1:
                cd = 'root/home'
            else:
                match command[1]:
                    case '..':
                        cd = '/'.join(cd.split("/")[0:-1])
                    case '_':
                        cd = command[2]
                    case _:
                        cd = f'{cd}/{command[1]}'
        case 'new':
            if command[1] == 'dir':
                for i in range(2, length):
                    os.mkdir(f'{cd}/{command[i]}')
                    print(f"Created directory '{command[i]}'")
            elif command[1] == 'file':
                for i in range(2, length):
                    open(f'{cd}/{command[i]}', 'a').close()
                    print(f"Created file '{command[i]}'")
            else:
                for i in range(1, length):
                    open(f'{cd}/{command[i]}', 'a').close()
                    print(f"Created file '{command[i]}'")
        case 'delete'|'del':
            for i in range(1, length):
                if os.path.isfile(f'{cd}/{command[i]}'):
                    os.remove(f'{cd}/{command[i]}')
                    print(f"Deleted file '{command[i]}'")
                elif os.path.isdir(f'{cd}/{command[i]}'):
                    shutil.rmtree(f'{cd}/{command[i]}')
                    print(f"Deleted directory '{command[i]}'")
        case 'ls':
            dir, file = True, True
            if length == 2:
                if command[1] == 'dir': dir = True; file = False
                else: file = True; dir = False
            for item in os.listdir(cd):
                if os.path.isfile(f'{cd}/{item}'):
                    if file: print(f'🗎  {item}')
                else:
                    if dir: print(f'🗀  {item}')
        
        case 'tree':
            if length == 2:
                tree(cd, 1, int(command[1]) + 1)
            else:
                tree(cd, 1, -1)

###############
# python main.py