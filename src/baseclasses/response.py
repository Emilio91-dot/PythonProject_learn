from src.enamc.global_enums import GlobalErrorMessage


class Response:
    """Convenience wrapper for JSON HTTP responses."""

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        if self.response_json is None:
            raise ValueError("The response JSON does not contain a 'data' field")

        if isinstance(self.response_json, list):
            self.parsed_object = [schema.model_validate(item) for item in self.response_json]
        else:
            self.parsed_object = schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        expected = status_code if isinstance(status_code, list) else [status_code]
        if self.response_status not in expected:
            raise AssertionError(GlobalErrorMessage.WRONG_STATUS_CODE.value)
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return f"Response(status={self.response_status})"
