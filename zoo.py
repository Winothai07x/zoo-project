class Zoo:
    def get_ticket_price(self, age):
        if age <= 0:
            return "Invalided"
        elif age <= 12:
            return 50
        elif age <= 20:
            return 100
        elif age <= 60:
            return 150
        else:
            return 100
