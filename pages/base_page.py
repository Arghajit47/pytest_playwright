from playwright.sync_api import expect, Locator


class BasePage:
    def __init__(self, page):
        self.page = page

    def waitForFullyPageLoad(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_load_state("load")

    def navigateToUrl(self, url: str):
        self.page.goto(url)
        self.waitForFullyPageLoad()

    def click(self, locator: str | Locator, index: int = 0):
        if isinstance(locator, str):
            self.page.locator(locator).nth(index).click()
        else:
            locator.nth(index).click()
        self.waitForFullyPageLoad()

    def fill(self, locator: str | Locator, text: str, index: int = 0):
        if isinstance(locator, str):
            self.page.locator(locator).nth(index).fill(text)
        else:
            locator.nth(index).fill(text)
        self.waitForFullyPageLoad()

    def verify_page_title(self, title: str):
        expect(self.page).to_have_title(title)

    def verify_element_is_visible(self, locator: str | Locator):
        if isinstance(locator, str):
            expect(self.page.locator(locator)).to_be_visible()
        else:
            expect(locator).to_be_visible()

    def verify_element_is_not_visible(self, locator: str | Locator):
        if isinstance(locator, str):
            expect(self.page.locator(locator)).to_be_hidden()
        else:
            expect(locator).to_be_hidden()

    def verify_element_is_enabled(self, locator: str | Locator):
        if isinstance(locator, str):
            expect(self.page.locator(locator)).to_be_enabled()
        else:
            expect(locator).to_be_enabled()

    def verify_element_is_disabled(self, locator: str | Locator):
        if isinstance(locator, str):
            expect(self.page.locator(locator)).to_be_disabled()
        else:
            expect(locator).to_be_disabled()

    def verify_element_is_checked(self, locator: str | Locator):
        if isinstance(locator, str):
            expect(self.page.locator(locator)).to_be_checked()
        else:
            expect(locator).to_be_checked()

    def verify_element_text(self, locator: str | Locator, text: str, index: int = 0):
        if isinstance(locator, str):
            expect(self.page.locator(locator).nth(index)).to_have_text(text)
        else:
            expect(locator.nth(index)).to_have_text(text)

    def verify_page_url(self, url: str):
        expect(self.page).to_have_url(url)

    def get_element_count(self, locator: str | Locator) -> int:
        if isinstance(locator, str):
            return self.page.locator(locator).count()
        else:
            return locator.count()

    def verify_element_count(self, locator: str | Locator, count: int):
        if isinstance(locator, str):
            expect(self.page.locator(locator)).to_have_count(count)
        else:
            expect(locator).to_have_count(count)

    def get_all_element_texts(self, locator: str | Locator):
        count = self.get_element_count(locator)
        if count == 0:
            raise ValueError("No elements found with the given locator")
        texts = []
        for i in range(count):
            texts.append(self.page.locator(locator).nth(i).inner_text())
        return texts

    def verify_all_element_texts(
        self, locator: str | Locator, expected_texts: list[str]
    ):
        actual_texts = self.get_all_element_texts(locator)
        self.verify_equal(actual_texts, expected_texts)

    def verify_element_texts_contains(self, locator: str | Locator, text: str):
        actual_texts = self.get_all_element_texts(locator)
        assert text in actual_texts, f"{text} not found in element texts"

    def verify_equal(self, actual, expected):
        assert actual == expected, f"{actual} != {expected}"

    def get_attribute(self, locator: str | Locator, attribute: str):
        if isinstance(locator, str):
            return self.page.locator(locator).get_attribute(attribute)
        else:
            return locator.get_attribute(attribute)

    def verify_element_text_ignore_case(
        self, locator: str | Locator, text: str, index: int = 0
    ):
        if isinstance(locator, str):
            expect(self.page.locator(locator).nth(index)).to_have_text(
                text, ignore_case=True
            )
        else:
            expect(locator.nth(index)).to_have_text(text, ignore_case=True)

    def capture_screenshot(self, path: str = "screenshots"):
        self.page.screenshot(path=path, full_page=True)
