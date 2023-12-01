# config.py
# Author: Jason Howe
# Communications file for Sparrow

import socket
import config
import ssl

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import dsa

def create_socket() -> socket.socket:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((config.IP, config.PORT))
    conn.listen(10)
    return conn
    

def create_secure_socket() -> socket.socket:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.SSLContext()
    context.verify_mode=ssl.CERT_NONE
    context.load_cert_chain(certfile=config.CERTFILE, keyfile=config.KEYFILE, password=None)
    s_conn = context.wrap_socket(conn, server_side=True)
    s_conn.bind((config.IP, config.PORT))
    s_conn.listen(10)
    return s_conn


def recieve(conn: socket.socket) -> str:
    try: 
        conn.settimeout(2)
        d = ""
        while True:
            chunk = conn.recv(1024).decode()
            if not chunk:
                break
            d += chunk
    except:
        pass
    return d


def send(conn: socket.socket, response: str) -> str:
    conn.sendall(response.encode())
    conn.close()


def parse_certs():
    # Load the X.509 certificate and private key from files
    with open(config.CERTFILE, 'rb') as cert_file:
        cert_data = cert_file.read()

    with open(config.KEYFILE, 'rb') as key_file:
        key_data = key_file.read()

    # Parse the X.509 certificate
    certificate = x509.load_pem_x509_certificate(cert_data, default_backend())

    # Parse the private key
    private_key = serialization.load_pem_private_key(key_data, password=None, backend=default_backend())

    # Validate the certificate and private key
    # Check that the private key matches the public key in the certificate
    if isinstance(private_key, rsa.RSAPrivateKey) and certificate.public_key().public_numbers() == private_key.public_key().public_numbers():
        print("Certificate and private key are a valid pair for RSA.")
    elif isinstance(private_key, ec.EllipticCurvePrivateKey) and certificate.public_key().public_numbers() == private_key.public_key().public_numbers():
        print("Certificate and private key are a valid pair for ECC.")
    elif isinstance(private_key, dsa.DSAPrivateKey) and certificate.public_key().public_numbers() == private_key.public_key().public_numbers():
        print("Certificate and private key are a valid pair for DSA.")
    else:
        print("Certificate and private key do not match.")

