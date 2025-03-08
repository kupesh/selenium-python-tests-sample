# Selenium Testing Project

## **Project Overview**
This project demonstrates how to use **Selenium with Python** for automated web testing. The test script performs a Google search and verifies the results.

## **Setup Instructions**

### **1. Clone the Repository**
```sh
git clone https://github.com/kupesh/selenium-project.git
cd selenium-project
```

### **2. Create a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Install Chrome and ChromeDriver**
```sh
brew install --cask google-chrome
brew install chromedriver
```

### **5. Verify Installation**
Run the following commands to ensure everything is installed correctly:
```sh
python -c "import selenium; print(selenium.__version__)"
chromedriver --version
google-chrome --version
```

---

## **Running the Tests**
### **1. Run a Single Test Script**
```sh
python test_google_search.py
```

### **2. Run Tests Using Pytest**
```sh
pytest test_google.py
```

### **3. Generate an HTML Test Report** (Optional)
```sh
pytest --html=report.html
```

---

## **Debugging Issues**

### **1. ChromeDriver Version Mismatch**
If you see an error like:
> `SessionNotCreatedException: Message: session not created due to version mismatch`

Run:
```sh
chromedriver --version
google-chrome --version
```
Ensure that **ChromeDriver** matches your **Chrome** version.
If not, update it:
```sh
brew uninstall chromedriver
brew install chromedriver
```

### **2. Selenium Module Not Found**
If `selenium` is not recognized, reinstall it inside the virtual environment:
```sh
source venv/bin/activate
pip install selenium
```

### **3. Run Debug Script**
To check for common issues, run the provided debug script:
```sh
python debug_check.py
```

---

## **Debug Script: debug_check.py**
Create a file named `debug_check.py` and add the following:

```python
import sys
import os
from selenium import webdriver

print("Python Executable:", sys.executable)
print("Python Version:", sys.version)
print("Selenium Installed Version:")
try:
    import selenium
    print(selenium.__version__)
except ImportError:
    print("Selenium not installed!")
    sys.exit(1)

print("Checking ChromeDriver...")
os.system("chromedriver --version")

print("Checking Google Chrome Version...")
os.system("google-chrome --version")

# Test if Selenium can launch Chrome
try:
    driver = webdriver.Chrome()
    print("Selenium successfully launched Chrome!")
    driver.quit()
except Exception as e:
    print("Error launching Chrome:", e)
```

Run the debug script:
```sh
python debug_check.py
```
This will check for common setup issues and provide guidance.

---

## **Contributing**
Feel free to fork the repository and submit pull requests to improve the project.

## **License**
This project is licensed under the MIT License. See `LICENSE` for details.

