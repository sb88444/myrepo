"""
> Use some rest client to make call to  http://deploynow.opexsoftware.com/DeployNow/rest/auth/login,
> use:  json payload {user: "ganesh.e.khakare@gmail.com", password: "0pex@123"} 
> Now using rest client and end point http://deploynow.opexsoftware.com/DeployNow/rest/provider …
> use the SESSION ID cookie from login api to make a GET call on this end point..
  it will return a JSON array , loop through it and print the name and the type. 
"""

import httplib2
import json

class testExample():

    def __init__(self):
        self.urlLogin = "https://deploynow.opexsoftware.com/DeployNow/rest/auth/login"
        self.urlLoginTest = "http://deploynow.opexsoftware.com/DeployNow/rest/provider"
        self.data = json.dumps({"user": "ganesh.e.khakare@gmail.com", "password": "0pex@123"})
        self.conn = httplib2.Http(".cache")
        self.headers = {"Content-Type": "application/json"}

    def login(self):
        """  Login into """
        cookie = None
        try:
            (resp, content) = self.conn.request(self.urlLogin,"POST", body=self.data, headers=self.headers) 
        except Exception as e:
            print "Error : %s" % e
            return None
        if self._valid_response(resp['status']):
            cookie = resp['set-cookie']
        return cookie
    # End login
        
    def get_json_array(self, headers):
        json_dict = None
        try:
            (resp, content) = self.conn.request(self.urlLoginTest,"GET", body=self.data, headers=headers)
        except Exception as e:
            print "Error : %s" % e
            return None
        if self._valid_response(resp['status']):
            json_dict = json.loads(content)
        return json_dict
    # End get_json_array

    def _valid_response(self, status):
        if status != "200":
            print resp['status']
            print "Failed to login"
            return False
        return True
    # End get_json_array
# End Class           


def main():
    test = testExample()
    cookie = test.login()
    headers = {'Cookie': cookie}

    item_dict = test.get_json_array(headers)
    for item in item_dict:
        print "name: %s" % item['name']
        print "type: %s" % item['type']



if __name__=="__main__":
    main()
