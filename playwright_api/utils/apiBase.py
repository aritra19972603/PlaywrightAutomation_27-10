

from playwright.sync_api import Playwright
ordersPayload={"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}





class APIUtils:

	def getToken(self,playwright:Playwright):
		api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
		response = api_request_context.post("/api/ecom/auth/login",
		                         data={"userEmail": "aritrajana97@gmail.com", "userPassword": "Aritra1997@"},

		                         )

		assert response.ok
		print(response.json())
		responseBody=response.json()
		return responseBody["token"]


	def createOrder(self,playwright: Playwright):
		token =self.getToken(playwright)
		api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
		response = api_request_context.post("/api/ecom/order/create-order",
		    data=ordersPayload,
		    headers={"Authorization": token,
		             "Content-Type": "application/json"}
		                        )
		print(response.json())
		responseBody=response.json()
		orderId= responseBody["orders"][0]
		return orderId







