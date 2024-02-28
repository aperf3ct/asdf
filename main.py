def gst_calculator():
    item = int(input("Enter the price of your item: "))
    with_gst = item * 1.15
    print("Your item with GST is ${}".format(with_gst))


gst_calculator()
