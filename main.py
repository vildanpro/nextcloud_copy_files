from db import Session, OcFilecacheModel


filter_string = '%groupfolders/trash/28/%'

with Session() as session:
    filtered_rows = session.query(OcFilecacheModel).filter(OcFilecacheModel.path.like(filter_string)).all()

print(filtered_rows)