import pandas as pd
from collections import OrderedDict


def vs_control(df, control="DMSO", norm_col="fluc"):
    """Normaliseerib katseandmed kontroll grupi vastu. Väärtused võtab `norm_col` tulbast."""
    ndf = df.groupby(["Konstruktid", "Treatments"]).mean().reset_index()
    konstruktid = list(OrderedDict.fromkeys(ndf["Konstruktid"]))
    dfs = []
    for konstrukt in konstruktid:
        df = ndf.set_index("Konstruktid").ix[konstrukt].reset_index()
        df["vs {}".format(control)] = df[norm_col] / float(df[df.Treatments == control][norm_col])
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)
