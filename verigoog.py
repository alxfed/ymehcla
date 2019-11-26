# -*- coding: utf-8 -*-
import googlemaps
import os
import time
from collections import OrderedDict
from scrapy.spiders import CSVFeedSpider


def text_menu(name, items):  # items must have a key 'name'
    def print_menu(items):
        print(name+'\n______')
        for i, item in enumerate(items):
            print('{}. - {}'.format(i, item['name']))
        print('999, - reject all...\n\n')

    loop = True
    while loop:
        print_menu(items)
        length = len(items)
        thing = input("Choose one: ")
        if thing == 999:
            return None
        elif thing <= length:
            return items[int(thing)]
        else:
            pass


class VerigoogSpider(CSVFeedSpider):

    name = 'verigoog'
    allowed_domains = ['google.com']
    start_urls = ['https://chicago-bucket.s3.us-east-2.amazonaws.com/crm/crm-exports-all-companies-2019-08-16.csv']
    headers = ['Company ID', 'Lead Status', 'Postal Code', 'Company Domain Name',
               'Phone Unidentified', 'Close Date', 'Associated Deals', 'City',
               'Name', 'Phone Toll', 'Phone Number', 'Phone Landline', 'About Us',
               'State/Region', 'Phone VoIP', 'Email address', 'Phone Mobile',
               'Lifecycle Stage', 'Street Address', 'Country',
               'Type', 'Website URL', 'Street Address Two']

    # Do adaptations here
    def adapt_response(self, response):
        # token = self.settings['GOOG_API_TOKEN']
        token = os.environ['GOOG_API_TOKEN']
        try:
            maps_client = googlemaps.Client(key=token, timeout=10,
                                            retry_timeout=2,
                                            queries_per_second=1,
                                            retry_over_query_limit=True)
        except ValueError:
            print('The API token does not work')
            exit(code=246)

        response.meta['maps_cli'] = maps_client
        return response

    def parse_row(self, response, row):
        location = {'lat': 41.8781136, 'lng': -87.6297982}
        maps_client = response.meta['maps_cli']

        header_start = self.headers[0]
        if row[header_start].startswith(header_start):
            yield None
        else:
            bias = 'circle:50000@' + str(location['lat']) + ',' + str(location['lng'])
            name = row['Name']
            text_of_request = name + ', ' + row['Street Address']
            result = maps_client.find_place(input=text_of_request,
                                            input_type="textquery",
                                            fields=['place_id'],
                                            location_bias=bias)
            if result['status'].startswith('ZERO_RESULTS'):
                yield row
            else:
                candidates = result['candidates']
                candidates_list = []

                # address = info['formatted_address']
                # name = info['name']
                for ind, candidate in enumerate(candidates):
                    place_id = candidate['place_id']
                    inf = maps_client.place(place_id=place_id,
                                                     fields=['name',
                                                             'formatted_address',
                                                             'formatted_phone_number',
                                                             'website'])['result']
                    candidates_list.append(inf)
                item = text_menu(name, candidates_list)
            yield item
