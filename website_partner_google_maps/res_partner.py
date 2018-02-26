# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2018 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def get_map(self, zoom=12, center=None, partners=None, icon=''):
        if len(partners) > 0:
            map_tmp = """function initMap() {
                    var center = {lat: %s, lng: %s};
                    var map = new google.maps.Map(document.getElementById('map'), {
                      zoom: %s,
                      center: center
                    });
                    %s
                  }"""
            marker_tmp = """
                    var marker%s = new google.maps.Marker({
                        title: '%s',
                        position: {lat: %s, lng: %s},
                        map: map,
                        icon: '%s'
                    });
                  """
            center = center.get_position() if center else partners[0].get_position()
            markers = ''
            for partner in partners:
                pos = partner.get_position()
                markers += marker_tmp %(partner.id, partner.name, pos['lat'], pos['lng'], icon)
            return map_tmp %(center['lat'], center['lng'], zoom, markers)
        return ''
