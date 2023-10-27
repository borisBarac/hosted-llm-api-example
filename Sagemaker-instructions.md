## Sagemaker model deploy steps:

Sagemaker has a bunch of pretrained models you can use. I was not able to find to to deploy the pretrained model as code, so that is why you have this file.


### Steps:

- Get aws permission to run GPU instances i used the g5.2xlarge for LLAMA2 7B chat model - 24gb gpu ram, price was 1.12$ per hour
- Make sure you are on **EU-WEST** regin (not all regions have all models)
- Go to jumpstart page, and jumpstart the sagemaker console (this step is gonna make a domain and a user automatically)
- Once the console is up, go to models, pick LLAMA2 7B, click deploy, and select the instance you want to run.
- In a couple of minutes the MODEL is gonna be deployed, and you will get a url you can use to access it from services
- you need to put this URL in the ENVINRONMENT of the lambda we are using to consume the model.


### Notes:
When done, do not forget to turn of the model, and shut down the console. This things are not cheap.
AWS is even charging when the console is running.