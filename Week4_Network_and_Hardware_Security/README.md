# **Week 4**

### Grading

Task #|Points|Description|
-----|:---:|----------|
[Task 1](#task-1-side-channels) | 1 | Side-channels
[Task 2](#task-2-slow-loris) | 1 | Slow Loris
[Task 3](#task-3-burpsuite-introduction) | 2 | BurpSuite & thc-hydra

---

# Tasks

### Task 1: Side-channels

**Excluding** speculative CPU attacks such as Meltdown or Spectre, choose an example of a side-channel attack and explain the following information about it:

- Brief explanation of what side-channel the attack uses and how

- What systems does it affect?

- What information is leaked via the side channel?

- Is there a documented case of it being used in a real life attack?

- Has it been fixed? If yes, how it was fixed?

You are not expected to produce an essay. Direct answers to questions above are sufficient. List sources and keep the answer concise at max 300 words not including sources.

---

### Task 2: Slow Loris

**HOX! Consider Slow Loris as a type of attack rather than the 'slowloris' program itself**

Seek information about the Slowloris Denial-of-Service attack and answer to the following questions:

- How does it work?

- Why is it unique while compared to the other high bandwith DDoS attacks?

- What are the effects of the attack?

- How can you mitigate/prevent the effects of the attack?

- Are there any notable instances of this style of attack being performed?

You are not expected to produce an essay. Direct answers to questions above are sufficient. List sources and keep the answer concise at max 300 words not including sources

---

### **Task 3**: BurpSuite Introduction

In this exercise we will take a brief look at a popular web security testing tool called BurpSuite and a password cracking tool called thc-hydra. The exercise requires quite a lot of setup and running an intentionally vulnerable web application (although locally).

**Needed tools:**  
BurpSuite Community Edition  
Docker Engine/Desktop  
Damn Vulnerable Web Application (DVWA)  
thc-hydra


**Returnable file**  
File that you should return will be a github repository link that contain clear screenshots of requested tasks and few explanations. This file/link should be returned to the Moodle return box.  

### Installing Burpsuite

To install the free community edition of BurpSuite go to https://portswigger.net/burp/communitydownload  

You will have to provide an email to be able to download the application. The Community Edition has some drawbacks, but they will not hinder us in this exercise.

**Windows and Mac**

Download the installer and follow the installation process

**Linux/Ubuntu**

In terminal, navigate to the folder where you downloaded the file. The file name may vary, **burpsuite_community_linux_v2023_2_3.sh** is just an example. Run the following commands to create an executable and run the installer. First command will create an executable and the second command will run it.

>chmod +x burpsuite_community_linux_v2023_2_3.sh  
>./burpsuite_community_linux_v2023_2_3.sh

After this you should be able to find BurpSuite in your installed programs.  

### Installing Docker Engine

If you have docker already installed you can skip this part

**Linux/Ubuntu**

For Linux (Ubuntu), follow the guide on the official page https://docs.docker.com/engine/install/ubuntu/

For first time setup, follow the steps from "Install using the apt repository" to the step where you verify the successful installation of Docker by running the "hello-world" image.  

**Windows/MacOS**

https://docs.docker.com/desktop/install/windows-install/

https://docs.docker.com/desktop/install/mac-install/

Download and follow the installer

### Setting things up  

#### BurpSuite

Start BurpSuite on your machine. Open a Temporary project and use BurpSuite defaults. You should land on the Dashboard of BurpSuite.  

We will be using the BurpSuite browser for this task. You can open the browser by navigating to the "Target" tab and clicking "Open browser"

![burp-win1](https://github.com/ouspg/SecurityEngineering/assets/44393530/787ed246-c99a-4c46-bf9a-e80f252d0c1d)


#### Running DVWA

**Damn Vulnerable Web Application (DVWA)** is an intentionally vulnerable website for testing different web vulnerabilities. It is listed in the OWASP Vulnerable Web Applications Directory (https://owasp.org/www-project-vulnerable-web-applications-directory/) and has a GitHub Repository at (https://github.com/digininja/DVWA). It also has a Docker image at (https://hub.docker.com/r/vulnerables/web-dvwa/)  

If you are doing this in a virtual machine, check that your Virtual Machine's networking mode is set to NAT. In VirtualBox it can be checked from network settings in the bottom right corner. If you have never changed these settings, there is most likely no problem here.   

We installed Docker Engine to streamline the setup of this web application. You can pull the DVWA docker image by running the following command

>docker pull vulnerables/web-dvwa

We can then simply run the image by running the following command in terminal  

>docker run --rm -it -p 80:80 vulnerables/web-dvwa  

**LINUX/UBUNTU** If you get an error about not being able to connect, make sure that the docker daemon is running by opening a second terminal and running the command

>sudo dockerd

If everything was successful, you should be able to access DVWA via http://localhost/  

![dvwa login](https://user-images.githubusercontent.com/44393530/225860828-023e7f7d-85cf-4bff-97f9-bf2e90fa1c88.PNG)

Enter the site with credentials  
Username: **admin**  
Password: **password**  

Scroll to the bottom of the page and initialize the database  

![dvwa 1](https://user-images.githubusercontent.com/44393530/225860916-2161939d-add1-4f10-8063-84e04691c6d1.PNG)

After this you will be returned to the login page and we can start learning few features of BurpSuite.  

## **Subtask 1**: Intercepting (0.25p)

BurpSuite browser is automatically setup as a proxy for BurpSuite and we are able to intercept the traffic going trough it.

Open the Proxy tab in BurpSuite and go to HTTP history. If you followed the instructions, there should be already some GET and POST requests visible. You can create more by attempting to login with wrong credentials. Here is a captured example with username=admin and password=hello  

![burp6](https://user-images.githubusercontent.com/44393530/225861070-8ed0edbd-5d87-4611-8ed6-2c6069e27666.PNG)

Now go to the **Intercept** tab and turn interception on  

![interception1](https://user-images.githubusercontent.com/44393530/225861142-66179b6f-3728-49e1-aee9-5eadd96aeeb5.PNG)

Now enter the site with credentials  
Username: **admin**  
Password: **password**  

The site should be frozen since we have intercepted the POST request. We can now modify the request as we like in BurpSuite. Go ahead and modify the User-Agent highlighted in the picture below. Type into the user agent **your name + name of a random household item**. After you have done the modification, release the POST request by pressing **Forward**. Also forward the GET request but there is no need to modify it.  

![interception2](https://user-images.githubusercontent.com/44393530/225861303-69ecc52f-ca2c-40a0-97f9-bb50fb9e827b.PNG)

Turn off interception and find the edited request from HTTP history. It should show the 'Original Request' at first. Click the 'Original Request' button to reveal a dropdown menu and choose 'Edited Request'. Now your changes should be visible in the inspector. 

![burp-edited-req](https://github.com/ouspg/SecurityEngineering/assets/44393530/4a216e07-25ce-48c8-8870-6b00c1ca9316)

To your github return repository, add a screenshot/screenshots of your edited post so that all the following information is visible.  

-**Listing of the last POST and GET request including timestamps and port**  
-**Entire Edited POST request in Raw format**  

## **Subtask 2**: Repeater (0.25p)

in the DVWA, go to the **DVWA Security** Tab and raise the security level from *Low* to *Medium* and click **Submit**  

Now go the **Weak session IDs** Tab and press **Generate**. This creates a cookie called *dvwaSession*.  

Generating the new session ID should show up in your HTTP history as a POST request. Right click the request and select **Send to Repeater**. Move to the highlighted Repeater tab  

![repeater1](https://user-images.githubusercontent.com/44393530/225861807-5921d774-e322-4b6d-9753-be438c685fef.PNG)

With the Repeater we can send previously sent request as many times as we want and even modify them. You can repeat the request by pressing **Send**. Below the request you can see the response.  

Try to figure out how the **dvwaSession** cookie is generated by looking at the response after multiple repeats. Return a brief explanation on how a new cookie is generated and a screenshots where both Request and a corresponding Response is visible in Raw or Pretty format.  

## **Subtask 3**: Intruder (0.25p)

In DVWA, Set the security back to *Low* and **Submit**. Then go to the **Brute Force** tab  

Try to login with credentials  
Username: **user**  
Password: **pass**  

Now go to HTTP history, right click on the GET request and click **Send to Intruder**. Move to the highlighted Intruder tab.  

![intruder1](https://user-images.githubusercontent.com/44393530/225862133-b3a25abc-df72-4a25-a993-680c9aafb050.PNG)

Intruder has automatically detected few payload positions. Remove these by pressing **Clear §**. Since we are only interested in brute forcing user credentials, we want to add a payload to the username and password variables. Highlight *user* and *pass* and insert those payload positions with **Add §**. The end result should look like this.  

![intruder3](https://user-images.githubusercontent.com/44393530/225862358-e57dc688-c2c0-4352-afc1-d7b2d33db50b.PNG)

Since we are simultaneously using multiple payload positions, choose the attack type **Cluster Bomb** from the drop down menu.  

Move to the **Payloads** tab. Here we can insert our credentials we want to test. Payload sets 1 and 2 represent 'username' and 'password' positions respectively.  

We could import a huge list of credentials if we wanted to. However the Community Edition has throttled performance and would take a long time iterating through long lists. Instead we will manually add few items.  

To Payload set 1 add the following items:  
**admin**  
**gordonb**  
**Your first name**  
**Your surname**  

To Payload set 2 add the following items:  
**password**  
**abc123**  
**letmein**  
**password123**  
**Your first name**  
**Your surname**  

End results should look something like this:  

![intruder4](https://user-images.githubusercontent.com/44393530/225862527-f8edb39b-eeb7-4ae5-904a-64d5c7a8f60f.PNG)
![intruder5](https://user-images.githubusercontent.com/44393530/225862547-551daa46-617e-44e8-b7b0-7354e4242981.PNG)

From the top right corner click **Start Attack**  

Inspect the results. Which bruteforce attemps were successful? Explain how did you come to this conclusion and what kind of evidence did you find from the responses?
Return the explanation along with a screenshot where all 24 attempts are listed. If you find evidence of a successful attempt from the responses, include it in the screenshot.  

## **Subtask 4**: Decoder (0.25p)

As a last task, we will take a quick look a the **Decoder** tab.  

While dealing with many kinds of requests we constantly come across decoded data  

Open the **Decoder** and write your name and student number into the first section.  

![decoder1](https://user-images.githubusercontent.com/44393530/225862736-1c7fefc6-697e-45f2-b94f-f5e23e2bac35.PNG)

Then **Encode** it as **URL**

![decoder2](https://user-images.githubusercontent.com/44393530/225862810-89ff0cec-aead-4ce8-a0f7-5b7bdb5a763e.PNG)

Then **Encode** it as **HTML**

![decoder3](https://user-images.githubusercontent.com/44393530/225862886-4f932491-9e5e-4244-a10a-83287c03ede3.PNG)

Finally use the **Smart Decode** function. Return a screenshot of all the encoded and decoded results.

## Preparation for Hydra task

Go to the CSRF tab on the DVWA. In this tab you can change the admin password. 

Go ahead and change your password to *cc* (two lowercase c letters). 

This rather shot password is used so you can quickly figure out whether the hydra command is working or not. We will change this later.

## **Subtask 5**: thc-hydra (1p)

https://github.com/vanhauser-thc/thc-hydra

thc-hydra is an open-source tool for finding credentials via wordlists or brute-forcing

Get the docker version of hydra with the command

>docker pull vanhauser/hydra

If you have hydra installed (pre-installed in Kali, for example) you can skip this.

With hydra, we will target the Brute Force section of DVWA.

We will craft a command that will brute force the password 'cc' that we just entered.

>docker run --network="host" vanhauser/hydra -V -f -I -l admin -x 1:2:a "YOUR-ANSWER-HERE://localhost/vulnerabilities/brute/:YOUR-ANSWER-HERE=^USER^&YOUR-ANSWER-HERE=^PASS^&Login=Login:H=Cookie\:PHPSESSID=YOUR-ANSWER-HERE; security=low:F=YOUR-ANSWER-HERE"

You will replace the YOUR-ANSWER-HERE sections with information you gather by inspecting the Brute Force tab with BurpSuite

Command breakdown:

>docker run --network="host" vanhauser/hydra

Runs the hydra docker image using host machines network. Without the *--network* parameter hydra will not be able to access the DVWA.

If you have hydra installed, you can replace the entire previous part of the command with just

>hydra

Flags/Parameters

>-V -f -I

-V: Hydra is verbose and shows each login attempt

-f: Exits the program after a successful login attempt is made

-I: (uppercase i) Brute force attempts can last for days. Hydra has the ability to restore and continue an interrupted session. This ignores previous attempts and starts always from the beginning.

>-l admin

(lowercase L) Tells hydra what to use as a login username during the brute force. Usually this would be pointing to a large wordlist full of usernames to test. This time we will only target the username 'admin'

>-x 1:2:a

Tells hydra to brute force the password. This is a special case, as hydra normally uses wordlists. '1:2:a' is a syntax for 'MIN:MAX:CHARSET'. This means hydra will start by bruteforcing with password length 1 and end after it has tested all combinations with the lenght of 2. CHARSET tells what kind of characters to test. Lowercase 'a' means only lowercase characters will be used to create the combinations.

>"YOUR-ANSWER-HERE://localhost/vulnerabilities/brute/:

Describes the HTTP method and target site. Here you will replace YOUR-ANSWER-HERE with either *http-post-form* or *http-get-form*. Use BurpSuite to figure out the correct method.

>YOUR-ANSWER-HERE=^USER^&YOUR-ANSWER-HERE=^PASS^&Login=Login:

This is important as ^USER^ and ^PASS^ are microsyntax for hydra to know which query parameters of the request contain information for username and password. Hydra will apply previously mentioned -l and -x commands to these parts respectively. Use BurpSuite to figure out the needed query parameters and fill them into your command.

>H=Cookie\:PHPSESSID=YOUR-ANSWER-HERE; security=low:

Information as required by the HTTP request. The important part here is the PHP session ID which is unique each time you run the DVWA. Find this using BurpSuite and fill it in. Also make sure DVWA security level is set to 'Low'.

>F=YOUR-ANSWER-HERE"

Sets the Failure state for Hydra. Hydra does not know when the login attempt is either successful or has failed. YOUR-ANSWER-HERE will be a string of characters that appear on the website after a failed login attempt. Hydra will look for this string of characters after each attempt and continue if it can find it.

When you have replaced all the YOUR-ANSWER-HERE sections, run the command. It should find your credentials *login "admin" - pass "cc"* and in the end it should look like this:

![hydra](https://github.com/ouspg/SecurityEngineering/assets/44393530/6d733cd5-e934-4e82-9753-5749c9316817)

After you have verified that your command works, go back to the CSRF tab and change your admin password. Create the new password with following parameters:
- length of exactly 4 letters
- only lowercase letters
- starts with the letter 'b'
- rest of the letters are from the following set of characters: *abcdefghijklmnopqrstuvwxyz*

Then modify the following part from the hydra command:

>-x 1:2:a

Modify it so the minimum and maximum range is correct so that hydra can find your four letter password.

*BEFORE YOU RUN THE COMMAND* Mark down the time you start the brute forcing progress. As a part of your assignment you will mark down how many minutes did the process take. When hydra finds the credentials, it will display the time it finished (in Greenwich Mean Time UTC+0)

Return the following:
- Screenshot of the finished hydra command where atleast finishing time and last attempt are visible. Make sure the four letter password you used is visible.
- How many minutes did the brute forcing process take
- The full hydra command

## **Clean up**

After getting your results you can close BurpSuite. Remember, that the BurpSuite project is temporary and you cannot access the results after closing.  

To close the docker image of DVMA, open the terminal window where docker is active and press **Ctrl+C**. This should close the image. You can also close the docker daemon with the same key combination. You can verify this with the command  

>docker info  

![docker stop](https://user-images.githubusercontent.com/44393530/225863084-e0e0ec21-9b46-480f-9603-a3bd5b72a4fa.PNG)

Return your GitHub repository link containing all the screenshots and explanations to the Moodle return box  
