from dataclasses import dataclass, field#significa campo
from hashlib import sha256

@dataclass
class Persona:
    nombre: str
    dni: str


@dataclass   
class Estudiante(Persona):
    ru: str

    def __hash__(self):
        return int(sha256(self.ru.encode()).hexdigest(), 16) #encode convierte a bites, la funcion hash necesita un entero


@dataclass
class Docente(Persona):
    sueldo: float
    titular: bool


@dataclass
class Auxiliar(Estudiante):
    sueldo: float
    nro_item: int


@dataclass
class Paralelo: #paralelo o grupo
    sigla: str
    docente: Docente
    #auxiliar: Optional[Auxiliar] = None # es opcional no es necesario para que funcione agregacion, puede ser Auxiliar como puede ser un None - pre python 3.9 from typing import Optional
    auxiliar: Auxiliar | None = None
    estudiantes: list[Estudiante] = field(default_factory=list)
    notas: list[int] = field(default_factory=list)


@dataclass
class Materia:
    nombre: str
    sigla: str
    paralelos: list[Paralelo] = field(default_factory=list)



