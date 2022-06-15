import surmin.example.SurMin as sm


def test_solve():
    def get_sigCV( Penal, iter ):
        return (Penal[0]-1)**2

    sm.SurMin ( 30, [0.0001], 1e-5, [0.5], get_sigCV )




