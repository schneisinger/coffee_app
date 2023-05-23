import uvicorn

class App:
     ...

app = App()

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, log_level="info")

# import re
# import sys
# from uvicorn.main import main

# if __name__ == '__main__':
#     sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
#     sys.exit(main())
