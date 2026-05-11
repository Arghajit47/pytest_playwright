from playwright.sync_api import expect, Locator
from pytest_pulse import pulse_step, step


class BasePage:

    def __init__(self, page):
        self.page = page

    def waitForFullyPageLoad(self):
        with pulse_step("Wait for full page load"):
            self.page.wait_for_load_state("domcontentloaded")
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_load_state("load")

    def navigateToUrl(self, url: str):
        with pulse_step("Navigate to the url"):
            self.page.goto(url)
            self.waitForFullyPageLoad()

    def click(self, locator: str | Locator, index: int = 0):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and Clicking on it"):
                self.page.locator(locator).nth(index).click()
                self.waitForFullyPageLoad()
        else:
            with pulse_step("Got Direct Locator, Clicking on it"):
                locator.nth(index).click()
                self.waitForFullyPageLoad()

    def fill(self, locator: str | Locator, text: str, index: int = 0):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and Filling it"):
                self.page.locator(locator).nth(index).fill(text)
                self.waitForFullyPageLoad()
        else:
            with pulse_step("Got Direct Locator, Filling it"):
                locator.nth(index).fill(text)
                self.waitForFullyPageLoad()

    def verify_page_title(self, title: str):
        with pulse_step("Verifying page title"):
            expect(self.page).to_have_title(title)

    def verify_element_is_visible(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_visible()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_visible()

    def verify_element_is_not_visible(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_hidden()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_hidden()

    def verify_element_is_enabled(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_enabled()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_enabled()

    def verify_element_is_disabled(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_disabled()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_disabled()

    def verify_element_is_checked(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_checked()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_checked()

    def verify_element_text(self, locator: str | Locator, text: str, index: int = 0):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator).nth(index)).to_have_text(text)
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator.nth(index)).to_have_text(text)

    def verify_page_url(self, url: str):
        with pulse_step("Verify page url"):
            self.waitForFullyPageLoad()
            expect(self.page).to_have_url(url)

    def get_element_count(self, locator: str | Locator) -> int:
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and getting element count"):
                return self.page.locator(locator).count()
        else:
            with pulse_step("Got Direct Locator, Getting element count"):
                return locator.count()

    def verify_element_count(self, locator: str | Locator, count: int):
        if isinstance(locator, str):
            with pulse_step(
                "Generating Locator from string and verifying element count"
            ):
                expect(self.page.locator(locator)).to_have_count(count)
        else:
            with pulse_step("Got Direct Locator, Verifying element count"):
                expect(locator).to_have_count(count)

    def get_all_element_texts(self, locator: str | Locator):
        with pulse_step("Getting all element texts"):
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
        with pulse_step("Generating Locator from string and verifying element texts"):
            actual_texts = self.get_all_element_texts(locator)
            self.verify_equal(actual_texts, expected_texts)

    def verify_element_texts_contains(
        self, locator: str | Locator, expected_texts: str
    ):
        with pulse_step(
            "Generating Locator from string and verifying element texts contains"
        ):
            actual_texts = self.get_all_element_texts(locator)
            self.verify_equal(actual_texts, expected_texts)

    def verify_equal(self, actual, expected):
        with pulse_step("Verifying equal"):
            assert actual == expected, f"{actual} != {expected}"

    def get_attribute(self, locator: str | Locator, attribute: str):
        with pulse_step("Getting attribute"):
            if isinstance(locator, str):
                return self.page.locator(locator).get_attribute(attribute)
            else:
                return locator.get_attribute(attribute)

    def verify_element_text_ignore_case(
        self, locator: str | Locator, text: str, index: int = 0
    ):
        with pulse_step("Verifying element text ignore case"):
            if isinstance(locator, str):
                expect(self.page.locator(locator).nth(index)).to_have_text(
                    text, ignore_case=True
                )
            else:
                expect(locator.nth(index)).to_have_text(text, ignore_case=True)

    def capture_screenshot(self, path: str = "screenshots"):
        with pulse_step("Capturing full pagescreenshot"):
            self.page.screenshot(path=path, full_page=True)
