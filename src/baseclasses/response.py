##from jsonschema import validate



from src.enamc.global_enums import GlobalErrorMessage



class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.response_status = response.status_code
        self.parsed_object = None


    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed.object = schema.parse_obj(item)
                self parsed_object = parsed_object
        else:
            schema.parse_obj(self.response_json)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        return self


    def get_parsed_object(self):
        return self.parsed_object
    def __str__(self):
        return ("Hi there")


       ## for item in reversed_posts:
            ##validate(item, POST_SCHEMA)