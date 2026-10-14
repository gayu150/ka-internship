def calculateDomesticCharges(a, b):

    #Step 1: Calculate Domestic Electricity Charges
    
    base_amount = a + b
    service_charge = base_amount * 0.05
    total = base_amount + service_charge
    return total


def calculateCommercialCharges(c, d):

   # Step 2: Calculate Commercial Electricity Charges
    
    base_amount = c + d
    service_charge = base_amount * 0.10
    total = base_amount + service_charge
    return total


def calculateIndustrialCharges(e):

    #Step 3: Calculate Industrial Electricity Charges
   
    base_amount = e
    service_charge = base_amount * 0.15
    total = base_amount + service_charge
    return total


def totalBill(a, b, c, d, e):
    
    #Step 4: Calculate Total Electricity Bill
    
    domestic_total = calculateDomesticCharges(a, b)
    commercial_total = calculateCommercialCharges(c, d)
    industrial_total = calculateIndustrialCharges(e)
    return domestic_total + commercial_total + industrial_total


def calculateDiscountedBill(a, b, c, d, e):
    
   # Step 5: Apply a 10% discount on the total bill and return final payable amount.
    
    total = totalBill(a, b, c, d, e)
    discount = total * 0.10
    final_amount = total - discount
    return final_amount


def main():
    # Pass 5 values directly as arguments (No input() used)
    a = 100.0  # Domestic connection 1
    b = 100.0  # Domestic connection 2
    c = 100.0  # Commercial connection 1
    d = 100.0  # Commercial connection 2
    e = 100.0  # Industrial connection

    # Calling the required functions
    domestic = calculateDomesticCharges(a, b)
    commercial = calculateCommercialCharges(c, d)
    industrial = calculateIndustrialCharges(e)
    total = totalBill(a, b, c, d, e)
    final_payable = calculateDiscountedBill(a, b, c, d, e)
    discount = total - final_payable

    # Display results formatted to 2 decimal places
    print(f"Domestic Charges: {domestic:.2f}")
    print(f"Commercial Charges: {commercial:.2f}")
    print(f"Industrial Charges: {industrial:.2f}")
    print(f"Total Electricity Bill: {total:.2f}")
    print(f"Discount (10%): {discount:.2f}")
    print(f"Final Payable Amount: {final_payable:.2f}")


if __name__ == "__main__":
    main()

