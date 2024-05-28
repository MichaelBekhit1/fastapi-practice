# fastapi-practice

## Setup


1. Copied 'First steps' code to main.py

2. Run from bash with live reload with:

`
python -m uvicorn main:app --reload
`

3. Activated the venv after:

`
echo "# fastapi-practice" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin [https://github.com/MichaelBekhit1/fastapi-practice.git]
git push -u origin main
`

4. Tutorial from [https://www.youtube.com/watch?v=cbASjoZZGIw] for basic set of routes

5. Containerise with Docker. In future can test disabling venv to disable python only dependencies and leave other structures active in container?

## Tips

1. "FastApi is typed e.g. I can require id: int" - information given by tutor but it shows in documentation for pydantic.basemodel
2. pydantic basemodel has class methods that create, manipulate and validate instances of the Model class.



