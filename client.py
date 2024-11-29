import requests

BASE_URL = "http://127.0.0.1:8000/api/products/"

# Add a new product
def add_product():
    print("Attempting to add product...")  # Debugging print statement
    product = {
        "name": "Sunscreen",
        "description": "Skin care products",
        "price": 1800.00
    }
    response = requests.post(BASE_URL, json=product)  # POST request to add a product
    
    # Print status code and response details
    print("Response Status Code:", response.status_code)
    if response.status_code == 201:
        print("Product created successfully:", response.json())
    else:
        print("Failed to create product:", response.text)  # Raw response in case of failure

# Retrieve all products
def get_products():
    print("Attempting to retrieve products...")  # Debugging print statement
    response = requests.get(BASE_URL)  # GET request to retrieve products
    
    # Print status code and response details
    print("Response Status Code:", response.status_code)
    if response.status_code == 200:
        products = response.json()
        print(f"Retrieved {len(products)} product(s):")
        for product in products:
            print(f"- Name: {product['name']}, Price: {product['price']}")
    else:
        print("Failed to retrieve products:", response.text)

# Main script execution
if __name__ == "__main__":
    print("Running client script...")
    add_product()  # Add a new product
    get_products()  # Retrieve all products
