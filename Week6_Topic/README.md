# **Week 6**

## Point distribution

- Task 1: 1 point
- Task 2: 1 point
- Task 3: 2 points

## **Task 3**: Securing Docker

**Linux required for full completion**

In this exercise we are checking out some tools to help you create better and more secure Docker containers. You are to either use your own Dockerfiles or images, create your own dockerfile for this exercise or you can use ones created by other people. The important part here is auditing and fixing the file, image or container. And you shouldn't use ones that have been audited; the files you choose for this task should provide some warnings, this is likely with most files.

> A small warning, as these tool can be quite complicated, if you have not used similar tools before, reading the documentation may take some time.

**Task 1A) Linting the Dockerfile**

We will start by first linting the Dockerfile, this will let you know the problems with the configuration, for example using the ```:latest``` tag. Depending on the type of Dockerile you are linting and which tool you are using to do this, you will be presented either with just the problems or the tool can give you directions on fixing these issues. 

You are free to use any Dockerfile linting tool you want, however a great tool worthy of a recommendation is [Hadolint](https://github.com/hadolint/hadolint), they also have a [GUI Web tool](https://hadolint.github.io/hadolint/) for those interested. The web tool is quite great, but doesn't offer the same customizability as the CLI tool, the functionality should be enough for this task if you don't feel comfortable on the command line. As stated on their GitHub, the tool can also be run on Docker, this makes it easier to run on different environments. ```docker pull hadolint/hadolint``` to pull the image. 

Here is a great chance to contribute to open source projects if you are looking for a great way to start contributing. You can find Open Source Software with Dockerfiles and lint these, fix the problems provided by the linter if they seem valid, open up a pull request and suggest these fixes with good explanations. 

Not all problems have to be fixed, but of course you should aim for fixing everything you can without breaking the program.

### What to return:
- What linter you used
- The dockerfile, before and after fixes
- Screenshot or .md file of the linter before and after fixes

[Hadolint](https://github.com/hadolint/hadolint)  
[Hadolint Web GUI](https://hadolint.github.io/hadolint/) 

**Task 1B) Static analysis**

Next comes analyzing the image for vulnerabilities in application containers. It is also common to use these scanners in CI/CD pipelines. You can use any analyzer you want, but we're going to recommend [Clair](https://github.com/quay/clair). Clair has awesome [documentation](https://quay.github.io/clair/) and you should refer this when using the tool, they cover at least **most** use cases and problems. You can use their [local dev environment](https://quay.github.io/clair/howto/testing.html) for this task. Their document says it is 
> "The easiest way to get Clair up and running for test purposes"

Here it is okay to not have any vulnerabilities, but in your answers it should show you have scanned.

### What to return:
- What analyzer you used
- The image used, or the Dockerfile to build it
- Screenshot or .md file of the analyzer output before and (if you did fix something) after the fixes

[Clair](https://github.com/quay/clair)  
[Clair docs](https://quay.github.io/clair/)

**Task 1C) Runtime Security**

Finally we are going to look at the runtime security of containers, here again you can use any tool you are more comfortable with, but we're going to recommend [Falco](https://github.com/falcosecurity/falco). They as well have a vast [documentation](https://falco.org/docs/) with multiple ways to install ad run the tool. The documentation has instructions for [installing on different Linux distributions](https://falco.org/docs/getting-started/source/), and we recommend following these, or following their own [tutorials](https://falco.org/docs/tutorials/).

Your goal here is to trigger alerts with the Falco tool, you can do this with ```--privileged``` containers, as the ```--privileged``` flag itself creates an alert. However if you can, try to trigger another alert from inside the container, here again their documentation provides great instructions on which types of activities create alerts.

> A good video with nice demo to help if documentation starts feeling dry: [The Video](https://www.youtube.com/watch?v=rBqBrYESryY&ab_channel=CNCF%5BCloudNativeComputingFoundation%5D)

### What to return:
- What runtime security scanner you used
- The image used, or the Dockerfile to build it
- Screenshot or .md file of the alerts created

[Falco](https://github.com/falcosecurity/falco)  
[Falco docs](https://falco.org/docs/)
