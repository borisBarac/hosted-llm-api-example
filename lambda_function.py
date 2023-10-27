import json
import os
import io
import boto3

LLAMA2_URL = os.environ['LLAMA2_URL']
sagemaker = boto3.client('runtime.sagemaker')

user_error_ret = {
    'statusCode': 401,
    'body': json.dumps('wrong body params')
}

def make_llama_json_query(user_context, system_context):
    return {
        "inputs": [[
            {"role": "system", "content": system_context},
            {"role": "user", "content": user_context}
            ]],
        "parameters": {
            "max_new_tokens":256, 
            "top_p":0.9, 
            "temperature":0.6
        }
    }

def lambda_handler(event, context):
    body = event['body']
    if type(body) is not str:
        return user_error_ret
    
    body_dict = json.loads(body)
    content_system = body_dict.get('content_system')
    content_user = body_dict.get('content_user')
    
    if content_user is None or content_system is None:
        return user_error_ret
    
    llama2_query = make_llama_json_query(content_user, content_system)
    llama2_response = sagemaker.invoke_endpoint(
        EndpointName=LLAMA2_URL,
        ContentType='application/json',
        Body=llama2_query,
        CustomAttributes="accept_eula=true"
    )
    
    result = json.loads(llama2_response['Body'].read().decode())

    return {
        'statusCode': 200,
        'headers': {'content-type': 'application/json'},
        'body': json.dumps(result)
    }