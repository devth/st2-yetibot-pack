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
  def run(self, endpoint, trigger):

    if not endpoint:
        raise ValueError('Missing "endpoint" config option')

    url = urljoin(endpoint, "/api")
    chat_source = trigger.data.source_channel

    result = json.loads(trigger.data.result.replace("|", "."))

    self.logger.info("post_yetibot")
    self.logger.info(json.dumps(result))

    command = 'echo ' + trigger.message + '\n' + result["stdout"]
    if result["failed"]:
      command  += "\n" + result["stderr"]

    headers = {}
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    data = {"chat-source": chat_source, "command": command}
    response = requests.post(url=url, headers=headers, data=data)

    if response.status_code == httplib.OK:
      self.logger.info('Message successfully posted')
    else:
      self.logger.exception('Failed to post message: %s' % (response.text))
    return True
