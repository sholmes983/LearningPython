import math
import argparse


def calc_diff(principal1, periods1, interest1, month1):
    nom_interest = interest1/1200
    term1 = principal1 / periods1
    dividend = principal1 * (month1 - 1)
    term2 = principal1 - (dividend/periods1)
    return math.ceil(term1 + nom_interest * term2)


parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=['diff', 'annuity'])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if args.type == 'diff':
    if args.principal is None or args.periods is None or args.interest is None:
        print('Incorrect parameters')
    elif args.payment is not None:
        print('Incorrect parameters')
    else:
        principal = int(args.principal)
        periods = int(args.periods)
        interest = float(args.interest)
        overpay = 0.0
        for i in range(1, periods + 1):
            monthly_payment = calc_diff(principal, periods, interest, i)
            print("Month {}: payment is {}".format(i, monthly_payment))
            overpay += monthly_payment
        overpay = overpay - principal
        print()
        print("Overpayment = {}".format(overpay))
elif args.type == 'annuity':
    if (args.interest is None or args.periods is None or args.principal is None) and \
       (args.interest is None or args.payment is None or args.periods is None) and \
       (args.principal is None or args.payment is None or args.interest is None):
        print('Incorrect parameters')
    else:
        if args.periods is None:
            principal = int(args.principal)
            payment = int(args.payment)
            interest = float(args.interest)
            nominal = interest/1200
            no_payments = math.log((payment
                                    / (payment - nominal * principal)), nominal + 1)
            months = int(math.ceil(no_payments))
            periods = months
            years = int(months / 12)
            months %= 12
            overpayment = periods * payment - principal
            if years == 0:
                if months > 1:
                    print('It will take {} months to repay this loan!'
                          .format(months))
                    print('Overpayment = {}'.format(overpayment))
                elif months == 1:
                    print('It will take you 1 month to repay this loan!')
                    print('Overpayment = {}'.format(overpayment))
                else:
                    print('It will take you 0 months to repay this loan!')
                    print('Overpayment = {}'.format(overpayment))
            elif years == 1:
                if months > 1:
                    print('It will take 1 year and {} months to repay this loan!'
                          .format(months))
                    print('Overpayment = {}'.format(overpayment))
                elif months == 1:
                    print('It will take 1 year and 1 month to repay this loan!')
                    print('Overpayment = {}'.format(overpayment))
                else:
                    print('It will take 1 year to repay this loan!')
                    print('Overpayment = {}'.format(overpayment))
            else:
                if months > 1:
                    print('It will take {} year and {} months to repay this loan!'
                          .format(years, months))
                    print('Overpayment = {}'.format(overpayment))
                elif months == 1:
                    print('It will take {} years and 1 month to repay this loan!'
                          .format(years))
                    print('Overpayment = {}'.format(overpayment))
                else:
                    print('It will take {} years to repay this loan!'.format(years))
                    print('Overpayment = {}'.format(overpayment))
        elif args.payment is None:
            principal = int(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)
            nominal = interest/1200
            payment = principal * (nominal * math.pow((1 + nominal), periods)) / ((math.pow((1 + nominal), periods)) - 1)
            payment = math.ceil(payment)
            overpayment = periods * payment - principal
            print('Your annuity payment = {}!'.format(payment))
            print('Overpayment = {}'.format(overpayment))
        elif args.principal is None:
            payment = float(args.payment)
            periods = int(args.periods)
            interest = float(args.interest)
            nominal = interest/1200
            principal = payment / ((nominal * math.pow((1 + nominal), periods)) / ((math.pow((1 + nominal), periods)) - 1))
            overpayment = periods * payment - principal
            print('Your loan principal = {0:.0f}!'.format(principal))
            print('Overpayment = {}'.format(overpayment))
else:
    print("Incorrect Parameters")
