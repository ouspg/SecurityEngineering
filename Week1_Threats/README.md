# Week 1

### Grading 

Task #|Points|Description|
-----|:---:|----------|
[Task 1](#task-1-what-measures-have-you-taken-to-protect-yourself-from-cyber-crimes) | 1 | Measures Against Cyber Crimes
[Task 2](#task-2-personal-threat-model) | 1 | Personal Threat Model
[Task 3](#task-3-company-security-policy) | 1 | Company Security Policy
[Task 4](#task-4-security-audit) | 1 | Personal Security Audit
[Task 5](#task-5-virtual-machine-with-docker) | 1 | Virtual Machine & Docker

---

> Please note the last task, 'virtual machine & docker' will have most focus on the exercise session to get it working for everyone doing it.

# Tasks

### Task 1: What measures have you taken to protect yourself from cyber crimes?

Write a short description of the actions you have done to fortify you defenses towards all sorts of cyber crimes, including possible servers and accounts you have. Please keep in mind not to include any specific details, such as passwords or tokens.

Have you been a victim of cyber crimes and do you think you could have prevented them? For example phishing and malware attacks. What could you improve on?

Please keep your answer concise, but at **minimum** 150 words.

---

### Task 2: Personal Threat Model

Possible tool to add to next run [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) 

A 'for more reading' [link](https://www.privacyguides.org/en/basics/threat-modeling/) 

A threat model is a tool used widely in security, it can be used for example to identify sensitive or vulnerable data or systems. Its goal is to identify potential vulnerabilities and a likely impact of a security breach, helping companies take proper measures to mitigate and / or prevent these. A threat model can also help companies assess and prioritize its security efforts by identifying which assets are the most critical and which threats are the most probable. Overall, a threat model is a vital part of a comprehensive cyber security strategy helping organizations manage risks and breaches, and how to allocate defense budget.

In this task we are focusing solely on the cyber side of threat models as you will be creating a personal threat model to identify and assess potential threats to your assets, for example sensitive information and online accounts.

The goal of creating a personal threat model is to help you understand potential ways to analyze your own cyber behavior and how to prioritize your efforts regarding your own personal security and privacy. It is also important for cyber security students to understand the types of threats they may face and what the potential impact can be. Threat modelling is also an important skill for security professionals and doing personal threat modelling can be translatable to real world businesses.

You can find more information on [OWASP Threat modelling](https://owasp.org/www-community/Threat_Modeling) and in [The Threat Modelling Manifesto](https://www.threatmodelingmanifesto.org/)

<details>
<summary>Here's few pointers for threat modelling:</summary>
<br>

- Identify your assets that could be targeted by cyber criminals

- Assess the threats and likelyhoods of them for each of your assets

- Identify vulnerabilities for example weak or repeated passwords

- Evaluate impact if an asset is compromised

- Mitigate or mitigation plan; determine what you can do now and what to do if compromised

</details>

We also recommend creating a visual representation of your threat model, diagrams and flowcharts are good for this. Discussing with your classmates can also help with any additional measures you can take to reduce your risks.

---

### Task 3: Company Security Policy
Pick two topics from the list below to write a security policy on.
An effort should be made to include one policy on one A4 page. 

<details>
<summary>Topics</summary>
<br>

- Password policy
- Physical access policy
- Cloud usage/security policy
- System authentication policy
- Network perimeter security policy
- Social media security policy
- BYOD(Bring Your Own Device) policy
- General purpose information security policy

</details>

These policies are to be kept quite straight-forward and easily understandable for any employee, this includes explaining certain not well-known topics, for example a VPN or a network perimeter. The second lecture "Threat Models and Security Policies" gives very good advice on how to write sensible policies.

You should also check [this](https://csrc.nist.rip/publications/nistpubs/800-12/800-12-html/chapter5.html) for detailed advice and explanation on for example types of policies. For example chapter 5.2.2 gives good insight on what basic components are good for issue-specific policies.
You don't have to contain yourself to just text, you may include for example pictures and data-flow charts where beneficial.

---

### Task 4: Personal Security Audit

~~In the previous tasks we tried to map out our precious data and security of our machines. Now we can perform a couple of tests to see if we find any anomalies or unsecured data. We also deploy a Security Information and Event Management software to monitor and analyze systems.~~ **TODO** *Rewrite and add vm part below, for the full point docker must work*

### Task 4A: Network scan 

Let's start with a network scan, by now most will have already heard about [NMAP](https://nmap.org/); a network mapper which is 
> "A free and open source utility for network exploration and security auditing" -[NMAP Book](https://nmap.org/book/preface.html) 

NMAP is available as both a CLI and [GUI (Zenmap)](https://nmap.org/zenmap/) application, most of the time you will use nmap from the command line. There are some benefits to Zenmap, such as the topology map, and we are going to showcase that here in this task. 

NMAP is available on all the commmon platforms and you can get it from their [website](https://nmap.org/download), however if you are using Linux, you can most likely get it from your package manager. Go ahead and proceed with the installation, for Linux you might have to install Zenmap package as it usually is not bundled with NMAP. If you are using Windows we recommend leaving everything as default.

>**Note**
>Before scanning your network, make sure to let everyone on the network know about it, and more importantly give them the ability to disconnect their devices. 

To scan your network you are going to need your ip address in CIDR notation, which will most likely look something like this: ```192.168.1.0/24```. Below you will find instruction for Linux, Windows and Mac.

<details>
<summary>Linux</summary>

The command ```ip a``` will show your ip address already in CIDR notation, you just have to find the address of the correct device, usually the second from the top as the first will be localhost. 

![ip a on Linux](https://github.com/ouspg/SecurityEngineering/blob/main/Week1_Threats/Images/Linux_ip_a.png)

Now make sure to swap the host part; part after the last '.' and before the '/' to a 0. Add the CIDR and this will be the address you will scan.

</details>

<details>
<summary>Windows</summary>

The command ipconfig will show you your ip address and the subnet mask, with these we will figure out the address you will scan.

![ipconfig on windows](https://github.com/ouspg/SecurityEngineering/blob/main/Week1_Threats/Images/Windows_ipconfig.PNG)

These are the numbers we care about.

The most common subnet mask in home networks is ```255.255.255.0``` this will result in '/24' at the end of the ip address. If your subnet mask is something else, please refer to this [cheat sheet](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/) to find out your CIDR notated address.

Now make sure to swap the host part of your ip address; part after the last '.' to a 0. Add the CIDR and this will the address you will scan. 

</details>

Now that we have the address we want to scan, open up Zenmap. The UI is mostly self-explanatory, put the ip address in CIDR notation to the target and choose intense scan for the profile, then just press scan. This should scan the devices in your network. While the scan is running, you can see the output the same way as in NMAP, wait for it to finish and comb through the output. Take note of open ports, scripts and operating systems the scan found.

Make your way over to the topology tab. Enable easy controls with the control button on the left. Here you should now see all the devices found, icon definitions can be seen after clicking the 'Legend' button on the right, and more info on the devices can be found by right clicking.

Save the scan with ```CTRL + S``` and take a screenshot of this topology screen with devices clearly visible, you can redact device information from the screenshot if you want to. 

>The topology map can show traceroutes when scanning outside your network, this is where the tool shines as a simple visual aid. 

**What to return:**
1. Did you find devices you did not know were in your network?
2. Were there open ports which should have been closed?
3. Did nmap find any vulnerabilities with the scripts?
4. Screenshot of the topology of your network. You can redact device information if you want.

### Task 4B: Account Security

This part of task 4 is to check yourself with haveibeenpwned. This should let you know if your account details have been leaked and what types of information was included.

[Haveibeenpwned](https://haveibeenpwned.com/) Is a website and very simple to use, you input your email address and it will search for leaks on platforms where you have accounts. The website shows you platforms it detected had been leaked and those leaks included your email address, however it is not a definitive list and there may be more leaks or dumps with your email included. Take a screenshot for the return. 

**What to return:**
1. Has your account details leaked?
2. Screenshot of haveibeenpwned search, you can redact information if you want.
3. Did you change passwords and/or email + password combos, that were leaked, if not, do it.

### Task 5: Virtual Machine with Docker

The last part of this weeks tasks is to set up the courses virtual machine and get it ready with docker working. This weeks exercise session will focus on this. 

**TODO** add a checklist here.

### Feedback
Be sure to give feedback on these tasks. Do you feel these to be the kind of skills you might need or want?
