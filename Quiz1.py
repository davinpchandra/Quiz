#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:17:30 2019

@author: davinpc
"""

#1. Inheritance
# a. The Parent Class is Spell and the Child Class is Accio and Confundo.
# b. The code will produce an error.
# c. The Confundo's get_description will be called because Confundo class has its own get_description method.
# d.
class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation 
        
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description() 
    
    def get_description(self):
        return 'No description' 
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm') 
        
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
    
    def study_spell(spell):
        print(spell)

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    
    # This is the answer for d.
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'
    
    def study_spell(spell): 
        print(spell)

spell = Accio() 
spell.execute() 
spell.study_spell()
spell2 = Confundo()
spell2.study_spell()
