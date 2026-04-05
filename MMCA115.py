import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Simulation Function
def simulate_users(initial_users, growth_rate, max_users, days):
    users = initial_users
    users_list = []

    for t in range(days):
        growth = growth_rate * users * (1 - users / max_users)  # Logistic Growth
        users += growth
        users_list.append(users)

    return users_list


st.set_page_config(page_title="AI App User Growth Model", layout="centered")

st.title("🤖 AI App User Growth Simulator")
st.write("Model: Exponential + Logistic Growth")

# Sidebar Inputs
st.sidebar.header("⚙️ Input Parameters")

initial_users = st.sidebar.slider("Initial Users", 100, 10000, 500)
growth_rate = st.sidebar.slider("Daily Growth Rate", 0.01, 0.5, 0.1)
max_users = st.sidebar.slider("Maximum User Capacity", 1000, 100000, 10000)
days = st.sidebar.slider("Simulation Days", 30, 365, 180)

# Overview
st.markdown("""
## 📌 Project Overview

This model predicts *AI app user adoption* over time using:

- 📈 Exponential Growth (early adoption phase)
- 📊 Logistic Growth (market saturation phase)

It helps in:

- Forecasting user growth  
- Planning infrastructure and scaling  
- Avoiding overloading servers  
""")

# Simulation
user_data = simulate_users(initial_users, growth_rate, max_users, days)

# Graph
st.subheader("📈 User Growth Over Time")

fig, ax = plt.subplots()
ax.plot(range(days), user_data, color='purple')
ax.set_xlabel("Days")
ax.set_ylabel("Number of Users")
st.pyplot(fig)

# Data Table
st.subheader("📊 User Data Table")

df = pd.DataFrame({
    "Day": list(range(days)),
    "Number of Users": np.round(user_data, 0).astype(int)
})

st.dataframe(df, use_container_width=True)

# Insights
current_users = user_data[-1]
utilization = current_users / max_users

st.subheader("🔍 Key Insights")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
👥 Current Users  
{current_users:.0f}
""")

with col2:
    st.info(f"""
⚙️ Utilization Ratio  
{utilization:.2f}
""")

# Interpretation
if utilization < 0.5:
    status = "Early Adoption"
elif utilization < 0.8:
    status = "Growing"
elif utilization < 1:
    status = "Near Saturation"
else:
    status = "Over Capacity"

st.success(f"""
💡 Interpretation:

* Utilization < 0.5 → Early adoption  
* 0.5 - 0.8 → Growing user base  
* 0.8 - 1 → Near saturation  
* >1 → Capacity exceeded  

Current status: *{status}*
""")

# Expansion Suggestion
st.subheader("🚀 Scaling Planning")

if utilization > 0.8:
    st.warning("⚠️ User base nearing system limits. Consider scaling infrastructure.")
elif utilization > 1:
    st.error("🚨 Users exceeded system capacity! Immediate scaling required.")
else:
    st.success("✅ Current system capacity is sufficient.")

# Mathematical Model
st.subheader("📘 Mathematical Model")

st.latex(r"U(t+1) = U(t) + r \cdot U(t) \cdot \left(1 - \frac{U(t)}{K} \right)")

st.markdown("""
*Where:*

* U(t) = Number of users at time t  
* r = Growth rate  
* K = Maximum user capacity  
""")

# Conclusion
st.subheader("📌 Conclusion")

st.write(f"""
🔹 User base grows rapidly initially (Exponential phase)  

🔹 Growth slows as it approaches system limits (Logistic phase)  

🔹 Final User Count: *{current_users:.0f}*  

🔹 Maximum Capacity: *{max_users}*  

🔹 System Status: *{status}*

👉 This model helps AI app developers plan scaling and infrastructure efficiently.
""")