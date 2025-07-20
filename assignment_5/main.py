from fastapi import FastAPI
from . import models, database
from .controllers import sandwich_controller, resource_controller, recipe_controller, order_controller

# Create tables if they don't exist
models.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI app
app = FastAPI(
    title="Sandwich Maker API",
    description="API for managing sandwiches, resources, recipes, and orders.",
    version="1.0.0"
)

# Include Sandwich routes
app.include_router(sandwich_controller.router)
app.include_router(resource_controller.router)
app.include_router(recipe_controller.router)
app.include_router(order_controller.router)


