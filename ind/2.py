# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# вывести имена совершеннолетних людей

def people(**kwargs):
    if kwargs:
        for name, age in kwargs.items():
            if age > 18:
                print(f"{name}: {age}")
    else:
        return None


if __name__ == "__main__":
    people(vova=6, sasha=19, kirill=35)
