import uvicorn 

if __name__ == "__main__":
    uvicorn.run(
        "src.main.server.server:app",
        host='localhost',
        port=3001,
        reload=True
    )