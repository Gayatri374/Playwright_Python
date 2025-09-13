import pandas as pd
from playwright.sync_api import sync_playwright





# Read the Excel file
df = pd.read_excel(r"C:\Users\Gpotadar\Downloads\Playwright_Login_TestCases.xlsx")




def run_test_cases():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Do NOT add ignore_https_errors here
        context = browser.new_context(ignore_https_errors=True)  # Set it here
        page = context.new_page()


        for index, row in df.iterrows():
            test_id = row['Test ID']
            step = row['Test Step']
            selector = str(row['Selector']) if not pd.isna(row['Selector']) else ""
            input_value = str(row['Input Value']) if not pd.isna(row['Input Value']) else ""

            print(f"\n Running: {test_id} - {step}")

            try:
                if "Navigate to" in step:
                    page.goto(input_value)
                elif "Check page title" in step:
                    assert page.title() == row['Expected Result']
                elif "Check if" in step:
                    page.wait_for_selector(selector, timeout=3000)
                elif "Login with" in step:
                    # Split selector and input
                    if "username" in selector and "password" in selector:
                        username, password = input_value.split('/')
                        page.fill("#username", username.strip())
                        page.fill("#password", password.strip())
                    page.click("#signIn")
                    page.wait_for_timeout(2000)  # wait for error/success
                elif "masked" in step:
                    input_type = page.get_attribute("#password", "type")
                    assert input_type == "password"
                elif "branding" in step:
                    assert page.inner_text("body").find("MetricStream Platform") != -1
                elif "keyboard" in step:
                    # just tab through elements
                    for _ in range(5):  # tab through fields
                        page.keyboard.press("Tab")
                else:
                    print("Skipping unknown test type")
            except Exception as e:
                print(f"Test {test_id} failed: {e}")

        browser.close()


if __name__ == "__main__":
    run_test_cases()
