from sqlalchemy import create_engine
from sqlalchemy import Column, VARCHAR, INTEGER, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from  config import DATABASE


engine = create_engine(URL.create(**DATABASE), echo=False, pool_size=10, max_overflow=10)
Base = declarative_base()


class OcFilecacheModel(Base):
    __tablename__ = 'oc_filecache'
    fileid = Column(BIGINT, primary_key=True)
    storage = Column(INTEGER)
    path = Column(VARCHAR)
    path_hash = Column(VARCHAR)
    parent = Column(INTEGER)
    name = Column(VARCHAR)
    mimetype = Column(INTEGER)
    size = Column(INTEGER)
    mtime = Column(INTEGER)
    storage_mtime = Column(INTEGER)
    encrypted = Column(INTEGER)
    unencrypted_size = Column(INTEGER)
    etag = Column(INTEGER)
    permissions = Column(INTEGER)
    checksum = Column(VARCHAR)

    def as_dict(self):
        new_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        new_dict_with_hierarchy = {
            'fileid': new_dict['fileid'],
            'storage': new_dict['storage'],
            'path': new_dict['path'],
            'path_hash': new_dict['path_hash'],
            'parent': new_dict['parent'],
            'name': new_dict['name'],
            'mimetype': new_dict['mimetype'],
            'size': new_dict['size'],
            'mtime': new_dict['mtime'],
            'storage_mtime': new_dict['storage_mtime'],
            'encrypted': new_dict['encrypted'],
            'unencrypted_size': new_dict['unencrypted_size'],
            'etag': new_dict['etag'],
            'permissions': new_dict['permissions'],
            'checksum': new_dict['checksum']
        }
        return new_dict_with_hierarchy


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
