# **Week 4**

### Grading

Task #|Points|Description|
-----|:---:|----------|
Task 1 | 1 | Side-channels
Task 2 | 1 | Slow Loris
Task 3 | 2 | BurpSuite & thc-hydra

---

# Tasks

### Task 1: Side-channels

Choose an example of a side-channel attack and explain the following information about it:

- Brief explanation of what side-channel the attack uses and how

- What systems does it affect?

- What information is leaked via the side channel?

- Is there a documented case of it being used in a real life attack?

- Has it been fixed? If yes, how it was fixed?

List sources and keep the answer concise at max 300 words not including sources.

---

### Task 2: Slow Loris

**HOX! Consider Slow Loris as a type of attack rather than the 'slowloris' program itself**

Seek information about the Slowloris Denial-of-Service attack and answer to the following questions:

- How does it work?

- Why is it unique while compared to the other high bandwith DDoS attacks?

- What are the effects of the attack?

- How can you mitigate/prevent the effects of the attack?

- Are there any notable instances of this style of attack being performed?

List sources and keep the answer concise at max 300 words not including sources

---

### **Task 3**: BurpSuite Introduction

In this exercise we will take a brief look at a popular web security testing tool called BurpSuite. The exercise requires quite a lot of setup and running an intentionally vulnerable web application (although locally), so using a Virtual Linux Machine is heavily recommended. All the following instructions will be for **Linux only**  

**Needed tools:**  
Virtual Machine (Linux)  
BurpSuite Community Edition  
Docker Engine  
Damn Vulnerable Web Application DVWA  
thc-hydra


**Returnable file**  
File that you should return will be a PDF or a github repository link that contain clear screenshots of requested tasks and few explanations. This file/link should be returned to the Moodle return box.  

### Installing Burpsuite

To install the free community edition of BurpSuite go to https://portswigger.net/burp/communitydownload  

You will have to provide an email to be able to download the application. The Community Edition has some drawbacks, but they will not hinder us in this exercise.

In terminal, navigate to the folder where you downloaded the file. The file name may vary, **burpsuite_community_linux_v2023_2_3.sh** is just a current example. Run the following commands to create an executable and run the installer. First command will create an executable and the second command will run it.

>chmod +x burpsuite_community_linux_v2023_2_3.sh  
>./burpsuite_community_linux_v2023_2_3.sh

After this you should be able to find BurpSuite in your installed programs.  

### Installing Docker Engine

For Linux (Ubuntu), follow the guide on the official page https://docs.docker.com/engine/install/ubuntu/

For first time setup, follow the steps from "Install using the apt repository" to the step where you verify the successful installation of Docker by running the "hello-world" image.  

### Setting things up  

#### BurpSuite

Start BurpSuite on your virtual machine. Open a Temporary project and use BurpSuite defaults. You should land on the Dashboard of BurpSuite.  

We will be using the BurpSuite browser for this task. You can open the browser by navigating to the "Target" tab and clicking "Open browser"

#### Running DVWA

