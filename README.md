---

# ACME Bank Login Automation Script

This repository contains a Robot Framework script designed to automate the login process for the applitools' 'ACME Bank' test website across multiple web browsers. The script utilizes the Browser library to perform actions in Chromium, WebKit, and Firefox.

## Features

- **Cross-Browser Testing**: The script launches the Acme login page in three different browsers: Chromium, WebKit, and Firefox.
- **Login Functionality**: It tests valid login scenarios by launching the login page for each browser.
- **Bad Login Scenarios**: The script also tests invalid login attempts with incorrect usernames and passwords to ensure proper error handling.

## Structure

### Settings

- **Library**: The script uses the `Browser` library to interact with web browsers.
- **Resource**: It imports a resource file named `Web-keys.robot`, which contains keywords and variables used in the test cases.

### Variables

- Currently, there are no specific variables defined in this section, but it can be expanded to include any necessary parameters or configurations.

### Test Cases

1. **Login To Acme**: 
   - Launches the Acme login page in three different browsers (Chromium, WebKit, and Firefox) to verify that the login functionality works across all platforms.

2. **Bad Logins**: 
   - Launches the Acme application in Chromium and attempts to log in with a bad username.
   - Launches the Acme application in WebKit and attempts to log in with an incorrect username and password combination.

## Requirements

- Robot Framework
- Browser library
- Web drivers for Chromium, WebKit, and Firefox (included with Browser Library)

## Usage

To run the tests, ensure you have the necessary dependencies installed and execute the following command in your terminal:

```bash
robot your_test_file.robot
```

Replace `your_test_file.robot` with the name of your Robot Framework script file, in this case 'login.robot'.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or additional features.

---
