
import socket

def is_ip_blacklisted_zen(ip_address):
    try:
        # Perform a DNS query to the Spamhaus Zen server
        query = '.'.join(reversed(ip_address.split("."))) + ".zen.spamhaus.org"
        socket.gethostbyname(query)
        return True
    except:
        return False

ip_address = "206.226.32.1" # Example IP address
if is_ip_blacklisted_zen(ip_address):
    print(f"{ip_address} is blacklisted on Spamhaus Zen.")
else:
    print(f"{ip_address} is not blacklisted on Spamhaus Zen.")
