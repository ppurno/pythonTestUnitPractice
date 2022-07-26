from bankaccountimpl import BankAccountImpl


class unit_Tests(object):
    def testStartingAmount(self):
        starting_balance = 20
        subject = BankAccountImpl(starting_balance)
        result = subject.get_balance()
        assert result == starting_balance


    def debitReductionMethod(self):
        amountToBeDebited=30
        initial_Balance=100
        subject=BankAccountImpl(initial_Balance)
        result=subject.debit(amountToBeDebited)
        assert result==initial_Balance-amountToBeDebited




if __name__ == "__main__":
    obj = unit_Tests()
    obj.testStartingAmount()
    obj.debitReductionMethod()
