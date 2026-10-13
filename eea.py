import pandas as pd


def analyze_energy(appliances, rate=7):
    """
    Calculate energy consumption and cost
    for each appliance.
    """

    df = pd.DataFrame(appliances)

    # Calculate energy in kWh
    df["Energy"] = (
        df["Power"] * df["Hours"] / 1000
    )

    # Calculate electricity cost
    df["Cost"] = df["Energy"] * rate

    # Total consumption
    total_energy = df["Energy"].sum()
    total_cost = df["Cost"].sum()

    # Highest energy-consuming appliance
    highest = df.loc[df["Energy"].idxmax()]

    # Energy-saving recommendations
    recommendations = []

    for _, row in df.iterrows():

        if row["Energy"] > 3:
            recommendations.append(
                f"Reduce usage of {row['Appliance']} "
                f"to save electricity."
            )

    if not recommendations:
        recommendations.append(
            "Your energy consumption is within "
            "the configured threshold."
        )

    return {
        "data": df,
        "total_energy": round(total_energy, 2),
        "total_cost": round(total_cost, 2),
        "highest": highest["Appliance"],
        "recommendations": recommendations
    }