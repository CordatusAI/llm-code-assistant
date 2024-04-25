# LLM Code Assistant
![Welcoming GIF](/assets/intro.gif)
This application aims to provide Cordatus users an out of the box local code assitant. It is built on top of Ollama to support wide range of Generative AI models including LLaMA-3, Phi-3, Codegemma, StarCoder2, Code-LLaMA, etc. The Streamlit web interface enables easy interaction with all the LLM models including selecting different models, code explanation, code optimization, code review and code writing tasks as well as file analysis for more complex texts. 

Application can be deployed seamlessly with Cordatus AI over a web browser or locally by building an image from the provided Dockerfile.

## 1. Deploying with Cordatus AI (Preferred)
This method allows you to access this application remotely while giving you additional abilities such as Remote SSH, AI Application Deployment, and Device Monitoring/Management.

### 1.1 Create an Account
You can create an account from **[this link](https://app.cordatus.ai/#/register)** for free.

![Register Page](/assets/register.png)

### 1.2 Register Your Device
Once you login to your account, navigate to the Download page from the left menu. Click on the Download Now button to get the automated installation script for the Cordatus AI.

![Download Page](/assets/download.png)

```
$ cd ~/Downloads
$ sudo chmod +x cordatus_install.sh
$ ./cordatus_install.sh
```
Once you run the script, please answer the prompts accordingly and confirm the step where reboot confirmation is asked.

After the reboot, please login to your account from Cordatus AI Client on NVIDIA Jetson or x86 device.

### 1.3 Deploy the Application
Navigate to the Applications tab from the left menu and find **Generative AI Applications** card.

![Applications Page](/assets/apps.png)

Once you enter the Details page, click on the **START APPLICATION ON YOUR DEVICE** button.

Select the device from the list which you want to deploy LLM Code Assistant application on and click on the Continue button.

![Select Device](/assets/select_device.png)

Select the appropriate app version from the list and continue.

![Select Version](/assets/select_version.png)

Set the remaining options for your remote deployment.

![Set Options](/assets/set_options.png)

### 1.4 Access to Application

## 2. Deploying with Docker Image Locally (Optional)
To deploy the application standalone, run the following command to run the Docker container.

```
$ docker run -ti \
        --gpus=all \
        --net=host \
        -v ~/ollama:/root/.ollama \
        cdcr.dev/cordatus/generative-ai-apps:llm-code-assistant
```

![Local Access](/assets/local_access.png)

Navigate to the local IP address and port combination using one of your web browser.

## BONUS: Build Docker Image Locally
You can also build and run the Docker image locally on your devices

```
$ git clone https://github.com/CordatusAI/llm-code-assistant.git
$ cd llm-code-assistant/
$ docker build -f Dockerfile -t cordatus/generative-ai-apps:local-llm-code-assistant .
```
```
$ docker run -ti \
        --gpus=all \
        --net=host \
        -v ~/ollama:/root/.ollama \
        generative-ai-apps:local-llm-code-assistant
```