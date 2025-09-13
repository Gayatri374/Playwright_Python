from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Open first page
    page1 = context.new_page()
    page1.goto("https://example.com")
    print("First page title:", page1.title())

    # Open second page (new tab)
    page2 = context.new_page()
    page2.goto("https://playwright.dev")
    print("Second page title:", page2.title())

    # Switch back to first page
    page1.bring_to_front()
    print("Back to first page:", page1.title())

    browser.close()