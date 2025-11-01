from playwright.sync_api import Page


def intercept_request(route):
	route.continue_(url="")



def test_Network_1(page:Page):
	page.goto("https://rahulshettyacademy.com/client/")
	page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_request)
	page.get_by_placeholder("email@example.com").fill("aritrajana97@gmail.com")
	page.get_by_placeholder("enter your passsword").fill("Aritra1997@")
	page.get_by_role("button",name="Login").click()
	page.locator(".btn-custom").filter(has_text="ORDERS").click()


