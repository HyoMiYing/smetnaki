from django.db import models

from datetime import datetime

DNEVI_V_MESECU_CHOICES = [
    ('1.', '1.'),
    ('2.', '2.'),
    ('3.', '3.'),
    ('4.', '4.'),
    ('5.', '5.'),
    ('6.', '6.'),
    ('7.', '7.'),
    ('8.', '8.'),
    ('9.', '9.'),
    ('10.', '10.'),
    ('11.', '11.'),
    ('12.', '12.'),
    ('13.', '13.'),
    ('14.', '14.'),
    ('15.', '15.'),
    ('16.', '16.'),
    ('17.', '17.'),
    ('18.', '18.'),    
    ('19.', '19.'),
    ('20.', '20.'),    
    ('21.', '21.'),
    ('22.', '22.'),    
    ('23.', '23.'),
    ('24.', '24.'),
    ('25.', '25.'),
    ('26.', '26.'),
    ('27.', '27.'),    
    ('28.', '28.'),
    ('29.', '29.'),    
    ('30.', '30.'),
    ('31.', '31.'),
]

MESECI_CHOICES = [
    ('JAN', 'Januar'),
    ('FEB', 'Februar'),
    ('MAR', 'Marec'),
    ('APR', 'April'),
    ('MAJ', 'Maj'),
    ('JUN', 'Junij'),
    ('JUL', 'Julij'),
    ('AVG', 'Avgust'),
    ('SEP', 'September'),
    ('OKT', 'Oktober'),
    ('NOV', 'November'),
    ('DEC', 'December'),
]

URA_CHOICES = [
    ('12h', '12h'),
    ('13h', '13h'),
    ('14h', '14h'),
    ('15h', '15h'),
    ('16h', '16h'),
    ('17h', '17h'),
    ('18h', '18h'),
    ('19h', '19h'),
    ('20h', '20h'),
    ('21h', '21h'),
    ('22h', '22h'),
    ('23h', '23h'),
    ('24h', '24h'),
]

class Koncert(models.Model):
    concert_venue = models.CharField(max_length=40)
    concert_ticket_price = models.CharField(max_length=3)
    concert_date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.concert_venue