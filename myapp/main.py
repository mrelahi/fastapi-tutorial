from fastapi import FastAPI
from api import users, courses, sections
from db.database import engine,get_db
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    description="managing students and courses",
    contact={
        "name": "Mahdi",
        "email": "elahi25084@gmail.com",
    }
)


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)