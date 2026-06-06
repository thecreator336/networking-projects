import socket
import threading

target = "192.168.0.1"
open_ports =[]

known_ports ={
	21: "FTP",
	22: "SSH",
	23: "Telnet",
	25: "SMTP",
	53: "DNS",
	80: "HTTP",
	443: "HTTPS",
	631: "IPP (Printing)",
	3306: "MySQL",
	5432: "PostgreSQL",
	8080: "HTTPS Alt"
}

def scan_port(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((target, port))
	sock.close()
	if result == 0:
		service = known_ports.get(port,"Unknown")
		open_ports.append(port)
		print(f"Port {port} is OPEN = {service}")

print(f"Scanning {target}....\n")

threads =[]
for port in range(1, 1025):
	t = threading.Thread(target=scan_port, args=(port,))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print(f"\nDone! Found {len(open_ports)} open ports")

