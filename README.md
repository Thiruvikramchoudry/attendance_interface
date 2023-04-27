# Attendance Monitoring System for MGNREGS

The Mahatma Gandhi National Rural Employment Guarantee Scheme (MGNREGS) is a government program in India that guarantees a minimum of 100 days of wage employment per year to rural households. To efficiently track and record the attendance of MGNREGS workers, a monitoring system needs to be put in place. 

## Table of Contents

- [Introduction](#introduction)
- [Scope and Requirements](#scope-and-requirements)
- [Technology and Tools](#technology-and-tools)
- [Design](#design)
- [Development](#development)
- [Deployment and Maintenance](#deployment-and-maintenance)
- [Conclusion](#conclusion)

## Introduction

This project aims to create a monitoring system for attendance in MGNREGS that will efficiently track and record the attendance of workers. The system will capture attendance in real-time, generate reports, and store attendance data securely. 

## Scope and Requirements

The monitoring system's scope includes the number of workers, the frequency of attendance, and the level of detail required. The system's requirements include the ability to capture attendance in real-time, generate reports, and store attendance data securely. 

## Technology and Tools

The monitoring system could be web-based or mobile-based, depending on the availability of internet connectivity and the devices used by workers. A database management system could be used to store attendance data securely, and a reporting tool could be used to generate reports.

## Design

The monitoring system will be designed to meet the requirements defined in the previous section. The design will include the user interface, the database schema, and the reporting framework. The user interface will be intuitive and easy to use, and the database schema will be optimized for performance and scalability. The reporting framework will be flexible enough to generate reports that meet the specific needs of the stakeholders.

## Development

The development will follow best practices and standards to ensure the quality and maintainability of the code. The system will be thoroughly tested to ensure that it meets the requirements and works as expected.

## Deployment and Maintenance

The monitoring system will be deployed to the production environment and tested again to ensure that it works correctly. The system will be maintained and updated regularly to address any issues that arise and to add new features as needed.
## Installation
To use this monitoring system, follow these steps:
1. Make sure that you have `Python 3`, `virtualenv` and `pip` installed.     
2. Clone the repository using the following command:
```bash
        $ git clone https://github.com/Thiruvikramchoudry/attendance_interface.git
 ```
 3. Create a python3 virtualenv, activate the environment and Install the project dependencies.  
    - For linux/macintosh:
    ```bash
        $ python3 -m venv venv
        $ source venv/bin/activate
        $ pip3 install -r requirements.txt
    ```   
    - For windows:
    ```bash
        python -m venv venv
        venv/Scripts/activate.bat
        pip install -r requirements.txt
    ```
### Steps to run
From now when you start your work, run ``source bin/activate`` inside the project repository and you can work with the django application as usual - 

```python
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py runserver
```

### Contributors
* [Thiruvikram Choudry](https://github.com/Thiruvikramchoudry)
* [Praveen](https://github.com/Praveen-18)  
* [Srinath](https://github.com/srinath0307)
* [Sridhar](https://github.com/srid20ad047)
* [Jaswanth](https://github.com/JASWANTHJET)
* [Sharavanan](https://github.com/Sharavanan69)
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.
## Conclusion

Creating a monitoring system for attendance tracking in MGNREGS requires careful planning and execution. By following the steps outlined in this project, we can create a system that efficiently tracks and records attendance and generates reports that provide valuable insights to stakeholders.
