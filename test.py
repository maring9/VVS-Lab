import requests


def test_main_page_status_code(code):
    response = requests.get('http://localhost:8080')
    assert code == response.status_code


def test_main_page_response(expectation):
    response = requests.get('http://localhost:8080')
    assert expectation == response.json()
    

def test_random_string():
    response = requests.get('http://localhost:8080/random')
    assert 200 != response.status_code
    
if __name__ =='__main__':
    test_main_page_status_code(200)
    test_main_page_response({'Software Verification and Validation': 'Welcome', 'Status': 200})
    test_random_string()
    
    print('Tests were successfull')