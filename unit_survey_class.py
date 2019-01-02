#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AnonymousSurvey():
    def __init__(self, question): 
        """存储一个问题 并为存储     """ 
        self.question = question 
        self.responses = []

    def show_question(self): 
        """显示调查问 """ 
        print(self.question)

    def store_response(self, new_response): 
        """存储单 调查  """ 
        self.responses.append(new_response)

    def show_results(self): 
        """显示  到的所有  """ 
        print("Survey results:") 
        for response in self.responses:
            print('- ' + response)