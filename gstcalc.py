amount = float(input("Enter Amount"))
gst = float(input("Enter GST Percentage:"))

print("1. Add GST")
print("2. Remove GST")

choice = int(input("Enter choice (1 or 2)"))

if choice == 1:
    gst_amount = (amount + gst)/100
    net_price = amount +gst_amount

    print("GST Amount = ",gst_amount)
    print("Net Price =",net_price)


elif choice == 2:
    gst_amount = amount - (amount * (100/(100 + gst)))
    net_price = amount +gst_amount

    print("GST Amount = ",gst_amount)
    print("Net Price =",net_price)

else :
    print("Invalid Choice")