# SimilarWeb-Python
[![Build Status](https://travis-ci.org/audiencepi/SimilarWeb-Python.svg?branch=master)](https://travis-ci.org/audiencepi/SimilarWeb-Python)
Python wrapper for [SimilarWeb API](https://developer.similarweb.com/estimated_visits_api) .

## Supported API
- [Traffic API](https://developer.similarweb.com/estimated_visits_api)
- [Rank and Reach API](https://developer.similarweb.com/rank_reach)
- [Engagement API](https://developer.similarweb.com/websites_traffic_and_engagement_pro_api)
- [Similar Websites API](https://developer.similarweb.com/similar_websites_api)
- [Also Visited API](https://developer.similarweb.com/also_visited_api)
- [Website Tags API](https://developer.similarweb.com/website_tags_api)
- [Website Categorization API](https://developer.similarweb.com/website_categorization_API)
- [Category Rank API](https://developer.similarweb.com/category_rank_api)
- [Top Sites API](https://developer.similarweb.com/top_sites)
- [Social Referrals API](https://developer.similarweb.com/social_referrals_api)
- [Search Keywords API](https://developer.similarweb.com/keywords_api)
- [Destinations API](https://developer.similarweb.com/destinations_api)
- [Referrals API](https://developer.similarweb.com/referring_websites_pro_api)
- [Keyword Competitors API](https://developer.similarweb.com/organic_paid_search_comptetitors_pro_api)
- [APP Details API](https://developer.similarweb.com/mobile_api_app_details)
- [Google Play Installs API](https://developer.similarweb.com/mobile_api_app_installs)
- [Related Site Apps API](https://developer.similarweb.com/mobile_api_related_apps)


## Installation

    pip install SimilarWeb-Python

## Examples
```python
import similarweb

# Parameters
api_key = YOUR_API_KEY
domain = "similarweb.com"
start_month = "1-2015" # in format M-YYYY
end_month = "2-2015" # in format M-YYYY
time_granularity = "MONTHLY" # Can be: Daily, Weekly, Monthly
main_domain_only = False # get metrics on the main domain only?

#================================
# TrafficAPI
#================================
client = similarweb.TrafficAPI(api_key, domain, start_month,
                               end_month, time_granularity,
                               main_domain_only)
results = client.query()

# RankAndReachAPI
client = similarweb.RankAndReachAPI(api_key, domain)
results = client.query()

#================================
# EngagementAPI
#================================
endpoint = "pageviews" # Can be: pageviews, visitduration, bouncerate
client = similarweb.EngagementAPI(api_key, endpoint, domain,
                                  start_month, end_month,
                                  time_granularity, main_domain_only)
results = client.query()

#================================
# SimilarWebsitesAPI
#================================
client = similarweb.SimilarWebsitesAPI(api_key, domain)
results = client.query()

#================================
# AlsoVisitedAPI
#================================
client = similarweb.AlsoVisitedAPI(api_key, domain)
results = client.query()

#================================
# WebsiteTagsAPI
#================================
client = similarweb.WebsiteTagsAPI(api_key, domain)
results = client.query()

#================================
# WebsiteCategorizationAPI
#================================
client = similarweb.WebsiteCategorizationAPI(api_key, domain)
results = client.query()

#================================
# CategoryRankAPI
#================================
client = similarweb.CategoryRankAPI(api_key, domain)
results = client.query()

#================================
# TopSitesAPI
#================================
# If left blank, `All Categories` will be requested.
# Use `http://api.similarweb.com/v1/TopSites/categories`
# to get a list of available categories.
category = "Shopping~Sports"

# If left blank, `Worldwide` will be requested.
# Use `http://api.similarweb.com/v1/TopSites/countries`
# to get a list of available categories.
category = "United States"
client = similarweb.TopSitesAPI(api_key, domain)
results = client.query()

# SocialReferralsAPI
client = similarweb.SocialReferralsAPI(api_key, domain)
results = client.query()

#================================
# SearchKeywordsAPI
#================================
endpoint = "orgsearch" # Can be: orgsearch, paidsearch
results_page = 2 # Enter for more than 10 results
client = similarweb.SearchKeywordsAPI(api_key, endpoint, domain,
                                      start_month, end_month,
                                      main_domain_only, results_page)
results = client.query()

#================================
# DestinationsAPI
#================================
client = similarweb.DestinationsAPI(api_key, domain)
results = client.query()

#================================
# ReferralsAPI
#================================
results_page = 2 # Enter for more than 10 results
client = similarweb.ReferralsAPI(api_key, domain, start_month,
                                 end_month, main_domain_only,
                                 results_page)
results = client.query()

#================================
# KeywordCompetitorsAPI
#================================
endpoint = "orgkwcompetitor" # Can be: orgkwcompetitor, paidkwcompetitor
results_page = 2 # Enter for more than 10 results
client = similarweb.KeywordCompetitorsAPI(api_key, endpoint,
                                          domain, start_month,
                                          end_month, main_domain_only, results_page)
results = client.query()

#================================
# AppDetailsAPI
#================================
app_id = "com.yahoo.mobile.client.android.mail" # ID of the app
app_store_id = 0 # 0 for Google Play Store, 1 for iOS AppStore
client = similarweb.AppDetailsAPI(api_key, app_id, app_store_id)
results = client.query()

#================================
# GoogleAppInstallsAPI
#================================
client = similarweb.GoogleAppInstallsAPI(api_key, app_id)
results = client.query()

#================================
# RelatedSiteAppsAPI
#================================
client = similarweb.RelatedSiteAppsAPI(api_key, domain, app_store_id)
results = client.query()
```

