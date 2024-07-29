# System Architecture

![image](https://github.com/user-attachments/assets/237748f6-78ea-447b-9003-9c51bda61162)

WebScan* presents a comprehensive overview of the project’s automated web attack surface analysis (ASA) system. The system is designed within a web application that allows users to input a target web URL and select the type of scans they wish to perform. The web interface is connected to a backend powered system by a Docker, which houses a variety of cybersecurity tools and scripts. The architecture is divided into two components, the web system and the docker server. The web system handles all user interactions like input validation, ethical user agreement, error handling, and displaying results. Once the user has provided the target URL and selected the scan type, it will run the specified scan script into the Docker Server. The docker server contains the core functionality of the automated ASA system. The scripts orchestrate the execution of various cybersecurity tools such as Nmap, Nikto, Uniscan, DNSmap, Wapiti, Wget, DavTest, Wafw00f, and Whatweb. Each tool performs specific security checks and vulnerability assessments on the target URL. Meanwhile, the system utilizes Kali Linux, a robust platform environment within the Docker container to run the scanning scripts on the selected tools. Once the scans are completed, the results are processed through a series of steps which includes vulnerability identification, prioritization, risk rating, remediation suggestions, all to generate the vulnerability report. Once the report is completed, it will be formatted into the web interface with an option for report installation. The architecture ensures a seamless flow from user input to comprehensive security analysis, making it an effective tool for automated web applications security assessment with customizable options enabled. 

# WebScan* UI

![image](https://github.com/user-attachments/assets/c0d90965-56c2-407d-b749-2095e47c8ec4)

## Problem Background
In the rapidly changing world of technological advancement, web domains have continued to serve as a critical gateway to most online interactions like communicating, shopping, entertainment, and learning where it involves multiple forms of information exchange. However, the rising dependance on web domains have also become the most attracted target that malicious actors would exploit vulnerabilities to launch attacks (Abokhodair, 2018). Leading to devastating consequences, like data breaches, reputational damage, and financial losses (Bilge, 2019). 
The alarming rise of cyberattacks has further proved a stronger need and requirement of security measures in place. According to a 2023 report by Cybersecurity Ventures, businesses are likely to anticipate a cyberattack in every 11 seconds in 2023, highlighting the urgency for automated solutions to protect the web domains from being an easy and high-vulnerability target (Cybersecurity Ventures, 2023).
This project aims to address the need for robust and proactive security measures to protect online assets like web domains while recognizing the limitations of time-consuming operations and high vulnerability oversighting for traditional manual web domain Attack Surface Analysis (ASA) (Bilge, 2019). This research aims to leverage the power of automation to assist in streamlining the process and enhancing effectiveness of identifying vulnerabilities. As such, the primary goal of this project is to implement an automated system for web domain ASA where the system will provide comprehensive analysis of domain attack surfaces, efficiently identify, and prioritize vulnerabilities based on their severity. This system will empower domain administrators to detect & mitigate vulnerabilities with actionable insights that can constantly strengthen the system security posture against evolving cyber threats.
This document outlines the research methodology used, including survey analysis with IT professionals, and defines the project’s objectives, scope, and deliverables. While the research aims to address the limitation of existing solutions, it contributes to enhance the overall cybersecurity resilience for web domain analysis. 


# Use Case Diagram

![image](https://github.com/user-attachments/assets/4608ee23-0775-409c-8692-6b359d3c9a51)
