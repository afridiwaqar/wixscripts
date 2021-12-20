# -*- coding: utf-8 -*-

import time
import csv
from StringIO import StringIO
from tempfile import TemporaryFile
import base64
import random
import string
import re
import pprint

import json
from json import loads
from dicttoxml import dicttoxml


def convert_paper_xml():

    questionsfile = "MGT_Subject.txt"
    
    file_obj_pointer = open(questionsfile, "r")
    subject = "Management Sciences and Project Management"
    test_title = "Entrance Test for Admission to MS Management Sciences and MS Project Management"
    position = 0
    op_position = 1
    test_description = "Entrance Test for Admission to MS Management Sciences and MS Project Management"
    xml_paper = subject + "_paper.xml"
    explanation = """SUBJECT"""

    xml_questions = """<?xml version="1.0" encoding="UTF-8" ?>
<tcexamquestions version="14.0.3">
	<header lang="en" date="2018-08-13 13:08:47">
	</header>
	<body>
		<module>
			<name>""" + str(test_title) + """</name>
			<enabled>true</enabled>
			<subject>
				<name>""" +str(subject) + """ </name>
				<description>""" + str(test_description) + """</description>
				<enabled>true</enabled>
"""

    line_read = file_obj_pointer.readline()
    recent_question_dict = {}
    mcq_questions_found = []
    pp = pprint.PrettyPrinter(indent=4)
    while line_read != "":
    
    	if op_position > 4:
	    	op_position = 1
	    	
        split_result = line_read.split('\r')
#        print "___________________________________", split_result
        if split_result:
            if len(split_result) > 2:
                for split_line in split_result:
                    print 'File Line Split'
                    question_match_found = re.search('^[Q]?[0-9]+\.[ ]?', split_line)
                    
                    if question_match_found:
                        '''Save the previous question'''
                        if recent_question_dict:
                            if 'question_options' in recent_question_dict:
                                if recent_question_dict['question_options']:
                                    if len(recent_question_dict['question_options']) > 1:
                                        mcq_questions_found.append(recent_question_dict)
#                                        print "111111111111111111111111111111", mcq_questions_found
#                                        pp.pprint(recent_question_dict)
                        recent_question_dict = {'file_line': split_line, 'question_text': split_line[len(question_match_found.group()):].strip(), 'question_options': []}
                    else:
                        question_option_match_found = re.search('^\(?[aAbBcCdDeEfF]\.?\)?[ ]?', split_line)

                        if question_option_match_found:
                            if recent_question_dict:
                                if 'question_options' in recent_question_dict:
                                    correct_flag = False
                                    option_correct_match_found = re.search('.+\*$', split_line.strip())
                                    if option_correct_match_found:
                                        correct_flag = True
#                                    print "222222222222222222222222222", question_options
                                    recent_question_dict['question_options'].append({'file_line': split_line, 'option_text': split_line[len(question_option_match_found.group()):].strip().replace('*', ''), 'correct': correct_flag})
#        print 'File Read'
        question_match_found = re.search('^[Q]?[0-9]+\.[ ]?', line_read)
#        op_position = 0
        if question_match_found:
            '''Save the previous question'''
            if recent_question_dict:
                if 'question_options' in recent_question_dict:
                    if recent_question_dict['question_options']:
                        if len(recent_question_dict['question_options']) > 1:
                            mcq_questions_found.append(recent_question_dict)
#                            print "333333333333333333333333333", recent_question_dict
#                            pp.pprint(recent_question_dict)
#            recent_question_dict = {'file_line': line_read, 'question_text': line_read[len(question_match_found.group()):].strip(), 'question_options': []}
            recent_question_dict = {'question_text': line_read[len(question_match_found.group()):].strip(), 'question_options': []}
#            print "WWWWWWWWWWWWWWWWWWWWWWW" + str(recent_question_dict['question_text'])
            position+=1
            #op_position += 1
            xml_questions += """
					</question>
        """ 
            xml_questions += """
					<question>
						<enabled>true</enabled>
						<type>single</type>
						<difficulty>1</difficulty>
						<position>""" + str(position)+ """</position>
						<timer>0</timer>
						<fullscreen>false</fullscreen>
						<inline_answers>false</inline_answers>
						<auto_next>false</auto_next>
						<description>"""+ str(recent_question_dict['question_text']) + """</description>
						<explanation> """ + str(explanation) + """</explanation>
"""
            #print question_match_found.group(), line_read[len(question_match_found.group()):]
        else: 
            question_option_match_found = re.search('^\(?[aAbBcCdDeEfF]\.?\)?[ ]?', line_read)

            if question_option_match_found:
#                op_position += 1
                if recent_question_dict:
                    if 'question_options' in recent_question_dict:
                        correct_flag = False
                        option_correct_match_found = re.search('.+\*$', line_read.strip())
                        if option_correct_match_found:
                            #print option_correct_match_found.group()
                            correct_flag = True
#                        recent_question_dict['question_options'].append({'file_line': line_read, 'option_text': line_read[len(question_option_match_found.group()):].strip().replace('*', ''), 'correct': correct_flag})
                        recent_question_dict['question_options'].append({'file_line': line_read, 'Options': line_read[len(question_option_match_found.group()):].strip().replace('*', ''), 'correct': correct_flag})
#                        print "QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ" + str(line_read[len(question_option_match_found.group()):].strip().replace('*', ''))
#                        print "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC" + str(correct_flag)
                        
#                        op_position += 1
                                                
#                        print "KKKKKKKKKKKKKKKKKKKKKKKKKKKKK" + str(op_position)
                        xml_questions += """
						<answer>
							<enabled>true</enabled>
							<isright>""" + str(correct_flag) + """</isright>
							<position>""" +str(op_position)+ """</position>
							<keyboard_key></keyboard_key>
							<description>""" + str(line_read[len(question_option_match_found.group()):].strip().replace('*', '')) + """</description>
							<explanation></explanation>
						</answer>"""
						
                        op_position += 1
            
						
#####################################################################################################################################
                        #print question_option_match_found.group(), line_read[len(question_option_match_found.group()):]
        line_read = file_obj_pointer.readline()
        
#    op_position = 0
       
    
    '''Save the last question'''
    if recent_question_dict:
        if 'question_options' in recent_question_dict:
            if recent_question_dict['question_options']:
                if len(recent_question_dict['question_options']) > 1:
                    mcq_questions_found.append(recent_question_dict)                    
 
    questions_processed = []
   
    xml_questions += """
		    </subject>
		</module>
	</body>
</tcexamquestions> """

    print xml_questions
    paper = open(xml_paper, "w")
    paper.write(xml_questions)
    file_obj_pointer.close()
    paper.close()
    return True

convert_paper_xml()
