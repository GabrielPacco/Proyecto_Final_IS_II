from backend.models.usuario import UsuariosModel

class AsistenteModel(UsuariosModel):
    def __init__(self, id_, nombre_, apellido_, correo_):
        UsuariosModel.__init__(self, id_, nombre_, apellido_, correo_)