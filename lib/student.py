#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    
    def learn(self, topic):
        # Add the provided string to the student's self.knowledge list
        self.knowledge.append(topic)