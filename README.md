### Self Hosted LLM Model with an Api

This is a simple example that shows how you can host **LLM open source models** (**LLAMA 2** in this case) on **AWS**, and expose them to your API.
<br/> You can see the configuration of the API GATEWAY setting i used to get it running in this repo. Also you have a example LAMBDA function in puthon with it's SAM template.

<br/> Only part of the code i was not able to make code infrastructure is the actual model deployment inside of SAGEMAKER. For that part and the details how to do it please refer to the [sagemaker-instructions](./Sagemaker-instructions.md)