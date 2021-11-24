import schemas
import models
from fastapi import FastAPI, Depends, status, HTTPException, File, UploadFile
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import desc

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

@app.post('/Create/Register', status_code = status.HTTP_201_CREATED, tags=['Create All'])
def create_account(request: schemas.user2, db : Session = Depends(get_db)):
    newaccount = models.Register( username=request.username, password=request.password,
                                  name=request.name, gender=request.gender, email=request.email, phone=request.phone )
    db.add(newaccount)
    db.commit()
    db.refresh(newaccount)

    return newaccount

@app.post('/Create/Box', status_code = status.HTTP_201_CREATED, tags=['Create All'])
async def create_box(request: schemas.isopodbox , db : Session = Depends(get_db)):

    newbox = models.Detailsbox( Namebox=request.Namebox, Typeisopod=request.Typeisopod,
                                  Temperature=request.Temperature, Humidity=request.Humidity )
    db.add(newbox)
    db.commit()
    db.refresh(newbox)

    return newbox

@app.post('/Create/Monitor', status_code = status.HTTP_201_CREATED, tags=['Create All'])
async def create_monitor(request: schemas.Monitor , db : Session = Depends(get_db)):

    newmonitor = models.ShowMonitor(Name=request.Name, Size=request.Size, Age=request.Age, Detail=request.Detail )

    db.add(newmonitor)
    db.commit()
    db.refresh(newmonitor)

    return newmonitor

@app.post('/Create/Inputimges', status_code = status.HTTP_201_CREATED, tags=['Create All'])
async def create_imges(image: UploadFile = File(...), db : Session = Depends(get_db)):

    file_location = f"imageUpload/{image.filename}"

    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())

    SendDB = models.Imagesave(Namepic = file_location)

    db.add(SendDB)
    db.commit()
    db.refresh(SendDB)

    return dict(ret=0, msg="Complete", data={"info": f"file '{image.filename}' saved at '{file_location}'"})


@app.post('/Check/Login', status_code = status.HTTP_201_CREATED, tags=['Check Login'])
async def CheckUP(request : schemas.Check , db : Session = Depends(get_db)):

            CheckUser = db.query(models.Register).filter(models.Register.username == request.username).first()

            if not CheckUser:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                        detail=f"Check Username and Password not found")

            if(CheckUser.password == request.password):
                return dict(ret = 0, msg = "Successful CheckUser")
            else:
                return dict(ret = -1, msg = "Fail CheckUser")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

@app.put('/Update/Register', status_code = status.HTTP_202_ACCEPTED, tags=['Update All'])
def update(request:schemas.user ,db : Session = Depends(get_db)):
    blogs = db.query(models.Register).filter(models.Register.id == request.id).first()

    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {request.id} not found")

    if blogs:
        if hasattr(blogs, 'username'):
                setattr(blogs, 'username', request.username)
        if hasattr(blogs, 'password'):
                setattr(blogs, 'password', request.password)
        if hasattr(blogs, 'name'):
                setattr(blogs, 'name', request.name)
        if hasattr(blogs, 'email'):
                setattr(blogs, 'email', request.email)
        if hasattr(blogs, 'phone'):
                setattr(blogs, 'phone', request.phone)

        db.commit()
        db.refresh(blogs)

    return 'updated'

@app.put('/Update/Box', status_code = status.HTTP_202_ACCEPTED, tags=['Update All'])
async def updatebox(request:schemas.isopodbox2 ,db : Session = Depends(get_db)):
    blogs = db.query(models.Detailsbox).filter(models.Detailsbox.id == request.id).first()

    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {request.id} not found")

    if blogs:
        if hasattr(blogs, 'Typeisopod'):
                setattr(blogs, 'Typeisopod', request.Typeisopod)
        if hasattr(blogs, 'Temperature'):
                setattr(blogs, 'Temperature', request.Temperature)
        if hasattr(blogs, 'Humidity'):
                setattr(blogs, 'Humidity', request.Humidity)


        db.commit()
        db.refresh(blogs)

    return 'updated'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

@app.get('/Show/Register', tags=['Show Register'])
def allDB(db : Session = Depends(get_db)):
    blogs = db.query(models.Register).all()

    return blogs

@app.get('/Show/Register/{id}', status_code = 200, tags=['Show Register'])
def show_id(id, db : Session = Depends(get_db),):
    blogs = db.query(models.Register).filter(models.Register.id == id).first()
    if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")

    return blogs

@app.get('/Show/Register/Last Record', tags=['Show Register'])
def show_last(db : Session = Depends(get_db)):
    blogs = db.query(models).order_by(models.Register.desc()).first()

    return blogs

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.get('/Show/IsopodBox', tags=['Show Isopod Box'])
def allDetailBox(db : Session = Depends(get_db)):
    blogs = db.query(models.Detailsbox).all()

    return blogs

@app.get('/Show/Monitor', tags=['Show Monitor'])
def allDetailMonitor(db : Session = Depends(get_db)):
    blogs = db.query(models.ShowMonitor).all()

    return blogs

@app.get('/Show/Image', tags=['Show NameImage'])
def allNameImage(db : Session = Depends(get_db)):
    blogs = db.query(models.Imagesave).all()

    return blogs

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.get('/Show/DataT', tags=['Show Data'])
def allData(db : Session = Depends(get_db)):
    blogs = db.query(models.GetdataT).all()

    return blogs

@app.get('/Show/DataT/One', tags=['Show Data'])
def show_last(db : Session = Depends(get_db)):
    blogs = db.query(models).order_by(models.GetdataT.desc()).first()

    return blogs


@app.get('/Show/DataH', tags=['Show Data'])
def allData(db : Session = Depends(get_db)):
    blogs = db.query(models.GetdataH).all()

    return blogs

@app.get('/Show/DataH/One', tags=['Show Data'])
def show_last(db : Session = Depends(get_db)):
    blogs = db.query(models).order_by(models.GetdataH.desc()).first()

    return blogs

@app.get('/Show/DataSTFA', tags=['Show Data'])
def allData(db : Session = Depends(get_db)):
    blogs = db.query(models.GetdataSTFA).all()

    return blogs

@app.get('/Show/DataSTFA/One', tags=['Show Data'])
def show_last(db : Session = Depends(get_db)):
    blogs = db.query(models).order_by(models.GetdataSTFA.desc()).first()

    return blogs

@app.get('/Show/DataSTFG', tags=['Show Data'])
def allData(db : Session = Depends(get_db)):
    blogs = db.query(models.GetdataSTFG).all()

    return blogs

@app.get('/Show/DataSTFG/One', tags=['Show Data'])
def show_last(db : Session = Depends(get_db)):
    blogs = db.query(models).order_by(models.GetdataSTFG.desc()).first()

    return blogs


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
