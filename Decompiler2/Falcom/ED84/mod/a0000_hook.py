from Falcom.ED84.Parser.scena_writer_helper import *

def funcCallBack(name: str, f: Callable):
    match name:
        case 'TK_MiniGame_Debug': return TK_MiniGame_Debug
        case _: pass

    pass

def _init():
    from Falcom.ED84.Parser.scena_writer import _gScena as scena
    scena.registerFuncCallback(funcCallBack)

_init()

def TK_MiniGame_Debug():
    PlayBGM(922, 1.0, 0x0000, 0x00000000, 0x00)

    chrmap = {
        ChrTable['黎恩']: 0x2001, #ChrTable['鋼之阿瑞安赫德'],
    }

    for chrid, newchrid in chrmap.items():
        notset = genLabel()
        end = genLabel()

        If(
            (
                (Expr.Eval, f'ModelGetBattleStyle({chrid})'),
                # (Expr.PushLong, 0),
                # Expr.Equ,
                Expr.Ez,
                Expr.Return,
            ),
            notset,
        )

        DebugString('set chrid')

        ModelSetChrId(chrid, newchrid)
        ModelSetBattleStyle(chrid, newchrid)

        Jump(end)

        label(notset)

        DebugString('unset chrid')

        ModelSetChrId(chrid, chrid)
        ModelSetBattleStyle(chrid, 0)

        label(end)

        AnimeClipRefreshSkin(chrid)

    FormationReset(0)
    FormationAddMember(0x00)
    FormationSetLeader(0)

    # Battle(0x00, 0x00000005, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    return Return()