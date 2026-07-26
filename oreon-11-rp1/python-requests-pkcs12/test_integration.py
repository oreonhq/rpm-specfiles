# SPDX-License-Identifier: MIT
import http.server
import os
import ssl
import subprocess
import threading
import unittest

import requests
import requests_pkcs12
import urllib3.util

# --- Configuration ---
HOST = "localhost"
IP_ADDRESS = "127.0.0.1"
PORT = 9443

# --- File Names ---
ROOT_CA_KEY = "test_rootCA.key"
ROOT_CA_CSR = "test_rootCA.csr"
ROOT_CA_PEM = "test_rootCA.pem"
SERVER_KEY = "test_server.key"
SERVER_CSR = "test_server.csr"
SERVER_CERT = "test_server.crt"
CLIENT_KEY = "test_client.key"
CLIENT_CSR = "test_client.csr"
CLIENT_CERT = "test_client.crt"
CLIENT_P12_NO_PWD = "test_client_no_pwd.p12"
CLIENT_P12_WITH_PWD = "test_client_with_pwd.p12"
CA_V3_EXT_FILE = "ca_v3.ext"
SERVER_V3_EXT_FILE = "server_v3.ext"
P12_PASSWORD = "testpassword"

GENERATED_FILES = [
    ROOT_CA_KEY,
    ROOT_CA_CSR,
    ROOT_CA_PEM,
    SERVER_KEY,
    SERVER_CSR,
    SERVER_CERT,
    CLIENT_KEY,
    CLIENT_CSR,
    CLIENT_CERT,
    CLIENT_P12_NO_PWD,
    CLIENT_P12_WITH_PWD,
    CA_V3_EXT_FILE,
    SERVER_V3_EXT_FILE,
    "test_rootCA.srl",
]


def run_command(args):
    """Helper function to run a shell command as a list of arguments."""
    subprocess.run(args, check=True)


