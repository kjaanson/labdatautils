
import pandas as pd

def vs_control(df,control="DMSO", norm_col="fluc"):
    """Normaliseerib katseandmed kontroll grupi vastu. Väärtused võtab `norm_col` tulbast."""
    ndf=df.groupby(["Konstruktid","Treatments"]).mean().reset_index()
    konstruktid=set(ndf.set_index("Konstruktid").index)
    dfs=[]
    for konstrukt in konstruktid:
        df=ndf.set_index("Konstruktid").ix[konstrukt].reset_index()
        df["vs {}".format(control)]=df[norm_col]/float(df[df.Treatments==control][norm_col])
        dfs.append(df)
    return pd.concat(dfs)