import unittest
import mock
import json
from similarweb.exceptions import InvalidResponseException
import similarweb


class TestTrafficAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"
        self.start_month = "5-2014"
        self.end_month = "6-2014"
        self.time_granularity = "MONTHLY"
        self.main_domain_only = False

        self.client = similarweb.TrafficAPI(self.api_key, self.domain, self.start_month,
                                            self.end_month, self.time_granularity, self.main_domain_only)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v1/visits?gr=MONTHLY&start=5-2014"
                    "&end=6-2014&md=false&Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Values": [{
                "Date": "2013-09-01",
                "Value": 356963532.0
            }, {
                "Date": "2013-09-02",
                "Value": 370288318.0
            }, {
                "Date": "2013-09-03",
                "Value": 384481631.0
            }]
        }

        expected = [{
            "Date": "2013-09-01",
            "Value": 356963532.0
        }, {
            "Date": "2013-09-02",
            "Value": 370288318.0
        }, {
            "Date": "2013-09-03",
            "Value": 384481631.0
        }]

        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestRankAndReachAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.RankAndReachAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v1/traffic?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "GlobalRank": 2,
            "CountryCode": 840,
            "CountryRank": 2,
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestEngagementAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.endpoint = "pageviews"
        self.domain = "similarweb.com"
        self.start_month = "5-2014"
        self.end_month = "6-2014"
        self.time_granularity = "MONTHLY"
        self.main_domain_only = False

        self.client = similarweb.EngagementAPI(self.api_key, self.endpoint, self.domain, self.start_month,
                                               self.end_month, self.time_granularity, self.main_domain_only)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v1/pageviews?gr=MONTHLY&start=5-2014"
                    "&end=6-2014&md=false&Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Values": [{
                "Date": "2013-09-01",
                "Value": 2.865204783102025
            },
                {
                "Date": "2013-09-02",
                "Value": 3.0618766793373418
            },
                {
                "Date": "2013-09-03",
                "Value": 2.8497896589996
            }]
        }

        expected = [{
            "Date": "2013-09-01",
            "Value": 2.865204783102025
        },
            {
            "Date": "2013-09-02",
                "Value": 3.0618766793373418
        },
            {
            "Date": "2013-09-03",
                "Value": 2.8497896589996
        }]

        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestSimilarWebsitesAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.SimilarWebsitesAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v2/similarsites?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "SimilarSites": [
                {
                    "Url": "amazon.com",
                    "Score": 0.9012942574949001
                },
                {
                    "Url": "ubid.com",
                    "Score": 0.7312487797958783
                },
                {
                    "Url": "overstock.com",
                    "Score": 0.6653412685291096
                }]
        }

        expected = [
            {
                "Url": "amazon.com",
                "Score": 0.9012942574949001
            },
            {
                "Url": "ubid.com",
                "Score": 0.7312487797958783
            },
            {
                "Url": "overstock.com",
                "Score": 0.6653412685291096
            }]

        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestAlsoVisitedAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.AlsoVisitedAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v2/alsovisited?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "AlsoVisited": [
                {
                    "Url": "youtube.com",
                    "Score": 0.0240163149806976
                }]
        }

        expected = [
            {
                "Url": "youtube.com",
                "Score": 0.0240163149806976
            }]

        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestWebsiteTagsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.WebsiteTagsAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v2/tags?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Tags": [
                {
                    "Name": "ebay",
                    "Score": 0.448100076050574
                },
                {
                    "Name": "shopping",
                    "Score": 0.40192654892152
                },
                {
                    "Name": "ebay auctions",
                    "Score": 0.394734724085174
                }]
        }

        expected = [
            {
                "Name": "ebay",
                "Score": 0.448100076050574
            },
            {
                "Name": "shopping",
                "Score": 0.40192654892152
            },
            {
                "Name": "ebay auctions",
                "Score": 0.394734724085174
            }]

        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestWebsiteCategorizationAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.WebsiteCategorizationAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v2/category?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Category": "Sports/Basketball"
        }

        expected = "Sports/Basketball"
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestCategoryRankAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.CategoryRankAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v2/CategoryRank?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Category": "Shopping",
            "CategoryRank": 1
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestTopSitesAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.category = "Shopping~Sports"
        self.country = "United States"

        self.client = similarweb.TopSitesAPI(self.api_key, self.category, self.country)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/v1/TopSites?Format=JSON"
                    "&country=United States&category=Shopping~Sports&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "1": "amazon.com",
            "2": "ebay.com",
            "3": "craigslist.org",
            "4": "walmart.com",
            "5": "bestbuy.com",
            "6": "aliexpress.com",
            "7": "target.com"
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestSocialReferralsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.SocialReferralsAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v1/socialreferringsites?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "SocialSources": [
                {
                    "Source": "Youtube",
                    "Value": 0.699753626365037
                }],
            "StartDate": "12/2012",
            "EndDate": "02/2013"
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestSearchKeywordsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.endpoint = "orgsearch"
        self.domain = "similarweb.com"
        self.start_month = "5-2014"
        self.end_month = "6-2014"
        self.main_domain_only = False
        self.results_page = 5

        self.client = similarweb.SearchKeywordsAPI(self.api_key, self.endpoint, self.domain, self.start_month,
                                                   self.end_month, self.main_domain_only, self.results_page)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v1/orgsearch?start=5-2014"
                    "&end=6-2014&md=false&page=5&Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Data": [
                {
                    "SearchTerm": "google",
                    "Visits": 0.35370287670560385,
                    "Change": -0.054669339162476696
                },
                {
                    "SearchTerm": "gmail",
                    "Visits": 0.08240189372826057,
                    "Change": -0.09094521264852375
                },
                {
                    "SearchTerm": "google.com",
                    "Visits": 0.04767900752285956,
                    "Change": -0.12005355937668932
                }],
            "ResultsCount": 10,
            "TotalCount": 53672,
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestDestinationsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"

        self.client = similarweb.DestinationsAPI(self.api_key, self.domain)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v2/leadingdestinationsites?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Sites": [
                "youtube.com",
                "facebook.com",
                "wikipedia.org",
                "yahoo.com",
                "googleusercontent.com",
                "pornhub.com",
                "amazon.com",
                "google.com.br",
                "imdb.com",
                "orkut.com"
            ],

            "StartDate": "12/2012",
            "EndDate": "02/2013"
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestReferralsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"
        self.start_month = "5-2014"
        self.end_month = "6-2014"
        self.main_domain_only = False
        self.results_page = 5

        self.client = similarweb.ReferralsAPI(self.api_key, self.domain, self.start_month,
                                              self.end_month, self.main_domain_only, self.results_page)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v1/referrals?start=5-2014"
                    "&end=6-2014&md=false&page=5&Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Data": [
                {
                    "Site": "accounts.google.com",
                    "Visits": 0.26538845554456164,
                    "Change": -0.020778539088788895
                },
                {
                    "Site": "mail.google.com",
                    "Visits": 0.0946150654521174,
                    "Change": 0.1226115991195885
                }
            ],
            "ResultsCount": 10,
            "TotalCount": 2583,
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestKeywordCompetitorsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.endpoint = "orgkwcompetitor"
        self.domain = "similarweb.com"
        self.start_month = "5-2014"
        self.end_month = "6-2014"
        self.main_domain_only = False
        self.results_page = 5

        self.client = similarweb.KeywordCompetitorsAPI(self.api_key, self.endpoint, self.domain, self.start_month,
                                                       self.end_month, self.main_domain_only, self.results_page)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Site/similarweb.com/v1/orgkwcompetitor?start=5-2014"
                    "&end=6-2014&md=false&page=5&Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Data": [
                {
                    "Domain": "accounts.youtube.com",
                    "Score": 0.01637974044476
                },
                {
                    "Domain": "akamaihd.net",
                    "Score": 0.012989426683271986
                },
                {
                    "Domain": "wikipedia.org",
                    "Score": 0.01032435596395393
                }
            ],
            "ResultsCount": 10,
            "TotalCount": 4241,
        }
        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestAppDetailsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.app_id = "com.yahoo.mobile.client.android.mail"
        self.app_store_id = 0

        self.client = similarweb.AppDetailsAPI(self.api_key, self.app_id, self.app_store_id)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Mobile/0/com.yahoo.mobile.client.android.mail"
                    "/v1/GetAppDetails?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "Title": "Yahoo Mail - Free Email App",
            "Cover": "https://lh6.ggpht.com/yzhSae3SIKlwv9lBzpCWaexNKgpLHXvwnxyEE7_oW3SdMv604v-YtUcQnGCyAUpX1lcm=w300",
            "Author": "Yahoo",
            "Price": "Free",
            "MainCategory": "Communication",
            "MainCategoryId": "communication",
            "Rating": 4.1736602783203125
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestGoogleAppInstallsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.app_id = "com.yahoo.mobile.client.android.mail"

        self.client = similarweb.GoogleAppInstallsAPI(self.api_key, self.app_id)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Mobile/0/com.yahoo.mobile.client.android.mail"
                    "/v1/GetAppInstalls?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "InstallsMin": 500000,
            "InstallsMax": 1000000
        }

        expected = json_payload
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)


class TestRelatedSiteAppsAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "a"
        self.domain = "similarweb.com"
        self.app_store_id = 0

        self.client = similarweb.RelatedSiteAppsAPI(self.api_key, self.domain, self.app_store_id)

    def test_url(self):
        result = self.client.url
        expected = ("http://api.similarweb.com/Mobile/0/similarweb.com"
                    "/v1/GetRelatedSiteApps?Format=JSON&UserKey=a")

        self.assertEquals(result, expected)

    @mock.patch("similarweb.base.requests.get")
    def test_query(self, mock_requests_get):
        # assert error response
        json_payload = {"Error": "Message"}
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        self.assertRaises(InvalidResponseException, self.client.query)

        # assert successful response
        json_payload = {
            "RelatedApps": [
                {
                    "AppId": "com.google.android.youtube",
                    "Title": "YouTube"
                },
                {
                    "AppId": "com.google.android.apps.maps",
                    "Title": "Maps"
                },
                {
                    "AppId": "com.google.android.gms",
                    "Title": "Google Play services"
                }]
        }

        expected = [
            {
                "AppId": "com.google.android.youtube",
                "Title": "YouTube"
            },
            {
                "AppId": "com.google.android.apps.maps",
                "Title": "Maps"
            },
            {
                "AppId": "com.google.android.gms",
                "Title": "Google Play services"
            }]
        response = type('response', (object,), {'text': json.dumps(json_payload)})
        mock_requests_get.return_value = response
        results = self.client.query()
        self.assertEquals(results, expected)
