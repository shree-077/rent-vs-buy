import matplotlib.pyplot as plt

def plot_net_worth(df, scenario_name):
    plt.figure()
    plt.plot(df["Year"], df["Owner Net Worth"], label="Buy (Net Worth)")
    plt.plot(df["Year"], df["Renter Net Worth"], label="Rent + Invest")
    plt.xlabel("Year")
    plt.ylabel("Net Worth (₹)")
    plt.title(f"Rent vs Buy – {scenario_name.capitalize()} Scenario")
    plt.legend()
    plt.grid(True)
    plt.show()
