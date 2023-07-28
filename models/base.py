#!/usr/bin/python3
"""
Classe Base Models de tous les models
Elle regroupe une classe de base qui serait une classe qui regroupera les proprietes et methode commune a tout les models. ELle fait donc gagner du temps en evitant les repetitions.
Tous les models qui seront cree vont herites de cette classe avant d'en disposer les fonction communes
Les models qui sont representes par des classes vont etre manipules en leur seur grace a un ORM (Object Relationship Manager) ici qui est sqlalchemy


Classe Base Models de tous les models
Elle regroupe une classe de base qui serait une classe qui regroupera les proprietes et methode commune a tout les models. ELle fait donc gagner du temps en evitant les repetitions.
Tous les models qui seront cree vont herites de cette classe avant d'en disposer les fonction communes
Les models qui sont representes par des classes vont etre manipules en leur seur grace a un ORM (Object Relationship Manager) ici qui est sqlalchemy


"""

from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from typing import Union
from pydantic import BaseModel
import os
import json
import models
#Base = declarative_base()

class Base(DeclarativeBase):
    """
    Instantier une classe de base qui herite de la classe DeclarativeBase permettant d'attributes des metadonnees indispensables pour la creation des tables de la base de donnee. Chaque Model represente une table
    """
    pass


class BaseModel:
    """
        La classe de Base de tous les models pour permettre une attribution des proprietes et methodes communes a toutes les classe
        ex :
            Id (Colonne commune a toutes les tables ici etant une propriete)
    """
    
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True )
    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False,
                            default=datetime.utcnow())
    updated_at : Mapped[datetime] = mapped_column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, props=None):
        """
        Instantiation d'un nouvel objet de la classe. Pour les model elle represente un objet de donnees
        :param props: dictionnaire reprensantant toute les valeur des proprites a donner au cours de la creation de cet nouvel objet. Elle est optionnel
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if props is not None:
            for key, value in props:
                setattr(self, key, value)
    
    def bm_update(self, name, value):
        """
            Methode permettant de Mettre a jour une propriete du model
        """
        setattr(self, name, value)
        #self.save()
    
    def save(self):
        """
            Enregistre l'object du model en cours de modification
            ie ajoute une nouvelle donnees a la table du model correspond
            Ici le self designant l'instance du model en cours
        """
        models.storage.new(self)
        models.storage.save()
    

class PyBaseModel(BaseModel):
    id : int
    created_at : Union[datetime, datetime.utcnow()] = datetime.utcnow()
