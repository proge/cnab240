
from cnab240.tipos import EventoBase


class EventoInclusao(EventoBase):
    def __init__(self, banco, **kwargs):
        super(EventoInclusao, self).__init__(banco, 1)
        args = self.clean_kwargs(kwargs)

        seg_a = self.banco.registros.SegmentoA(**args)
        self.adicionar_segmento(seg_a)

        seg_b = self.banco.registros.SegmentoB(**args)
        self.adicionar_segmento(seg_b)

        seg_c = self.banco.registros.SegmentoC(**args)
        self.adicionar_segmento(seg_c)

