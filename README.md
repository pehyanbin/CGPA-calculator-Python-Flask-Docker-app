# DOCKER PYTHON FLASK CGPA CALCULATOR<br>
This is a simple Swinburne CGPA calculator web application built using Python and Flask, containerized with Docker.<br><br>
### Prerequisites<br>
- Docker installed on your system<br><br>
- If you don't have Docker installed, you can download it from the official Docker website: https://www.docker.com/get-started<br><br>

### Instructions<br>
To run the application, follow these steps:<br>
1. **Clone the repository**:<br>
   ```bash
   git clone <repository_url>
   ```
2. **Build the Docker image**:<br>
   ```bash
   docker build -t cgpa-calculator .
   ```
3. **Run the Docker container**:<br>
   ```bash
   docker run -p 5000:5000 cgpa-calculator
   ```
4. **Access the application**:<br>
   Open your web browser and navigate to `http://localhost:5000`.
<br><br>
## Usage<br>
Enter the number of subjects and their respective grades in the provided form. The application will calculate the CGPA based on the entered grades.<br><br>
## Technologies Used<br>
- Python
- Flask
- Docker<br><br>

<b>Swinburne CGPA Calculator</b><br>
This CGPA calculator is specifically designed for Swinburne students to calculate their CGPA easily and accurately. It follows the Swinburne grading system and calculates the CGPA based on the entered grades.<br><br>
<b>Why Docker?</b><br>
Docker provides a lightweight and portable way to package the application along with its dependencies, ensuring consistent behavior across different environments.<br><br>
<i>What happen if I don't use docker?</i><br>
You can still run the application without Docker, but you will need to install the required dependencies manually.<br><br>
To run the application without Docker, follow these steps:<br>
1. **Install dependencies**:<br>
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the application**:<br>
   ```bash
   python appcode.py
   ```
3. **Access the application**:<br>
   Open your web browser and navigate to `http://localhost:5000`.
<br><br>

## In Conclusion<br>
With Docker, you don't need to install any dependencies manually. Docker takes care of everything, including the installation of Python and Flask.<br><br>
All you need to do is build the Docker image and run the container. Docker will handle the rest, including installing the required dependencies and running the application.<br><br>



