import pandas as pd

def run_single_scenario(inputs, scenario):
    # -------------------------
    # Base inputs
    # -------------------------
    property_price = inputs["property_price"]
    down_payment = inputs["down_payment"]
    loan_rate = inputs["loan_rate"]
    loan_tenure = inputs["loan_tenure"]
    maintenance_rate = inputs["maintenance_rate"]
    annual_property_tax = inputs["annual_property_tax"]
    analysis_years = inputs["analysis_years"]

    stamp_duty_rate = inputs["stamp_duty_rate"]
    selling_cost_rate = inputs["selling_cost_rate"]
    down_payment_return = inputs["down_payment_return"]

    # Scenario overrides
    rent = inputs["starting_rent"]
    rent_growth = scenario["rent_growth"]
    investment_return = scenario["investment_return"]
    property_appreciation = scenario["property_appreciation"]

    # -------------------------
    # Derived values
    # -------------------------
    loan_amount = property_price - down_payment
    monthly_rate = loan_rate / 12
    total_months = loan_tenure * 12

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** total_months
    ) / ((1 + monthly_rate) ** total_months - 1)

    loan_balance = loan_amount
    property_value = property_price
    investment_corpus = down_payment  # renter invests down payment

    stamp_duty_cost = property_price * stamp_duty_rate

    rows = []

    # -------------------------
    # Simulation
    # -------------------------
    for year in range(1, analysis_years + 1):

        # Loan mechanics
        if loan_balance > 0:
            interest_paid = loan_balance * loan_rate
            annual_emi = emi * 12
            principal_paid = min(annual_emi - interest_paid, loan_balance)
            loan_balance -= principal_paid
        else:
            interest_paid = 0
            principal_paid = 0
            annual_emi = 0

        maintenance_cost = property_value * maintenance_rate
        owning_cost = annual_emi + maintenance_cost + annual_property_tax

        renting_cost = rent * 12
        surplus = owning_cost - renting_cost

        # Investment growth
        investment_corpus = (
            investment_corpus * (1 + investment_return)
            + surplus
        )

        # Property appreciation
        property_value *= (1 + property_appreciation)

        rent *= (1 + rent_growth)

        rows.append({
            "Year": year,
            "Loan Balance": round(loan_balance),
            "Property Value": round(property_value),
            "Renter Corpus": round(investment_corpus)
        })

    df = pd.DataFrame(rows)

    # -------------------------
    # Exit adjustment
    # -------------------------
    selling_cost = property_value * selling_cost_rate
    owner_exit_value = property_value - selling_cost - loan_balance - stamp_duty_cost

    renter_final_value = investment_corpus

    return {
        "scenario": scenario["name"],
        "owner_net_worth": round(owner_exit_value),
        "renter_net_worth": round(renter_final_value),
        "df": df
    }


def run_all_scenarios(inputs):
    results = []

    for name, scenario in inputs["scenarios"].items():
        scenario["name"] = name
        result = run_single_scenario(inputs, scenario)
        results.append({
            "Scenario": name,
            "Owner Net Worth": result["owner_net_worth"],
            "Renter Net Worth": result["renter_net_worth"]
        })

    return pd.DataFrame(results)


def run_single_scenario(inputs, scenario):
    

    property_price = inputs["property_price"]
    down_payment = inputs["down_payment"]
    loan_rate = inputs["loan_rate"]
    loan_tenure = inputs["loan_tenure"]
    maintenance_rate = inputs["maintenance_rate"]
    annual_property_tax = inputs["annual_property_tax"]
    analysis_years = inputs["analysis_years"]

    stamp_duty_rate = inputs["stamp_duty_rate"]
    selling_cost_rate = inputs["selling_cost_rate"]

    rent = inputs["starting_rent"]
    rent_growth = scenario["rent_growth"]
    investment_return = scenario["investment_return"]
    property_appreciation = scenario["property_appreciation"]

    loan_amount = property_price - down_payment
    monthly_rate = loan_rate / 12
    total_months = loan_tenure * 12

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** total_months
    ) / ((1 + monthly_rate) ** total_months - 1)

    loan_balance = loan_amount
    property_value = property_price
    renter_corpus = down_payment

    stamp_duty_cost = property_price * stamp_duty_rate

    rows = []

    for year in range(1, analysis_years + 1):
        if loan_balance > 0:
            interest = loan_balance * loan_rate
            annual_emi = emi * 12
            principal = min(annual_emi - interest, loan_balance)
            loan_balance -= principal
        else:
            annual_emi = 0

        maintenance = property_value * maintenance_rate
        owning_cost = annual_emi + maintenance + annual_property_tax
        renting_cost = rent * 12

        surplus = owning_cost - renting_cost
        renter_corpus = renter_corpus * (1 + investment_return) + surplus

        property_value *= (1 + property_appreciation)
        rent *= (1 + rent_growth)

        owner_net_worth = property_value - loan_balance

        rows.append({
            "Year": year,
            "Owner Net Worth": owner_net_worth,
            "Renter Net Worth": renter_corpus
        })

    df = pd.DataFrame(rows)

    selling_cost = property_value * selling_cost_rate
    owner_exit_value = property_value - selling_cost - loan_balance - stamp_duty_cost

    return df, owner_exit_value, renter_corpus


