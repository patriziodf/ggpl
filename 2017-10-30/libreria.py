from larlib import *
def ggpl_stairBookcase2(dx, dy, dz):


    struttura_esterna = STRUCT([T([1, 2, 3])([0, 0.7, 0.02])(CUBOID([0.02, 0.33, 2.66])),
                                T([2, 3])([1.03, 0.02])(CUBOID([3.10, 0.02, 2.68])),
                                T(1)(3.08)(CUBOID([0.02, 1.03, 2.7])),
                                T([2, 3])([0.7, 2.68])(CUBOID([3.08, 0.35, 0.02])),
                                T(2)(0.7)(CUBOID([3.08, 0.35, 0.02]))])

    tavole_v = CUBOID([0.02, 0.33, 2.66])
    blocchi_v = []
    for i in range(1, 14): blocchi_v.append(T([1, 2, 3])([0.2 * i + 0.02 * i, 0.7, 0.02])(tavole_v))

    tavole_h = CUBOID([0.2, 0.33, 0.02])
    blocchi_h = []
    for i in range(1, 15):
        if i % 2 == 1:
            for k in range(1, 6):
                blocchi_h.append(
                    T([1, 2, 3])([0.2 * (i - 1) + 0.02 * i, 0.7, 0.47 * k + 0.02 * k])(tavole_h))

        else:
            blocchi_h.append(T([1, 2, 3])([0.2 * (i - 1) + 0.02 * i, 0.7, 0.23])(tavole_h))
            for k in range(1, 5):
                blocchi_h.append(
                    T([1, 2, 3])([0.2 * (i - 1) + 0.02 * i, 0.7, 0.47 * k + 0.23 + 0.02 * k])(tavole_h))

    scale_base = T(1)(0.66)(CUBOID([2.42, 0.7, 0.02]))
    scale_blocchi = CUBOID([0.22, 0.7, 0.02])
    scale = []
    scale_sotto = []

    for i in range(4, 15):
        if i % 2 == 0:
            scale_sotto.append(T([1, 3])([0.2 * (i - 1) + 0.02 * (i - 1), 0.02])(
                CUBOID([0.02, 0.7, 0.21 + 0.235 * (i - 4) + 0.02 * ((i / 2) - 2)])))
            scale.append(
                T([1, 3])([0.2 * (i - 1) + 0.02 * (i - 1), 0.21 + 0.235 * (i - 4) + 0.02 * ((i / 2) - 1)])(scale_blocchi))
            blocchi_h.append(T([1, 3])([0.2 * (i - 1) + 0.02 * i, 0.23])(CUBOID([0.2, 0.7, 0.02])))
            for k in range(2, (i / 2) - 1):
                blocchi_h.append(T([1, 3])([0.2 * (i - 1) + 0.02 * i, 0.47 * (k - 1) + 0.02 * (k - 1) + 0.23])(
                    CUBOID([0.2, 0.7, 0.02])))
        else:
            scale_sotto.append(T([1, 3])([0.2 * (i - 1) + 0.02 * (i - 1), 0.02])
                               (CUBOID([0.02, 0.7, 0.47 * ((i / 2) - 1) + 0.02 * ((i / 2) - 2)])))
            scale.append(
                T([1, 3])([0.2 * (i - 1) + 0.02 * (i - 1), 0.47 * ((i / 2) - 1) + 0.02 * ((i / 2) - 1)])(scale_blocchi))
            for k in range(2, (i / 2)):
                blocchi_h.append(
                    T([1, 3])([0.2 * (i - 1) + 0.02 * i, 0.47 * (k - 1) + 0.02 * (k - 1)])(CUBOID([0.2, 0.7, 0.02])))

    firstBlockStructure = STRUCT([struttura_esterna, STRUCT(blocchi_v), STRUCT(blocchi_h)])
    StairStructure = STRUCT([scale_base, STRUCT(scale_sotto), STRUCT(scale)])
    bookcase = TEXTURE("wood2.png")(STRUCT([firstBlockStructure, StairStructure]))


    return S([1, 2, 3])([dx, dy, dz])(bookcase)

#dx, dy, dz = 6, 3, 4
#VIEW(ggpl_stairBookcase2(dx, dy, dz))