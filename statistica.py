import pandas as pd
import scipy.stats as stats

# Gruppo 1
data_g1 = {
    "id_studente": ["RAINONE", "MANTOVANI", "SCARCHILLI", "LAZZARO", "MAGGIORE", "LA NOCE", "SPLENDIANI", "BIZZARRI"],
    "corrette": [18, 14, 15, 9, 9, 14, 15, 14],
    "sbagliate": [2, 6, 5, 11, 11, 6, 5, 6]
}

# Gruppo 2
data_g2 = {
    "id_studente": ["ASARO", "MANTOVANI", "SCARCHILLI", "LA NOCE", "SPLENDIANI", "RAINONE"],
    "corrette": [19, 20, 17, 19, 19, 18],
    "sbagliate": [1, 0, 3, 1, 1, 2]
}

# Creiamo i DataFrame
df1 = pd.DataFrame(data_g1)
df2 = pd.DataFrame(data_g2)

# Aggiungiamo colonne totali e percentuali
for df in [df1, df2]:
    df["totale"] = df["corrette"] + df["sbagliate"]
    df["percentuale"] = df["corrette"] / df["totale"] * 100

print("=== Statistiche Gruppo 1 ===")
print(df1.describe())
print("\n=== Statistiche Gruppo 2 ===")
print(df2.describe())

# T-test tra i due gruppi sulla percentuale corretta
t, p = stats.ttest_ind(df1["percentuale"], df2["percentuale"], equal_var=False)
print(f"\nT-test tra Gruppo 1 e Gruppo 2: t={t:.3f}, p={p:.4f}")

# Chi-quadro aggregato corrette/errate
tabella = pd.DataFrame({
    "corrette": [df1["corrette"].sum(), df2["corrette"].sum()],
    "sbagliate": [df1["sbagliate"].sum(), df2["sbagliate"].sum()]
}, index=["Gruppo1", "Gruppo2"])

chi2, p, dof, expected = stats.chi2_contingency(tabella)
print(f"\nChi-quadro su corrette/errate: chi2={chi2:.3f}, p={p:.4f}")
