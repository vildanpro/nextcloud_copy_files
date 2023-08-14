from db import Session, OcFilecacheModel


with Session() as session:
    filtered_rows = session.query(OcFilecacheModel).filter(OcFilecacheModel.path.like('%groupfolders/trash/28/%')).all()

print(filtered_rows)