## Router Reconnaissance Exercise

Performed a basic network reconnaissance exercise against my home router
(192.168.0.1) as a learning exercise on my own network.

### Steps taken:
1. **Port scanning** — discovered 4 open ports: 22, 53, 80, 443
2. **Service identification** — mapped ports to services (SSH, DNS, HTTP, HTTPS)
3. **SSH fingerprinting** — identified router was running outdated key exchange
   algorithms (diffie-hellman-group1-sha1, ssh-dss) flagged as weak by
   modern SSH clients
4. **Authentication attempt** — attempted login with default credentials,
   access denied (router uses non-default credentials)

### Findings:
- Router exposes SSH on port 22 to all LAN clients — likely for ISP remote management
- Outdated SSH algorithms suggest old firmware — potential security concern
- Default credentials not in use — good security practice by ISP

### Key learning:
This is exactly what steps 1-4 of a real penetration test look like:
reconnaissance → port scanning → service enumeration → credential testing.
All performed on own network for educational purposes.
