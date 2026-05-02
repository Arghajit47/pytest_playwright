# This is a pytest-playwright test file, always remember to add `test_` to the file name and `test_` to the test function name.


def test_example(page):
    page.goto("https://www.naukri.com")
    page.wait_for_load_state("domcontentloaded")
    print(page.title())
    assert (
        "Jobs - Recruitment - Job Search - Employment - Job Vacancies - Naukri.com"
        in page.title()
    )
    page.screenshot(path="naukri.png", full_page=True)
    page.close()
