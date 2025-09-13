from playwright.sync_api import sync_playwright

# Broken links - In a web page we test all the links
# How you will take all the links in a page


with sync_playwright() as p:
    try:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        page.goto('https://demo.automationtesting.in/Selectable.html')


        page.query_selector('//d[@id="nn"]').click()
        elements=page.query_selector_all('b')

        for i in elements:
            print(i.text_content())
        page.wait_for_timeout(3000)

    except Exception as e:
        print(str(e))
    finally:
        print('Executive')