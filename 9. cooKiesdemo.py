from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto('https://www.redbus.in/')


    # It will give all the cookies
    my_cookies=page.context.cookies()
    print(my_cookies)

    # It will clear all the cookies
    page.context.clear_cookies()


    # Add cookies

    new_cookies={
        'name':'ABC',
        'id':'243ertfghbnm'
    }

    # page.context.add_cookies([new_cookies])

    # Take Screenshot
    page.screenshot(path='test.png',full_page=True)