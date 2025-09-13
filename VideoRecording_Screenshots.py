from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(record_video_dir='./videorecording')
    page=context.new_page()


    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.wait_for_selector('//input[@name="username"]').type('Admin')
    page.wait_for_selector('//input[@name="password"]').type('admin123')
    page.wait_for_timeout(3000)
    # orange_screenshot and path
    page.screenshot(path='orange_screenshot/loginpage.png')
    page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)
    page.screenshot(path='orange_screenshot/homepage.png')
    context.close()
