from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
import io

from app.pipeline import (
    composicao_base,
    tipagem_df,
    target_check,
    feature_engineering
)

app = FastAPI(title="Customer Purchase API", version="1.0")

@app.get("/")
async def root():
    return {"message": "API está funcionando!"}


@app.post("/processar/")
    
async def processar_csv(file: UploadFile = File(...)):
    try:
        content = await file.read()
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))

        composicao = composicao_base(df)
        tipagem = tipagem_df(df)
        inconsistencias = target_check(df)
        df_processado = feature_engineering(df)

        return {
            "composicao_base": composicao,
            "tipagem_df": tipagem,
            "inconsistencias": inconsistencias,
            "amostra_dados": df_processado.head().to_dict(orient="records")
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
