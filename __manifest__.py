#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Point Customization of ticket",
    "version": "12.0.1.1.0",
    "category": "TPV, POS",
    "author": "Kewitz Colina",
    "website": "https://github.com/colinak",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        'base',
        'point_of_sale'
    ],
    "data": [
        # 'views/product_pricelist_item_view.xml'
        'templates/assets.xml'
    ],
    "demo": [],
    'qweb': [
        'static/src/xml/pos.xml'
    ]
}


