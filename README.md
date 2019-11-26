# Precise face-alignment
Precise face-alignment with opencv and dlib, using some geometry magic.
The difference between this face-alignment algorithm and others is in the fact that this one relies not onlly on the position of the eyes, but also depends on the position of the nose. The scheme of the algorithm is shown below :
![Alt text](https://github.com/HikkaV/Precise-face-alignment/blob/master/face_alignment.png?raw=true "Face alignment algorithm")
In order to use a programm do the following :
1) Make new virtualenv and activate it: <pre>virtualenv face-alignment</pre> <pre>source face-alignment/bin/activate</pre>
2) Clone this repo to some folder and move to it : <pre>git clone https://github.com/HikkaV/Precise-face-alignment</pre> 
   <pre>cd Precise-face-alignment/</pre>
3) Install requirments : <pre>pip install -r requirments.txt</pre>
4) In order to get to know available commands : <pre>python run.py -h</pre>
Currently two modes of algorithm are available : opencv cascade classifier mode and dlib 5 facial lendmarks recognizer mode. 
Note : dlib mode is much more precise.
Example of a programm :

**Original image** 
![Alt text](https://github.com/HikkaV/Precise-face-alignment/blob/master/tilthead.jpg?raw=true "Original image")


**Command** : 
<pre>python run.py --mode 1 --path_to_load=tilthead.jpg --path_to_save='smth.png'</pre>

**Result** :
![Alt text](https://github.com/HikkaV/Precise-face-alignment/blob/master/smth.png?raw=true "Result")
