# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import pytest
from unittest.mock import Mock

# module under test
from corehttp.exceptions import (
    HttpResponseError,
    SerializationError,
    DeserializationError,
)
from corehttp.rest import HttpRequest

from rest_client import MockRestClient
from utils import SYNC_TRANSPORTS


class FakeErrorOne(object):
    def __init__(self):
        self.error = Mock(message="A fake error", code="FakeErrorOne")


class FakeErrorTwo(object):
    def __init__(self):
        self.code = "FakeErrorTwo"
        self.message = "A different fake error"


class FakeHttpResponse(HttpResponseError):
    def __init__(self, response, error, *args, **kwargs):
        self.error = error
        super(FakeHttpResponse, self).__init__(self, response=response, *args, **kwargs)


class TestExceptions(object):
    def test_empty_httpresponse_error(self):
        error = HttpResponseError()
        assert str(error) == "Operation returned an invalid status 'None'"
        assert error.message == "Operation returned an invalid status 'None'"
        assert error.response is None
        assert error.reason is None
        assert error.status_code is None

    def test_message_httpresponse_error(self):
        error = HttpResponseError(message="Specific error message")
        assert str(error) == "Specific error message"
        assert error.message == "Specific error message"
        assert error.response is None
        assert error.reason is None
        assert error.status_code is None

    def test_error_continuation_token(self):
        error = HttpResponseError(message="Specific error message", continuation_token="foo")
        assert str(error) == "Specific error message"
        assert error.message == "Specific error message"
        assert error.response is None
        assert error.reason is None
        assert error.status_code is None
        assert error.continuation_token == "foo"

    @pytest.mark.parametrize("transport", SYNC_TRANSPORTS)
    def test_httpresponse_error_with_response(self, port, transport):
        request = HttpRequest("GET", url="http://localhost:{}/basic/string".format(port))
        client = MockRestClient(port, transport=transport())
        response = client.send_request(request, stream=False)
        error = HttpResponseError(response=response)
        assert error.message == "Operation returned an invalid status 'OK'"
        assert error.response is not None
        assert error.reason == "OK"
        assert isinstance(error.status_code, int)

    @pytest.mark.parametrize("transport", SYNC_TRANSPORTS)
    def test_httpresponse_error_with_model(self, port, transport):
        request = HttpRequest("GET", url="http://localhost:{}/basic/string".format(port))
        client = MockRestClient(port, transport=transport())
        response = client.send_request(request, stream=False)
        error = HttpResponseError(response=response, model=FakeErrorTwo())
        assert error.message == "Operation returned an invalid status 'OK'"
        assert error.response is not None
        assert error.reason == "OK"
        assert error.model
        assert error.model.code == "FakeErrorTwo"
        assert error.model.message == "A different fake error"
        assert isinstance(error.status_code, int)

    @pytest.mark.parametrize("transport", SYNC_TRANSPORTS)
    def test_malformed_json(self, port, transport):
        request = HttpRequest("GET", "/errors/malformed-json")
        client = MockRestClient(port, transport=transport())
        response = client.send_request(request)
        with pytest.raises(HttpResponseError) as ex:
            response.raise_for_status()
        assert (
            str(ex.value)
            == 'Operation returned an invalid status \'BAD REQUEST\'\nContent: {"code": 400, "error": {"global": ["MY-ERROR-MESSAGE-THAT-IS-COMING-FROM-THE-API"]'
        )

    @pytest.mark.parametrize("transport", SYNC_TRANSPORTS)
    def test_text(self, port, transport):
        request = HttpRequest("GET", "/errors/text")
        client = MockRestClient(port, transport=transport())
        response = client.send_request(request)
        with pytest.raises(HttpResponseError) as ex:
            response.raise_for_status()
        assert str(ex.value) == "Operation returned an invalid status 'BAD REQUEST'\nContent: I am throwing an error"


def test_serialization_error():
    message = "Oopsy bad input passed for serialization"
    error = SerializationError(message)
    with pytest.raises(SerializationError) as ex:
        raise error
    assert str(ex.value) == message

    with pytest.raises(ValueError) as ex:
        raise error
    assert str(ex.value) == message


def test_deserialization_error():
    message = "Oopsy bad input passed for serialization"
    error = DeserializationError(message)
    with pytest.raises(DeserializationError) as ex:
        raise error
    assert str(ex.value) == message

    with pytest.raises(ValueError) as ex:
        raise error
    assert str(ex.value) == message
