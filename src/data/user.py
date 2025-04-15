class User:
    def __init__(self, first_name, last_name, email, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            address=Address.from_dict(data['address'])
        )


class Address:
    def __init__(self, line1, line2, city, postcode, country, region):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.postcode = postcode
        self.country = country
        self.region = region

    @classmethod
    def from_dict(cls, data):
        return cls(
            line1=data['line1'],
            line2=data['line2'],
            city=data['city'],
            postcode=data['postcode'],
            country=data['country'],
            region=data['region']
        )
