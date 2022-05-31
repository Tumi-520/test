import uvicorn

# uvicorn config
# app     : The location of the fastapi root node
# host    : The host name that uvicorn is listening on
# port    : Listening port number
# workers : The number of threads used by multithreading
if __name__ == '__main__':
    uvicorn.run(app="app.main:server", host="127.0.0.1", port=8005, workers=1)
