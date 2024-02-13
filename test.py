import subprocess

command = ['python3', 'main.py']

input_data = '[genz] Hello how are you [http://www.example.com] ?\n'

process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stdout, stderr = process.communicate(input=input_data.encode())

print("Result:");
print(stdout.decode())