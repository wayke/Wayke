import unittest
import pyrnassus  

class TestData(unittest.TestCase):

    def setUp(self):
        self.muse=pyrnassus.Muse(None)

    def test_apply_callback_unkown_path(self):
        try:
            self.muse._apply_callback("unknownpath",[1])
            self.fail("This should break")

        except Exception:
            pass


    def test_apply_callback_with_builder(self):

        h=Holder()
        #register a data builder and a path
        self.muse.register_callback(pyrnassus.EEG,h.set,lambda x:x*2)
        self.muse._apply_callback(pyrnassus.EEG,2)
        self.assertEqual(h.value,4,"The callback and the data_bulider have been applied")




    def test_builder_eeg(self):
        """                
        Test the creation of electrode based dictionaries
        """
        values=[1,2,3,4]
        eeg=pyrnassus.builder_electrodes(values)
        self.assertEquals(eeg.TP9,1,"TP9 value is 1")
        self.assertEquals(eeg.FP1,2,"FP1 value is 2")
        self.assertEquals(eeg.FP2,3,"FP2 value is 3")
        self.assertEquals(eeg.TP10,4,"TP10 value is 4")

    def test_builder_acc(self):
        values=[1,2,3]
        acc=pyrnassus.builder_acc(values)
        self.assertEquals(acc.x,1,"x value is 1")
        self.assertEquals(acc.y,2,"y value is 2")
        self.assertEquals(acc.z,3,"z value is 3")

    def test_builder_batt(self):
        values=[5132,2,3,4]
        batt=pyrnassus.builder_batt(values)
        self.assertEquals(batt.charge,51.32,"charge is 51.32")
        self.assertEquals(batt.mvFuelGauge,2,"mvFuelGauge is 2")
        self.assertEquals(batt.mvACD,3,"mvACD value is 3")
        self.assertEquals(batt.temperature,4,"temp value is 4")

    def testbuilder_drlref(self):
        values=[1,2]
        reft=pyrnassus.builder_drlref(values)
        self.assertEquals(reft.drl,1,"drl is 1")
        self.assertEquals(reft.ref,2,"ref is 2")

    def test_from_json(self):
        values='{"message":"hi"}'
        jval=pyrnassus.from_json(values)
        self.assertEquals(jval["message"],"hi","message is hi")

    def testbuilder_annotation(self):
        values=["a","b","c","d","e"]
        ann=pyrnassus.builder_annotation(values)
        self.assertEquals(ann.data,"a","data is set to a")
        self.assertEquals(ann.format,"b","format is set to b")
        self.assertEquals(ann.type,"c","typeis set to c")
        self.assertEquals(ann.event_id,"d","event_id is set to e")
        self.assertEquals(ann.parent_id,"e","parent_id set to d")


    def test_eeg(self):
        """ Check eeg sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.EEG,holder.set)
        self.muse._apply_callback(pyrnassus.EEG,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")
        
    def test_eeg_quantization(self):
        """ Check EEG_QUANTIZAION sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.EEG_QUANTIZAION,holder.set)
        self.muse._apply_callback(pyrnassus.EEG_QUANTIZAION,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_dropped_samples(self):
        """ Check EEG_DROPPED_SAMPLES sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.EEG_DROPPED_SAMPLES,holder.set)
        self.muse._apply_callback(pyrnassus.EEG_DROPPED_SAMPLES,1)
        self.assertEquals(holder.value,1,"dropped samples value is 1")
        
    def test_acc(self):
        """ Check ACC sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ACC,holder.set)
        self.muse._apply_callback(pyrnassus.ACC,[1,2,3])
        self.assertEquals(holder.value.x,1,"acc x value is 1")
        self.assertEquals(holder.value.y,2,"acc y value is 2")
        self.assertEquals(holder.value.z,3,"acc y value is 3")

    def test_acc_dropped_samples(self):
        """ Check ACC_DROPPED_SAMPLES sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ACC_DROPPED_SAMPLES,holder.set)
        self.muse._apply_callback(pyrnassus.ACC_DROPPED_SAMPLES,1)
        self.assertEquals(holder.value,1,"dropped samples value is 1")

    def test_batt(self):
        """ Check BATT sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.BATT,holder.set)
        self.muse._apply_callback(pyrnassus.BATT,[5132,2,3,4])
        self.assertEquals(holder.value.charge,51.32,"charge is 51.32")
        self.assertEquals(holder.value.mvFuelGauge,2,"mvFuelGauge is 2")
        self.assertEquals(holder.value.mvACD,3,"mvACD value is 3")
        self.assertEquals(holder.value.temperature,4,"temp value is 4")

    def test_reference(self):
        """ Check DRLREF sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.DRLREF,holder.set)
        self.muse._apply_callback(pyrnassus.DRLREF,[1,2])
        self.assertEquals(holder.value.drl,1,"drl is 1")
        self.assertEquals(holder.value.ref ,2,"ref is 2")

    def test_config(self):
        """ Check CONFIG sanity """
        holder=Holder()
        self.muse.register_callback(pyrnassus.CONFIG,holder.set)
        self.muse._apply_callback(pyrnassus.CONFIG,'{"message":"hello"}')
        self.assertEquals(holder.value["message"],"hello","message is hello")

    def test_version(self):
        """ Check CONFIG sanity """
        holder=Holder()
        self.muse.register_callback(pyrnassus.CONFIG,holder.set)
        self.muse._apply_callback(pyrnassus.CONFIG,'{"message":"hello"}')
        self.assertEquals(holder.value["message"],"hello","message is hello")

    def test_annotation(self):
        """ Check ANNOTATION sanity """
        holder=Holder()
        self.muse.register_callback(pyrnassus.ANNOTATION,holder.set)
        self.muse._apply_callback(pyrnassus.ANNOTATION,["a","b","c","d","e"])
        self.assertEquals(holder.value.data,"a","data is set to a")
        self.assertEquals(holder.value.format,"b","format is set to b")
        self.assertEquals(holder.value.type,"c","typeis set to c")
        self.assertEquals(holder.value.event_id,"d","event_id is set to e")
        self.assertEquals(holder.value.parent_id,"e","parent_id set to d")

    def test_fft_tp9(self):
        """ Check ELEMENTS_RAW_FFT_TP9 sanity """
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_RAW_FFT_TP9,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_RAW_FFT_TP9,[1,2,3])
        self.assertEquals(len(holder.value),3,"data len makes sense")
        self.assertEquals(holder.value[0],1,"idx 0 is 1")
        self.assertEquals(holder.value[1],2,"idx 0 is 2")
        self.assertEquals(holder.value[2],3,"idx 0 is 3")

    def test_fft_fp1(self):
        """ Check ELEMENTS_RAW_FFT_FP1 sanity """
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_RAW_FFT_FP1,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_RAW_FFT_FP1,[1,2,3])
        self.assertEquals(len(holder.value),3,"data len makes sense")
        self.assertEquals(holder.value[0],1,"idx 0 is 1")
        self.assertEquals(holder.value[1],2,"idx 0 is 2")
        self.assertEquals(holder.value[2],3,"idx 0 is 3")

    def test_fft_fp2(self):
        """ Check ELEMENTS_RAW_FFT_FP1 sanity """
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_RAW_FFT_FP2,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_RAW_FFT_FP2,[1,2,3])
        self.assertEquals(len(holder.value),3,"data len makes sense")
        self.assertEquals(holder.value[0],1,"idx 0 is 1")
        self.assertEquals(holder.value[1],2,"idx 0 is 2")
        self.assertEquals(holder.value[2],3,"idx 0 is 3")

    def test_fft_tp10(self):
        """ Check ELEMENTS_RAW_FFT_FP1 sanity """
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_RAW_FFT_TP10,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_RAW_FFT_TP10,[1,2,3])
        self.assertEquals(len(holder.value),3,"data len makes sense")
        self.assertEquals(holder.value[0],1,"idx 0 is 1")
        self.assertEquals(holder.value[1],2,"idx 0 is 2")
        self.assertEquals(holder.value[2],3,"idx 0 is 3")

    def test_elements_low_freqs_absolute(self):
        """ Check ELEMENTS_LOW_FREQS_ABSOLUTE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_LOW_FREQS_ABSOLUTE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_LOW_FREQS_ABSOLUTE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_delta_absolute(self):
        """ Check ELEMENTS_DELTA_ABSOLUTE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_DELTA_ABSOLUTE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_DELTA_ABSOLUTE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_theta_absolute(self):
        """ Check ELEMENTS_THETA_ABSOLUTE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_THETA_ABSOLUTE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_THETA_ABSOLUTE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_alpha_absolute(self):
        """ Check ELEMENTS_ALPHA_ABSOLUTE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_ALPHA_ABSOLUTE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_ALPHA_ABSOLUTE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_beta_absolute(self):
        """ Check ELEMENTS_BETA_ABSOLUTE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_BETA_ABSOLUTE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_BETA_ABSOLUTE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_gamma_absolute(self):
        """ Check ELEMENTS_GAMMA_ABSOLUTE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_GAMMA_ABSOLUTE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_GAMMA_ABSOLUTE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")



    def test_elements_delta_relative(self):
        """ Check ELEMENTS_DELTA_RELATIVE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_DELTA_RELATIVE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_DELTA_RELATIVE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_theta_relative(self):
        """ Check ELEMENTS_THETA_RELATIVE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_THETA_RELATIVE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_THETA_RELATIVE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_alpha_relative(self):
        """ Check ELEMENTS_ALPHA_RELATIVE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_ALPHA_RELATIVE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_ALPHA_RELATIVE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_beta_relative(self):
        """ Check ELEMENTS_BETA_RELATIVE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_BETA_RELATIVE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_BETA_RELATIVE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_gamma_relative(self):
        """ Check ELEMENTS_GAMMA_RELATIVE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_GAMMA_RELATIVE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_GAMMA_RELATIVE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_delta_session_score(self):
        """ Check ELEMENTS_DELTA_SESSION_SCORE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_DELTA_SESSION_SCORE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_DELTA_SESSION_SCORE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_theta_session_score(self):
        """ Check ELEMENTS_THETA_SESSION_SCORE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_THETA_SESSION_SCORE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_THETA_SESSION_SCORE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_alpha_session_score(self):
        """ Check ELEMENTS_ALPHA_SESSION_SCORE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_ALPHA_SESSION_SCORE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_ALPHA_SESSION_SCORE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_beta_session_score(self):
        """ Check ELEMENTS_BETA_SESSION_SCORE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_BETA_SESSION_SCORE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_BETA_SESSION_SCORE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_gamma_session_score(self):
        """ Check ELEMENTS_GAMMA_SESSION_SCORE sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_GAMMA_SESSION_SCORE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_GAMMA_SESSION_SCORE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_elements_touching_forehead(self):
        """ Check ELEMENTS_TOUCHING_FOREHEAD sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_TOUCHING_FOREHEAD,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_TOUCHING_FOREHEAD,1)
        self.assertEquals(holder.value,1,"touching is 1")

    def test_elements_touching_forehead(self):
        """ Check EEG_DROPPED_SAMPLES sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_TOUCHING_FOREHEAD,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_TOUCHING_FOREHEAD,1)
        self.assertEquals(holder.value,1,"touching is 1")

    def test_horseshoe(self):
        """ Check horseshoe sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_HORSESHOE,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_HORSESHOE,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

    def test_is_good(self):
        """ Check is_good sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_IS_GOOD,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_IS_GOOD,[1,2,3,4])
        self.assertEquals(holder.value.TP9,1,"TP9 value is 1")
        self.assertEquals(holder.value.FP1,2,"FP1 value is 2")
        self.assertEquals(holder.value.FP2,3,"FP2 value is 3")
        self.assertEquals(holder.value.TP10,4,"TP10 value is 4")

            
    def test_elements_blink(self):
        """ Check BLINK sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_BLINK,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_BLINK,1)
        self.assertEquals(holder.value,1,"blink is 1")

    def test_elements_jaw_clench(self):
        """ Check JAW_CLENCH sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.ELEMENTS_JAW_CLENCH,holder.set)
        self.muse._apply_callback(pyrnassus.ELEMENTS_JAW_CLENCH,1)
        self.assertEquals(holder.value,1,"jaw_clench is 1")

    def test_elements_concentration(self):
        """ Check concentration sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.EXPERIMENTAL_CONCENTRATION,holder.set)
        self.muse._apply_callback(pyrnassus.EXPERIMENTAL_CONCENTRATION,1)
        self.assertEquals(holder.value,1,"concetration is 1")

    def test_elements_mellow(self):
        """ Check mellow sanity"""
        holder=Holder()
        self.muse.register_callback(pyrnassus.EXPERIMENTAL_MELLOW,holder.set)
        self.muse._apply_callback(pyrnassus.EXPERIMENTAL_MELLOW,1)
        self.assertEquals(holder.value,1,"mellow is 1")
    
class Holder(object):


    def __init__(self):
        self.value=None

    def set(self,value):
        self.value=value
        
