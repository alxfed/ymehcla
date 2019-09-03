"""
Hello world in sqlalchemy
"""

from sqlalchemy import *
from datetime import datetime

ABS_PATH = '/media/alxfed/toca/dbase/secondbase.sqlite' # the absolute path to a database
ymehcla_path = f'sqlite:///{ABS_PATH}'  # notice the _three_ slashes before the absolute path!
                                        # ':memory:' is an option too.

column_names = ['about_us', 'category', 'facebookfans', 'first_conversion_date',
                'first_conversion_event_name', 'first_deal_created_date',
                'founded_year', 'hs_analytics_first_timestamp',
                'hs_analytics_first_touch_converting_campaign',
                'hs_analytics_first_visit_timestamp', 'hs_analytics_last_timestamp',
                'hs_analytics_last_touch_converting_campaign',
                'hs_analytics_last_visit_timestamp', 'hs_analytics_num_page_views',
                'hs_analytics_num_visits', 'hs_analytics_source',
                'hs_analytics_source_data_1', 'hs_analytics_source_data_2',
                'hs_avatar_filemanager_key', 'hs_lastmodifieddate', 'hs_object_id',
                'hs_target_account', 'hubspot_owner_assigneddate', 'is_public',
                'num_associated_contacts', 'num_associated_deals',
                'num_conversion_events', 'phone_contact', 'phone_landline',
                'phone_mobile', 'phone_toll', 'phone_unidentified', 'phone_voip',
                'recent_conversion_date', 'recent_conversion_event_name',
                'recent_deal_amount', 'recent_deal_close_date', 'timezone',
                'total_money_raised', 'total_revenue', 'name', 'twitterhandle',
                'email_address', 'phone', 'twitterbio', 'twitterfollowers',
                'address', 'address2', 'facebook_company_page', 'city',
                'linkedin_company_page', 'linkedinbio', 'state', 'googleplus_page',
                'engagements_last_meeting_booked',
                'engagements_last_meeting_booked_campaign',
                'engagements_last_meeting_booked_medium',
                'engagements_last_meeting_booked_source',
                'hs_sales_email_last_replied', 'hubspot_owner_id',
                'notes_last_contacted', 'notes_last_updated',
                'notes_next_activity_date', 'num_contacted_notes',
                'num_notes', 'zip', 'country', 'hubspot_team_id',
                'hs_all_owner_ids', 'website', 'domain', 'hs_all_team_ids',
                'hs_all_accessible_team_ids', 'numberofemployees', 'industry',
                'annualrevenue', 'lifecyclestage', 'hs_lead_status',
                'hs_parent_company_id', 'type', 'description', 'hs_num_child_companies',
                'hubspotscore', 'createdate', 'closedate', 'first_contact_createdate',
                'days_to_close', 'web_technologies']

metadata = MetaData(ymehcla_path)