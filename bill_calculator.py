def tip_amount(bill_amount, tip_per):
    return bill_amount * tip_per * 0.01

# print tip_amount(100, 10)


# def total_bill(tip_amount, bill_amount):
#     return tip_amount + bill_amount


# print total_bill(10, 100)

# def split_bill(bill_amount,num_ppl):
#     return bill_amount/num_ppl

# print split_bill(100,3)

def main(): 
    print """
    1 - calculate tip
    2 - split the bill\n
    """
    org_bill_amt=float(raw_input("What is the original bill amount?"))
    tip_per=float(raw_input("What is the tip percentage?"))
    print "the tip amount is %f" % (tip_amount(org_bill_amt, tip_per))

main()



