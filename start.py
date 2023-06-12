#!/usr/bin/env python3

import uvicorn

class App:
     ...

app = App()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
