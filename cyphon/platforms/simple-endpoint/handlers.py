# -*- coding: utf-8 -*-
# Copyright 2017-2019 ControlScan, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Defines classes for JIRA actions.
"""

# standard library
import urllib
import requests

# third party
from django.conf import settings

# local
from ambassador.transport import Cargo
from responder.carrier import Carrier

class RestAPI(Carrier):
    """
    Class for accessing the JIRA Isssue API.
    """

    def __init__(self, *args, **kwargs):
        super(RestAPI, self).__init__(*args, **kwargs)
        self.server = "https://ensmc3mf2g0q.x.pipedream.net"
        print("qui1")

    def process_request(self, obj):
        """Create a JIRA issue for an Alert.

        Parameters
        ----------
        obj : |Alert|
            The |Alert| used to create the JIRA Issue.

        Returns
        -------
        |Cargo|
            The results of the API call to JIRA.

        """
        print("hello world")
        print(obj)
        r = requests.post('http://ensmc3mf2g0q.x.pipedream.net', json={
            "level": obj.level,
            "level": obj.status,
            "title": obj.title
        })
        return Cargo(status_code=r.status_code, data={}, notes=None)

