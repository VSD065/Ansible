from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import sys

def convert_key_to_numeric(key_path):
    try:
        with open(key_path, 'rb') as key_file:
            private_key = load_pem_private_key(key_file.read(), password=None)

            if isinstance(private_key, rsa.RSAPrivateKey):
                serialized_key = private_key.private_bytes(
                    encoding=serialization.Encoding.DER,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            else:
                raise ValueError("Unsupported key type. Only RSA keys are supported.")
            
            # Convert to numeric format
            numeric_key = ''.join(f'{byte:02x}' for byte in serialized_key)
            print(numeric_key)

    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 convert_pem_to_der.py <key_path>")
        sys.exit(1)

    key_path = sys.argv[1]
    convert_key_to_numeric(key_path)

