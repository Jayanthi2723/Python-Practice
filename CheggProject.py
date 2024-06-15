def calc_AGI(wages, interest, unemployment):
    # Convert negative values to positive
    wages = abs(wages)
    interest = abs(interest)
    unemployment = abs(unemployment)

    # Calculate AGI
    AGI = wages + interest + unemployment

    return AGI

def get_deduction(status):
    if status == 0:
        deduction = 6000
    elif status == 1:
        deduction = 12000
    elif status == 2:
        deduction = 24000
    else:
        deduction = 6000

    return deduction

def calc_taxable(AGI, deduction):
    taxable = AGI - deduction

    if taxable < 0:
        taxable = 0

    return taxable

def calc_tax(status, taxable):
    if status == 0:
        brackets = [0, 5100, 7650, 12750, 30750, 41500, 62250]
        rates = [0.0, 0.10, 0.12, 0.22, 0.24, 0.32, 0.35]
    elif status == 1:
        brackets = [0, 9700, 39475, 84200, 160725, 204100, 510300]
        rates = [0.0, 0.10, 0.12, 0.22, 0.24, 0.32, 0.35]
    elif status == 2:
        brackets = [0, 19400, 78950, 168400, 321450, 408200, 612350]
        rates = [0.0, 0.10, 0.12, 0.22, 0.24, 0.32, 0.35]
    else:
        return -1

    tax = 0.0

    for i in range(len(brackets) - 1):
        if taxable <= brackets[i+1]:
            tax += round((taxable - brackets[i]) * rates[i], 0)
            break
        else:
            tax += round((brackets[i+1] - brackets[i]) * rates[i], 0)

    return int(tax)

def calc_tax_due(status, taxable, taxes_withheld):
    if taxes_withheld < 0:
        taxes_withheld = 0

    tax = calc_tax(status, taxable)
    tax_due = tax - taxes_withheld

    return tax_due

# Main program
wages, interest, unemployment, status, taxes_withheld = input().split()
wages = int(wages)
interest = int(interest)
unemployment = int(unemployment)
status = int(status)
taxes_withheld = int(taxes_withheld)

# Calculate AGI
AGI = calc_AGI(wages, interest, unemployment)
print(f"AGI: ${AGI:,}")

# Calculate deduction
deduction = get_deduction(status)
print(f"Deduction: ${deduction:,}")

# Calculate taxable income
taxable = calc_taxable(AGI, deduction)
print(f"Taxable income: ${taxable:,}")

# Calculate federal tax
tax = calc_tax(status, taxable)
print(f"Federal tax: ${tax:,}")

# Calculate tax due
tax_due = calc_tax_due(status, taxable, taxes_withheld)
print(f"Tax due: ${tax_due:,}")
