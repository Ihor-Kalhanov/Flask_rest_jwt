from ma import ma


class CarSchema(ma.Schema):
    class Meta:
        fields = ("id", "brand", "year")
