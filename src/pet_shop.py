# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    name = pet_shop["name"]
    return name

def get_total_cash(pet_shop):
    sum = pet_shop["admin"]["total_cash"]
    return sum

def add_or_remove_cash(cash, amount): # cash is 1000
    cash["admin"]["total_cash"] = cash["admin"]["total_cash"] + amount
    return cash

def get_pets_sold(pet_shop):
    sold = pet_shop["admin"]["pets_sold"]
    return sold

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + amount
    return pet_shop

def get_stock_count(pet_shop):
    stock_amount = len(pet_shop["pets"])
    return stock_amount

def get_pets_by_breed(pet_shop, pet_breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, pet_name): #pet_name == "arthur"
    # breakpoint()
    animal_found = {}
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            animal_found = pet
            return animal_found
        
def remove_pet_by_name(pet_shop, pet_name):
    # breakpoint()
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)
            return pet_shop

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    cash = customers["cash"]
    return cash

def remove_customer_cash(customers, cash_adjust_sum):
    customers["cash"] = customers["cash"] - cash_adjust_sum
    return customers

def get_customer_pet_count(customers):
    count = len(customers["pets"])
    return count

def add_pet_to_customer(customer, new_pet):
    # breakpoint()
    customer["pets"].append(new_pet)
    return customer

def customer_can_afford_pet(customer, new_pet):
    cash = get_customer_cash(customer)
    pet_cost = new_pet["price"]
    if cash >= pet_cost:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    customer = add_pet_to_customer(customer, pet)
    pet_shop = increase_pets_sold(pet_shop, 1)
    customer["cash"] = get_customer_cash(customer) - pet["price"]
    pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop) + pet["price"]