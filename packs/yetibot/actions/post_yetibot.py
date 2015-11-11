# -*- coding: utf-8 -*-

import json
import httplib
import requests
import six
from six.moves.urllib.parse import urljoin

from st2actions.runners.pythonrunner import Action

__all__ = [
    'PostYetibot'
]

class PostYetibot(Action):
  def run(self, endpoint, chat_source, result, message):

    if not endpoint:
        raise ValueError('Missing "endpoint" config option')

    url = urljoin(endpoint, "/api")

    res = json.loads(result)
    self.logger.info(json.dumps(res))

    self.logger.info("post_yetibot")

    text = 'echo ' + message + '\n' + json.dumps(res)

    # if result["failed"]:
    #   command  += "\n" + result["stderr"]

    headers = {}
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    data = {"chat-source": chat_source, "text": text}
    response = requests.post(url=url, headers=headers, data=data)

    if response.status_code == httplib.OK:
      self.logger.info('Message successfully posted')
    else:
      self.logger.exception('Failed to post message: %s' % (response.text))
    return True
