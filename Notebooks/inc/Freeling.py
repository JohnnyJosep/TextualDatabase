import re
import requests

class Freeling:
    def __init__(self, host, port):
        self.endpoint = f'http://{host}:{port}'
        
    
    def analizer(self, text, logs=False):
        if logs:
            print(text)
        headers = {'Content-Type': 'text/plain'}
        
        response = requests.post(self.endpoint, headers=headers, data=text.encode('utf-8'))
        content = response.content.decode('utf-8')
        content = re.sub('\n\n', '\n', content)
        content = re.sub('\n$', '', content)
        
        if logs:
            print(content)
            
        return content
        