**Damn Vulnerable Web Application (DVWA)** is an intentionally vulnerable website for testing different web vulnerabilities. It is listed in the OWASP Vulnerable Web Applications Directory (https://owasp.org/www-project-vulnerable-web-applications-directory/) and has a GitHub Repository at (https://github.com/digininja/DVWA). It also has a Docker image at (https://hub.docker.com/r/vulnerables/web-dvwa/)  

Before proceeding check that your Virtual Machine's networking mode is set to NAT. In VirtualBox it can be checked from network settings in the bottom right corner.   

We installed Docker Engine to streamline the setup of this web application. You can pull the DVWA docker image by running the following command

>docker pull vulnerables/web-dvwa

We can then simply run the image by running the following command in terminal  

>docker run --rm -it -p 80:80 vulnerables/web-dvwa  

If you get an error about not being able to connect, make sure that the docker daemon is running by opening a second terminal and running the command

>sudo dockerd

If everything was successful, you should be able to access DVWA via http://localhost/  

![dvwa login](https://user-images.githubusercontent.com/44393530/225860828-023e7f7d-85cf-4bff-97f9-bf2e90fa1c88.PNG)

Enter the site with credentials  
Username: **admin**  
Password: **password**  

Scroll to the bottom of the page and initialize the database  

![dvwa 1](https://user-images.githubusercontent.com/44393530/225860916-2161939d-add1-4f10-8063-84e04691c6d1.PNG)

After this you will be returned to the login page and we can start learning few features of BurpSuite.  

## **Subtask 1**: Intercepting

BurpSuite browser is automatically setup as a proxy for BurpSuite and we are able to intercept the traffic going trough it.

Open the Proxy tab in BurpSuite and go to HTTP history. If you followed the instructions, there should be already some GET and POST requests visible. You can create more by attempting to login with wrong credentials. Here is a captured example with username=admin and password=hello  

![burp6](https://user-images.githubusercontent.com/44393530/225861070-8ed0edbd-5d87-4611-8ed6-2c6069e27666.PNG)

Now go to the **Intercept** tab and turn interception on  

![interception1](https://user-images.githubusercontent.com/44393530/225861142-66179b6f-3728-49e1-aee9-5eadd96aeeb5.PNG)

Now enter the site with credentials  
Username: **admin**  
Password: **password**  

The site should be frozen since we have intercepted the POST request. We can now modify the request as we like in BurpSuite. Go ahead and modify the User-Agent highlighted in the picture below. Type into the user agent your name + name of a random household item. After you have done the modification, release the POST request by pressing **Forward**. Also forward the GET request but there is no need to modify it.  

![interception2](https://user-images.githubusercontent.com/44393530/225861303-69ecc52f-ca2c-40a0-97f9-bb50fb9e827b.PNG)

Turn off interception and find the edited request from HTTP history. It should show the 'Original Request' at first. Click the 'Original Request' button to reveal a dropdown menu and choose 'Edited Request'. Now your changes should be visible in the inspector. As your returnable, add a screenshot of your edited post so that all the following information is visible.  

-**Listing of the last POST and GET request including timestamps and port**  
-**Atleast 15 rows of the Edited POST request in Raw format**  

## **Subtask 2**: Repeater

in the DVWA, go to the **DVWA Security** Tab and raise the security level from *Low* to *Medium* and click **Submit**  

Now go the **Weak session IDs** Tab and press **Generate**. This creates a cookie called *dvwaSession*.  

Generating the new session ID should show up in your HTTP history as a POST request. Right click the request and select **Send to Repeater**. Move to the highlighted Repeater tab  

![repeater1](https://user-images.githubusercontent.com/44393530/225861807-5921d774-e322-4b6d-9753-be438c685fef.PNG)

With the Repeater we can send previously sent request as many times as we want and even modify them. You can repeat the request by pressing **Send**. Below the request you can see the response.  

For your next returnable, try to figure out how the **dvwaSession** cookie is generated by looking at the response after multiple repeats. Return a brief explanation on how a new cookie is generated and a screenshot where atleast 15 lines of code is visible from both a Request and a corresponding Response in Raw or Pretty format.  

## **Subtask 3**: Intruder

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

## **Subtask 4**: Decoder

As a last task, we will take a quick look a the **Decoder** tab.  

While dealing with many kinds of requests we constantly come across decoded data  

Open the **Decoder** and write your name and student number into the first section.  

![decoder1](https://user-images.githubusercontent.com/44393530/225862736-1c7fefc6-697e-45f2-b94f-f5e23e2bac35.PNG)

Then **Encode** it as **URL**

![decoder2](https://user-images.githubusercontent.com/44393530/225862810-89ff0cec-aead-4ce8-a0f7-5b7bdb5a763e.PNG)

Then **Encode** it as **HTML**

![decoder3](https://user-images.githubusercontent.com/44393530/225862886-4f932491-9e5e-4244-a10a-83287c03ede3.PNG)

Finally use the **Smart Decode** function. Return a screenshot of all the encoded and decoded results.

## **Clean up**

After getting your results you can close BurpSuite. Remember, that the BurpSuite project is temporary and you cannot access the results after closing.  

To close the docker image of DVMA, open the terminal window where docker is active and press **Ctrl+C**. This should close the image. You can also close the docker daemon with the same key combination. You can verify this with the command  

>docker info  

![docker stop](https://user-images.githubusercontent.com/44393530/225863084-e0e0ec21-9b46-480f-9603-a3bd5b72a4fa.PNG)

Return your PDF containing all returnables to the Moodle return box  
