##############################################################################
#
#    Copyright (C) 2021 Ganar Ganar (https://ganargan.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Mailgun",
    "summary": """Setup the outgoing and incoming mail flow easily by using Mailgun""",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "author": "Ganar Ganar",
    "support": "soporte@ganargan.ar",
    "category": "Discuss",
    "depends": [
        "mail"
    ],
    "data": [
        "data/ir_cron_data.xml"
    ],
    "website": "https://github.com/ganarganar/mailing",
    "installable": True
}
