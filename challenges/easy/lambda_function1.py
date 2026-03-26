"""
Simple Temperature Converter Lambda Function
Convert Celsius to Fahrenheit
    
Expected input: {"temperature": 25}
Expected output: {"statusCode": 200, "body": 77}
"""
import json

def lambda_handler(event, context=None):
    celsius = event.get('temperature', None)
    
    if celsius == None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: temperature field is required')
        }
    
    # °F = (°C × 1.8) + 32
    fahrenheit = (float(celsius) * (9/5)) + 32
    fahrenheit = round(fahrenheit, 2)
    
    return {
        'statusCode': 200,
        'body': fahrenheit
    }
