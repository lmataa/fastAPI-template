import uvicorn
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {"Hello" : "World"}

# path parameters
@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return{"component_id":component_id}


# query parameters
@app.get("/component/")
async def read_component(number:int, text:Optional[str]):
    return {"number":number, "text": text}

def main():
    uvicorn.run(app)

if __name__ == "__main__":
    main()
