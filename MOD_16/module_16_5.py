from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


users = [
    User(id=1, username='UrbanUser', age=24),
    User(id=2, username='UrbanTest', age=22),
    User(id=3, username='Capybara', age=60)
]



@app.get('/')
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', context={'request': request, 'users': users})



@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    user = next((u for u in users if u.id == user_id), None)
    if user:
        return templates.TemplateResponse('users.html', context={'request': request, 'user': user})
    else:
        raise HTTPException(status_code=404, detail="User was not found")



@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> User:
    user_id = len(users) + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user



@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")



@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")


