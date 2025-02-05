# Encryption_Performance_project
# Encryption Algorithm Performance in Cloud

## Overview
This project evaluates the performance of various encryption algorithms, including AES, DES, a combination of AES & DES, and hybrid implementations, in a cloud environment. The research aims to balance security and efficiency by analyzing key performance indicators such as upload time, encryption time, CPU utilization, and memory usage.

## Features
- **Encryption Performance Analysis**: Evaluates AES, DES, AES+DES, and hybrid encryption methods.
- **Load Monitoring in Cloud**: Measures encryption impact on system performance.
- **Comparative Study**: Provides insights into the trade-offs between security and efficiency.
- **Real-Time Data Visualization**: Uses Streamlit for interactive data presentation.
- **Cloud Deployment**: Hosted on Azure for testing in a real-world environment.

## Tools & Technologies Used
- **Programming Language**: Python
- **Web Framework**: Streamlit (for visualization)
- **Cloud Platform**: Microsoft Azure
- **Encryption Libraries**:
  - Python Cryptography Library (AES, DES)
  - Crypto++ (C++)
  - PyCryptodome (Python)
- **Key Management**: Microsoft Azure Key Vault

## Installation & Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/encryption-performance-cloud.git
   cd encryption-performance-cloud
   ```
2. **Create a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

## Usage
- Upload files with or without encryption.
- Compare encryption performance based on upload time, encryption time, CPU usage, and memory consumption.
- Visualize data through an interactive dashboard.

## Results & Findings
- **Fastest Encryption**: AES 128-bit encryption has the lowest processing time (~0.9954 ms).
- **Lowest Resource Consumption**: No encryption results in 0% CPU usage but lacks security.
- **Balanced Approach**: Hybrid methods (AES+RSA) offer a trade-off between security and efficiency.

## Future Improvements
- Implement adaptive encryption strategies.
- Optimize encryption overhead for better performance.
- Extend analysis with real-world cloud deployments.

## Contributors
- Your Name ([GitHub Profile](https://github.com/your-username))

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or collaborations, feel free to reach out via GitHub issues or email.

---
**GitHub Repository:** [Encryption Performance in Cloud](https://github.com/your-username/encryption-performance-cloud)
