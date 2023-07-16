rent_amount = 800.00
insurance_amount = 12.58
vehicle_gas_amount = 80.00
netflix_amount = 12.49
food_amount = 700.00
save_amount = 170.00
phone_amount = 61.06
electric_amount = 29.25
gas_amount = 34.01
internet_amount = 65.00
disposable_amount = 600.00
medical_amount = 75.00
massage_amount = 198.00


budget_june_2023 = {
    'rent': rent_amount,
    'insurance': insurance_amount,
    'vehicle_gas': vehicle_gas_amount,
    'netflix': netflix_amount,
    'food': food_amount,
    'save': save_amount,
    'phone': phone_amount,
    'electric': electric_amount,
    'gas': gas_amount,
    'internet': internet_amount,
    'disposable': disposable_amount,
    'medical': medical_amount,
    'massage': massage_amount
}

#Print sum of budget dictionary
def total_budget(budget):
    total = 0
    for key in budget:
        total += budget[key]
    
    return round(total, 2)

print(total_budget(budget_june_2023))
