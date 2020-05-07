from flask_marshmallow import Marshmallow

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class PaisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'area', 'populacao')

pais_schema = PaisSchema(many=False)
paises_schema = PaisSchema(many=True)
    