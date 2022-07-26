from bankaccountimpl import BankAccountImpl


class unit_Tests(object):
    def testStartingAmount(self):
        starting_balance = 20
        subject = BankAccountImpl(starting_balance)
        result = subject.get_balance()
        assert result == starting_balance


if __name__ == "__main__":
    obj = unit_Tests()
    obj.testStartingAmount()
