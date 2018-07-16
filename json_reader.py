#!/usr/bin/env python2

# json_reader.py
# json_reader, by Chuan Tan <ct538@cam.ac.uk>
#
# Copyright (C) Chuan Tan 2018
#
# This programme is free software; you may redistribute and/or modify
# it under the terms of the Apache Licence, version 2.0.

# Usage: json_reader.py

# Reads from json files and adds stuff into database.

import psycopg2
import json
import pycountry
import uuid

def fix_amiacountry(country):
    if country == "palestine":
        return "PS"
    if country == "kosovo":
        return "XK"
    if country == "macedonia":
        return "MK"
    if country == "laos":
        return "LA"



def add_uuid_and_country_code(data):
    for JSONObject in data:
        institution_name = JSONObject["Institution"]
        JSONObject["Institution-uuid"] = str(uuid.uuid3(uuid.NAMESPACE_DNS,institution_name.encode("utf-8")))
        
        country = JSONObject["Country"].lower()
        # Fix for palestine, kosovo, macedonia and laos - both partially recognised states
        if country in ["palestine","kosovo","macedonia","laos"]:
            JSONObject["Country-code"] = fix_amiacountry(country)
        else:
            JSONObject["Country-code"] = pycountry.countries.lookup(country).alpha_2

    return data
        


conn = psycopg2.connect(database='obp_institutions',
                        user = 'obp',
                        password = 'some_secret_password',
                        host = '192.168.99.100',
                        port = '5432')
cursor = conn.cursor()

with open("data.json") as f:
    print "Loading JSON file."
    data = json.load(f)
    data = add_uuid_and_country_code(data)