class TestMTLSClient(unittest.TestCase):
    """Test suite for mTLS client connections with an embedded server."""

    httpd = None
    server_thread = None

    @staticmethod
    def _start_embedded_server():
        """Creates and returns a configured HTTPServer instance."""
        server_address = (IP_ADDRESS, PORT)

        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=SERVER_CERT, keyfile=SERVER_KEY)
        context.load_verify_locations(cafile=ROOT_CA_PEM)
        context.verify_mode = ssl.CERT_REQUIRED

        httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

        return httpd

    @classmethod
    def setUpClass(cls):
        """Set up the test environment: generate certs and start the server."""
        print("--- Setting up test environment ---")

        # 1. Create the v3.ext files and generate all certificates
        print("Generating certificates...")

        with open(CA_V3_EXT_FILE, "w") as f:
            f.write("subjectKeyIdentifier=hash\n")
            f.write("authorityKeyIdentifier=keyid:always,issuer\n")
            f.write("basicConstraints = critical,CA:TRUE\n")
            f.write("keyUsage = critical,digitalSignature,cRLSign,keyCertSign\n")

        with open(SERVER_V3_EXT_FILE, "w") as f:
            f.write("authorityKeyIdentifier=keyid,issuer\n")
            f.write("basicConstraints=CA:FALSE\n")
            f.write("subjectAltName = @alt_names\n\n[alt_names]\n")
            f.write(f"DNS.1 = {HOST}\nIP.1 = {IP_ADDRESS}\n")

        run_command(['openssl', 'genrsa', '-out', ROOT_CA_KEY, '4096'])
        run_command(
            [
                'openssl',
                'req',
                '-new',
                '-key',
                ROOT_CA_KEY,
                '-out',
                ROOT_CA_CSR,
                '-subj',
                '/C=ZZ/O=Test/CN=Test Root CA',
            ]
        )
        run_command(
            [
                'openssl',
                'x509',
                '-req',
                '-in',
                ROOT_CA_CSR,
                '-signkey',
                ROOT_CA_KEY,
                '-out',
                ROOT_CA_PEM,
                '-days',
                '31',
                '-sha512',
                '-extfile',
                CA_V3_EXT_FILE,
            ]
        )

        run_command(['openssl', 'genrsa', '-out', SERVER_KEY, '2048'])
        run_command(
            [
                'openssl',
                'req',
                '-new',
                '-key',
                SERVER_KEY,
                '-out',
                SERVER_CSR,
                '-subj',
                f'/C=ZZ/O=Test/CN={HOST}',
            ]
        )
        run_command(
            [
                'openssl',
                'x509',
                '-req',
                '-in',
                SERVER_CSR,
                '-CA',
                ROOT_CA_PEM,
                '-CAkey',
                ROOT_CA_KEY,
                '-CAcreateserial',
                '-out',
                SERVER_CERT,
                '-days',
                '7',
                '-sha512',
                '-extfile',
                SERVER_V3_EXT_FILE,
            ]
        )
        run_command(['openssl', 'genrsa', '-out', CLIENT_KEY, '2048'])
        run_command(
            [
                'openssl',
                'req',
                '-new',
                '-key',
                CLIENT_KEY,
                '-out',
                CLIENT_CSR,
                '-subj',
                '/C=ZZ/O=Test/CN=Test Client',
            ]
        )
        run_command(
            [
                'openssl',
                'x509',
                '-req',
                '-in',
                CLIENT_CSR,
                '-CA',
                ROOT_CA_PEM,
                '-CAkey',
                ROOT_CA_KEY,
                '-CAcreateserial',
                '-out',
                CLIENT_CERT,
                '-days',
                '7',
                '-sha512',
            ]
        )
        run_command(
            [
                'openssl',
                'pkcs12',
                '-export',
                '-out',
                CLIENT_P12_NO_PWD,
                '-inkey',
                CLIENT_KEY,
                '-in',
                CLIENT_CERT,
                '-passout',
                'pass:',
            ]
        )
        run_command(
            [
                'openssl',
                'pkcs12',
                '-export',
                '-out',
                CLIENT_P12_WITH_PWD,
                '-inkey',
                CLIENT_KEY,
                '-in',
                CLIENT_CERT,
                '-passout',
                f'pass:{P12_PASSWORD}',
            ]
        )
        print("Certificates generated successfully.")

        # 2. Start the embedded mTLS server in a background thread
        print(f"Starting embedded server on https://{IP_ADDRESS}:{PORT}")
        cls.httpd = cls._start_embedded_server()

        cls.server_thread = threading.Thread(target=cls.httpd.serve_forever)
        cls.server_thread.daemon = (
            True  # Allows main thread to exit even if server thread is running
        )
        cls.server_thread.start()

        print("Server is running in a background thread.")

        if hasattr(urllib3.util, 'IS_SECURETRANSPORT'):
            print(f"urllib3 version {urllib3.__version__} has IS_SECURETRANSPORT.")
            print("Forcing to True to pass IP as server_hostname.")
            urllib3.util.ssl_.IS_SECURETRANSPORT = True

    @classmethod
    def tearDownClass(cls):
        """Clean up the environment: stop the server and delete files."""
        print("\n--- Tearing down test environment ---")
        if cls.httpd:
            print("Shutting down embedded server...")
            cls.httpd.shutdown()
            cls.server_thread.join()
            print("Server stopped.")

        print("Cleaning up generated files...")
        for f in GENERATED_FILES:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass
        print("Cleanup complete.")

    def test_requests_pem_cert_with_hostname(self):
        """Tests connection to localhost using PEM certificate and key."""
        url = f"https://{HOST}:{PORT}"

        response = requests.get(url, cert=(CLIENT_CERT, CLIENT_KEY), verify=ROOT_CA_PEM, timeout=10)
        self.assertEqual(response.status_code, 200)

    def test_requests_pem_cert_with_ip(self):
        """Tests connection to 127.0.0.1 using PEM certificate and key."""
        url = f"https://{IP_ADDRESS}:{PORT}"

        response = requests.get(url, cert=(CLIENT_CERT, CLIENT_KEY), verify=ROOT_CA_PEM, timeout=10)
        self.assertEqual(response.status_code, 200)

    def test_requests_nocert_with_hostname(self):
        """Tests connection to localhost without client certificate."""
        url = f"https://{HOST}:{PORT}"

        with self.assertRaises(requests.exceptions.SSLError) as cm:
            requests.get(url, verify=ROOT_CA_PEM, timeout=10)

        exc = cm.exception
        self.assertIn("alert certificate required", str(exc))

    def test_requests_nocert_with_ip(self):
        """Tests connection to localhost without client certificate."""
        url = f"https://{IP_ADDRESS}:{PORT}"

        with self.assertRaises(requests.exceptions.SSLError) as cm:
            requests.get(url, verify=ROOT_CA_PEM, timeout=10)

        exc = cm.exception
        self.assertIn("alert certificate required", str(exc))

    def test_requests_pkcs12_with_password_and_hostname(self):
        """Tests connection using a password-protected PKCS12 file."""
        url = f"https://{HOST}:{PORT}"

        response = requests_pkcs12.get(
            url,
            pkcs12_filename=CLIENT_P12_WITH_PWD,
            pkcs12_password=P12_PASSWORD,
            verify=ROOT_CA_PEM,
            timeout=10,
        )
        self.assertEqual(response.status_code, 200)

    def test_requests_pkcs12_with_password_and_ip(self):
        """Tests connection using a password-protected PKCS12 file."""
        url = f"https://{IP_ADDRESS}:{PORT}"

        response = requests_pkcs12.get(
            url,
            pkcs12_filename=CLIENT_P12_WITH_PWD,
            pkcs12_password=P12_PASSWORD,
            verify=ROOT_CA_PEM,
            timeout=10,
        )
        self.assertEqual(response.status_code, 200)

    def test_requests_pkcs12_without_password_and_hostname(self):
        """Tests connection using a PKCS12 file with an empty password."""
        url = f"https://{HOST}:{PORT}"

        response = requests_pkcs12.get(
            url,
            pkcs12_filename=CLIENT_P12_NO_PWD,
            pkcs12_password="",
            verify=ROOT_CA_PEM,
            timeout=10,
        )
        self.assertEqual(response.status_code, 200)

    def test_requests_pkcs12_without_password_and_ip(self):
        """Tests connection using a PKCS12 file with an empty password."""
        url = f"https://{IP_ADDRESS}:{PORT}"

        response = requests_pkcs12.get(
            url,
            pkcs12_filename=CLIENT_P12_NO_PWD,
            pkcs12_password="",
            verify=ROOT_CA_PEM,
            timeout=10,
        )
        self.assertEqual(response.status_code, 200)

    def test_requests_pkcs12_with_password_none_and_hostname(self):
        """Tests connection using a PKCS12 file with None as password."""
        url = f"https://{HOST}:{PORT}"

        response = requests_pkcs12.get(
            url,
            pkcs12_filename=CLIENT_P12_NO_PWD,
            pkcs12_password=None,
            verify=ROOT_CA_PEM,
            timeout=10,
        )
        self.assertEqual(response.status_code, 200)

    def test_requests_pkcs12_with_password_none_and_ip(self):
        """Tests connection using a PKCS12 file with None as password."""
        url = f"https://{IP_ADDRESS}:{PORT}"

        response = requests_pkcs12.get(
            url,
            pkcs12_filename=CLIENT_P12_NO_PWD,
            pkcs12_password=None,
            verify=ROOT_CA_PEM,
            timeout=10,
        )
        self.assertEqual(response.status_code, 200)

    def test_requests_pkcs12_without_cert_parameters_and_hostname(self):
        """Tests requests_pkcs12 connection without PKCS12 file."""
        url = f"https://{HOST}:{PORT}"

        with self.assertRaises(requests.exceptions.SSLError) as cm:
            requests_pkcs12.get(url, verify=ROOT_CA_PEM, timeout=10)

        exc = cm.exception
        self.assertIn("alert certificate required", str(exc))

    def test_requests_pkcs12_without_cert_parameters_and_ip(self):
        """Tests requests_pkcs12 connection without PKCS12 file."""
        url = f"https://{IP_ADDRESS}:{PORT}"

        with self.assertRaises(requests.exceptions.SSLError) as cm:
            requests_pkcs12.get(url, verify=ROOT_CA_PEM, timeout=10)

        exc = cm.exception
        self.assertIn("alert certificate required", str(exc))

    def test_pkcs12_adapter_hostname(self):
        """Tests connection using Pkcs12Adapter with PKCS12 file and password."""
        url = f"https://{HOST}:{PORT}"
        client = requests.Session()
        client.mount(
            url,
            requests_pkcs12.Pkcs12Adapter(
                pkcs12_filename=CLIENT_P12_WITH_PWD, pkcs12_password=P12_PASSWORD
            ),
        )
        response = client.get(url, verify=ROOT_CA_PEM, timeout=10)
        self.assertEqual(response.status_code, 200)

    def test_pkcs12_adapter_ip(self):
        """Tests connection using Pkcs12Adapter with PKCS12 file and password."""
        url = f"https://{IP_ADDRESS}:{PORT}"
        client = requests.Session()
        client.mount(
            url,
            requests_pkcs12.Pkcs12Adapter(
                pkcs12_filename=CLIENT_P12_WITH_PWD, pkcs12_password=P12_PASSWORD
            ),
        )
        response = client.get(url, verify=ROOT_CA_PEM, timeout=10)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
