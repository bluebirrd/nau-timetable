from django.db import models


class Teacher(models.Model):
    """Teacher is a person giving lessons to students at university. He/she
    has a name (consisting of first_name, middle_name and last_name) and
    some position"""

    POSITIONS_LIST = (
        (0, 'аспірант'),
        (1, 'асистент'),
        (2, 'старший викладач'),
        (3, 'доцент'),
        (4, 'професор'),
    )

    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    position = models.IntegerField(null=True, choices=POSITIONS_LIST)


class Group(models.Model):
    """Group is a bunch of students which are taking courses together during
    their study. Group has a name (i.e. 'ТП-414'), degree (bachelors, masters,
    specialist) and type of education (full-time or remote)"""

    DEGREE_LIST = (
        (0, 'бакалавр'),
        (1, 'спеціаліст'),
        (2, 'магістр'),
    )
    TYPE_LIST = (
        (0, 'денна'),
        (1, 'заочна'),
    )

    name = models.CharField(max_length=6)
    degree = models.IntegerField(null=False, choices=DEGREE_LIST)
    type = models.IntegerField(null=False, choices=TYPE_LIST)


class Subject(models.Model):
    """Subject is a discipline students are learning at university. It has a
    name and short_name"""

    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=140)


class Building(models.Model):
    """Building is place where students take some (or all) of their lessons. It
    has a name and coordinates defined by latitude and longitude"""

    name = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Room(models.Model):
    """Room is a place inside the building where students have their lessons.
    It has a name and some number of building"""

    name = models.CharField(max_length=5)
    building = models.ForeignKey('Building')


class Lesson(models.Model):
    """
    Lesson is 95-minute block dedicated to studying a particular subject. It
    has a number (from 1 to 6), happens at some day of week (Monday to
    Saturday, in DB represented as 1 to 6), week (1st or 2nd), type (lecture,
    practice or lab), subject, teacher, groups (can be 1 or several), and room
    """

    NUMBER_LIST = (
        (1, '1 пара'),
        (2, '2 пара'),
        (3, '3 пара'),
        (4, '4 пара'),
        (5, '5 пара'),
        (6, '6 пара'),
    )
    DAY_LIST = (
        (1, 'понеділок'),
        (2, 'вівторок'),
        (3, 'середа'),
        (4, 'четвер'),
        (5, 'п\'ятниця'),
        (6, 'субота'),
    )
    TYPE_LIST = (
        (0, 'лекція'),
        (1, 'практика'),
        (2, 'лабораторна'),
    )
    SUBGROUP_LIST = (
        (1, '1 підгрупа'),
        (2, '2 підгрупа'),
    )

    number = models.IntegerField(null=False, choices=NUMBER_LIST)
    day = models.IntegerField(null=False, choices=DAY_LIST)
    week = models.BooleanField()
    type = models.IntegerField(null=True, choices=TYPE_LIST)
    subject = models.ForeignKey('Subject')
    teacher = models.ForeignKey('Teacher')
    groups = models.ManyToManyField('Group')
    subgroup_num = models.IntegerField(null=True, default=None,
                                       choices=SUBGROUP_LIST)
    room = models.ForeignKey('Room')
