# -*- coding: utf-8 -*-
import requests
import base64
import time
import logging

import mangopay
from .exceptions import APIError, DecodeError, AuthenticationError
from .signals import request_finished, request_started, request_error

from requests.exceptions import ConnectionError

try:
    import urllib.parse as urlrequest
except ImportError:
    import urllib as urlrequest

try:
    import simplejson as json
except ImportError:
    import json


logger = logging.getLogger('leetchi')

requests_session = requests.Session()


class APIRequest(object):
    def __init__(self, client_id=None, passphrase=None, api_url=None, api_sandbox_url=None, sandbox=True):
        if sandbox:
            self.api_url = api_sandbox_url or mangopay.api_sandbox_url
        else:
            self.api_url = api_url or mangopay.api_url

        self.my_client_id = client_id or mangopay.client_id
        self.my_passphrase = passphrase or mangopay.passphrase

    def _authorization(self):
        if self.my_client_id is None or self.my_passphrase is None:
            raise AuthenticationError(
                'Authentication failed. (Please set your Mangopay API username '
                'and password using "mangopay.client_id = CLIENT_ID" '
                'and "mangopay.passphrase = PASSPHRASE").')

        credentials = '%s:%s' % (self.my_client_id, self.my_passphrase)
        credentials = base64.b64encode(credentials.encode('ascii'))

        return 'Basic %s' % credentials

    def request(self, method, url, data=None, **params):
        params = params or {}

        headers = {
            'Authorization': self._authorization(),
            'Content-Type': 'application/json'
        }

        if data:
            data = json.dumps(data)

        encoded_params = urlrequest.urlencode(params)

        url = self._absolute_url(url, encoded_params)

        logger.info(u'DATA[IN -> %s]\n\t- headers: %s\n\t- content: %s' % (url, headers, data))

        ts = time.time()

        # signal:
        request_started.send(url=url, data=data, headers=headers, method=method)

        try:
            result = requests_session.request(method, url,
                                              data=data,
                                              headers=headers)
        except ConnectionError as e:
            raise APIError(e.message)

        laps = time.time() - ts

        # signal:
        request_finished.send(url=url,
                              data=data,
                              headers=headers,
                              method=method,
                              result=result,
                              laps=laps)

        logger.info(u'DATA[OUT -> %s][%2.3f seconds]\n\t- status_code: %s\n\t- headers: %s\n\t- content: %s' % (
            url,
            laps,
            result.status_code,
            result.headers,
            result.text if hasattr(result, 'text') else result.content)
        )

        if result.status_code not in (requests.codes.ok, requests.codes.not_found,
                                      requests.codes.created, requests.codes.accepted,
                                      requests.codes.no_content):
            self._create_apierror(result, url=url, data=data, method=method)
        elif result.status_code == requests.codes.no_content:
            return result, None
        else:
            if result.content:
                try:
                    return result, json.loads(result.content)
                except ValueError:
                    self._create_decodeerror(result, url=url)
            else:
                self._create_decodeerror(result, url=url)

    def _absolute_url(self, url, encoded_params):
        pattern = '%s%s%s'

        if encoded_params:
            pattern = '%s%s?%s'

        return pattern % (self.api_url, self._construct_api_url(url), encoded_params)

    def _construct_api_url(self, relative_url):
        return '%s%s' % (self.my_client_id, relative_url)

    def _create_apierror(self, result, url=None, data=None, method=None):
        text = result.text if hasattr(result, 'text') else result.content

        status_code = result.status_code

        headers = result.headers

        logger.error(u'API ERROR: status_code: %s | url: %s | method: %s | data: %r | headers: %s | content: %s' % (
            status_code,
            url,
            method,
            data,
            headers,
            text
        ))

        request_error.send(url=url, status_code=status_code, headers=headers)

        try:
            content = result.json()
        except ValueError:
            content = None

        raise APIError(text, code=status_code, content=content)

    def _create_decodeerror(self, result, url=None):

        text = result.text if hasattr(result, 'text') else result.content

        status_code = result.status_code

        headers = result.headers

        logger.error(u'DECODE ERROR: status_code: %s | headers: %s | content: %s' % (status_code,
                                                                                     headers,
                                                                                     text))

        request_error.send(url=url, status_code=status_code, headers=headers)

        try:
            content = result.json()
        except ValueError:
            content = None

        raise DecodeError(text,
                          code=status_code,
                          headers=headers,
                          content=content)
