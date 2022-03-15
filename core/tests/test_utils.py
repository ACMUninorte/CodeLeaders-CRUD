import json

from rest_framework.test import APIClient


class TestApiBase:
    def init(self):

        self.client = APIClient()
        self.json_response = {}
        self.print_output = False

    def send_request(self, request_method, *args, **kwargs):
        request_func = getattr(self.client, request_method)
        status_code = None

        if "multipart" not in kwargs:
            if "content_type" not in kwargs and request_method != "get":
                kwargs["content_type"] = "application/json"
                if "data" in kwargs:
                    data = kwargs.get("data", "")
                    kwargs["data"] = json.dumps(data)
        else:
            kwargs.pop("multipart")

        if "status_code" in kwargs:
            status_code = kwargs.pop("status_code")

        if "token" in kwargs:
            kwargs["HTTP_AUTHORIZATION"] = "Bearer %s" % kwargs.pop("token")

        self.response = request_func(*args, **kwargs)

        is_json = False
        if "content-type" in self.response._headers:
            content_types = self.response._headers["content-type"]
            is_json = "application/json" in content_types

        if is_json and self.response.content:
            self.json_response = self.response.json()
            if self.print_output:
                print(json.dumps(self.json_response, indent=4, ensure_ascii=False))

        if status_code:
            assert self.response.status_code == status_code

        return self.response

    def post(self, *args, **kwargs):
        return self.send_request("post", *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.send_request("get", *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.send_request("put", *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.send_request("patch", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.send_request("delete", *args, **kwargs)
