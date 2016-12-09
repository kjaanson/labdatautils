from unittest import TestCase
import pandas as pd

from pandas.util.testing import assert_frame_equal
from labdatautils.legacy import load_file, vs_control

"""Legacy functionality tests.
Tests all functions that are used in old scripts module used in notebooks.
If functionality is changed this should support it for awhile."""

class TestLLegacy(TestCase):

    def test_load_file_2ID(self):
        """Tests Tecan exported Excel measurement file loading."""

        df_2id_headerless_small = pd.DataFrame({
            'Konstruktid': ["rBDNF-luc2P", "rBDNF-luc2P", "rBDNF-luc2P", "rBDNF-luc2P", "rBDNF-luc2P", "rBDNF-luc2P",
                            "rBDNF-luc2P",
                            "rBDNF-luc2P", "rBDNF-luc2P", "rBDNF-luc2P", "rBDNF-luc2P", "Cherry", "hBDNF-luc2P-EF1a",
                            "hBDNF-luc2P-EF1a",
                            "hBDNF-luc2P-EF1a", "hBDNF-luc2P-EF1a", "hBDNF-luc2P-EF1a", "hBDNF-luc2P-EF1a",
                            "hBDNF-luc2P-EF1a",
                            "hBDNF-luc2P-EF1a", "hBDNF-luc2P-EF1a", "hBDNF-luc2P-EF1a", "hBDNF-luc2P-EF1a"],
            'Treatments': ["DMSO", "DMSO", "DMSO", "NE 25uM", "NE 25uM", "NE 25uM", "DA 150uM", "DA 150uM", "DA 150uM",
                           "untreat (+FBS)", "untreat (+FBS)", "none", "DMSO", "DMSO", "DMSO", "NE 25uM", "NE 25uM",
                           "NE 25uM", "DA 150uM", "DA 150uM", "DA 150uM", "untreat (+FBS)", "untreat (+FBS)"],
            'fluc': [75, 83, 78, 473, 346, 425, 446, 385, 408, 131, 107, 48, 131, 175, 131, 440, 402, 354, 405, 430,
                     437,
                     238, 236],
            'rluc': [64, 58, 46, 65, 45, 71, 48, 56, 63, 58, 60, 52, 1200, 1263, 1056, 1322, 1377, 1225, 1164, 1004,
                     1145,
                     2797, 2378],
        })

        df = load_file('test_files/tecan_2id_headerless_small.xlsx', fluc='luc2P', rluc='hrlucP')
        assert_frame_equal(df, df_2id_headerless_small)

    def test_vs_control(self):
        """Test in experiment normalisation to control."""

        df_normalised_correct = pd.DataFrame({
            'Konstruktid': ["pConst1", "pConst1", "pConst3", "pConst3"],
            'Treatments': ["Control", "Treat1", "Control", "Treat1"],
            'fluc': [25, 50, 30, 75],
            'vs Control': [1., 2., 1., 2.5]
        })

        df_experiment_sample = pd.DataFrame({
            'Konstruktid': ["pConst1", "pConst1", "pConst1", "pConst1", "pConst3", "pConst3", "pConst3", "pConst3",
                            "pConst1",
                            "pConst1", "pConst1", "pConst1", "pConst3", "pConst3", "pConst3", "pConst3"],
            'Treatments': ["Control", "Control", "Treat1", "Treat1", "Control", "Control", "Treat1", "Treat1",
                           "Control",
                           "Control",
                           "Treat1", "Treat1", "Control", "Control", "Treat1", "Treat1"],
            'fluc': [25, 25, 50, 50, 30, 30, 75, 75, 25, 25, 50, 50, 30, 30, 75, 75],
        })

        df_normalised = vs_control(df_experiment_sample, control="Control", norm_col="fluc")
        assert_frame_equal(df_normalised, df_normalised_correct)
