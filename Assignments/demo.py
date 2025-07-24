# Swiggy Product Information System using basic data types and formatting

# Inputs
product_id = int(input("Enter Food Item ID: "))
product_name = input("Enter Food Item Name: ")
price = float(input("Enter Price: ₹"))
categories = list(map(str.strip, input("Enter Categories (comma-separated, e.g., Main Course, Biryani): ").split(',')))
stock_details = tuple(map(int, input("Enter Available and Sold Stock : ").split()))
discount = float(input("Enter Discount Percentage: "))
features = set(map(str.strip, input("Enter Food Features (comma-separated, e.g., Spicy, Vegan): ").split(',')))

supplier_name, supplier_contact, supplier_location = map(str.strip, input("Enter Supplier Name, Contact Number, and Location : ").split(','))

supplier_details = {
    'Name': supplier_name,
    'Contact': supplier_contact,
    'Location': supplier_location
}

# Comma Separation
print("Food ID, Name, Price:", product_id, product_name, price, sep=', ')

# Percentage Formatting
print("Discount Offered: %.2f%%" % discount)

# f-strings
print(f"Food Item: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount}%")
print(f"Stock Available: {stock_details[0]} units")

# .format() method
print("Restaurant Details: Name - {}, Contact - {}, Location - {}".format(supplier_name, supplier_contact, supplier_location))
