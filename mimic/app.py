from fastapi import FastAPI, APIRouter

# Maybe create a function called load_routers or something that takes in the fast_api
# app and then appends all of the imported routers :shrug:
from mimic.controllers.status import router as status_router
from mimic.controllers.get import router as get_router
from mimic.controllers.manifests import router as manifest_router

app = FastAPI()

# Setup Testerozza System Routes
# The sys_router for is for Always ON System Routes
sys_router = APIRouter(prefix="/v1")

sys_router.include_router(manifest_router)
sys_router.include_router(status_router)


# Setup Mimic Routes.
# The mimic_router is the router that will handle all requests from a system under test (SUT) and echo's back the configured response
mimic_router = APIRouter()
mimic_router.include_router(get_router)

# Include the echo routes and system routes in the main application
app.include_router(sys_router)
app.include_router(mimic_router)
