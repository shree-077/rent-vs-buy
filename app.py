import streamlit as st
from rvo import run_single_scenario
from plots import plot_net_worth

st.set_page_config(page_title="Rent vs Buy Calculator", layout="wide")

st.title("Rent vs Buy – Decision Tool")

st.sidebar.header("Property & Loan")
property_price = st.sidebar.number_input("Property Price (₹)", 50_00_000, 5_00_00_000, 90_00_000)
down_payment = st.sidebar.number_input("Down Payment (₹)", 0, property_price, 20_00_000)
loan_rate = st.sidebar.slider("Loan Interest (%)", 5.0, 12.0, 8.0) / 100
loan_tenure = st.sidebar.slider("Loan Tenure (Years)", 5, 30, 20)

st.sidebar.header("Rent")
starting_rent = st.sidebar.number_input("Monthly Rent (₹)", 5_000, 1_00_000, 20_000)
rent_growth = st.sidebar.slider("Rent Growth (%)", 3.0, 12.0, 10.0) / 100

st.sidebar.header("Returns")
investment_return = st.sidebar.slider("Investment Return (%)", 6.0, 15.0, 11.0) / 100
property_appreciation = st.sidebar.slider("Property Appreciation (%)", 2.0, 12.0, 6.0) / 100

st.sidebar.header("Costs")
maintenance_rate = st.sidebar.slider("Maintenance (% of value)", 0.5, 2.0, 1.0) / 100
annual_property_tax = st.sidebar.number_input("Annual Property Tax (₹)", 0, 50_000, 10_000)
stamp_duty_rate = st.sidebar.slider("Stamp Duty (%)", 5.0, 8.0, 7.0) / 100
selling_cost_rate = st.sidebar.slider("Selling Cost (%)", 1.0, 4.0, 2.0) / 100

analysis_years = st.sidebar.slider("Analysis Period (Years)", 5, 30, 20)

inputs = {
    "property_price": property_price,
    "down_payment": down_payment,
    "loan_rate": loan_rate,
    "loan_tenure": loan_tenure,
    "starting_rent": starting_rent,
    "rent_growth": rent_growth,
    "investment_return": investment_return,
    "property_appreciation": property_appreciation,
    "maintenance_rate": maintenance_rate,
    "annual_property_tax": annual_property_tax,
    "stamp_duty_rate": stamp_duty_rate,
    "selling_cost_rate": selling_cost_rate,
    "analysis_years": analysis_years
}

scenario = {
    "name": "Custom",
    "rent_growth": rent_growth,
    "investment_return": investment_return,
    "property_appreciation": property_appreciation
}

df, owner_final, renter_final = run_single_scenario(inputs, scenario)

st.subheader("Net Worth Comparison")
col1, col2 = st.columns(2)

col1.metric("Buy – Final Net Worth", f"₹{owner_final:,.0f}")
col2.metric("Rent + Invest – Final Net Worth", f"₹{renter_final:,.0f}")

st.subheader("Net Worth Over Time")
st.line_chart(df.set_index("Year"))

st.subheader("Want help applying this to your situation?")

st.write(
    "This calculator shows the math. "
    "If you want help interpreting the result or planning next steps, you can explore more here."
)

st.markdown(
    """
    <a href="https://shreemoney.in" target="_blank">
        <button style="
            background-color:#0f4c81;
            color:white;
            padding:10px 18px;
            border:none;
            border-radius:6px;
            font-size:16px;
            cursor:pointer;
        ">
            Visit ShreeMoney
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.write(
        "You can reach me directly."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <a href="tel:+917559161118">
            <button style="
                width:40%;
                background-color:#0f4c81;
                color:white;
                padding:12px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
            ">
                📞 Call
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <a href="https://wa.me/917559161118" target="_blank">
            <button style="
                width:40%;
                background-color:#25D366;
                color:white;
                padding:12px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
            ">
                💬 WhatsApp
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
