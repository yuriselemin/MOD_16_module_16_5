from fastapi import FastAPI


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    user_id = str(max(int(k) for k in users.keys()) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'User {user_id} has been updated'
    else:
        return 'User not found'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f'User {user_id} has been deleted'
    else:
        return 'User not found'