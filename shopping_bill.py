import sys

# Ensure UTF-8 output encoding for rupee symbol (₹) across various terminals/environments
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def calculateElectronicsGST(a, b):
    
   # Step 1: Calculate electronics GST at 18%.
    electronics_amount = a + b
    gst = electronics_amount * 0.18
    total = electronics_amount + gst
    return total


def calculateFashionGST(c, d):

    #Step 2: Calculate fashion GST at 13%.
    fashion_amount = c + d
    gst = fashion_amount * 0.13
    total = fashion_amount + gst
    return total


def calculateFoodGST(e):

    #Step 3: Calculate food GST at 7%.
    food_amount = e
    gst = food_amount * 0.07
    total = food_amount + gst
    return total


def totalBill(a, b, c, d, e):
    
   # Step 4: Calculate total bill by summing the amounts after GST.
    electronics_total = calculateElectronicsGST(a, b)
    fashion_total = calculateFashionGST(c, d)
    food_total = calculateFoodGST(e)
    return electronics_total + fashion_total + food_total


def calculateDiscountedBill(a, b, c, d, e):
    
    #Step 5: Apply a 20% discount to the total bill after GST.
    
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    final_amount = total - discount
    return final_amount


def main():
    # Five item amounts passed directly as arguments (Sample values: 100 each)
    a = 100.0  # Electronics item 1
    b = 100.0  # Electronics item 2
    c = 100.0  # Fashion item 1
    d = 100.0  # Fashion item 2
    e = 100.0  # Food item

    # Perform calculations using required functions
    electronics_total = calculateElectronicsGST(a, b)
    fashion_total = calculateFashionGST(c, d)
    food_total = calculateFoodGST(e)
    total_after_gst = totalBill(a, b, c, d, e)
    final_payable = calculateDiscountedBill(a, b, c, d, e)
    discount = total_after_gst - final_payable

    # Display results formatted to 2 decimal places
    print(f"Electronics Total: ₹{electronics_total:.2f}")
    print(f"Fashion Total: ₹{fashion_total:.2f}")
    print(f"Food Total: ₹{food_total:.2f}")
    print(f"Total after GST: ₹{total_after_gst:.2f}")
    print(f"Discount (20%): ₹{discount:.2f}")
    print(f"Final Payable Amount: ₹{final_payable:.2f}")


if __name__ == "__main__":
    main()
