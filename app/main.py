import uvicorn
from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)

from app.modules.employees.views import router as employee_router
from app.modules.divisions.views import router as division_router
from app.modules.job.views import router as job_router
from app.modules.positions.views import router as position_router

app = FastAPI()

app.include_router(employee_router)
app.include_router(division_router)
app.include_router(job_router)
app.include_router(position_router)


@app.get('/home')
def root():
    return {
        'name': '9LabApi',
        'version': '1.0.0',
        'swagger': '/docs'
    }


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, host='0.0.0.0', reload=True, debug=True)
