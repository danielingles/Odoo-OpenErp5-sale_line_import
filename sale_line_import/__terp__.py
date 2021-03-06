# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Migrated from v6 to v5 by Daniel Inglés Andreu (danielingle@gmail.com)
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: julio (julio@vauxoo.com)
############################################################################
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

{
    "name": "Sale Line Import",
    "version": "1.1",
    "author" : "Vauxoo",
    "category": "Generic Modules/Product",
    "website" : "http://www.vauxoo.com/",
    "description": """Import a CSV file to lines of Sale Order
    """,
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'depends': ['sale'],
    'init_xml': [],
    'update_xml': ['security/wizard_import_line_security.xml',
        'wizard/sale_line_import_view.xml',
        ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
