from fastapi import FastAPI
from routes.routerDepartment import ApiRouter_Department
from routes.routerKelas import ApiRouter_Kelas
from routes.routerStudent import ApiRouter_Student

app = FastAPI(
    title="Belajar FastAPI",
    description="Belajar FastAPI",
    docs_url="/swgr"
)

app.include_router(ApiRouter_Department)
app.include_router(ApiRouter_Kelas)
app.include_router(ApiRouter_Student)