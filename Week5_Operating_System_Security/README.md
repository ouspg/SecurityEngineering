# Week 5

### Grading

Task #|Points|Description|
-----|:---:|----------|
[Task 1](#task1-bring-your-own-devices) | 1 | Bring Your Own Device
[Task 2](#task2-attacks-on-cpu-execution) | 1 | Attacks on CPU Execution
[Task 3](#task3-securing-os) | 1 | Securing OS
[Task 4](#task4-logging) | 1 | Logging 

---

# Tasks

### Task1: Bring your own devices

Following link containing NIST:s [security recommendations for workplace bring your own device](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1800-22.pdf). On the page 12 is listed following 9 threat events, and your job is to make one A4 sized poster or otherwise shortly summarize what each listed threat event means based on the document or your own research.

- Intrusive application practices
Answer:- Mobile OS APIs allow apps to share data with other apps, either by exposing specific services to other apps or by storing it to locations accessible to other apps. Sensitive information stored in commonly-accessible files/locations or openly accessible through intents may be read or potentially modified by apps untrusted by the developer, which may lead to a loss of confidentiality, integrity, or availability of that data.

- Account credential theft through phishing
Answer:- Phishing emails have been prevalent for a very long time. These emails typically link to websites geared at specific individuals, departments, or companies, and may be designed to look like their genuine counterpart with the intention of capturing credentials.

- outdated phones
Answer:- Organizations or individual users may develop and rely upon specific apps or devices to complete necessary work. Knowledge of a serious vulnerability affecting such an app or device increases the risk associated with using it to accomplish that work. However, the impact of being unable to complete the work as a result of abstaining from use of the app or device, may be unacceptable. Malicious applications that achieve privilege escalation in the context of the mobile OS, driver, peripheral firmware, or the kernel, may further achieve unauthorized access or modification of app, user, or system data, process memory, or execute other unauthorized actions on the device. 

- Sensitive data transmissions
Answer:- Phone calls can be intercepted by adversaries, who can listen to the calls. Transmission of app or device data unencrypted allows any attacker with access to the physical media channel to intercept that data. Even if the data is not directly sensitive, it may in combination with other data, allow an attacker in infer sensitive information or conduct other attacks against the user or device. Unencrypted or weakly encrypted Wi-Fi networks could allow adversaries to eavesdrop on connections.

- Brute-force attacks to unlock a phone
Answer:- Short or easy to guess PINs can be brute forced to unlock the device. Typical device usage scenarios result in fingerprints and smudges being left on the screen of a mobile device. Repeated taps to the same location on the screen may be discernable due to the clustering and build-up of similar prints, potentially allowing an attacker to infer some or all of the numbers or characters that appear in a device unlock PIN or password. This greatly facilitates an educated brute-force attack against the device unlock PIN or passcode, particularly when combined with similar attacks, such as recording events of device unlock by the a user.

- Application credential storage vulnerability
Answer:- Attackers able to steal authorized credentials could potentially login to sensitive services or devices, and gain unauthorized access to privileged information. If an app exchanges data with a compromised back-end server, it may be vulnerable to exploitation from what may be treated as a trusted system. This may provide an attacker with unauthorized access to sensitive user data or remote control over app behavior or content.

- Unmanaged device protection
Answer:- Root and jailbreak detection for mobile devices is based on detecting the changes that a process by which a mobile device was compromised would have caused. For instance, creation of files or directories that do not exist on uncompromised devices. Given the diversity of mobile devices, mobile OSs, the varying methods of compromise, and the potential for an attacker to intercept and forge acceptable responses to checks for such changes, root detection continues to be an area of challenge.

- Lost or stolen data protection
Answer:- Lost or stolen mobile devices gives an adversary unhindered access to the device, and if there’s an insecure or no PIN in place, access to the data on the device as well.

- Protecting enterprise data from being
Answer:- Enterprise data may be synchronized to unmanaged and potentially insecure 3rd party cloud services.

inadvertently backed up to a cloud service

---

### Task2: attacks on CPU execution
spectre and meltdown are two original side channel attacks discovered in 2017 that target cpu, and over the years more have been discovered. [This wikipedia article](https://en.wikipedia.org/wiki/Transient_execution_CPU_vulnerability) list some of them. Pick 3 of them to research about how exactly each exploits the system,their differences, which systems they targeted and how they can be mitigated. 

Answer in max 300 words. You are free to use tables or otherwise make to comparison easier to read if you wish.

---

### Task3: Securing OS
Following is a list of some of the more common vulnerabilities and attack vectors existing in operating systems.  

- Malware and Viruses
- Exploiting Software Vulnerabilities
- Phishing and Social Engineering
- Drive-by Downloads
- Zero-Day Exploits
- USB/Removable Media Attacks
- Password Cracking

Make short write up about each that answers following questions 
1. What harm can it cause to you?
2. How OS of your choosing (Windows, Mac, Linux) can mitigate it?
     - Function of the OS itself or external tools?


---

### Task4: Logging
Log files are records of events or actions that occur in a system, application, or program. Logs are essential for troubleshooting, debugging, and analyzing the behavior of software or hardware.

Find answers to following questions:
1. What kind of information would be saved into following types of log files
- Application logs
- Event logs
- Service logs
- System logs

2. Where in each of the common Operating Systems those logs would be stored (Windows, Mac, Linux(changes per distro so provide in answer which you are using)
3. What kind of threats could you notice by monitoring each log file?
4. How would you go about monitoring logs on your personal computer?


remember to list sources for information you use!
