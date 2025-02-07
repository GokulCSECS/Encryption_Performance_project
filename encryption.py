import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import psutil
from io import BytesIO
from azure.storage.blob import BlobServiceClient
from Crypto.Cipher import AES, DES3
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher.PKCS1_OAEP import new as OAEP_new

# Azure Storage Account details
azure_storage_account_name = "GOKUL"
azure_storage_account_key = "HRSIWK+CASY+EFYRYCVT+001061sa@aeVvlYoSCRYHdS9"
container_name = "webstoragedemo"

# Function to encrypt file
def encrypt_file(file, method):
    start_time = time.time()  # Start time for encryption
    data = file.read()
    
    if method == 'AES 256':
        cipher = AES.new(get_random_bytes(32), AES.MODE_EAX)
    elif method == 'AES 128':
        cipher = AES.new(get_random_bytes(16), AES.MODE_EAX)
    else:
        st.error("Unsupported encryption method")
        return None

    ciphertext, tag = cipher.encrypt_and_digest(data)
    elapsed_time = time.time() - start_time  # Measure encryption time
    
    return ciphertext, cipher.nonce, tag, elapsed_time

# Streamlit UI
st.title("File Encryption App")
uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "pdf"])

if uploaded_file is not None:
    encryption_method = st.selectbox("Select Encryption Method", ["AES 256", "AES 128"])
    
    if st.button("Encrypt"):
        ciphertext, nonce, tag, enc_time = encrypt_file(uploaded_file, encryption_method)
        st.success(f"File encrypted successfully in {enc_time:.4f} seconds")
