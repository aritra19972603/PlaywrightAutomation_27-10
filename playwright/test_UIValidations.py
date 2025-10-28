from playwright.sync_api import Page


def test_UIValidationsDynamicScript(page:Page):
	page.goto("https://rahulshettyacademy.com/loginpagePractise/")
	page.get_by_label("Username:").fill("rahulshettyacademy")
	page.get_by_label("Password:").fill("learning")
	page.get_by_role("combobox").select_option("teach")

	page.get_by_role("link",name="terms and conditions").click()
	page.locator("#terms").check()
	page.get_by_role("button", name="Sign In").click()
