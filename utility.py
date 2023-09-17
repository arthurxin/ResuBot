import os
import openai

class openai_chat:
    def __init__(self, key_path = "../../../.flying/"):
        with open(key_path + "openai_key.txt","r") as f:
            openai.api_key = f.readline().rstrip("\n")
    
    def get_completion_from_messages(self, messages, temperature=1, max_tokens=500):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            temperature=temperature, 
            max_tokens=max_tokens,
        )
        return response.choices[0].message["content"]

    def get_completion_from_messages_16k(self, messages, temperature=1, max_tokens=500):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=messages,
            temperature=temperature, 
            max_tokens=max_tokens,
        )
        return response.choices[0].message["content"]
    
def readtxtfile(filename):
    lines = ""
    with open(filename,'r') as file:
        for item in file:
            lines += item
    return lines

def get_openapi_key(key_path = "../../../.flying/"):
    with open(key_path + "openai_key.txt","r") as f:
            key = f.readline().rstrip("\n")
    return key

def get_claude_key(key_path = "../../../.flying/"):
    with open(key_path + "claude_key.txt","r") as f:
            key = f.readline().rstrip("\n")
    return key