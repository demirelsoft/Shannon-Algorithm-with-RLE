# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:13:42 2021

@author: rabia-mert-youness
"""

#this library for plots
from matplotlib import pyplot as plt

'''The NumPy library contains multidimensional array and matrix data structures'''
import numpy as np
import collections
import operator

import os

#tkinter library is used for interface design
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import PIL.Image
from PIL import Image
from PIL import ImageTk

#time library for calculate time of compression
import time

class Shannon:
    
    #there are two code_book for code list with RLE and without RLE 
    code_book = {}
    code_bookwo = {}
    def __init__(self, window):
        
        #this part choose size of app window and bg color
        self.window = window
        window.geometry('1700x900+50+50')
        window.title('Shannon-Fano Algorithm')
        window.configure(bg='blue')
        window.overrideredirect(1)
        
        
        self.action3 = Button(text='Show School', font=("Roboto", 14, "bold"), width=20, height=1, bg='#2E8B57',
                            fg='white', bd=14, cursor='star', activebackground='#90EE90', activeforeground='black',
                            command=self.open_img)
        self.action3.place(x=100, y=600)
        
        

        #main title of window
        self.main_label = Label(text='Shannon-Fano Algorithm', fg='#57E6F4', bg='blue',
                           font=("Roboto", 30, "bold"))
        self.main_label.pack(pady=30)
        
        #this is website
        self.text1 = Label(text='demirelsoft.com ', fg='red', bg='blue', font=("Roboto", 16, "bold"))
        self.text1.place(x=20, y=20)
        
        self.text2 = Label(text='Directed by:   Rabia Öztürk - Mert Demirel - Youness Hammadi ', fg='pink', bg='blue', font=("Roboto", 18, "bold"))
        self.text2.place(x=20, y=485)
        
        
        
##########################      RLE Algorithm    ##############################            
        
        #this is line of text
        self.text = Label(text='Input Text : ', fg='orange', bg='blue', font=("Roboto", 16, "bold"))
        self.text.place(x=50, y=130)
        
        self.text_input = Entry(window, width=40, fg='blue', bd='8', font=("Roboto", 15, "bold"))
        self.text_input.place(x=200, y=130)



        #this is line of compression
        self.compression = Label(text='Compression : ', fg='orange', bg='blue', font=("Roboto", 16, "bold"))
        self.compression.place(x=50, y=200)
        
        self.compression_rle = Entry(window, width=40, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.compression_rle.place(x=200, y=200)
        
        
        
        #this is line of compression time
        
        self.ctime = Label(text='Comp. Time : ', fg='orange', bg='blue', font=("Roboto", 16, "bold"))
        self.ctime.place(x=50, y=270)
        
        self.rle_time = Entry(window, width=40, fg='blue', bd='8', font=("Roboto", 15, "bold"))
        self.rle_time.place(x=200, y=270)


        #this is RLE compression starter button
        self.action1 = Button(text='Compress RLE', font=("Roboto", 14, "bold"), width=15, height=1, bg='orange',
                            fg='white', bd=14, cursor='star', activebackground='orange', activeforeground='black',
                            command=self.compress_rle)
        self.action1.place(x=700, y=200)
         

        
##########################  Shannon Fano with RLE Algorithm    ##############################            
        
        
        
        # Shannon Fano Bits counter with RLE ################        
        
        self.text = Label(text='Before Bits with RLE : ', fg='#EF94FF', bg='blue', font=("Roboto", 16, "bold"))
        self.text.place(x=1000, y=130)
        
        self.text = Label(text='After Bits with RLE : ', fg='#EF94FF', bg='blue', font=("Roboto", 16, "bold"))
        self.text.place(x=1000, y=200)
        
        self.bbits = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.bbits.place(x=1300, y=130)
        
        self.abits = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.abits.place(x=1300, y=200)
        

        
        # Code Shannon with RLE ################


        self.dictionary = Label(text='Code with RLE :', fg='#EF94FF', bg='blue', font=("Roboto", 16, "bold"))
        self.dictionary.place(x=1000, y=270)        
        
        self.dictionary_ = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.dictionary_.place(x=1300, y=270)
        


        # Time Shannon Alg. with RLE ###########

        self.stime_ = Label(text='Comp. Time with RLE :', fg='#EF94FF', bg='blue', font=("Roboto", 16, "bold"))
        self.stime_.place(x=1000, y=340)
        
        self.stimer = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.stimer.place(x=1300, y=340)



        # Compress Shannon algorithm with RLE ########
        
        self.compression123 = Label(text='Compression with RLE : ', fg='#EF94FF', bg='blue', font=("Roboto", 16, "bold"))
        self.compression123.place(x=1000, y=410)

        self.compression_SwithRLE = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.compression_SwithRLE.place(x=1300, y=410)


        # Compress Shannon algorithm with RLE button ########

        self.action = Button(text='Compress S with RLE', font=("Roboto", 14, "bold"), width=20, height=1, bg='#EF94FF',
                            fg='white', bd=14, cursor='star', activebackground='#EF94FF', activeforeground='black',
                            command=self.compress_shannon_withRLE)
        self.action.place(x=1000, y=820)



 ##########################  Shannon Fano without RLE Algorithm    ##############################        



         # Shannon Fano Bits counter without RLE ################        
        
        self.text = Label(text='Before Bits without RLE : ', fg='#2AE332', bg='blue', font=("Roboto", 16, "bold"))
        self.text.place(x=1000, y=480)
        
        self.text = Label(text='After Bits without RLE : ', fg='#2AE332', bg='blue', font=("Roboto", 16, "bold"))
        self.text.place(x=1000, y=550)
        
        self.wobbits = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.wobbits.place(x=1300, y=480)
        
        self.woabits = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.woabits.place(x=1300, y=550)
        

        
        # Code Shannon without RLE ################


        self.wodictionary = Label(text='Code without RLE :', fg='#2AE332', bg='blue', font=("Roboto", 16, "bold"))
        self.wodictionary.place(x=1000, y=620)        
        
        self.wodictionary_ = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.wodictionary_.place(x=1300, y=620)
        


        # Time Shannon Alg. without RLE ###########

        self.wostime_ = Label(text='Comp. Time without RLE :', fg='#2AE332', bg='blue', font=("Roboto", 16, "bold"))
        self.wostime_.place(x=1000, y=690)
        
        self.wostimer = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.wostimer.place(x=1300, y=690)



        # Compress Shannon algorithm without RLE ########
        
        self.wocompression123 = Label(text='Compression without RLE : ', fg='#2AE332', bg='blue', font=("Roboto", 16, "bold"))
        self.wocompression123.place(x=1000, y=760)

        self.compression_SwithoRLE = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.compression_SwithoRLE.place(x=1300, y=760)


        # Compress Shannon algorithm without RLE button ########

        self.action = Button(text='Compress S without RLE', font=("Roboto", 14, "bold"), width=20, height=1, bg='#2AE332',
                            fg='white', bd=14, cursor='star', activebackground='#2AE332', activeforeground='black',
                            command=self.compress_shannon_withoRLE)
        self.action.place(x=1300, y=820)
        
        
        #this is close button
        self.close_button = Button(text='X', font=("Roboto", 14, "bold"), width=3, height=1, bg='red', fg='white',
                       cursor='star', activebackground='red', activeforeground='black', command=self.close_button)
        self.close_button.place(x=1660, y=0)
        
        
        
################ Write Compration Ratio with RLE and without RLE ####
        
        self.cratiowRLE = Label(text='Comp. Ratio with RLE : ', fg='#EF94FF', bg='blue', font=("Roboto", 16, "bold"))
        self.cratiowRLE.place(x=50, y=345)
        
        self.cratiowRLE = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.cratiowRLE.place(x=310, y=340)
        
        
        self.cratiowoRLE = Label(text='Comp. Ratio without RLE : ', fg='#2AE332', bg='blue', font=("Roboto", 16, "bold"))
        self.cratiowoRLE.place(x=50, y=415)
        
        self.cratiowoRLE = Entry(window, width=30, fg='black', bd='8', font=("Roboto", 15, "bold"))
        self.cratiowoRLE.place(x=310, y=410)
        

############ PLOT S1 S2 S3 S4 S5 ################


        self.plot_button = Button(text='PLOT S1-S5', font=("Roboto", 14, "bold"), width=20, height=1, bg='#2E8B57',
                            fg='white', bd=14, cursor='star', activebackground='#90EE90', activeforeground='black',
                            command=self.plot)
        self.plot_button.place(x=100, y=820)




#############   Run length algorithm part   ##############
    
    def RLE(self, input):
        #this part time is start for rle algorithm
        self.start1 = time.time()
        #this part choose all input characters
        input = input + '#'
        #counter1 is counting how many times to repeat
        counter1 = 1
        #output1 is list of output values
        output1 = []
        
        #for loop is continues according to the length-1 of the word
        for i in range(0, len(input)-1):
                    #if first letter is equal to next letter counter value is one increases
                    if input[i] == input[i+1]:
                        counter1 += 1
                    #if first letter isn't equal to next letter  
                    elif input[i] != input[i+1]:
                        #First, the number of repetitions is written, followed by the character
                        result = (str(counter1)+str(input[i]))
                        #append result value to output1
                        output1.append(result.replace(" ", ""))
                        #print result
                        print(result)
                        #counter is equal 1 for next character
                        counter1 = 1
                        #this part time is end for rle algorithm
                        self.end1 = time.time()          
                        #calculation end1 time - start1 time
                        self.t1 = self.end1-self.start1    
        #print t1(rle time)               
        print(self.t1)
        return output1
    
    def compress_rle(self):
        #this part get text from thinker enter area
        text = self.text_input.get()
        #this part if text entery is empty, give error 
        if len(text) == 0:
            messagebox.showwarning('Please add text ', 'Entry is empty !')
        else:
            #this part if text entery isn't empty 
            #compress_rle value equal to the value from RLE
            compress_rle = self.RLE(text)
            
            #Time and compression values ​​are sent to entry
            self.rle_text(self.rle_time, self.t1)
            self.rle_text(self.compression_rle, compress_rle)
            
    #to change when text is refreshed. first delete after insert text
    def rle_text(self, var, text):
        var.delete(0, END)
        var.insert(0, text)
        return        
            
    #this part get text from thinker enter area        
    def close_button(self):
        self.window.destroy()
    
    
    
    
##############      This part shannon algorithm  with RLE    #############
    
    #to change when text is refreshed. first delete after insert text
    def set_text(self, var, text):
        var.delete(0, END)
        var.insert(0, text)
        return


    #when the press compress S with RLE 
    def compress_shannon_withRLE(self):
        #this part read Rle output values
        text = self.compression_rle.get()
        #this part remove all whitespace
        text = text.replace(" ", "")
        #before bits counter is 0
        self.bcount = 0
        for k in text: 
                #before bits count for loop
                self.bcount = self.bcount + 1
                
       
        
        if len(text) == 0:
            #if text area is empty, get warning message
            messagebox.showwarning('Please add text ', 'Entry is empty !')
        else:
            #x value is equal to text from create_list
            x = self.freq_list(text)
            #m value is equal to result of shannon_fano_structure(x)
            m = self.shannon_fano_structure(x)
            #write m values to dictionary_ (Code with RLE)
            self.set_text(self.dictionary_, m)
            #com value is equal to text from self.compressionwele
            com = self.compressionwrle(text)
            #com value write to self.compression_SwithRLE on window
            self.set_text(self.compression_SwithRLE, com)
            #comprassion time value equal to self.st
            self.st = self.stime(text)
            #wcount is bits of aftercomprassion
            self.wcount = 0
  
            for i in com: 
                if i == '0' or '1': 
                    #calculate how many chars in after compression
                    self.wcount = self.wcount + 1
            
            
            
            
            self.bcount = self.bcount*8
            
            #this part write all values on window text part
            self.set_text(self.cratiowRLE,self.bcount/self.wcount)
            self.set_text(self.bbits,self.bcount) 
            self.set_text(self.abits,self.wcount) 
            self.set_text(self.stimer,self.st) 
    
    

    #calculate frequency of all char. by one by
    def freq_list(self, text):
        self.start2 = time.time()
        #this part frequency dictionary of text
        list = dict(collections.Counter(text))
        #sort the list 
        list_sorted = sorted(list.items(), key=operator.itemgetter(1), reverse=True)

        # format the final list as [letters, frquancy, code]
        final_list = []
        for key, value in list_sorted:
            final_list.append([key, value, ''])
        #all characters value write by one by
        return final_list


    
    def divide_list(self, list):
        all_m = []
        left = 0
        right = 0
        #list is the freq all chars
        #lem(list) This is a list for which number of elements to be counted.
        #for loop continue range of 0 to len(list)
        #This part allows us to divide the frequencies into two, right and left.
        for i in range(0, len(list)):
            for j in range(i + 1, len(list)):
                right += list[j][1]
                
            for l in range(i, -1, -1):
                left += list[l][1]
                
            #absolute value is to be returned
            between = abs(right - left)
            all_m.append(between)

            left = 0
            right = 0
        
        # find min minus
        min = [all_m[0], 0]
        
        for z in range(1, len(all_m)):
            if all_m[z] < min[0]:
                min = [all_m[z], z]

        # cutting
        index_of_min = min[1]
        return list[0:index_of_min + 1], list[index_of_min + 1:]

    
    #two groups whose sum is approximately equal to each other are given the numbers 0 and 1 respectively
    def shannon_fano_structure(self, list):
        
        #first bigger list value is 0 second lower list value is 1
        l1, l2 = self.divide_list(list)
        for i in l1:
            i[2] += '0'
            self.code_book[i[0]] = i[2]

        for i in l2:
            i[2] += '1'
            self.code_book[i[0]] = i[2]


        if len(l1) > 1:
            self.shannon_fano_structure(l1)
        if len(l2) > 1:
            self.shannon_fano_structure(l2)
        
        #finally write code shaped 1 and 0 
        return self.code_book

    #final part is list of after comprassion values (1 and 0)
    def compressionwrle(self,text):
        after_compression = ''
        #the last part all chars. write in order of.
        for i in text:
            for j in self.code_book.keys():
                if i == j:
                    after_compression += self.code_book[j]
        
                   
        return after_compression
    
    #this part calculate compression time
    def stime(self,text):
        t2 = ''
        self.end2 = time.time()
        t2 = self.end2-self.start2
       
                   
        return t2
    
    

##############      This part shannon algorithm  without RLE    #############

    

    #to change when text is refreshed. first delete after insert text
    def set_textwo(self, var, text):
        var.delete(0, END)
        var.insert(0, text)
        return


    #when the press compress S with RLE 
    def compress_shannon_withoRLE(self):
        #this part read Rle output values
        text = self.text_input.get()
        
                #this part remove all whitespace
                #text = text.replace(" ", "")
                
                
        #before bits counter is 0
        self.wobcount = 0
        for k in text: 
                #before bits count for loop
                self.wobcount = self.wobcount + 1
                
       
        
        if len(text) == 0:
            messagebox.showwarning('Please add text ', 'Entry is empty !')
        else:
            x = self.freq_listwo(text)
            m = self.shannon_fano_structurewo(x)
            self.set_textwo(self.wodictionary_, m)
            wocom = self.compressionworle(text)
            self.set_textwo(self.compression_SwithoRLE, wocom)
            self.wost = self.wostime(text)
            self.wocount = 0
  
            for i in wocom: 
                if i == '0' or '1': 
                    self.wocount = self.wocount + 1
            print(self.bcount) 
            
            
            self.wobcount = self.wobcount*8
            
            self.set_textwo(self.cratiowoRLE,self.wobcount/self.wocount)
            self.set_textwo(self.wobbits,self.wobcount) 
            self.set_textwo(self.woabits,self.wocount) 
            self.set_textwo(self.wostimer,self.wost) 
    
    

    
    def freq_listwo(self, text):
        self.wostart2 = time.time()
        list = dict(collections.Counter(text))
        list_sorted = sorted(list.items(), key=operator.itemgetter(1), reverse=True)

        # format the final list as [letters, frquancy, code]
        final_list = []
        for key, value in list_sorted:
            final_list.append([key, value, ''])
        return final_list



    def divide_listwo(self, list):
        all_m = []
        left = 0
        right = 0
        for i in range(0, len(list)):
            for j in range(i + 1, len(list)):
                right += list[j][1]

            for l in range(i, -1, -1):
                left += list[l][1]

            between = abs(right - left)

            all_m.append(between)

            left = 0
            right = 0

        # find min minus
        min = [all_m[0], 0]
        for z in range(1, len(all_m)):
            if all_m[z] < min[0]:
                min = [all_m[z], z]

        # cutting
        index_of_min = min[1]

        return list[0:index_of_min + 1], list[index_of_min + 1:]


    def shannon_fano_structurewo(self, list):
        
        
        
        l1, l2 = self.divide_list(list)
        for i in l1:
            i[2] += '0'
            self.code_bookwo[i[0]] = i[2]

        for i in l2:
            i[2] += '1'
            self.code_bookwo[i[0]] = i[2]

        if len(l1) > 1:
            self.shannon_fano_structurewo(l1)
        if len(l2) > 1:
            self.shannon_fano_structurewo(l2)

        return self.code_bookwo


    def compressionworle(self,text):
        after_compression = ''
        for i in text:
            for j in self.code_book.keys():
                if i == j:
                    after_compression += self.code_book[j]
        
                   
        return after_compression
    
    def wostime(self,text):
        wot2 = ''
        self.woend2 = time.time()
        wot2 = self.woend2-self.wostart2
        print(wot2)
                   
        return wot2

    #this is the plot part, s1 to s5
    def plot(self):
        
        self.bit1  = 12000
        self.bit2  = 31569
        self.bit3  = 38141
        self.bit4  = 59639
        self.bit5  = 76349
        
        self.comp11  = 2.622
        self.comp22  = 2.577
        self.comp33  = 2.482
        self.comp44  = 2.456
        self.comp55  = 2.484
        
        self.t11     = 0.093
        self.t22     = 0.569
        self.t33     = 0.815
        self.t44     = 1.999
        self.t55     = 3.079
            
        
        fig, ax = plt.subplots()
        ax.scatter(self.bit1, self.comp11 , label='s1',color='blue')
        ax.scatter(self.bit2, self.comp22 , label='s2',color='red')
        ax.scatter(self.bit3, self.comp33 , label='s3',color='green')
        ax.scatter(self.bit4, self.comp44 , label='s4',color='black')
        ax.scatter(self.bit5, self.comp55 , label='s5',color='purple')
        ax.legend()
        ax.set_ylabel('Compression Ratio ')
        ax.set_xlabel('Bit lengths (in bits)')
        plt.show() 
        
        fig, ax = plt.subplots()
        ax.scatter(self.bit1, self.t11 , label='s1',color='blue')
        ax.scatter(self.bit2, self.t22 , label='s2',color='red')
        ax.scatter(self.bit3, self.t33 , label='s3',color='green')
        ax.scatter(self.bit4, self.t44 , label='s4',color='black')
        ax.scatter(self.bit5, self.t55 , label='s5',color='purple')
        ax.legend()
        ax.set_ylabel('Compression Time (in second)')
        ax.set_xlabel('Bit lengths (in bits)')
        plt.show() 
        
        
    def open_img(self):
        global img
        path = r"C:\Users\Electro\Desktop\son dersler\Yeni klasör (2)\\ikcu.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        
        panel = Label(window, image=img)
        panel.place(x=500, y=550)
    
    


#start tkinter and open window
window = Tk()




#Open Shannon in the Tkinter Window
gui = Shannon(window)
#the window is constantly working
window.mainloop()

