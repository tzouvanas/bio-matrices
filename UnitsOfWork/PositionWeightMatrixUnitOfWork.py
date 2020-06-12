from matrices.PositionWeightMatrix import PositionWeightMatrix


class PositionWeightMatrixUnitOfWork:

    def go(self):
        
        wm = PositionWeightMatrix()
        wm.add_sequence("TATAGA")
        wm.add_sequence("TATAAA")
        wm.add_sequence("TATAGA")
        wm.add_sequence("TATAAA")
        wm.add_sequence("GATAGT")
        wm.add_sequence("TATAAT")
        wm.add_sequence("TATAAT")
        wm.add_sequence("TATAGT")
        wm.update()
        wm.print()

        wm.print_score("TATAAA")
        wm.print_score("GATAAA")
        wm.print_score("TAATAA")
