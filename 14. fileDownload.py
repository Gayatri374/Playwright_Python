from playwright.sync_api import sync_playwright


def download_handle(download):
    file_location='./collectDownloadedfiles/demotest.zip'
    download.save_as(file_location)

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto('https://demo.automationtesting.in/FileDownload.html')

    page.on('download', download_handle)
    page.wait_for_selector('//a[@type="button"]').click()
    page.wait_for_timeout(3000)




def download_handle(download):
    file_location='./filename/saveasname'
    download.save_as(file_location)


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto('url')

    page.on('download',download_handle)
    page.wait_for_selector('xpath').click()

