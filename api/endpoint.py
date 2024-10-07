from fastapi import APIRouter, HTTPException, Query, Depends
from google.cloud import bigquery
from fastapi.security import HTTPBasicCredentials
from .security import verificar_usuario

router = APIRouter()

client = bigquery.Client()

TABLES = {
    "ventas": "deimox-dw.pruebas.ventas",
    "arriendos": "deimox-dw.pruebas.arriendos",
}

@router.get("/datos", response_description="Obtener datos de BigQuery")
async def obtener_datos(
    tabla: str = Query(..., description="Nombre de la tabla a consultar (ventas, arriendos)"),
    limit: int = Query(10, ge=1, description="Número máximo de resultados a devolver"),
    credentials: HTTPBasicCredentials = Depends(verificar_usuario)  # Requiere autenticación
):
    """
    Obtiene datos de BigQuery de la tabla especificada con un límite.

    - **tabla**: Nombre de la tabla a consultar (ventas o arriendos).
    - **limit**: Número máximo de resultados a devolver. Por defecto es 10.
    """
    try:
        if tabla not in TABLES:
            raise HTTPException(status_code=400, detail="Tabla no válida. Usa 'ventas' o 'arriendos'.")

        nombre_tabla = TABLES[tabla]

        query = f"SELECT * FROM `{nombre_tabla}` LIMIT @limit"
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("limit", "INT64", limit)
            ]
        )

        query_job = client.query(query, job_config=job_config)


        results = query_job.result()

        datos = [dict(row) for row in results]

        return {"data": datos}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))