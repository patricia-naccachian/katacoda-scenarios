#Docker Time!

##Creating Docker Image

In this step, we will create the Docker file. Docker is very case sensitive. We save this file as "Dockerfile" in the same file as "app.py" and "requirements.txt".

```
FROM python:3.7

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [“python3”]

CMD [“python","app.py”]
```

Now, we build a docker image using the command line, execute the following code.

`docker build -t atadevops.azurecr.io/atadevops-mlmodel:latest .`{{execute}}

atadevops.azurecr.io is the is the name of the registry that you get when you create a resource on Azure portal. 
"atadevops" stands for Automated Testing and DevOps.
atadevops-mlmodel is the name of the image, it can be anything we want. 
latest is the tag. 

##Running Container from Docker Image

Now that the image is created we will run a container locally and test the application before we push it to Azure Container Registry. To run the container locally execute the following code:

`docker run -d -p 5000:5000 atadevops.azurecr.io/atadevops-mlmodel`{{execute}}

## Next Step

In the next, we will proceed to upload the container onto ACR!