# **Week 6**

### Grading

Task #|Points|Description|
-----|:---:|----------|
[Task 1](#task-1-secure-running-environment) | 1 | Secure Running Environment
[Task 2](#task-2-supply-chain-attacks) | 1 | Supply Chain Attacks 
[Task 3](#task-3-securing-docker) | 2 | Securing docker

---

# Tasks

### Task 1: Secure Running Environment?

It is important to understand the differences and security capabilities of the concepts listed below. Choose two out of the four concepts and write a short explanation of them and their respective security capabilities and incapabilities.

Focus on giving a good overview of the security limits for the concepts.

- TPM
- Enclave
- Container
- Virtualization

**Max 300 words excluding sources.**

---

### Task 2: Supply Chain Attacks

In this task we are looking at the difficulties handling supply chain attacks, specifically detecting and responding.

For this scenario you are working for a networking hardware and software company, and you're tasked with securing their supply chain. The company manufactures and sells routers with their own software and other various networking accessories B2B and B2C.  Some parts for the routers have to be outsourced and manufactured outside company.

Research and write a report on concrete actions you could implement on the supply chain, trying to make sure the product is not being tampered or researched with malicious intent. Keep in mind, that the supply chain includes third party tools, code and update providing, as well as other companies maintaining firmware. Your supply chain must include **at least four** actors including your company. You should analyze the points of concerns in the report.

Provide reasoning for your choices and analyze what potential problems and additional actions these choices might require from your company.

Probable actors in such supply chains include, but are not limited to:

- Employees, in-house and outsourced
- Transportation companies
- Retail companies
- Storage facilities
- Part suppliers

<details>
<summary>Example supply chain</summary>
<br>

Hardware
- 3rd party company X manufactures antennas for the routers
- Truck company Y transports them to 
- Factory Z, where it is assembled by workers 
- Y transports them to resellers A and B

<br>

Software
- Own employees create it
- Company C provides contractual coders for help
- Company D audits software
- Company E hosts internal tools

<br>
You can use the examply supply chain in your task if you want to.
<br>
</details>

Some concepts to help you get started:
- NDR (Network Detection and Response)
- UBA (User Behavioral Analytics)
- EDR (Endpoint Detection and Response)
- TPM (Trusted Platform Module)

Real-life cases for inspiration:
- [SolarWinds](https://www.gao.gov/blog/solarwinds-cyberattack-demands-significant-federal-and-private-sector-response-infographic)
- [Routers, servers and networking equipment from the USA](https://www.infoworld.com/article/2608141/snowden--the-nsa-planted-backdoors-in-cisco-products.html) | Notice the second page accessible at the bottom of the article

**Minimum 500 words,  
Maximum 4 visual representations,  
Each visual representation is minus 50 words off the total required.**

For example a report with 3 visuals requires 350 words.  
The visuals must be useful for the report, ex. company logos do not count.

---

### Task 3: Securing Docker

**Linux required for full completion; [Course provided VM](https://ouspg.org/archlinux)**

In this exercise we are checking out some tools and practices to help you create better and more secure Docker containers. You are to either use your own Dockerfiles or images, create your own dockerfile for this exercise or you can use ones created by other people. The important part here is auditing and fixing the files, image or container. You shouldn't use ones that have been well audited; the files you choose for this task should provide some output, this is likely with most files.

> We have added an example Dockerfile with an additional file it needs, you may use this, but it might not be the easiest or best way to complete the task. You **need** to add permissions for the executable 'docker-entrypoint.sh' file before building.

These tasks provide a great chance to contribute to open source projects, especially if you are looking for a great way to make your first pull requests. You can find Open Source Software with Dockerfiles and lint these, fix the problems provided by the linter when valid, open up a pull request and suggest these fixes with good explanations. 

Your analysis with Trivy (or scanner of your choice) can be opened as an issue, or you can write it into a report and try to open a pull request for it or fixes you made. These might require more work to get accepted though, but can be a great contribution to certain projects.

> A small warning, as some of these tools can be quite complicated, reading through the documentation could take some time. All necessary parts **should** be in this task sheet, but not all problems can be covered. And due to the nature of the course, we expect students to learn and be able to read and take in documentations.

---

### Task 3A) Linting the Dockerfile 0.5p

We will start by first linting the Dockerfile, this will let you know of problems with the configuration, for example using the ```:latest``` tag. These tools will guide you towards  the best practices regarding [Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/). 

You are free to use any Dockerfile linting tool you want, however a great tool worthy of a recommendation is [Hadolint](https://github.com/hadolint/hadolint), they have the tool packaged into a container and they also have a [GUI Web tool](https://hadolint.github.io/hadolint/) for those interested. The web tool is quite great, but doesn't offer the same customizability as the CLI tool, the functionality is enough for this task, especially if you don't feel comfortable on the command line. As stated, the tool can also be run on Docker, this makes it easier to run on different environments. 

```docker pull hadolint/hadolint```  
To pull the image and can be run with:  
```docker run --rm -i hadolint/hadolint < Dockerfile```

> For running with custom rules and/or personal modifications you should refer to their own [instructions](https://github.com/hadolint/hadolint#how-to-use). 

Depending on the type of Dockerfile you are linting and which tool you are using to do this, you will be presented either with just the problems or the tool can give you directions on fixing these issues. 

Not all problems indicated by the tool have to be fixed, and not all warnings should be fixed blindly, but of course you should aim for fixing everything you can, while not breaking the program.

### What to return:
- What linter you used
- The dockerfile, before and after fixes
- Screenshot **or** .md file of the linter before and after fixes

[Hadolint](https://github.com/hadolint/hadolint)  
[Hadolint Web GUI](https://hadolint.github.io/hadolint/) 

---

### Task 3B) Container Image Analysis 0.5p

Next comes analyzing the image for vulnerabilities in containers. It is also common to use these scanners in CI/CD pipelines. Again, you can use any analyzer you want, but we're going to recommend [Trivy](https://github.com/aquasecurity/trivy). Trivy is an open source project by [Aquasecurity](https://www.aquasec.com/), and it has quite the nice [documentation](https://aquasecurity.github.io/trivy/v0.41/). This task should be doable without reading too much documentation, we do  however recommend checking it out.  They cover at least **most common** use cases and problems there. You can also refer to this documentation if you want to know more about the tool itself and other ways you can use it, such as Kubernetes, filesystem and GitHub repository scanning.

For building from Dockerfile ```docker build -t <name> .```

Trivy can be run on docker or it can be installed from a [binary](https://github.com/aquasecurity/trivy/releases/tag/v0.45.1) or from a [package manager](https://aquasecurity.github.io/trivy/v0.45/getting-started/installation/)  

For Archlinux ```pacman -S trivy```  
And then you can run it with:  
```trivy image <image_name>``` for Docker images.  

Running on docker should work with ```docker run aquasec/trivy image <image_name>```
  
Here you should **try** to fix atleast some errors, the recommended tool Trivy can tell you if a vulnerable piece of software has a patch or a newer version that addressed the vulnerability. However we do understand that not every vulnerability can be fixed.

### What to return:
- What analyzer you used
- The image used, **or** the Dockerfile to build it
- Screenshot **or** .md file of the analyzer output before and after the fixes

[Trivy](https://github.com/aquasecurity/trivy)  
[Trivy docs](https://aquasecurity.github.io/trivy/v0.41/)

---

### Task 3C) Runtime Security 1p

Finally we are going to look at the runtime security of containers, here again you can use any tool you want to, but we're going to recommend a tool originally by [Sysdig](https://sysdig.com/), currently under [CNCF](https://www.cncf.io/). The tool [Falco](https://github.com/falcosecurity/falco) is designed to detect and alert in real-time. The tool is for Linux operating systems.

They as well have a vast and very detailed [documentation](https://falco.org/docs/) with multiple ways to install and run the tool. The documentation has instructions for [installing on different Linux distributions](https://falco.org/docs/getting-started/source/), installing the [falco binary](https://falco.org/docs/getting-started/installation/#falco-binary), and running with Docker, which we recommend here. You can also use their own [tutorials](https://falco.org/docs/tutorials/) to get more familiar with the tool.

### Installing into Docker

For this task we are going to use the Fully Privileged Modern eBPF version, you can find more information and other ways to run it [here](https://falco.org/docs/setup/container/). 

The command provided on the page is  
```
docker pull falcosecurity/falco-no-driver:latest
docker run --rm -it \
           --privileged \
           -v /var/run/docker.sock:/host/var/run/docker.sock \
           -v /proc:/host/proc:ro \
           -v /etc:/host/etc:ro \
           falcosecurity/falco-no-driver:latest
```

This command will be enough to get you up and running with Falco, given you are already using linux with docker working.

### Triggering Alerts

If you used another way to install you need to choose the rules. If you used the method above, you can go forward and start looking at triggering alerts. 

For the task you need to trigger alerts about and from within the containers. One easy way you can trigger an alert is with ```--privileged``` containers, as the ```--privileged``` flag itself creates an alert.  

However you are to trigger another alert from within the containers, here again their documentation provides great instructions on which types of activities create which types of alerts, and with which rulesets, the above method uses the modern eBPF. 

If you are using the example Dockerfile for these tasks, you may for example install and/or run software inside a container for some output from falco.

> `docker run -it <image_name> /bin/sh` can be used to start an interactive shell in a container. You can use any shell you want, like bash, but not every distribution, or container has it.

You can modify the rules provided with the installation, not mandatory, however it is encouraged to take look at least.

### What to return:
- What runtime security scanner you used
- The image used, **or** the Dockerfile to build it
- Screenshot **or** .md file of the alerts created
- What commands and/or activities used to trigger the alerts

[Falco](https://github.com/falcosecurity/falco)  
[Falco docs](https://falco.org/docs/)
