

class MLToDBMapper:

    @staticmethod
    def mltodb(mlid):
        labels = {
            0: 8,
            1: 13,
            2: 14,
            3: 10,
            4: 6,
            5: 11,
            6: 7,
            7: 1,
            8: 4,
            9: 9,
            10: 5,
            11: 12,
            12: 15,
            13: 3,
            14: 2,
            15: 16
        }
        return labels[mlid]

    @staticmethod
    def dbtoml(dbid):
        labels = {
            8: 0,
            13: 1,
            14: 2,
            10: 3,
            6: 4,
            11: 5,
            7: 6,
            1: 7,
            4: 8,
            9: 9,
            5: 10,
            12: 11,
            15: 12,
            3: 13,
            2: 14,
            16: 15,
        }
        return labels[dbid]

