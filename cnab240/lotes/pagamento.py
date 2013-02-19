
from cnab240.tipos import LoteBase

class LotePagamento(LoteBase):
    HeaderCls = LotePagamento.banco.registros.HeaderLotePagamento
    TrailerCls = LotePagamento.banco.registros.TrailerLotePagamento

