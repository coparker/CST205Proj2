import numpy as ny  # http://www.numpy.org
import wave  # https://docs.python.org/2/library/wave.html
import struct  # https://docs.python.org/2/library/struct.html
import random # this is needed due to the wide variety of small values returned by the findFreqInHertz function

"""
@Author: Siddarth Krishnan
@Date:	 10/14/2016
		 This function extracts the frequency from the byte data of the given audio file
"""
def findFrequencyInHertz(waveFile):  # make a function that takes in a waveFile

    data = waveFile.readframes(waveFile.getnframes())  # get the data in string on bytes
    data1 = (int)(len(data) / 2)
	
    newData = struct.unpack('h' * data1 , data)# newData should convert the string of bytes into int values
    newData = ny.array(newData)  # make an array
    freq = ny.fft.fft(newData)  # fft the whole array
    freqInHertzArray = []  # create a freq array to store all the freq values

    for x in range(0, len(freq), 1000):
        freqInHertz = abs(freq[x] * 11025)  # convert all the fft values into hertz values
        freqInHertzArray.append(freqInHertz)  # push the hertz values into the freqHertzArray

    return freqInHertzArray  # return the freqInHertzArray

"""
@Author: Cody Parker
@Date:	 10/14/2016	
		 This function maps the values of the returned byte data to be between 0 and 255
		 as a side note those values were concentrated at the lower end of the spectrum and resulted
		 in a returned array of low values, making the randomization necessary for a more evident visual ef
"""
def run():
	myArray = []
	waveFile = wave.open('C:/dev/CST205Proj2/testFile.wav')  # creating a file
	freqInHertzArray = findFrequencyInHertz(waveFile)  # using the function and returning it to the array
	for i in freqInHertzArray:
		if max(freqInHertzArray)-min(freqInHertzArray) != 0:
			myArray.append((int)(((i-min(freqInHertzArray))/(max(freqInHertzArray)- min(freqInHertzArray))) * 255))
        
	return myArray

myArray1 = run()
for x in range(len(myArray1)-1):
    if(myArray1[x] == myArray1[x +1]):
        myArray1[x] = random.randint(0,255)
        myArray1[x + 1] = random.randint(0,255) # checks to see if the values are the same if they are then then the numbers at those index are randomized.
    
#print(myArray1)
