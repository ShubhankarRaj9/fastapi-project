from fastapi import FastAPI
#chapter-00
app = FastAPI()

@app.get('/') # path operation decorator
def read_root(): # path operation function
    return {'data':{'name' : 'Shubhankar'}}

@app.get('/about')
def read_root():
    return {'data':'about page'}
#chapter-01
myapp = FastAPI()

@myapp.get('/')
def index():
    return {'data':'blog list'}

@myapp.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished-blogs'}

@myapp.get('/blog/{id}')
def show(id:int):
    # defining path parameter 'id' of type int
    # fetch blog with id = id
    return {'data':id}

@myapp.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data':{'comment-1','comment-2'}}

# chapter-02
from typing import Optional

myapp = FastAPI()

@myapp.get('/blog')
def index(limit=10,published:bool=True, sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:   
        return {'data':f'{limit} blogs from the db'}

@myapp.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished-blogs'}

@myapp.get('/blog/{id}')
def show(id:int):
    # defining path parameter 'id' of type int
    # fetch blog with id = id
    return {'data':id}


@myapp.get('/blog/{id}/comments')
def comments(id,limit=10):
    # fetch comments of blog with id = id
    return {'data':{'comment-1','comment-2'}}

# chapter-03
from pydantic import BaseModel
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


app = FastAPI()


@app.post("/blog")
def create_blog(blog: Blog):
    return {'data':f'blog is created with title as {blog.title}'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)