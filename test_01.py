from testcases.base_tests import BaseTest
from parameterized import parameterized


class TextSearch(BaseTest):
    def setUp(self):
        super().setUp()
        self.base_selenium.get_url(url=self.url)

    def test006_feature(self, word):

        self.search_page.inurl_search(text=word)
        for result in self.results_page.get_results_urls():
            self.assertIn(word.lower(), result.lower())
