class Payment:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method
        
    def confirm(self):
        
        if self.payment_method == 'M-Pesa':
            
            return True  
        elif self.payment_method == 'Cash':
            
            return True  
        else:
           
            return False

class PaymentManager:
    def __init__(self):
        self.payments = []
    
    def process_payment(self, amount, payment_method):
        payment = Payment(amount, payment_method)
        success = payment.confirm()
        if success:
            self.payments.append(payment)
        return success


payment_manager = PaymentManager()


paid = payment_manager.process_payment(100.0, 'M-Pesa')
if paid:
    print('Payment successful!')
else:
    print('Payment failed.')


paid_by_cash = payment_manager.process_payment(50.0, 'Cash')
if paid_by_cash:
    print('Payment successful!')
else:
    print('Payment failed.')
