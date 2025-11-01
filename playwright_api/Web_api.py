from playwright.sync_api import Playwright, expect

from playwright_api.utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
	browser = playwright.chromium.launch(headless=False)
	context = browser.new_context()
	page = context.new_page()

	#create order->order id
	api_utils=APIUtils()
	orderId=api_utils.createOrder(playwright)



	#login
	page.goto("https://rahulshettyacademy.com/client/")
	page.get_by_placeholder("email@example.com").fill("aritrajana97@gmail.com")
	page.get_by_placeholder("enter your passsword").fill("Aritra1997@")
	page.get_by_role("button",name="Login").click()


	#order History page
	page.locator(".btn-custom").filter(has_text="ORDERS").click()
	row=page.locator("tr").filter(has_text=orderId)
	row.get_by_role("button",name="View").click()
	expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
	context.close()






