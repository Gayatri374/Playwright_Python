from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto('https://demo.automationtesting.in/Windows.html')

    

    # Mouse Actions

    # hover
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    page.wait_for_timeout(3000)

    # Click
    page.wait_for_selector('//a[text()="SwitchTo"]').click()

    # Double click
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()

    # Right click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button='right')

    # Shift
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=['Shift'])


    # Keyboard
    page.wait_for_selector('//a[text()="SwitchTo"]').press('A')
    # A-Z, 0-9, F1-F2, All special character, ArrowRight, ArrowDown, pageUp, pageDown, Enter, control, command,
    page.wait_for_selector('//a[text()="SwitchTo"]').press('$')