from playwright.sync_api import Page

fakePayloadOrderResponse={"data":[],"message":"No Orders"}
def intercept_response(route):
	route.fulfill(
		json=fakePayloadOrderResponse
	)

def test_Network_1(page:Page):
	page.goto("https://rahulshettyacademy.com/client/")
	page.route("https://rahulshettyacademy.com/api/ecom/user/get-cart-count/*",intercept_response)
	page.get_by_placeholder("email@example.com").fill("aritrajana97@gmail.com")
	page.get_by_placeholder("enter your passsword").fill("Aritra1997@")
	page.get_by_role("button",name="Login").click()
	page.locator(".btn-custom").filter(has_text="ORDERS").click()
	order_text=page.locator(".mt-4").text_content()
	print(order_text)

