# **Week 6**

## Point distribution

- Task 1: 1 point
- Task 2: 1 point
- Task 3: 2 points

## **Task 3**: Securing Docker

**Linux server type VM recommended. Follow instructions in [LINK]()**

In this exercise we are checking out some tools and practices to help you create better and more secure Docker containers. You are to either use your own Dockerfiles or images, create your own dockerfile for this exercise or you can use ones created by other people. The important part here is auditing and fixing the file, image or container. And you shouldn't use ones that have been well audited; the files you choose for this task should provide some output, this is likely with most files.

These tasks provide a great chance to contribute to open source projects, especially if you are looking for a great way to make your first pull requests. You can find Open Source Software with Dockerfiles and lint these, fix the problems provided by the linter if valid, open up a pull request and suggest these fixes with good explanations. Your analysis with Trivy (or scanner of your choice) can be opened as an issue, or you can write it into a report and try to open a pull request for it. These might require more work to get accepted though.

> A small warning, as some of these tools can be quite complicated,reading through the documentation could take some time. All necessary parts **should** be in this task sheet, but not all problems can be covered. And due to the nature of the course, we expect students to be able to read and take in documentations.

**Task 1A) Linting the Dockerfile**

We will start by first linting the Dockerfile, this will let you know of problems with the configuration, for example using the ```:latest``` tag. Depending on the type of Dockerile you are linting and which tool you are using to do this, you will be presented either with just the problems or the tool can give you directions on fixing these issues. 

You are free to use any Dockerfile linting tool you want, however a great tool worthy of a recommendation is [Hadolint](https://github.com/hadolint/hadolint), they also have a [GUI Web tool](https://hadolint.github.io/hadolint/) for those interested. The web tool is quite great, but doesn't offer the same customizability as the CLI tool, the functionality should be enough for this task if you don't feel comfortable on the command line. As stated on their GitHub, the tool can also be run on Docker, this makes it easier to run on different environments. ```docker pull hadolint/hadolint``` to pull the image. 

The Hadolint docker container has been pulled on the course VMs and can be run with:  
```docker run --rm -i hadolint/hadolint < Dockerfile```

Not all problems have to be fixed, and not all warnings should be fixed blindly, but of course you should aim for fixing everything you can while not breaking the program.

### What to return:
- What linter you used
- The dockerfile, before and after fixes
- Screenshot or .md file of the linter before and after fixes

[Hadolint](https://github.com/hadolint/hadolint)  
[Hadolint Web GUI](https://hadolint.github.io/hadolint/) 

**Task 1B) Image analysis**

Next comes analyzing the image for vulnerabilities in containers. It is also common to use these scanners in CI/CD pipelines. You can use any analyzer you want, but we're going to recommend [Trivy](https://github.com/aquasecurity/trivy). Trivy is an open source project by [Aquasecurity](https://www.aquasec.com/). It has quite the nice [documentation](https://aquasecurity.github.io/trivy/v0.41/). This task should be doable without reading documentaion, although they cover at least **most common** use cases and problems. You can also refer to this documentation if you want to know more about the tool itself and other ways you can use it, such as Kubernetes and GitHub repositories.

The tool has been installed on the course VMs and can be run with:  
```trivy image <image_name>``` for Docker image  
```trivy fs <folder_or_file>``` for Filesystem  
  
Here you should **try** to fix atleast some errors, the recommended tool Trivy can tell you if a vulnerable piece of software has a patch or a newer version that fixed the vulnerability. However we do understand that not every vulnerability can be fixed.

### What to return:
- What analyzer you used
- The image used, or the Dockerfile to build it
- Screenshot or .md file of the analyzer output before and (if you did fix something) after the fixes

[Trivy](https://github.com/aquasecurity/trivy)  
[Trivy docs](https://aquasecurity.github.io/trivy/v0.41/)

**Task 1C) Runtime Security**

Finally we are going to look at the runtime security of containers, here again you can use any tool you are more comfortable with, but we're going to recommend [Falco](https://github.com/falcosecurity/falco). They as well have a vast [documentation](https://falco.org/docs/) with multiple ways to install and run the tool. The documentation has instructions for [installing on different Linux distributions](https://falco.org/docs/getting-started/source/), and we recommend following these, or following their own [tutorials](https://falco.org/docs/tutorials/).

> Falco has been installed on the course VMs, however depending on the way used, might require configuration.

Your goal here is to trigger alerts with the tool, you can do this with ```--privileged``` containers, as the ```--privileged``` flag itself creates an alert. However if you can, try to trigger another alert from inside the container, here again their documentation provides great instructions on which types of activities create alerts.

### What to return:
- What runtime security scanner you used
- The image used, or the Dockerfile to build it
- Screenshot or .md file of the alerts created

[Falco](https://github.com/falcosecurity/falco)  
[Falco docs](https://falco.org/docs/)
