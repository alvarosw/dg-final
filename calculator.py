def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    """
    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    coverage = 0

    # Dicionário com os descontos por tipo de tarifa e consumo
    discount_dict = {
        "Residencial": {
            "< 10.000 kWh": 0.18,
            ">= 10.000 kWh e <= 20.000 kWh": 0.22,
            "> 20.000 kWh": 0.25,
        },
        "Comercial": {
            "< 10.000 kWh": 0.16,
            ">= 10.000 kWh e <= 20.000 kWh": 0.18,
            "> 20.000 kWh": 0.22,
        },
        "Industrial": {
            "< 10.000 kWh": 0.12,
            ">= 10.000 kWh e <= 20.000 kWh": 0.15,
            "> 20.000 kWh": 0.18,
        },
    }

    # Dicionário com os percentuais de cobertura por consumo
    coverage_dict = {
        "< 10.000 kWh": 0.9,
        ">= 10.000 kWh e <= 20.000 kWh": 0.95,
        "> 20.000 kWh": 0.99,
    }

    # Cálculo do consumo médio
    consumption_average = sum(consumption) / len(consumption)

    # Obtenção da faixa de consumo baseado no consumo médio
    if consumption_average < 10000:
        consumption_range = "< 10.000 kWh"
    elif consumption_average <= 20000:
        consumption_range = ">= 10.000 kWh e <= 20.000 kWh"
    else:
        consumption_range = "> 20.000 kWh"

    applied_discount = discount_dict[tax_type][consumption_range]
    coverage = coverage_dict.get(consumption_range)
    # Obtendo o percentual de cobertura baseado no consumo médio

    # Cálculo da economia mensal e anual
    monthly_savings = (
        distributor_tax * consumption_average * applied_discount * coverage
    )
    annual_savings = monthly_savings * 12

    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        applied_discount,
        coverage,
    )


if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial") == (
        1473.19,
        122.77,
        0.12,
        0.9,
    )

    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial") == (
        2295.32,
        191.28,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial") == (
        1405.56,
        117.13,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial") == (
        24591.16,
        2049.26,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial") == (
        32297.74,
        2691.48,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial") == (
        35776.75,
        2981.40,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial") == (
        60478.73,
        5039.89,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial") == (
        71602.56,
        5966.88,
        0.25,
        0.99,
    )

    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial") == (
        63832.12,
        5319.34,
        0.22,
        0.99,
    )

    print("Everything passed")
