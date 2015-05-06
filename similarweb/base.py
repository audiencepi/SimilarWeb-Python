import requests
import json
from abc import ABCMeta, abstractmethod
from similarweb.exceptions import InvalidResponseException, InvalidEndpointException
from similarweb import utils


class SimilarWeb(object):
    __metaclass__ = ABCMeta

    def __init__(self, api_key):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key
        """
        self.api_key = api_key

    @property
    def _base_url(self):
        return "http://api.similarweb.com"

    @abstractmethod
    def params(self):
        return

    @abstractmethod
    def url(self):
        return

    @abstractmethod
    def query(self):
        return


class TrafficAPI(SimilarWeb):

    def __init__(self, api_key, domain, start_month, end_month,
                 time_granularity="MONTHLY", main_domain_only=False):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.

        start_month: string
            Start Month in (M-YYYY) format

        end_month: string
            End Month in (M-YYYY) format

        time_granularity: string
            Time granularity of report. Can be: Daily, Weekly, Monthly

        main_domain_only: boolean
            Get metrics on the Main Domain only (i.e. not including subdomains)
        """

        self.domain = utils.domain_from_url(domain)
        self.start_month = start_month
        self.end_month = end_month
        self.time_granularity = time_granularity
        self.main_domain_only = main_domain_only
        super(TrafficAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["start_month"] = self.start_month
        params["end_month"] = self.end_month
        params["time_granularity"] = self.time_granularity
        params["main_domain_only"] = str(self.main_domain_only).lower()
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/visits?gr={time_granularity}&start={start_month}"
                   "&end={end_month}&md={main_domain_only}&Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Values' not in results:
            raise InvalidResponseException(results)

        return results['Values']


class RankAndReachAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(RankAndReachAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/traffic?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'GlobalRank' not in results:
            raise InvalidResponseException(results)

        return results


class EngagementAPI(SimilarWeb):

    def __init__(self, api_key, endpoint, domain, start_month, end_month,
                 time_granularity="MONTHLY", main_domain_only=False):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        endpoint: string
            Endpoint to use. Can be: pageviews, visitduration, bouncerate

        domain: string
            Domain to query.

        start_month: string
            Start Month in (M-YYYY) format

        end_month: string
            End Month in (M-YYYY) format

        time_granularity: string
            Time granularity of report. Can be: Daily, Weekly, Monthly

        main_domain_only: boolean
            Get metrics on the Main Domain only (i.e. not including subdomains)
        """

        if endpoint not in ["pageviews", "visitduration", "bouncerate"]:
            raise InvalidEndpointException("Endpoint must be one of the following values: "
                                           "pageviews, visitduration, bouncerate")

        self.endpoint = endpoint
        self.domain = utils.domain_from_url(domain)
        self.start_month = start_month
        self.end_month = end_month
        self.time_granularity = time_granularity
        self.main_domain_only = main_domain_only
        super(EngagementAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["endpoint"] = self.endpoint
        params["domain"] = self.domain
        params["start_month"] = self.start_month
        params["end_month"] = self.end_month
        params["time_granularity"] = self.time_granularity
        params["main_domain_only"] = str(self.main_domain_only).lower()
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/{endpoint}?gr={time_granularity}&start={start_month}"
                   "&end={end_month}&md={main_domain_only}&Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Values' not in results:
            raise InvalidResponseException(results)

        return results['Values']


class SimilarWebsitesAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(SimilarWebsitesAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v2/similarsites?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'SimilarSites' not in results:
            raise InvalidResponseException(results)

        return results['SimilarSites']


class AlsoVisitedAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(AlsoVisitedAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v2/alsovisited?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'AlsoVisited' not in results:
            raise InvalidResponseException(results)

        return results['AlsoVisited']


class WebsiteTagsAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(WebsiteTagsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v2/tags?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Tags' not in results:
            raise InvalidResponseException(results)

        return results['Tags']


class WebsiteCategorizationAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(WebsiteCategorizationAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v2/category?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Category' not in results:
            raise InvalidResponseException(results)

        return results['Category']


class CategoryRankAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(CategoryRankAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v2/CategoryRank?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Category' not in results:
            raise InvalidResponseException(results)

        return results


class TopSitesAPI(SimilarWeb):

    def __init__(self, api_key, category=None, country=None):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        category: string
            If left blank, `All Categories` will be requested.
            Use `http://api.similarweb.com/v1/TopSites/categories` to get a list of available categories.

        country: string
            If left blank, `Worldwide` will be requested.
            Use `http://api.similarweb.com/v1/TopSites/countries` to get a list of available categories.
        """

        self.category = category
        self.country = country
        super(TopSitesAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["category"] = self.category if self.category else ""
        params["country"] = self.country if self.country else ""
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/v1/TopSites?Format=JSON&country={country}&category={category}"
                   "&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if '1' not in results:
            raise InvalidResponseException(results)

        return results


class SocialReferralsAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(SocialReferralsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/socialreferringsites?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'SocialSources' not in results:
            raise InvalidResponseException(results)

        return results


class SearchKeywordsAPI(SimilarWeb):

    def __init__(self, api_key, endpoint, domain, start_month, end_month,
                 main_domain_only=False, results_page=None):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        endpoint: string
            Endpoint to use. Can be: orgsearch, paidsearch

        domain: string
            Domain to query.

        start_month: string
            Start Month in (M-YYYY) format

        end_month: string
            End Month in (M-YYYY) format

        main_domain_only: boolean
            Get metrics on the Main Domain only (i.e. not including subdomains)

        results_page: integer
            Enter for more than 10 results
        """

        if endpoint not in ["orgsearch", "paidsearch", ]:
            raise InvalidEndpointException("Endpoint must be one of the following values: "
                                           "orgsearch, paidsearch")

        self.domain = utils.domain_from_url(domain)
        self.endpoint = endpoint
        self.start_month = start_month
        self.end_month = end_month
        self.main_domain_only = main_domain_only
        self.results_page = results_page
        super(SearchKeywordsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["endpoint"] = self.endpoint
        params["domain"] = self.domain
        params["start_month"] = self.start_month
        params["end_month"] = self.end_month
        params["main_domain_only"] = str(self.main_domain_only).lower()
        params["results_page"] = self.results_page if self.results_page else ""
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/{endpoint}?start={start_month}&end={end_month}"
                   "&md={main_domain_only}&page={results_page}&Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Data' not in results:
            raise InvalidResponseException(results)

        return results


class DestinationsAPI(SimilarWeb):

    def __init__(self, api_key, domain):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.
        """

        self.domain = utils.domain_from_url(domain)
        super(DestinationsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v2/leadingdestinationsites?Format=JSON&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Sites' not in results:
            raise InvalidResponseException(results)

        return results


class ReferralsAPI(SimilarWeb):

    def __init__(self, api_key, domain, start_month, end_month,
                 main_domain_only=False, results_page=None):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.

        start_month: string
            Start Month in (M-YYYY) format

        end_month: string
            End Month in (M-YYYY) format

        main_domain_only: boolean
            Get metrics on the Main Domain only (i.e. not including subdomains)

        results_page: integer
            Enter for more than 10 results
        """

        self.domain = utils.domain_from_url(domain)
        self.start_month = start_month
        self.end_month = end_month
        self.main_domain_only = main_domain_only
        self.results_page = results_page
        super(ReferralsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["start_month"] = self.start_month
        params["end_month"] = self.end_month
        params["main_domain_only"] = str(self.main_domain_only).lower()
        params["results_page"] = self.results_page if self.results_page else ""
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/referrals?start={start_month}"
                   "&end={end_month}&md={main_domain_only}&page={results_page}&Format=JSON"
                   "&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Data' not in results:
            raise InvalidResponseException(results)

        return results


class KeywordCompetitorsAPI(SimilarWeb):

    def __init__(self, api_key, endpoint, domain, start_month, end_month,
                 main_domain_only=False, results_page=None):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        endpoint: string
            Endpoint to use. Can be: orgkwcompetitor, paidkwcompetitor

        domain: string
            Domain to query.

        start_month: string
            Start Month in (M-YYYY) format

        end_month: string
            End Month in (M-YYYY) format

        main_domain_only: boolean
            Get metrics on the Main Domain only (i.e. not including subdomains)

        results_page: integer
            Enter for more than 10 results
        """

        if endpoint not in ["orgkwcompetitor", "paidkwcompetitor", ]:
            raise InvalidEndpointException("Endpoint must be one of the following values: "
                                           "orgkwcompetitor, paidkwcompetitor")

        self.domain = utils.domain_from_url(domain)
        self.endpoint = endpoint
        self.start_month = start_month
        self.end_month = end_month
        self.main_domain_only = main_domain_only
        self.results_page = results_page
        super(KeywordCompetitorsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["endpoint"] = self.endpoint
        params["start_month"] = self.start_month
        params["end_month"] = self.end_month
        params["main_domain_only"] = str(self.main_domain_only).lower()
        params["results_page"] = self.results_page if self.results_page else ""
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Site/{domain}/v1/{endpoint}?start={start_month}"
                   "&end={end_month}&md={main_domain_only}&page={results_page}&Format=JSON"
                   "&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Data' not in results:
            raise InvalidResponseException(results)

        return results


class AppDetailsAPI(SimilarWeb):

    def __init__(self, api_key, app_id, app_store_id):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        app_id: string
            Enter the ID of the app (e.g. "com.yahoo.mobile.client.android.mail")

        app_store_id: integer
            0 for Google Play Store, 1 for iOS AppStore
        """

        self.app_id = app_id
        self.app_store_id = app_store_id
        super(AppDetailsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["app_id"] = self.app_id
        params["app_store_id"] = self.app_store_id
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Mobile/{app_store_id}/{app_id}/v1/GetAppDetails?Format=JSON"
                   "&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'Title' not in results:
            raise InvalidResponseException(results)

        return results


class GoogleAppInstallsAPI(SimilarWeb):

    def __init__(self, api_key, app_id):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        app_id: string
            Enter the ID of the app (e.g. "com.yahoo.mobile.client.android.mail")
        """

        self.app_id = app_id
        super(GoogleAppInstallsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["app_id"] = self.app_id
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Mobile/0/{app_id}/v1/GetAppInstalls?Format=JSON"
                   "&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'InstallsMin' not in results:
            raise InvalidResponseException(results)

        return results


class RelatedSiteAppsAPI(SimilarWeb):

    def __init__(self, api_key, domain, app_store_id):
        """
        Parameters
        ----------
        api_key: string
            SimilarWeb API key

        domain: string
            Domain to query.

        app_store_id: integer
            0 for Google Play Store, 1 for iOS AppStore
        """

        self.domain = utils.domain_from_url(domain)
        self.app_store_id = app_store_id
        super(RelatedSiteAppsAPI, self).__init__(api_key)

    @property
    def params(self):
        params = {}
        params["domain"] = self.domain
        params["app_store_id"] = self.app_store_id
        params["api_key"] = self.api_key
        return params

    @property
    def url(self):
        end_url = ("/Mobile/{app_store_id}/{domain}/v1/GetRelatedSiteApps?Format=JSON"
                   "&UserKey={api_key}".format(**self.params))
        return self._base_url + end_url

    def query(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        if 'RelatedApps' not in results:
            raise InvalidResponseException(results)

        return results['RelatedApps']
