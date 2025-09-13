from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    page.wait_for_selector("//input[@name='username']").type('Admin')
    page.wait_for_selector("//input[@name='password']").type('admin123')
    page.wait_for_selector('//button[text()=" Login "]').click()
    page.wait_for_timeout(8000)