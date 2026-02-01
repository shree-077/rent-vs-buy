from rvo import run_single_scenario

inputs = {
    "property_price": 90_00_000,
    "down_payment": 9_00_000,
    "loan_rate": 0.08,
    "loan_tenure": 15,
    "starting_rent": 25_000,
    "rent_growth": 0.10,
    "maintenance_rate": 0.005,
    "annual_property_tax": 10_000,
    "stamp_duty_rate": 0.07,
    "selling_cost_rate": 0.01,
    "analysis_years": 30
}

scenario = {
    "name": "Base",
    "investment_return": 0.11,
    "property_appreciation": 0.09,
    "rent_growth": 0.10
}

df, owner_final, renter_final = run_single_scenario(inputs, scenario)

print(df.head(3))
print(df.tail(3))
print("\nFINAL VALUES")
print("Owner:", round(owner_final))
print("Renter:", round(renter_final))

from plots import plot_net_worth
plot_net_worth(df, "Base")

