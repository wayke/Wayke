"""
The MIT License (MIT)

Copyright (c) 2015 Javier Asensio-Cubero capitan.cambio@gmail.com 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from liblo import ServerThread,TCP,UDP,make_method 
import sys 
import time
import json



#PATHS
EEG='/muse/eeg' 
EEG_QUANTIZAION='/muse/eeg/quantization'
EEG_DROPPED_SAMPLES='/muse/eeg/dropped_samples'
ACC='/muse/acc'
ACC_DROPPED_SAMPLES='/muse/acc/dropped_samples'
BATT='/muse/batt'
DRLREF='/muse/drlref'
CONFIG='/muse/config' 
VERSION='/muse/version'
ANNOTATION='/muse/annotation'
ELEMENTS_RAW_FFT0='/muse/elements/raw_fft0'
ELEMENTS_RAW_FFT1='/muse/elements/raw_fft1'
ELEMENTS_RAW_FFT2='/muse/elements/raw_fft2'
ELEMENTS_RAW_FFT3='/muse/elements/raw_fft3'
#ALIASES
ELEMENTS_RAW_FFT_TP9=ELEMENTS_RAW_FFT0
ELEMENTS_RAW_FFT_FP1=ELEMENTS_RAW_FFT1
ELEMENTS_RAW_FFT_FP2=ELEMENTS_RAW_FFT2
ELEMENTS_RAW_FFT_TP10=ELEMENTS_RAW_FFT3
ELEMENTS_LOW_FREQS_ABSOLUTE='/muse/elements/low_freqs_absolute'

ELEMENTS_DELTA_ABSOLUTE='/muse/elements/delta_absolute'
ELEMENTS_THETA_ABSOLUTE='/muse/elements/theta_absolute'
ELEMENTS_ALPHA_ABSOLUTE='/muse/elements/alpha_absolute'
ELEMENTS_BETA_ABSOLUTE='/muse/elements/beta_absolute'
ELEMENTS_GAMMA_ABSOLUTE='/muse/elements/gamma_absolute'

ELEMENTS_DELTA_RELATIVE='/muse/elements/delta_relative'
ELEMENTS_THETA_RELATIVE='/muse/elements/theta_relative'
ELEMENTS_ALPHA_RELATIVE='/muse/elements/alpha_relative'
ELEMENTS_BETA_RELATIVE='/muse/elements/beta_relative'
ELEMENTS_GAMMA_RELATIVE='/muse/elements/gamma_relative'

ELEMENTS_DELTA_SESSION_SCORE='/muse/elements/delta_session_score'
ELEMENTS_THETA_SESSION_SCORE='/muse/elements/theta_session_score'
ELEMENTS_ALPHA_SESSION_SCORE='/muse/elements/alpha_session_score'
ELEMENTS_BETA_SESSION_SCORE='/muse/elements/beta_session_score'
ELEMENTS_GAMMA_SESSION_SCORE='/muse/elements/gamma_session_score'

ELEMENTS_TOUCHING_FOREHEAD='/muse/elements/touching_forehead'

ELEMENTS_HORSESHOE='/muse/elements/horseshoe'
ELEMENTS_IS_GOOD='/muse/elements/is_good'
ELEMENTS_BLINK='/muse/elements/blink'
ELEMENTS_JAW_CLENCH='/muse/elements/jaw_clench'

EXPERIMENTAL_CONCENTRATION='/muse/elements/experimental/concentration'
EXPERIMENTAL_MELLOW='/muse/elements/experimental/mellow'


CONCENTRATION='/muse/elements/experimental/concentration'
MELLOW='/muse/elements/experimental/mellow'

#DATA_TYPES
DATA_TYPES={
                EEG:"ffff",
                EEG_QUANTIZAION:"iiii",
                EEG_DROPPED_SAMPLES:"i",
                ELEMENTS_HORSESHOE:"ffff",
                ACC:"fff",
                ACC_DROPPED_SAMPLES:"i",
                BATT:"iiii",
                DRLREF:"ff",
                CONFIG: "s",
                VERSION: "s",
                ANNOTATION:"sssss",
                ELEMENTS_RAW_FFT_TP9:"fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
                ELEMENTS_RAW_FFT_FP1:"fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
                ELEMENTS_RAW_FFT_FP2:"fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
                ELEMENTS_RAW_FFT_TP10:"fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
                ELEMENTS_LOW_FREQS_ABSOLUTE:"ffff",
                ELEMENTS_DELTA_ABSOLUTE:"ffff",
                ELEMENTS_THETA_ABSOLUTE:"ffff",
                ELEMENTS_ALPHA_ABSOLUTE:"ffff",
                ELEMENTS_BETA_ABSOLUTE:"ffff",
                ELEMENTS_GAMMA_ABSOLUTE:"ffff",
                ELEMENTS_DELTA_RELATIVE:"ffff",
                ELEMENTS_THETA_RELATIVE:"ffff",
                ELEMENTS_ALPHA_RELATIVE:"ffff",
                ELEMENTS_BETA_RELATIVE:"ffff",
                ELEMENTS_GAMMA_RELATIVE:"ffff",
                ELEMENTS_DELTA_SESSION_SCORE:"ffff",
                ELEMENTS_THETA_SESSION_SCORE:"ffff",
                ELEMENTS_ALPHA_SESSION_SCORE:"ffff",
                ELEMENTS_BETA_SESSION_SCORE:"ffff",
                ELEMENTS_GAMMA_SESSION_SCORE:"ffff",
                ELEMENTS_TOUCHING_FOREHEAD:"i",
                ELEMENTS_IS_GOOD:"iiii",
                ELEMENTS_BLINK:"i",
                ELEMENTS_JAW_CLENCH:"i",
                EXPERIMENTAL_CONCENTRATION:"f",
                EXPERIMENTAL_MELLOW:"f",




}

class ElectrodeReading(object):

        """ Holds the a reading from the electrodes"""

        def __init__(self,TP9,FP1,FP2,TP10):
                """ sets the electrode values """
                self.TP9=TP9
                self.FP1=FP1
                self.FP2=FP2
                self.TP10=TP10
                
class ACCReading(object):

        """ holds a reading from the accelometer """

        def __init__(self,x,y,z):
                self.x=x
                self.y=y
                self.z=z
                
class BattReading(object):
        """ Holds the readings from the battery computing the real values"""

        def __init__(self,charge,mvFuelGauge,mvACD,temperature):
                self.charge=charge/100.0
                self.mvFuelGauge=mvFuelGauge
                self.mvACD=mvACD
                self.temperature=temperature

class DRLRefReading(object):
        """ Holds the referece readings """
        def __init__(self,drl,ref):
                self.drl=drl
                self.ref=ref

class AnnotationReading(object):

    """ Holds an annotation reading"""

    def __init__(self,data,format,type, event_id,parent_id):

        self.data = data
        self.format = format
        self.type = type
        self.event_id = event_id
        self.parent_id = parent_id
        


class Muse(ServerThread):
    """ Based on https://sites.google.com/a/interaxon.ca/muse-developer-site/developer-getting-started-guide/osc_server.py?attredirects=0&d=1   
    Compatible with muse-io 3.6.X

    Usage:

    def myfunc(eeg):
        print eeg

    muse=Muse(5000)
    muse.register_callback(EEG,myfunc)
    muse.start()
    #wait!

    """

    #listen for messages on port 5001

    def __init__(self,port,proto=UDP):
        """ Constructor
            :port: Port to listen from
            :proto: Protocol liblo values TCP,UDP and UNIX
            """

        ServerThread.__init__(self,port,proto)
        self._callbacks={}
        self._fallback=None
        self._init_databuilders()

    def _init_databuilders(self):
            """ initialises the data builders for the different types of data 
                this can be costumizable when registering the callback 
            """
            self._databuilders={
                        EEG:builder_electrodes,
                        EEG_QUANTIZAION:builder_electrodes,
                        EEG_DROPPED_SAMPLES:_value,
                        ACC:builder_acc,
                        ACC_DROPPED_SAMPLES:_value,
                        BATT:builder_batt,
                        DRLREF:builder_drlref,
                        CONFIG:from_json,
                        VERSION:from_json,
                        ANNOTATION:builder_annotation,
                        ELEMENTS_RAW_FFT_TP9:_value,
                        ELEMENTS_RAW_FFT_FP1:_value,
                        ELEMENTS_RAW_FFT_FP2:_value,
                        ELEMENTS_RAW_FFT_TP10:_value,
                        ELEMENTS_LOW_FREQS_ABSOLUTE:builder_electrodes,
                        ELEMENTS_DELTA_ABSOLUTE:builder_electrodes,
                        ELEMENTS_THETA_ABSOLUTE:builder_electrodes,
                        ELEMENTS_ALPHA_ABSOLUTE:builder_electrodes,
                        ELEMENTS_BETA_ABSOLUTE:builder_electrodes,
                        ELEMENTS_GAMMA_ABSOLUTE:builder_electrodes,
                        ELEMENTS_DELTA_RELATIVE:builder_electrodes,
                        ELEMENTS_THETA_RELATIVE:builder_electrodes,
                        ELEMENTS_ALPHA_RELATIVE:builder_electrodes,
                        ELEMENTS_BETA_RELATIVE:builder_electrodes,
                        ELEMENTS_GAMMA_RELATIVE:builder_electrodes,
                        ELEMENTS_DELTA_SESSION_SCORE:builder_electrodes,
                        ELEMENTS_THETA_SESSION_SCORE:builder_electrodes,
                        ELEMENTS_ALPHA_SESSION_SCORE:builder_electrodes,
                        ELEMENTS_BETA_SESSION_SCORE:builder_electrodes,
                        ELEMENTS_GAMMA_SESSION_SCORE:builder_electrodes,
                        ELEMENTS_TOUCHING_FOREHEAD:_value,
                        ELEMENTS_HORSESHOE:builder_electrodes,
                        ELEMENTS_IS_GOOD:builder_electrodes,
                        ELEMENTS_BLINK:_value,
                        ELEMENTS_JAW_CLENCH:_value,
                        EXPERIMENTAL_CONCENTRATION:_value,
                        EXPERIMENTAL_MELLOW:_value,
                }
        

    def register_callback(self,path,callback,databuilder=None):
        """ Registers a callback that is applyied when a message from path is received
            the callback should be as fast as possible
        
            :path: osc path
            :callback: callback to trigger when data is received  
            :databuilder: a function that builds a specific data type or object with the received data before invoking the callback
        """
        if path in DATA_TYPES:
                self.add_method(path,DATA_TYPES[path],self._apply_callback)
                self._callbacks[path]=callback
                if databuilder!=None:
                        self._databuilders[path]=databuilder
        else:
                raise Exception("Path not found %s"%path)

    def _apply_callback(self,path,data):
        """ Applies the regestired callback to data
            :path: osc path
            :data: data to send to the callback
        """
        if  path in self._callbacks and path in self._databuilders:
                self._callbacks[path](self._databuilders[path](data))



def builder_electrodes(values):
        """
        Creates a  ElectrodeSet object with given electrode values
        :values: electrode values 
        :returns: a ElectrodeSet object 
        """
        return ElectrodeReading(values[0],values[1],values[2],values[3]) 

def builder_acc(values):
        """ Creates an ACC object from the values """
        return ACCReading(values[0],values[1],values[2])

def builder_batt(values):
        """ Creates a BattReading object from the values """
        return BattReading(values[0],values[1],values[2],values[3])

def builder_drlref(values):
        """ Creates a drlref reading from the values """
        return DRLRefReading(values[0],values[1])

def builder_annotation(values):
        """ Creates an annotation reading from the values """
        return AnnotationReading(values[0],values[1],values[2],values[3],values[4])


def from_json(value):
        return json.loads(value)

def _value(value):
        return value


