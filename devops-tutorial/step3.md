# Azure Container Registry  

Azure Container Registry (ACR) is an Azure-based, private registry, for Docker container images. 

First, we have to authenticate azure credentials on our local machine. We execute the following:

`docker login atadevops.azurecr.io`{{execute}}

The username is the name of our registry. In this case, our username is: "atadevops".
The password is under the Access keys of the Azure Container Registry resource that we created.

After authenticating, we can push the container we created to ACR. We execute the following:

`docker push atadevops.azurecr.io/atadevops-mlmodel:latest`{{execute}}

BOOM! We have finally succeeded in transfering the container to the cloud!


