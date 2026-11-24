# Just a sandbox where I learn Python + fastAPI

## Notes
- If the route has dynamic path name, and the handler function has the same name, fastapi consider that argument to be a Path param
- If the argument is missing from path, it's considered as Query param
- if the argument is a pydentic model, it's considered as request body
- if the argument is a pydentic model, but wrapped into Annotate with Query(), FastAPI consider it as a query params and automatically splits into singular props

## TODOs
- Refactor the architecture to have this structure.
```
src/
  routes/students.py
  schemas/student.py
  services/student_service.py
  models/student.py
```