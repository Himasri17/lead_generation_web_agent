def calculate_score(lead):
    score = 0

    # Role Fit
    role_keywords = ["toxicology", "safety", "preclinical", "3d"]
    if any(keyword in lead["Title"].lower() for keyword in role_keywords):
        score += 30

    # Funding Intent
    if lead["Funding_Stage"] in ["Series A", "Series B", "Series C"]:
        score += 20

    # Technographic Fit
    if lead["Uses_InVitro_Tech"] == "Yes":
        score += 15

    # Open to New Methodologies
    if lead["Open_to_NAMs"] == "Yes":
        score += 10

    # Location Hub
    hubs = ["boston", "cambridge", "bay area", "basel", "london"]
    if any(hub in lead["Company_HQ"].lower() for hub in hubs):
        score += 10

    # Scientific Intent
    if lead["Recent_Publication"] == "Yes":
        score += 40

    return min(score, 100)
