#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        kilometro = self.request.get("edKilometro", 0);
        tiempo = self.request.get("edTiempo" ,0 );
        consumo = self.request.get("edConsumo", 0);

        if len(kilometro.strip()) == 0 or len(tiempo.strip()) == 0 or len(consumo.strip()) == 0 or (kilometro <= 0) or (tiempo <= 0) or (consumo <= 0) or not kilometro.isdigit() or not tiempo.isdigit() or not consumo.isdigit() :
            consumoTotal = -1
            velocidad = -1
        else :
            velocidad = int(int(kilometro) / int(tiempo))
            consumoTotal = int(int(kilometro) * int(consumo))

        self.response.write("La velocidad media es: " + str(velocidad))
        self.response.write("   El consumo total es: " + str(consumoTotal))

app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
