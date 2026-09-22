from fastapi  import FastAPI,Request
from mockData import products
app = FastAPI()
@app.get("/")
def home():
    return "Welcome to FastAPI series"
@app.get("/products")
def get_products():
    return products
##Path parameters...
@app.get("/products/{product_id}")
def get_one_product(product_id:int):
    ##return{
     ##   "id":product_id
   ## }
    for oneProduct in products:
     if oneProduct.get("id") == product_id:
        return oneProduct
    return {
        "error":"Product not found"
    }
@app.get("/greet")
##def greet_user(name:str, age:int):
   ## return{
       ## "greet": f"hello {name}, your age is{age}"
   ##     }
def greet_user(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return{
        "greet": f"hello {query_params.get("name")}, Your age is {query_params.get("age")}"
        
    }