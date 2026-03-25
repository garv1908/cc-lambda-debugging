import unittest
from lambda_function1 import lambda_handler

score = 0

class TestLambdaFunction1(unittest.TestCase):

    def test_conversion(self):
        result = lambda_handler({"temperature": 25})
        self.assertEqual(result['body'], 77.0)
        score = score + 1
    
    def test_return_object(self):
        result = lambda_handler({"temperature": 25})
        self.assertEqual(result, {"statusCode": 200, "body": 77.0})
        score = score + 1

    def test_zero_celsius(self):
        result = lambda_handler({"temperature": 0})
        self.assertEqual(result['body'], 32.0)
        score = score + 1
    
    def test_negative_temperature(self):
        result = lambda_handler({"temperature": -40})
        self.assertEqual(result['body'], -40.0)
        score = score + 1

    
    def test_boiling_point(self):
        result = lambda_handler({"temperature": 100})
        self.assertEqual(result['body'], 212.0)
        score = score + 1
    
    def test_decimal_temperature(self):
        result = lambda_handler({"temperature": 36.5})
        self.assertEqual(result['body'], 97.7)
        score = score + 1
    
    def test_missing_temperature(self):
        result = lambda_handler({})
        self.assertEqual(result['statusCode'], 400)
        score = score + 1

    def test_none_temperature(self):
        result = lambda_handler({"temperature": None})
        self.assertEqual(result['statusCode'], 400)
        score = score + 1
    
    def test_large_temperature(self):
        result = lambda_handler({"temperature": 1000})
        self.assertEqual(result['body'], 1832.0)
        score = score + 1
    
    def test_absolute_zero(self):
        result = lambda_handler({"temperature": -273.15})
        self.assertEqual(result['body'], -459.67)
        score = score + 1

if __name__ == '__main__':
    unittest.main()
    print(score)