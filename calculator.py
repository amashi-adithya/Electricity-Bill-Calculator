print("Electricity Bill Calculator")

consumer_type = input("Enter consumer type (domestic/corporate/religious): ")
units = float(input("Enter electricity usage in kWh: "))

bill = 0

if consumer_type == "domestic":
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + (units - 100) * 15
    else:
        bill = (100 * 10) + (100 * 15) + (units - 200) * 20
