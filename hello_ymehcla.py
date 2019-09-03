"""
Hello world in sqlalchemy
"""

from sqlalchemy import *
from datetime import datetime

ABS_PATH = '/media/alxfed/toca/dbase/secondbase.sqlite' # the absolute path to a database
ymehcla_path = f'sqlite:///{ABS_PATH}'  # notice the _three_ slashes before the absolute path!
                                        # ':memory:' is an option too.

column_names = ['companyId', 'name', 'category', 'type', 'description',
                'address', 'address2', 'city', 'state', 'zip', 'country',
                'timezone',
                'phone', 'phone_contact', 'phone_mobile', 'phone_voip',
                'phone_toll','phone_landline', 'phone_unidentified',
                'website', 'domain', 'email_address',
                'industry', 'about_us', 'founded_year', 'numberofemployees',
                'is_public', 'annualrevenue', 'lifecyclestage',
                'notes_last_contacted', 'notes_last_updated',
                'total_money_raised', 'total_revenue', 'twitterhandle',
                'twitterbio', 'twitterfollowers',
                'facebook_company_page', 'facebookfans',
                'linkedin_company_page', 'linkedinbio', 'googleplus_page',
                'recent_conversion_date', 'recent_conversion_event_name',
                'recent_deal_amount', 'recent_deal_close_date',
                'hs_num_child_companies',
                'createdate', 'closedate',
                'first_contact_createdate', 'first_conversion_date',
                'first_conversion_event_name', 'first_deal_created_date',
                'days_to_close',
                'hubspot_team_id', 'hs_parent_company_id',
                'hs_all_owner_ids', 'hs_all_team_ids',
                'hs_all_accessible_team_ids', 'hs_lead_status',
                'hs_analytics_first_timestamp', 'hs_lastmodifieddate', 'hs_object_id',
                'hs_target_account', 'hubspot_owner_assigneddate',
                'hs_analytics_first_touch_converting_campaign',
                'hs_analytics_first_visit_timestamp', 'hs_analytics_last_timestamp',
                'hs_analytics_last_touch_converting_campaign',
                'hs_analytics_last_visit_timestamp', 'hs_analytics_num_page_views',
                'hs_analytics_num_visits', 'hs_analytics_source',
                'hs_analytics_source_data_1', 'hs_analytics_source_data_2',
                'num_associated_contacts', 'num_associated_deals',
                'num_conversion_events',
                'engagements_last_meeting_booked',
                'engagements_last_meeting_booked_campaign',
                'engagements_last_meeting_booked_medium',
                'engagements_last_meeting_booked_source',
                'hs_sales_email_last_replied', 'hubspot_owner_id',
                'notes_next_activity_date', 'num_contacted_notes',
                'num_notes', 'hubspotscore',
                'hs_avatar_filemanager_key', 'web_technologies']

metadata = MetaData(ymehcla_path)

companies = Table('companies', metadata,
                  Column('companyId', Integer, primary_key=True),
                  Column('name', Unicode(50), default=''),
                  Column('category', Unicode(50), default=''),
                  Column('type', Unicode(50), default=''),
                  Column('description', Unicode(255), default=''),
                  Column('address', Unicode(80), default=''),
                  Column('address2', Unicode(80), default=''),
                  Column('city', Unicode(50), default=''),
                  Column('state', Unicode(50), default=''),
                  Column('zip', Unicode(50), default=''),
                  Column('country', Unicode(50), default=''),
                  Column('timezone', Unicode(50), default=''),
                  Column('phone', Unicode(50), default=''),
                  Column('phone_contact', Unicode(50), default=''),
                  Column('phone_mobile', Unicode(50), default=''),
                  Column('phone_voip', Unicode(50), default=''),
                  Column('phone_toll', Unicode(50), default=''),
                  Column('phone_landline', Unicode(50), default=''),
                  Column('phone_unidentified', Unicode(50), default=''),
                  Column('website', Unicode(50), default=''),
                  Column('domain', Unicode(50), default=''),
                  Column('email_address', Unicode(50), default=''))