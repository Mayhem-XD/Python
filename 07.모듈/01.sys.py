import sys

print(sys.getwindowsversion())

print(len(sys.argv))
print(sys.argv)

while True:
    cmd = input('prompt> ')
    if cmd == 'exit':
        sys.exit()
    print(cmd)