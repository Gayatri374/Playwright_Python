import pandas as pd
from playwright.sync_api import sync_playwright

# Read the Excel file
df = pd.read_excel(r"C:\Users\Gpotadar\Downloads\Playwright_Login_TestCases.xlsx")


def run_test_cases():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()

            for index, row in df.iterrows():
                test_id = row['Test ID']
                step = row['Test Step']
                selector = str(row['Selector']) if not pd.isna(row['Selector']) else ""
                input_value = str(row['Input Value']) if not pd.isna(row['Input Value']) else ""
                expected = str(row['Expected Result']) if not pd.isna(row['Expected Result']) else ""

                print(f"\n🧪 Running: {test_id} - {step}")
                try:
                    if "Navigate to" in step:
                        page.goto(input_value, wait_until="load")

                    elif "page title" in step.lower():
                        actual_title = page.title()
                        assert expected in actual_title

                    elif "Check if" in step:
                        page.wait_for_selector(selector, state="visible", timeout=5000)

                    elif "Login with" in step:
                        if "username" in selector and "password" in selector:
                            if '/' in input_value:
                                username, password = input_value.split('/')
                            else:
                                username, password = "SYSTEMI", "welcome*12"
                            page.fill("#username", username.strip())
                            page.fill("#password", password.strip())
                        page.click("#signIn")
                        page.wait_for_timeout(2000)

                    elif "masked" in step:
                        input_type = page.get_attribute("#password", "type")
                        assert input_type == "password"

                    elif "branding" in step:
                        page.wait_for_selector("body", timeout=3000)
                        body_text = page.inner_text("body")
                        assert "MetricStream Platform" in body_text

                    elif "keyboard" in step:
                        for _ in range(5):
                            page.keyboard.press("Tab")

                    df.at[index, "Result"] = "Pass"

                except Exception as e:
                    error_msg = str(e)
                    df.at[index, "Result"] = "Fail"
                    df.at[index, "Error"] = error_msg
                    screenshot_path = f"screenshots/{test_id}.png"
                    try:
                        page.screenshot(path=screenshot_path)
                        df.at[index, "Screenshot"] = screenshot_path
                    except:
                        df.at[index, "Screenshot"] = "Screenshot Failed"
                    print(f"❌ Test {test_id} failed: {error_msg}")

            # Save Excel after all test cases
            df.to_excel(r"C:\Users\Gpotadar\Downloads\Playwright_Login_TestCases_Results.xlsx", index=False)
            print("\n✅ Test execution completed. Results saved to Excel.")

            # Safe close
            browser.close()
    except Exception as outer:
        print("❌ Playwright failed to initialize or crashed:", outer)