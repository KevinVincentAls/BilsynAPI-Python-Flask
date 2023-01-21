#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('./logs/debug.log'),
                    logging.StreamHandler(sys.stdout)])


def nummerplade(query):
    #token = os.environ['token']
    token = 'sb_sk_91ec442399a0439eb5708e61c8c28c0e'
    headers = \
        {'Authorization': 'Bearer ' + token}
    r = \
        requests.get('https://api.synsbasen.dk/v1/vehicles/registration/'
                      + query, headers=headers)
    data = r.text
    parse_json = json.loads(data)

    # print(parse_json.keys())
    # print(parse_json["model"])

    type = parse_json['data']['kind']
    status = parse_json['data']['status']
    reg = parse_json['data']['registration']
    make = parse_json['data']['brand']
    model = parse_json['data']['model']
    variant = parse_json['data']['variant']
    årgang = parse_json['data']['model_year']
    leasing = parse_json['data']['leasing_period_start']
    syn = parse_json['data']['inspections'][0]['result']
    stel = parse_json['data']['inspections'][0]['vin']
    mileage = parse_json['data']['mileage']
    estimated_mileage = parse_json['data']['mileage_annual_average']
    inspection_date = parse_json['data']['last_inspection_date']
    reg_date = parse_json['data']['first_registration_date']
    pdf = parse_json['data']['inspections'][0]['pdf']

    return (
        type,
        status,
        reg,
        make,
        model,
        variant,
        årgang,
        leasing,
        syn,
        stel,
        mileage,
        estimated_mileage,
        inspection_date,
        reg_date,
        pdf,
        )


    # print(parse_json)
