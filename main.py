from fastapi import FastAPI
from routes.routerDepartment import ApiRouter_Department
from routes.routerGrade import ApiRouter_Grade
from routes.routerKelas import ApiRouter_Kelas

app = FastAPI(
    title="Belajar FastAPI",
    description="Belajar FastAPI",
    docs_url="/swgr"
)

app.include_router(ApiRouter_Department)
app.include_router(ApiRouter_Grade)
app.include_router(ApiRouter_Kelas)