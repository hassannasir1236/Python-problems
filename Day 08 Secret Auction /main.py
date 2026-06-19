bids_data = {}

while True:

    name = input("Please enter user name: ")
    bid = int(input("Please enter bid: "))

    # store data
    bids_data[name] = bid

    addNext = input("Please enter Y to continue and N to stop: ").upper()

    if addNext == "N":
        break


# Find highest bidder
high_value_name = ""
high_value_bid = 0

for name in bids_data:

    if bids_data[name] > high_value_bid:
        high_value_bid = bids_data[name]
        high_value_name = name


print("\n🏆 Winner:", high_value_name)
print("💰 Highest Bid:", high_value_bid)