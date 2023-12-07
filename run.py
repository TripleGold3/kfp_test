import json

metadata = {
    'outputs': [{
        'type': 'web-app',
        'storage': 'inline',
        'source': "<iframe src='http://10.43.129.213:30021' width='100%' height='600px'></iframe>",
    }]
}

with open('/mlpipeline-ui-metadata.json', 'w') as f:
    json.dump(metadata, f)
