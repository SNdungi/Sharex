#Share Investment package defining the investment,share prices and transactional charges
class Investment:
    def __init__ (self,name,value,sell_price,buy_price,charge_lowtier=0.0213,charge_uppertier=0.0184):
        self.name=name
        self.value=float(value)  
        self.lowtier=float(charge_lowtier)
        self.uppertier=float(charge_uppertier)
        self.share_sp=float(sell_price)
        self.share_bp=float(buy_price)
    
    def get_min_sell_price(value,buying,charge):
        if 1000<=value<100000:
            rate_of_growth=round(1/(1-charge)**2,2)
            return buying*rate_of_growth       
        elif value>=100000:
            rate_of_growth=round(1/(1-charge)**2,2)
            return buying*rate_of_growth
        else: 
            print("Amount less than 1,000")        

    def inv_txn_charge(self):
        if 1000<=self.value<100000:
            return self.value*self.lowtier
        elif self.value>=100000:
            return self.value*self.uppertier
        else: 
            print("Amount less than 1,000")

    def share_volume(self):
        try:
            sv=round((self.value-self.inv_txn_charge())/self.share_bp,-2)
            return sv
        except ZeroDivisionError as zde:
            print('Share purchase price should be greater than: Zero-O',zde)

    def purchase_residual(self):
        residual=self.value-self.inv_txn_charge()-(self.share_volume()*self.share_bp)
        print('investment less charge:',self.value-self.inv_txn_charge())
        print('rounded share volume:',self.share_volume()*self.share_bp)
        return residual
    

    def sell_value(self):
        return self.share_volume()*self.share_sp
    
    def inv_rtn_charge(self):
        if 1000<=self.sell_value()<100000:
            return self.sell_value()*self.lowtier
        elif self.value>=100000:
            return self.sell_value()*self.uppertier
        else: 
            print("Amount less than 1,000")    
      

    def expected_ROI(self):
        try:
            sell_value=self.share_volume()*self.share_sp
            net_return= sell_value-self.inv_rtn_charge()
            return round(net_return+self.purchase_residual()-self.value,0)
        except ZeroDivisionError as zde:
            print('Share purchase price should be greater than: Zero-O',zde)

    def __str__(self):
        return f"{self.name} : investment = {self.value}"  


        
