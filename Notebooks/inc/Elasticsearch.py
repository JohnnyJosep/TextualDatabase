import json
import requests

class Elasticsearch:
    def __init__(self, host, port, username, password):
        self.endpoint = f'http://{username}:{password}@{host}:{port}'
        self.headers = {'Content-Type': 'application/json'}
            
            
    def postData(self, index, data, logs=False):
        url = f'{self.endpoint}/{index}/_doc'
        jsonData = json.dumps(data, indent=2)
        
        if logs:
            print(f'POST {url}')
            print(jsonData)
            
        response = requests.post(url, headers=self.headers, data=jsonData)
        if response.status_code != 201 or logs:
            print(response.text)
            
    
    def getDateHistogram(self, index, field, interval="day", logs=False):
        url = f'{self.endpoint}/{index}/_search?size=0'
        data = {"aggs": {"over_time": {"date_histogram": {"field": field, "calendar_interval": interval}}}}        
        jsonData = json.dumps(data, indent=2)
        
        if logs:
            print(f'POST {url}')
            print(jsonData)
            
        response = requests.post(url, headers=self.headers, data=jsonData)
        if response.status_code > 300 or logs:
            print(response.status_code)
            print(response.text)
            
        jsonResponse = json.loads(response.text)
        results = []
        for result in jsonResponse['aggregations']['over_time']['buckets']:
            value = {'key': result['key_as_string'], 'count': result['doc_count']}
            results.append(value)
        
        return results
    
    
    def getTermAggregation(self, index, field, logs=False):
        url = f'{self.endpoint}/{index}/_search?size=0'
        data = {"aggs": {"termAggs": {"terms": { "field": field, "size": 1000 }}}}
        
        jsonData = json.dumps(data, indent=2)
        
        if logs:
            print(f'POST {url}')
            print(jsonData)
            
        response = requests.post(url, headers=self.headers, data=jsonData)
        if response.status_code > 300 or logs:
            print(response.status_code)
            print(response.text)
            
        jsonResponse = json.loads(response.text)
        results = []
        for result in jsonResponse['aggregations']['termAggs']['buckets']:
            value = {'key': result['key'], 'count': result['doc_count']}
            results.append(value)
        
        return results
    
    def getRange(self, index, field, gte, lt, logs=False):
        url = f'{self.endpoint}/{index}/_search'
        data = {"query": {"range": {field: {"gte": gte, "lt": lt}}}}
        
        jsonData = json.dumps(data, indent=2)
        
        if logs:
            print(f'POST {url}')
            print(jsonData)
            
        response = requests.post(url, headers=self.headers, data=jsonData)
        if response.status_code > 300 or logs:
            print(response.status_code)
            print(response.text)
            
            
        jsonResponse = json.loads(response.text)
        results = []
        for result in jsonResponse['hits']['hits']:
            results.append(result['_source'])
        
        return results
        