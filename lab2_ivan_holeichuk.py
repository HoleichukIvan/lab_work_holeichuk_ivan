class Policy:
    def __init__(self, policy_number, insured_name, insured_amount, premium):
        self.policy_number = policy_number
        self.insured_name = insured_name
        self.__insured_amount = insured_amount
        self.__premium = premium

    def policy_info(self):
        return f"Policy #{self.policy_number} for {self.insured_name}"

    def update_premium(self, new_premium):
        self.__premium = new_premium

    @staticmethod
    def welcome_message():
        return "Welcome to our insurance company!"

class Claim:
    def __init__(self, claim_number, policy_number, claim_amount):
        self.claim_number = claim_number
        self.policy_number = policy_number
        self.__claim_amount = claim_amount

    def claim_info(self):
        return f"Claim #{self.claim_number} for Policy #{self.policy_number}"

    def update_claim(self, new_amount):
        self.__claim_amount = new_amount

class LifePolicy(Policy):
    def __init__(self, policy_number, insured_name, insured_amount, premium, age):
        super().__init__(policy_number, insured_name, insured_amount, premium)
        self.age = age

    def policy_info(self):
        return f"Life {super().policy_info()}, Age: {self.age}"

class HealthPolicy(Policy):
    def __init__(self, policy_number, insured_name, insured_amount, premium, disease_covered):
        super().__init__(policy_number, insured_name, insured_amount, premium)
        self.disease_covered = disease_covered

    def policy_info(self):
        return f"Health {super().policy_info()}, Covers: {self.disease_covered}"

class CarPolicy(Policy, Claim):
    def __init__(self, policy_number, insured_name, insured_amount, premium, car_model, claim_number, claim_amount):
        Policy.__init__(self, policy_number, insured_name, insured_amount, premium)
        Claim.__init__(self, claim_number, policy_number, claim_amount)
        self.car_model = car_model

    def policy_info(self):
        return f"Car {self.car_model} - {super().policy_info()}"

# Демонстраційний алгоритм
life_policy = LifePolicy(101, "Ivan Holeichuk", 100000, 1200, 30)
health_policy = HealthPolicy(102, "Oksana Shevchenko", 50000, 900, "Diabetes")
car_policy = CarPolicy(201, "Vasya Petrenko", 50000, 800, "Toyota Corolla", 301, 1000)

policies = [life_policy, health_policy, car_policy]

for p in policies:
    print(p.policy_info())

print(life_policy.welcome_message())

life_policy.update_premium(1300)
health_policy.update_premium(950)
car_policy.update_claim(1200)

print(life_policy.policy_info())
print(health_policy.policy_info())
print(car_policy.claim_info())
