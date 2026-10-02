from fastapi  import FastAPI,Request
from mockData import products
from dtos import ProductDTO
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
    ##different types of HTTP Methods
@app.post("/create_products")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return{
        "status":"product created Successfully....", "data":products
    }
@app.put("/update_product/{product_id}")
def update_product(product_id:int, product_data:ProductDTO):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return{
                "status":"product updated successfully", "product":product_data
            }
            return{
                "error":"Product not found"
            }

@app.delete("/delete_product/{product_id}")         
def delete_product(product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product=products.pop(index)
            return{
                "status":"product deleted successfully"
            }
    return{
        "error":"Product not found"
    }   
            