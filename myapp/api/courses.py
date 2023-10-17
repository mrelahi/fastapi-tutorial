import fastapi
from api.crud.courses import *
from db.database import get_db
from fastapi import Depends, HTTPException
from schemas.course import Course, CourseCreate
from sqlalchemy.orm import Session

router = fastapi.APIRouter(tags=["courses"])


@router.get("/courses/", response_model=list[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses/",response_model=CourseCreate)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)


@router.get("/courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.put("/courses/{course_id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{course_id}")
async def delete_course():
    return {"courses": []}





