# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2019 Vertel AB (<http://vertel.se>).
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

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    state = fields.Selection(selection_add=[('cancelled', 'Cancelled')])
    # TODO: Make this a relation to another model instead?
    cancel_reason = fields.Selection(selection=[('1', '1'),
                                        ('2', '2'),
                                        ('3', '3'),
                                        ('4', '4')],
                                        string='Cancel reason', 
                                        default='1', 
                                        help="Reason for cancelling the meeting")
    # meeting_status = fields.Selection(selection=[('request', 'Requested by applicant'),
    #                                     ('planned', 'Planned by administrator'),
    #                                     ('finished', 'Meeting finished according to plan'),
    #                                     ('canceled', 'Cancelled by administrator'),
    #                                     ('failed', 'Applicant failed to attend to the meeting')],
    #                                     string='Meeting status', 
    #                                     default='request', 
    #                                     help="Reasons for having or cancelling the meeting")
