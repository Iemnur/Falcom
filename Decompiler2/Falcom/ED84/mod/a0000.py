import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED84.Parser.scena_writer_helper import *
import a0000_hook

scena = createScenaWriter('a0000.dat')

# id: 0x0000 offset: 0x1708
@scena.Code('')
def func_1708():
    Return()

# id: 0x0001 offset: 0x170C
@scena.BattleSetting('BTLSET000')
def BTLSET000():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = 20.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 477,
        dangerBGM      = 456,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_1', 'mon999_1', 'mon998_1', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0002 offset: 0x180C
@scena.BattleSetting('BTLSET001')
def BTLSET001():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 0.0,
        y              = 0.0,
        z              = 0.0,
        direction      = 0.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 477,
        dangerBGM      = 456,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_1', 'mon999_1', 'mon999_1', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0003 offset: 0x190C
@scena.BattleSetting('BTLSET002')
def BTLSET002():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 474,
        dangerBGM      = 456,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon996', 'mon996', 'mon999', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0004 offset: 0x1A0C
@scena.BattleSetting('BTLSET003')
def BTLSET003():
    return ScenaBattleSetting(
        mapName        = 'm6090',
        x              = -72.16000366210938,
        y              = -0.3799999952316284,
        z              = 103.2300033569336,
        direction      = 131.89999389648438,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000001,
        bgm            = 720,
        dangerBGM      = 720,
        word34         = 0,
        word36         = 0,
        atBonus        = 3,
        battleScript   = 'btl0257',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_1', 'mon999_1', 'mon999_1', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0005 offset: 0x1B0C
@scena.BattleSetting('BTLSETEXP')
def BTLSETEXP():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_0', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0006 offset: 0x1C0C
@scena.BattleSetting('BTLSETMANY')
def BTLSETMANY():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_1', 'mon999_1', 'mon999_1', 'mon999_1', 'mon999_1', 'mon999_1', 'mon999_1', 'mon999_1'],
                encounterProbability    = [100, 100, 100, 100, 100, 100, 100, 100],
            ),
        ],
    )

# id: 0x0007 offset: 0x1D0C
@scena.BattleSetting('BTLSETGEN')
def BTLSETGEN():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 0.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0008',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon996_0', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0008 offset: 0x1E0C
@scena.BattleSetting('BTLSET_NORESULT')
def BTLSET_NORESULT():
    return ScenaBattleSetting(
        mapName        = 'm6090',
        x              = 0.0,
        y              = 0.0,
        z              = 0.0,
        direction      = 0.0,
        length         = 20.0,
        width          = 20.0,
        word28         = 259,
        flags          = 0x00000001,
        bgm            = 720,
        dangerBGM      = 720,
        word34         = 0,
        word36         = 0,
        atBonus        = 3,
        battleScript   = 'btl0259',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr001_9', 'chr000_c11', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0009 offset: 0x1F0C
@scena.BattleSetting('BTLSETBONUS')
def BTLSETBONUS():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 10,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_1', 'mon999_1', 'mon999_1', 'mon999_1', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 100, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x000A offset: 0x200C
@scena.BattleSetting('BTLSET_TRIAL01')
def BTLSET_TRIAL01():
    return ScenaBattleSetting(
        mapName        = 'be0000',
        x              = 0.0,
        y              = 0.0,
        z              = 0.0,
        direction      = 0.0,
        length         = 20.0,
        width          = 20.0,
        word28         = 950,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_1', 'mon999_1', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x000B offset: 0x210C
@scena.BattleSetting('BTLSETDEBUG')
def BTLSETDEBUG():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 9,
        flags          = 0x00000000,
        bgm            = 477,
        dangerBGM      = 456,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x000C offset: 0x220C
@scena.BattleSetting('BTLSETDEBUG2')
def BTLSETDEBUG2():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 9,
        flags          = 0x00000000,
        bgm            = 477,
        dangerBGM      = 456,
        word34         = 0,
        word36         = 0,
        atBonus        = 10,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x000D offset: 0x230C
@scena.BattleSetting('BTLSETDEBUG3')
def BTLSETDEBUG3():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 200.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 9,
        flags          = 0x00000000,
        bgm            = 477,
        dangerBGM      = 456,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x000E offset: 0x240C
@scena.BattleSetting('BTLSET_QS343_02')
def BTLSET_QS343_02():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 904,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0904',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr003', 'chr035_c00', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x000F offset: 0x250C
@scena.BattleSetting('BTLSET_ID02E_00')
def BTLSET_ID02E_00():
    return ScenaBattleSetting(
        mapName        = 'm7420',
        x              = -60.0,
        y              = 16.0,
        z              = 5.0,
        direction      = 0.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 311,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0311',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr381', 'chr382', 'chr382', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0010 offset: 0x260C
@scena.BattleSetting('BTLSET_ID03B_01')
def BTLSET_ID03B_01():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 354,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0354',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr736', 'chr737', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0011 offset: 0x270C
@scena.BattleSetting('BTLSET_ID01B_05')
def BTLSET_ID01B_05():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 208,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0208',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr030', 'chr076', 'chr074', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0012 offset: 0x280C
@scena.BattleSetting('BTLSET_ID01B_05_B')
def BTLSET_ID01B_05_B():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 311,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0208',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr030', 'chr076', '0', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0013 offset: 0x290C
@scena.BattleSetting('BTLSET_ID01C_00')
def BTLSET_ID01C_00():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 209,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0209',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr064', 'chr031_c00', 'chr617', 'chr215', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 100, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0014 offset: 0x2A0C
@scena.BattleSetting('BTLSET_ID01D_02')
def BTLSET_ID01D_02():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 212,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0212',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr032', 'chr025_c01', 'chr024', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0015 offset: 0x2B0C
@scena.BattleSetting('BTLSET_ID01X_03')
def BTLSET_ID01X_03():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 253,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0253',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr103_c00', 'chr103', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0016 offset: 0x2C0C
@scena.BattleSetting('BTLSET_ID01X_06')
def BTLSET_ID01X_06():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 256,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0256',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr034_c00', 'chr039', 'chr037', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0017 offset: 0x2D0C
@scena.BattleSetting('BTLSET_ID01X_08')
def BTLSET_ID01X_08():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 258,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0258',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr078', 'chr033', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0018 offset: 0x2E0C
@scena.BattleSetting('BTLSET_ID02B_02')
def BTLSET_ID02B_02():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 304,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0304',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr023', 'chr019_0', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0019 offset: 0x2F0C
@scena.BattleSetting('BTLSET_ID02C_01')
def BTLSET_ID02C_01():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 306,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0306',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr056_c00', 'chr062', '', '3411', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x001A offset: 0x300C
@scena.BattleSetting('BTLSET_ID02E_02')
def BTLSET_ID02E_02():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 313,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0313',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr024_0', 'chr074_0', 'chr076_0', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x001B offset: 0x310C
@scena.BattleSetting('BTLSET_ID02E_04')
def BTLSET_ID02E_04():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 315,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0315',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr101', 'chr032', 'chr031_c00_0', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x001C offset: 0x320C
@scena.BattleSetting('BTLSET_ID02E_05')
def BTLSET_ID02E_05():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 316,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0316',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr064_0', 'chr030_0', 'chr072_0', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x001D offset: 0x330C
@scena.BattleSetting('BTLSET_ID02D_03')
def BTLSET_ID02D_03():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 310,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0310',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr040', 'chr617_0', 'chr215_0', 'chr618', 'chr216', 'chr216', '', ''],
                encounterProbability    = [100, 100, 100, 100, 100, 100, 0, 0],
            ),
        ],
    )

# id: 0x001E offset: 0x340C
@scena.BattleSetting('BTLSET_ID04_07')
def BTLSET_ID04_07():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 407,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0407',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr032', 'chr101', 'mon999', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x001F offset: 0x350C
@scena.BattleSetting('BTLSET_ID04_08')
def BTLSET_ID04_08():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 8.0,
        width          = 20.0,
        word28         = 408,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0408',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr022_c01', 'chr070', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0020 offset: 0x360C
@scena.BattleSetting('BTLSET_ID05_00')
def BTLSET_ID05_00():
    return ScenaBattleSetting(
        mapName        = 'm9101',
        x              = 0.0,
        y              = 0.0,
        z              = 0.0,
        direction      = 0.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 500,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 1,
        battleScript   = 'btl0500',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon461', 'mon461_c00', 'mon461_c01', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0021 offset: 0x370C
@scena.BattleSetting('BTLSET_ID05_00B')
def BTLSET_ID05_00B():
    return ScenaBattleSetting(
        mapName        = 'm9101',
        x              = 0.0,
        y              = 0.0,
        z              = 0.0,
        direction      = 0.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 501,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 1,
        battleScript   = 'btl0500',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon461', 'mon461_c00', 'mon461_c01', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0022 offset: 0x380C
@scena.BattleSetting('BTLSET_ID05_00C')
def BTLSET_ID05_00C():
    return ScenaBattleSetting(
        mapName        = 'm9101',
        x              = 0.0,
        y              = 0.0,
        z              = 0.0,
        direction      = 0.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 502,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 1,
        battleScript   = 'btl0500',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon461', 'mon461_c00', 'mon461_c01', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0023 offset: 0x390C
@scena.BattleSetting('BTLSET_EV98')
def BTLSET_EV98():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl0001',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon999_1', 'mon999_1', 'mon999_1', '', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0024 offset: 0x3A0C
@scena.BattleSetting('BTLSET_EV99')
def BTLSET_EV99():
    return ScenaBattleSetting(
        mapName        = '',
        x              = 100.0,
        y              = -100.0,
        z              = 100.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 0,
        flags          = 0x00000000,
        bgm            = 0,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = '',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['mon148', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
            ScenaBattleMonsterSet(
                id                      = 0x1,
                monsters                = ['mon148', 'mon148', '', '', '', '', '', ''],
                encounterProbability    = [100, 100, 0, 0, 0, 0, 0, 0],
            ),
            ScenaBattleMonsterSet(
                id                      = 0x2,
                monsters                = ['mon148', 'mon148', 'mon148', 'mon148', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 100, 0, 0, 0, 0],
            ),
            ScenaBattleMonsterSet(
                id                      = 0x3,
                monsters                = ['mon148', 'mon148', 'mon148', 'mon148', 'mon148', 'mon148', '', ''],
                encounterProbability    = [100, 100, 100, 100, 100, 100, 0, 0],
            ),
        ],
    )

# id: 0x0025 offset: 0x3CC8
@scena.BattleSetting('BTLSET1000')
def BTLSET1000():
    return ScenaBattleSetting(
        mapName        = 't0280',
        x              = 0.0,
        y              = 0.0,
        z              = 0.0,
        direction      = 0.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 1098,
        flags          = 0x00000000,
        bgm            = 452,
        dangerBGM      = 0,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl1098',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['rob030s_0', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0026 offset: 0x3DC8
@scena.Code('PreInit')
def PreInit():
    OP_14(0x80000000)
    OP_13(0x00400000)
    SetScenaFlags(ScenaFlag(0x0062, 2, 0x312))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            Expr.Return,
        ),
        'loc_3DE7',
    )

    SetScenaFlags(ScenaFlag(0x0060, 5, 0x305))
    SetScenaFlags(ScenaFlag(0x0061, 0, 0x308))
    SetScenaFlags(ScenaFlag(0x0061, 1, 0x309))

    def _loc_3DE7(): pass

    label('loc_3DE7')

    Return()

# id: 0x0027 offset: 0x3DE8
@scena.Code('Init')
def Init():
    OP_3A(0x05, 0x0001, 0x0001)
    OP_3A(0x06, 0x0001)
    OP_14(0x00000400)
    OP_3B(0x64, 1000, 0.0, 1.0)
    OP_3A(0x01, 0x02C7, 0x01)
    ModelCtrl(0x0D, 'TrialBox01', 'LP_trialbox01', 0x17B0, 0x270F)

    If(
        (
            (Expr.Eval, "ModelCtrl(0x20)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E36',
    )

    FormationCtrl(0x1C, 0x00)

    def _loc_3E36(): pass

    label('loc_3E36')

    Return()

# id: 0x0028 offset: 0x3E38
@scena.Code('Reinit')
def Reinit():
    OP_AC(0x00, 0x03)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            Expr.Return,
        ),
        'loc_3E5D',
    )

    CreateThread(0xFFFF, 0x00, ScriptId.Current, 'EV_Test_Evsave_Load')

    def _loc_3E5D(): pass

    label('loc_3E5D')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x3B6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EAE',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EA5',
    )

    SetScenaFlags(ScenaFlag(0x02F6, 0, 0x17B0))
    SetLookpointFlag(0x01, 'LP_trialbox01', 0x0001)
    CreateThread(0xFFFF, 0x00, ScriptId.Current, 'LP_trialbox01_Get')

    def _loc_3EA5(): pass

    label('loc_3EA5')

    OP_08(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3EAE(): pass

    label('loc_3EAE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_423B',
    )

    CreateChr(0x03EC, 'C_CHR027', '迷你游戏测试', '', 0x00, 0x00008000, 0x00000000, 4.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.3, '', 'TK_MiniGame_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    OP_9E(0x11, 1004, 1)
    OP_3A(0x04, 0x02C7, 1.0, 0x0000, 0x00000000, 0x00)
    CreateChr(0x03E8, 'C_MON999', '打C大倉鼠戰鬥測試', '', 0x00, 0x00008000, 0x00000000, 3.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Battle_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    OP_38(0x03E8, 0x00, 0x0A, 'AniAttachEQU350')
    CreateChr(0x03EA, 'C_CHR011_C10', '常用/任务测试', '', 0x00, 0x00008000, 0x00000000, 1.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Quest_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03E9, 'C_CHR000_C10', '事件跳转测试', '', 0x00, 0x00008000, 0x00000000, 0.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_EV_Jump', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03EB, 'C_CHR010_C10', '对话脚本测试', '', 0x00, 0x00008000, 0x00000000, -1.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_System_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03ED, 'C_CHR012_C10', '队伍相关測試', '', 0x00, 0x00008000, 0x00000000, -3.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Camp_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03EE, 'C_CHR013_C10', '手冊測試/管理', '', 0x00, 0x00008000, 0x00000000, -4.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Note_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03EF, 'C_CHR015_C10', '商店測試', '', 0x00, 0x00008000, 0x00000000, -6.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Shop_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    OP_86(0x01, 0x0000, 0x008E, 0x0000, 0x0000, 0x0000, 0x03EF, 0.0, 0.0, 0.0, '')

    Jump('loc_4556')

    def _loc_423B(): pass

    label('loc_423B')

    CreateChr(0x03EC, 'C_CHR999', '迷你游戏测试', '', 0x00, 0x00008000, 0x00000000, 4.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.3, '', 'TK_MiniGame_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03E8, 'C_CHR999', '打C大倉鼠戰鬥測試', '', 0x00, 0x00008000, 0x00000000, 3.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Battle_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03EA, 'C_CHR999', '常用/任务测试', '', 0x00, 0x00008000, 0x00000000, 1.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Quest_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03E9, 'C_CHR999', '任务跳转测试', '', 0x00, 0x00008000, 0x00000000, 0.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_EV_Jump', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03EB, 'C_CHR999', '对话脚本测试', '', 0x00, 0x00008000, 0x00000000, -1.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_System_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03ED, 'C_CHR999', '队伍测试', '', 0x00, 0x00008000, 0x00000000, -3.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Camp_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03EE, 'C_CHR999', '手冊測試/管理', '', 0x00, 0x00008000, 0x00000000, -4.5, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Note_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x03EF, 'C_CHR999', '商店測試', '', 0x00, 0x00008000, 0x00000000, -6.0, 0.0, -1.0, 0.0, 1.0, 1.6, 0.2, '', 'TK_Shop_Debug', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)

    def _loc_4556(): pass

    label('loc_4556')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['妙婕'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['米莉亞姆'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000004)

    Return()

# id: 0x0029 offset: 0x45D8
@scena.Code('TK_Event_Jump_Test')
def TK_Event_Jump_Test():
    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '克蕾雅測試', 0x00000002)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_4625'),
        (0x00000002, 'loc_4641'),
        (-1, 'loc_465D'),
    )

    def _loc_4625(): pass

    label('loc_4625')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x9999, 0x0))

    Jump('loc_465D')

    def _loc_4641(): pass

    label('loc_4641')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x9998, 0x0))

    Jump('loc_465D')

    def _loc_465D(): pass

    label('loc_465D')

    Return()

# id: 0x002A offset: 0x4660
@scena.Code('TK_QuestUI_Debug')
def TK_QuestUI_Debug():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4669(): pass

    label('loc_4669')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5297',
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '▼任务确认画面（手冊）', 0x00000064)
    MenuCmd(0x01, 0x01, '▼任务确认画面（電腦）', 0x00000065)
    MenuCmd(0x01, 0x01, '▼AP加算+300', 0x0000006C)
    MenuCmd(0x01, 0x01, '▼分校充实度+10', 0x0000006D)
    MenuCmd(0x01, 0x01, '▼分校充实度+50', 0x0000006E)
    MenuCmd(0x01, 0x01, '▼学院等级+1', 0x0000006F)
    MenuCmd(0x01, 0x01, '▼学院等级复位', 0x00000070)
    MenuCmd(0x01, 0x01, '任务完成（获得奖金）', 0x00000078)
    MenuCmd(0x01, 0x01, '奖杯用任务完成', 0x00000082)
    MenuCmd(0x01, 0x01, '▼quest_check_report', 0x0000008C)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★I部①萨瑟兰特篇结束', 0x00000096)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅰ部休息日①结束', 0x00000097)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅰ部②结束', 0x00000098)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★I部分休息日②结束', 0x00000099)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★I部③克洛斯贝尔篇结束', 0x0000009A)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★断章结束', 0x0000009B)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅱ部第②部分结束', 0x0000009C)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅱ部③ドレクル篇结束', 0x0000009D)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅱ部④revs篇结束', 0x0000009E)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅱ部⑤潘塔格里尔篇结束', 0x0000009F)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅲ部③龙的灵场结束', 0x000000A0)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★Ⅲ部⑤星之灵场篇结束', 0x000000A1)
    MenuCmd(0x01, 0x01, '▼任务报告画面：★最后一幕・作战开始前', 0x000000A2)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000064, 'loc_4BA0'),
        (0x00000065, 'loc_4BB8'),
        (0x0000006C, 'loc_4BD0'),
        (0x0000006D, 'loc_4BDE'),
        (0x0000006E, 'loc_4BE9'),
        (0x0000006F, 'loc_4BF4'),
        (0x00000070, 'loc_4BFF'),
        (0x00000078, 'loc_4C10'),
        (0x00000082, 'loc_4C65'),
        (0x0000008C, 'loc_4C8D'),
        (0x00000096, 'loc_4D0F'),
        (0x00000097, 'loc_4D8B'),
        (0x00000098, 'loc_4DB0'),
        (0x00000099, 'loc_4DFD'),
        (0x0000009A, 'loc_4E49'),
        (0x0000009B, 'loc_4EB4'),
        (0x0000009C, 'loc_4F19'),
        (0x0000009D, 'loc_4F68'),
        (0x0000009E, 'loc_4FC8'),
        (0x0000009F, 'loc_5061'),
        (0x000000A0, 'loc_50B6'),
        (0x000000A1, 'loc_5186'),
        (0x000000A2, 'loc_51FD'),
        (-1, 'loc_5284'),
    )

    def _loc_4BA0(): pass

    label('loc_4BA0')

    OP_7C(0x00, 0x00, 0x0008, 0x000D, 0x270F, 0x270F, 0x270F, 0x270F, 0x270F)
    OP_7C(0x01)

    Jump('loc_5292')

    def _loc_4BB8(): pass

    label('loc_4BB8')

    OP_7C(0x00, 0x01, 0x0008, 0x000D, 0x270F, 0x270F, 0x270F, 0x270F, 0x270F)
    OP_7C(0x01)

    Jump('loc_5292')

    def _loc_4BD0(): pass

    label('loc_4BD0')

    OP_18(
        0x0F,
        (
            (Expr.PushLong, 0x12C),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_5292')

    def _loc_4BDE(): pass

    label('loc_4BDE')

    OP_87(0x00, 0x0000000A)

    Jump('loc_5292')

    def _loc_4BE9(): pass

    label('loc_4BE9')

    OP_87(0x00, 0x00000032)

    Jump('loc_5292')

    def _loc_4BF4(): pass

    label('loc_4BF4')

    OP_87(0x03, 0x00000001)

    Jump('loc_5292')

    def _loc_4BFF(): pass

    label('loc_4BFF')

    OP_87(0x01, 0x00000000)
    OP_87(0x02, 0x00000000)

    Jump('loc_5292')

    def _loc_4C10(): pass

    label('loc_4C10')

    OP_18(
        0x00,
        (
            (Expr.Eval, "QuestCtrl(0x0001, 0x07)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'クエスト報酬#1C#0G#0Cミラを獲得した。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_5292')

    def _loc_4C65(): pass

    label('loc_4C65')

    Call(ScriptId.Current, 'TK_QuestUI_DebugQuestFlag', (0xFF, 0x32, 0x0))

    Jump('loc_5292')

    def _loc_4C8D(): pass

    label('loc_4C8D')

    If(
        (
            (Expr.Eval, "OP_9C(0x02, 0x0005)"),
            Expr.Return,
        ),
        'loc_4CD2',
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '有可以报告最终章的任务',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_4D0A')

    def _loc_4CD2(): pass

    label('loc_4CD2')

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '没有可以报告最终章的任务',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    def _loc_4D0A(): pass

    label('loc_4D0A')

    Jump('loc_5292')

    def _loc_4D0F(): pass

    label('loc_4D0F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4D2B',
    )

    QuestCtrl(0x00C8, 0x03, 0x01, 0x02)
    QuestCtrl(0x00C8, 0x03, 0x02, 0x02)

    Jump('loc_4D37')

    def _loc_4D2B(): pass

    label('loc_4D2B')

    QuestCtrl(0x00C9, 0x03, 0x01, 0x02)
    QuestCtrl(0x00C9, 0x03, 0x02, 0x02)

    def _loc_4D37(): pass

    label('loc_4D37')

    QuestCtrl(0x00CA, 0x03, 0x01, 0x02)
    QuestCtrl(0x00CA, 0x03, 0x02, 0x02)
    QuestCtrl(0x00CB, 0x03, 0x01, 0x02)
    QuestCtrl(0x00CB, 0x03, 0x02, 0x02)
    QuestCtrl(0x00CC, 0x03, 0x01, 0x02)
    QuestCtrl(0x00CC, 0x03, 0x02, 0x02)
    QuestCtrl(0x00CD, 0x03, 0x01, 0x02)
    QuestCtrl(0x00CD, 0x03, 0x02, 0x02)
    QuestCtrl(0x0001, 0x03, 0x02, 0x02)
    QuestCtrl(0x0002, 0x03, 0x02, 0x02)
    QuestCtrl(0x0003, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x001F, 0x0001, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4D8B(): pass

    label('loc_4D8B')

    QuestCtrl(0x0004, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x001F, 0x0001, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x001F, 0x0001, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4DB0(): pass

    label('loc_4DB0')

    QuestCtrl(0x00CE, 0x03, 0x01, 0x02)
    QuestCtrl(0x00CE, 0x03, 0x02, 0x02)
    QuestCtrl(0x00CF, 0x03, 0x01, 0x02)
    QuestCtrl(0x00CF, 0x03, 0x02, 0x02)
    QuestCtrl(0x0005, 0x03, 0x02, 0x02)
    QuestCtrl(0x0006, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4DE5',
    )

    QuestCtrl(0x0006, 0x06, 0x0002)

    def _loc_4DE5(): pass

    label('loc_4DE5')

    QuestCtrl(0x0007, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x001F, 0x0002, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4DFD(): pass

    label('loc_4DFD')

    QuestCtrl(0x0008, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4E19',
    )

    QuestCtrl(0x0008, 0x06, 0x0002)

    Jump('loc_4E2A')

    def _loc_4E19(): pass

    label('loc_4E19')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4E2A',
    )

    QuestCtrl(0x0008, 0x06, 0x0001)

    def _loc_4E2A(): pass

    label('loc_4E2A')

    OP_9C(0x00, 0x00, 0x001F, 0x0002, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x001F, 0x0002, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4E49(): pass

    label('loc_4E49')

    QuestCtrl(0x00D0, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D0, 0x03, 0x02, 0x02)
    QuestCtrl(0x00D1, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D1, 0x03, 0x02, 0x02)
    QuestCtrl(0x00D2, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D2, 0x03, 0x02, 0x02)
    QuestCtrl(0x00D3, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D3, 0x03, 0x02, 0x02)
    QuestCtrl(0x0009, 0x03, 0x02, 0x02)
    QuestCtrl(0x000A, 0x03, 0x02, 0x02)
    QuestCtrl(0x000B, 0x03, 0x02, 0x02)
    QuestCtrl(0x000C, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4EA2',
    )

    QuestCtrl(0x000C, 0x06, 0x0002)

    def _loc_4EA2(): pass

    label('loc_4EA2')

    OP_9C(0x00, 0x00, 0x001F, 0x0003, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4EB4(): pass

    label('loc_4EB4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4ED0',
    )

    QuestCtrl(0x00D6, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D6, 0x03, 0x02, 0x02)

    Jump('loc_4EE8')

    def _loc_4ED0(): pass

    label('loc_4ED0')

    QuestCtrl(0x00D4, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D4, 0x03, 0x02, 0x02)
    QuestCtrl(0x00D5, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D5, 0x03, 0x02, 0x02)

    def _loc_4EE8(): pass

    label('loc_4EE8')

    QuestCtrl(0x00D7, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D7, 0x03, 0x02, 0x02)
    QuestCtrl(0x000D, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0xFFFF, 0x0003, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0xFFFF, 0x0003, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4F19(): pass

    label('loc_4F19')

    QuestCtrl(0x00D8, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D8, 0x03, 0x02, 0x02)
    QuestCtrl(0x00D9, 0x03, 0x01, 0x02)
    QuestCtrl(0x00D9, 0x03, 0x02, 0x02)
    QuestCtrl(0x000E, 0x03, 0x02, 0x02)
    QuestCtrl(0x000F, 0x03, 0x02, 0x02)
    QuestCtrl(0x0010, 0x03, 0x02, 0x02)
    QuestCtrl(0x0011, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x00CF, 0x0004, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x00CF, 0x0004, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4F68(): pass

    label('loc_4F68')

    QuestCtrl(0x00DA, 0x03, 0x01, 0x02)
    QuestCtrl(0x00DA, 0x03, 0x02, 0x02)
    QuestCtrl(0x00DB, 0x03, 0x01, 0x02)
    QuestCtrl(0x00DB, 0x03, 0x02, 0x02)
    QuestCtrl(0x0012, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4F97',
    )

    QuestCtrl(0x0012, 0x06, 0x0002)

    def _loc_4F97(): pass

    label('loc_4F97')

    QuestCtrl(0x0013, 0x03, 0x02, 0x02)
    QuestCtrl(0x0014, 0x03, 0x02, 0x02)
    QuestCtrl(0x0015, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x00CF, 0x0005, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x00CF, 0x0005, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_4FC8(): pass

    label('loc_4FC8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4FE4',
    )

    QuestCtrl(0x00DE, 0x03, 0x01, 0x02)
    QuestCtrl(0x00DE, 0x03, 0x02, 0x02)

    Jump('loc_500C')

    def _loc_4FE4(): pass

    label('loc_4FE4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5000',
    )

    QuestCtrl(0x00DD, 0x03, 0x01, 0x02)
    QuestCtrl(0x00DD, 0x03, 0x02, 0x02)

    Jump('loc_500C')

    def _loc_5000(): pass

    label('loc_5000')

    QuestCtrl(0x00DC, 0x03, 0x01, 0x02)
    QuestCtrl(0x00DC, 0x03, 0x02, 0x02)

    def _loc_500C(): pass

    label('loc_500C')

    QuestCtrl(0x00DF, 0x03, 0x01, 0x02)
    QuestCtrl(0x00DF, 0x03, 0x02, 0x02)
    QuestCtrl(0x00E0, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E0, 0x03, 0x02, 0x02)
    QuestCtrl(0x00E1, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E1, 0x03, 0x02, 0x02)
    QuestCtrl(0x0016, 0x03, 0x02, 0x02)
    QuestCtrl(0x0017, 0x03, 0x02, 0x02)
    QuestCtrl(0x0018, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x002C, 0x0006, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x002C, 0x0006, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_5061(): pass

    label('loc_5061')

    QuestCtrl(0x00E2, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E2, 0x03, 0x02, 0x02)
    QuestCtrl(0x00E3, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E3, 0x03, 0x02, 0x02)
    QuestCtrl(0x00E4, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E4, 0x03, 0x02, 0x02)
    QuestCtrl(0x0019, 0x03, 0x02, 0x02)
    QuestCtrl(0x001A, 0x03, 0x02, 0x02)
    QuestCtrl(0x001B, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x002C, 0x0007, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x002C, 0x0007, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_50B6(): pass

    label('loc_50B6')

    QuestCtrl(0x00E5, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E5, 0x03, 0x02, 0x02)
    QuestCtrl(0x00E6, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E6, 0x03, 0x02, 0x02)
    QuestCtrl(0x001C, 0x03, 0x02, 0x02)
    QuestCtrl(0x001D, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_50F0',
    )

    QuestCtrl(0x001D, 0x06, 0x0002)

    Jump('loc_5101')

    def _loc_50F0(): pass

    label('loc_50F0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5101',
    )

    QuestCtrl(0x001D, 0x06, 0x0001)

    def _loc_5101(): pass

    label('loc_5101')

    QuestCtrl(0x001E, 0x03, 0x02, 0x02)
    QuestCtrl(0x001F, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5123',
    )

    QuestCtrl(0x001F, 0x06, 0x0002)

    Jump('loc_5134')

    def _loc_5123(): pass

    label('loc_5123')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5134',
    )

    QuestCtrl(0x001F, 0x06, 0x0001)

    def _loc_5134(): pass

    label('loc_5134')

    QuestCtrl(0x0020, 0x03, 0x02, 0x02)
    QuestCtrl(0x0021, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5156',
    )

    QuestCtrl(0x0021, 0x06, 0x0002)

    Jump('loc_5167')

    def _loc_5156(): pass

    label('loc_5156')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5167',
    )

    QuestCtrl(0x0021, 0x06, 0x0001)

    def _loc_5167(): pass

    label('loc_5167')

    OP_9C(0x00, 0x00, 0x0013, 0x0008, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x0013, 0x0008, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_5186(): pass

    label('loc_5186')

    QuestCtrl(0x00E7, 0x03, 0x01, 0x02)
    QuestCtrl(0x00E7, 0x03, 0x02, 0x02)
    QuestCtrl(0x0022, 0x03, 0x02, 0x02)
    QuestCtrl(0x0023, 0x03, 0x02, 0x02)
    QuestCtrl(0x0024, 0x03, 0x02, 0x02)
    QuestCtrl(0x0025, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_51BB',
    )

    QuestCtrl(0x0025, 0x06, 0x0002)

    def _loc_51BB(): pass

    label('loc_51BB')

    QuestCtrl(0x0026, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_51D2',
    )

    QuestCtrl(0x0026, 0x06, 0x0002)

    def _loc_51D2(): pass

    label('loc_51D2')

    QuestCtrl(0x0027, 0x03, 0x02, 0x02)
    QuestCtrl(0x0028, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x0013, 0x0009, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x0013, 0x0009, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_51FD(): pass

    label('loc_51FD')

    QuestCtrl(0x0029, 0x03, 0x02, 0x02)
    QuestCtrl(0x002A, 0x03, 0x02, 0x02)
    QuestCtrl(0x002B, 0x03, 0x02, 0x02)
    QuestCtrl(0x002C, 0x03, 0x02, 0x02)
    QuestCtrl(0x002D, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5231',
    )

    QuestCtrl(0x002D, 0x06, 0x0002)

    Jump('loc_5242')

    def _loc_5231(): pass

    label('loc_5231')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5242',
    )

    QuestCtrl(0x002D, 0x06, 0x0001)

    def _loc_5242(): pass

    label('loc_5242')

    QuestCtrl(0x002E, 0x03, 0x02, 0x02)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5259',
    )

    QuestCtrl(0x002E, 0x06, 0x0002)

    def _loc_5259(): pass

    label('loc_5259')

    QuestCtrl(0x002F, 0x03, 0x02, 0x02)
    QuestCtrl(0x0030, 0x03, 0x02, 0x02)
    OP_9C(0x00, 0x00, 0x0013, 0x000A, 0x00000001)
    OP_9C(0x01)
    OP_9C(0x00, 0x01, 0x0013, 0x000A, 0x00000000)
    OP_9C(0x01)

    Jump('loc_5292')

    def _loc_5284(): pass

    label('loc_5284')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5292')

    def _loc_5292(): pass

    label('loc_5292')

    Jump('loc_4669')

    def _loc_5297(): pass

    label('loc_5297')

    Return()

# id: 0x002B offset: 0x5298
@scena.Code('TK_QuestUI_DebugQuestFlag')
def TK_QuestUI_DebugQuestFlag():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    Switch(
        (
            (Expr.Expr25, 0x0),
            Expr.Return,
        ),
        (0x00000032, 'loc_5309'),
        (0x00000028, 'loc_5387'),
        (0x00000022, 'loc_5399'),
        (0x00000020, 'loc_5417'),
        (0x00000019, 'loc_5483'),
        (0x00000018, 'loc_54B9'),
        (0x00000017, 'loc_54EF'),
        (0x00000016, 'loc_5537'),
        (0x0000000F, 'loc_557F'),
        (0x0000000D, 'loc_5591'),
        (0x0000000C, 'loc_55D9'),
        (0x0000000B, 'loc_5621'),
        (-1, 'loc_5669'),
    )

    def _loc_5309(): pass

    label('loc_5309')

    QuestCtrl(0x002A, 0x03, 0x01, 0x02)
    QuestCtrl(0x002A, 0x03, 0x02, 0x02)
    QuestCtrl(0x002A, 0x04, 0x04, 0x02)
    QuestCtrl(0x002B, 0x03, 0x01, 0x02)
    QuestCtrl(0x002B, 0x03, 0x02, 0x02)
    QuestCtrl(0x002B, 0x04, 0x04, 0x02)
    QuestCtrl(0x002C, 0x03, 0x01, 0x02)
    QuestCtrl(0x002C, 0x03, 0x02, 0x02)
    QuestCtrl(0x002C, 0x04, 0x04, 0x02)
    QuestCtrl(0x002D, 0x03, 0x01, 0x02)
    QuestCtrl(0x002D, 0x03, 0x02, 0x02)
    QuestCtrl(0x002D, 0x04, 0x04, 0x02)
    QuestCtrl(0x002E, 0x03, 0x01, 0x02)
    QuestCtrl(0x002E, 0x03, 0x02, 0x02)
    QuestCtrl(0x002E, 0x04, 0x04, 0x02)
    QuestCtrl(0x002F, 0x03, 0x01, 0x02)
    QuestCtrl(0x002F, 0x03, 0x02, 0x02)
    QuestCtrl(0x002F, 0x04, 0x04, 0x02)
    QuestCtrl(0x0030, 0x03, 0x01, 0x02)
    QuestCtrl(0x0030, 0x03, 0x02, 0x02)
    QuestCtrl(0x0030, 0x04, 0x04, 0x02)

    def _loc_5387(): pass

    label('loc_5387')

    QuestCtrl(0x0029, 0x03, 0x01, 0x02)
    QuestCtrl(0x0029, 0x03, 0x02, 0x02)
    QuestCtrl(0x0029, 0x04, 0x04, 0x02)

    def _loc_5399(): pass

    label('loc_5399')

    QuestCtrl(0x0022, 0x03, 0x01, 0x02)
    QuestCtrl(0x0022, 0x03, 0x02, 0x02)
    QuestCtrl(0x0022, 0x04, 0x04, 0x02)
    QuestCtrl(0x0023, 0x03, 0x01, 0x02)
    QuestCtrl(0x0023, 0x03, 0x02, 0x02)
    QuestCtrl(0x0023, 0x04, 0x04, 0x02)
    QuestCtrl(0x0024, 0x03, 0x01, 0x02)
    QuestCtrl(0x0024, 0x03, 0x02, 0x02)
    QuestCtrl(0x0024, 0x04, 0x04, 0x02)
    QuestCtrl(0x0025, 0x03, 0x01, 0x02)
    QuestCtrl(0x0025, 0x03, 0x02, 0x02)
    QuestCtrl(0x0025, 0x04, 0x04, 0x02)
    QuestCtrl(0x0026, 0x03, 0x01, 0x02)
    QuestCtrl(0x0026, 0x03, 0x02, 0x02)
    QuestCtrl(0x0026, 0x04, 0x04, 0x02)
    QuestCtrl(0x0027, 0x03, 0x01, 0x02)
    QuestCtrl(0x0027, 0x03, 0x02, 0x02)
    QuestCtrl(0x0027, 0x04, 0x04, 0x02)
    QuestCtrl(0x0028, 0x03, 0x01, 0x02)
    QuestCtrl(0x0028, 0x03, 0x02, 0x02)
    QuestCtrl(0x0028, 0x04, 0x04, 0x02)

    def _loc_5417(): pass

    label('loc_5417')

    QuestCtrl(0x001C, 0x03, 0x01, 0x02)
    QuestCtrl(0x001C, 0x03, 0x02, 0x02)
    QuestCtrl(0x001C, 0x04, 0x04, 0x02)
    QuestCtrl(0x001D, 0x03, 0x01, 0x02)
    QuestCtrl(0x001D, 0x03, 0x02, 0x02)
    QuestCtrl(0x001D, 0x04, 0x04, 0x02)
    QuestCtrl(0x001E, 0x03, 0x01, 0x02)
    QuestCtrl(0x001E, 0x03, 0x02, 0x02)
    QuestCtrl(0x001E, 0x04, 0x04, 0x02)
    QuestCtrl(0x001F, 0x03, 0x01, 0x02)
    QuestCtrl(0x001F, 0x03, 0x02, 0x02)
    QuestCtrl(0x001F, 0x04, 0x04, 0x02)
    QuestCtrl(0x0020, 0x03, 0x01, 0x02)
    QuestCtrl(0x0020, 0x03, 0x02, 0x02)
    QuestCtrl(0x0020, 0x04, 0x04, 0x02)
    QuestCtrl(0x0021, 0x03, 0x01, 0x02)
    QuestCtrl(0x0021, 0x03, 0x02, 0x02)
    QuestCtrl(0x0021, 0x04, 0x04, 0x02)

    def _loc_5483(): pass

    label('loc_5483')

    QuestCtrl(0x0019, 0x03, 0x01, 0x02)
    QuestCtrl(0x0019, 0x03, 0x02, 0x02)
    QuestCtrl(0x0019, 0x04, 0x04, 0x02)
    QuestCtrl(0x001A, 0x03, 0x01, 0x02)
    QuestCtrl(0x001A, 0x03, 0x02, 0x02)
    QuestCtrl(0x001A, 0x04, 0x04, 0x02)
    QuestCtrl(0x001B, 0x03, 0x01, 0x02)
    QuestCtrl(0x001B, 0x03, 0x02, 0x02)
    QuestCtrl(0x001B, 0x04, 0x04, 0x02)

    def _loc_54B9(): pass

    label('loc_54B9')

    QuestCtrl(0x0016, 0x03, 0x01, 0x02)
    QuestCtrl(0x0016, 0x03, 0x02, 0x02)
    QuestCtrl(0x0016, 0x04, 0x04, 0x02)
    QuestCtrl(0x0017, 0x03, 0x01, 0x02)
    QuestCtrl(0x0017, 0x03, 0x02, 0x02)
    QuestCtrl(0x0017, 0x04, 0x04, 0x02)
    QuestCtrl(0x0018, 0x03, 0x01, 0x02)
    QuestCtrl(0x0018, 0x03, 0x02, 0x02)
    QuestCtrl(0x0018, 0x04, 0x04, 0x02)

    def _loc_54EF(): pass

    label('loc_54EF')

    QuestCtrl(0x0012, 0x03, 0x01, 0x02)
    QuestCtrl(0x0012, 0x03, 0x02, 0x02)
    QuestCtrl(0x0012, 0x04, 0x04, 0x02)
    QuestCtrl(0x0013, 0x03, 0x01, 0x02)
    QuestCtrl(0x0013, 0x03, 0x02, 0x02)
    QuestCtrl(0x0013, 0x04, 0x04, 0x02)
    QuestCtrl(0x0014, 0x03, 0x01, 0x02)
    QuestCtrl(0x0014, 0x03, 0x02, 0x02)
    QuestCtrl(0x0014, 0x04, 0x04, 0x02)
    QuestCtrl(0x0015, 0x03, 0x01, 0x02)
    QuestCtrl(0x0015, 0x03, 0x02, 0x02)
    QuestCtrl(0x0015, 0x04, 0x04, 0x02)

    def _loc_5537(): pass

    label('loc_5537')

    QuestCtrl(0x000E, 0x03, 0x01, 0x02)
    QuestCtrl(0x000E, 0x03, 0x02, 0x02)
    QuestCtrl(0x000E, 0x04, 0x04, 0x02)
    QuestCtrl(0x000F, 0x03, 0x01, 0x02)
    QuestCtrl(0x000F, 0x03, 0x02, 0x02)
    QuestCtrl(0x000F, 0x04, 0x04, 0x02)
    QuestCtrl(0x0010, 0x03, 0x01, 0x02)
    QuestCtrl(0x0010, 0x03, 0x02, 0x02)
    QuestCtrl(0x0010, 0x04, 0x04, 0x02)
    QuestCtrl(0x0011, 0x03, 0x01, 0x02)
    QuestCtrl(0x0011, 0x03, 0x02, 0x02)
    QuestCtrl(0x0011, 0x04, 0x04, 0x02)

    def _loc_557F(): pass

    label('loc_557F')

    QuestCtrl(0x000D, 0x03, 0x01, 0x02)
    QuestCtrl(0x000D, 0x03, 0x02, 0x02)
    QuestCtrl(0x000D, 0x04, 0x04, 0x02)

    def _loc_5591(): pass

    label('loc_5591')

    QuestCtrl(0x0009, 0x03, 0x01, 0x02)
    QuestCtrl(0x0009, 0x03, 0x02, 0x02)
    QuestCtrl(0x0009, 0x04, 0x04, 0x02)
    QuestCtrl(0x000A, 0x03, 0x01, 0x02)
    QuestCtrl(0x000A, 0x03, 0x02, 0x02)
    QuestCtrl(0x000A, 0x04, 0x04, 0x02)
    QuestCtrl(0x000B, 0x03, 0x01, 0x02)
    QuestCtrl(0x000B, 0x03, 0x02, 0x02)
    QuestCtrl(0x000B, 0x04, 0x04, 0x02)
    QuestCtrl(0x000C, 0x03, 0x01, 0x02)
    QuestCtrl(0x000C, 0x03, 0x02, 0x02)
    QuestCtrl(0x000C, 0x04, 0x04, 0x02)

    def _loc_55D9(): pass

    label('loc_55D9')

    QuestCtrl(0x0005, 0x03, 0x01, 0x02)
    QuestCtrl(0x0005, 0x03, 0x02, 0x02)
    QuestCtrl(0x0005, 0x04, 0x04, 0x02)
    QuestCtrl(0x0006, 0x03, 0x01, 0x02)
    QuestCtrl(0x0006, 0x03, 0x02, 0x02)
    QuestCtrl(0x0006, 0x04, 0x04, 0x02)
    QuestCtrl(0x0007, 0x03, 0x01, 0x02)
    QuestCtrl(0x0007, 0x03, 0x02, 0x02)
    QuestCtrl(0x0007, 0x04, 0x04, 0x02)
    QuestCtrl(0x0008, 0x03, 0x01, 0x02)
    QuestCtrl(0x0008, 0x03, 0x02, 0x02)
    QuestCtrl(0x0008, 0x04, 0x04, 0x02)

    def _loc_5621(): pass

    label('loc_5621')

    QuestCtrl(0x0001, 0x03, 0x01, 0x02)
    QuestCtrl(0x0001, 0x03, 0x02, 0x02)
    QuestCtrl(0x0001, 0x04, 0x04, 0x02)
    QuestCtrl(0x0002, 0x03, 0x01, 0x02)
    QuestCtrl(0x0002, 0x03, 0x02, 0x02)
    QuestCtrl(0x0002, 0x04, 0x04, 0x02)
    QuestCtrl(0x0003, 0x03, 0x01, 0x02)
    QuestCtrl(0x0003, 0x03, 0x02, 0x02)
    QuestCtrl(0x0003, 0x04, 0x04, 0x02)
    QuestCtrl(0x0004, 0x03, 0x01, 0x02)
    QuestCtrl(0x0004, 0x03, 0x02, 0x02)
    QuestCtrl(0x0004, 0x04, 0x04, 0x02)

    def _loc_5669(): pass

    label('loc_5669')

    Return()

# id: 0x002C offset: 0x566C
@scena.Code('TK_Quest_Debug')
def TK_Quest_Debug():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5691(): pass

    label('loc_5691')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_57E5',
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '▼任务', 0x00000001)
    MenuCmd(0x01, 0x00, '▼羁绊活动', 0x00000002)
    MenuCmd(0x01, 0x00, '▼子事件', 0x00000003)
    MenuCmd(0x01, 0x00, '▼深入要素', 0x00000004)
    MenuCmd(0x01, 0x00, '▼任务报告画面>', 0x00000064)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000001, 'loc_575E'),
        (0x00000002, 'loc_5773'),
        (0x00000003, 'loc_5789'),
        (0x00000004, 'loc_57A1'),
        (0x00000064, 'loc_57B9'),
        (-1, 'loc_57D2'),
    )

    def _loc_575E(): pass

    label('loc_575E')

    Call(ScriptId.Map, 'EV_QuestJump')

    Jump('loc_57E0')

    def _loc_5773(): pass

    label('loc_5773')

    Call(ScriptId.Map, 'EV_KizunaJump')

    Jump('loc_57E0')

    def _loc_5789(): pass

    label('loc_5789')

    Call(ScriptId.Map, 'EV_SubeventJump')

    Jump('loc_57E0')

    def _loc_57A1(): pass

    label('loc_57A1')

    Call(ScriptId.Map, 'EV_YarikomiJump')

    Jump('loc_57E0')

    def _loc_57B9(): pass

    label('loc_57B9')

    Call(ScriptId.Map, 'TK_QuestUI_Debug')

    Jump('loc_57E0')

    def _loc_57D2(): pass

    label('loc_57D2')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_57E0')

    def _loc_57E0(): pass

    label('loc_57E0')

    Jump('loc_5691')

    def _loc_57E5(): pass

    label('loc_57E5')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))

    Return()

# id: 0x002D offset: 0x57FC
@scena.Code('EV_QuestJump')
def EV_QuestJump():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5805(): pass

    label('loc_5805')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_679D',
    )

    MenuCmd(0x00, 0x01, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'QS110_伊斯特米亚森林的通缉魔兽（战）', 0x0000006E)
    MenuCmd(0x01, 0x01, 'QS111_代替药的材料收集', 0x0000006F)
    MenuCmd(0x01, 0x01, 'QS112_龙灵窟的攻略', 0x00000070)
    MenuCmd(0x01, 0x01, 'QS115_月影亭的魔女汤', 0x00000073)
    MenuCmd(0x01, 0x01, 'QS120_月灵窟的攻略', 0x00000078)
    MenuCmd(0x01, 0x01, 'QS121_收拾纠纷', 0x00000079)
    MenuCmd(0x01, 0x01, 'QS122_北兰格多克峡谷路的通缉魔兽（战）', 0x0000007A)
    MenuCmd(0x01, 0x01, 'QS125_魔女之村的课外授课', 0x0000007D)
    MenuCmd(0x01, 0x01, 'QS130_国家总动员法的问卷调查', 0x00000082)
    MenuCmd(0x01, 0x01, 'QS131_星灵窟的攻略', 0x00000083)
    MenuCmd(0x01, 0x01, 'QS132_乌拉斯拉间道的通缉魔兽（战）', 0x00000084)
    MenuCmd(0x01, 0x01, 'QS133_搜索克林', 0x00000085)
    MenuCmd(0x01, 0x01, '─────────────────────', 0x00000000)
    MenuCmd(0x01, 0x01, 'QS150_修理吊坠', 0x00000096)
    MenuCmd(0x01, 0x01, '─────────────────────', 0x00000000)
    MenuCmd(0x01, 0x01, 'QS220_征兵家族支援基金（战）', 0x000000DC)
    MenuCmd(0x01, 0x01, 'QS221_超稀有食材的回收', 0x000000DD)
    MenuCmd(0x01, 0x01, 'QS222_帕鲁姆间道的通缉魔兽（莫伊罗）（战）', 0x000000DE)
    MenuCmd(0x01, 0x01, 'QS223_里维埃拉的苦难', 0x000000DF)
    MenuCmd(0x01, 0x01, 'QS230_搜索旅行者', 0x000000E6)
    MenuCmd(0x01, 0x01, 'QS231_旧型蒸馏机的修理', 0x000000E7)
    MenuCmd(0x01, 0x01, 'QS232_西拉玛路街道的通缉魔兽（战）', 0x000000E8)
    MenuCmd(0x01, 0x01, 'QS233_变得奇怪的馬（战）', 0x000000E9)
    MenuCmd(0x01, 0x01, 'QS240_消失的蔷薇贝尔克人偶（战）', 0x000000F0)
    MenuCmd(0x01, 0x01, 'QS241_某个紧急案件的处理（战）', 0x000000F1)
    MenuCmd(0x01, 0x01, 'QS242_拉马尔故道的通缉魔兽（艾尔达）（战）', 0x000000F2)
    MenuCmd(0x01, 0x01, 'QS250_离散的家属', 0x000000FA)
    MenuCmd(0x01, 0x01, 'QS251_污秽温泉的净化', 0x000000FB)
    MenuCmd(0x01, 0x01, 'QS252_雅芳丘陵的通缉魔兽（洛斯托尔姆）（战）', 0x000000FC)
    MenuCmd(0x01, 0x01, '─────────────────────', 0x00000000)
    MenuCmd(0x01, 0x01, 'QS320_保护ハーキュリーズ（战）', 0x00000140)
    MenuCmd(0x01, 0x01, 'QS321_连续出演广播剧', 0x00000141)
    MenuCmd(0x01, 0x01, 'QS322_伽拉湖周游道的通缉魔兽', 0x00000142)
    MenuCmd(0x01, 0x01, 'QS323_记者尼尔森的采访', 0x00000143)
    MenuCmd(0x01, 0x01, 'QS324_应对通信障碍（战）', 0x00000144)
    MenuCmd(0x01, 0x01, 'QS325_父女的认真比赛', 0x00000145)
    MenuCmd(0x01, 0x01, 'QS340_来自凯&蒂亚的委托（战）', 0x00000154)
    MenuCmd(0x01, 0x01, 'QS341_兰格多克峡谷·北部的通缉魔兽（战）', 0x00000155)
    MenuCmd(0x01, 0x01, 'QS342_艾琳的解放作战（战）', 0x00000156)
    MenuCmd(0x01, 0x01, 'QS343_不屈不挠的钻研（战）', 0x00000157)
    MenuCmd(0x01, 0x01, 'QS344_激烈的对决', 0x00000158)
    MenuCmd(0x01, 0x01, 'QS345_寻找药材（战）', 0x00000159)
    MenuCmd(0x01, 0x01, 'QS346_地下通道X区的通缉魔兽（战）', 0x0000015A)
    MenuCmd(0x01, 0x01, '─────────────────────', 0x00000000)
    MenuCmd(0x01, 0x01, 'QS400_没有仁义的喝酒大賽', 0x00000190)
    MenuCmd(0x01, 0x01, '─────────────────────', 0x00000000)
    MenuCmd(0x01, 0x01, 'QS500_阿尔斯特收获节', 0x000001F4)
    MenuCmd(0x01, 0x01, 'QS501_阿兰的说服（骑）', 0x000001F5)
    MenuCmd(0x01, 0x01, 'QS502_小要塞的通缉魔兽（战）', 0x000001F6)
    MenuCmd(0x01, 0x01, 'QS503_搜索迪安娜老板（战）', 0x000001F7)
    MenuCmd(0x01, 0x01, 'QS504_十年来的师徒对决', 0x000001F8)
    MenuCmd(0x01, 0x01, 'QS505_哈梅尔的异界化（战）', 0x000001F9)
    MenuCmd(0x01, 0x01, 'QS506_大地圣兽的考验（战）', 0x000001FA)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_6335'),
        (0x0000006E, 'loc_633A'),
        (0x0000006F, 'loc_6351'),
        (0x00000070, 'loc_6368'),
        (0x00000073, 'loc_637F'),
        (0x00000078, 'loc_6396'),
        (0x00000079, 'loc_63AD'),
        (0x0000007A, 'loc_63C4'),
        (0x0000007D, 'loc_63DB'),
        (0x00000082, 'loc_63F2'),
        (0x00000083, 'loc_6409'),
        (0x00000084, 'loc_6420'),
        (0x00000085, 'loc_6437'),
        (0x00000096, 'loc_644E'),
        (0x000000DC, 'loc_6465'),
        (0x000000DD, 'loc_647C'),
        (0x000000DE, 'loc_6493'),
        (0x000000DF, 'loc_64AA'),
        (0x000000E6, 'loc_64C1'),
        (0x000000E7, 'loc_64D8'),
        (0x000000E8, 'loc_64EF'),
        (0x000000E9, 'loc_6506'),
        (0x000000F0, 'loc_651D'),
        (0x000000F1, 'loc_6534'),
        (0x000000F2, 'loc_654B'),
        (0x000000FA, 'loc_6562'),
        (0x000000FB, 'loc_6579'),
        (0x000000FC, 'loc_6590'),
        (0x00000140, 'loc_65A7'),
        (0x00000141, 'loc_65BE'),
        (0x00000142, 'loc_65D5'),
        (0x00000143, 'loc_65EC'),
        (0x00000144, 'loc_6603'),
        (0x00000145, 'loc_661A'),
        (0x00000154, 'loc_6631'),
        (0x00000155, 'loc_6648'),
        (0x00000156, 'loc_665F'),
        (0x00000157, 'loc_6676'),
        (0x00000158, 'loc_668D'),
        (0x00000159, 'loc_66A4'),
        (0x0000015A, 'loc_66BB'),
        (0x00000190, 'loc_66D2'),
        (0x000001F4, 'loc_66E9'),
        (0x000001F5, 'loc_6700'),
        (0x000001F6, 'loc_6717'),
        (0x000001F7, 'loc_672E'),
        (0x000001F8, 'loc_6745'),
        (0x000001F9, 'loc_675C'),
        (0x000001FA, 'loc_6773'),
        (-1, 'loc_678A'),
    )

    def _loc_6335(): pass

    label('loc_6335')

    Jump('loc_6798')

    def _loc_633A(): pass

    label('loc_633A')

    Call(ScriptId.Current, 'EV_Jump_QS_110')

    Jump('loc_6798')

    def _loc_6351(): pass

    label('loc_6351')

    Call(ScriptId.Current, 'EV_Jump_QS_111')

    Jump('loc_6798')

    def _loc_6368(): pass

    label('loc_6368')

    Call(ScriptId.Current, 'EV_Jump_QS_112')

    Jump('loc_6798')

    def _loc_637F(): pass

    label('loc_637F')

    Call(ScriptId.Current, 'EV_Jump_QS_115')

    Jump('loc_6798')

    def _loc_6396(): pass

    label('loc_6396')

    Call(ScriptId.Current, 'EV_Jump_QS_120')

    Jump('loc_6798')

    def _loc_63AD(): pass

    label('loc_63AD')

    Call(ScriptId.Current, 'EV_Jump_QS_121')

    Jump('loc_6798')

    def _loc_63C4(): pass

    label('loc_63C4')

    Call(ScriptId.Current, 'EV_Jump_QS_122')

    Jump('loc_6798')

    def _loc_63DB(): pass

    label('loc_63DB')

    Call(ScriptId.Current, 'EV_Jump_QS_125')

    Jump('loc_6798')

    def _loc_63F2(): pass

    label('loc_63F2')

    Call(ScriptId.Current, 'EV_Jump_QS_130')

    Jump('loc_6798')

    def _loc_6409(): pass

    label('loc_6409')

    Call(ScriptId.Current, 'EV_Jump_QS_131')

    Jump('loc_6798')

    def _loc_6420(): pass

    label('loc_6420')

    Call(ScriptId.Current, 'EV_Jump_QS_132')

    Jump('loc_6798')

    def _loc_6437(): pass

    label('loc_6437')

    Call(ScriptId.Current, 'EV_Jump_QS_133')

    Jump('loc_6798')

    def _loc_644E(): pass

    label('loc_644E')

    Call(ScriptId.Current, 'EV_Jump_QS_150')

    Jump('loc_6798')

    def _loc_6465(): pass

    label('loc_6465')

    Call(ScriptId.Current, 'EV_Jump_QS_220')

    Jump('loc_6798')

    def _loc_647C(): pass

    label('loc_647C')

    Call(ScriptId.Current, 'EV_Jump_QS_221')

    Jump('loc_6798')

    def _loc_6493(): pass

    label('loc_6493')

    Call(ScriptId.Current, 'EV_Jump_QS_222')

    Jump('loc_6798')

    def _loc_64AA(): pass

    label('loc_64AA')

    Call(ScriptId.Current, 'EV_Jump_QS_223')

    Jump('loc_6798')

    def _loc_64C1(): pass

    label('loc_64C1')

    Call(ScriptId.Current, 'EV_Jump_QS_230')

    Jump('loc_6798')

    def _loc_64D8(): pass

    label('loc_64D8')

    Call(ScriptId.Current, 'EV_Jump_QS_231')

    Jump('loc_6798')

    def _loc_64EF(): pass

    label('loc_64EF')

    Call(ScriptId.Current, 'EV_Jump_QS_232')

    Jump('loc_6798')

    def _loc_6506(): pass

    label('loc_6506')

    Call(ScriptId.Current, 'EV_Jump_QS_233')

    Jump('loc_6798')

    def _loc_651D(): pass

    label('loc_651D')

    Call(ScriptId.Current, 'EV_Jump_QS_240')

    Jump('loc_6798')

    def _loc_6534(): pass

    label('loc_6534')

    Call(ScriptId.Current, 'EV_Jump_QS_241')

    Jump('loc_6798')

    def _loc_654B(): pass

    label('loc_654B')

    Call(ScriptId.Current, 'EV_Jump_QS_242')

    Jump('loc_6798')

    def _loc_6562(): pass

    label('loc_6562')

    Call(ScriptId.Current, 'EV_Jump_QS_250')

    Jump('loc_6798')

    def _loc_6579(): pass

    label('loc_6579')

    Call(ScriptId.Current, 'EV_Jump_QS_251')

    Jump('loc_6798')

    def _loc_6590(): pass

    label('loc_6590')

    Call(ScriptId.Current, 'EV_Jump_QS_252')

    Jump('loc_6798')

    def _loc_65A7(): pass

    label('loc_65A7')

    Call(ScriptId.Current, 'EV_Jump_QS_320')

    Jump('loc_6798')

    def _loc_65BE(): pass

    label('loc_65BE')

    Call(ScriptId.Current, 'EV_Jump_QS_321')

    Jump('loc_6798')

    def _loc_65D5(): pass

    label('loc_65D5')

    Call(ScriptId.Current, 'EV_Jump_QS_322')

    Jump('loc_6798')

    def _loc_65EC(): pass

    label('loc_65EC')

    Call(ScriptId.Current, 'EV_Jump_QS_323')

    Jump('loc_6798')

    def _loc_6603(): pass

    label('loc_6603')

    Call(ScriptId.Current, 'EV_Jump_QS_324')

    Jump('loc_6798')

    def _loc_661A(): pass

    label('loc_661A')

    Call(ScriptId.Current, 'EV_Jump_QS_325')

    Jump('loc_6798')

    def _loc_6631(): pass

    label('loc_6631')

    Call(ScriptId.Current, 'EV_Jump_QS_340')

    Jump('loc_6798')

    def _loc_6648(): pass

    label('loc_6648')

    Call(ScriptId.Current, 'EV_Jump_QS_341')

    Jump('loc_6798')

    def _loc_665F(): pass

    label('loc_665F')

    Call(ScriptId.Current, 'EV_Jump_QS_342')

    Jump('loc_6798')

    def _loc_6676(): pass

    label('loc_6676')

    Call(ScriptId.Current, 'EV_Jump_QS_343')

    Jump('loc_6798')

    def _loc_668D(): pass

    label('loc_668D')

    Call(ScriptId.Current, 'EV_Jump_QS_344')

    Jump('loc_6798')

    def _loc_66A4(): pass

    label('loc_66A4')

    Call(ScriptId.Current, 'EV_Jump_QS_345')

    Jump('loc_6798')

    def _loc_66BB(): pass

    label('loc_66BB')

    Call(ScriptId.Current, 'EV_Jump_QS_346')

    Jump('loc_6798')

    def _loc_66D2(): pass

    label('loc_66D2')

    Call(ScriptId.Current, 'EV_Jump_QS_400')

    Jump('loc_6798')

    def _loc_66E9(): pass

    label('loc_66E9')

    Call(ScriptId.Current, 'EV_Jump_QS_500')

    Jump('loc_6798')

    def _loc_6700(): pass

    label('loc_6700')

    Call(ScriptId.Current, 'EV_Jump_QS_501')

    Jump('loc_6798')

    def _loc_6717(): pass

    label('loc_6717')

    Call(ScriptId.Current, 'EV_Jump_QS_502')

    Jump('loc_6798')

    def _loc_672E(): pass

    label('loc_672E')

    Call(ScriptId.Current, 'EV_Jump_QS_503')

    Jump('loc_6798')

    def _loc_6745(): pass

    label('loc_6745')

    Call(ScriptId.Current, 'EV_Jump_QS_504')

    Jump('loc_6798')

    def _loc_675C(): pass

    label('loc_675C')

    Call(ScriptId.Current, 'EV_Jump_QS_505')

    Jump('loc_6798')

    def _loc_6773(): pass

    label('loc_6773')

    Call(ScriptId.Current, 'EV_Jump_QS_506')

    Jump('loc_6798')

    def _loc_678A(): pass

    label('loc_678A')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6798')

    def _loc_6798(): pass

    label('loc_6798')

    Jump('loc_5805')

    def _loc_679D(): pass

    label('loc_679D')

    Return()

# id: 0x002E offset: 0x67A0
@scena.Code('EV_Jump_QS_110')
def EV_Jump_QS_110():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_67A9(): pass

    label('loc_67A9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_68A2',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS110_01][手配魔獣を撃破　　　　　　　　]', 0x00007000)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6855',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1012),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_6855(): pass

    label('loc_6855')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_686A',
    )

    QuestCtrl(0x0001, 0x04, 0x02, 0x02)

    def _loc_686A(): pass

    label('loc_686A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007000, 'loc_687B'),
        (-1, 'loc_6898'),
    )

    def _loc_687B(): pass

    label('loc_687B')

    OP_28((0xDD, 'm0600'), (0xDD, 'QS110_01_JUMP'), 0x00)

    Jump('loc_689D')

    def _loc_6898(): pass

    label('loc_6898')

    Jump('loc_689D')

    def _loc_689D(): pass

    label('loc_689D')

    Jump('loc_67A9')

    def _loc_68A2(): pass

    label('loc_68A2')

    Return()

# id: 0x002F offset: 0x68A4
@scena.Code('EV_Jump_QS_111')
def EV_Jump_QS_111():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_68AD(): pass

    label('loc_68AD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A7B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS111_01]【听霍维斯教区长的话】', 0x00007020)
    MenuCmd(0x01, 0x02, '[QS111_02A][访问大教堂]', 0x00007021)
    MenuCmd(0x01, 0x02, '[QS111_02B1“去食材店”', 0x00007022)
    MenuCmd(0x01, 0x02, '[QS111_02B2“发现‘尼姑’”', 0x00007023)
    MenuCmd(0x01, 0x02, '[QS111_03][达成事件]', 0x00007024)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_69DF',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1026),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_69DF(): pass

    label('loc_69DF')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A00',
    )

    QuestCtrl(0x0002, 0x04, 0x01, 0x02)
    QuestCtrl(0x0002, 0x04, 0x02, 0x02)
    QuestCtrl(0x0002, 0x04, 0x08, 0x02)

    def _loc_6A00(): pass

    label('loc_6A00')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007024, 'loc_6A31'),
        (0x00007023, 'loc_6A3A'),
        (0x00007022, 'loc_6A3D'),
        (0x00007021, 'loc_6A3D'),
        (0x00007020, 'loc_6A46'),
        (-1, 'loc_6A4B'),
    )

    def _loc_6A31(): pass

    label('loc_6A31')

    SetScenaFlags(ScenaFlag(0x05C5, 1, 0x2E29))
    SetScenaFlags(ScenaFlag(0x05C4, 7, 0x2E27))
    SetScenaFlags(ScenaFlag(0x05D0, 6, 0x2E86))

    def _loc_6A3A(): pass

    label('loc_6A3A')

    SetScenaFlags(ScenaFlag(0x05C5, 0, 0x2E28))

    def _loc_6A3D(): pass

    label('loc_6A3D')

    SetScenaFlags(ScenaFlag(0x05C4, 6, 0x2E26))
    QuestCtrl(0x0002, 0x03, 0x01, 0x02)

    def _loc_6A46(): pass

    label('loc_6A46')

    Jump('loc_6A4B')

    def _loc_6A4B(): pass

    label('loc_6A4B')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A76',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_6A76(): pass

    label('loc_6A76')

    Jump('loc_68AD')

    def _loc_6A7B(): pass

    label('loc_6A7B')

    Return()

# id: 0x0030 offset: 0x6A7C
@scena.Code('EV_Jump_QS_112')
def EV_Jump_QS_112():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6A85(): pass

    label('loc_6A85')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6CF9',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS112_01] [龍霊窟を発見する　　　　　　　]', 0x00007040)
    MenuCmd(0x01, 0x02, '[QS112_02] [龍霊窟の攻略を開始する　　　　]', 0x00007041)
    MenuCmd(0x01, 0x02, '[QS112_03] [終点の祭壇前でのボス戦　　　　]', 0x00007042)
    MenuCmd(0x01, 0x02, '[QS112_03B][幻視を見る　　　　　　　　　　]', 0x00007043)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6BF8',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1012),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_6BF8(): pass

    label('loc_6BF8')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C19',
    )

    QuestCtrl(0x0003, 0x04, 0x01, 0x02)
    QuestCtrl(0x0003, 0x04, 0x02, 0x02)
    QuestCtrl(0x0003, 0x04, 0x08, 0x02)

    def _loc_6C19(): pass

    label('loc_6C19')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007043, 'loc_6C42'),
        (0x00007042, 'loc_6C45'),
        (0x00007041, 'loc_6C48'),
        (0x00007040, 'loc_6C4B'),
        (-1, 'loc_6C56'),
    )

    def _loc_6C42(): pass

    label('loc_6C42')

    SetScenaFlags(ScenaFlag(0x05C0, 3, 0x2E03))

    def _loc_6C45(): pass

    label('loc_6C45')

    SetScenaFlags(ScenaFlag(0x05C0, 2, 0x2E02))

    def _loc_6C48(): pass

    label('loc_6C48')

    SetScenaFlags(ScenaFlag(0x05C0, 1, 0x2E01))

    def _loc_6C4B(): pass

    label('loc_6C4B')

    QuestCtrl(0x0003, 0x03, 0x01, 0x02)

    Jump('loc_6C56')

    def _loc_6C56(): pass

    label('loc_6C56')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007040, 'loc_6C7F'),
        (0x00007041, 'loc_6C9B'),
        (0x00007042, 'loc_6CB7'),
        (0x00007043, 'loc_6CD3'),
        (-1, 'loc_6CEF'),
    )

    def _loc_6C7F(): pass

    label('loc_6C7F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7040, 0x0))

    Jump('loc_6CF4')

    def _loc_6C9B(): pass

    label('loc_6C9B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7041, 0x0))

    Jump('loc_6CF4')

    def _loc_6CB7(): pass

    label('loc_6CB7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7042, 0x0))

    Jump('loc_6CF4')

    def _loc_6CD3(): pass

    label('loc_6CD3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7043, 0x0))

    Jump('loc_6CF4')

    def _loc_6CEF(): pass

    label('loc_6CEF')

    Jump('loc_6CF4')

    def _loc_6CF4(): pass

    label('loc_6CF4')

    Jump('loc_6A85')

    def _loc_6CF9(): pass

    label('loc_6CF9')

    Return()

# id: 0x0031 offset: 0x6CFC
@scena.Code('EV_Jump_QS_115')
def EV_Jump_QS_115():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6D05(): pass

    label('loc_6D05')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E64',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS115_01][宿酒場のライザに依頼を聞く　　]', 0x00007060)
    MenuCmd(0x01, 0x02, '[QS115_02][達成イベント　　　　　　　　　]', 0x00007061)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6DF2',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1052),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_6DF2(): pass

    label('loc_6DF2')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E13',
    )

    QuestCtrl(0x0004, 0x04, 0x01, 0x02)
    QuestCtrl(0x0004, 0x04, 0x02, 0x02)
    QuestCtrl(0x0004, 0x04, 0x08, 0x02)

    def _loc_6E13(): pass

    label('loc_6E13')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007061, 'loc_6E2C'),
        (0x00007060, 'loc_6E2F'),
        (-1, 'loc_6E34'),
    )

    def _loc_6E2C(): pass

    label('loc_6E2C')

    SetScenaFlags(ScenaFlag(0x05C3, 1, 0x2E19))

    def _loc_6E2F(): pass

    label('loc_6E2F')

    Jump('loc_6E34')

    def _loc_6E34(): pass

    label('loc_6E34')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E5F',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_6E5F(): pass

    label('loc_6E5F')

    Jump('loc_6D05')

    def _loc_6E64(): pass

    label('loc_6E64')

    Return()

# id: 0x0032 offset: 0x6E68
@scena.Code('EV_Jump_QS_120')
def EV_Jump_QS_120():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6E71(): pass

    label('loc_6E71')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6FD8',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS120_01] [終点の祭壇前でのボス戦　　　　]', 0x00007080)
    MenuCmd(0x01, 0x02, '[QS120_01B][幻視を見る　　　　　　　　　　]', 0x00007081)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F60',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x105B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_6F60(): pass

    label('loc_6F60')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F81',
    )

    QuestCtrl(0x0005, 0x04, 0x01, 0x02)
    QuestCtrl(0x0005, 0x04, 0x02, 0x02)
    QuestCtrl(0x0005, 0x04, 0x08, 0x02)

    def _loc_6F81(): pass

    label('loc_6F81')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007081, 'loc_6F9A'),
        (0x00007080, 'loc_6F9D'),
        (-1, 'loc_6FA8'),
    )

    def _loc_6F9A(): pass

    label('loc_6F9A')

    SetScenaFlags(ScenaFlag(0x05C0, 5, 0x2E05))

    def _loc_6F9D(): pass

    label('loc_6F9D')

    QuestCtrl(0x0005, 0x03, 0x01, 0x02)

    Jump('loc_6FA8')

    def _loc_6FA8(): pass

    label('loc_6FA8')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6FD3',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_6FD3(): pass

    label('loc_6FD3')

    Jump('loc_6E71')

    def _loc_6FD8(): pass

    label('loc_6FD8')

    Return()

# id: 0x0033 offset: 0x6FDC
@scena.Code('EV_Jump_QS_121')
def EV_Jump_QS_121():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6FE5(): pass

    label('loc_6FE5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7398',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS121_01] [新兵クリスに依頼を聞く　　　　]', 0x000070A0)
    MenuCmd(0x01, 0x02, '[QS121_02] [《アリーシャ》で話を聞く　　　]', 0x000070A1)
    MenuCmd(0x01, 0x02, '[QS121_03] [《トゥーランドット》で話を聞く]', 0x000070A2)
    MenuCmd(0x01, 0x02, '[QS121_04] [《デッケン》で新兵スタンと話す]', 0x000070A3)
    MenuCmd(0x01, 0x02, '[QS121_05] [《白樺亭》で話を聞く　　　　　]', 0x000070A4)
    MenuCmd(0x01, 0x02, '[QS121_06] [料理を渡す　　　　　　　　　　]', 0x000070A5)
    MenuCmd(0x01, 0x02, '[QS121_06B][達成イベント　　　　　　　　　]', 0x000070A6)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_721E',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1065),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_721E(): pass

    label('loc_721E')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_723F',
    )

    QuestCtrl(0x0006, 0x04, 0x01, 0x02)
    QuestCtrl(0x0006, 0x04, 0x02, 0x02)
    QuestCtrl(0x0006, 0x04, 0x08, 0x02)

    def _loc_723F(): pass

    label('loc_723F')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000070A6, 'loc_7280'),
        (0x000070A5, 'loc_7283'),
        (0x000070A4, 'loc_7296'),
        (0x000070A3, 'loc_7299'),
        (0x000070A2, 'loc_729C'),
        (0x000070A1, 'loc_729F'),
        (0x000070A0, 'loc_72A8'),
        (-1, 'loc_72AD'),
    )

    def _loc_7280(): pass

    label('loc_7280')

    SetScenaFlags(ScenaFlag(0x05C6, 0, 0x2E30))

    def _loc_7283(): pass

    label('loc_7283')

    SetScenaFlags(ScenaFlag(0x05C5, 7, 0x2E2F))
    AddItem(0x00, 0x0BD5, 1)
    AddItem(0x00, 0x0BBC, 1)

    def _loc_7296(): pass

    label('loc_7296')

    SetScenaFlags(ScenaFlag(0x05C5, 6, 0x2E2E))

    def _loc_7299(): pass

    label('loc_7299')

    SetScenaFlags(ScenaFlag(0x05C5, 5, 0x2E2D))

    def _loc_729C(): pass

    label('loc_729C')

    SetScenaFlags(ScenaFlag(0x05C5, 4, 0x2E2C))

    def _loc_729F(): pass

    label('loc_729F')

    SetScenaFlags(ScenaFlag(0x05C5, 3, 0x2E2B))
    QuestCtrl(0x0006, 0x03, 0x01, 0x02)

    def _loc_72A8(): pass

    label('loc_72A8')

    Jump('loc_72AD')

    def _loc_72AD(): pass

    label('loc_72AD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x70A5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7368',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, 'イベントを直接起動する', 0x00000001)
    OP_75(0x01, 0x00, '会話できる場所に移動する', 0x00000002)
    OP_75(0x02, 0x00, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF9)
    OP_75(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7368',
    )

    OP_28((0xDD, 't4030'), (0xDD, 'DefaultEntry'), 0x00)

    def _loc_7368(): pass

    label('loc_7368')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7393',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_7393(): pass

    label('loc_7393')

    Jump('loc_6FE5')

    def _loc_7398(): pass

    label('loc_7398')

    Return()

# id: 0x0034 offset: 0x739C
@scena.Code('EV_Jump_QS_122')
def EV_Jump_QS_122():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_73A5(): pass

    label('loc_73A5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_749E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS122_01][手配魔獣を撃破　　　　　　　　]', 0x000070C0)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7451',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x105B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_7451(): pass

    label('loc_7451')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7466',
    )

    QuestCtrl(0x0007, 0x04, 0x02, 0x02)

    def _loc_7466(): pass

    label('loc_7466')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000070C0, 'loc_7477'),
        (-1, 'loc_7494'),
    )

    def _loc_7477(): pass

    label('loc_7477')

    OP_28((0xDD, 'r3450'), (0xDD, 'QS122_01_JUMP'), 0x00)

    Jump('loc_7499')

    def _loc_7494(): pass

    label('loc_7494')

    Jump('loc_7499')

    def _loc_7499(): pass

    label('loc_7499')

    Jump('loc_73A5')

    def _loc_749E(): pass

    label('loc_749E')

    Return()

# id: 0x0035 offset: 0x74A0
@scena.Code('EV_Jump_QS_125')
def EV_Jump_QS_125():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_74A9(): pass

    label('loc_74A9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7743',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS125_01][魔女アウラに依頼を聞く　　　　]', 0x000070E0)
    MenuCmd(0x01, 0x02, '[QS125_02][子どもたちへの授業　　　　　　]', 0x000070E1)
    MenuCmd(0x01, 0x02, '[QS125_03][達成イベント　　　　　　　　　]', 0x000070E2)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75D7',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_75D7(): pass

    label('loc_75D7')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75F8',
    )

    QuestCtrl(0x0008, 0x04, 0x01, 0x02)
    QuestCtrl(0x0008, 0x04, 0x02, 0x02)
    QuestCtrl(0x0008, 0x04, 0x08, 0x02)

    def _loc_75F8(): pass

    label('loc_75F8')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000070E2, 'loc_7619'),
        (0x000070E1, 'loc_761C'),
        (0x000070E0, 'loc_770E'),
        (-1, 'loc_7713'),
    )

    def _loc_7619(): pass

    label('loc_7619')

    SetScenaFlags(ScenaFlag(0x05C6, 3, 0x2E33))

    def _loc_761C(): pass

    label('loc_761C')

    SetScenaFlags(ScenaFlag(0x05C6, 2, 0x2E32))
    QuestCtrl(0x0008, 0x03, 0x01, 0x02)

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, 'クルトを選ぶ', 0x00000001)
    OP_75(0x01, 0x00, 'アルティナを選ぶ', 0x00000002)
    OP_75(0x01, 0x00, 'アッシュを選ぶ', 0x00000003)
    OP_75(0x01, 0x00, 'ミュゼを選ぶ', 0x00000004)
    OP_75(0x02, 0x00, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF9)
    OP_75(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_76DF',
    )

    SetScenaFlags(ScenaFlag(0x05D1, 2, 0x2E8A))

    Jump('loc_770E')

    def _loc_76DF(): pass

    label('loc_76DF')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_76F5',
    )

    SetScenaFlags(ScenaFlag(0x05D1, 3, 0x2E8B))

    Jump('loc_770E')

    def _loc_76F5(): pass

    label('loc_76F5')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_770B',
    )

    SetScenaFlags(ScenaFlag(0x05D1, 4, 0x2E8C))

    Jump('loc_770E')

    def _loc_770B(): pass

    label('loc_770B')

    SetScenaFlags(ScenaFlag(0x05D1, 5, 0x2E8D))

    def _loc_770E(): pass

    label('loc_770E')

    Jump('loc_7713')

    def _loc_7713(): pass

    label('loc_7713')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_773E',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_773E(): pass

    label('loc_773E')

    Jump('loc_74A9')

    def _loc_7743(): pass

    label('loc_7743')

    Return()

# id: 0x0036 offset: 0x7744
@scena.Code('EV_Jump_QS_130')
def EV_Jump_QS_130():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_774D(): pass

    label('loc_774D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D4F',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS130_01] [グレイスに話しかける　　　　　]', 0x00007100)
    MenuCmd(0x01, 0x02, '[QS130_02A][ラルフからのアンケート　　　　]', 0x00007101)
    MenuCmd(0x01, 0x02, '[QS130_02B][プルーナたちからのアンケート　]', 0x00007102)
    MenuCmd(0x01, 0x02, '[QS130_02C][ラマンダからのアンケート　　　]', 0x00007103)
    MenuCmd(0x01, 0x02, '[QS130_02D][客引きピムからのアンケート　　]', 0x00007104)
    MenuCmd(0x01, 0x02, '[QS130_02E][アイリスからのアンケート　　　]', 0x00007105)
    MenuCmd(0x01, 0x02, '[QS130_02F][ロナルドからのアンケート　　　]', 0x00007106)
    MenuCmd(0x01, 0x02, '[QS130_02G][アンネからのアンケート　　　　]', 0x00007107)
    MenuCmd(0x01, 0x02, '[QS130_02H][オーゼルからのアンケート　　　]', 0x00007108)
    MenuCmd(0x01, 0x02, '[QS130_02I][ビショップからのアンケート　　]', 0x00007109)
    MenuCmd(0x01, 0x02, '[QS130_03] [アンケート終了　　　　　　　　]', 0x0000710A)
    MenuCmd(0x01, 0x02, '[QS130_03B][仮編集部に戻る　　　　　　　　]', 0x0000710B)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AD3',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x10AA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    SetScenaFlags(ScenaFlag(0x0588, 5, 0x2C45))
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_7AD3(): pass

    label('loc_7AD3')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AF4',
    )

    QuestCtrl(0x0009, 0x04, 0x01, 0x02)
    QuestCtrl(0x0009, 0x04, 0x02, 0x02)
    QuestCtrl(0x0009, 0x04, 0x08, 0x02)

    def _loc_7AF4(): pass

    label('loc_7AF4')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000710B, 'loc_7B5D'),
        (0x0000710A, 'loc_7B60'),
        (0x00007109, 'loc_7B63'),
        (0x00007108, 'loc_7B66'),
        (0x00007107, 'loc_7B69'),
        (0x00007106, 'loc_7B6C'),
        (0x00007105, 'loc_7B6F'),
        (0x00007104, 'loc_7B72'),
        (0x00007103, 'loc_7B75'),
        (0x00007102, 'loc_7B78'),
        (0x00007101, 'loc_7B7B'),
        (0x00007100, 'loc_7B81'),
        (-1, 'loc_7B8C'),
    )

    def _loc_7B5D(): pass

    label('loc_7B5D')

    SetScenaFlags(ScenaFlag(0x05C2, 2, 0x2E12))

    def _loc_7B60(): pass

    label('loc_7B60')

    SetScenaFlags(ScenaFlag(0x05C2, 1, 0x2E11))

    def _loc_7B63(): pass

    label('loc_7B63')

    SetScenaFlags(ScenaFlag(0x05C2, 0, 0x2E10))

    def _loc_7B66(): pass

    label('loc_7B66')

    SetScenaFlags(ScenaFlag(0x05C1, 7, 0x2E0F))

    def _loc_7B69(): pass

    label('loc_7B69')

    SetScenaFlags(ScenaFlag(0x05C1, 6, 0x2E0E))

    def _loc_7B6C(): pass

    label('loc_7B6C')

    SetScenaFlags(ScenaFlag(0x05C1, 5, 0x2E0D))

    def _loc_7B6F(): pass

    label('loc_7B6F')

    SetScenaFlags(ScenaFlag(0x05C1, 4, 0x2E0C))

    def _loc_7B72(): pass

    label('loc_7B72')

    SetScenaFlags(ScenaFlag(0x05C1, 3, 0x2E0B))

    def _loc_7B75(): pass

    label('loc_7B75')

    SetScenaFlags(ScenaFlag(0x05C1, 2, 0x2E0A))

    def _loc_7B78(): pass

    label('loc_7B78')

    SetScenaFlags(ScenaFlag(0x05C1, 1, 0x2E09))

    def _loc_7B7B(): pass

    label('loc_7B7B')

    SetScenaFlags(ScenaFlag(0x05D0, 0, 0x2E80))
    SetScenaFlags(ScenaFlag(0x05C1, 0, 0x2E08))

    def _loc_7B81(): pass

    label('loc_7B81')

    QuestCtrl(0x0009, 0x03, 0x01, 0x02)

    Jump('loc_7B8C')

    def _loc_7B8C(): pass

    label('loc_7B8C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007100, 'loc_7BF5'),
        (0x00007101, 'loc_7C11'),
        (0x00007102, 'loc_7C2D'),
        (0x00007103, 'loc_7C49'),
        (0x00007104, 'loc_7C65'),
        (0x00007105, 'loc_7C81'),
        (0x00007106, 'loc_7C9D'),
        (0x00007107, 'loc_7CB9'),
        (0x00007108, 'loc_7CD5'),
        (0x00007109, 'loc_7CF1'),
        (0x0000710A, 'loc_7D0D'),
        (0x0000710B, 'loc_7D29'),
        (-1, 'loc_7D45'),
    )

    def _loc_7BF5(): pass

    label('loc_7BF5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7100, 0x0))

    Jump('loc_7D4A')

    def _loc_7C11(): pass

    label('loc_7C11')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7101, 0x0))

    Jump('loc_7D4A')

    def _loc_7C2D(): pass

    label('loc_7C2D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7102, 0x0))

    Jump('loc_7D4A')

    def _loc_7C49(): pass

    label('loc_7C49')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7103, 0x0))

    Jump('loc_7D4A')

    def _loc_7C65(): pass

    label('loc_7C65')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7104, 0x0))

    Jump('loc_7D4A')

    def _loc_7C81(): pass

    label('loc_7C81')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7105, 0x0))

    Jump('loc_7D4A')

    def _loc_7C9D(): pass

    label('loc_7C9D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7106, 0x0))

    Jump('loc_7D4A')

    def _loc_7CB9(): pass

    label('loc_7CB9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7107, 0x0))

    Jump('loc_7D4A')

    def _loc_7CD5(): pass

    label('loc_7CD5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7108, 0x0))

    Jump('loc_7D4A')

    def _loc_7CF1(): pass

    label('loc_7CF1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7109, 0x0))

    Jump('loc_7D4A')

    def _loc_7D0D(): pass

    label('loc_7D0D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x710A, 0x0))

    Jump('loc_7D4A')

    def _loc_7D29(): pass

    label('loc_7D29')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x710B, 0x0))

    Jump('loc_7D4A')

    def _loc_7D45(): pass

    label('loc_7D45')

    Jump('loc_7D4A')

    def _loc_7D4A(): pass

    label('loc_7D4A')

    Jump('loc_774D')

    def _loc_7D4F(): pass

    label('loc_7D4F')

    Return()

# id: 0x0037 offset: 0x7D50
@scena.Code('EV_Jump_QS_131')
def EV_Jump_QS_131():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_7D59(): pass

    label('loc_7D59')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7FCD',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS131_01] [星霊窟の出現を目撃する　　　　]', 0x00007120)
    MenuCmd(0x01, 0x02, '[QS131_02] [星霊窟の攻略を開始する　　　　]', 0x00007121)
    MenuCmd(0x01, 0x02, '[QS131_03] [終点の祭壇前でのボス戦　　　　]', 0x00007122)
    MenuCmd(0x01, 0x02, '[QS131_03B][幻視を見る　　　　　　　　　　]', 0x00007123)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7ECC',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x109A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_7ECC(): pass

    label('loc_7ECC')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7EED',
    )

    QuestCtrl(0x000A, 0x04, 0x01, 0x02)
    QuestCtrl(0x000A, 0x04, 0x02, 0x02)
    QuestCtrl(0x000A, 0x04, 0x08, 0x02)

    def _loc_7EED(): pass

    label('loc_7EED')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007123, 'loc_7F16'),
        (0x00007122, 'loc_7F19'),
        (0x00007121, 'loc_7F1C'),
        (0x00007120, 'loc_7F1F'),
        (-1, 'loc_7F2A'),
    )

    def _loc_7F16(): pass

    label('loc_7F16')

    SetScenaFlags(ScenaFlag(0x05C2, 6, 0x2E16))

    def _loc_7F19(): pass

    label('loc_7F19')

    SetScenaFlags(ScenaFlag(0x05C2, 5, 0x2E15))

    def _loc_7F1C(): pass

    label('loc_7F1C')

    SetScenaFlags(ScenaFlag(0x05C2, 4, 0x2E14))

    def _loc_7F1F(): pass

    label('loc_7F1F')

    QuestCtrl(0x000A, 0x03, 0x01, 0x02)

    Jump('loc_7F2A')

    def _loc_7F2A(): pass

    label('loc_7F2A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007120, 'loc_7F53'),
        (0x00007121, 'loc_7F6F'),
        (0x00007122, 'loc_7F8B'),
        (0x00007123, 'loc_7FA7'),
        (-1, 'loc_7FC3'),
    )

    def _loc_7F53(): pass

    label('loc_7F53')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7120, 0x0))

    Jump('loc_7FC8')

    def _loc_7F6F(): pass

    label('loc_7F6F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7121, 0x0))

    Jump('loc_7FC8')

    def _loc_7F8B(): pass

    label('loc_7F8B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7122, 0x0))

    Jump('loc_7FC8')

    def _loc_7FA7(): pass

    label('loc_7FA7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7123, 0x0))

    Jump('loc_7FC8')

    def _loc_7FC3(): pass

    label('loc_7FC3')

    Jump('loc_7FC8')

    def _loc_7FC8(): pass

    label('loc_7FC8')

    Jump('loc_7D59')

    def _loc_7FCD(): pass

    label('loc_7FCD')

    Return()

# id: 0x0038 offset: 0x7FD0
@scena.Code('EV_Jump_QS_132')
def EV_Jump_QS_132():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_7FD9(): pass

    label('loc_7FD9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_80D2',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS132_01][手配魔獣を撃破　　　　　　　　]', 0x00007140)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8085',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x109A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_8085(): pass

    label('loc_8085')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_809A',
    )

    QuestCtrl(0x000B, 0x04, 0x02, 0x02)

    def _loc_809A(): pass

    label('loc_809A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007140, 'loc_80AB'),
        (-1, 'loc_80C8'),
    )

    def _loc_80AB(): pass

    label('loc_80AB')

    OP_28((0xDD, 'r2220'), (0xDD, 'QS132_01_JUMP'), 0x00)

    Jump('loc_80CD')

    def _loc_80C8(): pass

    label('loc_80C8')

    Jump('loc_80CD')

    def _loc_80CD(): pass

    label('loc_80CD')

    Jump('loc_7FD9')

    def _loc_80D2(): pass

    label('loc_80D2')

    Return()

# id: 0x0039 offset: 0x80D4
@scena.Code('EV_Jump_QS_133')
def EV_Jump_QS_133():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_80DD(): pass

    label('loc_80DD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84A4',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS133_01] [ハロルド＆ソフィアと話す　　　]', 0x00007160)
    MenuCmd(0x01, 0x02, '[QS133_01B][マシューと話す　　　　　　　　]', 0x00007161)
    MenuCmd(0x01, 0x02, '[QS133_02] [案内嬢カルミナと話す　　　　　]', 0x00007162)
    MenuCmd(0x01, 0x02, '[QS133_03] [カビランに話しかける　　　　　]', 0x00007163)
    MenuCmd(0x01, 0x02, '[QS133_04] [受付嬢レミーナに話しかける　　]', 0x00007164)
    MenuCmd(0x01, 0x02, '[QS133_05] [コリンを発見する　　　　　　　]', 0x00007165)
    MenuCmd(0x01, 0x02, '[QS133_06] [達成イベント　　　　　　　　　]', 0x00007166)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8316',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x10C6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_8316(): pass

    label('loc_8316')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8337',
    )

    QuestCtrl(0x000C, 0x04, 0x01, 0x02)
    QuestCtrl(0x000C, 0x04, 0x02, 0x02)
    QuestCtrl(0x000C, 0x04, 0x08, 0x02)

    def _loc_8337(): pass

    label('loc_8337')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007166, 'loc_8378'),
        (0x00007165, 'loc_837B'),
        (0x00007164, 'loc_837E'),
        (0x00007163, 'loc_8381'),
        (0x00007162, 'loc_8384'),
        (0x00007161, 'loc_8387'),
        (0x00007160, 'loc_8390'),
        (-1, 'loc_8395'),
    )

    def _loc_8378(): pass

    label('loc_8378')

    SetScenaFlags(ScenaFlag(0x05C4, 0, 0x2E20))

    def _loc_837B(): pass

    label('loc_837B')

    SetScenaFlags(ScenaFlag(0x05C3, 7, 0x2E1F))

    def _loc_837E(): pass

    label('loc_837E')

    SetScenaFlags(ScenaFlag(0x05C3, 6, 0x2E1E))

    def _loc_8381(): pass

    label('loc_8381')

    SetScenaFlags(ScenaFlag(0x05C3, 5, 0x2E1D))

    def _loc_8384(): pass

    label('loc_8384')

    SetScenaFlags(ScenaFlag(0x05C3, 4, 0x2E1C))

    def _loc_8387(): pass

    label('loc_8387')

    SetScenaFlags(ScenaFlag(0x05C3, 3, 0x2E1B))
    QuestCtrl(0x000C, 0x03, 0x01, 0x02)

    def _loc_8390(): pass

    label('loc_8390')

    Jump('loc_8395')

    def _loc_8395(): pass

    label('loc_8395')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007160, 'loc_83D6'),
        (0x00007161, 'loc_83F2'),
        (0x00007162, 'loc_840E'),
        (0x00007163, 'loc_842A'),
        (0x00007164, 'loc_8446'),
        (0x00007165, 'loc_8462'),
        (0x00007166, 'loc_847E'),
        (-1, 'loc_849A'),
    )

    def _loc_83D6(): pass

    label('loc_83D6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7160, 0x0))

    Jump('loc_849F')

    def _loc_83F2(): pass

    label('loc_83F2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7161, 0x0))

    Jump('loc_849F')

    def _loc_840E(): pass

    label('loc_840E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7162, 0x0))

    Jump('loc_849F')

    def _loc_842A(): pass

    label('loc_842A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7163, 0x0))

    Jump('loc_849F')

    def _loc_8446(): pass

    label('loc_8446')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7164, 0x0))

    Jump('loc_849F')

    def _loc_8462(): pass

    label('loc_8462')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7165, 0x0))

    Jump('loc_849F')

    def _loc_847E(): pass

    label('loc_847E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7166, 0x0))

    Jump('loc_849F')

    def _loc_849A(): pass

    label('loc_849A')

    Jump('loc_849F')

    def _loc_849F(): pass

    label('loc_849F')

    Jump('loc_80DD')

    def _loc_84A4(): pass

    label('loc_84A4')

    Return()

# id: 0x003A offset: 0x84A8
@scena.Code('EV_Jump_QS_150')
def EV_Jump_QS_150():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_84B1(): pass

    label('loc_84B1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_872C',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS150_01] [エマ＆ガンドルフに話しかける　]', 0x00007180)
    MenuCmd(0x01, 0x02, '[QS150_02A][ドリアード・ティア入手　　　　]', 0x00007181)
    MenuCmd(0x01, 0x02, '[QS150_02B][ロートスの蔦入手　　　　　　　]', 0x00007182)
    MenuCmd(0x01, 0x02, '[QS150_03] [クエスト達成　　　　　　　　　]', 0x00007183)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8625',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x2008),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01X')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_8625(): pass

    label('loc_8625')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8646',
    )

    QuestCtrl(0x000D, 0x04, 0x01, 0x02)
    QuestCtrl(0x000D, 0x04, 0x02, 0x02)
    QuestCtrl(0x000D, 0x04, 0x08, 0x02)

    def _loc_8646(): pass

    label('loc_8646')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007183, 'loc_866F'),
        (0x00007182, 'loc_8675'),
        (0x00007181, 'loc_8675'),
        (0x00007180, 'loc_8684'),
        (-1, 'loc_8689'),
    )

    def _loc_866F(): pass

    label('loc_866F')

    SetScenaFlags(ScenaFlag(0x05C4, 4, 0x2E24))
    SetScenaFlags(ScenaFlag(0x05C4, 3, 0x2E23))

    def _loc_8675(): pass

    label('loc_8675')

    SetScenaFlags(ScenaFlag(0x05D0, 3, 0x2E83))
    SetScenaFlags(ScenaFlag(0x05C4, 2, 0x2E22))
    QuestCtrl(0x000D, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    def _loc_8684(): pass

    label('loc_8684')

    Jump('loc_8689')

    def _loc_8689(): pass

    label('loc_8689')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007180, 'loc_86B2'),
        (0x00007181, 'loc_86CE'),
        (0x00007182, 'loc_86EA'),
        (0x00007183, 'loc_8706'),
        (-1, 'loc_8722'),
    )

    def _loc_86B2(): pass

    label('loc_86B2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7180, 0x0))

    Jump('loc_8727')

    def _loc_86CE(): pass

    label('loc_86CE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7181, 0x0))

    Jump('loc_8727')

    def _loc_86EA(): pass

    label('loc_86EA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7182, 0x0))

    Jump('loc_8727')

    def _loc_8706(): pass

    label('loc_8706')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7183, 0x0))

    Jump('loc_8727')

    def _loc_8722(): pass

    label('loc_8722')

    Jump('loc_8727')

    def _loc_8727(): pass

    label('loc_8727')

    Jump('loc_84B1')

    def _loc_872C(): pass

    label('loc_872C')

    Return()

# id: 0x003B offset: 0x8730
@scena.Code('EV_Jump_QS_220')
def EV_Jump_QS_220():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8739(): pass

    label('loc_8739')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B68',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS220_01] [元締めから話を聞く　　　　　　]', 0x000071A0)
    MenuCmd(0x01, 0x02, '[QS220_02A][シーラから話を聞く　　　　　　]', 0x000071A1)
    MenuCmd(0x01, 0x02, '[QS220_02B][帝都憲兵から話を聞く　　　　　]', 0x000071A2)
    MenuCmd(0x01, 0x02, '[QS220_02C][ジェロームたちから話を聞く　　]', 0x000071A3)
    MenuCmd(0x01, 0x02, '[QS220_03] [情報整理する　　　　　　　　　]', 0x000071A4)
    MenuCmd(0x01, 0x02, '[QS220_04] [街道でトラックを見つける　　　]', 0x000071A5)
    MenuCmd(0x01, 0x02, '[QS220_04B][支援基金の正体を暴く　　　　　]', 0x000071A6)
    MenuCmd(0x01, 0x02, '[QS220_05] [解決イベント　　　　　　　　　]', 0x000071A7)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89B4',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_89B4(): pass

    label('loc_89B4')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89C9',
    )

    QuestCtrl(0x000E, 0x04, 0x02, 0x02)

    def _loc_89C9(): pass

    label('loc_89C9')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000071A7, 'loc_8A12'),
        (0x000071A6, 'loc_8A15'),
        (0x000071A5, 'loc_8A18'),
        (0x000071A4, 'loc_8A1B'),
        (0x000071A3, 'loc_8A1E'),
        (0x000071A2, 'loc_8A21'),
        (0x000071A1, 'loc_8A24'),
        (0x000071A0, 'loc_8A27'),
        (-1, 'loc_8A35'),
    )

    def _loc_8A12(): pass

    label('loc_8A12')

    SetScenaFlags(ScenaFlag(0x0753, 3, 0x3A9B))

    def _loc_8A15(): pass

    label('loc_8A15')

    SetScenaFlags(ScenaFlag(0x0753, 2, 0x3A9A))

    def _loc_8A18(): pass

    label('loc_8A18')

    SetScenaFlags(ScenaFlag(0x0753, 1, 0x3A99))

    def _loc_8A1B(): pass

    label('loc_8A1B')

    SetScenaFlags(ScenaFlag(0x0753, 0, 0x3A98))

    def _loc_8A1E(): pass

    label('loc_8A1E')

    SetScenaFlags(ScenaFlag(0x0752, 7, 0x3A97))

    def _loc_8A21(): pass

    label('loc_8A21')

    SetScenaFlags(ScenaFlag(0x0752, 6, 0x3A96))

    def _loc_8A24(): pass

    label('loc_8A24')

    SetScenaFlags(ScenaFlag(0x0752, 5, 0x3A95))

    def _loc_8A27(): pass

    label('loc_8A27')

    QuestCtrl(0x000E, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    Jump('loc_8A35')

    def _loc_8A35(): pass

    label('loc_8A35')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000071A0, 'loc_8A7E'),
        (0x000071A1, 'loc_8A9A'),
        (0x000071A2, 'loc_8AB6'),
        (0x000071A3, 'loc_8AD2'),
        (0x000071A4, 'loc_8AEE'),
        (0x000071A5, 'loc_8B0A'),
        (0x000071A6, 'loc_8B26'),
        (0x000071A7, 'loc_8B42'),
        (-1, 'loc_8B5E'),
    )

    def _loc_8A7E(): pass

    label('loc_8A7E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A0, 0x0))

    Jump('loc_8B63')

    def _loc_8A9A(): pass

    label('loc_8A9A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A1, 0x0))

    Jump('loc_8B63')

    def _loc_8AB6(): pass

    label('loc_8AB6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A2, 0x0))

    Jump('loc_8B63')

    def _loc_8AD2(): pass

    label('loc_8AD2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A3, 0x0))

    Jump('loc_8B63')

    def _loc_8AEE(): pass

    label('loc_8AEE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A4, 0x0))

    Jump('loc_8B63')

    def _loc_8B0A(): pass

    label('loc_8B0A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A5, 0x0))

    Jump('loc_8B63')

    def _loc_8B26(): pass

    label('loc_8B26')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A6, 0x0))

    Jump('loc_8B63')

    def _loc_8B42(): pass

    label('loc_8B42')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71A7, 0x0))

    Jump('loc_8B63')

    def _loc_8B5E(): pass

    label('loc_8B5E')

    Jump('loc_8B63')

    def _loc_8B63(): pass

    label('loc_8B63')

    Jump('loc_8739')

    def _loc_8B68(): pass

    label('loc_8B68')

    Return()

# id: 0x003C offset: 0x8B6C
@scena.Code('EV_Jump_QS_221')
def EV_Jump_QS_221():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8B75(): pass

    label('loc_8B75')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8E60',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS221_01] [オーヴィッドに話しかける　　　]', 0x000071C0)
    MenuCmd(0x01, 0x02, '[QS221_02A][パルム間道②のＬＰを調べる　　]', 0x000071C1)
    MenuCmd(0x01, 0x02, '[QS221_02B][パルム間道①のＬＰを調べる　　]', 0x000071C2)
    MenuCmd(0x01, 0x02, '[QS221_03] [アグリア旧道でフレディを発見　]', 0x000071C3)
    MenuCmd(0x01, 0x02, '[QS221_04] [クエスト達成　　　　　　　　　]', 0x000071C4)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D2D',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    def _loc_8D2D(): pass

    label('loc_8D2D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D4E',
    )

    QuestCtrl(0x000F, 0x04, 0x01, 0x02)
    QuestCtrl(0x000F, 0x04, 0x02, 0x02)
    QuestCtrl(0x000F, 0x04, 0x08, 0x02)

    def _loc_8D4E(): pass

    label('loc_8D4E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000071C4, 'loc_8D7F'),
        (0x000071C3, 'loc_8D82'),
        (0x000071C2, 'loc_8D8B'),
        (0x000071C1, 'loc_8D8B'),
        (0x000071C0, 'loc_8D8E'),
        (-1, 'loc_8D99'),
    )

    def _loc_8D7F(): pass

    label('loc_8D7F')

    SetScenaFlags(ScenaFlag(0x0756, 2, 0x3AB2))

    def _loc_8D82(): pass

    label('loc_8D82')

    SetScenaFlags(ScenaFlag(0x0756, 1, 0x3AB1))
    SetScenaFlags(ScenaFlag(0x0756, 0, 0x3AB0))
    SetScenaFlags(ScenaFlag(0x0763, 6, 0x3B1E))

    def _loc_8D8B(): pass

    label('loc_8D8B')

    SetScenaFlags(ScenaFlag(0x0755, 7, 0x3AAF))

    def _loc_8D8E(): pass

    label('loc_8D8E')

    QuestCtrl(0x000F, 0x03, 0x01, 0x02)

    Jump('loc_8D99')

    def _loc_8D99(): pass

    label('loc_8D99')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000071C0, 'loc_8DCA'),
        (0x000071C1, 'loc_8DE6'),
        (0x000071C2, 'loc_8E02'),
        (0x000071C3, 'loc_8E1E'),
        (0x000071C4, 'loc_8E3A'),
        (-1, 'loc_8E56'),
    )

    def _loc_8DCA(): pass

    label('loc_8DCA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71C0, 0x0))

    Jump('loc_8E5B')

    def _loc_8DE6(): pass

    label('loc_8DE6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71C1, 0x0))

    Jump('loc_8E5B')

    def _loc_8E02(): pass

    label('loc_8E02')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71C2, 0x0))

    Jump('loc_8E5B')

    def _loc_8E1E(): pass

    label('loc_8E1E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71C3, 0x0))

    Jump('loc_8E5B')

    def _loc_8E3A(): pass

    label('loc_8E3A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x71C4, 0x0))

    Jump('loc_8E5B')

    def _loc_8E56(): pass

    label('loc_8E56')

    Jump('loc_8E5B')

    def _loc_8E5B(): pass

    label('loc_8E5B')

    Jump('loc_8B75')

    def _loc_8E60(): pass

    label('loc_8E60')

    Return()

# id: 0x003D offset: 0x8E64
@scena.Code('EV_Jump_QS_222')
def EV_Jump_QS_222():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8E6D(): pass

    label('loc_8E6D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F6F',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS222_01][手配魔獣を撃破　　　　　　　　]', 0x000071E0)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F19',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_8F19(): pass

    label('loc_8F19')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F34',
    )

    QuestCtrl(0x0010, 0x03, 0x01, 0x02)
    QuestCtrl(0x0010, 0x04, 0x02, 0x02)

    def _loc_8F34(): pass

    label('loc_8F34')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000071E0, 'loc_8F45'),
        (-1, 'loc_8F65'),
    )

    def _loc_8F45(): pass

    label('loc_8F45')

    FormationCtrl(0x1C, 0x01)
    OP_28((0xDD, 'r1210'), (0xDD, 'QS222_01_JUMP'), 0x00)

    Jump('loc_8F6A')

    def _loc_8F65(): pass

    label('loc_8F65')

    Jump('loc_8F6A')

    def _loc_8F6A(): pass

    label('loc_8F6A')

    Jump('loc_8E6D')

    def _loc_8F6F(): pass

    label('loc_8F6F')

    Return()

# id: 0x003E offset: 0x8F70
@scena.Code('EV_Jump_QS_223')
def EV_Jump_QS_223():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8F79(): pass

    label('loc_8F79')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_950A',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS223_01] [リヴィエラコートに入る　　　　]', 0x00007200)
    MenuCmd(0x01, 0x02, '[QS223_02A][レジを調べる　　　　　　　　　]', 0x00007201)
    MenuCmd(0x01, 0x02, '[QS223_02B][カーポに話を聞く　　　　　　　]', 0x00007202)
    MenuCmd(0x01, 0x02, '[QS223_02C][窓を調べる　　　　　　　　　　]', 0x00007203)
    MenuCmd(0x01, 0x02, '[QS223_03] [案内状に気が付く　　　　　　　]', 0x00007204)
    MenuCmd(0x01, 0x02, '[QS223_04] [執事オリバーに話しかける　　　]', 0x00007205)
    MenuCmd(0x01, 0x02, '[QS223_05] [グリシーヌに話しかける　　　　]', 0x00007206)
    MenuCmd(0x01, 0x02, '[QS223_06] [ハーマンに話しかける　　　　　]', 0x00007207)
    MenuCmd(0x01, 0x02, '[QS223_07] [許可証を届ける　　　　　　　　]', 0x00007208)
    MenuCmd(0x01, 0x02, '[QS223_07B][港湾区のリヴィエラコートの外観]', 0x00007209)
    MenuCmd(0x01, 0x02, '[QS223_07C][リヴィエラコート移転　　　　　]', 0x0000720A)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92BA',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3036),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_92BA(): pass

    label('loc_92BA')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92DB',
    )

    QuestCtrl(0x0011, 0x04, 0x01, 0x02)
    QuestCtrl(0x0011, 0x04, 0x02, 0x02)
    QuestCtrl(0x0011, 0x04, 0x08, 0x02)

    def _loc_92DB(): pass

    label('loc_92DB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000720A, 'loc_933C'),
        (0x00007209, 'loc_933F'),
        (0x00007208, 'loc_9342'),
        (0x00007207, 'loc_9345'),
        (0x00007206, 'loc_9348'),
        (0x00007205, 'loc_934B'),
        (0x00007204, 'loc_934E'),
        (0x00007203, 'loc_9354'),
        (0x00007202, 'loc_9357'),
        (0x00007201, 'loc_935A'),
        (0x00007200, 'loc_9366'),
        (-1, 'loc_936B'),
    )

    def _loc_933C(): pass

    label('loc_933C')

    SetScenaFlags(ScenaFlag(0x075A, 5, 0x3AD5))

    def _loc_933F(): pass

    label('loc_933F')

    SetScenaFlags(ScenaFlag(0x075A, 4, 0x3AD4))

    def _loc_9342(): pass

    label('loc_9342')

    SetScenaFlags(ScenaFlag(0x075A, 3, 0x3AD3))

    def _loc_9345(): pass

    label('loc_9345')

    SetScenaFlags(ScenaFlag(0x075A, 2, 0x3AD2))

    def _loc_9348(): pass

    label('loc_9348')

    SetScenaFlags(ScenaFlag(0x075A, 1, 0x3AD1))

    def _loc_934B(): pass

    label('loc_934B')

    SetScenaFlags(ScenaFlag(0x075A, 0, 0x3AD0))

    def _loc_934E(): pass

    label('loc_934E')

    SetScenaFlags(ScenaFlag(0x0764, 2, 0x3B22))
    SetScenaFlags(ScenaFlag(0x0759, 7, 0x3ACF))

    def _loc_9354(): pass

    label('loc_9354')

    SetScenaFlags(ScenaFlag(0x0759, 6, 0x3ACE))

    def _loc_9357(): pass

    label('loc_9357')

    SetScenaFlags(ScenaFlag(0x0759, 5, 0x3ACD))

    def _loc_935A(): pass

    label('loc_935A')

    SetScenaFlags(ScenaFlag(0x0764, 0, 0x3B20))
    SetScenaFlags(ScenaFlag(0x0759, 4, 0x3ACC))
    QuestCtrl(0x0011, 0x03, 0x01, 0x02)

    def _loc_9366(): pass

    label('loc_9366')

    Jump('loc_936B')

    def _loc_936B(): pass

    label('loc_936B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007200, 'loc_93CC'),
        (0x00007201, 'loc_93E8'),
        (0x00007202, 'loc_9404'),
        (0x00007203, 'loc_9420'),
        (0x00007204, 'loc_943C'),
        (0x00007205, 'loc_9458'),
        (0x00007206, 'loc_9474'),
        (0x00007207, 'loc_9490'),
        (0x00007208, 'loc_94AC'),
        (0x00007209, 'loc_94C8'),
        (0x0000720A, 'loc_94E4'),
        (-1, 'loc_9500'),
    )

    def _loc_93CC(): pass

    label('loc_93CC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7200, 0x0))

    Jump('loc_9505')

    def _loc_93E8(): pass

    label('loc_93E8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7201, 0x0))

    Jump('loc_9505')

    def _loc_9404(): pass

    label('loc_9404')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7202, 0x0))

    Jump('loc_9505')

    def _loc_9420(): pass

    label('loc_9420')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7203, 0x0))

    Jump('loc_9505')

    def _loc_943C(): pass

    label('loc_943C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7204, 0x0))

    Jump('loc_9505')

    def _loc_9458(): pass

    label('loc_9458')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7205, 0x0))

    Jump('loc_9505')

    def _loc_9474(): pass

    label('loc_9474')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7206, 0x0))

    Jump('loc_9505')

    def _loc_9490(): pass

    label('loc_9490')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7207, 0x0))

    Jump('loc_9505')

    def _loc_94AC(): pass

    label('loc_94AC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7208, 0x0))

    Jump('loc_9505')

    def _loc_94C8(): pass

    label('loc_94C8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7209, 0x0))

    Jump('loc_9505')

    def _loc_94E4(): pass

    label('loc_94E4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x720A, 0x0))

    Jump('loc_9505')

    def _loc_9500(): pass

    label('loc_9500')

    Jump('loc_9505')

    def _loc_9505(): pass

    label('loc_9505')

    Jump('loc_8F79')

    def _loc_950A(): pass

    label('loc_950A')

    Return()

# id: 0x003F offset: 0x950C
@scena.Code('EV_Jump_QS_230')
def EV_Jump_QS_230():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9515(): pass

    label('loc_9515')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A39',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS230_01]    [カエラから話を聞く　　　　　　]', 0x00007220)
    MenuCmd(0x01, 0x02, '[QS230_02]    [フォックスから話を聞く　　　　]', 0x00007221)
    MenuCmd(0x01, 0x02, '[QS230_03]    [イカロスマートで聞き込み　　　]', 0x00007222)
    MenuCmd(0x01, 0x02, '[QS230_04]    [マッケンローから話を聞く　　　]', 0x00007223)
    MenuCmd(0x01, 0x02, '[QS230_05]    [コーディの気配を察知する　　　]', 0x00007224)
    MenuCmd(0x01, 0x02, '[QS230_05ST_A][ＳＴ：質屋の先　　　　　　　　]', 0x00007225)
    MenuCmd(0x01, 0x02, '[QS230_05ST_B][ＳＴ：教会の前の道　　　　　　]', 0x00007226)
    MenuCmd(0x01, 0x02, '[QS230_05ST_C][ＳＴ：西峡谷道のエントリ　　　]', 0x00007227)
    MenuCmd(0x01, 0x02, '[QS230_05ST_D][ＳＴ：屋内（５箇所）　　　　　]', 0x00007228)
    MenuCmd(0x01, 0x02, '[QS230_06]    [カジノ前でコーディ発見　　　　]', 0x00007229)
    MenuCmd(0x01, 0x02, '[QS230_06B]   [北峡谷道へ　　　　　　　　　　]', 0x0000722A)
    MenuCmd(0x01, 0x02, '[QS230_06ST]  [ＳＴ：北峡谷道②のエントリ　　]', 0x0000722B)
    MenuCmd(0x01, 0x02, '[QS230_06ST_B][ＳＴ：ラクウェルのエントリ　　]', 0x0000722C)
    MenuCmd(0x01, 0x02, '[QS230_07]    [ハーキュリーズを発見　　　　　]', 0x0000722D)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9949',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    def _loc_9949(): pass

    label('loc_9949')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_996A',
    )

    QuestCtrl(0x0012, 0x04, 0x01, 0x02)
    QuestCtrl(0x0012, 0x04, 0x02, 0x02)
    QuestCtrl(0x0012, 0x04, 0x08, 0x02)

    def _loc_996A(): pass

    label('loc_996A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000722D, 'loc_99E3'),
        (0x0000722C, 'loc_99E6'),
        (0x0000722B, 'loc_99E9'),
        (0x0000722A, 'loc_99EC'),
        (0x00007229, 'loc_99EF'),
        (0x00007228, 'loc_99EF'),
        (0x00007227, 'loc_99EF'),
        (0x00007226, 'loc_99EF'),
        (0x00007225, 'loc_99EF'),
        (0x00007224, 'loc_99F2'),
        (0x00007223, 'loc_99F5'),
        (0x00007222, 'loc_99F8'),
        (0x00007221, 'loc_99FB'),
        (0x00007220, 'loc_99FE'),
        (-1, 'loc_9A09'),
    )

    def _loc_99E3(): pass

    label('loc_99E3')

    SetScenaFlags(ScenaFlag(0x075A, 7, 0x3AD7))

    def _loc_99E6(): pass

    label('loc_99E6')

    SetScenaFlags(ScenaFlag(0x0757, 7, 0x3ABF))

    def _loc_99E9(): pass

    label('loc_99E9')

    SetScenaFlags(ScenaFlag(0x0757, 6, 0x3ABE))

    def _loc_99EC(): pass

    label('loc_99EC')

    SetScenaFlags(ScenaFlag(0x0757, 5, 0x3ABD))

    def _loc_99EF(): pass

    label('loc_99EF')

    SetScenaFlags(ScenaFlag(0x0757, 0, 0x3AB8))

    def _loc_99F2(): pass

    label('loc_99F2')

    SetScenaFlags(ScenaFlag(0x0756, 7, 0x3AB7))

    def _loc_99F5(): pass

    label('loc_99F5')

    SetScenaFlags(ScenaFlag(0x0756, 6, 0x3AB6))

    def _loc_99F8(): pass

    label('loc_99F8')

    SetScenaFlags(ScenaFlag(0x0756, 5, 0x3AB5))

    def _loc_99FB(): pass

    label('loc_99FB')

    SetScenaFlags(ScenaFlag(0x0756, 4, 0x3AB4))

    def _loc_99FE(): pass

    label('loc_99FE')

    QuestCtrl(0x0012, 0x03, 0x01, 0x02)

    Jump('loc_9A09')

    def _loc_9A09(): pass

    label('loc_9A09')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A34',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_9A34(): pass

    label('loc_9A34')

    Jump('loc_9515')

    def _loc_9A39(): pass

    label('loc_9A39')

    Return()

# id: 0x0040 offset: 0x9A3C
@scena.Code('EV_Jump_QS_231')
def EV_Jump_QS_231():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9A45(): pass

    label('loc_9A45')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D9E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS231_01] [ミリオたちと話をする　　　　　]', 0x00007240)
    MenuCmd(0x01, 0x02, '[QS231_02A][パルムで材料調達　　　　　　　]', 0x00007241)
    MenuCmd(0x01, 0x02, '[QS231_02B][エリンの里で材料調達　　　　　]', 0x00007242)
    MenuCmd(0x01, 0x02, '[QS231_02C][メルカバで材料調達　　　　　　]', 0x00007243)
    MenuCmd(0x01, 0x02, '[QS231_03] [ミリオたちに材料を渡す　　　　]', 0x00007244)
    MenuCmd(0x01, 0x02, '[QS231_03B][クエスト達成　　　　　　　　　]', 0x00007245)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C3F',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    def _loc_9C3F(): pass

    label('loc_9C3F')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C60',
    )

    QuestCtrl(0x0013, 0x04, 0x01, 0x02)
    QuestCtrl(0x0013, 0x04, 0x02, 0x02)
    QuestCtrl(0x0013, 0x04, 0x08, 0x02)

    def _loc_9C60(): pass

    label('loc_9C60')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007245, 'loc_9C99'),
        (0x00007244, 'loc_9CA5'),
        (0x00007243, 'loc_9CA5'),
        (0x00007242, 'loc_9CA5'),
        (0x00007241, 'loc_9CA5'),
        (0x00007240, 'loc_9CA8'),
        (-1, 'loc_9CB3'),
    )

    def _loc_9C99(): pass

    label('loc_9C99')

    SetScenaFlags(ScenaFlag(0x0758, 5, 0x3AC5))
    SetScenaFlags(ScenaFlag(0x0758, 4, 0x3AC4))
    SetScenaFlags(ScenaFlag(0x0758, 3, 0x3AC3))
    SetScenaFlags(ScenaFlag(0x0758, 2, 0x3AC2))

    def _loc_9CA5(): pass

    label('loc_9CA5')

    SetScenaFlags(ScenaFlag(0x0758, 1, 0x3AC1))

    def _loc_9CA8(): pass

    label('loc_9CA8')

    QuestCtrl(0x0013, 0x03, 0x01, 0x02)

    Jump('loc_9CB3')

    def _loc_9CB3(): pass

    label('loc_9CB3')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007240, 'loc_9CEC'),
        (0x00007241, 'loc_9D08'),
        (0x00007242, 'loc_9D24'),
        (0x00007243, 'loc_9D40'),
        (0x00007244, 'loc_9D5C'),
        (0x00007245, 'loc_9D78'),
        (-1, 'loc_9D94'),
    )

    def _loc_9CEC(): pass

    label('loc_9CEC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7240, 0x0))

    Jump('loc_9D99')

    def _loc_9D08(): pass

    label('loc_9D08')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7241, 0x0))

    Jump('loc_9D99')

    def _loc_9D24(): pass

    label('loc_9D24')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7242, 0x0))

    Jump('loc_9D99')

    def _loc_9D40(): pass

    label('loc_9D40')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7243, 0x0))

    Jump('loc_9D99')

    def _loc_9D5C(): pass

    label('loc_9D5C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7244, 0x0))

    Jump('loc_9D99')

    def _loc_9D78(): pass

    label('loc_9D78')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7245, 0x0))

    Jump('loc_9D99')

    def _loc_9D94(): pass

    label('loc_9D94')

    Jump('loc_9D99')

    def _loc_9D99(): pass

    label('loc_9D99')

    Jump('loc_9A45')

    def _loc_9D9E(): pass

    label('loc_9D9E')

    Return()

# id: 0x0041 offset: 0x9DA0
@scena.Code('EV_Jump_QS_232')
def EV_Jump_QS_232():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9DA9(): pass

    label('loc_9DA9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9EA8',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS232_01][手配魔獣を撃破　　　　　　　　]', 0x00007260)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9E55',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_9E55(): pass

    label('loc_9E55')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9E70',
    )

    QuestCtrl(0x0014, 0x03, 0x01, 0x02)
    QuestCtrl(0x0014, 0x04, 0x02, 0x02)

    def _loc_9E70(): pass

    label('loc_9E70')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007260, 'loc_9E81'),
        (-1, 'loc_9E9E'),
    )

    def _loc_9E81(): pass

    label('loc_9E81')

    OP_28((0xDD, 'r3010'), (0xDD, 'QS232_01_JUMP'), 0x00)

    Jump('loc_9EA3')

    def _loc_9E9E(): pass

    label('loc_9E9E')

    Jump('loc_9EA3')

    def _loc_9EA3(): pass

    label('loc_9EA3')

    Jump('loc_9DA9')

    def _loc_9EA8(): pass

    label('loc_9EA8')

    Return()

# id: 0x0042 offset: 0x9EAC
@scena.Code('EV_Jump_QS_233')
def EV_Jump_QS_233():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9EB5(): pass

    label('loc_9EB5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A295',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS233_00] [アルベールの一般会話　　　　　]', 0x00007280)
    MenuCmd(0x01, 0x02, '[QS233_01] [依頼を聞く　　　　　　　　　　]', 0x00007281)
    MenuCmd(0x01, 0x02, '[QS233_02] [馬を発見する　　　　　　　　　]', 0x00007282)
    MenuCmd(0x01, 0x02, '[QS233_03] [馬を再び発見する　　　　　　　]', 0x00007283)
    MenuCmd(0x01, 0x02, '[QS233_04] [ダーティスタリオンとの戦闘　　]', 0x00007284)
    MenuCmd(0x01, 0x02, '[QS233_04B][浄化されるカイザーダイス　　　]', 0x00007285)
    MenuCmd(0x01, 0x02, '[QS233_05] [達成イベント　　　　　　　　　]', 0x00007286)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A10A',
    )

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x7280),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A0D8',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x306B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A0E1')

    def _loc_A0D8(): pass

    label('loc_A0D8')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x306D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A0E1(): pass

    label('loc_A0E1')

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_A10A(): pass

    label('loc_A10A')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A12B',
    )

    QuestCtrl(0x0015, 0x04, 0x01, 0x02)
    QuestCtrl(0x0015, 0x04, 0x02, 0x02)
    QuestCtrl(0x0015, 0x04, 0x08, 0x02)

    def _loc_A12B(): pass

    label('loc_A12B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007286, 'loc_A16C'),
        (0x00007285, 'loc_A16F'),
        (0x00007284, 'loc_A172'),
        (0x00007283, 'loc_A175'),
        (0x00007282, 'loc_A178'),
        (0x00007281, 'loc_A17B'),
        (0x00007280, 'loc_A181'),
        (-1, 'loc_A186'),
    )

    def _loc_A16C(): pass

    label('loc_A16C')

    SetScenaFlags(ScenaFlag(0x0754, 1, 0x3AA1))

    def _loc_A16F(): pass

    label('loc_A16F')

    SetScenaFlags(ScenaFlag(0x0754, 0, 0x3AA0))

    def _loc_A172(): pass

    label('loc_A172')

    SetScenaFlags(ScenaFlag(0x0753, 7, 0x3A9F))

    def _loc_A175(): pass

    label('loc_A175')

    SetScenaFlags(ScenaFlag(0x0753, 6, 0x3A9E))

    def _loc_A178(): pass

    label('loc_A178')

    SetScenaFlags(ScenaFlag(0x0753, 5, 0x3A9D))

    def _loc_A17B(): pass

    label('loc_A17B')

    SetScenaFlags(ScenaFlag(0x06F6, 4, 0x37B4))
    SetScenaFlags(ScenaFlag(0x075B, 0, 0x3AD8))

    def _loc_A181(): pass

    label('loc_A181')

    Jump('loc_A186')

    def _loc_A186(): pass

    label('loc_A186')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007280, 'loc_A1C7'),
        (0x00007281, 'loc_A1E3'),
        (0x00007282, 'loc_A1FF'),
        (0x00007283, 'loc_A21B'),
        (0x00007284, 'loc_A237'),
        (0x00007285, 'loc_A253'),
        (0x00007286, 'loc_A26F'),
        (-1, 'loc_A28B'),
    )

    def _loc_A1C7(): pass

    label('loc_A1C7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7280, 0x0))

    Jump('loc_A290')

    def _loc_A1E3(): pass

    label('loc_A1E3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7281, 0x0))

    Jump('loc_A290')

    def _loc_A1FF(): pass

    label('loc_A1FF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7282, 0x0))

    Jump('loc_A290')

    def _loc_A21B(): pass

    label('loc_A21B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7283, 0x0))

    Jump('loc_A290')

    def _loc_A237(): pass

    label('loc_A237')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7284, 0x0))

    Jump('loc_A290')

    def _loc_A253(): pass

    label('loc_A253')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7285, 0x0))

    Jump('loc_A290')

    def _loc_A26F(): pass

    label('loc_A26F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7286, 0x0))

    Jump('loc_A290')

    def _loc_A28B(): pass

    label('loc_A28B')

    Jump('loc_A290')

    def _loc_A290(): pass

    label('loc_A290')

    Jump('loc_9EB5')

    def _loc_A295(): pass

    label('loc_A295')

    Return()

# id: 0x0043 offset: 0xA298
@scena.Code('EV_Jump_QS_240')
def EV_Jump_QS_240():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A2A1(): pass

    label('loc_A2A1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A66B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS240_01] [老婦人に話しかける　　　　　　]', 0x000072A0)
    MenuCmd(0x01, 0x02, '[QS240_01B][老婦人から話を聞く　　　　　　]', 0x000072A1)
    MenuCmd(0x01, 0x02, '[QS240_02] [兄妹宅でトランク発見　　　　　]', 0x000072A2)
    MenuCmd(0x01, 0x02, '[QS240_02B][『シャル』を発見する　　　　　]', 0x000072A3)
    MenuCmd(0x01, 0x02, '[QS240_03] [白百合の場所でトランク発見　　]', 0x000072A4)
    MenuCmd(0x01, 0x02, '[QS240_04] [第１相最奥でトランク発見　　　]', 0x000072A5)
    MenuCmd(0x01, 0x02, '[QS240_04B][マリアベル＆怪盗Ｂ登場　　　　]', 0x000072A6)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4C4',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    def _loc_A4C4(): pass

    label('loc_A4C4')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4E5',
    )

    QuestCtrl(0x0016, 0x04, 0x01, 0x02)
    QuestCtrl(0x0016, 0x04, 0x02, 0x02)
    QuestCtrl(0x0016, 0x04, 0x08, 0x02)

    def _loc_A4E5(): pass

    label('loc_A4E5')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000072A6, 'loc_A526'),
        (0x000072A5, 'loc_A529'),
        (0x000072A4, 'loc_A52C'),
        (0x000072A3, 'loc_A52F'),
        (0x000072A2, 'loc_A532'),
        (0x000072A1, 'loc_A535'),
        (0x000072A0, 'loc_A538'),
        (-1, 'loc_A55C'),
    )

    def _loc_A526(): pass

    label('loc_A526')

    SetScenaFlags(ScenaFlag(0x0750, 7, 0x3A87))

    def _loc_A529(): pass

    label('loc_A529')

    SetScenaFlags(ScenaFlag(0x0750, 6, 0x3A86))

    def _loc_A52C(): pass

    label('loc_A52C')

    SetScenaFlags(ScenaFlag(0x0750, 5, 0x3A85))

    def _loc_A52F(): pass

    label('loc_A52F')

    SetScenaFlags(ScenaFlag(0x0750, 4, 0x3A84))

    def _loc_A532(): pass

    label('loc_A532')

    SetScenaFlags(ScenaFlag(0x0750, 3, 0x3A83))

    def _loc_A535(): pass

    label('loc_A535')

    SetScenaFlags(ScenaFlag(0x0750, 2, 0x3A82))

    def _loc_A538(): pass

    label('loc_A538')

    QuestCtrl(0x0016, 0x03, 0x01, 0x02)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    Jump('loc_A55C')

    def _loc_A55C(): pass

    label('loc_A55C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000072A0, 'loc_A59D'),
        (0x000072A1, 'loc_A5B9'),
        (0x000072A2, 'loc_A5D5'),
        (0x000072A3, 'loc_A5F1'),
        (0x000072A4, 'loc_A60D'),
        (0x000072A5, 'loc_A629'),
        (0x000072A6, 'loc_A645'),
        (-1, 'loc_A661'),
    )

    def _loc_A59D(): pass

    label('loc_A59D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72A0, 0x0))

    Jump('loc_A666')

    def _loc_A5B9(): pass

    label('loc_A5B9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72A1, 0x0))

    Jump('loc_A666')

    def _loc_A5D5(): pass

    label('loc_A5D5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72A2, 0x0))

    Jump('loc_A666')

    def _loc_A5F1(): pass

    label('loc_A5F1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72A3, 0x0))

    Jump('loc_A666')

    def _loc_A60D(): pass

    label('loc_A60D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72A4, 0x0))

    Jump('loc_A666')

    def _loc_A629(): pass

    label('loc_A629')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72A5, 0x0))

    Jump('loc_A666')

    def _loc_A645(): pass

    label('loc_A645')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72A6, 0x0))

    Jump('loc_A666')

    def _loc_A661(): pass

    label('loc_A661')

    Jump('loc_A666')

    def _loc_A666(): pass

    label('loc_A666')

    Jump('loc_A2A1')

    def _loc_A66B(): pass

    label('loc_A66B')

    Return()

# id: 0x0044 offset: 0xA66C
@scena.Code('EV_Jump_QS_241')
def EV_Jump_QS_241():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A675(): pass

    label('loc_A675')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AC7F',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS241_00]  [峡谷へ向かう・選択肢　　　　　]', 0x000072C0)
    MenuCmd(0x01, 0x02, '[QS241_01]  [セレスタンから依頼を聞く　　　]', 0x000072C1)
    MenuCmd(0x01, 0x02, '[QS241_02]  [作戦を開始する・選択肢　　　　]', 0x000072C2)
    MenuCmd(0x01, 0x02, '[QS241_03_A][西ラングドック峡谷道に到着Ａ　]', 0x000072C3)
    MenuCmd(0x01, 0x02, '[QS241_03_B][西ラングドック峡谷道に到着Ｂ　]', 0x000072C4)
    MenuCmd(0x01, 0x02, '[QS241_04]  [ロック＝パティオ前での戦闘　　]', 0x000072C5)
    MenuCmd(0x01, 0x02, '[QS241_04B] [ロック＝パティオ前での戦闘後　]', 0x000072C6)
    MenuCmd(0x01, 0x02, '[QS241_05]  [北の猟兵たちとの戦闘　　　　　]', 0x000072C7)
    MenuCmd(0x01, 0x02, '[QS241_05B] [北の猟兵たちとの戦闘後　　　　]', 0x000072C8)
    MenuCmd(0x01, 0x02, '[QS241_06]  [飛行船前での戦闘　　　　　　　]', 0x000072C9)
    MenuCmd(0x01, 0x02, '[QS241_06B] [救出作戦の完了　　　　　　　　]', 0x000072CA)
    MenuCmd(0x01, 0x02, '[QS241_07]  [解決イベント　　　　　　　　　]', 0x000072CB)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA07',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    def _loc_AA07(): pass

    label('loc_AA07')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA28',
    )

    QuestCtrl(0x0016, 0x04, 0x01, 0x02)
    QuestCtrl(0x0016, 0x04, 0x02, 0x02)
    QuestCtrl(0x0016, 0x04, 0x08, 0x02)

    def _loc_AA28(): pass

    label('loc_AA28')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000072CB, 'loc_AA91'),
        (0x000072CA, 'loc_AA94'),
        (0x000072C9, 'loc_AA97'),
        (0x000072C8, 'loc_AA9A'),
        (0x000072C7, 'loc_AA9D'),
        (0x000072C6, 'loc_AAA0'),
        (0x000072C5, 'loc_AAA3'),
        (0x000072C4, 'loc_AAA9'),
        (0x000072C3, 'loc_AAA9'),
        (0x000072C2, 'loc_AAAC'),
        (0x000072C1, 'loc_AAB2'),
        (0x000072C0, 'loc_AAB5'),
        (-1, 'loc_AAC0'),
    )

    def _loc_AA91(): pass

    label('loc_AA91')

    SetScenaFlags(ScenaFlag(0x0755, 5, 0x3AAD))

    def _loc_AA94(): pass

    label('loc_AA94')

    SetScenaFlags(ScenaFlag(0x0755, 4, 0x3AAC))

    def _loc_AA97(): pass

    label('loc_AA97')

    SetScenaFlags(ScenaFlag(0x0755, 3, 0x3AAB))

    def _loc_AA9A(): pass

    label('loc_AA9A')

    SetScenaFlags(ScenaFlag(0x0755, 2, 0x3AAA))

    def _loc_AA9D(): pass

    label('loc_AA9D')

    SetScenaFlags(ScenaFlag(0x0755, 1, 0x3AA9))

    def _loc_AAA0(): pass

    label('loc_AAA0')

    SetScenaFlags(ScenaFlag(0x0755, 0, 0x3AA8))

    def _loc_AAA3(): pass

    label('loc_AAA3')

    SetScenaFlags(ScenaFlag(0x0754, 7, 0x3AA7))
    SetScenaFlags(ScenaFlag(0x0754, 6, 0x3AA6))

    def _loc_AAA9(): pass

    label('loc_AAA9')

    SetScenaFlags(ScenaFlag(0x0754, 5, 0x3AA5))

    def _loc_AAAC(): pass

    label('loc_AAAC')

    SetScenaFlags(ScenaFlag(0x0754, 4, 0x3AA4))
    SetScenaFlags(ScenaFlag(0x049C, 1, 0x24E1))

    def _loc_AAB2(): pass

    label('loc_AAB2')

    SetScenaFlags(ScenaFlag(0x0754, 3, 0x3AA3))

    def _loc_AAB5(): pass

    label('loc_AAB5')

    QuestCtrl(0x0017, 0x03, 0x01, 0x02)

    Jump('loc_AAC0')

    def _loc_AAC0(): pass

    label('loc_AAC0')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000072C0, 'loc_AB29'),
        (0x000072C1, 'loc_AB45'),
        (0x000072C2, 'loc_AB61'),
        (0x000072C3, 'loc_AB79'),
        (0x000072C4, 'loc_AB95'),
        (0x000072C5, 'loc_ABB1'),
        (0x000072C6, 'loc_ABCD'),
        (0x000072C7, 'loc_ABE9'),
        (0x000072C8, 'loc_AC05'),
        (0x000072C9, 'loc_AC21'),
        (0x000072CA, 'loc_AC3D'),
        (0x000072CB, 'loc_AC59'),
        (-1, 'loc_AC75'),
    )

    def _loc_AB29(): pass

    label('loc_AB29')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C0, 0x0))

    Jump('loc_AC7A')

    def _loc_AB45(): pass

    label('loc_AB45')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C1, 0x0))

    Jump('loc_AC7A')

    def _loc_AB61(): pass

    label('loc_AB61')

    OP_28((0xDD, 't4000'), (0xDD, 'go_r3400'), 0x00)

    Jump('loc_AC7A')

    def _loc_AB79(): pass

    label('loc_AB79')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C3, 0x0))

    Jump('loc_AC7A')

    def _loc_AB95(): pass

    label('loc_AB95')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C4, 0x0))

    Jump('loc_AC7A')

    def _loc_ABB1(): pass

    label('loc_ABB1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C5, 0x0))

    Jump('loc_AC7A')

    def _loc_ABCD(): pass

    label('loc_ABCD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C6, 0x0))

    Jump('loc_AC7A')

    def _loc_ABE9(): pass

    label('loc_ABE9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C7, 0x0))

    Jump('loc_AC7A')

    def _loc_AC05(): pass

    label('loc_AC05')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C8, 0x0))

    Jump('loc_AC7A')

    def _loc_AC21(): pass

    label('loc_AC21')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72C9, 0x0))

    Jump('loc_AC7A')

    def _loc_AC3D(): pass

    label('loc_AC3D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72CA, 0x0))

    Jump('loc_AC7A')

    def _loc_AC59(): pass

    label('loc_AC59')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x72CB, 0x0))

    Jump('loc_AC7A')

    def _loc_AC75(): pass

    label('loc_AC75')

    Jump('loc_AC7A')

    def _loc_AC7A(): pass

    label('loc_AC7A')

    Jump('loc_A675')

    def _loc_AC7F(): pass

    label('loc_AC7F')

    Return()

# id: 0x0045 offset: 0xAC80
@scena.Code('EV_Jump_QS_242')
def EV_Jump_QS_242():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_AC89(): pass

    label('loc_AC89')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD8B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS242_01][手配魔獣を撃破　　　　　　　　]', 0x000072E0)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD35',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_AD35(): pass

    label('loc_AD35')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD50',
    )

    QuestCtrl(0x0018, 0x03, 0x01, 0x02)
    QuestCtrl(0x0018, 0x04, 0x02, 0x02)

    def _loc_AD50(): pass

    label('loc_AD50')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000072E0, 'loc_AD61'),
        (-1, 'loc_AD81'),
    )

    def _loc_AD61(): pass

    label('loc_AD61')

    FormationCtrl(0x1C, 0x01)
    OP_28((0xDD, 'r7000'), (0xDD, 'QS242_01_JUMP'), 0x00)

    Jump('loc_AD86')

    def _loc_AD81(): pass

    label('loc_AD81')

    Jump('loc_AD86')

    def _loc_AD86(): pass

    label('loc_AD86')

    Jump('loc_AC89')

    def _loc_AD8B(): pass

    label('loc_AD8B')

    Return()

# id: 0x0046 offset: 0xAD8C
@scena.Code('EV_Jump_QS_250')
def EV_Jump_QS_250():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_AD95(): pass

    label('loc_AD95')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B0EE',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS250_01] [クインズ卿と話をする・選択肢　]', 0x00007300)
    MenuCmd(0x01, 0x02, '[QS250_01B][クインズ卿と話をする　　　　　]', 0x00007301)
    MenuCmd(0x01, 0x02, '[QS250_01C][家族の捜索を開始する　　　　　]', 0x00007302)
    MenuCmd(0x01, 0x02, '[QS250_02A][ヘレナを見つける　　　　　　　]', 0x00007303)
    MenuCmd(0x01, 0x02, '[QS250_02B][ルナ・エクレアを見つける　　　]', 0x00007304)
    MenuCmd(0x01, 0x02, '[QS250_03] [クエスト達成　　　　　　　　　]', 0x00007305)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF8F',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    def _loc_AF8F(): pass

    label('loc_AF8F')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AFB0',
    )

    QuestCtrl(0x0019, 0x04, 0x01, 0x02)
    QuestCtrl(0x0019, 0x04, 0x02, 0x02)
    QuestCtrl(0x0019, 0x04, 0x08, 0x02)

    def _loc_AFB0(): pass

    label('loc_AFB0')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007305, 'loc_AFE9'),
        (0x00007304, 'loc_AFEC'),
        (0x00007303, 'loc_AFEF'),
        (0x00007302, 'loc_AFF2'),
        (0x00007301, 'loc_AFF5'),
        (0x00007300, 'loc_AFF8'),
        (-1, 'loc_B003'),
    )

    def _loc_AFE9(): pass

    label('loc_AFE9')

    SetScenaFlags(ScenaFlag(0x075B, 2, 0x3ADA))

    def _loc_AFEC(): pass

    label('loc_AFEC')

    SetScenaFlags(ScenaFlag(0x075B, 1, 0x3AD9))

    def _loc_AFEF(): pass

    label('loc_AFEF')

    SetScenaFlags(ScenaFlag(0x0759, 1, 0x3AC9))

    def _loc_AFF2(): pass

    label('loc_AFF2')

    SetScenaFlags(ScenaFlag(0x0759, 0, 0x3AC8))

    def _loc_AFF5(): pass

    label('loc_AFF5')

    SetScenaFlags(ScenaFlag(0x0758, 7, 0x3AC7))

    def _loc_AFF8(): pass

    label('loc_AFF8')

    QuestCtrl(0x0019, 0x03, 0x01, 0x02)

    Jump('loc_B003')

    def _loc_B003(): pass

    label('loc_B003')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007300, 'loc_B03C'),
        (0x00007301, 'loc_B058'),
        (0x00007302, 'loc_B074'),
        (0x00007303, 'loc_B090'),
        (0x00007304, 'loc_B0AC'),
        (0x00007305, 'loc_B0C8'),
        (-1, 'loc_B0E4'),
    )

    def _loc_B03C(): pass

    label('loc_B03C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7300, 0x0))

    Jump('loc_B0E9')

    def _loc_B058(): pass

    label('loc_B058')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7301, 0x0))

    Jump('loc_B0E9')

    def _loc_B074(): pass

    label('loc_B074')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7302, 0x0))

    Jump('loc_B0E9')

    def _loc_B090(): pass

    label('loc_B090')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7303, 0x0))

    Jump('loc_B0E9')

    def _loc_B0AC(): pass

    label('loc_B0AC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7304, 0x0))

    Jump('loc_B0E9')

    def _loc_B0C8(): pass

    label('loc_B0C8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7305, 0x0))

    Jump('loc_B0E9')

    def _loc_B0E4(): pass

    label('loc_B0E4')

    Jump('loc_B0E9')

    def _loc_B0E9(): pass

    label('loc_B0E9')

    Jump('loc_AD95')

    def _loc_B0EE(): pass

    label('loc_B0EE')

    Return()

# id: 0x0047 offset: 0xB0F0
@scena.Code('EV_Jump_QS_251')
def EV_Jump_QS_251():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B0F9(): pass

    label('loc_B0F9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B62D',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS251_01]   [魔女ダリエから話を聞く　　　　]', 0x00007320)
    MenuCmd(0x01, 0x02, '[QS251_02A]  [盆地の温泉に杭を打ち込む　　　]', 0x00007321)
    MenuCmd(0x01, 0x02, '[QS251_02B]  [間道①で温泉に杭を打ち込む　　]', 0x00007322)
    MenuCmd(0x01, 0x02, '[QS251_02C_A][島の洞窟の温泉に杭を打ち込むＡ]', 0x00007323)
    MenuCmd(0x01, 0x02, '[QS251_02C_B][島の洞窟の温泉に杭を打ち込むＢ]', 0x00007324)
    MenuCmd(0x01, 0x02, '[QS251_03]   [魔女ダリエに報告する　　　　　]', 0x00007325)
    MenuCmd(0x01, 0x02, '[QS251_03B]  [オスギリアス盆地の温泉が浄化　]', 0x00007326)
    MenuCmd(0x01, 0x02, '[QS251_03C]  [ミルサンテ間道①の温泉が浄化　]', 0x00007327)
    MenuCmd(0x01, 0x02, '[QS251_03D]  [ブリオニア島の温泉が浄化　　　]', 0x00007328)
    MenuCmd(0x01, 0x02, '[QS251_03E]  [エリンの里の温泉が浄化　　　　]', 0x00007329)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B40C',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_B40C(): pass

    label('loc_B40C')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B42D',
    )

    QuestCtrl(0x001A, 0x04, 0x01, 0x02)
    QuestCtrl(0x001A, 0x04, 0x02, 0x02)
    QuestCtrl(0x001A, 0x04, 0x08, 0x02)

    def _loc_B42D(): pass

    label('loc_B42D')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007329, 'loc_B486'),
        (0x00007328, 'loc_B489'),
        (0x00007327, 'loc_B48C'),
        (0x00007326, 'loc_B48F'),
        (0x00007325, 'loc_B492'),
        (0x00007324, 'loc_B495'),
        (0x00007323, 'loc_B498'),
        (0x00007322, 'loc_B49B'),
        (0x00007321, 'loc_B49E'),
        (0x00007320, 'loc_B4A4'),
        (-1, 'loc_B4B2'),
    )

    def _loc_B486(): pass

    label('loc_B486')

    SetScenaFlags(ScenaFlag(0x0752, 2, 0x3A92))

    def _loc_B489(): pass

    label('loc_B489')

    SetScenaFlags(ScenaFlag(0x0752, 1, 0x3A91))

    def _loc_B48C(): pass

    label('loc_B48C')

    SetScenaFlags(ScenaFlag(0x0752, 0, 0x3A90))

    def _loc_B48F(): pass

    label('loc_B48F')

    SetScenaFlags(ScenaFlag(0x0751, 7, 0x3A8F))

    def _loc_B492(): pass

    label('loc_B492')

    SetScenaFlags(ScenaFlag(0x0751, 6, 0x3A8E))

    def _loc_B495(): pass

    label('loc_B495')

    SetScenaFlags(ScenaFlag(0x0751, 5, 0x3A8D))

    def _loc_B498(): pass

    label('loc_B498')

    SetScenaFlags(ScenaFlag(0x0751, 4, 0x3A8C))

    def _loc_B49B(): pass

    label('loc_B49B')

    SetScenaFlags(ScenaFlag(0x0751, 3, 0x3A8B))

    def _loc_B49E(): pass

    label('loc_B49E')

    SetScenaFlags(ScenaFlag(0x0760, 0, 0x3B00))
    SetScenaFlags(ScenaFlag(0x0751, 2, 0x3A8A))

    def _loc_B4A4(): pass

    label('loc_B4A4')

    QuestCtrl(0x001A, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    Jump('loc_B4B2')

    def _loc_B4B2(): pass

    label('loc_B4B2')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007320, 'loc_B50B'),
        (0x00007321, 'loc_B527'),
        (0x00007322, 'loc_B543'),
        (0x00007323, 'loc_B55F'),
        (0x00007324, 'loc_B57B'),
        (0x00007325, 'loc_B597'),
        (0x00007326, 'loc_B5B3'),
        (0x00007327, 'loc_B5CF'),
        (0x00007328, 'loc_B5EB'),
        (0x00007329, 'loc_B607'),
        (-1, 'loc_B623'),
    )

    def _loc_B50B(): pass

    label('loc_B50B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7320, 0x0))

    Jump('loc_B628')

    def _loc_B527(): pass

    label('loc_B527')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7321, 0x0))

    Jump('loc_B628')

    def _loc_B543(): pass

    label('loc_B543')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7322, 0x0))

    Jump('loc_B628')

    def _loc_B55F(): pass

    label('loc_B55F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7323, 0x0))

    Jump('loc_B628')

    def _loc_B57B(): pass

    label('loc_B57B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7324, 0x0))

    Jump('loc_B628')

    def _loc_B597(): pass

    label('loc_B597')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7325, 0x0))

    Jump('loc_B628')

    def _loc_B5B3(): pass

    label('loc_B5B3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7326, 0x0))

    Jump('loc_B628')

    def _loc_B5CF(): pass

    label('loc_B5CF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7327, 0x0))

    Jump('loc_B628')

    def _loc_B5EB(): pass

    label('loc_B5EB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7328, 0x0))

    Jump('loc_B628')

    def _loc_B607(): pass

    label('loc_B607')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7329, 0x0))

    Jump('loc_B628')

    def _loc_B623(): pass

    label('loc_B623')

    Jump('loc_B628')

    def _loc_B628(): pass

    label('loc_B628')

    Jump('loc_B0F9')

    def _loc_B62D(): pass

    label('loc_B62D')

    Return()

# id: 0x0048 offset: 0xB630
@scena.Code('EV_Jump_QS_252')
def EV_Jump_QS_252():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B639(): pass

    label('loc_B639')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B73B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS252_01][手配魔獣を撃破　　　　　　　　]', 0x00007340)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6E5',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_B6E5(): pass

    label('loc_B6E5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B700',
    )

    QuestCtrl(0x001B, 0x03, 0x01, 0x02)
    QuestCtrl(0x001B, 0x04, 0x02, 0x02)

    def _loc_B700(): pass

    label('loc_B700')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007340, 'loc_B711'),
        (-1, 'loc_B731'),
    )

    def _loc_B711(): pass

    label('loc_B711')

    FormationCtrl(0x1C, 0x01)
    OP_28((0xDD, 'r6000'), (0xDD, 'QS252_01_JUMP'), 0x00)

    Jump('loc_B736')

    def _loc_B731(): pass

    label('loc_B731')

    Jump('loc_B736')

    def _loc_B736(): pass

    label('loc_B736')

    Jump('loc_B639')

    def _loc_B73B(): pass

    label('loc_B73B')

    Return()

# id: 0x0049 offset: 0xB73C
@scena.Code('EV_Jump_QS_320')
def EV_Jump_QS_320():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B745(): pass

    label('loc_B745')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD2E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS320_01]  [カエラ＆ハンフリーから話を聞く]　', 0x00007360)
    MenuCmd(0x01, 0x02, '[QS320_02]  [エイボン丘陵に降り立つ　　　　]　', 0x00007361)
    MenuCmd(0x01, 0x02, '[QS320_02ST][ＳＴ：引き返すのを止められる　]　', 0x00007362)
    MenuCmd(0x01, 0x02, '[QS320_03]  [ハーキュリーズ隊員と交戦　　　]戦', 0x00007363)
    MenuCmd(0x01, 0x02, '[QS320_03B] [ハーキュリーズ隊員との戦闘後　]　', 0x00007364)
    MenuCmd(0x01, 0x02, '[QS320_03LP][無力化した共和国隊員の共通ＬＰ]　', 0x00007365)
    MenuCmd(0x01, 0x02, '[QS320_04]  [隊長と交戦　　　　　　　　　　]戦', 0x00007366)
    MenuCmd(0x01, 0x02, '[QS320_04B] [クエスト達成　　　　　　　　　]　', 0x00007367)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BC74',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007367, 'loc_BA13'),
        (0x00007366, 'loc_BA13'),
        (0x00007365, 'loc_BA13'),
        (0x00007364, 'loc_BA13'),
        (0x00007363, 'loc_BA13'),
        (0x00007362, 'loc_BA13'),
        (0x00007361, 'loc_BA13'),
        (0x00007360, 'loc_BC56'),
        (-1, 'loc_BC74'),
    )

    def _loc_BA13(): pass

    label('loc_BA13')

    OP_23(0x05, 0xFFFF, 0x00A0, 0xFFFF, 0xFFFF, 0x00)

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, 'エマを連れて行く', 0x00000001)
    OP_75(0x01, 0x00, 'ガイウスを連れて行く', 0x00000002)
    OP_75(0x02, 0x00, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF9)
    OP_75(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB5C',
    )

    SetScenaFlags(ScenaFlag(0x08A2, 2, 0x4512))
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0005)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x02, 0x0004)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x03, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2E,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)

    Jump('loc_BC0B')

    def _loc_BB5C(): pass

    label('loc_BB5C')

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0008)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x02, 0x0004)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x03, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2E,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)

    def _loc_BC0B(): pass

    label('loc_BC0B')

    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x08A2, 2, 0x4512)),
            Expr.Return,
        ),
        'loc_BC49',
    )

    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000010)

    Jump('loc_BC51')

    def _loc_BC49(): pass

    label('loc_BC49')

    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000010)

    def _loc_BC51(): pass

    label('loc_BC51')

    Jump('loc_BC74')

    def _loc_BC56(): pass

    label('loc_BC56')

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    Jump('loc_BC74')

    def _loc_BC74(): pass

    label('loc_BC74')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BC95',
    )

    QuestCtrl(0x001C, 0x04, 0x01, 0x02)
    QuestCtrl(0x001C, 0x04, 0x02, 0x02)
    QuestCtrl(0x001C, 0x04, 0x08, 0x02)

    def _loc_BC95(): pass

    label('loc_BC95')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007367, 'loc_BCDE'),
        (0x00007366, 'loc_BCE1'),
        (0x00007365, 'loc_BCE4'),
        (0x00007364, 'loc_BCE7'),
        (0x00007363, 'loc_BCEA'),
        (0x00007362, 'loc_BCED'),
        (0x00007361, 'loc_BCF0'),
        (0x00007360, 'loc_BCF3'),
        (-1, 'loc_BCFE'),
    )

    def _loc_BCDE(): pass

    label('loc_BCDE')

    SetScenaFlags(ScenaFlag(0x088C, 6, 0x4466))

    def _loc_BCE1(): pass

    label('loc_BCE1')

    SetScenaFlags(ScenaFlag(0x088C, 5, 0x4465))

    def _loc_BCE4(): pass

    label('loc_BCE4')

    SetScenaFlags(ScenaFlag(0x088C, 4, 0x4464))

    def _loc_BCE7(): pass

    label('loc_BCE7')

    SetScenaFlags(ScenaFlag(0x088C, 3, 0x4463))

    def _loc_BCEA(): pass

    label('loc_BCEA')

    SetScenaFlags(ScenaFlag(0x088C, 2, 0x4462))

    def _loc_BCED(): pass

    label('loc_BCED')

    SetScenaFlags(ScenaFlag(0x088C, 1, 0x4461))

    def _loc_BCF0(): pass

    label('loc_BCF0')

    SetScenaFlags(ScenaFlag(0x088C, 0, 0x4460))

    def _loc_BCF3(): pass

    label('loc_BCF3')

    QuestCtrl(0x001C, 0x03, 0x01, 0x02)

    Jump('loc_BCFE')

    def _loc_BCFE(): pass

    label('loc_BCFE')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD29',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_BD29(): pass

    label('loc_BD29')

    Jump('loc_B745')

    def _loc_BD2E(): pass

    label('loc_BD2E')

    Return()

# id: 0x004A offset: 0xBD30
@scena.Code('EV_Jump_QS_321')
def EV_Jump_QS_321():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BD39(): pass

    label('loc_BD39')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C0AD',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS321_01] [ムンクから話を聞く　　　　　　]', 0x00007380)
    MenuCmd(0x01, 0x02, '[QS321_02A][エーデルに相談する　　　　　　]', 0x00007381)
    MenuCmd(0x01, 0x02, '[QS321_02B][ヴィヴィに相談する　　　　　　]', 0x00007382)
    MenuCmd(0x01, 0x02, '[QS321_02C][ドロテに相談する　　　　　　　]', 0x00007383)
    MenuCmd(0x01, 0x02, '[QS321_02D][ベリルに相談する　　　　　　　]', 0x00007384)
    MenuCmd(0x01, 0x02, '[QS321_03] [ラジオドラマの収録　　　　　　]', 0x00007385)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF30',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_BF30(): pass

    label('loc_BF30')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF51',
    )

    QuestCtrl(0x001D, 0x04, 0x01, 0x02)
    QuestCtrl(0x001D, 0x04, 0x02, 0x02)
    QuestCtrl(0x001D, 0x04, 0x08, 0x02)

    def _loc_BF51(): pass

    label('loc_BF51')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007385, 'loc_BF8A'),
        (0x00007384, 'loc_BF8D'),
        (0x00007383, 'loc_BF90'),
        (0x00007382, 'loc_BF93'),
        (0x00007381, 'loc_BF96'),
        (0x00007380, 'loc_BF9C'),
        (-1, 'loc_BFC2'),
    )

    def _loc_BF8A(): pass

    label('loc_BF8A')

    SetScenaFlags(ScenaFlag(0x0880, 4, 0x4404))

    def _loc_BF8D(): pass

    label('loc_BF8D')

    SetScenaFlags(ScenaFlag(0x0880, 3, 0x4403))

    def _loc_BF90(): pass

    label('loc_BF90')

    SetScenaFlags(ScenaFlag(0x0880, 2, 0x4402))

    def _loc_BF93(): pass

    label('loc_BF93')

    SetScenaFlags(ScenaFlag(0x0880, 1, 0x4401))

    def _loc_BF96(): pass

    label('loc_BF96')

    SetScenaFlags(ScenaFlag(0x08A0, 0, 0x4500))
    SetScenaFlags(ScenaFlag(0x0880, 0, 0x4400))

    def _loc_BF9C(): pass

    label('loc_BF9C')

    QuestCtrl(0x001D, 0x03, 0x01, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x7382),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BFBD',
    )

    FormationCtrl(0x1C, 0x01)

    def _loc_BFBD(): pass

    label('loc_BFBD')

    Jump('loc_BFC2')

    def _loc_BFC2(): pass

    label('loc_BFC2')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007380, 'loc_BFFB'),
        (0x00007381, 'loc_C017'),
        (0x00007382, 'loc_C033'),
        (0x00007383, 'loc_C04F'),
        (0x00007384, 'loc_C06B'),
        (0x00007385, 'loc_C087'),
        (-1, 'loc_C0A3'),
    )

    def _loc_BFFB(): pass

    label('loc_BFFB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7380, 0x0))

    Jump('loc_C0A8')

    def _loc_C017(): pass

    label('loc_C017')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7381, 0x0))

    Jump('loc_C0A8')

    def _loc_C033(): pass

    label('loc_C033')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7382, 0x0))

    Jump('loc_C0A8')

    def _loc_C04F(): pass

    label('loc_C04F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7383, 0x0))

    Jump('loc_C0A8')

    def _loc_C06B(): pass

    label('loc_C06B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7384, 0x0))

    Jump('loc_C0A8')

    def _loc_C087(): pass

    label('loc_C087')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7385, 0x0))

    Jump('loc_C0A8')

    def _loc_C0A3(): pass

    label('loc_C0A3')

    Jump('loc_C0A8')

    def _loc_C0A8(): pass

    label('loc_C0A8')

    Jump('loc_BD39')

    def _loc_C0AD(): pass

    label('loc_C0AD')

    Return()

# id: 0x004B offset: 0xC0B0
@scena.Code('EV_Jump_QS_322')
def EV_Jump_QS_322():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C0B9(): pass

    label('loc_C0B9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C1BB',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS322_01][手配魔獣を撃破　　　　　　　　]', 0x000073A0)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C165',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_C165(): pass

    label('loc_C165')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C180',
    )

    QuestCtrl(0x001E, 0x03, 0x01, 0x02)
    QuestCtrl(0x001E, 0x04, 0x02, 0x02)

    def _loc_C180(): pass

    label('loc_C180')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000073A0, 'loc_C191'),
        (-1, 'loc_C1B1'),
    )

    def _loc_C191(): pass

    label('loc_C191')

    FormationCtrl(0x1C, 0x01)
    OP_28((0xDD, 'r5200'), (0xDD, 'QS322_01_JUMP'), 0x00)

    Jump('loc_C1B6')

    def _loc_C1B1(): pass

    label('loc_C1B1')

    Jump('loc_C1B6')

    def _loc_C1B6(): pass

    label('loc_C1B6')

    Jump('loc_C0B9')

    def _loc_C1BB(): pass

    label('loc_C1BB')

    Return()

# id: 0x004C offset: 0xC1BC
@scena.Code('EV_Jump_QS_323')
def EV_Jump_QS_323():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C1C5(): pass

    label('loc_C1C5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C43F',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS323_01] [休憩ロッジでトマス達と遭遇する]', 0x000073C0)
    MenuCmd(0x01, 0x02, '[QS323_02] [取材イベント　　　　　　　　　]', 0x000073C1)
    MenuCmd(0x01, 0x02, '[QS323_02B][運搬車でニールセン達が去る　　]', 0x000073C2)
    MenuCmd(0x01, 0x02, '[QS323_02C][トマスたちを見送る　　　　　　]', 0x000073C3)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C338',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_C338(): pass

    label('loc_C338')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C359',
    )

    QuestCtrl(0x001F, 0x04, 0x01, 0x02)
    QuestCtrl(0x001F, 0x04, 0x02, 0x02)
    QuestCtrl(0x001F, 0x04, 0x08, 0x02)

    def _loc_C359(): pass

    label('loc_C359')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000073C3, 'loc_C382'),
        (0x000073C2, 'loc_C385'),
        (0x000073C1, 'loc_C388'),
        (0x000073C0, 'loc_C38E'),
        (-1, 'loc_C39C'),
    )

    def _loc_C382(): pass

    label('loc_C382')

    SetScenaFlags(ScenaFlag(0x0881, 1, 0x4409))

    def _loc_C385(): pass

    label('loc_C385')

    SetScenaFlags(ScenaFlag(0x0881, 0, 0x4408))

    def _loc_C388(): pass

    label('loc_C388')

    SetScenaFlags(ScenaFlag(0x08A0, 1, 0x4501))
    SetScenaFlags(ScenaFlag(0x0880, 7, 0x4407))

    def _loc_C38E(): pass

    label('loc_C38E')

    QuestCtrl(0x001F, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    Jump('loc_C39C')

    def _loc_C39C(): pass

    label('loc_C39C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000073C0, 'loc_C3C5'),
        (0x000073C1, 'loc_C3E1'),
        (0x000073C2, 'loc_C3FD'),
        (0x000073C3, 'loc_C419'),
        (-1, 'loc_C435'),
    )

    def _loc_C3C5(): pass

    label('loc_C3C5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73C0, 0x0))

    Jump('loc_C43A')

    def _loc_C3E1(): pass

    label('loc_C3E1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73C1, 0x0))

    Jump('loc_C43A')

    def _loc_C3FD(): pass

    label('loc_C3FD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73C2, 0x0))

    Jump('loc_C43A')

    def _loc_C419(): pass

    label('loc_C419')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73C3, 0x0))

    Jump('loc_C43A')

    def _loc_C435(): pass

    label('loc_C435')

    Jump('loc_C43A')

    def _loc_C43A(): pass

    label('loc_C43A')

    Jump('loc_C1C5')

    def _loc_C43F(): pass

    label('loc_C43F')

    Return()

# id: 0x004D offset: 0xC440
@scena.Code('EV_Jump_QS_324')
def EV_Jump_QS_324():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C449(): pass

    label('loc_C449')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CCC5',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS324_01]     [ヴァレリーから依頼の話を聞く　]', 0x000073E0)
    MenuCmd(0x01, 0x02, '[QS324_02A1]   [Ａ：ルイゼと合流する　　　　　]', 0x000073E1)
    MenuCmd(0x01, 0x02, '[QS324_02A2]   [Ａ：魔獣とエンカウント　　　　]', 0x000073E2)
    MenuCmd(0x01, 0x02, '[QS324_02A2B]  [Ａ：魔獣戦後　　　　　　　　　]', 0x000073E3)
    MenuCmd(0x01, 0x02, '[QS324_02A3]   [Ａ：原因の人形兵器と遭遇　　　]', 0x000073E4)
    MenuCmd(0x01, 0x02, '[QS324_02A3B]  [Ａ：ファランクス戦後　　　　　]', 0x000073E5)
    MenuCmd(0x01, 0x02, '[QS324_02AST_A][ＳＴ：オルディス方面ストッパー]', 0x000073E6)
    MenuCmd(0x01, 0x02, '[QS324_02AST_B][ＳＴ：砂浜方面のストッパー　　]', 0x000073E7)
    MenuCmd(0x01, 0x02, '[QS324_02AST_C][ＳＴ：海岸道②方面のストッパー]', 0x000073E8)
    MenuCmd(0x01, 0x02, '[QS324_02B1]   [Ｂ：タチアナと合流する　　　　]', 0x000073E9)
    MenuCmd(0x01, 0x02, '[QS324_02B2]   [Ｂ：魔獣とエンカウント　　　　]', 0x000073EA)
    MenuCmd(0x01, 0x02, '[QS324_02B2B]  [Ｂ：魔獣戦後　　　　　　　　　]', 0x000073EB)
    MenuCmd(0x01, 0x02, '[QS324_02B3]   [Ｂ：原因の人形兵器と遭遇　　　]', 0x000073EC)
    MenuCmd(0x01, 0x02, '[QS324_02B3B]  [Ｂ：ゼフィランサス戦後　　　　]', 0x000073ED)
    MenuCmd(0x01, 0x02, '[QS324_02BST_A][ＳＴ：西側のストッパー　　　　]', 0x000073EE)
    MenuCmd(0x01, 0x02, '[QS324_02BST_B][ＳＴ：三叉路東のストッパー　　]', 0x000073EF)
    MenuCmd(0x01, 0x02, '[QS324_03]     [達成イベント　　　　　　　　　]', 0x000073F0)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C95A',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_C95A(): pass

    label('loc_C95A')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C97B',
    )

    QuestCtrl(0x0020, 0x04, 0x01, 0x02)
    QuestCtrl(0x0020, 0x04, 0x02, 0x02)
    QuestCtrl(0x0020, 0x04, 0x08, 0x02)

    def _loc_C97B(): pass

    label('loc_C97B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000073ED, 'loc_C9FC'),
        (0x000073EC, 'loc_C9FF'),
        (0x000073EB, 'loc_CA02'),
        (0x000073EA, 'loc_CA05'),
        (0x000073EE, 'loc_CA05'),
        (0x000073EF, 'loc_CA05'),
        (0x000073E9, 'loc_CA08'),
        (0x000073E5, 'loc_CA1C'),
        (0x000073E4, 'loc_CA1F'),
        (0x000073E3, 'loc_CA22'),
        (0x000073E2, 'loc_CA25'),
        (0x000073E8, 'loc_CA25'),
        (0x000073E7, 'loc_CA25'),
        (0x000073E6, 'loc_CA25'),
        (0x000073E1, 'loc_CA28'),
        (-1, 'loc_CA3C'),
    )

    def _loc_C9FC(): pass

    label('loc_C9FC')

    SetScenaFlags(ScenaFlag(0x0882, 7, 0x4417))

    def _loc_C9FF(): pass

    label('loc_C9FF')

    SetScenaFlags(ScenaFlag(0x0882, 6, 0x4416))

    def _loc_CA02(): pass

    label('loc_CA02')

    SetScenaFlags(ScenaFlag(0x0882, 5, 0x4415))

    def _loc_CA05(): pass

    label('loc_CA05')

    SetScenaFlags(ScenaFlag(0x0882, 4, 0x4414))

    def _loc_CA08(): pass

    label('loc_CA08')

    SetScenaFlags(ScenaFlag(0x0881, 3, 0x440B))
    SetScenaFlags(ScenaFlag(0x08A0, 2, 0x4502))
    QuestCtrl(0x0020, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    Jump('loc_CA3C')

    def _loc_CA1C(): pass

    label('loc_CA1C')

    SetScenaFlags(ScenaFlag(0x0881, 7, 0x440F))

    def _loc_CA1F(): pass

    label('loc_CA1F')

    SetScenaFlags(ScenaFlag(0x0881, 6, 0x440E))

    def _loc_CA22(): pass

    label('loc_CA22')

    SetScenaFlags(ScenaFlag(0x0881, 5, 0x440D))

    def _loc_CA25(): pass

    label('loc_CA25')

    SetScenaFlags(ScenaFlag(0x0881, 4, 0x440C))

    def _loc_CA28(): pass

    label('loc_CA28')

    SetScenaFlags(ScenaFlag(0x0881, 3, 0x440B))
    SetScenaFlags(ScenaFlag(0x08A0, 2, 0x4502))
    QuestCtrl(0x0020, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    Jump('loc_CA3C')

    def _loc_CA3C(): pass

    label('loc_CA3C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000073E0, 'loc_CACD'),
        (0x000073E1, 'loc_CAE9'),
        (0x000073E2, 'loc_CB05'),
        (0x000073E3, 'loc_CB21'),
        (0x000073E4, 'loc_CB3D'),
        (0x000073E5, 'loc_CB59'),
        (0x000073E6, 'loc_CB75'),
        (0x000073E7, 'loc_CB91'),
        (0x000073E8, 'loc_CBAD'),
        (0x000073E9, 'loc_CBC9'),
        (0x000073EA, 'loc_CBE5'),
        (0x000073EB, 'loc_CC01'),
        (0x000073EC, 'loc_CC1D'),
        (0x000073ED, 'loc_CC39'),
        (0x000073EE, 'loc_CC55'),
        (0x000073EF, 'loc_CC71'),
        (0x000073F0, 'loc_CC8D'),
        (-1, 'loc_CCBB'),
    )

    def _loc_CACD(): pass

    label('loc_CACD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E0, 0x0))

    Jump('loc_CCC0')

    def _loc_CAE9(): pass

    label('loc_CAE9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E1, 0x0))

    Jump('loc_CCC0')

    def _loc_CB05(): pass

    label('loc_CB05')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E2, 0x0))

    Jump('loc_CCC0')

    def _loc_CB21(): pass

    label('loc_CB21')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E3, 0x0))

    Jump('loc_CCC0')

    def _loc_CB3D(): pass

    label('loc_CB3D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E4, 0x0))

    Jump('loc_CCC0')

    def _loc_CB59(): pass

    label('loc_CB59')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E5, 0x0))

    Jump('loc_CCC0')

    def _loc_CB75(): pass

    label('loc_CB75')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E6, 0x0))

    Jump('loc_CCC0')

    def _loc_CB91(): pass

    label('loc_CB91')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E7, 0x0))

    Jump('loc_CCC0')

    def _loc_CBAD(): pass

    label('loc_CBAD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E8, 0x0))

    Jump('loc_CCC0')

    def _loc_CBC9(): pass

    label('loc_CBC9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73E9, 0x0))

    Jump('loc_CCC0')

    def _loc_CBE5(): pass

    label('loc_CBE5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73EA, 0x0))

    Jump('loc_CCC0')

    def _loc_CC01(): pass

    label('loc_CC01')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73EB, 0x0))

    Jump('loc_CCC0')

    def _loc_CC1D(): pass

    label('loc_CC1D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73EC, 0x0))

    Jump('loc_CCC0')

    def _loc_CC39(): pass

    label('loc_CC39')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73ED, 0x0))

    Jump('loc_CCC0')

    def _loc_CC55(): pass

    label('loc_CC55')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73EE, 0x0))

    Jump('loc_CCC0')

    def _loc_CC71(): pass

    label('loc_CC71')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73EF, 0x0))

    Jump('loc_CCC0')

    def _loc_CC8D(): pass

    label('loc_CC8D')

    OP_71(0x00, 0x440B, 0x441A)
    SetScenaFlags(ScenaFlag(0x08A0, 2, 0x4502))
    QuestCtrl(0x0020, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x73F0, 0x0))

    Jump('loc_CCC0')

    def _loc_CCBB(): pass

    label('loc_CCBB')

    Jump('loc_CCC0')

    def _loc_CCC0(): pass

    label('loc_CCC0')

    Jump('loc_C449')

    def _loc_CCC5(): pass

    label('loc_CCC5')

    Return()

# id: 0x004E offset: 0xCCC8
@scena.Code('EV_Jump_QS_325')
def EV_Jump_QS_325():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CCD1(): pass

    label('loc_CCD1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CECC',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS325_01][マヤから話を聞く　　　　　　　]', 0x00007400)
    MenuCmd(0x01, 0x02, '[QS325_02][マヤとジョゼフの対決　　　　　]', 0x00007401)
    MenuCmd(0x01, 0x02, '[QS325_03][達成イベント　　　　　　　　　]', 0x00007402)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CDFF',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_CDFF(): pass

    label('loc_CDFF')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE20',
    )

    QuestCtrl(0x0021, 0x04, 0x01, 0x02)
    QuestCtrl(0x0021, 0x04, 0x02, 0x02)
    QuestCtrl(0x0021, 0x04, 0x08, 0x02)

    def _loc_CE20(): pass

    label('loc_CE20')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007402, 'loc_CE39'),
        (0x00007401, 'loc_CE3C'),
        (-1, 'loc_CE4D'),
    )

    def _loc_CE39(): pass

    label('loc_CE39')

    SetScenaFlags(ScenaFlag(0x0883, 5, 0x441D))

    def _loc_CE3C(): pass

    label('loc_CE3C')

    SetScenaFlags(ScenaFlag(0x0883, 4, 0x441C))
    SetScenaFlags(ScenaFlag(0x08A0, 3, 0x4503))
    QuestCtrl(0x0021, 0x03, 0x01, 0x02)

    Jump('loc_CE4D')

    def _loc_CE4D(): pass

    label('loc_CE4D')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007400, 'loc_CE6E'),
        (0x00007401, 'loc_CE8A'),
        (0x00007402, 'loc_CEA6'),
        (-1, 'loc_CEC2'),
    )

    def _loc_CE6E(): pass

    label('loc_CE6E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7400, 0x0))

    Jump('loc_CEC7')

    def _loc_CE8A(): pass

    label('loc_CE8A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7401, 0x0))

    Jump('loc_CEC7')

    def _loc_CEA6(): pass

    label('loc_CEA6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7402, 0x0))

    Jump('loc_CEC7')

    def _loc_CEC2(): pass

    label('loc_CEC2')

    Jump('loc_CEC7')

    def _loc_CEC7(): pass

    label('loc_CEC7')

    Jump('loc_CCD1')

    def _loc_CECC(): pass

    label('loc_CECC')

    Return()

# id: 0x004F offset: 0xCED0
@scena.Code('EV_Jump_QS_340')
def EV_Jump_QS_340():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CED9(): pass

    label('loc_CED9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D5BA',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS340_01] [カイ＆ティーリアから話を聞く　]', 0x00007420)
    MenuCmd(0x01, 0x02, '[QS340_02A][オーシュに聞き込み　　　　　　]', 0x00007421)
    MenuCmd(0x01, 0x02, '[QS340_02B][ジルダ＆ジルバンに聞き込み　　]', 0x00007422)
    MenuCmd(0x01, 0x02, '[QS340_02C][町長に聞き込み　　　　　　　　]', 0x00007423)
    MenuCmd(0x01, 0x02, '[QS340_02D][教区長に聞き込み　　　　　　　]', 0x00007424)
    MenuCmd(0x01, 0x02, '[QS340_02E][ブランに聞き込み　　　　　　　]', 0x00007425)
    MenuCmd(0x01, 0x02, '[QS340_03] [カイとティーリアの家に向かう　]', 0x00007426)
    MenuCmd(0x01, 0x02, '[QS340_04] [情報を整理する　　　　　　　　]', 0x00007427)
    MenuCmd(0x01, 0x02, '[QS340_05] [カイ達に話し掛けて作戦を始める]', 0x00007428)
    MenuCmd(0x01, 0x02, '[QS340_06] [住民が退避したアルスターの町　]', 0x00007429)
    MenuCmd(0x01, 0x02, '[QS340_07] [街道を行くアルスターの住民たち]', 0x0000742A)
    MenuCmd(0x01, 0x02, '[QS340_08] [ワッズとの対決　　　　　　　　]', 0x0000742B)
    MenuCmd(0x01, 0x02, '[QS340_08B][エステルたちとヒューゴ登場　　]', 0x0000742C)
    MenuCmd(0x01, 0x02, '[QS340_09] [解決イベント　　　　　　　　　]', 0x0000742D)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D2E3',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    def _loc_D2E3(): pass

    label('loc_D2E3')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D304',
    )

    QuestCtrl(0x0022, 0x04, 0x01, 0x02)
    QuestCtrl(0x0022, 0x04, 0x02, 0x02)
    QuestCtrl(0x0022, 0x04, 0x08, 0x02)

    def _loc_D304(): pass

    label('loc_D304')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000742D, 'loc_D37D'),
        (0x0000742C, 'loc_D380'),
        (0x0000742B, 'loc_D383'),
        (0x0000742A, 'loc_D386'),
        (0x00007429, 'loc_D389'),
        (0x00007428, 'loc_D38C'),
        (0x00007427, 'loc_D38F'),
        (0x00007426, 'loc_D392'),
        (0x00007425, 'loc_D395'),
        (0x00007424, 'loc_D398'),
        (0x00007423, 'loc_D39B'),
        (0x00007422, 'loc_D39E'),
        (0x00007421, 'loc_D3A1'),
        (0x00007420, 'loc_D3A4'),
        (-1, 'loc_D3AF'),
    )

    def _loc_D37D(): pass

    label('loc_D37D')

    SetScenaFlags(ScenaFlag(0x088B, 5, 0x445D))

    def _loc_D380(): pass

    label('loc_D380')

    SetScenaFlags(ScenaFlag(0x088B, 4, 0x445C))

    def _loc_D383(): pass

    label('loc_D383')

    SetScenaFlags(ScenaFlag(0x088B, 3, 0x445B))

    def _loc_D386(): pass

    label('loc_D386')

    SetScenaFlags(ScenaFlag(0x088B, 2, 0x445A))

    def _loc_D389(): pass

    label('loc_D389')

    SetScenaFlags(ScenaFlag(0x088B, 1, 0x4459))

    def _loc_D38C(): pass

    label('loc_D38C')

    SetScenaFlags(ScenaFlag(0x088B, 0, 0x4458))

    def _loc_D38F(): pass

    label('loc_D38F')

    SetScenaFlags(ScenaFlag(0x088A, 7, 0x4457))

    def _loc_D392(): pass

    label('loc_D392')

    SetScenaFlags(ScenaFlag(0x088A, 6, 0x4456))

    def _loc_D395(): pass

    label('loc_D395')

    SetScenaFlags(ScenaFlag(0x088A, 5, 0x4455))

    def _loc_D398(): pass

    label('loc_D398')

    SetScenaFlags(ScenaFlag(0x088A, 4, 0x4454))

    def _loc_D39B(): pass

    label('loc_D39B')

    SetScenaFlags(ScenaFlag(0x088A, 3, 0x4453))

    def _loc_D39E(): pass

    label('loc_D39E')

    SetScenaFlags(ScenaFlag(0x088A, 2, 0x4452))

    def _loc_D3A1(): pass

    label('loc_D3A1')

    SetScenaFlags(ScenaFlag(0x088A, 1, 0x4451))

    def _loc_D3A4(): pass

    label('loc_D3A4')

    QuestCtrl(0x0022, 0x03, 0x01, 0x02)

    Jump('loc_D3AF')

    def _loc_D3AF(): pass

    label('loc_D3AF')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007420, 'loc_D428'),
        (0x00007421, 'loc_D444'),
        (0x00007422, 'loc_D460'),
        (0x00007423, 'loc_D47C'),
        (0x00007424, 'loc_D498'),
        (0x00007425, 'loc_D4B4'),
        (0x00007426, 'loc_D4D0'),
        (0x00007427, 'loc_D4EC'),
        (0x00007428, 'loc_D508'),
        (0x00007429, 'loc_D524'),
        (0x0000742A, 'loc_D540'),
        (0x0000742B, 'loc_D55C'),
        (0x0000742C, 'loc_D578'),
        (0x0000742D, 'loc_D594'),
        (-1, 'loc_D5B0'),
    )

    def _loc_D428(): pass

    label('loc_D428')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7420, 0x0))

    Jump('loc_D5B5')

    def _loc_D444(): pass

    label('loc_D444')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7421, 0x0))

    Jump('loc_D5B5')

    def _loc_D460(): pass

    label('loc_D460')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7422, 0x0))

    Jump('loc_D5B5')

    def _loc_D47C(): pass

    label('loc_D47C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7423, 0x0))

    Jump('loc_D5B5')

    def _loc_D498(): pass

    label('loc_D498')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7424, 0x0))

    Jump('loc_D5B5')

    def _loc_D4B4(): pass

    label('loc_D4B4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7425, 0x0))

    Jump('loc_D5B5')

    def _loc_D4D0(): pass

    label('loc_D4D0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7426, 0x0))

    Jump('loc_D5B5')

    def _loc_D4EC(): pass

    label('loc_D4EC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7427, 0x0))

    Jump('loc_D5B5')

    def _loc_D508(): pass

    label('loc_D508')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7428, 0x0))

    Jump('loc_D5B5')

    def _loc_D524(): pass

    label('loc_D524')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7429, 0x0))

    Jump('loc_D5B5')

    def _loc_D540(): pass

    label('loc_D540')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x742A, 0x0))

    Jump('loc_D5B5')

    def _loc_D55C(): pass

    label('loc_D55C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x742B, 0x0))

    Jump('loc_D5B5')

    def _loc_D578(): pass

    label('loc_D578')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x742C, 0x0))

    Jump('loc_D5B5')

    def _loc_D594(): pass

    label('loc_D594')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x742D, 0x0))

    Jump('loc_D5B5')

    def _loc_D5B0(): pass

    label('loc_D5B0')

    Jump('loc_D5B5')

    def _loc_D5B5(): pass

    label('loc_D5B5')

    Jump('loc_CED9')

    def _loc_D5BA(): pass

    label('loc_D5BA')

    Return()

# id: 0x0050 offset: 0xD5BC
@scena.Code('EV_Jump_QS_341')
def EV_Jump_QS_341():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D5C5(): pass

    label('loc_D5C5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D6C7',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS341_01][手配魔獣を撃破　　　　　　　　]', 0x00007440)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D671',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_D671(): pass

    label('loc_D671')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D68C',
    )

    QuestCtrl(0x0023, 0x03, 0x01, 0x02)
    QuestCtrl(0x0023, 0x04, 0x02, 0x02)

    def _loc_D68C(): pass

    label('loc_D68C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007440, 'loc_D69D'),
        (-1, 'loc_D6BD'),
    )

    def _loc_D69D(): pass

    label('loc_D69D')

    FormationCtrl(0x1C, 0x01)
    OP_28((0xDD, 'r3430'), (0xDD, 'QS341_01_JUMP'), 0x00)

    Jump('loc_D6C2')

    def _loc_D6BD(): pass

    label('loc_D6BD')

    Jump('loc_D6C2')

    def _loc_D6C2(): pass

    label('loc_D6C2')

    Jump('loc_D5C5')

    def _loc_D6C7(): pass

    label('loc_D6C7')

    Return()

# id: 0x0051 offset: 0xD6C8
@scena.Code('EV_Jump_QS_342')
def EV_Jump_QS_342():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D6D1(): pass

    label('loc_D6D1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E2B9',
    )

    MenuCmd(0x00, 0x02, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS342_00]  [航行中のカレイジャスⅡ　　　　]　', 0x00007460)
    MenuCmd(0x01, 0x02, '[QS342_00B] [エリンに降りられない事に気付く]　', 0x00007461)
    MenuCmd(0x01, 0x02, '[QS342_01A] [エイボン丘陵の転位石前・選択肢]　', 0x00007462)
    MenuCmd(0x01, 0x02, '[QS342_01AB][エイボン丘陵の転位石前を確認　]　', 0x00007463)
    MenuCmd(0x01, 0x02, '[QS342_01B] [大森林の転位石前・選択肢　　　]　', 0x00007464)
    MenuCmd(0x01, 0x02, '[QS342_01BB][大森林の転位石前を確認　　　　]　', 0x00007465)
    MenuCmd(0x01, 0x02, '[QS342_02]  [カレイジャスⅡでの作戦会議　　]　', 0x00007466)
    MenuCmd(0x01, 0x02, '[QS342_03]  [エリン解放作戦開始　　　　　　]　', 0x00007467)
    MenuCmd(0x01, 0x02, '[QS342_03B] [大森林側の部隊に陽動を仕掛ける]　', 0x00007468)
    MenuCmd(0x01, 0x02, '[QS342_03C] [エマたちが結界に綻びを作る　　]　', 0x00007469)
    MenuCmd(0x01, 0x02, '[QS342_03D] [サングラール第一相入口に転位　]　', 0x0000746A)
    MenuCmd(0x01, 0x02, '[QS342_04]  [強化猟兵との戦闘１　　　　　　]戦', 0x0000746B)
    MenuCmd(0x01, 0x02, '[QS342_04B] [強化猟兵との戦闘１終了後　　　]　', 0x0000746C)
    MenuCmd(0x01, 0x02, '[QS342_05]  [強化猟兵との戦闘２　　　　　　]戦', 0x0000746D)
    MenuCmd(0x01, 0x02, '[QS342_05B] [強化猟兵との戦闘２終了後　　　]　', 0x0000746E)
    MenuCmd(0x01, 0x02, '[QS342_06]  [転位石使用不可を確認　　　　　]　', 0x0000746F)
    MenuCmd(0x01, 0x02, '[QS342_07]  [虚力場発生器を停止する１　　　]　', 0x00007470)
    MenuCmd(0x01, 0x02, '[QS342_08]  [エリンの里に入る　　　　　　　]　', 0x00007471)
    MenuCmd(0x01, 0x02, '[QS342_08B] [陽動班の激闘・エイボン丘陵　　]　', 0x00007472)
    MenuCmd(0x01, 0x02, '[QS342_08C] [陽動班の激闘・イストミア大森林]　', 0x00007473)
    MenuCmd(0x01, 0x02, '[QS342_08D] [強化猟兵との戦闘３　　　　　　]戦', 0x00007474)
    MenuCmd(0x01, 0x02, '[QS342_08E] [強化猟兵との戦闘３終了後　　　]　', 0x00007475)
    MenuCmd(0x01, 0x02, '[QS342_09]  [虚力場発生器を停止する２　　　]　', 0x00007476)
    MenuCmd(0x01, 0x02, '[QS342_10]  [強化猟兵との戦闘４　　　　　　]戦', 0x00007477)
    MenuCmd(0x01, 0x02, '[QS342_10B] [接続用ダミーイベント　　　　　]　', 0x00007478)
    MenuCmd(0x01, 0x02, '[QS342_10C] [陽動班への援護・エイボン丘陵　]　', 0x00007479)
    MenuCmd(0x01, 0x02, '[QS342_10D] [陽動班への援護・大森林　　　　]　', 0x0000747A)
    MenuCmd(0x01, 0x02, '[QS342_10E] [里人たちとの再会　　　　　　　]　', 0x0000747B)
    MenuCmd(0x01, 0x02, '[QS342_11]  [ＶＳギルバート＆アハツェン　　]戦', 0x0000747C)
    MenuCmd(0x01, 0x02, '[QS342_11B] [事件解決　　　　　　　　　　　]　', 0x0000747D)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E107',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000747D, 'loc_E069'),
        (0x0000747C, 'loc_E069'),
        (0x0000747B, 'loc_E069'),
        (0x0000747A, 'loc_E069'),
        (0x00007479, 'loc_E069'),
        (0x00007478, 'loc_E069'),
        (0x00007477, 'loc_E069'),
        (0x00007476, 'loc_E069'),
        (0x00007475, 'loc_E069'),
        (0x00007474, 'loc_E069'),
        (0x00007473, 'loc_E069'),
        (0x00007472, 'loc_E069'),
        (0x00007471, 'loc_E069'),
        (0x00007470, 'loc_E069'),
        (0x0000746F, 'loc_E069'),
        (0x0000746E, 'loc_E069'),
        (0x0000746D, 'loc_E069'),
        (0x0000746C, 'loc_E069'),
        (0x0000746B, 'loc_E069'),
        (0x0000746A, 'loc_E069'),
        (0x00007469, 'loc_E0FF'),
        (0x00007468, 'loc_E0FF'),
        (0x00007467, 'loc_E0FF'),
        (0x00007466, 'loc_E0FF'),
        (0x00007465, 'loc_E0FF'),
        (0x00007464, 'loc_E0FF'),
        (0x00007463, 'loc_E0FF'),
        (0x00007462, 'loc_E0FF'),
        (0x00007461, 'loc_E0FF'),
        (0x00007460, 'loc_E0FF'),
        (-1, 'loc_E107'),
    )

    def _loc_E069(): pass

    label('loc_E069')

    FormationCtrl(0x1C, 0x01)

    OP_18(
        0x27,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['蘭迪'])
    FormationAddMember(ChrTable['阿加特'])
    FormationAddMember(ChrTable['緹歐'])
    FormationAddMember(ChrTable['緹妲'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['緹妲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['奧利維爾'], 0x01000000)
    FormationAddMember(ChrTable['奧利維爾'])

    Jump('loc_E107')

    def _loc_E0FF(): pass

    label('loc_E0FF')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_E107')

    def _loc_E107(): pass

    label('loc_E107')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E128',
    )

    QuestCtrl(0x0024, 0x04, 0x01, 0x02)
    QuestCtrl(0x0024, 0x04, 0x02, 0x02)
    QuestCtrl(0x0024, 0x04, 0x08, 0x02)

    def _loc_E128(): pass

    label('loc_E128')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000747D, 'loc_E221'),
        (0x0000747C, 'loc_E224'),
        (0x0000747B, 'loc_E227'),
        (0x0000747A, 'loc_E22A'),
        (0x00007479, 'loc_E22D'),
        (0x00007478, 'loc_E230'),
        (0x00007477, 'loc_E233'),
        (0x00007476, 'loc_E236'),
        (0x00007475, 'loc_E239'),
        (0x00007474, 'loc_E23C'),
        (0x00007473, 'loc_E23F'),
        (0x00007472, 'loc_E242'),
        (0x00007471, 'loc_E245'),
        (0x00007470, 'loc_E248'),
        (0x0000746F, 'loc_E24B'),
        (0x0000746E, 'loc_E24E'),
        (0x0000746D, 'loc_E251'),
        (0x0000746C, 'loc_E254'),
        (0x0000746B, 'loc_E257'),
        (0x0000746A, 'loc_E25A'),
        (0x00007469, 'loc_E25D'),
        (0x00007468, 'loc_E260'),
        (0x00007467, 'loc_E263'),
        (0x00007466, 'loc_E266'),
        (0x00007465, 'loc_E269'),
        (0x00007464, 'loc_E26F'),
        (0x00007463, 'loc_E272'),
        (0x00007462, 'loc_E278'),
        (0x00007461, 'loc_E27B'),
        (0x00007460, 'loc_E27E'),
        (-1, 'loc_E289'),
    )

    def _loc_E221(): pass

    label('loc_E221')

    SetScenaFlags(ScenaFlag(0x0887, 5, 0x443D))

    def _loc_E224(): pass

    label('loc_E224')

    SetScenaFlags(ScenaFlag(0x0887, 4, 0x443C))

    def _loc_E227(): pass

    label('loc_E227')

    SetScenaFlags(ScenaFlag(0x0887, 3, 0x443B))

    def _loc_E22A(): pass

    label('loc_E22A')

    SetScenaFlags(ScenaFlag(0x0887, 2, 0x443A))

    def _loc_E22D(): pass

    label('loc_E22D')

    SetScenaFlags(ScenaFlag(0x0887, 1, 0x4439))

    def _loc_E230(): pass

    label('loc_E230')

    SetScenaFlags(ScenaFlag(0x0887, 0, 0x4438))

    def _loc_E233(): pass

    label('loc_E233')

    SetScenaFlags(ScenaFlag(0x0886, 7, 0x4437))

    def _loc_E236(): pass

    label('loc_E236')

    SetScenaFlags(ScenaFlag(0x0886, 6, 0x4436))

    def _loc_E239(): pass

    label('loc_E239')

    SetScenaFlags(ScenaFlag(0x0886, 5, 0x4435))

    def _loc_E23C(): pass

    label('loc_E23C')

    SetScenaFlags(ScenaFlag(0x0886, 4, 0x4434))

    def _loc_E23F(): pass

    label('loc_E23F')

    SetScenaFlags(ScenaFlag(0x0886, 3, 0x4433))

    def _loc_E242(): pass

    label('loc_E242')

    SetScenaFlags(ScenaFlag(0x0886, 2, 0x4432))

    def _loc_E245(): pass

    label('loc_E245')

    SetScenaFlags(ScenaFlag(0x0886, 1, 0x4431))

    def _loc_E248(): pass

    label('loc_E248')

    SetScenaFlags(ScenaFlag(0x0886, 0, 0x4430))

    def _loc_E24B(): pass

    label('loc_E24B')

    SetScenaFlags(ScenaFlag(0x0885, 7, 0x442F))

    def _loc_E24E(): pass

    label('loc_E24E')

    SetScenaFlags(ScenaFlag(0x0885, 6, 0x442E))

    def _loc_E251(): pass

    label('loc_E251')

    SetScenaFlags(ScenaFlag(0x0885, 5, 0x442D))

    def _loc_E254(): pass

    label('loc_E254')

    SetScenaFlags(ScenaFlag(0x0885, 4, 0x442C))

    def _loc_E257(): pass

    label('loc_E257')

    SetScenaFlags(ScenaFlag(0x0885, 3, 0x442B))

    def _loc_E25A(): pass

    label('loc_E25A')

    SetScenaFlags(ScenaFlag(0x0885, 2, 0x442A))

    def _loc_E25D(): pass

    label('loc_E25D')

    SetScenaFlags(ScenaFlag(0x0885, 1, 0x4429))

    def _loc_E260(): pass

    label('loc_E260')

    SetScenaFlags(ScenaFlag(0x0885, 0, 0x4428))

    def _loc_E263(): pass

    label('loc_E263')

    SetScenaFlags(ScenaFlag(0x0884, 7, 0x4427))

    def _loc_E266(): pass

    label('loc_E266')

    SetScenaFlags(ScenaFlag(0x0884, 6, 0x4426))

    def _loc_E269(): pass

    label('loc_E269')

    SetScenaFlags(ScenaFlag(0x08A1, 0, 0x4508))
    SetScenaFlags(ScenaFlag(0x0884, 5, 0x4425))

    def _loc_E26F(): pass

    label('loc_E26F')

    SetScenaFlags(ScenaFlag(0x0884, 4, 0x4424))

    def _loc_E272(): pass

    label('loc_E272')

    SetScenaFlags(ScenaFlag(0x08A0, 7, 0x4507))
    SetScenaFlags(ScenaFlag(0x0884, 3, 0x4423))

    def _loc_E278(): pass

    label('loc_E278')

    SetScenaFlags(ScenaFlag(0x0884, 2, 0x4422))

    def _loc_E27B(): pass

    label('loc_E27B')

    SetScenaFlags(ScenaFlag(0x0884, 1, 0x4421))

    def _loc_E27E(): pass

    label('loc_E27E')

    QuestCtrl(0x0024, 0x03, 0x01, 0x02)

    Jump('loc_E289')

    def _loc_E289(): pass

    label('loc_E289')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E2B4',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_E2B4(): pass

    label('loc_E2B4')

    Jump('loc_D6D1')

    def _loc_E2B9(): pass

    label('loc_E2B9')

    Return()

# id: 0x0052 offset: 0xE2BC
@scena.Code('EV_Jump_QS_343')
def EV_Jump_QS_343():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E2C5(): pass

    label('loc_E2C5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E4C9',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS343_01][ゼシカ＆ウェインと会話　　　　]　', 0x00007480)
    MenuCmd(0x01, 0x02, '[QS343_02][ラウラ＆デュバリィとの手合わせ]戦', 0x00007481)
    MenuCmd(0x01, 0x02, '[QS343_03][達成イベント　　　　　　　　　]　', 0x00007482)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3FC',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_E3FC(): pass

    label('loc_E3FC')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E41D',
    )

    QuestCtrl(0x0025, 0x04, 0x01, 0x02)
    QuestCtrl(0x0025, 0x04, 0x02, 0x02)
    QuestCtrl(0x0025, 0x04, 0x08, 0x02)

    def _loc_E41D(): pass

    label('loc_E41D')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007482, 'loc_E436'),
        (0x00007481, 'loc_E439'),
        (-1, 'loc_E44A'),
    )

    def _loc_E436(): pass

    label('loc_E436')

    SetScenaFlags(ScenaFlag(0x0888, 0, 0x4440))

    def _loc_E439(): pass

    label('loc_E439')

    SetScenaFlags(ScenaFlag(0x0887, 7, 0x443F))
    SetScenaFlags(ScenaFlag(0x08A1, 1, 0x4509))
    QuestCtrl(0x0025, 0x03, 0x01, 0x02)

    Jump('loc_E44A')

    def _loc_E44A(): pass

    label('loc_E44A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007480, 'loc_E46B'),
        (0x00007481, 'loc_E487'),
        (0x00007482, 'loc_E4A3'),
        (-1, 'loc_E4BF'),
    )

    def _loc_E46B(): pass

    label('loc_E46B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7480, 0x0))

    Jump('loc_E4C4')

    def _loc_E487(): pass

    label('loc_E487')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7481, 0x0))

    Jump('loc_E4C4')

    def _loc_E4A3(): pass

    label('loc_E4A3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7482, 0x0))

    Jump('loc_E4C4')

    def _loc_E4BF(): pass

    label('loc_E4BF')

    Jump('loc_E4C4')

    def _loc_E4C4(): pass

    label('loc_E4C4')

    Jump('loc_E2C5')

    def _loc_E4C9(): pass

    label('loc_E4C9')

    Return()

# id: 0x0053 offset: 0xE4CC
@scena.Code('EV_Jump_QS_344')
def EV_Jump_QS_344():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E4D5(): pass

    label('loc_E4D5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E74B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS344_00][ミランダと会話　　　　　　　　]', 0x000074A0)
    MenuCmd(0x01, 0x02, '[QS344_01][レオノーラ＆シャーリィを発見　]', 0x000074A1)
    MenuCmd(0x01, 0x02, '[QS344_02][シャーリィとの水泳勝負　　　　]', 0x000074A2)
    MenuCmd(0x01, 0x02, '[QS344_03][達成イベント　　　　　　　　　]', 0x000074A4)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E644',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_E644(): pass

    label('loc_E644')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E665',
    )

    QuestCtrl(0x0026, 0x04, 0x01, 0x02)
    QuestCtrl(0x0026, 0x04, 0x02, 0x02)
    QuestCtrl(0x0026, 0x04, 0x08, 0x02)

    def _loc_E665(): pass

    label('loc_E665')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000074A4, 'loc_E68E'),
        (0x000074A2, 'loc_E691'),
        (0x000074A1, 'loc_E697'),
        (0x000074A0, 'loc_E6A0'),
        (-1, 'loc_E6A8'),
    )

    def _loc_E68E(): pass

    label('loc_E68E')

    SetScenaFlags(ScenaFlag(0x0888, 4, 0x4444))

    def _loc_E691(): pass

    label('loc_E691')

    SetScenaFlags(ScenaFlag(0x0888, 3, 0x4443))
    SetScenaFlags(ScenaFlag(0x08A1, 2, 0x450A))

    def _loc_E697(): pass

    label('loc_E697')

    SetScenaFlags(ScenaFlag(0x0888, 2, 0x4442))
    QuestCtrl(0x0026, 0x03, 0x01, 0x02)

    def _loc_E6A0(): pass

    label('loc_E6A0')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_E6A8')

    def _loc_E6A8(): pass

    label('loc_E6A8')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000074A0, 'loc_E6D1'),
        (0x000074A1, 'loc_E6ED'),
        (0x000074A2, 'loc_E709'),
        (0x000074A4, 'loc_E725'),
        (-1, 'loc_E741'),
    )

    def _loc_E6D1(): pass

    label('loc_E6D1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74A0, 0x0))

    Jump('loc_E746')

    def _loc_E6ED(): pass

    label('loc_E6ED')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74A1, 0x0))

    Jump('loc_E746')

    def _loc_E709(): pass

    label('loc_E709')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74A2, 0x0))

    Jump('loc_E746')

    def _loc_E725(): pass

    label('loc_E725')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74A4, 0x0))

    Jump('loc_E746')

    def _loc_E741(): pass

    label('loc_E741')

    Jump('loc_E746')

    def _loc_E746(): pass

    label('loc_E746')

    Jump('loc_E4D5')

    def _loc_E74B(): pass

    label('loc_E74B')

    Return()

# id: 0x0054 offset: 0xE74C
@scena.Code('EV_Jump_QS_345')
def EV_Jump_QS_345():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E755(): pass

    label('loc_E755')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EB38',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS345_01]  [スタークと会話　　　　　　　　]', 0x000074C0)
    MenuCmd(0x01, 0x02, '[QS345_02A] [カイリ＆フリッツと遭遇　　　　]', 0x000074C1)
    MenuCmd(0x01, 0x02, '[QS345_02AB][ゼルスヘイム戦後　　　　　　　]', 0x000074C2)
    MenuCmd(0x01, 0x02, '[QS345_02B1] [シドニー＆エイダと遭遇１　　　]', 0x000074C3)
    MenuCmd(0x01, 0x02, '[QS345_02B2] [シドニー＆エイダと遭遇２　　　]', 0x000074C4)
    MenuCmd(0x01, 0x02, '[QS345_02BB][クインクマンバ戦後　　　　　　]', 0x000074C5)
    MenuCmd(0x01, 0x02, '[QS345_03]  [達成イベント　　　　　　　　　]', 0x000074C6)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E997',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_E997(): pass

    label('loc_E997')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E9B8',
    )

    QuestCtrl(0x0027, 0x04, 0x01, 0x02)
    QuestCtrl(0x0027, 0x04, 0x02, 0x02)
    QuestCtrl(0x0027, 0x04, 0x08, 0x02)

    def _loc_E9B8(): pass

    label('loc_E9B8')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000074C5, 'loc_E9E9'),
        (0x000074C4, 'loc_E9EC'),
        (0x000074C3, 'loc_E9EF'),
        (0x000074C2, 'loc_EA03'),
        (0x000074C1, 'loc_EA06'),
        (-1, 'loc_EA1A'),
    )

    def _loc_E9E9(): pass

    label('loc_E9E9')

    SetScenaFlags(ScenaFlag(0x0889, 4, 0x444C))

    def _loc_E9EC(): pass

    label('loc_E9EC')

    SetScenaFlags(ScenaFlag(0x0889, 3, 0x444B))

    def _loc_E9EF(): pass

    label('loc_E9EF')

    SetScenaFlags(ScenaFlag(0x0889, 0, 0x4448))
    SetScenaFlags(ScenaFlag(0x08A1, 3, 0x450B))
    QuestCtrl(0x0027, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    Jump('loc_EA1A')

    def _loc_EA03(): pass

    label('loc_EA03')

    SetScenaFlags(ScenaFlag(0x0889, 1, 0x4449))

    def _loc_EA06(): pass

    label('loc_EA06')

    SetScenaFlags(ScenaFlag(0x0889, 0, 0x4448))
    SetScenaFlags(ScenaFlag(0x08A1, 3, 0x450B))
    QuestCtrl(0x0027, 0x03, 0x01, 0x02)
    FormationCtrl(0x1C, 0x01)

    Jump('loc_EA1A')

    def _loc_EA1A(): pass

    label('loc_EA1A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000074C0, 'loc_EA5B'),
        (0x000074C1, 'loc_EA77'),
        (0x000074C2, 'loc_EA93'),
        (0x000074C3, 'loc_EAAF'),
        (0x000074C4, 'loc_EACB'),
        (0x000074C5, 'loc_EAE7'),
        (0x000074C6, 'loc_EB03'),
        (-1, 'loc_EB2E'),
    )

    def _loc_EA5B(): pass

    label('loc_EA5B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74C0, 0x0))

    Jump('loc_EB33')

    def _loc_EA77(): pass

    label('loc_EA77')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74C1, 0x0))

    Jump('loc_EB33')

    def _loc_EA93(): pass

    label('loc_EA93')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74C2, 0x0))

    Jump('loc_EB33')

    def _loc_EAAF(): pass

    label('loc_EAAF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74C3, 0x0))

    Jump('loc_EB33')

    def _loc_EACB(): pass

    label('loc_EACB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74C4, 0x0))

    Jump('loc_EB33')

    def _loc_EAE7(): pass

    label('loc_EAE7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74C5, 0x0))

    Jump('loc_EB33')

    def _loc_EB03(): pass

    label('loc_EB03')

    OP_71(0x00, 0x4448, 0x444D)
    FormationCtrl(0x1C, 0x01)
    QuestCtrl(0x0027, 0x03, 0x01, 0x02)
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x74C6, 0x0))

    Jump('loc_EB33')

    def _loc_EB2E(): pass

    label('loc_EB2E')

    Jump('loc_EB33')

    def _loc_EB33(): pass

    label('loc_EB33')

    Jump('loc_E755')

    def _loc_EB38(): pass

    label('loc_EB38')

    Return()

# id: 0x0055 offset: 0xEB3C
@scena.Code('EV_Jump_QS_346')
def EV_Jump_QS_346():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_EB45(): pass

    label('loc_EB45')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC3E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS346_01][手配魔獣を撃破　　　　　　　　]', 0x000074E0)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EBF1',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4089),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_EBF1(): pass

    label('loc_EBF1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC06',
    )

    QuestCtrl(0x0028, 0x04, 0x02, 0x02)

    def _loc_EC06(): pass

    label('loc_EC06')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000074E0, 'loc_EC17'),
        (-1, 'loc_EC34'),
    )

    def _loc_EC17(): pass

    label('loc_EC17')

    OP_28((0xDD, 'm1300'), (0xDD, 'QS346_01_JUMP'), 0x00)

    Jump('loc_EC39')

    def _loc_EC34(): pass

    label('loc_EC34')

    Jump('loc_EC39')

    def _loc_EC39(): pass

    label('loc_EC39')

    Jump('loc_EB45')

    def _loc_EC3E(): pass

    label('loc_EC3E')

    Return()

# id: 0x0056 offset: 0xEC40
@scena.Code('EV_Jump_QS_400')
def EV_Jump_QS_400():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_EC49(): pass

    label('loc_EC49')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F097',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS400_01] [サラ＆シャロンに話しかける　　]', 0x00007500)
    MenuCmd(0x01, 0x02, '[QS400_02A][ローゼリアたちに話しかける　　]', 0x00007501)
    MenuCmd(0x01, 0x02, '[QS400_02B][ルーシーに話しかける　　　　　]', 0x00007502)
    MenuCmd(0x01, 0x02, '[QS400_02C][エーデルに話しかける　　　　　]', 0x00007503)
    MenuCmd(0x01, 0x02, '[QS400_02D][セシルに話しかける　　　　　　]', 0x00007504)
    MenuCmd(0x01, 0x02, '[QS400_02E][オーレリアに話しかける　　　　]', 0x00007505)
    MenuCmd(0x01, 0x02, '[QS400_02F][シェラザードに話しかける　　　]', 0x00007506)
    MenuCmd(0x01, 0x02, '[QS400_02X][全員に声をかけた　　　　　　　]', 0x00007507)
    MenuCmd(0x01, 0x02, '[QS400_03] [予選　　　　　　　　　　　　　]', 0x00007508)
    MenuCmd(0x01, 0x02, '[QS400_04] [最終決戦　　　　　　　　　　　]', 0x00007509)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EF49',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_EF49(): pass

    label('loc_EF49')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EF6A',
    )

    QuestCtrl(0x0029, 0x04, 0x01, 0x02)
    QuestCtrl(0x0029, 0x04, 0x02, 0x02)
    QuestCtrl(0x0029, 0x04, 0x08, 0x02)

    def _loc_EF6A(): pass

    label('loc_EF6A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007509, 'loc_EFC3'),
        (0x00007508, 'loc_EFC6'),
        (0x00007507, 'loc_EFC9'),
        (0x00007506, 'loc_EFDB'),
        (0x00007505, 'loc_EFDB'),
        (0x00007504, 'loc_EFDB'),
        (0x00007503, 'loc_EFDB'),
        (0x00007502, 'loc_EFDB'),
        (0x00007501, 'loc_EFDB'),
        (0x00007500, 'loc_EFDE'),
        (-1, 'loc_EFE3'),
    )

    def _loc_EFC3(): pass

    label('loc_EFC3')

    SetScenaFlags(ScenaFlag(0x0991, 0, 0x4C88))

    def _loc_EFC6(): pass

    label('loc_EFC6')

    SetScenaFlags(ScenaFlag(0x0990, 7, 0x4C87))

    def _loc_EFC9(): pass

    label('loc_EFC9')

    SetScenaFlags(ScenaFlag(0x0990, 6, 0x4C86))
    SetScenaFlags(ScenaFlag(0x0990, 5, 0x4C85))
    SetScenaFlags(ScenaFlag(0x0990, 4, 0x4C84))
    SetScenaFlags(ScenaFlag(0x0990, 3, 0x4C83))
    SetScenaFlags(ScenaFlag(0x0990, 2, 0x4C82))
    SetScenaFlags(ScenaFlag(0x0990, 1, 0x4C81))

    def _loc_EFDB(): pass

    label('loc_EFDB')

    SetScenaFlags(ScenaFlag(0x0990, 0, 0x4C80))

    def _loc_EFDE(): pass

    label('loc_EFDE')

    Jump('loc_EFE3')

    def _loc_EFE3(): pass

    label('loc_EFE3')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x7507),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F067',
    )

    CreateChr(ChrTable['黎恩'], 'C_CHR000', 'リィン', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    Call(ScriptId.System4, 'QS400_02X')
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7508, 0x0))

    Jump('loc_F092')

    def _loc_F067(): pass

    label('loc_F067')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F092',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr23, 0xF8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0x11, 0x0, 0x0))

    def _loc_F092(): pass

    label('loc_F092')

    Jump('loc_EC49')

    def _loc_F097(): pass

    label('loc_F097')

    Return()

# id: 0x0057 offset: 0xF098
@scena.Code('EV_Jump_QS_500')
def EV_Jump_QS_500():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F0A1(): pass

    label('loc_F0A1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F63A',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS500_01]  [サンディ＆ジルダに話かける　　]', 0x00007520)
    MenuCmd(0x01, 0x02, '[QS500_02A1][《グリシーヌ生花店》に行く　　]', 0x00007521)
    MenuCmd(0x01, 0x02, '[QS500_02A2][サニーリリィを入手する　　　　]', 0x00007522)
    MenuCmd(0x01, 0x02, '[QS500_02BA][百貨店《タイムズ》に行く　　　]', 0x00007523)
    MenuCmd(0x01, 0x02, '[QS500_02BB][《野菜屋タッカー》に行く　　　]', 0x00007524)
    MenuCmd(0x01, 0x02, '[QS500_02BC][《クロスベル商工組合》に行く　]', 0x00007525)
    MenuCmd(0x01, 0x02, '[QS500_02BD][ガレットフラワーを入手する　　]', 0x00007526)
    MenuCmd(0x01, 0x02, '[QS500_02C1][リーザに話を聞く　　　　　　　]', 0x00007527)
    MenuCmd(0x01, 0x02, '[QS500_02C2][メイプルバジルを入手する　　　]', 0x00007528)
    MenuCmd(0x01, 0x02, '[QS500_03]  [収穫祭開始　　　　　　　　　　]', 0x00007529)
    MenuCmd(0x01, 0x02, '[QS500_04]  [アリエルの碑石にお参りする　　]', 0x0000752A)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F3ED',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_F3ED(): pass

    label('loc_F3ED')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F40E',
    )

    QuestCtrl(0x002A, 0x04, 0x01, 0x02)
    QuestCtrl(0x002A, 0x04, 0x02, 0x02)
    QuestCtrl(0x002A, 0x04, 0x08, 0x02)

    def _loc_F40E(): pass

    label('loc_F40E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000752A, 'loc_F46F'),
        (0x00007529, 'loc_F472'),
        (0x00007528, 'loc_F478'),
        (0x00007527, 'loc_F47B'),
        (0x00007526, 'loc_F47E'),
        (0x00007525, 'loc_F481'),
        (0x00007524, 'loc_F484'),
        (0x00007523, 'loc_F487'),
        (0x00007522, 'loc_F48A'),
        (0x00007521, 'loc_F48D'),
        (0x00007520, 'loc_F490'),
        (-1, 'loc_F49B'),
    )

    def _loc_F46F(): pass

    label('loc_F46F')

    SetScenaFlags(ScenaFlag(0x0A45, 4, 0x522C))

    def _loc_F472(): pass

    label('loc_F472')

    SetScenaFlags(ScenaFlag(0x0A50, 6, 0x5286))
    SetScenaFlags(ScenaFlag(0x0A45, 3, 0x522B))

    def _loc_F478(): pass

    label('loc_F478')

    SetScenaFlags(ScenaFlag(0x0A45, 2, 0x522A))

    def _loc_F47B(): pass

    label('loc_F47B')

    SetScenaFlags(ScenaFlag(0x0A45, 1, 0x5229))

    def _loc_F47E(): pass

    label('loc_F47E')

    SetScenaFlags(ScenaFlag(0x0A45, 0, 0x5228))

    def _loc_F481(): pass

    label('loc_F481')

    SetScenaFlags(ScenaFlag(0x0A44, 7, 0x5227))

    def _loc_F484(): pass

    label('loc_F484')

    SetScenaFlags(ScenaFlag(0x0A44, 6, 0x5226))

    def _loc_F487(): pass

    label('loc_F487')

    SetScenaFlags(ScenaFlag(0x0A44, 5, 0x5225))

    def _loc_F48A(): pass

    label('loc_F48A')

    SetScenaFlags(ScenaFlag(0x0A44, 4, 0x5224))

    def _loc_F48D(): pass

    label('loc_F48D')

    SetScenaFlags(ScenaFlag(0x0A44, 3, 0x5223))

    def _loc_F490(): pass

    label('loc_F490')

    QuestCtrl(0x002A, 0x03, 0x01, 0x02)

    Jump('loc_F49B')

    def _loc_F49B(): pass

    label('loc_F49B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007520, 'loc_F4FC'),
        (0x00007521, 'loc_F518'),
        (0x00007522, 'loc_F534'),
        (0x00007523, 'loc_F550'),
        (0x00007524, 'loc_F56C'),
        (0x00007525, 'loc_F588'),
        (0x00007526, 'loc_F5A4'),
        (0x00007527, 'loc_F5C0'),
        (0x00007528, 'loc_F5DC'),
        (0x00007529, 'loc_F5F8'),
        (0x0000752A, 'loc_F614'),
        (-1, 'loc_F630'),
    )

    def _loc_F4FC(): pass

    label('loc_F4FC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7520, 0x0))

    Jump('loc_F635')

    def _loc_F518(): pass

    label('loc_F518')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7521, 0x0))

    Jump('loc_F635')

    def _loc_F534(): pass

    label('loc_F534')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7522, 0x0))

    Jump('loc_F635')

    def _loc_F550(): pass

    label('loc_F550')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7523, 0x0))

    Jump('loc_F635')

    def _loc_F56C(): pass

    label('loc_F56C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7524, 0x0))

    Jump('loc_F635')

    def _loc_F588(): pass

    label('loc_F588')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7525, 0x0))

    Jump('loc_F635')

    def _loc_F5A4(): pass

    label('loc_F5A4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7526, 0x0))

    Jump('loc_F635')

    def _loc_F5C0(): pass

    label('loc_F5C0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7527, 0x0))

    Jump('loc_F635')

    def _loc_F5DC(): pass

    label('loc_F5DC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7528, 0x0))

    Jump('loc_F635')

    def _loc_F5F8(): pass

    label('loc_F5F8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7529, 0x0))

    Jump('loc_F635')

    def _loc_F614(): pass

    label('loc_F614')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x752A, 0x0))

    Jump('loc_F635')

    def _loc_F630(): pass

    label('loc_F630')

    Jump('loc_F635')

    def _loc_F635(): pass

    label('loc_F635')

    Jump('loc_F0A1')

    def _loc_F63A(): pass

    label('loc_F63A')

    Return()

# id: 0x0058 offset: 0xF63C
@scena.Code('EV_Jump_QS_501')
def EV_Jump_QS_501():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F645(): pass

    label('loc_F645')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F9AD',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS501_01] [アランたちの声を聞く　　　　　]　', 0x00007540)
    MenuCmd(0x01, 0x02, '[QS501_02] [沼地でアランと対峙する　　　　]　', 0x00007541)
    MenuCmd(0x01, 0x02, '[QS501_03] [パトリックに話をする　　　　　]　', 0x00007542)
    MenuCmd(0x01, 0x02, '[QS501_04] [アランとの対決　　　　　　　　]騎', 0x00007543)
    MenuCmd(0x01, 0x02, '[QS501_04B][ゾルゲ・メルギア戦後　　　　　]　', 0x00007544)
    MenuCmd(0x01, 0x02, '[QS501_04C][解決イベント　　　　　　　　　]　', 0x00007545)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F84E',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_F84E(): pass

    label('loc_F84E')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F86F',
    )

    QuestCtrl(0x002B, 0x04, 0x01, 0x02)
    QuestCtrl(0x002B, 0x04, 0x02, 0x02)
    QuestCtrl(0x002B, 0x04, 0x08, 0x02)

    def _loc_F86F(): pass

    label('loc_F86F')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007545, 'loc_F8A8'),
        (0x00007544, 'loc_F8AB'),
        (0x00007543, 'loc_F8AE'),
        (0x00007542, 'loc_F8B1'),
        (0x00007541, 'loc_F8B4'),
        (0x00007540, 'loc_F8B7'),
        (-1, 'loc_F8C2'),
    )

    def _loc_F8A8(): pass

    label('loc_F8A8')

    SetScenaFlags(ScenaFlag(0x0A43, 6, 0x521E))

    def _loc_F8AB(): pass

    label('loc_F8AB')

    SetScenaFlags(ScenaFlag(0x0A43, 5, 0x521D))

    def _loc_F8AE(): pass

    label('loc_F8AE')

    SetScenaFlags(ScenaFlag(0x0A43, 4, 0x521C))

    def _loc_F8B1(): pass

    label('loc_F8B1')

    SetScenaFlags(ScenaFlag(0x0A43, 3, 0x521B))

    def _loc_F8B4(): pass

    label('loc_F8B4')

    SetScenaFlags(ScenaFlag(0x0A43, 2, 0x521A))

    def _loc_F8B7(): pass

    label('loc_F8B7')

    QuestCtrl(0x002B, 0x03, 0x01, 0x02)

    Jump('loc_F8C2')

    def _loc_F8C2(): pass

    label('loc_F8C2')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007540, 'loc_F8FB'),
        (0x00007541, 'loc_F917'),
        (0x00007542, 'loc_F933'),
        (0x00007543, 'loc_F94F'),
        (0x00007544, 'loc_F96B'),
        (0x00007545, 'loc_F987'),
        (-1, 'loc_F9A3'),
    )

    def _loc_F8FB(): pass

    label('loc_F8FB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7540, 0x0))

    Jump('loc_F9A8')

    def _loc_F917(): pass

    label('loc_F917')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7541, 0x0))

    Jump('loc_F9A8')

    def _loc_F933(): pass

    label('loc_F933')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7542, 0x0))

    Jump('loc_F9A8')

    def _loc_F94F(): pass

    label('loc_F94F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7543, 0x0))

    Jump('loc_F9A8')

    def _loc_F96B(): pass

    label('loc_F96B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7544, 0x0))

    Jump('loc_F9A8')

    def _loc_F987(): pass

    label('loc_F987')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7545, 0x0))

    Jump('loc_F9A8')

    def _loc_F9A3(): pass

    label('loc_F9A3')

    Jump('loc_F9A8')

    def _loc_F9A8(): pass

    label('loc_F9A8')

    Jump('loc_F645')

    def _loc_F9AD(): pass

    label('loc_F9AD')

    Return()

# id: 0x0059 offset: 0xF9B0
@scena.Code('EV_Jump_QS_502')
def EV_Jump_QS_502():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F9B9(): pass

    label('loc_F9B9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FAB8',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS502_01][手配魔獣を撃破　　　　　　　　]', 0x00007560)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FA65',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_FA65(): pass

    label('loc_FA65')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FA80',
    )

    QuestCtrl(0x002C, 0x03, 0x01, 0x02)
    QuestCtrl(0x002C, 0x04, 0x02, 0x02)

    def _loc_FA80(): pass

    label('loc_FA80')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007560, 'loc_FA91'),
        (-1, 'loc_FAAE'),
    )

    def _loc_FA91(): pass

    label('loc_FA91')

    OP_28((0xDD, 'm0590'), (0xDD, 'QS502_01_JUMP'), 0x00)

    Jump('loc_FAB3')

    def _loc_FAAE(): pass

    label('loc_FAAE')

    Jump('loc_FAB3')

    def _loc_FAB3(): pass

    label('loc_FAB3')

    Jump('loc_F9B9')

    def _loc_FAB8(): pass

    label('loc_FAB8')

    Return()

# id: 0x005A offset: 0xFABC
@scena.Code('EV_Jump_QS_503')
def EV_Jump_QS_503():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FAC5(): pass

    label('loc_FAC5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_105F0',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS503_01]  [マイヤー＆ハルシュから話を聞く]', 0x00007580)
    MenuCmd(0x01, 0x02, '[QS503_02A] [エルサと会話　　　　　　　　　]', 0x00007581)
    MenuCmd(0x01, 0x02, '[QS503_02B] [ディアナについて尋ねる　　　　]', 0x00007582)
    MenuCmd(0x01, 0x02, '[QS503_02C] [調査を開始する　　　　　　　　]', 0x00007583)
    MenuCmd(0x01, 0x02, '[QS503_02ST][ＳＴ：他の街区に行こうとする　]', 0x00007584)
    MenuCmd(0x01, 0x02, '[QS503_03A] [ロイから話を聞く　　　　　　　]', 0x00007585)
    MenuCmd(0x01, 0x02, '[QS503_03B] [リナリーから話を聞く　　　　　]', 0x00007586)
    MenuCmd(0x01, 0x02, '[QS503_03C] [エリックから話を聞く　　　　　]', 0x00007587)
    MenuCmd(0x01, 0x02, '[QS503_04]  [失踪者の行方を推理　　　　　　]', 0x00007588)
    MenuCmd(0x01, 0x02, '[QS503_04ST][ＳＴ：支援課ビルに入れない　　]', 0x00007589)
    MenuCmd(0x01, 0x02, '[QS503_04A] [ジオフロントの扉・選択肢　　　]', 0x0000758A)
    MenuCmd(0x01, 0x02, '[QS503_04B] [ジオフロントＦの攻略開始　　　]', 0x0000758B)
    MenuCmd(0x01, 0x02, '[QS503_05]  [ヴァルジェムとの戦闘①　　　　]', 0x0000758C)
    MenuCmd(0x01, 0x02, '[QS503_05B] [サンドラを救出　　　　　　　　]', 0x0000758D)
    MenuCmd(0x01, 0x02, '[QS503_06]  [ヴァルジェムとの戦闘②　　　　]', 0x0000758E)
    MenuCmd(0x01, 0x02, '[QS503_06B] [プルーナを救出　　　　　　　　]', 0x0000758F)
    MenuCmd(0x01, 0x02, '[QS503_07]  [ヴァルジェムとの戦闘③　　　　]', 0x00007590)
    MenuCmd(0x01, 0x02, '[QS503_07B] [メイリンを救出　　　　　　　　]', 0x00007591)
    MenuCmd(0x01, 0x02, '[QS503_08]  [スキュラマームとの戦闘　　　　]', 0x00007592)
    MenuCmd(0x01, 0x02, '[QS503_08B] [ディアナを救出　　　　　　　　]', 0x00007593)
    MenuCmd(0x01, 0x02, '[QS503_08C] [特務支援課ビルの外観　　　　　]', 0x00007594)
    MenuCmd(0x01, 0x02, '[QS503_08D] [達成イベント　　　　　　　　　]', 0x00007595)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1019A',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x7583),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1019A',
    )

    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    Call(ScriptId.System, 'FC_TSMenu_Reset')

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['悠娜'])
    FormationAddMember(ChrTable['羅伊德'])
    FormationAddMember(ChrTable['艾莉'])
    FormationAddMember(ChrTable['緹歐'])
    FormationAddMember(ChrTable['蘭迪'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['測試：庫爾特襯衫'], 0x01000000)
    FormationAddMember(ChrTable['測試：庫爾特襯衫'])

    OP_18(
        0x27,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1019A(): pass

    label('loc_1019A')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_101BB',
    )

    QuestCtrl(0x002D, 0x04, 0x01, 0x02)
    QuestCtrl(0x002D, 0x04, 0x02, 0x02)
    QuestCtrl(0x002D, 0x04, 0x08, 0x02)

    def _loc_101BB(): pass

    label('loc_101BB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007595, 'loc_10274'),
        (0x00007594, 'loc_10277'),
        (0x00007593, 'loc_1027A'),
        (0x00007592, 'loc_1027D'),
        (0x00007591, 'loc_10280'),
        (0x00007590, 'loc_10283'),
        (0x0000758F, 'loc_10286'),
        (0x0000758E, 'loc_10289'),
        (0x0000758D, 'loc_1028C'),
        (0x0000758C, 'loc_1028F'),
        (0x0000758B, 'loc_10292'),
        (0x0000758A, 'loc_10295'),
        (0x00007589, 'loc_10298'),
        (0x00007588, 'loc_1029B'),
        (0x00007587, 'loc_102A4'),
        (0x00007586, 'loc_102A4'),
        (0x00007585, 'loc_102A4'),
        (0x00007584, 'loc_102A7'),
        (0x00007583, 'loc_102AA'),
        (0x00007582, 'loc_102AD'),
        (0x00007581, 'loc_102B0'),
        (0x00007580, 'loc_102B9'),
        (-1, 'loc_102BE'),
    )

    def _loc_10274(): pass

    label('loc_10274')

    SetScenaFlags(ScenaFlag(0x0A48, 2, 0x5242))

    def _loc_10277(): pass

    label('loc_10277')

    SetScenaFlags(ScenaFlag(0x0A48, 1, 0x5241))

    def _loc_1027A(): pass

    label('loc_1027A')

    SetScenaFlags(ScenaFlag(0x0A48, 0, 0x5240))

    def _loc_1027D(): pass

    label('loc_1027D')

    SetScenaFlags(ScenaFlag(0x0A47, 7, 0x523F))

    def _loc_10280(): pass

    label('loc_10280')

    SetScenaFlags(ScenaFlag(0x0A47, 6, 0x523E))

    def _loc_10283(): pass

    label('loc_10283')

    SetScenaFlags(ScenaFlag(0x0A47, 5, 0x523D))

    def _loc_10286(): pass

    label('loc_10286')

    SetScenaFlags(ScenaFlag(0x0A47, 4, 0x523C))

    def _loc_10289(): pass

    label('loc_10289')

    SetScenaFlags(ScenaFlag(0x0A47, 3, 0x523B))

    def _loc_1028C(): pass

    label('loc_1028C')

    SetScenaFlags(ScenaFlag(0x0A47, 2, 0x523A))

    def _loc_1028F(): pass

    label('loc_1028F')

    SetScenaFlags(ScenaFlag(0x0A47, 1, 0x5239))

    def _loc_10292(): pass

    label('loc_10292')

    SetScenaFlags(ScenaFlag(0x0A47, 0, 0x5238))

    def _loc_10295(): pass

    label('loc_10295')

    SetScenaFlags(ScenaFlag(0x0A46, 7, 0x5237))

    def _loc_10298(): pass

    label('loc_10298')

    SetScenaFlags(ScenaFlag(0x0A46, 6, 0x5236))

    def _loc_1029B(): pass

    label('loc_1029B')

    SetScenaFlags(ScenaFlag(0x0A46, 5, 0x5235))
    SetScenaFlags(ScenaFlag(0x0A46, 4, 0x5234))
    SetScenaFlags(ScenaFlag(0x0A46, 3, 0x5233))

    def _loc_102A4(): pass

    label('loc_102A4')

    SetScenaFlags(ScenaFlag(0x0A46, 2, 0x5232))

    def _loc_102A7(): pass

    label('loc_102A7')

    SetScenaFlags(ScenaFlag(0x0A46, 1, 0x5231))

    def _loc_102AA(): pass

    label('loc_102AA')

    SetScenaFlags(ScenaFlag(0x0A46, 0, 0x5230))

    def _loc_102AD(): pass

    label('loc_102AD')

    SetScenaFlags(ScenaFlag(0x0A45, 7, 0x522F))

    def _loc_102B0(): pass

    label('loc_102B0')

    SetScenaFlags(ScenaFlag(0x0A45, 6, 0x522E))
    QuestCtrl(0x002D, 0x03, 0x01, 0x02)

    def _loc_102B9(): pass

    label('loc_102B9')

    Jump('loc_102BE')

    def _loc_102BE(): pass

    label('loc_102BE')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00007580, 'loc_10377'),
        (0x00007581, 'loc_10393'),
        (0x00007582, 'loc_103AF'),
        (0x00007583, 'loc_103CB'),
        (0x00007584, 'loc_103E7'),
        (0x00007585, 'loc_1040A'),
        (0x00007586, 'loc_10426'),
        (0x00007587, 'loc_10442'),
        (0x00007588, 'loc_1045E'),
        (0x00007589, 'loc_1047A'),
        (0x0000758A, 'loc_10496'),
        (0x0000758B, 'loc_104B2'),
        (0x0000758C, 'loc_104CE'),
        (0x0000758D, 'loc_104EA'),
        (0x0000758E, 'loc_10506'),
        (0x0000758F, 'loc_10522'),
        (0x00007590, 'loc_1053E'),
        (0x00007591, 'loc_1055A'),
        (0x00007592, 'loc_10576'),
        (0x00007593, 'loc_10592'),
        (0x00007594, 'loc_105AE'),
        (0x00007595, 'loc_105CA'),
        (-1, 'loc_105E6'),
    )

    def _loc_10377(): pass

    label('loc_10377')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7580, 0x0))

    Jump('loc_105EB')

    def _loc_10393(): pass

    label('loc_10393')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7581, 0x0))

    Jump('loc_105EB')

    def _loc_103AF(): pass

    label('loc_103AF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7582, 0x0))

    Jump('loc_105EB')

    def _loc_103CB(): pass

    label('loc_103CB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7583, 0x0))

    Jump('loc_105EB')

    def _loc_103E7(): pass

    label('loc_103E7')

    OP_28((0xDD, 'c0200'), (0xDD, 'ST_QS503_02ST_CALL1'), 0x00)

    Jump('loc_105EB')

    def _loc_1040A(): pass

    label('loc_1040A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7585, 0x0))

    Jump('loc_105EB')

    def _loc_10426(): pass

    label('loc_10426')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7586, 0x0))

    Jump('loc_105EB')

    def _loc_10442(): pass

    label('loc_10442')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7587, 0x0))

    Jump('loc_105EB')

    def _loc_1045E(): pass

    label('loc_1045E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7587, 0x0))

    Jump('loc_105EB')

    def _loc_1047A(): pass

    label('loc_1047A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7589, 0x0))

    Jump('loc_105EB')

    def _loc_10496(): pass

    label('loc_10496')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x758A, 0x0))

    Jump('loc_105EB')

    def _loc_104B2(): pass

    label('loc_104B2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x758B, 0x0))

    Jump('loc_105EB')

    def _loc_104CE(): pass

    label('loc_104CE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x758C, 0x0))

    Jump('loc_105EB')

    def _loc_104EA(): pass

    label('loc_104EA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x758D, 0x0))

    Jump('loc_105EB')

    def _loc_10506(): pass

    label('loc_10506')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x758E, 0x0))

    Jump('loc_105EB')

    def _loc_10522(): pass

    label('loc_10522')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x758F, 0x0))

    Jump('loc_105EB')

    def _loc_1053E(): pass

    label('loc_1053E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7590, 0x0))

    Jump('loc_105EB')

    def _loc_1055A(): pass

    label('loc_1055A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7591, 0x0))

    Jump('loc_105EB')

    def _loc_10576(): pass

    label('loc_10576')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7592, 0x0))

    Jump('loc_105EB')

    def _loc_10592(): pass

    label('loc_10592')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7593, 0x0))

    Jump('loc_105EB')

    def _loc_105AE(): pass

    label('loc_105AE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7594, 0x0))

    Jump('loc_105EB')

    def _loc_105CA(): pass

    label('loc_105CA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x7595, 0x0))

    Jump('loc_105EB')

    def _loc_105E6(): pass

    label('loc_105E6')

    Jump('loc_105EB')

    def _loc_105EB(): pass

    label('loc_105EB')

    Jump('loc_FAC5')

    def _loc_105F0(): pass

    label('loc_105F0')

    Return()

# id: 0x005B offset: 0x105F4
@scena.Code('EV_Jump_QS_504')
def EV_Jump_QS_504():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_105FD(): pass

    label('loc_105FD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_107F7',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS504_01][スタークと会話　　　　　　　　]', 0x000075A0)
    MenuCmd(0x01, 0x02, '[QS504_02][勝負イベント　　　　　　　　　]', 0x000075A1)
    MenuCmd(0x01, 0x02, '[QS504_03][達成イベント　　　　　　　　　]', 0x000075A2)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1072B',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1072B(): pass

    label('loc_1072B')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1074C',
    )

    QuestCtrl(0x002E, 0x04, 0x01, 0x02)
    QuestCtrl(0x002E, 0x04, 0x02, 0x02)
    QuestCtrl(0x002E, 0x04, 0x08, 0x02)

    def _loc_1074C(): pass

    label('loc_1074C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075A2, 'loc_1076D'),
        (0x000075A1, 'loc_10770'),
        (0x000075A0, 'loc_10773'),
        (-1, 'loc_10778'),
    )

    def _loc_1076D(): pass

    label('loc_1076D')

    SetScenaFlags(ScenaFlag(0x0A44, 1, 0x5221))

    def _loc_10770(): pass

    label('loc_10770')

    SetScenaFlags(ScenaFlag(0x0A44, 0, 0x5220))

    def _loc_10773(): pass

    label('loc_10773')

    Jump('loc_10778')

    def _loc_10778(): pass

    label('loc_10778')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075A0, 'loc_10799'),
        (0x000075A1, 'loc_107B5'),
        (0x000075A2, 'loc_107D1'),
        (-1, 'loc_107ED'),
    )

    def _loc_10799(): pass

    label('loc_10799')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75A0, 0x0))

    Jump('loc_107F2')

    def _loc_107B5(): pass

    label('loc_107B5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75A1, 0x0))

    Jump('loc_107F2')

    def _loc_107D1(): pass

    label('loc_107D1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75A2, 0x0))

    Jump('loc_107F2')

    def _loc_107ED(): pass

    label('loc_107ED')

    Jump('loc_107F2')

    def _loc_107F2(): pass

    label('loc_107F2')

    Jump('loc_105FD')

    def _loc_107F7(): pass

    label('loc_107F7')

    Return()

# id: 0x005C offset: 0x107F8
@scena.Code('EV_Jump_QS_505')
def EV_Jump_QS_505():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10801(): pass

    label('loc_10801')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10EE2',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS505_00] [廃道前で山猫号Ⅱを発見　　　　]', 0x000075C0)
    MenuCmd(0x01, 0x02, '[QS505_01] [お参りをするかの選択　　　　　]', 0x000075C1)
    MenuCmd(0x01, 0x02, '[QS505_01B][異変発生　　　　　　　　　　　]', 0x000075C2)
    MenuCmd(0x01, 0x02, '[QS505_01C][異界化したハーメル廃道　　　　]', 0x000075C3)
    MenuCmd(0x01, 0x02, '[QS505_02] [亡者との戦い①　　　　　　　　]', 0x000075C4)
    MenuCmd(0x01, 0x02, '[QS505_02B][亡者との戦い①終了後　　　　　]', 0x000075C5)
    MenuCmd(0x01, 0x02, '[QS505_03] [亡者との戦い②　　　　　　　　]', 0x000075C6)
    MenuCmd(0x01, 0x02, '[QS505_03B][亡者との戦い②終了後　　　　　]', 0x000075C7)
    MenuCmd(0x01, 0x02, '[QS505_04] [亡者との戦い③　　　　　　　　]', 0x000075C8)
    MenuCmd(0x01, 0x02, '[QS505_04B][亡者との戦い③終了後　　　　　]', 0x000075C9)
    MenuCmd(0x01, 0x02, '[QS505_05] [廃村に入る　　　　　　　　　　]', 0x000075CA)
    MenuCmd(0x01, 0x02, '[QS505_06] [大ボス・ベヌウ上位版との決戦　]', 0x000075CB)
    MenuCmd(0x01, 0x02, '[QS505_06B][異変解決　　　　　　　　　　　]', 0x000075CC)
    MenuCmd(0x01, 0x02, '[QS505_06C][クエスト達成　　　　　　　　　]', 0x000075CD)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10C08',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_10C08(): pass

    label('loc_10C08')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10C29',
    )

    QuestCtrl(0x002F, 0x04, 0x01, 0x02)
    QuestCtrl(0x002F, 0x04, 0x02, 0x02)
    QuestCtrl(0x002F, 0x04, 0x08, 0x02)

    def _loc_10C29(): pass

    label('loc_10C29')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075CD, 'loc_10CA2'),
        (0x000075CC, 'loc_10CA5'),
        (0x000075CB, 'loc_10CA8'),
        (0x000075CA, 'loc_10CAB'),
        (0x000075C9, 'loc_10CAE'),
        (0x000075C8, 'loc_10CB1'),
        (0x000075C7, 'loc_10CB4'),
        (0x000075C6, 'loc_10CB7'),
        (0x000075C5, 'loc_10CBA'),
        (0x000075C4, 'loc_10CBD'),
        (0x000075C3, 'loc_10CC0'),
        (0x000075C2, 'loc_10CC3'),
        (0x000075C1, 'loc_10CC9'),
        (0x000075C0, 'loc_10CCC'),
        (-1, 'loc_10CD7'),
    )

    def _loc_10CA2(): pass

    label('loc_10CA2')

    SetScenaFlags(ScenaFlag(0x0A41, 5, 0x520D))

    def _loc_10CA5(): pass

    label('loc_10CA5')

    SetScenaFlags(ScenaFlag(0x0A41, 4, 0x520C))

    def _loc_10CA8(): pass

    label('loc_10CA8')

    SetScenaFlags(ScenaFlag(0x0A41, 3, 0x520B))

    def _loc_10CAB(): pass

    label('loc_10CAB')

    SetScenaFlags(ScenaFlag(0x0A41, 2, 0x520A))

    def _loc_10CAE(): pass

    label('loc_10CAE')

    SetScenaFlags(ScenaFlag(0x0A41, 1, 0x5209))

    def _loc_10CB1(): pass

    label('loc_10CB1')

    SetScenaFlags(ScenaFlag(0x0A41, 0, 0x5208))

    def _loc_10CB4(): pass

    label('loc_10CB4')

    SetScenaFlags(ScenaFlag(0x0A40, 7, 0x5207))

    def _loc_10CB7(): pass

    label('loc_10CB7')

    SetScenaFlags(ScenaFlag(0x0A40, 6, 0x5206))

    def _loc_10CBA(): pass

    label('loc_10CBA')

    SetScenaFlags(ScenaFlag(0x0A40, 5, 0x5205))

    def _loc_10CBD(): pass

    label('loc_10CBD')

    SetScenaFlags(ScenaFlag(0x0A40, 4, 0x5204))

    def _loc_10CC0(): pass

    label('loc_10CC0')

    SetScenaFlags(ScenaFlag(0x0A40, 3, 0x5203))

    def _loc_10CC3(): pass

    label('loc_10CC3')

    SetScenaFlags(ScenaFlag(0x0A50, 0, 0x5280))
    SetScenaFlags(ScenaFlag(0x0A40, 2, 0x5202))

    def _loc_10CC9(): pass

    label('loc_10CC9')

    SetScenaFlags(ScenaFlag(0x0A40, 1, 0x5201))

    def _loc_10CCC(): pass

    label('loc_10CCC')

    QuestCtrl(0x002F, 0x03, 0x01, 0x02)

    Jump('loc_10CD7')

    def _loc_10CD7(): pass

    label('loc_10CD7')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075C0, 'loc_10D50'),
        (0x000075C1, 'loc_10D6C'),
        (0x000075C2, 'loc_10D88'),
        (0x000075C3, 'loc_10DA4'),
        (0x000075C4, 'loc_10DC0'),
        (0x000075C5, 'loc_10DDC'),
        (0x000075C6, 'loc_10DF8'),
        (0x000075C7, 'loc_10E14'),
        (0x000075C8, 'loc_10E30'),
        (0x000075C9, 'loc_10E4C'),
        (0x000075CA, 'loc_10E68'),
        (0x000075CB, 'loc_10E84'),
        (0x000075CC, 'loc_10EA0'),
        (0x000075CD, 'loc_10EBC'),
        (-1, 'loc_10ED8'),
    )

    def _loc_10D50(): pass

    label('loc_10D50')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C0, 0x0))

    Jump('loc_10EDD')

    def _loc_10D6C(): pass

    label('loc_10D6C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C1, 0x0))

    Jump('loc_10EDD')

    def _loc_10D88(): pass

    label('loc_10D88')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C2, 0x0))

    Jump('loc_10EDD')

    def _loc_10DA4(): pass

    label('loc_10DA4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C3, 0x0))

    Jump('loc_10EDD')

    def _loc_10DC0(): pass

    label('loc_10DC0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C4, 0x0))

    Jump('loc_10EDD')

    def _loc_10DDC(): pass

    label('loc_10DDC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C5, 0x0))

    Jump('loc_10EDD')

    def _loc_10DF8(): pass

    label('loc_10DF8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C6, 0x0))

    Jump('loc_10EDD')

    def _loc_10E14(): pass

    label('loc_10E14')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C7, 0x0))

    Jump('loc_10EDD')

    def _loc_10E30(): pass

    label('loc_10E30')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C8, 0x0))

    Jump('loc_10EDD')

    def _loc_10E4C(): pass

    label('loc_10E4C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75C9, 0x0))

    Jump('loc_10EDD')

    def _loc_10E68(): pass

    label('loc_10E68')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75CA, 0x0))

    Jump('loc_10EDD')

    def _loc_10E84(): pass

    label('loc_10E84')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75CB, 0x0))

    Jump('loc_10EDD')

    def _loc_10EA0(): pass

    label('loc_10EA0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75CC, 0x0))

    Jump('loc_10EDD')

    def _loc_10EBC(): pass

    label('loc_10EBC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75CD, 0x0))

    Jump('loc_10EDD')

    def _loc_10ED8(): pass

    label('loc_10ED8')

    Jump('loc_10EDD')

    def _loc_10EDD(): pass

    label('loc_10EDD')

    Jump('loc_10801')

    def _loc_10EE2(): pass

    label('loc_10EE2')

    Return()

# id: 0x005D offset: 0x10EE4
@scena.Code('EV_Jump_QS_506')
def EV_Jump_QS_506():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10EED(): pass

    label('loc_10EED')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11727',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[QS506_01] [トヴァルからの聯絡　　　　　　]　', 0x000075E0)
    MenuCmd(0x01, 0x02, '[QS506_02] [聖霊窟が出現しているのを発見　]　', 0x000075E1)
    MenuCmd(0x01, 0x02, '[QS506_03] [遺跡に入る・選択肢　　　　　　]　', 0x000075E2)
    MenuCmd(0x01, 0x02, '[QS506_03B][トヴァルと共に遺跡に入る　　　]　', 0x000075E3)
    MenuCmd(0x01, 0x02, '[QS506_04] [大地の聖獣の試練　　　　　　　]戦', 0x000075E4)
    MenuCmd(0x01, 0x02, '[QS506_04B][加護を授かる　　　　　　　　　]　', 0x000075E5)
    MenuCmd(0x01, 0x02, '[QS506_04C][クエスト達成　　　　　　　　　]　', 0x000075E6)
    MenuCmd(0x01, 0x02, '[QS506_EX01][大地の聖獣の試練・救済版　　　]　', 0x000075E7)
    MenuCmd(0x01, 0x02, '[QS506_EX02][因果の渦を調べる・選択肢　　　]　', 0x000075E8)
    MenuCmd(0x01, 0x02, '[QS506_EX03][因果の渦から戻ってくる　　　　]　', 0x000075E9)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11279',
    )

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075E9, 'loc_11234'),
        (0x000075E8, 'loc_11234'),
        (0x000075E7, 'loc_11234'),
        (0x000075E6, 'loc_11242'),
        (0x000075E5, 'loc_11242'),
        (0x000075E4, 'loc_11242'),
        (0x000075E3, 'loc_11242'),
        (0x000075E2, 'loc_11242'),
        (0x000075E1, 'loc_11242'),
        (0x000075E0, 'loc_11242'),
        (-1, 'loc_11250'),
    )

    def _loc_11234(): pass

    label('loc_11234')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6077),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11250')

    def _loc_11242(): pass

    label('loc_11242')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11250')

    def _loc_11250(): pass

    label('loc_11250')

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_11279(): pass

    label('loc_11279')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1129A',
    )

    QuestCtrl(0x0030, 0x04, 0x01, 0x02)
    QuestCtrl(0x0030, 0x04, 0x02, 0x02)
    QuestCtrl(0x0030, 0x04, 0x08, 0x02)

    def _loc_1129A(): pass

    label('loc_1129A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075E6, 'loc_112CB'),
        (0x000075E5, 'loc_112CB'),
        (0x000075E4, 'loc_112CB'),
        (0x000075E3, 'loc_112CB'),
        (0x000075E1, 'loc_112CB'),
        (-1, 'loc_114A5'),
    )

    def _loc_112CB(): pass

    label('loc_112CB')

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '救済版にしない', 0x00000001)
    MenuCmd(0x01, 0x02, '救済版にする', 0x00000002)
    MenuCmd(0x02, 0x02, 0x00, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF9)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11371',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6077),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    SetScenaFlags(ScenaFlag(0x0A43, 0, 0x5218))
    SetScenaFlags(ScenaFlag(0x0A42, 7, 0x5217))
    SetScenaFlags(ScenaFlag(0x0060, 3, 0x303))

    def _loc_11371(): pass

    label('loc_11371')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x75E6),
            Expr.Equ,
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x75E5),
            Expr.Equ,
            Expr.Or,
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x75E4),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_114A0',
    )

    FormationCtrl(0x14, 0x0000, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0019)
    OP_C4(0x02, 0x00, 0xF0A6)
    OP_C4(0x02, 0x00, 0xF0A7)
    OP_C4(0x02, 0x00, 0xF0A8)
    OP_C4(0x02, 0x00, 0xF0A9)
    OP_C4(0x02, 0x00, 0xF0AA)
    OP_C4(0x02, 0x00, 0xF0AB)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_69(0x14, 0x01, 0x00)
    FormationCtrl(0x14, 0x0000, 0x0019, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['托娃'], 0x00000110)
    MenuChrFlagCmd(0x00, 0xF0A6, 0x00000100)
    MenuChrFlagCmd(0x00, 0xF0A7, 0x00000100)
    MenuChrFlagCmd(0x00, 0xF0A8, 0x00000100)
    MenuChrFlagCmd(0x00, 0xF0A9, 0x00000100)
    MenuChrFlagCmd(0x00, 0xF0AA, 0x00000100)
    MenuChrFlagCmd(0x00, 0xF0AB, 0x00000100)

    def _loc_114A0(): pass

    label('loc_114A0')

    Jump('loc_114A5')

    def _loc_114A5(): pass

    label('loc_114A5')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075E9, 'loc_114FE'),
        (0x000075E8, 'loc_1150D'),
        (0x000075E7, 'loc_11510'),
        (0x000075E6, 'loc_11518'),
        (0x000075E5, 'loc_1151B'),
        (0x000075E4, 'loc_1151E'),
        (0x000075E3, 'loc_11521'),
        (0x000075E2, 'loc_11524'),
        (0x000075E1, 'loc_11527'),
        (0x000075E0, 'loc_1154E'),
        (-1, 'loc_11553'),
    )

    def _loc_114FE(): pass

    label('loc_114FE')

    SetScenaFlags(ScenaFlag(0x0A42, 5, 0x5215))
    SetScenaFlags(ScenaFlag(0x0A42, 4, 0x5214))
    SetScenaFlags(ScenaFlag(0x0A42, 3, 0x5213))
    SetScenaFlags(ScenaFlag(0x0A42, 1, 0x5211))
    SetScenaFlags(ScenaFlag(0x0A43, 0, 0x5218))

    def _loc_1150D(): pass

    label('loc_1150D')

    SetScenaFlags(ScenaFlag(0x0A42, 7, 0x5217))

    def _loc_11510(): pass

    label('loc_11510')

    SetScenaFlags(ScenaFlag(0x0060, 3, 0x303))

    Jump('loc_11553')

    def _loc_11518(): pass

    label('loc_11518')

    SetScenaFlags(ScenaFlag(0x0A42, 5, 0x5215))

    def _loc_1151B(): pass

    label('loc_1151B')

    SetScenaFlags(ScenaFlag(0x0A42, 4, 0x5214))

    def _loc_1151E(): pass

    label('loc_1151E')

    SetScenaFlags(ScenaFlag(0x0A42, 3, 0x5213))

    def _loc_11521(): pass

    label('loc_11521')

    SetScenaFlags(ScenaFlag(0x0A42, 2, 0x5212))

    def _loc_11524(): pass

    label('loc_11524')

    SetScenaFlags(ScenaFlag(0x0A42, 1, 0x5211))

    def _loc_11527(): pass

    label('loc_11527')

    SetScenaFlags(ScenaFlag(0x0A42, 0, 0x5210))

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x6077),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11543',
    )

    QuestCtrl(0x0030, 0x03, 0x01, 0x02)

    Jump('loc_11549')

    def _loc_11543(): pass

    label('loc_11543')

    QuestCtrl(0x0031, 0x03, 0x01, 0x02)

    def _loc_11549(): pass

    label('loc_11549')

    Jump('loc_11553')

    def _loc_1154E(): pass

    label('loc_1154E')

    Jump('loc_11553')

    def _loc_11553(): pass

    label('loc_11553')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000075E0, 'loc_115AC'),
        (0x000075E1, 'loc_11621'),
        (0x000075E2, 'loc_1163D'),
        (0x000075E3, 'loc_11659'),
        (0x000075E4, 'loc_11675'),
        (0x000075E5, 'loc_11691'),
        (0x000075E6, 'loc_116AD'),
        (0x000075E7, 'loc_116C9'),
        (0x000075E8, 'loc_116E5'),
        (0x000075E9, 'loc_11701'),
        (-1, 'loc_1171D'),
    )

    def _loc_115AC(): pass

    label('loc_115AC')

    CreateChr(ChrTable['黎恩'], 'C_CHR000', 'リィン', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    Call(ScriptId.System4, 'QS506_01')
    OP_28((0xDD, 'v3000'), (0xDD, 'DefaultEntry'), 0x00)

    Jump('loc_11722')

    def _loc_11621(): pass

    label('loc_11621')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E1, 0x0))

    Jump('loc_11722')

    def _loc_1163D(): pass

    label('loc_1163D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E2, 0x0))

    Jump('loc_11722')

    def _loc_11659(): pass

    label('loc_11659')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E3, 0x0))

    Jump('loc_11722')

    def _loc_11675(): pass

    label('loc_11675')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E4, 0x0))

    Jump('loc_11722')

    def _loc_11691(): pass

    label('loc_11691')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E5, 0x0))

    Jump('loc_11722')

    def _loc_116AD(): pass

    label('loc_116AD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E6, 0x0))

    Jump('loc_11722')

    def _loc_116C9(): pass

    label('loc_116C9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E7, 0x0))

    Jump('loc_11722')

    def _loc_116E5(): pass

    label('loc_116E5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E8, 0x0))

    Jump('loc_11722')

    def _loc_11701(): pass

    label('loc_11701')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x75E9, 0x0))

    Jump('loc_11722')

    def _loc_1171D(): pass

    label('loc_1171D')

    Jump('loc_11722')

    def _loc_11722(): pass

    label('loc_11722')

    Jump('loc_10EED')

    def _loc_11727(): pass

    label('loc_11727')

    Return()

# id: 0x005E offset: 0x11728
@scena.Code('EV_KizunaJump')
def EV_KizunaJump():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11731(): pass

    label('loc_11731')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12326',
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1179D',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持０）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_1179D(): pass

    label('loc_1179D')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_117EE',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持１）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_117EE(): pass

    label('loc_117EE')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1183F',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持２）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_1183F(): pass

    label('loc_1183F')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11890',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持３）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_11890(): pass

    label('loc_11890')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_118E1',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持４）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_118E1(): pass

    label('loc_118E1')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11932',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持５）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_11932(): pass

    label('loc_11932')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11983',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持６）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_11983(): pass

    label('loc_11983')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_119D4',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持７）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_119D4(): pass

    label('loc_119D4')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A25',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持８）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_11A25(): pass

    label('loc_11A25')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A76',
    )

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持９）》', 0x00000065)

    Jump('loc_11AB4')

    def _loc_11A76(): pass

    label('loc_11A76')

    MenuCmd(0x01, 0x01, '《絆行動ポイントを増やす（所持？）》', 0x00000065)

    def _loc_11AB4(): pass

    label('loc_11AB4')

    MenuCmd(0x01, 0x01, '[KZ01xx][絆イベント01・ユウナ　　] ＞', 0x00000001)
    MenuCmd(0x01, 0x01, '[KZ02xx][絆イベント02・クルト　　] ＞', 0x00000002)
    MenuCmd(0x01, 0x01, '[KZ03xx][絆イベント03・アルティナ] ＞', 0x00000003)
    MenuCmd(0x01, 0x01, '[KZ04xx][絆イベント04・ミュゼ　　] ＞', 0x00000004)
    MenuCmd(0x01, 0x01, '[KZ05xx][絆イベント05・アッシュ　] ＞', 0x00000005)
    MenuCmd(0x01, 0x01, '[KZ06xx][絆イベント06・アリサ　　] ＞', 0x00000006)
    MenuCmd(0x01, 0x01, '[KZ07xx][絆イベント07・エリオット] ＞', 0x00000007)
    MenuCmd(0x01, 0x01, '[KZ08xx][絆イベント08・ラウラ　　] ＞', 0x00000008)
    MenuCmd(0x01, 0x01, '[KZ09xx][絆イベント09・マキアス　] ＞', 0x00000009)
    MenuCmd(0x01, 0x01, '[KZ10xx][絆イベント10・エマ　　　] ＞', 0x0000000A)
    MenuCmd(0x01, 0x01, '[KZ11xx][絆イベント11・ユーシス　] ＞', 0x0000000B)
    MenuCmd(0x01, 0x01, '[KZ12xx][絆イベント12・フィー　　] ＞', 0x0000000C)
    MenuCmd(0x01, 0x01, '[KZ13xx][絆イベント13・ガイウス　] ＞', 0x0000000D)
    MenuCmd(0x01, 0x01, '[KZ14xx][絆イベント14・クロウ　　] ＞', 0x0000000E)
    MenuCmd(0x01, 0x01, '[KZ15xx][絆イベント15・サラ　　　] ＞', 0x0000000F)
    MenuCmd(0x01, 0x01, '[KZ16xx][絆イベント16・トワ　　　] ＞', 0x00000010)
    MenuCmd(0x01, 0x01, '[KZ17xx][絆イベント17・デュバリィ] ＞', 0x00000011)
    MenuCmd(0x01, 0x01, '[KZ18xx][絆イベント18・セリーヌ　] ＞', 0x00000012)
    MenuCmd(0x01, 0x01, '[KZ19xx][絆イベント19・アルフィン] ＞', 0x00000013)
    MenuCmd(0x01, 0x01, '[KZ20xx][絆イベント20・エリゼ　　] ＞', 0x00000014)
    MenuCmd(0x01, 0x01, '[KZ99xx][前日譚アトラクション　　] ＞', 0x00000063)
    MenuCmd(0x01, 0x01, '[KZ0Xxx][前日譚その他　　　　　　] ＞', 0x00000015)
    MenuCmd(0x01, 0x01, '《絆行動ポイントをゼロにする》', 0x00000064)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x15),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11FFB',
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))

    def _loc_11FFB(): pass

    label('loc_11FFB')

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_120CC'),
        (0x00000002, 'loc_120E5'),
        (0x00000003, 'loc_120FE'),
        (0x00000004, 'loc_12117'),
        (0x00000005, 'loc_12130'),
        (0x00000006, 'loc_12149'),
        (0x00000007, 'loc_12162'),
        (0x00000008, 'loc_1217B'),
        (0x00000009, 'loc_12194'),
        (0x0000000A, 'loc_121AD'),
        (0x0000000B, 'loc_121C6'),
        (0x0000000C, 'loc_121DF'),
        (0x0000000D, 'loc_121F8'),
        (0x0000000E, 'loc_12211'),
        (0x0000000F, 'loc_1222A'),
        (0x00000010, 'loc_12243'),
        (0x00000011, 'loc_1225C'),
        (0x00000012, 'loc_12275'),
        (0x00000013, 'loc_1228E'),
        (0x00000014, 'loc_122A7'),
        (0x00000063, 'loc_122C0'),
        (0x00000015, 'loc_122D9'),
        (0x00000064, 'loc_122F2'),
        (0x00000065, 'loc_122FA'),
        (0x000000C8, 'loc_12302'),
        (-1, 'loc_12313'),
    )

    def _loc_120CC(): pass

    label('loc_120CC')

    Call(ScriptId.Current, 'EV_KizunaJump_01')

    Jump('loc_12321')

    def _loc_120E5(): pass

    label('loc_120E5')

    Call(ScriptId.Current, 'EV_KizunaJump_02')

    Jump('loc_12321')

    def _loc_120FE(): pass

    label('loc_120FE')

    Call(ScriptId.Current, 'EV_KizunaJump_03')

    Jump('loc_12321')

    def _loc_12117(): pass

    label('loc_12117')

    Call(ScriptId.Current, 'EV_KizunaJump_04')

    Jump('loc_12321')

    def _loc_12130(): pass

    label('loc_12130')

    Call(ScriptId.Current, 'EV_KizunaJump_05')

    Jump('loc_12321')

    def _loc_12149(): pass

    label('loc_12149')

    Call(ScriptId.Current, 'EV_KizunaJump_06')

    Jump('loc_12321')

    def _loc_12162(): pass

    label('loc_12162')

    Call(ScriptId.Current, 'EV_KizunaJump_07')

    Jump('loc_12321')

    def _loc_1217B(): pass

    label('loc_1217B')

    Call(ScriptId.Current, 'EV_KizunaJump_08')

    Jump('loc_12321')

    def _loc_12194(): pass

    label('loc_12194')

    Call(ScriptId.Current, 'EV_KizunaJump_09')

    Jump('loc_12321')

    def _loc_121AD(): pass

    label('loc_121AD')

    Call(ScriptId.Current, 'EV_KizunaJump_10')

    Jump('loc_12321')

    def _loc_121C6(): pass

    label('loc_121C6')

    Call(ScriptId.Current, 'EV_KizunaJump_11')

    Jump('loc_12321')

    def _loc_121DF(): pass

    label('loc_121DF')

    Call(ScriptId.Current, 'EV_KizunaJump_12')

    Jump('loc_12321')

    def _loc_121F8(): pass

    label('loc_121F8')

    Call(ScriptId.Current, 'EV_KizunaJump_13')

    Jump('loc_12321')

    def _loc_12211(): pass

    label('loc_12211')

    Call(ScriptId.Current, 'EV_KizunaJump_14')

    Jump('loc_12321')

    def _loc_1222A(): pass

    label('loc_1222A')

    Call(ScriptId.Current, 'EV_KizunaJump_15')

    Jump('loc_12321')

    def _loc_12243(): pass

    label('loc_12243')

    Call(ScriptId.Current, 'EV_KizunaJump_16')

    Jump('loc_12321')

    def _loc_1225C(): pass

    label('loc_1225C')

    Call(ScriptId.Current, 'EV_KizunaJump_17')

    Jump('loc_12321')

    def _loc_12275(): pass

    label('loc_12275')

    Call(ScriptId.Current, 'EV_KizunaJump_18')

    Jump('loc_12321')

    def _loc_1228E(): pass

    label('loc_1228E')

    Call(ScriptId.Current, 'EV_KizunaJump_19')

    Jump('loc_12321')

    def _loc_122A7(): pass

    label('loc_122A7')

    Call(ScriptId.Current, 'EV_KizunaJump_20')

    Jump('loc_12321')

    def _loc_122C0(): pass

    label('loc_122C0')

    Call(ScriptId.Current, 'EV_KizunaJump_99')

    Jump('loc_12321')

    def _loc_122D9(): pass

    label('loc_122D9')

    Call(ScriptId.Current, 'EV_KizunaJump_0X')

    Jump('loc_12321')

    def _loc_122F2(): pass

    label('loc_122F2')

    OP_88(0x0000)

    Jump('loc_12321')

    def _loc_122FA(): pass

    label('loc_122FA')

    OP_89(0x0001)

    Jump('loc_12321')

    def _loc_12302(): pass

    label('loc_12302')

    OP_71(0x01, 0x5C00, 0x5C7F)
    OP_71(0x01, 0x5C80, 0x5CFF)

    Jump('loc_12321')

    def _loc_12313(): pass

    label('loc_12313')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_12321')

    def _loc_12321(): pass

    label('loc_12321')

    Jump('loc_11731')

    def _loc_12326(): pass

    label('loc_12326')

    Return()

# id: 0x005F offset: 0x12328
@scena.Code('FC_KizunFlagSet_Special')
def FC_KizunFlagSet_Special():
    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '全員の《特別な思い出》１回目のフラグを立てる', 0x000000C9)
    MenuCmd(0x01, 0x01, '全員の《特別な思い出》両方のフラグを立てる', 0x000000CA)
    MenuCmd(0x01, 0x01, 'フラグを消す（キャンセルしても消えています）', 0x000000D1)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)
    MenuCmd(0x10, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x000000CA, 'loc_1243C'),
        (0x000000C9, 'loc_1245D'),
        (-1, 'loc_1247E'),
    )

    def _loc_1243C(): pass

    label('loc_1243C')

    SetScenaFlags(ScenaFlag(0x0B60, 7, 0x5B07))
    SetScenaFlags(ScenaFlag(0x0B63, 6, 0x5B1E))
    SetScenaFlags(ScenaFlag(0x0B65, 1, 0x5B29))
    SetScenaFlags(ScenaFlag(0x0B6F, 4, 0x5B7C))
    SetScenaFlags(ScenaFlag(0x0B67, 1, 0x5B39))
    SetScenaFlags(ScenaFlag(0x0B68, 4, 0x5B44))
    SetScenaFlags(ScenaFlag(0x0B6A, 5, 0x5B55))
    SetScenaFlags(ScenaFlag(0x0B6C, 1, 0x5B61))
    SetScenaFlags(ScenaFlag(0x0B6E, 6, 0x5B76))
    SetScenaFlags(ScenaFlag(0x0B73, 7, 0x5B9F))
    SetScenaFlags(ScenaFlag(0x0B72, 6, 0x5B96))

    def _loc_1245D(): pass

    label('loc_1245D')

    SetScenaFlags(ScenaFlag(0x0B60, 4, 0x5B04))
    SetScenaFlags(ScenaFlag(0x0B63, 0, 0x5B18))
    SetScenaFlags(ScenaFlag(0x0B64, 6, 0x5B26))
    SetScenaFlags(ScenaFlag(0x0B6F, 2, 0x5B7A))
    SetScenaFlags(ScenaFlag(0x0B66, 6, 0x5B36))
    SetScenaFlags(ScenaFlag(0x0B68, 2, 0x5B42))
    SetScenaFlags(ScenaFlag(0x0B6A, 1, 0x5B51))
    SetScenaFlags(ScenaFlag(0x0B6B, 7, 0x5B5F))
    SetScenaFlags(ScenaFlag(0x0B6E, 4, 0x5B74))
    SetScenaFlags(ScenaFlag(0x0B73, 3, 0x5B9B))
    SetScenaFlags(ScenaFlag(0x0B72, 3, 0x5B93))

    def _loc_1247E(): pass

    label('loc_1247E')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1248C')

    def _loc_1248C(): pass

    label('loc_1248C')

    Return()

# id: 0x0060 offset: 0x12490
@scena.Code('EV_KizunaJump_01')
def EV_KizunaJump_01():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12499(): pass

    label('loc_12499')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12A49',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0101_00][ユウナ①発生会話　　　　　　　]', 0x00008000)
    MenuCmd(0x01, 0x02, '[KZ0101_01][ユウナ①ユウナの勉強を見る　　]', 0x00008001)
    MenuCmd(0x01, 0x02, '[KZ0101_02][ユウナ①甲板での語らい　　　　]', 0x00008002)
    MenuCmd(0x01, 0x02, '[KZ0102_00][ユウナ②発生会話　　　　　　　]', 0x00008003)
    MenuCmd(0x01, 0x02, '[KZ0102_01][ユウナ②ボート遊びをする　　　]', 0x00008004)
    MenuCmd(0x01, 0x02, '[KZ0103_00][ユウナ③発生会話　　　　　　　]', 0x00008006)
    MenuCmd(0x01, 0x02, '[KZ0103_01][ユウナ③テニスの練習試合をする]', 0x00008007)
    MenuCmd(0x01, 0x02, '[KZ0104_00][ユウナ・前日譚・誘いを受ける　]', 0x00008009)
    MenuCmd(0x01, 0x02, '[KZ0105_00][ユウナ・前日譚・最終シーン　　]', 0x0000800A)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008000, 'loc_12767'),
        (0x00008001, 'loc_12767'),
        (0x00008002, 'loc_12767'),
        (0x00008003, 'loc_12788'),
        (0x00008004, 'loc_12788'),
        (0x00008006, 'loc_127A9'),
        (0x00008007, 'loc_127A9'),
        (0x00008009, 'loc_127CA'),
        (0x0000800A, 'loc_127CA'),
        (-1, 'loc_127EC'),
    )

    def _loc_12767(): pass

    label('loc_12767')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_127FA')

    def _loc_12788(): pass

    label('loc_12788')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_127FA')

    def _loc_127A9(): pass

    label('loc_127A9')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_127FA')

    def _loc_127CA(): pass

    label('loc_127CA')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_127FA')

    def _loc_127EC(): pass

    label('loc_127EC')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_127FA')

    def _loc_127FA(): pass

    label('loc_127FA')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1281E',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1281E(): pass

    label('loc_1281E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008000, 'loc_1283F'),
        (0x00008003, 'loc_1283F'),
        (0x00008006, 'loc_1283F'),
        (-1, 'loc_128C5'),
    )

    def _loc_1283F(): pass

    label('loc_1283F')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ユウナの前で操作許可にします。\n',
            'ユウナに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_128C5')

    def _loc_128C5(): pass

    label('loc_128C5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_128EE',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_128EE(): pass

    label('loc_128EE')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008000, 'loc_1293F'),
        (0x00008001, 'loc_1295B'),
        (0x00008002, 'loc_12977'),
        (0x00008003, 'loc_12993'),
        (0x00008004, 'loc_129AF'),
        (0x00008006, 'loc_129CB'),
        (0x00008007, 'loc_129E7'),
        (0x00008009, 'loc_12A03'),
        (0x0000800A, 'loc_12A23'),
        (-1, 'loc_12A3F'),
    )

    def _loc_1293F(): pass

    label('loc_1293F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8000, 0x0))

    Jump('loc_12A44')

    def _loc_1295B(): pass

    label('loc_1295B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8001, 0x0))

    Jump('loc_12A44')

    def _loc_12977(): pass

    label('loc_12977')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8002, 0x0))

    Jump('loc_12A44')

    def _loc_12993(): pass

    label('loc_12993')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8003, 0x0))

    Jump('loc_12A44')

    def _loc_129AF(): pass

    label('loc_129AF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8004, 0x0))

    Jump('loc_12A44')

    def _loc_129CB(): pass

    label('loc_129CB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8006, 0x0))

    Jump('loc_12A44')

    def _loc_129E7(): pass

    label('loc_129E7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8007, 0x0))

    Jump('loc_12A44')

    def _loc_12A03(): pass

    label('loc_12A03')

    FormationAddMember(ChrTable['悠娜'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8009, 0x0))

    Jump('loc_12A44')

    def _loc_12A23(): pass

    label('loc_12A23')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x800A, 0x0))

    Jump('loc_12A44')

    def _loc_12A3F(): pass

    label('loc_12A3F')

    Jump('loc_12A44')

    def _loc_12A44(): pass

    label('loc_12A44')

    Jump('loc_12499')

    def _loc_12A49(): pass

    label('loc_12A49')

    Return()

# id: 0x0061 offset: 0x12A4C
@scena.Code('EV_KizunaJump_02')
def EV_KizunaJump_02():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12A55(): pass

    label('loc_12A55')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12F45',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0201_00][クルト①発生会話　　　　　　　]', 0x00008010)
    MenuCmd(0x01, 0x02, '[KZ0201_01][クルト①質屋に向かう　　　　　]', 0x00008011)
    MenuCmd(0x01, 0x02, '[KZ0201_02][クルト①ロランの左手剣を発見　]', 0x00008012)
    MenuCmd(0x01, 0x02, '[KZ0201_03][クルト①先祖の想いに触れる　　]', 0x00008013)
    MenuCmd(0x01, 0x02, '[KZ0202_00][クルト②発生会話　　　　　　　]', 0x00008015)
    MenuCmd(0x01, 0x02, '[KZ0202_01][クルト②パルムの道場前に来る　]', 0x00008016)
    MenuCmd(0x01, 0x02, '[KZ0202_02][クルト②ミュラーとの立会い　　]', 0x00008017)
    MenuCmd(0x01, 0x02, '[KZ0203_00][クルト・アトラクション後　　　]', 0x00008019)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008010, 'loc_12CD9'),
        (0x00008011, 'loc_12CD9'),
        (0x00008012, 'loc_12CD9'),
        (0x00008013, 'loc_12CD9'),
        (0x00008015, 'loc_12CFA'),
        (0x00008016, 'loc_12CFA'),
        (0x00008017, 'loc_12CFA'),
        (0x00008019, 'loc_12D1B'),
        (-1, 'loc_12D3D'),
    )

    def _loc_12CD9(): pass

    label('loc_12CD9')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_12D4B')

    def _loc_12CFA(): pass

    label('loc_12CFA')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_12D4B')

    def _loc_12D1B(): pass

    label('loc_12D1B')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_12D4B')

    def _loc_12D3D(): pass

    label('loc_12D3D')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_12D4B')

    def _loc_12D4B(): pass

    label('loc_12D4B')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12D6F',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_12D6F(): pass

    label('loc_12D6F')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008010, 'loc_12D88'),
        (0x00008015, 'loc_12D88'),
        (-1, 'loc_12E0E'),
    )

    def _loc_12D88(): pass

    label('loc_12D88')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'クルトの前で操作許可にします。\n',
            'クルトに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_12E0E')

    def _loc_12E0E(): pass

    label('loc_12E0E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008010, 'loc_12E57'),
        (0x00008011, 'loc_12E73'),
        (0x00008012, 'loc_12E8F'),
        (0x00008013, 'loc_12EAB'),
        (0x00008015, 'loc_12EC7'),
        (0x00008016, 'loc_12EE3'),
        (0x00008017, 'loc_12EFF'),
        (0x00008019, 'loc_12F1B'),
        (-1, 'loc_12F3B'),
    )

    def _loc_12E57(): pass

    label('loc_12E57')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8010, 0x0))

    Jump('loc_12F40')

    def _loc_12E73(): pass

    label('loc_12E73')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8011, 0x0))

    Jump('loc_12F40')

    def _loc_12E8F(): pass

    label('loc_12E8F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8012, 0x0))

    Jump('loc_12F40')

    def _loc_12EAB(): pass

    label('loc_12EAB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8013, 0x0))

    Jump('loc_12F40')

    def _loc_12EC7(): pass

    label('loc_12EC7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8015, 0x0))

    Jump('loc_12F40')

    def _loc_12EE3(): pass

    label('loc_12EE3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8016, 0x0))

    Jump('loc_12F40')

    def _loc_12EFF(): pass

    label('loc_12EFF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8017, 0x0))

    Jump('loc_12F40')

    def _loc_12F1B(): pass

    label('loc_12F1B')

    FormationAddMember(ChrTable['庫爾特'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8019, 0x0))

    Jump('loc_12F40')

    def _loc_12F3B(): pass

    label('loc_12F3B')

    Jump('loc_12F40')

    def _loc_12F40(): pass

    label('loc_12F40')

    Jump('loc_12A55')

    def _loc_12F45(): pass

    label('loc_12F45')

    Return()

# id: 0x0062 offset: 0x12F48
@scena.Code('EV_KizunaJump_03')
def EV_KizunaJump_03():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12F51(): pass

    label('loc_12F51')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_135E1',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0301_00][アルティナ①発生会話　　　　　]', 0x00008020)
    MenuCmd(0x01, 0x02, '[KZ0301_01][アルティナ①ハッキングする　　]', 0x00008021)
    MenuCmd(0x01, 0x02, '[KZ0302_00][アルティナ②発生イベント　　　]', 0x00008022)
    MenuCmd(0x01, 0x02, '[KZ0302_01][アルティナ②アルティナを助ける]', 0x00008023)
    MenuCmd(0x01, 0x02, '[KZ0303_00][アルティナ③ジョルジュの聯絡　]', 0x00008025)
    MenuCmd(0x01, 0x02, '[KZ0303_01][アルティナ③発生会話　　　　　]', 0x00008026)
    MenuCmd(0x01, 0x02, '[KZ0303_02][アルティナ③黒の工房の探索開始]', 0x00008027)
    MenuCmd(0x01, 0x02, '[KZ0303_03][アルティナ③培養槽エリアを探索]', 0x00008028)
    MenuCmd(0x01, 0x02, '[KZ0303_04][アルティナ③空の培養槽を発見　]', 0x00008029)
    MenuCmd(0x01, 0x02, '[KZ0304_00][アルティナ・前日譚・誘われる　]', 0x0000802B)
    MenuCmd(0x01, 0x02, '[KZ0305_00][アルティナ・前日譚・最終シーン]', 0x0000802C)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008020, 'loc_132B3'),
        (0x00008021, 'loc_132B3'),
        (0x00008022, 'loc_132D4'),
        (0x00008023, 'loc_132D4'),
        (0x00008025, 'loc_132F5'),
        (0x00008026, 'loc_132F5'),
        (0x00008027, 'loc_132F5'),
        (0x00008028, 'loc_132F5'),
        (0x00008029, 'loc_132F5'),
        (0x0000802B, 'loc_13316'),
        (0x0000802C, 'loc_13316'),
        (-1, 'loc_13338'),
    )

    def _loc_132B3(): pass

    label('loc_132B3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_13346')

    def _loc_132D4(): pass

    label('loc_132D4')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_13346')

    def _loc_132F5(): pass

    label('loc_132F5')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_13346')

    def _loc_13316(): pass

    label('loc_13316')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_13346')

    def _loc_13338(): pass

    label('loc_13338')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_13346')

    def _loc_13346(): pass

    label('loc_13346')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1336A',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1336A(): pass

    label('loc_1336A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008020, 'loc_13383'),
        (0x00008026, 'loc_13383'),
        (-1, 'loc_13415'),
    )

    def _loc_13383(): pass

    label('loc_13383')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'アルティナの前で操作許可にします。\n',
            'アルティナに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_13415')

    def _loc_13415(): pass

    label('loc_13415')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1343E',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_1343E(): pass

    label('loc_1343E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008020, 'loc_1349F'),
        (0x00008021, 'loc_134BB'),
        (0x00008022, 'loc_134D7'),
        (0x00008023, 'loc_134F3'),
        (0x00008025, 'loc_1350F'),
        (0x00008026, 'loc_1352B'),
        (0x00008027, 'loc_13547'),
        (0x00008028, 'loc_13563'),
        (0x00008029, 'loc_1357F'),
        (0x0000802B, 'loc_1359B'),
        (0x0000802C, 'loc_135BB'),
        (-1, 'loc_135D7'),
    )

    def _loc_1349F(): pass

    label('loc_1349F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8020, 0x0))

    Jump('loc_135DC')

    def _loc_134BB(): pass

    label('loc_134BB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8021, 0x0))

    Jump('loc_135DC')

    def _loc_134D7(): pass

    label('loc_134D7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8022, 0x0))

    Jump('loc_135DC')

    def _loc_134F3(): pass

    label('loc_134F3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8023, 0x0))

    Jump('loc_135DC')

    def _loc_1350F(): pass

    label('loc_1350F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8025, 0x0))

    Jump('loc_135DC')

    def _loc_1352B(): pass

    label('loc_1352B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8026, 0x0))

    Jump('loc_135DC')

    def _loc_13547(): pass

    label('loc_13547')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8027, 0x0))

    Jump('loc_135DC')

    def _loc_13563(): pass

    label('loc_13563')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8028, 0x0))

    Jump('loc_135DC')

    def _loc_1357F(): pass

    label('loc_1357F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8029, 0x0))

    Jump('loc_135DC')

    def _loc_1359B(): pass

    label('loc_1359B')

    FormationAddMember(ChrTable['亞爾緹娜'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x802B, 0x0))

    Jump('loc_135DC')

    def _loc_135BB(): pass

    label('loc_135BB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x802C, 0x0))

    Jump('loc_135DC')

    def _loc_135D7(): pass

    label('loc_135D7')

    Jump('loc_135DC')

    def _loc_135DC(): pass

    label('loc_135DC')

    Jump('loc_12F51')

    def _loc_135E1(): pass

    label('loc_135E1')

    Return()

# id: 0x0063 offset: 0x135E4
@scena.Code('EV_KizunaJump_04')
def EV_KizunaJump_04():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_135ED(): pass

    label('loc_135ED')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13B95',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0401_00][ミュゼ①小型銃を見る　　　　　]', 0x00008030)
    MenuCmd(0x01, 0x02, '[KZ0401_01][ミュゼ①発生イベント　　　　　]', 0x00008031)
    MenuCmd(0x01, 0x02, '[KZ0401_02][ミュゼ①ビデオ通信を目撃する　]', 0x00008032)
    MenuCmd(0x01, 0x02, '[KZ0402_00][ミュゼ②発生会話　　　　　　　]', 0x00008033)
    MenuCmd(0x01, 0x02, '[KZ0402_01][ミュゼ②野点を行う　　　　　　]', 0x00008034)
    MenuCmd(0x01, 0x02, '[KZ0403_00][ミュゼ③発生会話　　　　　　　]', 0x00008036)
    MenuCmd(0x01, 0x02, '[KZ0403_01][ミュゼ③海水浴をする　　　　　]', 0x00008037)
    MenuCmd(0x01, 0x02, '[KZ0404_00][ミュゼ・前日譚・誘いを受ける　]', 0x00008039)
    MenuCmd(0x01, 0x02, '[KZ0405_00][ミュゼ・前日譚・最終シーン　　]', 0x0000803A)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008030, 'loc_138BB'),
        (0x00008031, 'loc_138BB'),
        (0x00008032, 'loc_138BB'),
        (0x00008033, 'loc_138DC'),
        (0x00008034, 'loc_138DC'),
        (0x00008036, 'loc_138FD'),
        (0x00008037, 'loc_138FD'),
        (0x00008039, 'loc_1391E'),
        (0x0000803A, 'loc_1391E'),
        (-1, 'loc_13940'),
    )

    def _loc_138BB(): pass

    label('loc_138BB')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_1394E')

    def _loc_138DC(): pass

    label('loc_138DC')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_1394E')

    def _loc_138FD(): pass

    label('loc_138FD')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_1394E')

    def _loc_1391E(): pass

    label('loc_1391E')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_1394E')

    def _loc_13940(): pass

    label('loc_13940')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1394E')

    def _loc_1394E(): pass

    label('loc_1394E')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13972',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_13972(): pass

    label('loc_13972')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008033, 'loc_1398B'),
        (0x00008036, 'loc_1398B'),
        (-1, 'loc_13A11'),
    )

    def _loc_1398B(): pass

    label('loc_1398B')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ミュゼの前で操作許可にします。\n',
            'ミュゼに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_13A11')

    def _loc_13A11(): pass

    label('loc_13A11')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13A3A',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_13A3A(): pass

    label('loc_13A3A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008030, 'loc_13A8B'),
        (0x00008031, 'loc_13AA7'),
        (0x00008032, 'loc_13AC3'),
        (0x00008033, 'loc_13ADF'),
        (0x00008034, 'loc_13AFB'),
        (0x00008036, 'loc_13B17'),
        (0x00008037, 'loc_13B33'),
        (0x00008039, 'loc_13B4F'),
        (0x0000803A, 'loc_13B6F'),
        (-1, 'loc_13B8B'),
    )

    def _loc_13A8B(): pass

    label('loc_13A8B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8030, 0x0))

    Jump('loc_13B90')

    def _loc_13AA7(): pass

    label('loc_13AA7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8031, 0x0))

    Jump('loc_13B90')

    def _loc_13AC3(): pass

    label('loc_13AC3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8032, 0x0))

    Jump('loc_13B90')

    def _loc_13ADF(): pass

    label('loc_13ADF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8033, 0x0))

    Jump('loc_13B90')

    def _loc_13AFB(): pass

    label('loc_13AFB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8034, 0x0))

    Jump('loc_13B90')

    def _loc_13B17(): pass

    label('loc_13B17')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8036, 0x0))

    Jump('loc_13B90')

    def _loc_13B33(): pass

    label('loc_13B33')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8037, 0x0))

    Jump('loc_13B90')

    def _loc_13B4F(): pass

    label('loc_13B4F')

    FormationAddMember(ChrTable['妙婕'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8039, 0x0))

    Jump('loc_13B90')

    def _loc_13B6F(): pass

    label('loc_13B6F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x803A, 0x0))

    Jump('loc_13B90')

    def _loc_13B8B(): pass

    label('loc_13B8B')

    Jump('loc_13B90')

    def _loc_13B90(): pass

    label('loc_13B90')

    Jump('loc_135ED')

    def _loc_13B95(): pass

    label('loc_13B95')

    Return()

# id: 0x0064 offset: 0x13B98
@scena.Code('EV_KizunaJump_05')
def EV_KizunaJump_05():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13BA1(): pass

    label('loc_13BA1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13FBB',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0501_00][アッシュ①発生会話　　　　　　]', 0x00008040)
    MenuCmd(0x01, 0x02, '[KZ0501_01][アッシュ①実家の掃除をする　　]', 0x00008041)
    MenuCmd(0x01, 0x02, '[KZ0502_00][アッシュ②発生会話　　　　　　]', 0x00008043)
    MenuCmd(0x01, 0x02, '[KZ0502_01][アッシュ②ブラッドに事情を聞く]', 0x00008044)
    MenuCmd(0x01, 0x02, '[KZ0502_02][アッシュ②過去にけじめをつける]', 0x00008045)
    MenuCmd(0x01, 0x02, '[KZ0503_00][アッシュ・アトラクション後　　]', 0x00008047)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008040, 'loc_13D91'),
        (0x00008041, 'loc_13D91'),
        (0x00008043, 'loc_13DB2'),
        (0x00008044, 'loc_13DB2'),
        (0x00008045, 'loc_13DB2'),
        (0x00008047, 'loc_13DD3'),
        (-1, 'loc_13DF5'),
    )

    def _loc_13D91(): pass

    label('loc_13D91')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_13E03')

    def _loc_13DB2(): pass

    label('loc_13DB2')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_13E03')

    def _loc_13DD3(): pass

    label('loc_13DD3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_13E03')

    def _loc_13DF5(): pass

    label('loc_13DF5')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_13E03')

    def _loc_13E03(): pass

    label('loc_13E03')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13E27',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_13E27(): pass

    label('loc_13E27')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008040, 'loc_13E40'),
        (0x00008043, 'loc_13E40'),
        (-1, 'loc_13ECC'),
    )

    def _loc_13E40(): pass

    label('loc_13E40')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'アッシュの前で操作許可にします。\n',
            'アッシュに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_13ECC')

    def _loc_13ECC(): pass

    label('loc_13ECC')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008040, 'loc_13F05'),
        (0x00008041, 'loc_13F21'),
        (0x00008043, 'loc_13F3D'),
        (0x00008044, 'loc_13F59'),
        (0x00008045, 'loc_13F75'),
        (0x00008047, 'loc_13F91'),
        (-1, 'loc_13FB1'),
    )

    def _loc_13F05(): pass

    label('loc_13F05')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8040, 0x0))

    Jump('loc_13FB6')

    def _loc_13F21(): pass

    label('loc_13F21')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8041, 0x0))

    Jump('loc_13FB6')

    def _loc_13F3D(): pass

    label('loc_13F3D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8043, 0x0))

    Jump('loc_13FB6')

    def _loc_13F59(): pass

    label('loc_13F59')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8044, 0x0))

    Jump('loc_13FB6')

    def _loc_13F75(): pass

    label('loc_13F75')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8045, 0x0))

    Jump('loc_13FB6')

    def _loc_13F91(): pass

    label('loc_13F91')

    FormationAddMember(ChrTable['亞修'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8047, 0x0))

    Jump('loc_13FB6')

    def _loc_13FB1(): pass

    label('loc_13FB1')

    Jump('loc_13FB6')

    def _loc_13FB6(): pass

    label('loc_13FB6')

    Jump('loc_13BA1')

    def _loc_13FBB(): pass

    label('loc_13FBB')

    Return()

# id: 0x0065 offset: 0x13FBC
@scena.Code('EV_KizunaJump_06')
def EV_KizunaJump_06():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13FC5(): pass

    label('loc_13FC5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14470',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0601_00][アリサ①発生会話　　　　　　　]', 0x00008050)
    MenuCmd(0x01, 0x02, '[KZ0601_01][アリサ①ＥＸＡの整備を手伝う　]', 0x00008051)
    MenuCmd(0x01, 0x02, '[KZ0602_00][アリサ②発生会話　　　　　　　]', 0x00008052)
    MenuCmd(0x01, 0x02, '[KZ0602_01][アリサ②ＲＦ本社ビルに向かう　]', 0x00008053)
    MenuCmd(0x01, 0x02, '[KZ0602_02][アリサ②第五の調査を行う　　　]', 0x00008054)
    MenuCmd(0x01, 0x02, '[KZ0603_00][アリサ・前日譚・約束をする　　]', 0x00008055)
    MenuCmd(0x01, 0x02, '[KZ0604_00][アリサ・前日譚・最終シーン　　]', 0x00008056)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008050, 'loc_141FF'),
        (0x00008051, 'loc_141FF'),
        (0x00008052, 'loc_14220'),
        (0x00008053, 'loc_14220'),
        (0x00008054, 'loc_14220'),
        (0x00008055, 'loc_14241'),
        (0x00008056, 'loc_14241'),
        (-1, 'loc_14263'),
    )

    def _loc_141FF(): pass

    label('loc_141FF')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_14271')

    def _loc_14220(): pass

    label('loc_14220')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_14271')

    def _loc_14241(): pass

    label('loc_14241')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_14271')

    def _loc_14263(): pass

    label('loc_14263')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_14271')

    def _loc_14271(): pass

    label('loc_14271')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14295',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_14295(): pass

    label('loc_14295')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008050, 'loc_142AE'),
        (0x00008052, 'loc_142AE'),
        (-1, 'loc_14334'),
    )

    def _loc_142AE(): pass

    label('loc_142AE')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'アリサの前で操作許可にします。\n',
            'アリサに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_14334')

    def _loc_14334(): pass

    label('loc_14334')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1435D',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_1435D(): pass

    label('loc_1435D')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008050, 'loc_1439E'),
        (0x00008051, 'loc_143BA'),
        (0x00008052, 'loc_143D6'),
        (0x00008053, 'loc_143F2'),
        (0x00008054, 'loc_1440E'),
        (0x00008055, 'loc_1442A'),
        (0x00008056, 'loc_1444A'),
        (-1, 'loc_14466'),
    )

    def _loc_1439E(): pass

    label('loc_1439E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8050, 0x0))

    Jump('loc_1446B')

    def _loc_143BA(): pass

    label('loc_143BA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8051, 0x0))

    Jump('loc_1446B')

    def _loc_143D6(): pass

    label('loc_143D6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8052, 0x0))

    Jump('loc_1446B')

    def _loc_143F2(): pass

    label('loc_143F2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8053, 0x0))

    Jump('loc_1446B')

    def _loc_1440E(): pass

    label('loc_1440E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8054, 0x0))

    Jump('loc_1446B')

    def _loc_1442A(): pass

    label('loc_1442A')

    FormationAddMember(ChrTable['亞莉莎'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8055, 0x0))

    Jump('loc_1446B')

    def _loc_1444A(): pass

    label('loc_1444A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8056, 0x0))

    Jump('loc_1446B')

    def _loc_14466(): pass

    label('loc_14466')

    Jump('loc_1446B')

    def _loc_1446B(): pass

    label('loc_1446B')

    Jump('loc_13FC5')

    def _loc_14470(): pass

    label('loc_14470')

    Return()

# id: 0x0066 offset: 0x14474
@scena.Code('EV_KizunaJump_07')
def EV_KizunaJump_07():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1447D(): pass

    label('loc_1447D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14798',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0701_00][エリオット①発生会話　　　　　]', 0x00008060)
    MenuCmd(0x01, 0x02, '[KZ0701_01][エリオット①ラジオ放送を聴く　]', 0x00008061)
    MenuCmd(0x01, 0x02, '[KZ0701_02][エリオット①二人の目を覚ます　]', 0x00008062)
    MenuCmd(0x01, 0x02, '[KZ0702_00][エリオット・アトラクション後　]', 0x00008064)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008060, 'loc_145D9'),
        (0x00008061, 'loc_145D9'),
        (0x00008062, 'loc_145D9'),
        (0x00008064, 'loc_145FA'),
        (-1, 'loc_1461C'),
    )

    def _loc_145D9(): pass

    label('loc_145D9')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_1462A')

    def _loc_145FA(): pass

    label('loc_145FA')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_1462A')

    def _loc_1461C(): pass

    label('loc_1461C')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1462A')

    def _loc_1462A(): pass

    label('loc_1462A')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1464E',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1464E(): pass

    label('loc_1464E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008060, 'loc_1465F'),
        (-1, 'loc_146F1'),
    )

    def _loc_1465F(): pass

    label('loc_1465F')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'エリオットの前で操作許可にします。\n',
            'エリオットに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_146F1')

    def _loc_146F1(): pass

    label('loc_146F1')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008060, 'loc_1471A'),
        (0x00008061, 'loc_14736'),
        (0x00008062, 'loc_14752'),
        (0x00008064, 'loc_1476E'),
        (-1, 'loc_1478E'),
    )

    def _loc_1471A(): pass

    label('loc_1471A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8060, 0x0))

    Jump('loc_14793')

    def _loc_14736(): pass

    label('loc_14736')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8061, 0x0))

    Jump('loc_14793')

    def _loc_14752(): pass

    label('loc_14752')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8062, 0x0))

    Jump('loc_14793')

    def _loc_1476E(): pass

    label('loc_1476E')

    FormationAddMember(ChrTable['艾略特'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8064, 0x0))

    Jump('loc_14793')

    def _loc_1478E(): pass

    label('loc_1478E')

    Jump('loc_14793')

    def _loc_14793(): pass

    label('loc_14793')

    Jump('loc_1447D')

    def _loc_14798(): pass

    label('loc_14798')

    Return()

# id: 0x0067 offset: 0x1479C
@scena.Code('EV_KizunaJump_08')
def EV_KizunaJump_08():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_147A5(): pass

    label('loc_147A5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14BE2',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0801_00][ラウラ①発生会話　　　　　　　]', 0x00008070)
    MenuCmd(0x01, 0x02, '[KZ0801_01][ラウラ①日帰り修行をする　　　]', 0x00008071)
    MenuCmd(0x01, 0x02, '[KZ0802_00][ラウラ②発生会話　　　　　　　]', 0x00008072)
    MenuCmd(0x01, 0x02, '[KZ0802_01][ラウラ②ラウラが奥義を極める　]', 0x00008073)
    MenuCmd(0x01, 0x02, '[KZ0803_00][ラウラ・前日譚・約束をする　　]', 0x00008074)
    MenuCmd(0x01, 0x02, '[KZ0804_00][ラウラ・前日譚・最終シーン　　]', 0x00008075)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008070, 'loc_14995'),
        (0x00008071, 'loc_14995'),
        (0x00008072, 'loc_149B6'),
        (0x00008073, 'loc_149B6'),
        (0x00008074, 'loc_149D7'),
        (0x00008075, 'loc_149D7'),
        (-1, 'loc_149F9'),
    )

    def _loc_14995(): pass

    label('loc_14995')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_14A07')

    def _loc_149B6(): pass

    label('loc_149B6')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_14A07')

    def _loc_149D7(): pass

    label('loc_149D7')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_14A07')

    def _loc_149F9(): pass

    label('loc_149F9')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_14A07')

    def _loc_14A07(): pass

    label('loc_14A07')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14A2B',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_14A2B(): pass

    label('loc_14A2B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008070, 'loc_14A44'),
        (0x00008072, 'loc_14A44'),
        (-1, 'loc_14ACA'),
    )

    def _loc_14A44(): pass

    label('loc_14A44')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ラウラの前で操作許可にします。\n',
            'ラウラに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_14ACA')

    def _loc_14ACA(): pass

    label('loc_14ACA')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14AF3',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_14AF3(): pass

    label('loc_14AF3')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008070, 'loc_14B2C'),
        (0x00008071, 'loc_14B48'),
        (0x00008072, 'loc_14B64'),
        (0x00008073, 'loc_14B80'),
        (0x00008074, 'loc_14B9C'),
        (0x00008075, 'loc_14BBC'),
        (-1, 'loc_14BD8'),
    )

    def _loc_14B2C(): pass

    label('loc_14B2C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8070, 0x0))

    Jump('loc_14BDD')

    def _loc_14B48(): pass

    label('loc_14B48')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8071, 0x0))

    Jump('loc_14BDD')

    def _loc_14B64(): pass

    label('loc_14B64')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8072, 0x0))

    Jump('loc_14BDD')

    def _loc_14B80(): pass

    label('loc_14B80')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8073, 0x0))

    Jump('loc_14BDD')

    def _loc_14B9C(): pass

    label('loc_14B9C')

    FormationAddMember(ChrTable['勞拉'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8074, 0x0))

    Jump('loc_14BDD')

    def _loc_14BBC(): pass

    label('loc_14BBC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8075, 0x0))

    Jump('loc_14BDD')

    def _loc_14BD8(): pass

    label('loc_14BD8')

    Jump('loc_14BDD')

    def _loc_14BDD(): pass

    label('loc_14BDD')

    Jump('loc_147A5')

    def _loc_14BE2(): pass

    label('loc_14BE2')

    Return()

# id: 0x0068 offset: 0x14BE4
@scena.Code('EV_KizunaJump_09')
def EV_KizunaJump_09():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_14BED(): pass

    label('loc_14BED')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14EFF',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0901_00][マキアス①発生会話　　　　　　]', 0x00008080)
    MenuCmd(0x01, 0x02, '[KZ0901_01][マキアス①知事から話を聞く　　]', 0x00008081)
    MenuCmd(0x01, 0x02, '[KZ0901_02][マキアス①アーサーと対峙する]', 0x00008082)
    MenuCmd(0x01, 0x02, '[KZ0902_00][マキアス・アトラクション後　　]', 0x00008084)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008080, 'loc_14D46'),
        (0x00008081, 'loc_14D46'),
        (0x00008082, 'loc_14D46'),
        (0x00008084, 'loc_14D67'),
        (-1, 'loc_14D89'),
    )

    def _loc_14D46(): pass

    label('loc_14D46')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_14D97')

    def _loc_14D67(): pass

    label('loc_14D67')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_14D97')

    def _loc_14D89(): pass

    label('loc_14D89')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_14D97')

    def _loc_14D97(): pass

    label('loc_14D97')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14DBB',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_14DBB(): pass

    label('loc_14DBB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008080, 'loc_14DCC'),
        (-1, 'loc_14E58'),
    )

    def _loc_14DCC(): pass

    label('loc_14DCC')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'マキアスの前で操作許可にします。\n',
            'マキアスに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_14E58')

    def _loc_14E58(): pass

    label('loc_14E58')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008080, 'loc_14E81'),
        (0x00008081, 'loc_14E9D'),
        (0x00008082, 'loc_14EB9'),
        (0x00008084, 'loc_14ED5'),
        (-1, 'loc_14EF5'),
    )

    def _loc_14E81(): pass

    label('loc_14E81')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8080, 0x0))

    Jump('loc_14EFA')

    def _loc_14E9D(): pass

    label('loc_14E9D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8081, 0x0))

    Jump('loc_14EFA')

    def _loc_14EB9(): pass

    label('loc_14EB9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8082, 0x0))

    Jump('loc_14EFA')

    def _loc_14ED5(): pass

    label('loc_14ED5')

    FormationAddMember(ChrTable['馬奇亞斯'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8084, 0x0))

    Jump('loc_14EFA')

    def _loc_14EF5(): pass

    label('loc_14EF5')

    Jump('loc_14EFA')

    def _loc_14EFA(): pass

    label('loc_14EFA')

    Jump('loc_14BED')

    def _loc_14EFF(): pass

    label('loc_14EFF')

    Return()

# id: 0x0069 offset: 0x14F00
@scena.Code('EV_KizunaJump_10')
def EV_KizunaJump_10():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_14F09(): pass

    label('loc_14F09')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15592',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1001_00][エマ①発生会話　　　　　　　　]', 0x00008090)
    MenuCmd(0x01, 0x02, '[KZ1001_01][エマ①ロゼのアトリエに向かう　]', 0x00008091)
    MenuCmd(0x01, 0x02, '[KZ1001_02][エマ①リィンの呪い解呪を試みる]', 0x00008092)
    MenuCmd(0x01, 0x02, '[KZ1001_04][エマ①アトリエを飛び出す　　　]', 0x00008094)
    MenuCmd(0x01, 0x02, '[KZ1001_05][エマ①転位石前での語らい　　　]', 0x00008095)
    MenuCmd(0x01, 0x02, '[KZ1002_00][エマ②発生会話　　　　　　　　]', 0x00008096)
    MenuCmd(0x01, 0x02, '[KZ1002_01][エマ②術を唱える　　　　　　　]', 0x00008097)
    MenuCmd(0x01, 0x02, '[KZ1002_02][エマ②精神世界に潜行　　　　　]', 0x00008098)
    MenuCmd(0x01, 0x02, '[KZ1002_03][エマ②医務室での語らい　　　　]', 0x00008099)
    MenuCmd(0x01, 0x02, '[KZ1003_00][エマ・前日譚・約束をする　　　]', 0x0000809A)
    MenuCmd(0x01, 0x02, '[KZ1004_00][エマ・前日譚・最終シーン　　　]', 0x0000809B)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008090, 'loc_15273'),
        (0x00008091, 'loc_15273'),
        (0x00008092, 'loc_15273'),
        (0x00008093, 'loc_15273'),
        (0x00008094, 'loc_15273'),
        (0x00008095, 'loc_15273'),
        (0x00008096, 'loc_15294'),
        (0x00008097, 'loc_15294'),
        (0x00008098, 'loc_15294'),
        (0x00008099, 'loc_15294'),
        (0x0000809A, 'loc_152B5'),
        (0x0000809B, 'loc_152B5'),
        (-1, 'loc_152D7'),
    )

    def _loc_15273(): pass

    label('loc_15273')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_152E5')

    def _loc_15294(): pass

    label('loc_15294')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_152E5')

    def _loc_152B5(): pass

    label('loc_152B5')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_152E5')

    def _loc_152D7(): pass

    label('loc_152D7')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_152E5')

    def _loc_152E5(): pass

    label('loc_152E5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15309',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_15309(): pass

    label('loc_15309')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008090, 'loc_15322'),
        (0x00008096, 'loc_15322'),
        (-1, 'loc_153A2'),
    )

    def _loc_15322(): pass

    label('loc_15322')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'エマの前で操作許可にします。\n',
            'エマに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_153A2')

    def _loc_153A2(): pass

    label('loc_153A2')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_153CB',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_153CB(): pass

    label('loc_153CB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008090, 'loc_15434'),
        (0x00008091, 'loc_15450'),
        (0x00008092, 'loc_1546C'),
        (0x00008093, 'loc_15488'),
        (0x00008094, 'loc_154A4'),
        (0x00008095, 'loc_154C0'),
        (0x00008096, 'loc_154DC'),
        (0x00008097, 'loc_154F8'),
        (0x00008098, 'loc_15514'),
        (0x00008099, 'loc_15530'),
        (0x0000809A, 'loc_1554C'),
        (0x0000809B, 'loc_1556C'),
        (-1, 'loc_15588'),
    )

    def _loc_15434(): pass

    label('loc_15434')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8090, 0x0))

    Jump('loc_1558D')

    def _loc_15450(): pass

    label('loc_15450')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8091, 0x0))

    Jump('loc_1558D')

    def _loc_1546C(): pass

    label('loc_1546C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8092, 0x0))

    Jump('loc_1558D')

    def _loc_15488(): pass

    label('loc_15488')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8093, 0x0))

    Jump('loc_1558D')

    def _loc_154A4(): pass

    label('loc_154A4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8094, 0x0))

    Jump('loc_1558D')

    def _loc_154C0(): pass

    label('loc_154C0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8095, 0x0))

    Jump('loc_1558D')

    def _loc_154DC(): pass

    label('loc_154DC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8096, 0x0))

    Jump('loc_1558D')

    def _loc_154F8(): pass

    label('loc_154F8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8097, 0x0))

    Jump('loc_1558D')

    def _loc_15514(): pass

    label('loc_15514')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8098, 0x0))

    Jump('loc_1558D')

    def _loc_15530(): pass

    label('loc_15530')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8099, 0x0))

    Jump('loc_1558D')

    def _loc_1554C(): pass

    label('loc_1554C')

    FormationAddMember(ChrTable['艾瑪'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x809A, 0x0))

    Jump('loc_1558D')

    def _loc_1556C(): pass

    label('loc_1556C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x809B, 0x0))

    Jump('loc_1558D')

    def _loc_15588(): pass

    label('loc_15588')

    Jump('loc_1558D')

    def _loc_1558D(): pass

    label('loc_1558D')

    Jump('loc_14F09')

    def _loc_15592(): pass

    label('loc_15592')

    Return()

# id: 0x006A offset: 0x15594
@scena.Code('EV_KizunaJump_11')
def EV_KizunaJump_11():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1559D(): pass

    label('loc_1559D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_158B2',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1101_00][ユーシス①発生会話　　　　　　]', 0x000080A0)
    MenuCmd(0x01, 0x02, '[KZ1101_01][ユーシス①アルノー達と再会する]', 0x000080A1)
    MenuCmd(0x01, 0x02, '[KZ1101_02][ユーシス①書類整理を手伝う　　]', 0x000080A2)
    MenuCmd(0x01, 0x02, '[KZ1102_00][ユーシス・アトラクション後　　]', 0x000080A4)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080A0, 'loc_156F9'),
        (0x000080A1, 'loc_156F9'),
        (0x000080A2, 'loc_156F9'),
        (0x000080A4, 'loc_1571A'),
        (-1, 'loc_1573C'),
    )

    def _loc_156F9(): pass

    label('loc_156F9')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_1574A')

    def _loc_1571A(): pass

    label('loc_1571A')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_1574A')

    def _loc_1573C(): pass

    label('loc_1573C')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1574A')

    def _loc_1574A(): pass

    label('loc_1574A')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1576E',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1576E(): pass

    label('loc_1576E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080A0, 'loc_1577F'),
        (-1, 'loc_1580B'),
    )

    def _loc_1577F(): pass

    label('loc_1577F')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ユーシスの前で操作許可にします。\n',
            'ユーシスに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_1580B')

    def _loc_1580B(): pass

    label('loc_1580B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080A0, 'loc_15834'),
        (0x000080A1, 'loc_15850'),
        (0x000080A2, 'loc_1586C'),
        (0x000080A4, 'loc_15888'),
        (-1, 'loc_158A8'),
    )

    def _loc_15834(): pass

    label('loc_15834')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80A0, 0x0))

    Jump('loc_158AD')

    def _loc_15850(): pass

    label('loc_15850')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80A1, 0x0))

    Jump('loc_158AD')

    def _loc_1586C(): pass

    label('loc_1586C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80A2, 0x0))

    Jump('loc_158AD')

    def _loc_15888(): pass

    label('loc_15888')

    FormationAddMember(ChrTable['尤西斯'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80A4, 0x0))

    Jump('loc_158AD')

    def _loc_158A8(): pass

    label('loc_158A8')

    Jump('loc_158AD')

    def _loc_158AD(): pass

    label('loc_158AD')

    Jump('loc_1559D')

    def _loc_158B2(): pass

    label('loc_158B2')

    Return()

# id: 0x006B offset: 0x158B4
@scena.Code('EV_KizunaJump_12')
def EV_KizunaJump_12():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_158BD(): pass

    label('loc_158BD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15D7D',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1201_00][フィー①発生会話　　　　　　　]　', 0x000080B0)
    MenuCmd(0x01, 0x02, '[KZ1201_01][フィー①模擬戦を行う　　　　　]戦', 0x000080B1)
    MenuCmd(0x01, 0x02, '[KZ1201_02][フィー①模擬戦後の語らい　　　]　', 0x000080B2)
    MenuCmd(0x01, 0x02, '[KZ1202_00][フィー②発生会話　　　　　　　]　', 0x000080B3)
    MenuCmd(0x01, 0x02, '[KZ1202_01][フィー②墓参りをする　　　　　]　', 0x000080B4)
    MenuCmd(0x01, 0x02, '[KZ1203_00][フィー・前日譚・約束をする　　]　', 0x000080B5)
    MenuCmd(0x01, 0x02, '[KZ1204_00][フィー・前日譚・最終シーン　　]　', 0x000080B6)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080B0, 'loc_15B0C'),
        (0x000080B1, 'loc_15B0C'),
        (0x000080B2, 'loc_15B0C'),
        (0x000080B3, 'loc_15B2D'),
        (0x000080B4, 'loc_15B2D'),
        (0x000080B5, 'loc_15B4E'),
        (0x000080B6, 'loc_15B4E'),
        (-1, 'loc_15B70'),
    )

    def _loc_15B0C(): pass

    label('loc_15B0C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_15B7E')

    def _loc_15B2D(): pass

    label('loc_15B2D')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_15B7E')

    def _loc_15B4E(): pass

    label('loc_15B4E')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_15B7E')

    def _loc_15B70(): pass

    label('loc_15B70')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_15B7E')

    def _loc_15B7E(): pass

    label('loc_15B7E')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15BA2',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_15BA2(): pass

    label('loc_15BA2')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080B0, 'loc_15BBB'),
        (0x000080B3, 'loc_15BBB'),
        (-1, 'loc_15C41'),
    )

    def _loc_15BBB(): pass

    label('loc_15BBB')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'フィーの前で操作許可にします。\n',
            'フィーに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_15C41')

    def _loc_15C41(): pass

    label('loc_15C41')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15C6A',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_15C6A(): pass

    label('loc_15C6A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080B0, 'loc_15CAB'),
        (0x000080B1, 'loc_15CC7'),
        (0x000080B2, 'loc_15CE3'),
        (0x000080B3, 'loc_15CFF'),
        (0x000080B4, 'loc_15D1B'),
        (0x000080B5, 'loc_15D37'),
        (0x000080B6, 'loc_15D57'),
        (-1, 'loc_15D73'),
    )

    def _loc_15CAB(): pass

    label('loc_15CAB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80B0, 0x0))

    Jump('loc_15D78')

    def _loc_15CC7(): pass

    label('loc_15CC7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80B1, 0x0))

    Jump('loc_15D78')

    def _loc_15CE3(): pass

    label('loc_15CE3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80B2, 0x0))

    Jump('loc_15D78')

    def _loc_15CFF(): pass

    label('loc_15CFF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80B3, 0x0))

    Jump('loc_15D78')

    def _loc_15D1B(): pass

    label('loc_15D1B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80B4, 0x0))

    Jump('loc_15D78')

    def _loc_15D37(): pass

    label('loc_15D37')

    FormationAddMember(ChrTable['菲'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80B5, 0x0))

    Jump('loc_15D78')

    def _loc_15D57(): pass

    label('loc_15D57')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80B6, 0x0))

    Jump('loc_15D78')

    def _loc_15D73(): pass

    label('loc_15D73')

    Jump('loc_15D78')

    def _loc_15D78(): pass

    label('loc_15D78')

    Jump('loc_158BD')

    def _loc_15D7D(): pass

    label('loc_15D7D')

    Return()

# id: 0x006C offset: 0x15D80
@scena.Code('EV_KizunaJump_13')
def EV_KizunaJump_13():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_15D89(): pass

    label('loc_15D89')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16030',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1301_00][ガイウス①発生会話　　　　　　]', 0x000080C0)
    MenuCmd(0x01, 0x02, '[KZ1301_01][ガイウス①ウォレスとの手合わせ]', 0x000080C1)
    MenuCmd(0x01, 0x02, '[KZ1302_00][ガイウス・アトラクション後　　]', 0x000080C3)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080C0, 'loc_15E9B'),
        (0x000080C1, 'loc_15E9B'),
        (0x000080C3, 'loc_15EBC'),
        (-1, 'loc_15EDE'),
    )

    def _loc_15E9B(): pass

    label('loc_15E9B')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_15EEC')

    def _loc_15EBC(): pass

    label('loc_15EBC')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_15EEC')

    def _loc_15EDE(): pass

    label('loc_15EDE')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_15EEC')

    def _loc_15EEC(): pass

    label('loc_15EEC')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15F10',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_15F10(): pass

    label('loc_15F10')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080C0, 'loc_15F21'),
        (-1, 'loc_15FAD'),
    )

    def _loc_15F21(): pass

    label('loc_15F21')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ガイウスの前で操作許可にします。\n',
            'ガイウスに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_15FAD')

    def _loc_15FAD(): pass

    label('loc_15FAD')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080C0, 'loc_15FCE'),
        (0x000080C1, 'loc_15FEA'),
        (0x000080C3, 'loc_16006'),
        (-1, 'loc_16026'),
    )

    def _loc_15FCE(): pass

    label('loc_15FCE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80C0, 0x0))

    Jump('loc_1602B')

    def _loc_15FEA(): pass

    label('loc_15FEA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80C1, 0x0))

    Jump('loc_1602B')

    def _loc_16006(): pass

    label('loc_16006')

    FormationAddMember(ChrTable['蓋烏斯'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80C3, 0x0))

    Jump('loc_1602B')

    def _loc_16026(): pass

    label('loc_16026')

    Jump('loc_1602B')

    def _loc_1602B(): pass

    label('loc_1602B')

    Jump('loc_15D89')

    def _loc_16030(): pass

    label('loc_16030')

    Return()

# id: 0x006D offset: 0x16034
@scena.Code('EV_KizunaJump_14')
def EV_KizunaJump_14():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1603D(): pass

    label('loc_1603D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1652D',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1401_00][クロウ①発生会話　　　　　　　]', 0x000080D0)
    MenuCmd(0x01, 0x02, '[KZ1401_01][クロウ①クロウにＶＭを指南する]', 0x000080D1)
    MenuCmd(0x01, 0x02, '[KZ1402_00][クロウ②発生会話　　　　　　　]', 0x000080D2)
    MenuCmd(0x01, 0x02, '[KZ1402_01][クロウ②老婆にＧの形見を渡す　]', 0x000080D3)
    MenuCmd(0x01, 0x02, '[KZ1402_02][クロウ②青年にＶの形見を渡す　]', 0x000080D4)
    MenuCmd(0x01, 0x02, '[KZ1402_03][クロウ②Ｓと聯絡を取る　　　　]', 0x000080D5)
    MenuCmd(0x01, 0x02, '[KZ1402_04][クロウ②飛翔するヴァリマール達]', 0x000080D6)
    MenuCmd(0x01, 0x02, '[KZ1403_00][クロウ・アトラクション後　　　]', 0x000080D8)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080D0, 'loc_162C1'),
        (0x000080D1, 'loc_162C1'),
        (0x000080D2, 'loc_162E2'),
        (0x000080D3, 'loc_162E2'),
        (0x000080D4, 'loc_162E2'),
        (0x000080D5, 'loc_162E2'),
        (0x000080D6, 'loc_162E2'),
        (0x000080D8, 'loc_16303'),
        (-1, 'loc_16325'),
    )

    def _loc_162C1(): pass

    label('loc_162C1')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_16333')

    def _loc_162E2(): pass

    label('loc_162E2')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_16333')

    def _loc_16303(): pass

    label('loc_16303')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_16333')

    def _loc_16325(): pass

    label('loc_16325')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_16333')

    def _loc_16333(): pass

    label('loc_16333')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16357',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_16357(): pass

    label('loc_16357')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080D0, 'loc_16370'),
        (0x000080D2, 'loc_16370'),
        (-1, 'loc_163F6'),
    )

    def _loc_16370(): pass

    label('loc_16370')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'クロウの前で操作許可にします。\n',
            'クロウに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_163F6')

    def _loc_163F6(): pass

    label('loc_163F6')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080D0, 'loc_1643F'),
        (0x000080D1, 'loc_1645B'),
        (0x000080D2, 'loc_16477'),
        (0x000080D3, 'loc_16493'),
        (0x000080D4, 'loc_164AF'),
        (0x000080D5, 'loc_164CB'),
        (0x000080D6, 'loc_164E7'),
        (0x000080D8, 'loc_16503'),
        (-1, 'loc_16523'),
    )

    def _loc_1643F(): pass

    label('loc_1643F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D0, 0x0))

    Jump('loc_16528')

    def _loc_1645B(): pass

    label('loc_1645B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D1, 0x0))

    Jump('loc_16528')

    def _loc_16477(): pass

    label('loc_16477')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D2, 0x0))

    Jump('loc_16528')

    def _loc_16493(): pass

    label('loc_16493')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D3, 0x0))

    Jump('loc_16528')

    def _loc_164AF(): pass

    label('loc_164AF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D4, 0x0))

    Jump('loc_16528')

    def _loc_164CB(): pass

    label('loc_164CB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D5, 0x0))

    Jump('loc_16528')

    def _loc_164E7(): pass

    label('loc_164E7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D6, 0x0))

    Jump('loc_16528')

    def _loc_16503(): pass

    label('loc_16503')

    FormationAddMember(ChrTable['克蕾雅少校'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80D8, 0x0))

    Jump('loc_16528')

    def _loc_16523(): pass

    label('loc_16523')

    Jump('loc_16528')

    def _loc_16528(): pass

    label('loc_16528')

    Jump('loc_1603D')

    def _loc_1652D(): pass

    label('loc_1652D')

    Return()

# id: 0x006E offset: 0x16530
@scena.Code('EV_KizunaJump_15')
def EV_KizunaJump_15():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_16539(): pass

    label('loc_16539')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16A64',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1501_00][サラ①発生会話　　　　　　　　]　', 0x000080E0)
    MenuCmd(0x01, 0x02, '[KZ1501_01][サラ①最悪の鬼化するリィン　　]戦', 0x000080E1)
    MenuCmd(0x01, 0x02, '[KZ1501_02][サラ①リィンが自分を取り戻す　]　', 0x000080E2)
    MenuCmd(0x01, 0x02, '[KZ1501_03][サラ①メルカバに戻る　　　　　]　', 0x000080E3)
    MenuCmd(0x01, 0x02, '[KZ1502_00][サラ②発生会話　　　　　　　　]　', 0x000080E4)
    MenuCmd(0x01, 0x02, '[KZ1502_01][サラ②墓参りをする　　　　　　]　', 0x000080E5)
    MenuCmd(0x01, 0x02, '[KZ1503_00][サラ・前日譚・約束をする　　　]　', 0x000080E6)
    MenuCmd(0x01, 0x02, '[KZ1504_00][サラ・前日譚・最終シーン　　　]　', 0x000080E7)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080E0, 'loc_167D5'),
        (0x000080E1, 'loc_167D5'),
        (0x000080E2, 'loc_167D5'),
        (0x000080E3, 'loc_167D5'),
        (0x000080E4, 'loc_167F6'),
        (0x000080E5, 'loc_167F6'),
        (0x000080E6, 'loc_16817'),
        (0x000080E7, 'loc_16817'),
        (-1, 'loc_16839'),
    )

    def _loc_167D5(): pass

    label('loc_167D5')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_16847')

    def _loc_167F6(): pass

    label('loc_167F6')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_16847')

    def _loc_16817(): pass

    label('loc_16817')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_16847')

    def _loc_16839(): pass

    label('loc_16839')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_16847')

    def _loc_16847(): pass

    label('loc_16847')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1686B',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1686B(): pass

    label('loc_1686B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080E0, 'loc_16884'),
        (0x000080E4, 'loc_16884'),
        (-1, 'loc_16904'),
    )

    def _loc_16884(): pass

    label('loc_16884')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'サラの前で操作許可にします。\n',
            'サラに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_16904')

    def _loc_16904(): pass

    label('loc_16904')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1692D',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_1692D(): pass

    label('loc_1692D')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080E0, 'loc_16976'),
        (0x000080E1, 'loc_16992'),
        (0x000080E2, 'loc_169AE'),
        (0x000080E3, 'loc_169CA'),
        (0x000080E4, 'loc_169E6'),
        (0x000080E5, 'loc_16A02'),
        (0x000080E6, 'loc_16A1E'),
        (0x000080E7, 'loc_16A3E'),
        (-1, 'loc_16A5A'),
    )

    def _loc_16976(): pass

    label('loc_16976')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E0, 0x0))

    Jump('loc_16A5F')

    def _loc_16992(): pass

    label('loc_16992')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E1, 0x0))

    Jump('loc_16A5F')

    def _loc_169AE(): pass

    label('loc_169AE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E2, 0x0))

    Jump('loc_16A5F')

    def _loc_169CA(): pass

    label('loc_169CA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E3, 0x0))

    Jump('loc_16A5F')

    def _loc_169E6(): pass

    label('loc_169E6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E4, 0x0))

    Jump('loc_16A5F')

    def _loc_16A02(): pass

    label('loc_16A02')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E5, 0x0))

    Jump('loc_16A5F')

    def _loc_16A1E(): pass

    label('loc_16A1E')

    FormationAddMember(ChrTable['莎拉'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E6, 0x0))

    Jump('loc_16A5F')

    def _loc_16A3E(): pass

    label('loc_16A3E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80E7, 0x0))

    Jump('loc_16A5F')

    def _loc_16A5A(): pass

    label('loc_16A5A')

    Jump('loc_16A5F')

    def _loc_16A5F(): pass

    label('loc_16A5F')

    Jump('loc_16539')

    def _loc_16A64(): pass

    label('loc_16A64')

    Return()

# id: 0x006F offset: 0x16A68
@scena.Code('EV_KizunaJump_16')
def EV_KizunaJump_16():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_16A71(): pass

    label('loc_16A71')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16EA8',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1601_00][トワ①発生会話　　　　　　　　]', 0x000080F0)
    MenuCmd(0x01, 0x02, '[KZ1601_01][トワ①解析作業を手伝う　　　　]', 0x000080F1)
    MenuCmd(0x01, 0x02, '[KZ1602_00][トワ②発生会話　　　　　　　　]', 0x000080F2)
    MenuCmd(0x01, 0x02, '[KZ1602_01][トワ②事故現場を見に行く　　　]', 0x000080F3)
    MenuCmd(0x01, 0x02, '[KZ1603_00][トワ・前日譚・約束をする　　　]', 0x000080F4)
    MenuCmd(0x01, 0x02, '[KZ1604_00][トワ・前日譚・最終シーン　　　]', 0x000080F5)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080F0, 'loc_16C61'),
        (0x000080F1, 'loc_16C61'),
        (0x000080F2, 'loc_16C82'),
        (0x000080F3, 'loc_16C82'),
        (0x000080F4, 'loc_16CA3'),
        (0x000080F5, 'loc_16CA3'),
        (-1, 'loc_16CC5'),
    )

    def _loc_16C61(): pass

    label('loc_16C61')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_16CD3')

    def _loc_16C82(): pass

    label('loc_16C82')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_16CD3')

    def _loc_16CA3(): pass

    label('loc_16CA3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_16CD3')

    def _loc_16CC5(): pass

    label('loc_16CC5')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_16CD3')

    def _loc_16CD3(): pass

    label('loc_16CD3')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16CF7',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_16CF7(): pass

    label('loc_16CF7')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080F0, 'loc_16D10'),
        (0x000080F2, 'loc_16D10'),
        (-1, 'loc_16D90'),
    )

    def _loc_16D10(): pass

    label('loc_16D10')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'トワの前で操作許可にします。\n',
            'トワに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_16D90')

    def _loc_16D90(): pass

    label('loc_16D90')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16DB9',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_16DB9(): pass

    label('loc_16DB9')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000080F0, 'loc_16DF2'),
        (0x000080F1, 'loc_16E0E'),
        (0x000080F2, 'loc_16E2A'),
        (0x000080F3, 'loc_16E46'),
        (0x000080F4, 'loc_16E62'),
        (0x000080F5, 'loc_16E82'),
        (-1, 'loc_16E9E'),
    )

    def _loc_16DF2(): pass

    label('loc_16DF2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80F0, 0x0))

    Jump('loc_16EA3')

    def _loc_16E0E(): pass

    label('loc_16E0E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80F1, 0x0))

    Jump('loc_16EA3')

    def _loc_16E2A(): pass

    label('loc_16E2A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80F2, 0x0))

    Jump('loc_16EA3')

    def _loc_16E46(): pass

    label('loc_16E46')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80F3, 0x0))

    Jump('loc_16EA3')

    def _loc_16E62(): pass

    label('loc_16E62')

    FormationAddMember(ChrTable['測試：妙婕制服測試'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80F4, 0x0))

    Jump('loc_16EA3')

    def _loc_16E82(): pass

    label('loc_16E82')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x80F5, 0x0))

    Jump('loc_16EA3')

    def _loc_16E9E(): pass

    label('loc_16E9E')

    Jump('loc_16EA3')

    def _loc_16EA3(): pass

    label('loc_16EA3')

    Jump('loc_16A71')

    def _loc_16EA8(): pass

    label('loc_16EA8')

    Return()

# id: 0x0070 offset: 0x16EAC
@scena.Code('EV_KizunaJump_17')
def EV_KizunaJump_17():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_16EB5(): pass

    label('loc_16EB5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_172D5',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1701_00][デュバリィ①発生会話　　　　　]', 0x00008100)
    MenuCmd(0x01, 0x02, '[KZ1701_01][デュバリィ①立会い稽古を受ける]', 0x00008101)
    MenuCmd(0x01, 0x02, '[KZ1702_00][デュバリィ②発生会話　　　　　]', 0x00008103)
    MenuCmd(0x01, 0x02, '[KZ1702_01][デュバリィ②甲冑を引き取る　　]', 0x00008104)
    MenuCmd(0x01, 0x02, '[KZ1702_02][デュバリィ②船着場での語らい　]', 0x00008105)
    MenuCmd(0x01, 0x02, '[KZ1703_00][デュバリィ・アトラクション後　]', 0x00008107)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008100, 'loc_170A5'),
        (0x00008101, 'loc_170A5'),
        (0x00008103, 'loc_170C6'),
        (0x00008104, 'loc_170C6'),
        (0x00008105, 'loc_170C6'),
        (0x00008107, 'loc_170E7'),
        (-1, 'loc_17109'),
    )

    def _loc_170A5(): pass

    label('loc_170A5')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_17117')

    def _loc_170C6(): pass

    label('loc_170C6')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_17117')

    def _loc_170E7(): pass

    label('loc_170E7')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_17117')

    def _loc_17109(): pass

    label('loc_17109')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17117')

    def _loc_17117(): pass

    label('loc_17117')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1713B',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1713B(): pass

    label('loc_1713B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008100, 'loc_17154'),
        (0x00008103, 'loc_17154'),
        (-1, 'loc_171E6'),
    )

    def _loc_17154(): pass

    label('loc_17154')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'デュバリィの前で操作許可にします。\n',
            'デュバリィに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_171E6')

    def _loc_171E6(): pass

    label('loc_171E6')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008100, 'loc_1721F'),
        (0x00008101, 'loc_1723B'),
        (0x00008103, 'loc_17257'),
        (0x00008104, 'loc_17273'),
        (0x00008105, 'loc_1728F'),
        (0x00008107, 'loc_172AB'),
        (-1, 'loc_172CB'),
    )

    def _loc_1721F(): pass

    label('loc_1721F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8100, 0x0))

    Jump('loc_172D0')

    def _loc_1723B(): pass

    label('loc_1723B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8101, 0x0))

    Jump('loc_172D0')

    def _loc_17257(): pass

    label('loc_17257')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8103, 0x0))

    Jump('loc_172D0')

    def _loc_17273(): pass

    label('loc_17273')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8104, 0x0))

    Jump('loc_172D0')

    def _loc_1728F(): pass

    label('loc_1728F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8105, 0x0))

    Jump('loc_172D0')

    def _loc_172AB(): pass

    label('loc_172AB')

    FormationAddMember(ChrTable['杜巴莉'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8107, 0x0))

    Jump('loc_172D0')

    def _loc_172CB(): pass

    label('loc_172CB')

    Jump('loc_172D0')

    def _loc_172D0(): pass

    label('loc_172D0')

    Jump('loc_16EB5')

    def _loc_172D5(): pass

    label('loc_172D5')

    Return()

# id: 0x0071 offset: 0x172D8
@scena.Code('EV_KizunaJump_18')
def EV_KizunaJump_18():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_172E1(): pass

    label('loc_172E1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17839',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1801_00][セリーヌ①発生会話　　　　　　]', 0x00008110)
    MenuCmd(0x01, 0x02, '[KZ1801_01][セリーヌ①露店で商品を見る　　]', 0x00008111)
    MenuCmd(0x01, 0x02, '[KZ1801_02][セリーヌ①ミルクをご馳走する　]', 0x00008112)
    MenuCmd(0x01, 0x02, '[KZ1801_03][セリーヌ①仕立て屋で棚を見る　]', 0x00008113)
    MenuCmd(0x01, 0x02, '[KZ1801_04][セリーヌ①贈り物を身につける　]', 0x00008114)
    MenuCmd(0x01, 0x02, '[KZ1802_00][セリーヌ②発生会話　　　　　　]', 0x00008116)
    MenuCmd(0x01, 0x02, '[KZ1802_01][セリーヌ②セリーヌが転移する　]', 0x00008117)
    MenuCmd(0x01, 0x02, '[KZ1802_02][セリーヌ②修行をするセリーヌ　]', 0x00008118)
    MenuCmd(0x01, 0x02, '[KZ1803_00][セリーヌ・アトラクション後　　]', 0x0000811A)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008110, 'loc_175AF'),
        (0x00008111, 'loc_175AF'),
        (0x00008112, 'loc_175AF'),
        (0x00008113, 'loc_175AF'),
        (0x00008114, 'loc_175AF'),
        (0x00008116, 'loc_175D0'),
        (0x00008117, 'loc_175D0'),
        (0x00008118, 'loc_175D0'),
        (0x0000811A, 'loc_175F1'),
        (-1, 'loc_17613'),
    )

    def _loc_175AF(): pass

    label('loc_175AF')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_17621')

    def _loc_175D0(): pass

    label('loc_175D0')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_17621')

    def _loc_175F1(): pass

    label('loc_175F1')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_17621')

    def _loc_17613(): pass

    label('loc_17613')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17621')

    def _loc_17621(): pass

    label('loc_17621')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17645',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_17645(): pass

    label('loc_17645')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008110, 'loc_17656'),
        (-1, 'loc_176E2'),
    )

    def _loc_17656(): pass

    label('loc_17656')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'セリーヌの前で操作許可にします。\n',
            'セリーヌに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_176E2')

    def _loc_176E2(): pass

    label('loc_176E2')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008110, 'loc_17733'),
        (0x00008111, 'loc_1774F'),
        (0x00008112, 'loc_1776B'),
        (0x00008113, 'loc_17787'),
        (0x00008114, 'loc_177A3'),
        (0x00008116, 'loc_177BF'),
        (0x00008117, 'loc_177DB'),
        (0x00008118, 'loc_177F7'),
        (0x0000811A, 'loc_17813'),
        (-1, 'loc_1782F'),
    )

    def _loc_17733(): pass

    label('loc_17733')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8110, 0x0))

    Jump('loc_17834')

    def _loc_1774F(): pass

    label('loc_1774F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8111, 0x0))

    Jump('loc_17834')

    def _loc_1776B(): pass

    label('loc_1776B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8112, 0x0))

    Jump('loc_17834')

    def _loc_17787(): pass

    label('loc_17787')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8113, 0x0))

    Jump('loc_17834')

    def _loc_177A3(): pass

    label('loc_177A3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8114, 0x0))

    Jump('loc_17834')

    def _loc_177BF(): pass

    label('loc_177BF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8116, 0x0))

    Jump('loc_17834')

    def _loc_177DB(): pass

    label('loc_177DB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8117, 0x0))

    Jump('loc_17834')

    def _loc_177F7(): pass

    label('loc_177F7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8118, 0x0))

    Jump('loc_17834')

    def _loc_17813(): pass

    label('loc_17813')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x811A, 0x0))

    Jump('loc_17834')

    def _loc_1782F(): pass

    label('loc_1782F')

    Jump('loc_17834')

    def _loc_17834(): pass

    label('loc_17834')

    Jump('loc_172E1')

    def _loc_17839(): pass

    label('loc_17839')

    Return()

# id: 0x0072 offset: 0x1783C
@scena.Code('EV_KizunaJump_19')
def EV_KizunaJump_19():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17845(): pass

    label('loc_17845')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17C8E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ1901_00][アルフィン①発生会話　　　　　]', 0x00008120)
    MenuCmd(0x01, 0x02, '[KZ1901_01][アルフィン①アルスターに行く　]', 0x00008121)
    MenuCmd(0x01, 0x02, '[KZ1902_00][アルフィン②発生会話　　　　　]', 0x00008123)
    MenuCmd(0x01, 0x02, '[KZ1902_01][アルフィン②セドリックに会う　]', 0x00008124)
    MenuCmd(0x01, 0x02, '[KZ1903_00][アルフィン・前日譚・誘われる　]', 0x00008126)
    MenuCmd(0x01, 0x02, '[KZ1904_00][アルフィン・前日譚・最終シーン]', 0x00008127)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008120, 'loc_17A35'),
        (0x00008121, 'loc_17A35'),
        (0x00008123, 'loc_17A56'),
        (0x00008124, 'loc_17A56'),
        (0x00008126, 'loc_17A77'),
        (0x00008127, 'loc_17A77'),
        (-1, 'loc_17A99'),
    )

    def _loc_17A35(): pass

    label('loc_17A35')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_17AA7')

    def _loc_17A56(): pass

    label('loc_17A56')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_17AA7')

    def _loc_17A77(): pass

    label('loc_17A77')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_17AA7')

    def _loc_17A99(): pass

    label('loc_17A99')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17AA7')

    def _loc_17AA7(): pass

    label('loc_17AA7')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17ACB',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_17ACB(): pass

    label('loc_17ACB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008120, 'loc_17AE4'),
        (0x00008123, 'loc_17AE4'),
        (-1, 'loc_17B76'),
    )

    def _loc_17AE4(): pass

    label('loc_17AE4')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'アルフィンの前で操作許可にします。\n',
            'アルフィンに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_17B76')

    def _loc_17B76(): pass

    label('loc_17B76')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17B9F',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_17B9F(): pass

    label('loc_17B9F')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008120, 'loc_17BD8'),
        (0x00008121, 'loc_17BF4'),
        (0x00008123, 'loc_17C10'),
        (0x00008124, 'loc_17C2C'),
        (0x00008126, 'loc_17C48'),
        (0x00008127, 'loc_17C68'),
        (-1, 'loc_17C84'),
    )

    def _loc_17BD8(): pass

    label('loc_17BD8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8120, 0x0))

    Jump('loc_17C89')

    def _loc_17BF4(): pass

    label('loc_17BF4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8121, 0x0))

    Jump('loc_17C89')

    def _loc_17C10(): pass

    label('loc_17C10')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8123, 0x0))

    Jump('loc_17C89')

    def _loc_17C2C(): pass

    label('loc_17C2C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8124, 0x0))

    Jump('loc_17C89')

    def _loc_17C48(): pass

    label('loc_17C48')

    FormationAddMember(ChrTable['測試：杜巴莉'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8126, 0x0))

    Jump('loc_17C89')

    def _loc_17C68(): pass

    label('loc_17C68')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8127, 0x0))

    Jump('loc_17C89')

    def _loc_17C84(): pass

    label('loc_17C84')

    Jump('loc_17C89')

    def _loc_17C89(): pass

    label('loc_17C89')

    Jump('loc_17845')

    def _loc_17C8E(): pass

    label('loc_17C8E')

    Return()

# id: 0x0073 offset: 0x17C90
@scena.Code('EV_KizunaJump_20')
def EV_KizunaJump_20():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17C99(): pass

    label('loc_17C99')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_181B2',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ2001_00][エリゼ①発生会話　　　　　　　]', 0x00008130)
    MenuCmd(0x01, 0x02, '[KZ2001_01][エリゼ①テオたちと通信する　　]', 0x00008131)
    MenuCmd(0x01, 0x02, '[KZ2002_00][エリゼ②発生会話　　　　　　　]', 0x00008132)
    MenuCmd(0x01, 0x02, '[KZ2002_01][エリゼ②占い師の家に向かう　　]', 0x00008133)
    MenuCmd(0x01, 0x02, '[KZ2002_02][エリゼ②服に魔力を込めてもらう]', 0x00008134)
    MenuCmd(0x01, 0x02, '[KZ2002_03][エリゼ②広場での語らい　　　　]', 0x00008135)
    MenuCmd(0x01, 0x02, '[KZ2003_00][エリゼ・前日譚・誘いを受ける　]', 0x00008136)
    MenuCmd(0x01, 0x02, '[KZ2004_00][エリゼ・前日譚・最終シーン　　]', 0x00008137)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008130, 'loc_17F1D'),
        (0x00008131, 'loc_17F1D'),
        (0x00008132, 'loc_17F3E'),
        (0x00008133, 'loc_17F3E'),
        (0x00008134, 'loc_17F3E'),
        (0x00008135, 'loc_17F3E'),
        (0x00008136, 'loc_17F5F'),
        (0x00008137, 'loc_17F5F'),
        (-1, 'loc_17F81'),
    )

    def _loc_17F1D(): pass

    label('loc_17F1D')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    Jump('loc_17F8F')

    def _loc_17F3E(): pass

    label('loc_17F3E')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')

    Jump('loc_17F8F')

    def _loc_17F5F(): pass

    label('loc_17F5F')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_17F8F')

    def _loc_17F81(): pass

    label('loc_17F81')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17F8F')

    def _loc_17F8F(): pass

    label('loc_17F8F')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17FB3',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_17FB3(): pass

    label('loc_17FB3')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008130, 'loc_17FCC'),
        (0x00008132, 'loc_17FCC'),
        (-1, 'loc_18052'),
    )

    def _loc_17FCC(): pass

    label('loc_17FCC')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'エリゼの前で操作許可にします。\n',
            'エリゼに話しかけて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_18052')

    def _loc_18052(): pass

    label('loc_18052')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1807B',
    )

    Call(ScriptId.Current, 'FC_KizunFlagSet_Special')

    def _loc_1807B(): pass

    label('loc_1807B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008130, 'loc_180C4'),
        (0x00008131, 'loc_180E0'),
        (0x00008132, 'loc_180FC'),
        (0x00008133, 'loc_18118'),
        (0x00008134, 'loc_18134'),
        (0x00008135, 'loc_18150'),
        (0x00008136, 'loc_1816C'),
        (0x00008137, 'loc_1818C'),
        (-1, 'loc_181A8'),
    )

    def _loc_180C4(): pass

    label('loc_180C4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8130, 0x0))

    Jump('loc_181AD')

    def _loc_180E0(): pass

    label('loc_180E0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8131, 0x0))

    Jump('loc_181AD')

    def _loc_180FC(): pass

    label('loc_180FC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8132, 0x0))

    Jump('loc_181AD')

    def _loc_18118(): pass

    label('loc_18118')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8133, 0x0))

    Jump('loc_181AD')

    def _loc_18134(): pass

    label('loc_18134')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8134, 0x0))

    Jump('loc_181AD')

    def _loc_18150(): pass

    label('loc_18150')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8135, 0x0))

    Jump('loc_181AD')

    def _loc_1816C(): pass

    label('loc_1816C')

    FormationAddMember(ChrTable['測試：奧利維爾'])
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8136, 0x0))

    Jump('loc_181AD')

    def _loc_1818C(): pass

    label('loc_1818C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8137, 0x0))

    Jump('loc_181AD')

    def _loc_181A8(): pass

    label('loc_181A8')

    Jump('loc_181AD')

    def _loc_181AD(): pass

    label('loc_181AD')

    Jump('loc_17C99')

    def _loc_181B2(): pass

    label('loc_181B2')

    Return()

# id: 0x0074 offset: 0x181B4
@scena.Code('EV_KizunaJump_99')
def EV_KizunaJump_99():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_181BD(): pass

    label('loc_181BD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_191F6',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ9901_00][壮行会・チュートリアル　　　　]', 0x00008140)
    MenuCmd(0x01, 0x02, '[KZ9902_00][観覧車・選択肢　　　　　　　　]', 0x00008141)
    MenuCmd(0x01, 0x02, '[KZ9902_01][観覧車に乗る　　　　　　　　　]', 0x00008142)
    MenuCmd(0x01, 0x02, '[KZ9903_00][ホラーコースター・選択肢　　　]', 0x00008143)
    MenuCmd(0x01, 0x02, '[KZ9903_01][ホラーコースターに乗る　　　　]', 0x00008144)
    MenuCmd(0x01, 0x02, '[KZ9903_02][ホラーコースター終了後の語らい]', 0x00008146)
    MenuCmd(0x01, 0x02, '[KZ9904_00][鏡の城・選択肢　　　　　　　　]', 0x00008148)
    MenuCmd(0x01, 0x02, '[KZ9904_01][鏡の城に入る　　　　　　　　　]', 0x00008149)
    MenuCmd(0x01, 0x02, '[KZ9904_02][ベンチでの語らい　　　　　　　]', 0x0000814A)
    MenuCmd(0x01, 0x02, '[KZ9904_03][ベリルに占ってもらう　　　　　]', 0x0000814B)
    MenuCmd(0x01, 0x02, '[KZ9905_00][ドリンクスタンド・選択肢　　　]', 0x0000814D)
    MenuCmd(0x01, 0x02, '[KZ9905_01][オリジナルドリンクを楽しむ　　]', 0x0000814E)
    MenuCmd(0x01, 0x02, '[KZ9906_00][砂浜で花火・選択肢　　　　　　]', 0x0000814F)
    MenuCmd(0x01, 0x02, '[KZ9906_01][パートナーと線香花火をする　　]', 0x00008150)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008140, 'loc_185FD'),
        (0x00008141, 'loc_185FD'),
        (0x00008142, 'loc_185FD'),
        (0x00008143, 'loc_185FD'),
        (0x00008144, 'loc_185FD'),
        (0x00008146, 'loc_185FD'),
        (0x00008148, 'loc_185FD'),
        (0x00008149, 'loc_185FD'),
        (0x0000814A, 'loc_185FD'),
        (0x0000814B, 'loc_185FD'),
        (0x0000814D, 'loc_185FD'),
        (0x0000814E, 'loc_185FD'),
        (0x0000814F, 'loc_185FD'),
        (0x00008150, 'loc_185FD'),
        (-1, 'loc_1861F'),
    )

    def _loc_185FD(): pass

    label('loc_185FD')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_1862D')

    def _loc_1861F(): pass

    label('loc_1861F')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1862D')

    def _loc_1862D(): pass

    label('loc_1862D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18651',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_18651(): pass

    label('loc_18651')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008142, 'loc_1869A'),
        (0x00008144, 'loc_1869A'),
        (0x00008146, 'loc_1869A'),
        (0x00008149, 'loc_18A3D'),
        (0x0000814A, 'loc_18A3D'),
        (0x0000814B, 'loc_18A3D'),
        (0x0000814E, 'loc_18C27'),
        (0x00008150, 'loc_18DFD'),
        (-1, 'loc_18FEB'),
    )

    def _loc_1869A(): pass

    label('loc_1869A')

    OP_C6(0x08, 0xFFFF, 0x00, 0x01, 0x01)
    OP_23(0x05, 0xFFFF, 0x0050, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '誰を誘いますか？\n',
            '（※チケットを１枚消費します）\n',
            '                                ',
            TxtCtl.Enter,
        ),
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0011, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, 'ユウナ', 0x00000001)
    MenuCmd(0x01, 0x00, 'クルト', 0x00000002)
    MenuCmd(0x01, 0x00, 'アルティナ', 0x00000003)
    MenuCmd(0x01, 0x00, 'ミュゼ', 0x00000004)
    MenuCmd(0x01, 0x00, 'アッシュ', 0x00000005)
    MenuCmd(0x01, 0x00, 'アリサ', 0x00000006)
    MenuCmd(0x01, 0x00, 'エリオット', 0x00000007)
    MenuCmd(0x01, 0x00, 'ラウラ', 0x00000008)
    MenuCmd(0x01, 0x00, 'マキアス', 0x00000009)
    MenuCmd(0x01, 0x00, 'エマ', 0x0000000A)
    MenuCmd(0x01, 0x00, 'ユーシス', 0x0000000B)
    MenuCmd(0x01, 0x00, 'フィー', 0x0000000C)
    MenuCmd(0x01, 0x00, 'ガイウス', 0x0000000D)
    MenuCmd(0x01, 0x00, 'クロウ', 0x0000000E)
    MenuCmd(0x01, 0x00, 'サラ', 0x0000000F)
    MenuCmd(0x01, 0x00, 'トワ', 0x00000010)
    MenuCmd(0x01, 0x00, 'デュバリィ', 0x00000011)
    MenuCmd(0x01, 0x00, 'セリーヌ', 0x00000012)
    MenuCmd(0x01, 0x00, 'アルフィン', 0x00000013)
    MenuCmd(0x01, 0x00, 'エリゼ', 0x00000014)
    MenuCmd(0x02, 0x00, 0x00, 0xFFFF, 0x010E, 0x00)
    MenuCmd(0x04, 0x00, 0xF9)
    MenuCmd(0x03, 0x00)
    OP_25(0x00)
    OP_C6(0x08, 0xFFFF, 0x00, 0xFF, 0x00)
    Call(ScriptId.System, 'FC_Kizuna_Sub_Point_Consume')

    Switch(
        (
            (Expr.Expr23, 0xF9),
            Expr.Return,
        ),
        (0x00000001, 'loc_18984'),
        (0x00000002, 'loc_1898D'),
        (0x00000003, 'loc_18996'),
        (0x00000004, 'loc_1899F'),
        (0x00000005, 'loc_189A8'),
        (0x00000006, 'loc_189B1'),
        (0x00000007, 'loc_189BA'),
        (0x00000008, 'loc_189C3'),
        (0x00000009, 'loc_189CC'),
        (0x0000000A, 'loc_189D5'),
        (0x0000000B, 'loc_189DE'),
        (0x0000000C, 'loc_189E7'),
        (0x0000000D, 'loc_189F0'),
        (0x0000000E, 'loc_189F9'),
        (0x0000000F, 'loc_18A02'),
        (0x00000010, 'loc_18A0B'),
        (0x00000011, 'loc_18A14'),
        (0x00000012, 'loc_18A1D'),
        (0x00000013, 'loc_18A26'),
        (0x00000014, 'loc_18A2F'),
        (-1, 'loc_18A38'),
    )

    def _loc_18984(): pass

    label('loc_18984')

    FormationAddMember(ChrTable['悠娜'])

    Jump('loc_18A38')

    def _loc_1898D(): pass

    label('loc_1898D')

    FormationAddMember(ChrTable['庫爾特'])

    Jump('loc_18A38')

    def _loc_18996(): pass

    label('loc_18996')

    FormationAddMember(ChrTable['亞爾緹娜'])

    Jump('loc_18A38')

    def _loc_1899F(): pass

    label('loc_1899F')

    FormationAddMember(ChrTable['妙婕'])

    Jump('loc_18A38')

    def _loc_189A8(): pass

    label('loc_189A8')

    FormationAddMember(ChrTable['亞修'])

    Jump('loc_18A38')

    def _loc_189B1(): pass

    label('loc_189B1')

    FormationAddMember(ChrTable['亞莉莎'])

    Jump('loc_18A38')

    def _loc_189BA(): pass

    label('loc_189BA')

    FormationAddMember(ChrTable['艾略特'])

    Jump('loc_18A38')

    def _loc_189C3(): pass

    label('loc_189C3')

    FormationAddMember(ChrTable['勞拉'])

    Jump('loc_18A38')

    def _loc_189CC(): pass

    label('loc_189CC')

    FormationAddMember(ChrTable['馬奇亞斯'])

    Jump('loc_18A38')

    def _loc_189D5(): pass

    label('loc_189D5')

    FormationAddMember(ChrTable['艾瑪'])

    Jump('loc_18A38')

    def _loc_189DE(): pass

    label('loc_189DE')

    FormationAddMember(ChrTable['尤西斯'])

    Jump('loc_18A38')

    def _loc_189E7(): pass

    label('loc_189E7')

    FormationAddMember(ChrTable['菲'])

    Jump('loc_18A38')

    def _loc_189F0(): pass

    label('loc_189F0')

    FormationAddMember(ChrTable['蓋烏斯'])

    Jump('loc_18A38')

    def _loc_189F9(): pass

    label('loc_189F9')

    FormationAddMember(ChrTable['克蕾雅少校'])

    Jump('loc_18A38')

    def _loc_18A02(): pass

    label('loc_18A02')

    FormationAddMember(ChrTable['莎拉'])

    Jump('loc_18A38')

    def _loc_18A0B(): pass

    label('loc_18A0B')

    FormationAddMember(ChrTable['測試：妙婕制服測試'])

    Jump('loc_18A38')

    def _loc_18A14(): pass

    label('loc_18A14')

    FormationAddMember(ChrTable['杜巴莉'])

    Jump('loc_18A38')

    def _loc_18A1D(): pass

    label('loc_18A1D')

    FormationAddMember(ChrTable['測試：恩奈雅'])

    Jump('loc_18A38')

    def _loc_18A26(): pass

    label('loc_18A26')

    FormationAddMember(ChrTable['測試：杜巴莉'])

    Jump('loc_18A38')

    def _loc_18A2F(): pass

    label('loc_18A2F')

    FormationAddMember(ChrTable['測試：奧利維爾'])

    Jump('loc_18A38')

    def _loc_18A38(): pass

    label('loc_18A38')

    Jump('loc_18FEB')

    def _loc_18A3D(): pass

    label('loc_18A3D')

    OP_C6(0x08, 0xFFFF, 0x00, 0x01, 0x01)
    OP_23(0x05, 0xFFFF, 0x0050, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '誰を誘いますか？\n',
            '（※チケットを１枚消費します）\n',
            '                                ',
            TxtCtl.Enter,
        ),
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, 'アリサ', 0x00000001)
    MenuCmd(0x01, 0x00, 'サラ', 0x00000002)
    MenuCmd(0x01, 0x00, 'エリゼ', 0x00000003)
    MenuCmd(0x01, 0x00, 'セリーヌ', 0x00000004)
    MenuCmd(0x01, 0x00, 'クロウ', 0x00000005)
    MenuCmd(0x01, 0x00, 'エリオット', 0x00000006)
    MenuCmd(0x02, 0x00, 0x00, 0xFFFF, 0x010E, 0x00)
    MenuCmd(0x04, 0x00, 0xF9)
    MenuCmd(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_C6(0x08, 0xFFFF, 0x00, 0xFF, 0x00)
    Call(ScriptId.System, 'FC_Kizuna_Sub_Point_Consume')

    Switch(
        (
            (Expr.Expr23, 0xF9),
            Expr.Return,
        ),
        (0x00000001, 'loc_18BBC'),
        (0x00000002, 'loc_18BCD'),
        (0x00000003, 'loc_18BDE'),
        (0x00000004, 'loc_18BEF'),
        (0x00000005, 'loc_18C00'),
        (0x00000006, 'loc_18C11'),
        (-1, 'loc_18C22'),
    )

    def _loc_18BBC(): pass

    label('loc_18BBC')

    FormationAddMember(ChrTable['亞莉莎'])
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x01000000)

    Jump('loc_18C22')

    def _loc_18BCD(): pass

    label('loc_18BCD')

    FormationAddMember(ChrTable['莎拉'])
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x01000000)

    Jump('loc_18C22')

    def _loc_18BDE(): pass

    label('loc_18BDE')

    FormationAddMember(ChrTable['測試：奧利維爾'])
    MenuChrFlagCmd(0x00, ChrTable['測試：奧利維爾'], 0x01000000)

    Jump('loc_18C22')

    def _loc_18BEF(): pass

    label('loc_18BEF')

    FormationAddMember(ChrTable['測試：恩奈雅'])
    MenuChrFlagCmd(0x00, ChrTable['測試：恩奈雅'], 0x01000000)

    Jump('loc_18C22')

    def _loc_18C00(): pass

    label('loc_18C00')

    FormationAddMember(ChrTable['克蕾雅少校'])
    MenuChrFlagCmd(0x00, ChrTable['克蕾雅少校'], 0x01000000)

    Jump('loc_18C22')

    def _loc_18C11(): pass

    label('loc_18C11')

    FormationAddMember(ChrTable['艾略特'])
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x01000000)

    Jump('loc_18C22')

    def _loc_18C22(): pass

    label('loc_18C22')

    Jump('loc_18FEB')

    def _loc_18C27(): pass

    label('loc_18C27')

    OP_C6(0x08, 0xFFFF, 0x00, 0x01, 0x01)
    OP_23(0x05, 0xFFFF, 0x0050, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '誰を誘いますか？\n',
            '（※チケットを１枚消費します）\n',
            '                                ',
            TxtCtl.Enter,
        ),
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, 'トワ', 0x00000001)
    MenuCmd(0x01, 0x00, 'エマ', 0x00000002)
    MenuCmd(0x01, 0x00, 'ラウラ', 0x00000003)
    MenuCmd(0x01, 0x00, 'ガイウス', 0x00000004)
    MenuCmd(0x01, 0x00, 'マキアス', 0x00000005)
    MenuCmd(0x01, 0x00, 'ミュゼ', 0x00000006)
    MenuCmd(0x01, 0x00, 'クルト', 0x00000007)
    MenuCmd(0x02, 0x00, 0x00, 0xFFFF, 0x010E, 0x00)
    MenuCmd(0x04, 0x00, 0xF9)
    MenuCmd(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_C6(0x08, 0xFFFF, 0x00, 0xFF, 0x00)
    Call(ScriptId.System, 'FC_Kizuna_Sub_Point_Consume')

    Switch(
        (
            (Expr.Expr23, 0xF9),
            Expr.Return,
        ),
        (0x00000001, 'loc_18DB9'),
        (0x00000002, 'loc_18DC2'),
        (0x00000003, 'loc_18DCB'),
        (0x00000004, 'loc_18DD4'),
        (0x00000005, 'loc_18DDD'),
        (0x00000006, 'loc_18DE6'),
        (0x00000007, 'loc_18DEF'),
        (-1, 'loc_18DF8'),
    )

    def _loc_18DB9(): pass

    label('loc_18DB9')

    FormationAddMember(ChrTable['測試：妙婕制服測試'])

    Jump('loc_18DF8')

    def _loc_18DC2(): pass

    label('loc_18DC2')

    FormationAddMember(ChrTable['艾瑪'])

    Jump('loc_18DF8')

    def _loc_18DCB(): pass

    label('loc_18DCB')

    FormationAddMember(ChrTable['勞拉'])

    Jump('loc_18DF8')

    def _loc_18DD4(): pass

    label('loc_18DD4')

    FormationAddMember(ChrTable['蓋烏斯'])

    Jump('loc_18DF8')

    def _loc_18DDD(): pass

    label('loc_18DDD')

    FormationAddMember(ChrTable['馬奇亞斯'])

    Jump('loc_18DF8')

    def _loc_18DE6(): pass

    label('loc_18DE6')

    FormationAddMember(ChrTable['妙婕'])

    Jump('loc_18DF8')

    def _loc_18DEF(): pass

    label('loc_18DEF')

    FormationAddMember(ChrTable['庫爾特'])

    Jump('loc_18DF8')

    def _loc_18DF8(): pass

    label('loc_18DF8')

    Jump('loc_18FEB')

    def _loc_18DFD(): pass

    label('loc_18DFD')

    OP_C6(0x08, 0xFFFF, 0x00, 0x01, 0x01)
    OP_23(0x05, 0xFFFF, 0x0050, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '誰を誘いますか？\n',
            '（※チケットを１枚消費します）\n',
            '                                ',
            TxtCtl.Enter,
        ),
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, 'ユウナ', 0x00000001)
    MenuCmd(0x01, 0x00, 'アルティナ', 0x00000002)
    MenuCmd(0x01, 0x00, 'フィー', 0x00000003)
    MenuCmd(0x01, 0x00, 'デュバリィ', 0x00000004)
    MenuCmd(0x01, 0x00, 'アルフィン', 0x00000005)
    MenuCmd(0x01, 0x00, 'アッシュ', 0x00000006)
    MenuCmd(0x01, 0x00, 'ユーシス', 0x00000007)
    MenuCmd(0x02, 0x00, 0x00, 0xFFFF, 0x010E, 0x00)
    MenuCmd(0x04, 0x00, 0xF9)
    MenuCmd(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_C6(0x08, 0xFFFF, 0x00, 0xFF, 0x00)
    Call(ScriptId.System, 'FC_Kizuna_Sub_Point_Consume')

    Switch(
        (
            (Expr.Expr23, 0xF9),
            Expr.Return,
        ),
        (0x00000001, 'loc_18FA7'),
        (0x00000002, 'loc_18FB0'),
        (0x00000003, 'loc_18FB9'),
        (0x00000004, 'loc_18FC2'),
        (0x00000005, 'loc_18FCB'),
        (0x00000006, 'loc_18FD4'),
        (0x00000007, 'loc_18FDD'),
        (-1, 'loc_18FE6'),
    )

    def _loc_18FA7(): pass

    label('loc_18FA7')

    FormationAddMember(ChrTable['悠娜'])

    Jump('loc_18FE6')

    def _loc_18FB0(): pass

    label('loc_18FB0')

    FormationAddMember(ChrTable['亞爾緹娜'])

    Jump('loc_18FE6')

    def _loc_18FB9(): pass

    label('loc_18FB9')

    FormationAddMember(ChrTable['菲'])

    Jump('loc_18FE6')

    def _loc_18FC2(): pass

    label('loc_18FC2')

    FormationAddMember(ChrTable['杜巴莉'])

    Jump('loc_18FE6')

    def _loc_18FCB(): pass

    label('loc_18FCB')

    FormationAddMember(ChrTable['測試：杜巴莉'])

    Jump('loc_18FE6')

    def _loc_18FD4(): pass

    label('loc_18FD4')

    FormationAddMember(ChrTable['亞修'])

    Jump('loc_18FE6')

    def _loc_18FDD(): pass

    label('loc_18FDD')

    FormationAddMember(ChrTable['尤西斯'])

    Jump('loc_18FE6')

    def _loc_18FE6(): pass

    label('loc_18FE6')

    Jump('loc_18FEB')

    def _loc_18FEB(): pass

    label('loc_18FEB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008140, 'loc_19064'),
        (0x00008141, 'loc_19080'),
        (0x00008142, 'loc_1909C'),
        (0x00008143, 'loc_190B8'),
        (0x00008144, 'loc_190D4'),
        (0x00008146, 'loc_190F0'),
        (0x00008148, 'loc_1910C'),
        (0x00008149, 'loc_19128'),
        (0x0000814A, 'loc_19144'),
        (0x0000814B, 'loc_19160'),
        (0x0000814D, 'loc_1917C'),
        (0x0000814E, 'loc_19198'),
        (0x0000814F, 'loc_191B4'),
        (0x00008150, 'loc_191D0'),
        (-1, 'loc_191EC'),
    )

    def _loc_19064(): pass

    label('loc_19064')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x5010, 0x0))

    Jump('loc_191F1')

    def _loc_19080(): pass

    label('loc_19080')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8141, 0x0))

    Jump('loc_191F1')

    def _loc_1909C(): pass

    label('loc_1909C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8142, 0x0))

    Jump('loc_191F1')

    def _loc_190B8(): pass

    label('loc_190B8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8143, 0x0))

    Jump('loc_191F1')

    def _loc_190D4(): pass

    label('loc_190D4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8144, 0x0))

    Jump('loc_191F1')

    def _loc_190F0(): pass

    label('loc_190F0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8146, 0x0))

    Jump('loc_191F1')

    def _loc_1910C(): pass

    label('loc_1910C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8148, 0x0))

    Jump('loc_191F1')

    def _loc_19128(): pass

    label('loc_19128')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8149, 0x0))

    Jump('loc_191F1')

    def _loc_19144(): pass

    label('loc_19144')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x814A, 0x0))

    Jump('loc_191F1')

    def _loc_19160(): pass

    label('loc_19160')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x814B, 0x0))

    Jump('loc_191F1')

    def _loc_1917C(): pass

    label('loc_1917C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x814D, 0x0))

    Jump('loc_191F1')

    def _loc_19198(): pass

    label('loc_19198')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x814E, 0x0))

    Jump('loc_191F1')

    def _loc_191B4(): pass

    label('loc_191B4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x814F, 0x0))

    Jump('loc_191F1')

    def _loc_191D0(): pass

    label('loc_191D0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8150, 0x0))

    Jump('loc_191F1')

    def _loc_191EC(): pass

    label('loc_191EC')

    Jump('loc_191F1')

    def _loc_191F1(): pass

    label('loc_191F1')

    Jump('loc_181BD')

    def _loc_191F6(): pass

    label('loc_191F6')

    Return()

# id: 0x0075 offset: 0x191F8
@scena.Code('EV_KizunaJump_0X')
def EV_KizunaJump_0X():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_19201(): pass

    label('loc_19201')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19FDC',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[KZ0X00_00] [アナウンスが流れる　　　　　　]', 0x00008160)
    MenuCmd(0x01, 0x02, '[KZ0X01_00A][夜の自由行動が終わる・選択肢　]', 0x0000816B)
    MenuCmd(0x01, 0x02, '[KZ0X01_00] [夜の自由行動が終わる　　　　　]', 0x0000816C)
    MenuCmd(0x01, 0x02, '[KZ0X02_00] [男たちの一夜　　　　　　　　　]', 0x0000816D)
    MenuCmd(0x01, 0x02, '[KZ0X02_01] [夜の湖水浴場　　　　　　　　　]', 0x0000816E)
    MenuCmd(0x01, 0x02, '─────────────────────', 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 0, 0x5C80)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ユウナからの誘いを受けた　　　　　　　　', 0x00000001, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 1, 0x5C81)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'アルティナからの誘いを受けた　　　　　　', 0x00000002, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 2, 0x5C82)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ミュゼからの誘いを受けた　　　　　　　　', 0x00000003, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 3, 0x5C83)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'アリサと約束をした　　　　　　　　　　　', 0x00000004, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 4, 0x5C84)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ラウラと約束をした　　　　　　　　　　　', 0x00000005, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 5, 0x5C85)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'エマと約束をした　　　　　　　　　　　　', 0x00000006, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 6, 0x5C86)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'フィーと約束をした　　　　　　　　　　　', 0x00000007, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 7, 0x5C87)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'サラと約束をした　　　　　　　　　　　　', 0x00000008, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 0, 0x5C88)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'トワと約束をした　　　　　　　　　　　　', 0x00000009, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 1, 0x5C89)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'アルフィンからの誘いを受けた　　　　　　', 0x0000000A, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 2, 0x5C8A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'エリゼからの誘いを受けた　　　　　　　　', 0x0000000B, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x02, '《最終シーン分岐の判定テスト》', 0x00000064)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008160, 'loc_1984D'),
        (0x0000816B, 'loc_1984D'),
        (0x0000816C, 'loc_1984D'),
        (0x0000816D, 'loc_1984D'),
        (0x0000816E, 'loc_1984D'),
        (0x00000000, 'loc_1986F'),
        (0x00000001, 'loc_19874'),
        (0x00000002, 'loc_1987C'),
        (0x00000003, 'loc_19884'),
        (0x00000004, 'loc_1988C'),
        (0x00000005, 'loc_19894'),
        (0x00000006, 'loc_1989C'),
        (0x00000007, 'loc_198A4'),
        (0x00000008, 'loc_198AC'),
        (0x00000009, 'loc_198B4'),
        (0x0000000A, 'loc_198BC'),
        (0x0000000B, 'loc_198C4'),
        (0x00000064, 'loc_198CC'),
        (-1, 'loc_19E0F'),
    )

    def _loc_1984D(): pass

    label('loc_1984D')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')

    Jump('loc_19E1D')

    def _loc_1986F(): pass

    label('loc_1986F')

    Jump('loc_19E1D')

    def _loc_19874(): pass

    label('loc_19874')

    OP_12(0x5C80)

    Jump('loc_19E1D')

    def _loc_1987C(): pass

    label('loc_1987C')

    OP_12(0x5C81)

    Jump('loc_19E1D')

    def _loc_19884(): pass

    label('loc_19884')

    OP_12(0x5C82)

    Jump('loc_19E1D')

    def _loc_1988C(): pass

    label('loc_1988C')

    OP_12(0x5C83)

    Jump('loc_19E1D')

    def _loc_19894(): pass

    label('loc_19894')

    OP_12(0x5C84)

    Jump('loc_19E1D')

    def _loc_1989C(): pass

    label('loc_1989C')

    OP_12(0x5C85)

    Jump('loc_19E1D')

    def _loc_198A4(): pass

    label('loc_198A4')

    OP_12(0x5C86)

    Jump('loc_19E1D')

    def _loc_198AC(): pass

    label('loc_198AC')

    OP_12(0x5C87)

    Jump('loc_19E1D')

    def _loc_198B4(): pass

    label('loc_198B4')

    OP_12(0x5C88)

    Jump('loc_19E1D')

    def _loc_198BC(): pass

    label('loc_198BC')

    OP_12(0x5C89)

    Jump('loc_19E1D')

    def _loc_198C4(): pass

    label('loc_198C4')

    OP_12(0x5C8A)

    Jump('loc_19E1D')

    def _loc_198CC(): pass

    label('loc_198CC')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 0, 0x5C80)),
            Expr.Return,
        ),
        'loc_198E7',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_198E7(): pass

    label('loc_198E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 1, 0x5C81)),
            Expr.Return,
        ),
        'loc_198F9',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_198F9(): pass

    label('loc_198F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 2, 0x5C82)),
            Expr.Return,
        ),
        'loc_1990B',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1990B(): pass

    label('loc_1990B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 1, 0x5C89)),
            Expr.Return,
        ),
        'loc_1991D',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1991D(): pass

    label('loc_1991D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 2, 0x5C8A)),
            Expr.Return,
        ),
        'loc_1992F',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1992F(): pass

    label('loc_1992F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 3, 0x5C83)),
            Expr.Return,
        ),
        'loc_19941',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x100),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_19941(): pass

    label('loc_19941')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 4, 0x5C84)),
            Expr.Return,
        ),
        'loc_19953',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x200),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_19953(): pass

    label('loc_19953')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 5, 0x5C85)),
            Expr.Return,
        ),
        'loc_19965',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x400),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_19965(): pass

    label('loc_19965')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 6, 0x5C86)),
            Expr.Return,
        ),
        'loc_19977',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x800),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_19977(): pass

    label('loc_19977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 7, 0x5C87)),
            Expr.Return,
        ),
        'loc_19989',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x1000),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_19989(): pass

    label('loc_19989')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 0, 0x5C88)),
            Expr.Return,
        ),
        'loc_1999B',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x2000),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1999B(): pass

    label('loc_1999B')

    OP_23(0x05, 0xFFFF, 0x00A0, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '仮・最後に過ごす相手を選んでください。',
            TxtCtl.ShowAll,
            0x8,
            TxtCtl.Enter,
        ),
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 0, 0x5C80)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'ユウナ', 0x00000001, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 1, 0x5C81)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'アルティナ', 0x00000002, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 2, 0x5C82)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'ミュゼ', 0x00000004, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 3, 0x5C83)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'アリサ', 0x00000100, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 4, 0x5C84)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'ラウラ', 0x00000200, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 5, 0x5C85)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'エマ', 0x00000400, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 6, 0x5C86)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'フィー', 0x00000800, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B90, 7, 0x5C87)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'サラ', 0x00001000, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 0, 0x5C88)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'トワ', 0x00002000, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 1, 0x5C89)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'アルフィン', 0x00000008, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B91, 2, 0x5C8A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, 'エリゼ', 0x00000010, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x02, 0x00, 0x00, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x00, 0xF7)
    MenuCmd(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    If(
        (
            (Expr.Expr23, 0xF6),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C1E',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '約束をしているキャラも\n',
            '誘いを受けたキャラもいません。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_19E01')

    def _loc_19C1E(): pass

    label('loc_19C1E')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.Expr23, 0xF6),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C87',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '選んだキャラは、約束も誘いもないキャラです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_19E01')

    def _loc_19C87(): pass

    label('loc_19C87')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFF00),
            Expr.And,
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFF00),
            Expr.And,
            Expr.Xor,
            Expr.Return,
        ),
        'loc_19CFE',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '選んだキャラが以外に約束をしたキャラがいます。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_19E01')

    def _loc_19CFE(): pass

    label('loc_19CFE')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFF),
            Expr.And,
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFF),
            Expr.And,
            Expr.Xor,
            Expr.Return,
        ),
        'loc_19DA0',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '選んだキャラが以外に約束をしたキャラはいませんが、\n',
            '誘われたキャラはいます。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    Jump('loc_19E01')

    def _loc_19DA0(): pass

    label('loc_19DA0')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '約束か誘いがあったのは一人で、その人を選びました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)

    def _loc_19E01(): pass

    label('loc_19E01')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_19E1D')

    def _loc_19E0F(): pass

    label('loc_19E0F')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_19E1D')

    def _loc_19E1D(): pass

    label('loc_19E1D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xD),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19E3D',
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_19E3D(): pass

    label('loc_19E3D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19E6A',
    )

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_19E6A(): pass

    label('loc_19E6A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000816E, 'loc_19E9B'),
        (0x0000816D, 'loc_19E9E'),
        (0x0000816C, 'loc_19EA1'),
        (0x0000816B, 'loc_19EA4'),
        (0x00008160, 'loc_19EAD'),
        (-1, 'loc_19EBB'),
    )

    def _loc_19E9B(): pass

    label('loc_19E9B')

    SetScenaFlags(ScenaFlag(0x0B76, 7, 0x5BB7))

    def _loc_19E9E(): pass

    label('loc_19E9E')

    SetScenaFlags(ScenaFlag(0x0B76, 6, 0x5BB6))

    def _loc_19EA1(): pass

    label('loc_19EA1')

    SetScenaFlags(ScenaFlag(0x0B76, 5, 0x5BB5))

    def _loc_19EA4(): pass

    label('loc_19EA4')

    SetScenaFlags(ScenaFlag(0x0B76, 3, 0x5BB3))
    SetScenaFlags(ScenaFlag(0x0B76, 4, 0x5BB4))
    SetScenaFlags(ScenaFlag(0x0981, 4, 0x4C0C))

    def _loc_19EAD(): pass

    label('loc_19EAD')

    OP_71(0x00, 0x4C04, 0x4C0B)
    SetScenaFlags(ScenaFlag(0x0982, 1, 0x4C11))

    Jump('loc_19EBB')

    def _loc_19EBB(): pass

    label('loc_19EBB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008160, 'loc_19EEC'),
        (0x0000816B, 'loc_19F08'),
        (0x0000816C, 'loc_19F7E'),
        (0x0000816D, 'loc_19F9A'),
        (0x0000816E, 'loc_19FB6'),
        (-1, 'loc_19FD2'),
    )

    def _loc_19EEC(): pass

    label('loc_19EEC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8162, 0x0))

    Jump('loc_19FD7')

    def _loc_19F08(): pass

    label('loc_19F08')

    CreateChr(ChrTable['黎恩'], 'C_CHR000', 'リィン', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    Call(ScriptId.System4, 'SB_KZ0X01_00A')
    OP_28((0xDD, 'f4010'), (0xDD, 'go_f4000'), 0x00)

    Jump('loc_19FD7')

    def _loc_19F7E(): pass

    label('loc_19F7E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x816C, 0x0))

    Jump('loc_19FD7')

    def _loc_19F9A(): pass

    label('loc_19F9A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x816D, 0x0))

    Jump('loc_19FD7')

    def _loc_19FB6(): pass

    label('loc_19FB6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x816E, 0x0))

    Jump('loc_19FD7')

    def _loc_19FD2(): pass

    label('loc_19FD2')

    Jump('loc_19FD7')

    def _loc_19FD7(): pass

    label('loc_19FD7')

    Jump('loc_19201')

    def _loc_19FDC(): pass

    label('loc_19FDC')

    Return()

# id: 0x0076 offset: 0x19FE0
@scena.Code('EV_SubeventJump')
def EV_SubeventJump():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_19FE9(): pass

    label('loc_19FE9')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AB0C',
    )

    MenuCmd(0x00, 0x01, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '[SB_00_00] [序・エリンの里　　　　　　　　　] ＞', 0x00000001)
    MenuCmd(0x01, 0x01, '[SB_01B_00][Ⅰ部サザーラント編・セントアーク] ＞', 0x00000002)
    MenuCmd(0x01, 0x01, '[SB_01C_00][Ⅰ部ラマール編・エリンの里　　　] ＞', 0x00000003)
    MenuCmd(0x01, 0x01, '[SB_01C_01][Ⅰ部ラマール編・ミルサンテ　　　] ＞', 0x00000004)
    MenuCmd(0x01, 0x01, '[SB_01C_02][Ⅰ部ラマール編・ラクウェル　　　] ＞', 0x00000005)
    MenuCmd(0x01, 0x01, '[SB_01C_04][Ⅰ部ラマール編・アルスター　　　] ＞', 0x00000006)
    MenuCmd(0x01, 0x01, '[SB_01D_00][Ⅰ部クロスベル編・エリンの里　　] ＞', 0x00000007)
    MenuCmd(0x01, 0x01, '[SB_01D_01][Ⅰ部クロスベル編・山猫号内部　　] ＞', 0x00000008)
    MenuCmd(0x01, 0x01, '[SB_01D_02][Ⅰ部クロスベル編・クロスベル市内] ＞', 0x00000009)
    MenuCmd(0x01, 0x01, '[SB_01D_03][Ⅰ部クロスベル編・ミシュラム　　] ＞', 0x0000000A)
    MenuCmd(0x01, 0x01, '[SB_01X_00][断章・エリンの里　　　　　　　　] ＞', 0x0000000B)
    MenuCmd(0x01, 0x01, '[SB_02A_00][Ⅱ部・エリンの里　　　　　　　　] ＞', 0x0000000C)
    MenuCmd(0x01, 0x01, '[SB_02A_01][Ⅱ部・メルカバ　　　　　　　　　] ＞', 0x0000000D)
    MenuCmd(0x01, 0x01, '[SB_02A_02][Ⅱ部ブリオニア編　　　　　　　　] ＞', 0x0000000E)
    MenuCmd(0x01, 0x01, '[SB_02B_00][Ⅱ部オルディス編　　　　　　　　] ＞', 0x0000000F)
    MenuCmd(0x01, 0x01, '[SB_02C_00][Ⅱ部ドレックノール編　　　　　　] ＞', 0x00000010)
    MenuCmd(0x01, 0x01, '[SB_02D_00][Ⅱ部リーヴス編・ミルサンテ　　　] ＞', 0x00000011)
    MenuCmd(0x01, 0x01, '[SB_02D_01][Ⅱ部リーヴス編・リーヴス　　　　] ＞', 0x00000012)
    MenuCmd(0x01, 0x01, '[SB_02D_02][Ⅱ部リーヴス編・第Ⅱ分校　　　　] ＞', 0x00000013)
    MenuCmd(0x01, 0x01, '[SB_02E_00][Ⅱ部パンタグリュエル編　　　　　] ＞', 0x00000014)
    MenuCmd(0x01, 0x01, '[SB_03A_00][Ⅲ部・カレイジャス　　　　　　　] ＞', 0x00000015)
    MenuCmd(0x01, 0x01, '[SB_03B_00][Ⅲ部・ガルガンチュア編　　　　　] ＞', 0x00000016)
    MenuCmd(0x01, 0x01, '[SB_03D_00][Ⅲ部・裏オルキスタワー編　　　　] ＞', 0x00000017)
    MenuCmd(0x01, 0x01, '[SB_03E_00][Ⅲ部・星の霊場編・ウルスラ病院　] ＞', 0x00000018)
    MenuCmd(0x01, 0x01, '[SB_03X_00][前日譚・ミシュラム　　　　　　　] ＞', 0x00000019)
    MenuCmd(0x01, 0x01, '[SB_04_00] [最終幕　　　　　　　　　　　　　] ＞', 0x0000001A)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_1A857'),
        (0x00000002, 'loc_1A870'),
        (0x00000003, 'loc_1A88A'),
        (0x00000004, 'loc_1A8A4'),
        (0x00000005, 'loc_1A8BE'),
        (0x00000006, 'loc_1A8D8'),
        (0x00000007, 'loc_1A8F2'),
        (0x00000008, 'loc_1A90C'),
        (0x00000009, 'loc_1A926'),
        (0x0000000A, 'loc_1A940'),
        (0x0000000B, 'loc_1A95A'),
        (0x0000000C, 'loc_1A974'),
        (0x0000000D, 'loc_1A98E'),
        (0x0000000E, 'loc_1A9A8'),
        (0x0000000F, 'loc_1A9C2'),
        (0x00000010, 'loc_1A9DC'),
        (0x00000011, 'loc_1A9F6'),
        (0x00000012, 'loc_1AA10'),
        (0x00000013, 'loc_1AA2A'),
        (0x00000014, 'loc_1AA44'),
        (0x00000015, 'loc_1AA5E'),
        (0x00000016, 'loc_1AA78'),
        (0x00000017, 'loc_1AA92'),
        (0x00000018, 'loc_1AAAC'),
        (0x00000019, 'loc_1AAC6'),
        (0x0000001A, 'loc_1AAE0'),
        (-1, 'loc_1AAF9'),
    )

    def _loc_1A857(): pass

    label('loc_1A857')

    Call(ScriptId.Current, 'EV_Jump_SB_00_00')

    Jump('loc_1AB07')

    def _loc_1A870(): pass

    label('loc_1A870')

    Call(ScriptId.Current, 'EV_Jump_SB_01B_00')

    Jump('loc_1AB07')

    def _loc_1A88A(): pass

    label('loc_1A88A')

    Call(ScriptId.Current, 'EV_Jump_SB_01C_00')

    Jump('loc_1AB07')

    def _loc_1A8A4(): pass

    label('loc_1A8A4')

    Call(ScriptId.Current, 'EV_Jump_SB_01C_01')

    Jump('loc_1AB07')

    def _loc_1A8BE(): pass

    label('loc_1A8BE')

    Call(ScriptId.Current, 'EV_Jump_SB_01C_02')

    Jump('loc_1AB07')

    def _loc_1A8D8(): pass

    label('loc_1A8D8')

    Call(ScriptId.Current, 'EV_Jump_SB_01C_04')

    Jump('loc_1AB07')

    def _loc_1A8F2(): pass

    label('loc_1A8F2')

    Call(ScriptId.Current, 'EV_Jump_SB_01D_00')

    Jump('loc_1AB07')

    def _loc_1A90C(): pass

    label('loc_1A90C')

    Call(ScriptId.Current, 'EV_Jump_SB_01D_01')

    Jump('loc_1AB07')

    def _loc_1A926(): pass

    label('loc_1A926')

    Call(ScriptId.Current, 'EV_Jump_SB_01D_02')

    Jump('loc_1AB07')

    def _loc_1A940(): pass

    label('loc_1A940')

    Call(ScriptId.Current, 'EV_Jump_SB_01D_03')

    Jump('loc_1AB07')

    def _loc_1A95A(): pass

    label('loc_1A95A')

    Call(ScriptId.Current, 'EV_Jump_SB_01X_00')

    Jump('loc_1AB07')

    def _loc_1A974(): pass

    label('loc_1A974')

    Call(ScriptId.Current, 'EV_Jump_SB_02A_00')

    Jump('loc_1AB07')

    def _loc_1A98E(): pass

    label('loc_1A98E')

    Call(ScriptId.Current, 'EV_Jump_SB_02A_01')

    Jump('loc_1AB07')

    def _loc_1A9A8(): pass

    label('loc_1A9A8')

    Call(ScriptId.Current, 'EV_Jump_SB_02A_02')

    Jump('loc_1AB07')

    def _loc_1A9C2(): pass

    label('loc_1A9C2')

    Call(ScriptId.Current, 'EV_Jump_SB_02B_00')

    Jump('loc_1AB07')

    def _loc_1A9DC(): pass

    label('loc_1A9DC')

    Call(ScriptId.Current, 'EV_Jump_SB_02C_00')

    Jump('loc_1AB07')

    def _loc_1A9F6(): pass

    label('loc_1A9F6')

    Call(ScriptId.Current, 'EV_Jump_SB_02D_00')

    Jump('loc_1AB07')

    def _loc_1AA10(): pass

    label('loc_1AA10')

    Call(ScriptId.Current, 'EV_Jump_SB_02D_01')

    Jump('loc_1AB07')

    def _loc_1AA2A(): pass

    label('loc_1AA2A')

    Call(ScriptId.Current, 'EV_Jump_SB_02D_02')

    Jump('loc_1AB07')

    def _loc_1AA44(): pass

    label('loc_1AA44')

    Call(ScriptId.Current, 'EV_Jump_SB_02E_00')

    Jump('loc_1AB07')

    def _loc_1AA5E(): pass

    label('loc_1AA5E')

    Call(ScriptId.Current, 'EV_Jump_SB_03A_00')

    Jump('loc_1AB07')

    def _loc_1AA78(): pass

    label('loc_1AA78')

    Call(ScriptId.Current, 'EV_Jump_SB_03B_00')

    Jump('loc_1AB07')

    def _loc_1AA92(): pass

    label('loc_1AA92')

    Call(ScriptId.Current, 'EV_Jump_SB_03D_00')

    Jump('loc_1AB07')

    def _loc_1AAAC(): pass

    label('loc_1AAAC')

    Call(ScriptId.Current, 'EV_Jump_SB_03E_00')

    Jump('loc_1AB07')

    def _loc_1AAC6(): pass

    label('loc_1AAC6')

    Call(ScriptId.Current, 'EV_Jump_SB_03X_00')

    Jump('loc_1AB07')

    def _loc_1AAE0(): pass

    label('loc_1AAE0')

    Call(ScriptId.Current, 'EV_Jump_SB_04_00')

    Jump('loc_1AB07')

    def _loc_1AAF9(): pass

    label('loc_1AAF9')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1AB07')

    def _loc_1AB07(): pass

    label('loc_1AB07')

    Jump('loc_19FE9')

    def _loc_1AB0C(): pass

    label('loc_1AB0C')

    Return()

# id: 0x0077 offset: 0x1AB10
@scena.Code('EV_Jump_SB_00_00')
def EV_Jump_SB_00_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1AB19(): pass

    label('loc_1AB19')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B0F1',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_00_01_00][ラウラとの会話　　　　　　　　]', 0x00008180)
    MenuCmd(0x01, 0x02, '[SB_00_01_01][アリサとの会話　　　　　　　　]', 0x00008181)
    MenuCmd(0x01, 0x02, '[SB_00_01_02][ユーシスとの会話　　　　　　　]', 0x00008182)
    MenuCmd(0x01, 0x02, '[SB_00_01_03][アトリエに戻ることにする　　　]', 0x00008183)
    MenuCmd(0x01, 0x02, '[SB_00_01_04][アトリエに戻る・選択肢　　　　]', 0x00008185)
    MenuCmd(0x01, 0x02, '[SB_00_01_05][エリオット＆ガイウスとの会話　]', 0x00008186)
    MenuCmd(0x01, 0x02, '[SB_00_01_06][フィー＆サラとの会話　　　　　]', 0x00008187)
    MenuCmd(0x01, 0x02, '[SB_00_01_07][マキアス＆ランディとの会話　　]', 0x00008188)
    MenuCmd(0x01, 0x02, '[SB_00_01_08][エマ＆ロゼとの会話　　　　　　]', 0x00008189)
    MenuCmd(0x01, 0x02, '[SB_00_01_09][妖精の湯を確認する　　　　　　]', 0x0000818A)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008180, 'loc_1AE45'),
        (0x00008181, 'loc_1AE45'),
        (0x00008182, 'loc_1AE45'),
        (0x00008183, 'loc_1AE45'),
        (0x00008185, 'loc_1AE45'),
        (0x00008186, 'loc_1AE45'),
        (0x00008187, 'loc_1AE45'),
        (0x00008188, 'loc_1AE45'),
        (0x00008189, 'loc_1AE45'),
        (0x0000818A, 'loc_1AE45'),
        (-1, 'loc_1AE53'),
    )

    def _loc_1AE45(): pass

    label('loc_1AE45')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x39),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1AE61')

    def _loc_1AE53(): pass

    label('loc_1AE53')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1AE61')

    def _loc_1AE61(): pass

    label('loc_1AE61')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AE98',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_00')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1AE98(): pass

    label('loc_1AE98')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008180, 'loc_1AEF1'),
        (0x00008181, 'loc_1AF0D'),
        (0x00008182, 'loc_1AF29'),
        (0x00008183, 'loc_1AF45'),
        (0x00008185, 'loc_1AF70'),
        (0x00008186, 'loc_1B05B'),
        (0x00008187, 'loc_1B077'),
        (0x00008188, 'loc_1B093'),
        (0x00008189, 'loc_1B0AF'),
        (0x0000818A, 'loc_1B0CB'),
        (-1, 'loc_1B0E7'),
    )

    def _loc_1AEF1(): pass

    label('loc_1AEF1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8180, 0x0))

    Jump('loc_1B0EC')

    def _loc_1AF0D(): pass

    label('loc_1AF0D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8181, 0x0))

    Jump('loc_1B0EC')

    def _loc_1AF29(): pass

    label('loc_1AF29')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8182, 0x0))

    Jump('loc_1B0EC')

    def _loc_1AF45(): pass

    label('loc_1AF45')

    SetScenaFlags(ScenaFlag(0x0534, 1, 0x29A1))
    OP_71(0x00, 0x29C0, 0x29C2)
    OP_71(0x00, 0x29C7, 0x29CA)
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8184, 0x0))

    Jump('loc_1B0EC')

    def _loc_1AF70(): pass

    label('loc_1AF70')

    SetScenaFlags(ScenaFlag(0x0534, 1, 0x29A1))
    OP_71(0x00, 0x29C0, 0x29C3)
    OP_71(0x00, 0x29C7, 0x29CA)
    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ＬＰの前（正面玄関）で操作許可にします。そのまま調べて下さい。\n',
            '勝手口を調べる場合は移動して下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8185, 0x0))

    Jump('loc_1B0EC')

    def _loc_1B05B(): pass

    label('loc_1B05B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8186, 0x0))

    Jump('loc_1B0EC')

    def _loc_1B077(): pass

    label('loc_1B077')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8187, 0x0))

    Jump('loc_1B0EC')

    def _loc_1B093(): pass

    label('loc_1B093')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8188, 0x0))

    Jump('loc_1B0EC')

    def _loc_1B0AF(): pass

    label('loc_1B0AF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8189, 0x0))

    Jump('loc_1B0EC')

    def _loc_1B0CB(): pass

    label('loc_1B0CB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x818A, 0x0))

    Jump('loc_1B0EC')

    def _loc_1B0E7(): pass

    label('loc_1B0E7')

    Jump('loc_1B0EC')

    def _loc_1B0EC(): pass

    label('loc_1B0EC')

    Jump('loc_1AB19')

    def _loc_1B0F1(): pass

    label('loc_1B0F1')

    Return()

# id: 0x0078 offset: 0x1B0F4
@scena.Code('EV_Jump_SB_01B_00')
def EV_Jump_SB_01B_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B0FD(): pass

    label('loc_1B0FD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B3DA',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01B_00_00][宿酒場で徴兵の話を聞く　　　　]', 0x0000818B)
    MenuCmd(0x01, 0x02, '[SB_01B_00_01][城館前で衛士隊を見かける　　　]', 0x0000818C)
    MenuCmd(0x01, 0x02, '[SB_01B_00_02][大聖堂でフィオナと会う　　　　]', 0x0000818D)
    MenuCmd(0x01, 0x02, '[SB_01B_01_00][北サザーラント街道に出る　　　]', 0x0000818E)
    MenuCmd(0x01, 0x02, '[SB_01B_01_01][検問を見かける　　　　　　　　]', 0x0000818F)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000818B, 'loc_1B2B2'),
        (0x0000818C, 'loc_1B2B2'),
        (0x0000818D, 'loc_1B2B2'),
        (0x0000818E, 'loc_1B2C0'),
        (0x0000818F, 'loc_1B2C0'),
        (-1, 'loc_1B2CE'),
    )

    def _loc_1B2B2(): pass

    label('loc_1B2B2')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x101C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B2DC')

    def _loc_1B2C0(): pass

    label('loc_1B2C0')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x101F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B2DC')

    def _loc_1B2CE(): pass

    label('loc_1B2CE')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B2DC')

    def _loc_1B2DC(): pass

    label('loc_1B2DC')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B313',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1B313(): pass

    label('loc_1B313')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000818B, 'loc_1B344'),
        (0x0000818C, 'loc_1B360'),
        (0x0000818D, 'loc_1B37C'),
        (0x0000818E, 'loc_1B398'),
        (0x0000818F, 'loc_1B3B4'),
        (-1, 'loc_1B3D0'),
    )

    def _loc_1B344(): pass

    label('loc_1B344')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x818B, 0x0))

    Jump('loc_1B3D5')

    def _loc_1B360(): pass

    label('loc_1B360')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x818C, 0x0))

    Jump('loc_1B3D5')

    def _loc_1B37C(): pass

    label('loc_1B37C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x818D, 0x0))

    Jump('loc_1B3D5')

    def _loc_1B398(): pass

    label('loc_1B398')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x818E, 0x0))

    Jump('loc_1B3D5')

    def _loc_1B3B4(): pass

    label('loc_1B3B4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x818F, 0x0))

    Jump('loc_1B3D5')

    def _loc_1B3D0(): pass

    label('loc_1B3D0')

    Jump('loc_1B3D5')

    def _loc_1B3D5(): pass

    label('loc_1B3D5')

    Jump('loc_1B0FD')

    def _loc_1B3DA(): pass

    label('loc_1B3DA')

    Return()

# id: 0x0079 offset: 0x1B3DC
@scena.Code('EV_Jump_SB_01C_00')
def EV_Jump_SB_01C_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B3E5(): pass

    label('loc_1B3E5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B4F0',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01C_00_00][アッシュとの会話　　　　　　　]', 0x00008190)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008190, 'loc_1B466'),
        (-1, 'loc_1B474'),
    )

    def _loc_1B466(): pass

    label('loc_1B466')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1052),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B482')

    def _loc_1B474(): pass

    label('loc_1B474')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B482')

    def _loc_1B482(): pass

    label('loc_1B482')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B4B9',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1B4B9(): pass

    label('loc_1B4B9')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008190, 'loc_1B4CA'),
        (-1, 'loc_1B4E6'),
    )

    def _loc_1B4CA(): pass

    label('loc_1B4CA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8190, 0x0))

    Jump('loc_1B4EB')

    def _loc_1B4E6(): pass

    label('loc_1B4E6')

    Jump('loc_1B4EB')

    def _loc_1B4EB(): pass

    label('loc_1B4EB')

    Jump('loc_1B3E5')

    def _loc_1B4F0(): pass

    label('loc_1B4F0')

    Return()

# id: 0x007A offset: 0x1B4F4
@scena.Code('EV_Jump_SB_01C_01')
def EV_Jump_SB_01C_01():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B4FD(): pass

    label('loc_1B4FD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B80F',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01C_01_00][宿酒場でシドニーと再会　　　　]', 0x00008191)
    MenuCmd(0x01, 0x02, '[SB_01C_01_01][雑貨・工房に入る　　　　　　　]', 0x00008192)
    MenuCmd(0x01, 0x02, '[SB_01C_01_02][雑貨屋でディアナと話す　　　　]', 0x00008193)
    MenuCmd(0x01, 0x02, '[SB_01C_01_03][シドニーと会った後のディアナ　]', 0x00008194)
    MenuCmd(0x01, 0x02, '[SB_01C_01_10][アナベルと再会　　　　　　　　]', 0x00008195)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008191, 'loc_1B6B2'),
        (0x00008192, 'loc_1B6B2'),
        (0x00008193, 'loc_1B6B2'),
        (0x00008194, 'loc_1B6B2'),
        (0x00008195, 'loc_1B6C0'),
        (-1, 'loc_1B6CE'),
    )

    def _loc_1B6B2(): pass

    label('loc_1B6B2')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x105C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B6DC')

    def _loc_1B6C0(): pass

    label('loc_1B6C0')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x105E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B6DC')

    def _loc_1B6CE(): pass

    label('loc_1B6CE')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B6DC')

    def _loc_1B6DC(): pass

    label('loc_1B6DC')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B713',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1B713(): pass

    label('loc_1B713')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008194, 'loc_1B734'),
        (0x00008191, 'loc_1B73A'),
        (0x00008193, 'loc_1B740'),
        (-1, 'loc_1B748'),
    )

    def _loc_1B734(): pass

    label('loc_1B734')

    SetScenaFlags(ScenaFlag(0x05A1, 0, 0x2D08))
    SetScenaFlags(ScenaFlag(0x05B0, 5, 0x2D85))

    def _loc_1B73A(): pass

    label('loc_1B73A')

    SetScenaFlags(ScenaFlag(0x05A0, 7, 0x2D07))
    SetScenaFlags(ScenaFlag(0x05B0, 7, 0x2D87))

    def _loc_1B740(): pass

    label('loc_1B740')

    SetScenaFlags(ScenaFlag(0x05B0, 6, 0x2D86))

    Jump('loc_1B748')

    def _loc_1B748(): pass

    label('loc_1B748')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008191, 'loc_1B779'),
        (0x00008192, 'loc_1B795'),
        (0x00008193, 'loc_1B7B1'),
        (0x00008194, 'loc_1B7CD'),
        (0x00008195, 'loc_1B7E9'),
        (-1, 'loc_1B805'),
    )

    def _loc_1B779(): pass

    label('loc_1B779')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8191, 0x0))

    Jump('loc_1B80A')

    def _loc_1B795(): pass

    label('loc_1B795')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8192, 0x0))

    Jump('loc_1B80A')

    def _loc_1B7B1(): pass

    label('loc_1B7B1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8193, 0x0))

    Jump('loc_1B80A')

    def _loc_1B7CD(): pass

    label('loc_1B7CD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8194, 0x0))

    Jump('loc_1B80A')

    def _loc_1B7E9(): pass

    label('loc_1B7E9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8195, 0x0))

    Jump('loc_1B80A')

    def _loc_1B805(): pass

    label('loc_1B805')

    Jump('loc_1B80A')

    def _loc_1B80A(): pass

    label('loc_1B80A')

    Jump('loc_1B4FD')

    def _loc_1B80F(): pass

    label('loc_1B80F')

    Return()

# id: 0x007B offset: 0x1B810
@scena.Code('EV_Jump_SB_01C_02')
def EV_Jump_SB_01C_02():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B819(): pass

    label('loc_1B819')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BC0E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01C_02_00][教会でシスター・オルファと話す]', 0x00008196)
    MenuCmd(0x01, 0x02, '[SB_01C_02_01][パブでモーリー＆ブラッドと話す]', 0x00008197)
    MenuCmd(0x01, 0x02, '[SB_01C_02_02][バーでジュリアと話す　　　　　]', 0x00008198)
    MenuCmd(0x01, 0x02, '[SB_01C_03_00][ミゲルと遭遇　　　　　　　　　]', 0x00008199)
    MenuCmd(0x01, 0x02, '[SB_01C_03_01][峡谷地帯への道の封鎖を見かける]', 0x0000819A)
    MenuCmd(0x01, 0x02, '[SB_01C_03_02][アッシュの部屋を訪ねる　　　　]', 0x0000819B)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008196, 'loc_1BA1B'),
        (0x00008197, 'loc_1BA1B'),
        (0x00008198, 'loc_1BA1B'),
        (0x0000819B, 'loc_1BA29'),
        (0x00008199, 'loc_1BA29'),
        (0x0000819A, 'loc_1BA37'),
        (-1, 'loc_1BA45'),
    )

    def _loc_1BA1B(): pass

    label('loc_1BA1B')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1061),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BA53')

    def _loc_1BA29(): pass

    label('loc_1BA29')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1065),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BA53')

    def _loc_1BA37(): pass

    label('loc_1BA37')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1067),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BA53')

    def _loc_1BA45(): pass

    label('loc_1BA45')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BA53')

    def _loc_1BA53(): pass

    label('loc_1BA53')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BA8A',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1BA8A(): pass

    label('loc_1BA8A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008196, 'loc_1BAC3'),
        (0x00008197, 'loc_1BADF'),
        (0x00008198, 'loc_1BAFB'),
        (0x0000819B, 'loc_1BB17'),
        (0x00008199, 'loc_1BB33'),
        (0x0000819A, 'loc_1BB52'),
        (-1, 'loc_1BC04'),
    )

    def _loc_1BAC3(): pass

    label('loc_1BAC3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8196, 0x0))

    Jump('loc_1BC09')

    def _loc_1BADF(): pass

    label('loc_1BADF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8197, 0x0))

    Jump('loc_1BC09')

    def _loc_1BAFB(): pass

    label('loc_1BAFB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8198, 0x0))

    Jump('loc_1BC09')

    def _loc_1BB17(): pass

    label('loc_1BB17')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x819B, 0x0))

    Jump('loc_1BC09')

    def _loc_1BB33(): pass

    label('loc_1BB33')

    SetScenaFlags(ScenaFlag(0x05B1, 7, 0x2D8F))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8199, 0x0))

    Jump('loc_1BC09')

    def _loc_1BB52(): pass

    label('loc_1BB52')

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ストッパーの前で操作許可にします。\n',
            'そのまま柵に向かって移動して下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x819A, 0x0))

    Jump('loc_1BC09')

    def _loc_1BC04(): pass

    label('loc_1BC04')

    Jump('loc_1BC09')

    def _loc_1BC09(): pass

    label('loc_1BC09')

    Jump('loc_1B819')

    def _loc_1BC0E(): pass

    label('loc_1BC0E')

    Return()

# id: 0x007C offset: 0x1BC10
@scena.Code('EV_Jump_SB_01C_04')
def EV_Jump_SB_01C_04():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1BC19(): pass

    label('loc_1BC19')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BF59',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01C_04_00][カイ・ティーリアの家に近づく　]', 0x0000819C)
    MenuCmd(0x01, 0x02, '[SB_01C_04_01][カイ・ティーリアと話す　　　　]', 0x0000819D)
    MenuCmd(0x01, 0x02, '[SB_01C_04_02][蒸留所を訪れる　　　　　　　　]', 0x0000819E)
    MenuCmd(0x01, 0x02, '[SB_01C_04_03][蒸留所でメモを見つける　　　　]', 0x0000819F)
    MenuCmd(0x01, 0x02, '[SB_01C_04_04][レンハイム家跡地に訪れる　　　]', 0x000081A0)
    MenuCmd(0x01, 0x02, '[SB_01C_04_05][ニールセンとの会話　　　　　　]', 0x000081A1)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000819C, 'loc_1BE1B'),
        (0x0000819D, 'loc_1BE1B'),
        (0x0000819E, 'loc_1BE1B'),
        (0x0000819F, 'loc_1BE1B'),
        (0x000081A0, 'loc_1BE1B'),
        (0x000081A1, 'loc_1BE1B'),
        (-1, 'loc_1BE29'),
    )

    def _loc_1BE1B(): pass

    label('loc_1BE1B')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x106F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BE37')

    def _loc_1BE29(): pass

    label('loc_1BE29')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BE37')

    def _loc_1BE37(): pass

    label('loc_1BE37')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BE6E',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1BE6E(): pass

    label('loc_1BE6E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000819C, 'loc_1BEA7'),
        (0x0000819D, 'loc_1BEC3'),
        (0x0000819E, 'loc_1BEDF'),
        (0x0000819F, 'loc_1BEFB'),
        (0x000081A0, 'loc_1BF17'),
        (0x000081A1, 'loc_1BF33'),
        (-1, 'loc_1BF4F'),
    )

    def _loc_1BEA7(): pass

    label('loc_1BEA7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x819C, 0x0))

    Jump('loc_1BF54')

    def _loc_1BEC3(): pass

    label('loc_1BEC3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x819D, 0x0))

    Jump('loc_1BF54')

    def _loc_1BEDF(): pass

    label('loc_1BEDF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x819E, 0x0))

    Jump('loc_1BF54')

    def _loc_1BEFB(): pass

    label('loc_1BEFB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x819F, 0x0))

    Jump('loc_1BF54')

    def _loc_1BF17(): pass

    label('loc_1BF17')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A0, 0x0))

    Jump('loc_1BF54')

    def _loc_1BF33(): pass

    label('loc_1BF33')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A1, 0x0))

    Jump('loc_1BF54')

    def _loc_1BF4F(): pass

    label('loc_1BF4F')

    Jump('loc_1BF54')

    def _loc_1BF54(): pass

    label('loc_1BF54')

    Jump('loc_1BC19')

    def _loc_1BF59(): pass

    label('loc_1BF59')

    Return()

# id: 0x007D offset: 0x1BF5C
@scena.Code('EV_Jump_SB_01D_00')
def EV_Jump_SB_01D_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1BF65(): pass

    label('loc_1BF65')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C155',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01D_00_00][工房でアリサ＆アルティナと会話]', 0x000081A2)
    MenuCmd(0x01, 0x02, '[SB_01D_00_01][工房でアリサと会話　　　　　　]', 0x000081A3)
    MenuCmd(0x01, 0x02, '[SB_01D_00_02][ミュゼとの会話　　　　　　　　]', 0x000081A4)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081A2, 'loc_1C080'),
        (0x000081A3, 'loc_1C080'),
        (0x000081A4, 'loc_1C080'),
        (-1, 'loc_1C08E'),
    )

    def _loc_1C080(): pass

    label('loc_1C080')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C09C')

    def _loc_1C08E(): pass

    label('loc_1C08E')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C09C')

    def _loc_1C09C(): pass

    label('loc_1C09C')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C0D3',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1C0D3(): pass

    label('loc_1C0D3')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081A2, 'loc_1C0F4'),
        (0x000081A3, 'loc_1C110'),
        (0x000081A4, 'loc_1C12F'),
        (-1, 'loc_1C14B'),
    )

    def _loc_1C0F4(): pass

    label('loc_1C0F4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A2, 0x0))

    Jump('loc_1C150')

    def _loc_1C110(): pass

    label('loc_1C110')

    SetScenaFlags(ScenaFlag(0x05B2, 5, 0x2D95))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A3, 0x0))

    Jump('loc_1C150')

    def _loc_1C12F(): pass

    label('loc_1C12F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A4, 0x0))

    Jump('loc_1C150')

    def _loc_1C14B(): pass

    label('loc_1C14B')

    Jump('loc_1C150')

    def _loc_1C150(): pass

    label('loc_1C150')

    Jump('loc_1BF65')

    def _loc_1C155(): pass

    label('loc_1C155')

    Return()

# id: 0x007E offset: 0x1C158
@scena.Code('EV_Jump_SB_01D_01')
def EV_Jump_SB_01D_01():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C161(): pass

    label('loc_1C161')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C3BF',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01D_01_00][ブリッジでジョゼットと会話　　]', 0x000081A5)
    MenuCmd(0x01, 0x02, '[SB_01D_01_01][旧Ⅶ組と会話　　　　　　　　　]', 0x000081A6)
    MenuCmd(0x01, 0x02, '[SB_01D_01_02][アルティナ＆ミュゼと会話　　　]', 0x000081A7)
    MenuCmd(0x01, 0x02, '[SB_01D_01_03][クルト＆アッシュと会話　　　　]', 0x000081A8)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081A5, 'loc_1C2C9'),
        (0x000081A6, 'loc_1C2C9'),
        (0x000081A7, 'loc_1C2C9'),
        (0x000081A8, 'loc_1C2C9'),
        (-1, 'loc_1C2D7'),
    )

    def _loc_1C2C9(): pass

    label('loc_1C2C9')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x108A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C2E5')

    def _loc_1C2D7(): pass

    label('loc_1C2D7')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C2E5')

    def _loc_1C2E5(): pass

    label('loc_1C2E5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C31C',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1C31C(): pass

    label('loc_1C31C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081A5, 'loc_1C345'),
        (0x000081A6, 'loc_1C361'),
        (0x000081A7, 'loc_1C37D'),
        (0x000081A8, 'loc_1C399'),
        (-1, 'loc_1C3B5'),
    )

    def _loc_1C345(): pass

    label('loc_1C345')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A5, 0x0))

    Jump('loc_1C3BA')

    def _loc_1C361(): pass

    label('loc_1C361')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A6, 0x0))

    Jump('loc_1C3BA')

    def _loc_1C37D(): pass

    label('loc_1C37D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A7, 0x0))

    Jump('loc_1C3BA')

    def _loc_1C399(): pass

    label('loc_1C399')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A8, 0x0))

    Jump('loc_1C3BA')

    def _loc_1C3B5(): pass

    label('loc_1C3B5')

    Jump('loc_1C3BA')

    def _loc_1C3BA(): pass

    label('loc_1C3BA')

    Jump('loc_1C161')

    def _loc_1C3BF(): pass

    label('loc_1C3BF')

    Return()

# id: 0x007F offset: 0x1C3C0
@scena.Code('EV_Jump_SB_01D_02')
def EV_Jump_SB_01D_02():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C3C9(): pass

    label('loc_1C3C9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CA9F',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01D_02_00][港湾区に到着　　　　　　　　　]', 0x000081A9)
    MenuCmd(0x01, 0x02, '[SB_01D_02_01][ＲＦビルに入る　　　　　　　　]', 0x000081AA)
    MenuCmd(0x01, 0x02, '[SB_01D_02_02][ＲＦビルでアディスンと話す　　]', 0x000081AB)
    MenuCmd(0x01, 0x02, '[SB_01D_02_03][中央広場に到着　　　　　　　　]', 0x000081AC)
    MenuCmd(0x01, 0x02, '[SB_01D_02_04][ウェンディと話す　　　　　　　]', 0x000081AD)
    MenuCmd(0x01, 0x02, '[SB_01D_02_05][歓楽街に到着　　　　　　　　　]', 0x000081AE)
    MenuCmd(0x01, 0x02, '[SB_01D_02_06][アルカンシェルに入る　　　　　]', 0x000081AF)
    MenuCmd(0x01, 0x02, '[SB_01D_02_07][シュリの練習を確認　　　　　　]', 0x000081B0)
    MenuCmd(0x01, 0x02, '[SB_01D_02_08][イメルダと話す　　　　　　　　]', 0x000081B1)
    MenuCmd(0x01, 0x02, '[SB_01D_02_09][西通りに到着　　　　　　　　　]', 0x000081B2)
    MenuCmd(0x01, 0x02, '[SB_01D_02_10][オスカーと話す　　　　　　　　]', 0x000081B3)
    MenuCmd(0x01, 0x02, '[SB_01D_02_11][クロスベル通信社を発見する　　]', 0x000081B4)
    MenuCmd(0x01, 0x02, '[SB_01D_02_12][グレイスと遭遇　　　　　　　　]', 0x000081B5)
    MenuCmd(0x01, 0x02, '[SB_01D_02_20][サザークが拘留のため連行される]', 0x00008267)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081A9, 'loc_1C833'),
        (0x000081AA, 'loc_1C833'),
        (0x000081AB, 'loc_1C833'),
        (0x000081AC, 'loc_1C833'),
        (0x000081AD, 'loc_1C833'),
        (0x000081AE, 'loc_1C833'),
        (0x000081AF, 'loc_1C833'),
        (0x000081B0, 'loc_1C833'),
        (0x000081B1, 'loc_1C833'),
        (0x000081B2, 'loc_1C833'),
        (0x000081B3, 'loc_1C833'),
        (0x000081B4, 'loc_1C833'),
        (0x000081B5, 'loc_1C833'),
        (0x00008267, 'loc_1C841'),
        (-1, 'loc_1C84F'),
    )

    def _loc_1C833(): pass

    label('loc_1C833')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x109A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C85D')

    def _loc_1C841(): pass

    label('loc_1C841')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x10AB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C85D')

    def _loc_1C84F(): pass

    label('loc_1C84F')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C85D')

    def _loc_1C85D(): pass

    label('loc_1C85D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C894',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1C894(): pass

    label('loc_1C894')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081A9, 'loc_1C90D'),
        (0x000081AA, 'loc_1C929'),
        (0x000081AB, 'loc_1C945'),
        (0x000081AC, 'loc_1C961'),
        (0x000081AD, 'loc_1C97D'),
        (0x000081AE, 'loc_1C999'),
        (0x000081AF, 'loc_1C9B5'),
        (0x000081B0, 'loc_1C9D1'),
        (0x000081B1, 'loc_1C9ED'),
        (0x000081B2, 'loc_1CA09'),
        (0x000081B3, 'loc_1CA25'),
        (0x000081B4, 'loc_1CA41'),
        (0x000081B5, 'loc_1CA5D'),
        (0x00008267, 'loc_1CA79'),
        (-1, 'loc_1CA95'),
    )

    def _loc_1C90D(): pass

    label('loc_1C90D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81A9, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C929(): pass

    label('loc_1C929')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81AA, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C945(): pass

    label('loc_1C945')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81AB, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C961(): pass

    label('loc_1C961')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81AC, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C97D(): pass

    label('loc_1C97D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81AD, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C999(): pass

    label('loc_1C999')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81AE, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C9B5(): pass

    label('loc_1C9B5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81AF, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C9D1(): pass

    label('loc_1C9D1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B0, 0x0))

    Jump('loc_1CA9A')

    def _loc_1C9ED(): pass

    label('loc_1C9ED')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B1, 0x0))

    Jump('loc_1CA9A')

    def _loc_1CA09(): pass

    label('loc_1CA09')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B2, 0x0))

    Jump('loc_1CA9A')

    def _loc_1CA25(): pass

    label('loc_1CA25')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B3, 0x0))

    Jump('loc_1CA9A')

    def _loc_1CA41(): pass

    label('loc_1CA41')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B4, 0x0))

    Jump('loc_1CA9A')

    def _loc_1CA5D(): pass

    label('loc_1CA5D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B5, 0x0))

    Jump('loc_1CA9A')

    def _loc_1CA79(): pass

    label('loc_1CA79')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8267, 0x0))

    Jump('loc_1CA9A')

    def _loc_1CA95(): pass

    label('loc_1CA95')

    Jump('loc_1CA9A')

    def _loc_1CA9A(): pass

    label('loc_1CA9A')

    Jump('loc_1C3C9')

    def _loc_1CA9F(): pass

    label('loc_1CA9F')

    Return()

# id: 0x0080 offset: 0x1CAA0
@scena.Code('EV_Jump_SB_01D_03')
def EV_Jump_SB_01D_03():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CAA9(): pass

    label('loc_1CAA9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D083',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01D_03_00][観覧車エリアに到着　　　　　　]', 0x000081B6)
    MenuCmd(0x01, 0x02, '[SB_01D_03_01][アレイスターと話す　　　　　　]', 0x000081B7)
    MenuCmd(0x01, 0x02, '[SB_01D_03_02][ホラーコースターエリアに到着　]', 0x000081B8)
    MenuCmd(0x01, 0x02, '[SB_01D_03_03][アントンと再会　　　　　　　　]', 0x000081B9)
    MenuCmd(0x01, 0x02, '[SB_01D_03_04][鏡の城エリアに到着　　　　　　]', 0x000081BA)
    MenuCmd(0x01, 0x02, '[SB_01D_03_05][鏡の城の待合室に入る　　　　　]', 0x000081BB)
    MenuCmd(0x01, 0x02, '[SB_01D_03_06][受付に話す　　　　　　　　　　]', 0x000081BC)
    MenuCmd(0x01, 0x02, '[SB_01D_03_07][鏡の城に入る　　　　　　　　　]', 0x000081BD)
    MenuCmd(0x01, 0x02, '[SB_01D_03_08][ベリルに占ってもらう　　　　　]', 0x000081BE)
    MenuCmd(0x01, 0x02, '[SB_01D_03_09][待合室に戻る　　　　　　　　　]', 0x000081BF)
    MenuCmd(0x01, 0x02, '[SB_01D_03_10][ビーチを訪れる　　　　　　　　]', 0x0000827E)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081B6, 'loc_1CE2C'),
        (0x000081B7, 'loc_1CE2C'),
        (0x000081B8, 'loc_1CE2C'),
        (0x000081B9, 'loc_1CE2C'),
        (0x000081BA, 'loc_1CE2C'),
        (0x000081BB, 'loc_1CE2C'),
        (0x000081BC, 'loc_1CE2C'),
        (0x000081BD, 'loc_1CE2C'),
        (0x000081BE, 'loc_1CE2C'),
        (0x000081BF, 'loc_1CE2C'),
        (0x0000827E, 'loc_1CE2C'),
        (-1, 'loc_1CE3A'),
    )

    def _loc_1CE2C(): pass

    label('loc_1CE2C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x10C4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CE48')

    def _loc_1CE3A(): pass

    label('loc_1CE3A')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CE48')

    def _loc_1CE48(): pass

    label('loc_1CE48')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CE7F',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1CE7F(): pass

    label('loc_1CE7F')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081B7, 'loc_1CEC0'),
        (0x000081B9, 'loc_1CEC8'),
        (0x000081BF, 'loc_1CED0'),
        (0x000081BE, 'loc_1CED3'),
        (0x000081BD, 'loc_1CED6'),
        (0x000081BC, 'loc_1CED9'),
        (0x000081BB, 'loc_1CEDC'),
        (-1, 'loc_1CEE4'),
    )

    def _loc_1CEC0(): pass

    label('loc_1CEC0')

    SetScenaFlags(ScenaFlag(0x05B4, 6, 0x2DA6))

    Jump('loc_1CEE4')

    def _loc_1CEC8(): pass

    label('loc_1CEC8')

    SetScenaFlags(ScenaFlag(0x05B5, 0, 0x2DA8))

    Jump('loc_1CEE4')

    def _loc_1CED0(): pass

    label('loc_1CED0')

    SetScenaFlags(ScenaFlag(0x05B5, 6, 0x2DAE))

    def _loc_1CED3(): pass

    label('loc_1CED3')

    SetScenaFlags(ScenaFlag(0x05B5, 5, 0x2DAD))

    def _loc_1CED6(): pass

    label('loc_1CED6')

    SetScenaFlags(ScenaFlag(0x05B5, 4, 0x2DAC))

    def _loc_1CED9(): pass

    label('loc_1CED9')

    SetScenaFlags(ScenaFlag(0x05B5, 3, 0x2DAB))

    def _loc_1CEDC(): pass

    label('loc_1CEDC')

    SetScenaFlags(ScenaFlag(0x05B5, 2, 0x2DAA))

    Jump('loc_1CEE4')

    def _loc_1CEE4(): pass

    label('loc_1CEE4')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081B6, 'loc_1CF45'),
        (0x000081B7, 'loc_1CF61'),
        (0x000081B8, 'loc_1CF7D'),
        (0x000081B9, 'loc_1CF99'),
        (0x000081BA, 'loc_1CFB5'),
        (0x000081BB, 'loc_1CFD1'),
        (0x000081BC, 'loc_1CFED'),
        (0x000081BD, 'loc_1D009'),
        (0x000081BE, 'loc_1D025'),
        (0x000081BF, 'loc_1D041'),
        (0x0000827E, 'loc_1D05D'),
        (-1, 'loc_1D079'),
    )

    def _loc_1CF45(): pass

    label('loc_1CF45')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B6, 0x0))

    Jump('loc_1D07E')

    def _loc_1CF61(): pass

    label('loc_1CF61')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B7, 0x0))

    Jump('loc_1D07E')

    def _loc_1CF7D(): pass

    label('loc_1CF7D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B8, 0x0))

    Jump('loc_1D07E')

    def _loc_1CF99(): pass

    label('loc_1CF99')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81B9, 0x0))

    Jump('loc_1D07E')

    def _loc_1CFB5(): pass

    label('loc_1CFB5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81BA, 0x0))

    Jump('loc_1D07E')

    def _loc_1CFD1(): pass

    label('loc_1CFD1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81BB, 0x0))

    Jump('loc_1D07E')

    def _loc_1CFED(): pass

    label('loc_1CFED')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81BC, 0x0))

    Jump('loc_1D07E')

    def _loc_1D009(): pass

    label('loc_1D009')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81BD, 0x0))

    Jump('loc_1D07E')

    def _loc_1D025(): pass

    label('loc_1D025')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81BE, 0x0))

    Jump('loc_1D07E')

    def _loc_1D041(): pass

    label('loc_1D041')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81BF, 0x0))

    Jump('loc_1D07E')

    def _loc_1D05D(): pass

    label('loc_1D05D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x827E, 0x0))

    Jump('loc_1D07E')

    def _loc_1D079(): pass

    label('loc_1D079')

    Jump('loc_1D07E')

    def _loc_1D07E(): pass

    label('loc_1D07E')

    Jump('loc_1CAA9')

    def _loc_1D083(): pass

    label('loc_1D083')

    Return()

# id: 0x0081 offset: 0x1D084
@scena.Code('EV_Jump_SB_01X_00')
def EV_Jump_SB_01X_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1D08D(): pass

    label('loc_1D08D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D391',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_01X_00_00][万屋でアリサ＆レンと会話　　　]', 0x000081C0)
    MenuCmd(0x01, 0x02, '[SB_01X_00_01][万屋でレンと会話　　　　　　　]', 0x000081C1)
    MenuCmd(0x01, 0x02, '[SB_01X_00_02][必須会話後のレン　　　　　　　]', 0x000081C2)
    MenuCmd(0x01, 0x02, '[SB_01X_00_03][温泉手前でユウナ＆キーアと会話]', 0x000081C3)
    MenuCmd(0x01, 0x02, '[SB_01X_00_04][会話後のユウナ＆キーア　　　　]', 0x000081C4)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081C0, 'loc_1D242'),
        (0x000081C1, 'loc_1D242'),
        (0x000081C2, 'loc_1D242'),
        (0x000081C3, 'loc_1D242'),
        (0x000081C4, 'loc_1D242'),
        (-1, 'loc_1D250'),
    )

    def _loc_1D242(): pass

    label('loc_1D242')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x2008),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D25E')

    def _loc_1D250(): pass

    label('loc_1D250')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D25E')

    def _loc_1D25E(): pass

    label('loc_1D25E')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D296',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_01X')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1D296(): pass

    label('loc_1D296')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081C2, 'loc_1D2B7'),
        (0x000081C1, 'loc_1D2BA'),
        (0x000081C4, 'loc_1D2C2'),
        (-1, 'loc_1D2CA'),
    )

    def _loc_1D2B7(): pass

    label('loc_1D2B7')

    SetScenaFlags(ScenaFlag(0x06B6, 1, 0x35B1))

    def _loc_1D2BA(): pass

    label('loc_1D2BA')

    SetScenaFlags(ScenaFlag(0x06B6, 0, 0x35B0))

    Jump('loc_1D2CA')

    def _loc_1D2C2(): pass

    label('loc_1D2C2')

    SetScenaFlags(ScenaFlag(0x06B6, 3, 0x35B3))

    Jump('loc_1D2CA')

    def _loc_1D2CA(): pass

    label('loc_1D2CA')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081C0, 'loc_1D2FB'),
        (0x000081C1, 'loc_1D317'),
        (0x000081C2, 'loc_1D333'),
        (0x000081C3, 'loc_1D34F'),
        (0x000081C4, 'loc_1D36B'),
        (-1, 'loc_1D387'),
    )

    def _loc_1D2FB(): pass

    label('loc_1D2FB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C0, 0x0))

    Jump('loc_1D38C')

    def _loc_1D317(): pass

    label('loc_1D317')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C1, 0x0))

    Jump('loc_1D38C')

    def _loc_1D333(): pass

    label('loc_1D333')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C2, 0x0))

    Jump('loc_1D38C')

    def _loc_1D34F(): pass

    label('loc_1D34F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C3, 0x0))

    Jump('loc_1D38C')

    def _loc_1D36B(): pass

    label('loc_1D36B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C4, 0x0))

    Jump('loc_1D38C')

    def _loc_1D387(): pass

    label('loc_1D387')

    Jump('loc_1D38C')

    def _loc_1D38C(): pass

    label('loc_1D38C')

    Jump('loc_1D08D')

    def _loc_1D391(): pass

    label('loc_1D391')

    Return()

# id: 0x0082 offset: 0x1D394
@scena.Code('EV_Jump_SB_02A_00')
def EV_Jump_SB_02A_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1D39D(): pass

    label('loc_1D39D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DA3D',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02A_00_00][宿酒場でランディ達と会話　　　]', 0x000081C5)
    MenuCmd(0x01, 0x02, '[SB_02A_00_01][宿酒場でランディ＆キーアと会話]', 0x000081C6)
    MenuCmd(0x01, 0x02, '[SB_02A_00_02][宿酒場でアガット＆レンと会話　]', 0x000081C7)
    MenuCmd(0x01, 0x02, '[SB_02A_00_03][万屋でガイウス達と会話　　　　]', 0x000081C8)
    MenuCmd(0x01, 0x02, '[SB_02A_00_04][アトリエでロゼ達と会話　　　　]', 0x000081C9)
    MenuCmd(0x01, 0x02, '[SB_02A_00_05][アトリエでエマと会話　　　　　]', 0x000081CA)
    MenuCmd(0x01, 0x02, '[SB_02A_00_06][アトリエでクロチルダと会話　　]', 0x000081CB)
    MenuCmd(0x01, 0x02, '[SB_02A_00_07][アトリエでセリーヌと会話　　　]', 0x000081CC)
    MenuCmd(0x01, 0x02, '[SB_02A_00_08][アトリエでロゼと会話　　　　　]', 0x000081CD)
    MenuCmd(0x01, 0x02, '[SB_02A_00_09][宿酒場でオーレリア達との会話　]', 0x000081CE)
    MenuCmd(0x01, 0x02, '[SB_02A_00_10][エリオット＆マキアス＆ユーシス]', 0x000081CF)
    MenuCmd(0x01, 0x02, '[SB_02A_00_11][ヴァリマールの前で改めて決心　]', 0x000081D0)
    MenuCmd(0x01, 0x02, '[SB_02A_00_12][アリサ達との会話　　　　　　　]', 0x000081D1)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081C5, 'loc_1D7BA'),
        (0x000081C6, 'loc_1D7BA'),
        (0x000081C7, 'loc_1D7BA'),
        (0x000081C8, 'loc_1D7BA'),
        (0x000081C9, 'loc_1D7BA'),
        (0x000081CA, 'loc_1D7BA'),
        (0x000081CB, 'loc_1D7BA'),
        (0x000081CC, 'loc_1D7BA'),
        (0x000081CD, 'loc_1D7BA'),
        (0x000081CE, 'loc_1D7BA'),
        (0x000081CF, 'loc_1D7BA'),
        (0x000081D0, 'loc_1D7BA'),
        (0x000081D1, 'loc_1D7BA'),
        (-1, 'loc_1D7C8'),
    )

    def _loc_1D7BA(): pass

    label('loc_1D7BA')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D7D6')

    def _loc_1D7C8(): pass

    label('loc_1D7C8')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D7D6')

    def _loc_1D7D6(): pass

    label('loc_1D7D6')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D80D',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1D80D(): pass

    label('loc_1D80D')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081C6, 'loc_1D846'),
        (0x000081C7, 'loc_1D846'),
        (0x000081CA, 'loc_1D84E'),
        (0x000081CB, 'loc_1D84E'),
        (0x000081CC, 'loc_1D84E'),
        (0x000081CD, 'loc_1D84E'),
        (-1, 'loc_1D856'),
    )

    def _loc_1D846(): pass

    label('loc_1D846')

    SetScenaFlags(ScenaFlag(0x0730, 0, 0x3980))

    Jump('loc_1D856')

    def _loc_1D84E(): pass

    label('loc_1D84E')

    SetScenaFlags(ScenaFlag(0x0730, 4, 0x3984))

    Jump('loc_1D856')

    def _loc_1D856(): pass

    label('loc_1D856')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081C5, 'loc_1D8C7'),
        (0x000081C6, 'loc_1D8E3'),
        (0x000081C7, 'loc_1D8FF'),
        (0x000081C8, 'loc_1D91B'),
        (0x000081C9, 'loc_1D937'),
        (0x000081CA, 'loc_1D953'),
        (0x000081CB, 'loc_1D96F'),
        (0x000081CC, 'loc_1D98B'),
        (0x000081CD, 'loc_1D9A7'),
        (0x000081CE, 'loc_1D9C3'),
        (0x000081CF, 'loc_1D9DF'),
        (0x000081D0, 'loc_1D9FB'),
        (0x000081D1, 'loc_1DA17'),
        (-1, 'loc_1DA33'),
    )

    def _loc_1D8C7(): pass

    label('loc_1D8C7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C5, 0x0))

    Jump('loc_1DA38')

    def _loc_1D8E3(): pass

    label('loc_1D8E3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C6, 0x0))

    Jump('loc_1DA38')

    def _loc_1D8FF(): pass

    label('loc_1D8FF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C7, 0x0))

    Jump('loc_1DA38')

    def _loc_1D91B(): pass

    label('loc_1D91B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C8, 0x0))

    Jump('loc_1DA38')

    def _loc_1D937(): pass

    label('loc_1D937')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81C9, 0x0))

    Jump('loc_1DA38')

    def _loc_1D953(): pass

    label('loc_1D953')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81CA, 0x0))

    Jump('loc_1DA38')

    def _loc_1D96F(): pass

    label('loc_1D96F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81CB, 0x0))

    Jump('loc_1DA38')

    def _loc_1D98B(): pass

    label('loc_1D98B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81CC, 0x0))

    Jump('loc_1DA38')

    def _loc_1D9A7(): pass

    label('loc_1D9A7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81CD, 0x0))

    Jump('loc_1DA38')

    def _loc_1D9C3(): pass

    label('loc_1D9C3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81CE, 0x0))

    Jump('loc_1DA38')

    def _loc_1D9DF(): pass

    label('loc_1D9DF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81CF, 0x0))

    Jump('loc_1DA38')

    def _loc_1D9FB(): pass

    label('loc_1D9FB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D0, 0x0))

    Jump('loc_1DA38')

    def _loc_1DA17(): pass

    label('loc_1DA17')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D1, 0x0))

    Jump('loc_1DA38')

    def _loc_1DA33(): pass

    label('loc_1DA33')

    Jump('loc_1DA38')

    def _loc_1DA38(): pass

    label('loc_1DA38')

    Jump('loc_1D39D')

    def _loc_1DA3D(): pass

    label('loc_1DA3D')

    Return()

# id: 0x0083 offset: 0x1DA40
@scena.Code('EV_Jump_SB_02A_01')
def EV_Jump_SB_02A_01():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DA49(): pass

    label('loc_1DA49')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DD4A',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02A_01_00][甲板でユウナ＆アルティナと会話]', 0x000081D2)
    MenuCmd(0x01, 0x02, '[SB_02A_01_01][アリサとブリッジで会話　　　　]', 0x000081D3)
    MenuCmd(0x01, 0x02, '[SB_02A_01_02][ロジーヌからのアナウンス　　　]', 0x000081D4)
    MenuCmd(0x01, 0x02, '[SB_02A_01_03][鏡前でアリサにハグされる　　　]', 0x000081D7)
    MenuCmd(0x01, 0x02, '[SB_02A_01_04][セリーヌ　　　　　　　　　　　]', 0x000081D8)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081D2, 'loc_1DBFE'),
        (0x000081D3, 'loc_1DBFE'),
        (0x000081D4, 'loc_1DBFE'),
        (0x000081D7, 'loc_1DBFE'),
        (0x000081D8, 'loc_1DBFE'),
        (-1, 'loc_1DC0C'),
    )

    def _loc_1DBFE(): pass

    label('loc_1DBFE')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x300C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DC1A')

    def _loc_1DC0C(): pass

    label('loc_1DC0C')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DC1A')

    def _loc_1DC1A(): pass

    label('loc_1DC1A')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DC51',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1DC51(): pass

    label('loc_1DC51')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081D7, 'loc_1DC6A'),
        (0x000081D4, 'loc_1DC75'),
        (-1, 'loc_1DC83'),
    )

    def _loc_1DC6A(): pass

    label('loc_1DC6A')

    OP_71(0x00, 0x398B, 0x398D)

    Jump('loc_1DC83')

    def _loc_1DC75(): pass

    label('loc_1DC75')

    SetScenaFlags(ScenaFlag(0x0721, 4, 0x390C))
    OP_71(0x00, 0x3989, 0x398A)

    Jump('loc_1DC83')

    def _loc_1DC83(): pass

    label('loc_1DC83')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081D2, 'loc_1DCB4'),
        (0x000081D3, 'loc_1DCD0'),
        (0x000081D4, 'loc_1DCEC'),
        (0x000081D7, 'loc_1DD08'),
        (0x000081D8, 'loc_1DD24'),
        (-1, 'loc_1DD40'),
    )

    def _loc_1DCB4(): pass

    label('loc_1DCB4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D2, 0x0))

    Jump('loc_1DD45')

    def _loc_1DCD0(): pass

    label('loc_1DCD0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D3, 0x0))

    Jump('loc_1DD45')

    def _loc_1DCEC(): pass

    label('loc_1DCEC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D5, 0x0))

    Jump('loc_1DD45')

    def _loc_1DD08(): pass

    label('loc_1DD08')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D7, 0x0))

    Jump('loc_1DD45')

    def _loc_1DD24(): pass

    label('loc_1DD24')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D8, 0x0))

    Jump('loc_1DD45')

    def _loc_1DD40(): pass

    label('loc_1DD40')

    Jump('loc_1DD45')

    def _loc_1DD45(): pass

    label('loc_1DD45')

    Jump('loc_1DA49')

    def _loc_1DD4A(): pass

    label('loc_1DD4A')

    Return()

# id: 0x0084 offset: 0x1DD4C
@scena.Code('EV_Jump_SB_02A_02')
def EV_Jump_SB_02A_02():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DD55(): pass

    label('loc_1DD55')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DED4',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02A_02_00][巨神像を改めて全員で確認する　]', 0x000081D9)
    MenuCmd(0x01, 0x02, '[SB_02A_02_01][巨神像側に進めない　　　　　　]', 0x000081DA)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081D9, 'loc_1DE23'),
        (0x000081DA, 'loc_1DE23'),
        (-1, 'loc_1DE31'),
    )

    def _loc_1DE23(): pass

    label('loc_1DE23')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DE3F')

    def _loc_1DE31(): pass

    label('loc_1DE31')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DE3F')

    def _loc_1DE3F(): pass

    label('loc_1DE3F')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DE76',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1DE76(): pass

    label('loc_1DE76')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081D9, 'loc_1DE8F'),
        (0x000081DA, 'loc_1DEAB'),
        (-1, 'loc_1DECA'),
    )

    def _loc_1DE8F(): pass

    label('loc_1DE8F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81D9, 0x0))

    Jump('loc_1DECF')

    def _loc_1DEAB(): pass

    label('loc_1DEAB')

    SetScenaFlags(ScenaFlag(0x0732, 0, 0x3990))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81DA, 0x0))

    Jump('loc_1DECF')

    def _loc_1DECA(): pass

    label('loc_1DECA')

    Jump('loc_1DECF')

    def _loc_1DECF(): pass

    label('loc_1DECF')

    Jump('loc_1DD55')

    def _loc_1DED4(): pass

    label('loc_1DED4')

    Return()

# id: 0x0085 offset: 0x1DED8
@scena.Code('EV_Jump_SB_02B_00')
def EV_Jump_SB_02B_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DEE1(): pass

    label('loc_1DEE1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E2AE',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02B_00_00][海上要塞を見かける　　　　　　]', 0x000081DC)
    MenuCmd(0x01, 0x02, '[SB_02B_02_00][船員酒場でレオノーラに会う　　]', 0x000081DD)
    MenuCmd(0x01, 0x02, '[SB_02B_02_01][レーグニッツとクレアを見かける]', 0x000081DE)
    MenuCmd(0x01, 0x02, '[SB_02B_02_02][ガラス工房のシュトラウスと話す]', 0x000081DF)
    MenuCmd(0x01, 0x02, '[SB_02B_02_03][イーグレット家の様子を窺う　　]', 0x000081E0)
    MenuCmd(0x01, 0x02, '[SB_02B_02_04][港湾区の変化を確認する　　　　]', 0x000081E1)
    MenuCmd(0x01, 0x02, '[SB_02B_03_00][試しの扉を発見する　　　　　　]', 0x000081E2)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081DC, 'loc_1E130'),
        (0x000081DD, 'loc_1E13E'),
        (0x000081DE, 'loc_1E13E'),
        (0x000081DF, 'loc_1E13E'),
        (0x000081E0, 'loc_1E13E'),
        (0x000081E1, 'loc_1E13E'),
        (0x000081E2, 'loc_1E14C'),
        (-1, 'loc_1E15A'),
    )

    def _loc_1E130(): pass

    label('loc_1E130')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3035),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E168')

    def _loc_1E13E(): pass

    label('loc_1E13E')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3039),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E168')

    def _loc_1E14C(): pass

    label('loc_1E14C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3041),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E168')

    def _loc_1E15A(): pass

    label('loc_1E15A')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E168')

    def _loc_1E168(): pass

    label('loc_1E168')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E19F',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1E19F(): pass

    label('loc_1E19F')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081DC, 'loc_1E1E0'),
        (0x000081DD, 'loc_1E1FC'),
        (0x000081DE, 'loc_1E218'),
        (0x000081DF, 'loc_1E234'),
        (0x000081E0, 'loc_1E250'),
        (0x000081E1, 'loc_1E26C'),
        (0x000081E2, 'loc_1E288'),
        (-1, 'loc_1E2A4'),
    )

    def _loc_1E1E0(): pass

    label('loc_1E1E0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81DC, 0x0))

    Jump('loc_1E2A9')

    def _loc_1E1FC(): pass

    label('loc_1E1FC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81DD, 0x0))

    Jump('loc_1E2A9')

    def _loc_1E218(): pass

    label('loc_1E218')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81DE, 0x0))

    Jump('loc_1E2A9')

    def _loc_1E234(): pass

    label('loc_1E234')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81DF, 0x0))

    Jump('loc_1E2A9')

    def _loc_1E250(): pass

    label('loc_1E250')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E0, 0x0))

    Jump('loc_1E2A9')

    def _loc_1E26C(): pass

    label('loc_1E26C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E1, 0x0))

    Jump('loc_1E2A9')

    def _loc_1E288(): pass

    label('loc_1E288')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E2, 0x0))

    Jump('loc_1E2A9')

    def _loc_1E2A4(): pass

    label('loc_1E2A4')

    Jump('loc_1E2A9')

    def _loc_1E2A9(): pass

    label('loc_1E2A9')

    Jump('loc_1DEE1')

    def _loc_1E2AE(): pass

    label('loc_1E2AE')

    Return()

# id: 0x0086 offset: 0x1E2B0
@scena.Code('EV_Jump_SB_02C_00')
def EV_Jump_SB_02C_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1E2B9(): pass

    label('loc_1E2B9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E8AE',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02C_00_00] [聖堂広場でアルカンシェルと会う]', 0x000081E3)
    MenuCmd(0x01, 0x02, '[SB_02C_00_01] [フィオナと再会する　　　　　　]', 0x000081E4)
    MenuCmd(0x01, 0x02, '[SB_02C_00_02] [貴族街・バラッド侯を見かける　]', 0x000081E5)
    MenuCmd(0x01, 0x02, '[SB_02C_00_03] [ゴライアスを発見（先行版）　　]', 0x000081E6)
    MenuCmd(0x01, 0x02, '[SB_02C_00_04] [ゴライアスを発見（フリー版）　]', 0x000081E7)
    MenuCmd(0x01, 0x02, '[SB_02C_01_00] [ＶＳ第四機甲師団・一般配置　　]', 0x00008268)
    MenuCmd(0x01, 0x02, '[SB_02C_01_01] [ＶＳ第四機甲師団・その②　　　]', 0x00008269)
    MenuCmd(0x01, 0x02, '[SB_02C_01_01B][その②後・再配置　　　　　　　]', 0x0000826A)
    MenuCmd(0x01, 0x02, '[SB_02C_01_02] [ＶＳ第四機甲師団・その③　　　]', 0x0000826B)
    MenuCmd(0x01, 0x02, '[SB_02C_01_02B][その③後・再配置　　　　　　　]', 0x0000826C)
    MenuCmd(0x01, 0x02, '[SB_02C_01_03] [無力化した師団兵の共通ＬＰ　　]', 0x0000826D)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081E3, 'loc_1E647'),
        (0x000081E4, 'loc_1E647'),
        (0x000081E5, 'loc_1E647'),
        (0x000081E6, 'loc_1E647'),
        (0x000081E7, 'loc_1E655'),
        (0x00008268, 'loc_1E663'),
        (0x00008269, 'loc_1E663'),
        (0x0000826A, 'loc_1E663'),
        (0x0000826B, 'loc_1E663'),
        (0x0000826C, 'loc_1E663'),
        (0x0000826D, 'loc_1E663'),
        (-1, 'loc_1E671'),
    )

    def _loc_1E647(): pass

    label('loc_1E647')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x306B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E67F')

    def _loc_1E655(): pass

    label('loc_1E655')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E67F')

    def _loc_1E663(): pass

    label('loc_1E663')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3077),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E67F')

    def _loc_1E671(): pass

    label('loc_1E671')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E67F')

    def _loc_1E67F(): pass

    label('loc_1E67F')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E6B6',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1E6B6(): pass

    label('loc_1E6B6')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000826D, 'loc_1E6EF'),
        (0x0000826C, 'loc_1E6F2'),
        (0x0000826B, 'loc_1E6F5'),
        (0x0000826A, 'loc_1E6F8'),
        (0x00008269, 'loc_1E6FB'),
        (0x00008268, 'loc_1E6FB'),
        (-1, 'loc_1E70C'),
    )

    def _loc_1E6EF(): pass

    label('loc_1E6EF')

    SetScenaFlags(ScenaFlag(0x073B, 1, 0x39D9))

    def _loc_1E6F2(): pass

    label('loc_1E6F2')

    SetScenaFlags(ScenaFlag(0x073B, 0, 0x39D8))

    def _loc_1E6F5(): pass

    label('loc_1E6F5')

    SetScenaFlags(ScenaFlag(0x073A, 7, 0x39D7))

    def _loc_1E6F8(): pass

    label('loc_1E6F8')

    SetScenaFlags(ScenaFlag(0x073A, 6, 0x39D6))

    def _loc_1E6FB(): pass

    label('loc_1E6FB')

    SetScenaFlags(ScenaFlag(0x06F9, 2, 0x37CA))
    SetScenaFlags(ScenaFlag(0x06F9, 3, 0x37CB))
    SetScenaFlags(ScenaFlag(0x06F9, 4, 0x37CC))
    SetScenaFlags(ScenaFlag(0x06F9, 5, 0x37CD))

    Jump('loc_1E70C')

    def _loc_1E70C(): pass

    label('loc_1E70C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081E3, 'loc_1E76D'),
        (0x000081E4, 'loc_1E789'),
        (0x000081E5, 'loc_1E7A5'),
        (0x000081E6, 'loc_1E7C1'),
        (0x000081E7, 'loc_1E7DD'),
        (0x00008268, 'loc_1E7FC'),
        (0x00008269, 'loc_1E818'),
        (0x0000826A, 'loc_1E834'),
        (0x0000826B, 'loc_1E850'),
        (0x0000826C, 'loc_1E86C'),
        (0x0000826D, 'loc_1E888'),
        (-1, 'loc_1E8A4'),
    )

    def _loc_1E76D(): pass

    label('loc_1E76D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E3, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E789(): pass

    label('loc_1E789')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E4, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E7A5(): pass

    label('loc_1E7A5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E5, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E7C1(): pass

    label('loc_1E7C1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E6, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E7DD(): pass

    label('loc_1E7DD')

    FormationCtrl(0x1C, 0x01)
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E7, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E7FC(): pass

    label('loc_1E7FC')

    OP_28((0xDD, 'm7000'), (0xDD, 'DefaultEntry'), 0x00)

    Jump('loc_1E8A9')

    def _loc_1E818(): pass

    label('loc_1E818')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8269, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E834(): pass

    label('loc_1E834')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x826A, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E850(): pass

    label('loc_1E850')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x826B, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E86C(): pass

    label('loc_1E86C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x826C, 0x0))

    Jump('loc_1E8A9')

    def _loc_1E888(): pass

    label('loc_1E888')

    OP_28((0xDD, 'm7000'), (0xDD, 'EV_02C_10_00'), 0x00)

    Jump('loc_1E8A9')

    def _loc_1E8A4(): pass

    label('loc_1E8A4')

    Jump('loc_1E8A9')

    def _loc_1E8A9(): pass

    label('loc_1E8A9')

    Jump('loc_1E2B9')

    def _loc_1E8AE(): pass

    label('loc_1E8AE')

    Return()

# id: 0x0087 offset: 0x1E8B0
@scena.Code('EV_Jump_SB_02D_00')
def EV_Jump_SB_02D_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1E8B9(): pass

    label('loc_1E8B9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EA43',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02D_00_00][宿酒場でシドニー達と会話　　　]', 0x000081E8)
    MenuCmd(0x01, 0x02, '[SB_02D_00_01][月霊窟に反応　　　　　　　　　]', 0x000081E9)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081E8, 'loc_1E987'),
        (0x000081E9, 'loc_1E995'),
        (-1, 'loc_1E9A3'),
    )

    def _loc_1E987(): pass

    label('loc_1E987')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x309A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E9B1')

    def _loc_1E995(): pass

    label('loc_1E995')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x309A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E9B1')

    def _loc_1E9A3(): pass

    label('loc_1E9A3')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E9B1')

    def _loc_1E9B1(): pass

    label('loc_1E9B1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E9E8',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1E9E8(): pass

    label('loc_1E9E8')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081E8, 'loc_1EA01'),
        (0x000081E9, 'loc_1EA1D'),
        (-1, 'loc_1EA39'),
    )

    def _loc_1EA01(): pass

    label('loc_1EA01')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E8, 0x0))

    Jump('loc_1EA3E')

    def _loc_1EA1D(): pass

    label('loc_1EA1D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81E9, 0x0))

    Jump('loc_1EA3E')

    def _loc_1EA39(): pass

    label('loc_1EA39')

    Jump('loc_1EA3E')

    def _loc_1EA3E(): pass

    label('loc_1EA3E')

    Jump('loc_1E8B9')

    def _loc_1EA43(): pass

    label('loc_1EA43')

    Return()

# id: 0x0088 offset: 0x1EA44
@scena.Code('EV_Jump_SB_02D_01')
def EV_Jump_SB_02D_01():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1EA4D(): pass

    label('loc_1EA4D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EC3D',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02D_01_00][フランキーと再会　　　　　　　]', 0x000081EA)
    MenuCmd(0x01, 0x02, '[SB_02D_01_01][フランキーと話す　　　　　　　]', 0x000081EB)
    MenuCmd(0x01, 0x02, '[SB_02D_01_02][人気のない宿舎を確認する　　　]', 0x000081EC)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081EA, 'loc_1EB68'),
        (0x000081EB, 'loc_1EB68'),
        (0x000081EC, 'loc_1EB68'),
        (-1, 'loc_1EB76'),
    )

    def _loc_1EB68(): pass

    label('loc_1EB68')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30A0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1EB84')

    def _loc_1EB76(): pass

    label('loc_1EB76')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1EB84')

    def _loc_1EB84(): pass

    label('loc_1EB84')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EBBB',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1EBBB(): pass

    label('loc_1EBBB')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081EA, 'loc_1EBDC'),
        (0x000081EB, 'loc_1EBF8'),
        (0x000081EC, 'loc_1EC17'),
        (-1, 'loc_1EC33'),
    )

    def _loc_1EBDC(): pass

    label('loc_1EBDC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81EA, 0x0))

    Jump('loc_1EC38')

    def _loc_1EBF8(): pass

    label('loc_1EBF8')

    SetScenaFlags(ScenaFlag(0x0733, 7, 0x399F))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81EB, 0x0))

    Jump('loc_1EC38')

    def _loc_1EC17(): pass

    label('loc_1EC17')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81EC, 0x0))

    Jump('loc_1EC38')

    def _loc_1EC33(): pass

    label('loc_1EC33')

    Jump('loc_1EC38')

    def _loc_1EC38(): pass

    label('loc_1EC38')

    Jump('loc_1EA4D')

    def _loc_1EC3D(): pass

    label('loc_1EC3D')

    Return()

# id: 0x0089 offset: 0x1EC40
@scena.Code('EV_Jump_SB_02D_02')
def EV_Jump_SB_02D_02():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1EC49(): pass

    label('loc_1EC49')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F100',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02D_02_00] [芸術室で本校生徒との戦闘　　　]戦', 0x000081ED)
    MenuCmd(0x01, 0x02, '[SB_02D_02_01] [カードキーを入手　　　　　　　]', 0x000081EE)
    MenuCmd(0x01, 0x02, '[SB_02D_02_02] [本校生徒との戦闘・軍略会議室　]', 0x0000826E)
    MenuCmd(0x01, 0x02, '[SB_02D_02_02B][軍略会議室・再配置　　　　　　]', 0x0000826F)
    MenuCmd(0x01, 0x02, '[SB_02D_02_03] [本校生徒との戦闘・プール前　　]', 0x00008270)
    MenuCmd(0x01, 0x02, '[SB_02D_02_03B][プール前・再配置　　　　　　　]', 0x00008271)
    MenuCmd(0x01, 0x02, '[SB_02D_02_04] [本校生徒との戦闘・クラブハウス]', 0x00008272)
    MenuCmd(0x01, 0x02, '[SB_02D_02_04B][クラブハウス・再配置　　　　　]', 0x00008273)
    MenuCmd(0x01, 0x02, '[SB_02D_02_05] [無力化した本校生の共通ＬＰ　　]', 0x00008274)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081ED, 'loc_1EF3E'),
        (0x000081EE, 'loc_1EF3E'),
        (0x0000826E, 'loc_1EF3E'),
        (0x0000826F, 'loc_1EF3E'),
        (0x00008270, 'loc_1EF3E'),
        (0x00008271, 'loc_1EF3E'),
        (0x00008272, 'loc_1EF3E'),
        (0x00008273, 'loc_1EF3E'),
        (0x00008274, 'loc_1EF3E'),
        (-1, 'loc_1EF4C'),
    )

    def _loc_1EF3E(): pass

    label('loc_1EF3E')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30A6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1EF5A')

    def _loc_1EF4C(): pass

    label('loc_1EF4C')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1EF5A')

    def _loc_1EF5A(): pass

    label('loc_1EF5A')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EF91',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_1EF91(): pass

    label('loc_1EF91')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081ED, 'loc_1EFE2'),
        (0x000081EE, 'loc_1EFFE'),
        (0x0000826E, 'loc_1F01D'),
        (0x0000826F, 'loc_1F039'),
        (0x00008270, 'loc_1F058'),
        (0x00008271, 'loc_1F074'),
        (0x00008272, 'loc_1F093'),
        (0x00008273, 'loc_1F0AF'),
        (0x00008274, 'loc_1F0CE'),
        (-1, 'loc_1F0F6'),
    )

    def _loc_1EFE2(): pass

    label('loc_1EFE2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81ED, 0x0))

    Jump('loc_1F0FB')

    def _loc_1EFFE(): pass

    label('loc_1EFFE')

    SetScenaFlags(ScenaFlag(0x0734, 2, 0x39A2))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81EE, 0x0))

    Jump('loc_1F0FB')

    def _loc_1F01D(): pass

    label('loc_1F01D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x826E, 0x0))

    Jump('loc_1F0FB')

    def _loc_1F039(): pass

    label('loc_1F039')

    SetScenaFlags(ScenaFlag(0x073B, 3, 0x39DB))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x826F, 0x0))

    Jump('loc_1F0FB')

    def _loc_1F058(): pass

    label('loc_1F058')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8270, 0x0))

    Jump('loc_1F0FB')

    def _loc_1F074(): pass

    label('loc_1F074')

    SetScenaFlags(ScenaFlag(0x073B, 5, 0x39DD))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8271, 0x0))

    Jump('loc_1F0FB')

    def _loc_1F093(): pass

    label('loc_1F093')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8272, 0x0))

    Jump('loc_1F0FB')

    def _loc_1F0AF(): pass

    label('loc_1F0AF')

    SetScenaFlags(ScenaFlag(0x073B, 7, 0x39DF))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8273, 0x0))

    Jump('loc_1F0FB')

    def _loc_1F0CE(): pass

    label('loc_1F0CE')

    OP_71(0x00, 0x39DB, 0x39E0)
    OP_71(0x00, 0x39A2, 0x39A3)
    OP_28((0xDD, 't0210'), (0xDD, 'DefaultEntry'), 0x00)

    Jump('loc_1F0FB')

    def _loc_1F0F6(): pass

    label('loc_1F0F6')

    Jump('loc_1F0FB')

    def _loc_1F0FB(): pass

    label('loc_1F0FB')

    Jump('loc_1EC49')

    def _loc_1F100(): pass

    label('loc_1F100')

    Return()

# id: 0x008A offset: 0x1F104
@scena.Code('EV_Jump_SB_02E_00')
def EV_Jump_SB_02E_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F10D(): pass

    label('loc_1F10D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2058B',
    )

    MenuCmd(0x00, 0x02, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_02E_00_00][ブリッジでガイウスと会話　　　]', 0x000081EF)
    MenuCmd(0x01, 0x02, '[SB_02E_00_01][目的地に向かう・選択肢　　　　]', 0x000081F0)
    MenuCmd(0x01, 0x02, '[SB_02E_01_00][ロイドたちとの会話　　　　　　]', 0x000081F1)
    MenuCmd(0x01, 0x02, '[SB_02E_01_01][ロイドたちとの会話２　　　　　]', 0x000081F2)
    MenuCmd(0x01, 0x02, '[SB_02E_01_02][エリィたちとの会話　　　　　　]', 0x000081F3)
    MenuCmd(0x01, 0x02, '[SB_02E_01_03][エリィたちとの会話２　　　　　]', 0x000081F4)
    MenuCmd(0x01, 0x02, '[SB_02E_01_04][エステルたちとの会話　　　　　]', 0x000081F5)
    MenuCmd(0x01, 0x02, '[SB_02E_01_05][エステルたちとの会話２　　　　]', 0x000081F6)
    MenuCmd(0x01, 0x02, '[SB_02E_01_06][エステルたちとの会話３　　　　]', 0x000081F7)
    MenuCmd(0x01, 0x02, '[SB_02E_01_07][ヨシュアたちとの会話　　　　　]', 0x000081F8)
    MenuCmd(0x01, 0x02, '[SB_02E_01_08][ヨシュアたちとの会話２　　　　]', 0x000081F9)
    MenuCmd(0x01, 0x02, '[SB_02E_01_09][カエラ達との会話　　　　　　　]', 0x000081FA)
    MenuCmd(0x01, 0x02, '[SB_02E_01_10][カエラ達との会話２　　　　　　]', 0x000081FB)
    MenuCmd(0x01, 0x02, '[SB_02E_01_11][ウォレス達との会話　　　　　　]', 0x000081FC)
    MenuCmd(0x01, 0x02, '[SB_02E_01_12][ウォレス達との会話２　　　　　]', 0x000081FD)
    MenuCmd(0x01, 0x02, '[SB_02E_01_13][ルーシー達との会話　　　　　　]', 0x000081FE)
    MenuCmd(0x01, 0x02, '[SB_02E_01_14][ロジーヌ達との会話　　　　　　]', 0x000081FF)
    MenuCmd(0x01, 0x02, '[SB_02E_02_00][カシウスとの会話　　　　　　　]', 0x00008200)
    MenuCmd(0x01, 0x02, '[SB_02E_02_01][ラウンジでエリィ達と会話　　　]', 0x00008201)
    MenuCmd(0x01, 0x02, '[SB_02E_02_02][エリィ＆アリサと会話　　　　　]', 0x00008202)
    MenuCmd(0x01, 0x02, '[SB_02E_02_03][ユウナ＆オーレリアと会話　　　]', 0x00008203)
    MenuCmd(0x01, 0x02, '[SB_02E_02_04][控え室でクローゼ達と会話　　　]', 0x00008204)
    MenuCmd(0x01, 0x02, '[SB_02E_02_05][エステル＆アルフィンと会話　　]', 0x00008205)
    MenuCmd(0x01, 0x02, '[SB_02E_02_06][エステル＆アルフィンと会話２　]', 0x00008206)
    MenuCmd(0x01, 0x02, '[SB_02E_02_07][クローゼ＆ルーシーと会話　　　]', 0x00008207)
    MenuCmd(0x01, 0x02, '[SB_02E_02_08][クローゼ＆ルーシーと会話２　　]', 0x00008208)
    MenuCmd(0x01, 0x02, '[SB_02E_02_09][客室でキーア達と会話　　　　　]', 0x00008209)
    MenuCmd(0x01, 0x02, '[SB_02E_02_10][アンゼリカ＆セリーヌと会話　　]', 0x0000820A)
    MenuCmd(0x01, 0x02, '[SB_02E_02_11][キーア＆レン＆ティータと会話　]', 0x0000820B)
    MenuCmd(0x01, 0x02, '[SB_02E_02_12][客室でカシウス達と会話　　　　]', 0x0000820C)
    MenuCmd(0x01, 0x02, '[SB_02E_02_13][客室でカシウス達と会話２　　　]', 0x0000820D)
    MenuCmd(0x01, 0x02, '[SB_02E_02_14][ラウラ＆クルトと会話　　　　　]', 0x0000820E)
    MenuCmd(0x01, 0x02, '[SB_02E_02_15][共和国控え室を調べる　　　　　]', 0x0000820F)
    MenuCmd(0x01, 0x02, '[SB_02E_02_16][ランディ達との会話　　　　　　]', 0x00008210)
    MenuCmd(0x01, 0x02, '[SB_02E_02_17][ロックスミス達との会話　　　　]', 0x00008211)
    MenuCmd(0x01, 0x02, '[SB_02E_02_18][ロックスミス達との会話２　　　]', 0x00008212)
    MenuCmd(0x01, 0x02, '[SB_02E_02_19][カエラ達との会話　　　　　　　]', 0x00008213)
    MenuCmd(0x01, 0x02, '[SB_02E_02_20][公国控え室を調べる　　　　　　]', 0x00008214)
    MenuCmd(0x01, 0x02, '[SB_02E_02_21][公国控え室を調べる２　　　　　]', 0x00008215)
    MenuCmd(0x01, 0x02, '[SB_02E_02_22][アルバート大公達との会話　　　]', 0x00008216)
    MenuCmd(0x01, 0x02, '[SB_02E_02_23][ウォレス達との会話　　　　　　]', 0x00008217)
    MenuCmd(0x01, 0x02, '[SB_02E_02_24][グレイス達との会話　　　　　　]', 0x00008218)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081EF, 'loc_1FDE3'),
        (0x000081F0, 'loc_1FDE3'),
        (0x000081F1, 'loc_1FDF1'),
        (0x000081F2, 'loc_1FDF1'),
        (0x000081F3, 'loc_1FDF1'),
        (0x000081F4, 'loc_1FDF1'),
        (0x000081F5, 'loc_1FDF1'),
        (0x000081F6, 'loc_1FDF1'),
        (0x000081F7, 'loc_1FDF1'),
        (0x000081F8, 'loc_1FDF1'),
        (0x000081F9, 'loc_1FDF1'),
        (0x000081FA, 'loc_1FDF1'),
        (0x000081FB, 'loc_1FDF1'),
        (0x000081FC, 'loc_1FDF1'),
        (0x000081FD, 'loc_1FDF1'),
        (0x000081FE, 'loc_1FDF1'),
        (0x000081FF, 'loc_1FDF1'),
        (0x00008200, 'loc_1FDFF'),
        (0x00008201, 'loc_1FDFF'),
        (0x00008202, 'loc_1FDFF'),
        (0x00008203, 'loc_1FDFF'),
        (0x00008204, 'loc_1FDFF'),
        (0x00008205, 'loc_1FDFF'),
        (0x00008206, 'loc_1FDFF'),
        (0x00008207, 'loc_1FDFF'),
        (0x00008208, 'loc_1FDFF'),
        (0x00008209, 'loc_1FDFF'),
        (0x0000820A, 'loc_1FDFF'),
        (0x0000820B, 'loc_1FDFF'),
        (0x0000820C, 'loc_1FDFF'),
        (0x0000820D, 'loc_1FDFF'),
        (0x0000820E, 'loc_1FDFF'),
        (0x0000820F, 'loc_1FDFF'),
        (0x00008210, 'loc_1FDFF'),
        (0x00008211, 'loc_1FDFF'),
        (0x00008212, 'loc_1FDFF'),
        (0x00008213, 'loc_1FDFF'),
        (0x00008214, 'loc_1FDFF'),
        (0x00008215, 'loc_1FDFF'),
        (0x00008216, 'loc_1FDFF'),
        (0x00008217, 'loc_1FDFF'),
        (0x00008218, 'loc_1FDFF'),
        (-1, 'loc_1FE0D'),
    )

    def _loc_1FDE3(): pass

    label('loc_1FDE3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1FE1B')

    def _loc_1FDF1(): pass

    label('loc_1FDF1')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1FE1B')

    def _loc_1FDFF(): pass

    label('loc_1FDFF')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30DB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1FE1B')

    def _loc_1FE0D(): pass

    label('loc_1FE0D')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1FE1B')

    def _loc_1FE1B(): pass

    label('loc_1FE1B')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FE9E',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x30DB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FE9E',
    )

    SetScenaFlags(ScenaFlag(0x0734, 6, 0x39A6))
    SetScenaFlags(ScenaFlag(0x0734, 7, 0x39A7))
    SetScenaFlags(ScenaFlag(0x0735, 0, 0x39A8))
    SetScenaFlags(ScenaFlag(0x0735, 1, 0x39A9))
    SetScenaFlags(ScenaFlag(0x0735, 2, 0x39AA))
    SetScenaFlags(ScenaFlag(0x0735, 3, 0x39AB))
    SetScenaFlags(ScenaFlag(0x0735, 4, 0x39AC))
    SetScenaFlags(ScenaFlag(0x0735, 5, 0x39AD))
    SetScenaFlags(ScenaFlag(0x0735, 6, 0x39AE))
    SetScenaFlags(ScenaFlag(0x0738, 2, 0x39C2))
    SetScenaFlags(ScenaFlag(0x0738, 3, 0x39C3))
    SetScenaFlags(ScenaFlag(0x0738, 4, 0x39C4))
    SetScenaFlags(ScenaFlag(0x0738, 5, 0x39C5))
    SetScenaFlags(ScenaFlag(0x0739, 6, 0x39CE))
    SetScenaFlags(ScenaFlag(0x0739, 7, 0x39CF))

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x8200),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FE9E',
    )

    SetScenaFlags(ScenaFlag(0x0735, 7, 0x39AF))

    def _loc_1FE9E(): pass

    label('loc_1FE9E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081FD, 'loc_1FF2F'),
        (0x000081FB, 'loc_1FF37'),
        (0x000081F7, 'loc_1FF3F'),
        (0x000081F6, 'loc_1FF42'),
        (0x00008202, 'loc_1FF4A'),
        (0x00008203, 'loc_1FF4A'),
        (0x00008201, 'loc_1FF4D'),
        (0x00008205, 'loc_1FF55'),
        (0x00008207, 'loc_1FF55'),
        (0x00008204, 'loc_1FF58'),
        (0x0000820A, 'loc_1FF60'),
        (0x0000820B, 'loc_1FF60'),
        (0x00008209, 'loc_1FF63'),
        (0x0000820D, 'loc_1FF6B'),
        (0x0000820E, 'loc_1FF6B'),
        (0x0000820C, 'loc_1FF6E'),
        (0x00008212, 'loc_1FF76'),
        (-1, 'loc_1FF7E'),
    )

    def _loc_1FF2F(): pass

    label('loc_1FF2F')

    SetScenaFlags(ScenaFlag(0x0738, 4, 0x39C4))

    Jump('loc_1FF7E')

    def _loc_1FF37(): pass

    label('loc_1FF37')

    SetScenaFlags(ScenaFlag(0x0738, 2, 0x39C2))

    Jump('loc_1FF7E')

    def _loc_1FF3F(): pass

    label('loc_1FF3F')

    SetScenaFlags(ScenaFlag(0x0735, 3, 0x39AB))

    def _loc_1FF42(): pass

    label('loc_1FF42')

    SetScenaFlags(ScenaFlag(0x0735, 2, 0x39AA))

    Jump('loc_1FF7E')

    def _loc_1FF4A(): pass

    label('loc_1FF4A')

    SetScenaFlags(ScenaFlag(0x0736, 0, 0x39B0))

    def _loc_1FF4D(): pass

    label('loc_1FF4D')

    SetScenaFlags(ScenaFlag(0x0735, 2, 0x39AA))

    Jump('loc_1FF7E')

    def _loc_1FF55(): pass

    label('loc_1FF55')

    SetScenaFlags(ScenaFlag(0x0736, 3, 0x39B3))

    def _loc_1FF58(): pass

    label('loc_1FF58')

    SetScenaFlags(ScenaFlag(0x0735, 2, 0x39AA))

    Jump('loc_1FF7E')

    def _loc_1FF60(): pass

    label('loc_1FF60')

    SetScenaFlags(ScenaFlag(0x0737, 0, 0x39B8))

    def _loc_1FF63(): pass

    label('loc_1FF63')

    SetScenaFlags(ScenaFlag(0x0735, 2, 0x39AA))

    Jump('loc_1FF7E')

    def _loc_1FF6B(): pass

    label('loc_1FF6B')

    SetScenaFlags(ScenaFlag(0x0737, 3, 0x39BB))

    def _loc_1FF6E(): pass

    label('loc_1FF6E')

    SetScenaFlags(ScenaFlag(0x0735, 2, 0x39AA))

    Jump('loc_1FF7E')

    def _loc_1FF76(): pass

    label('loc_1FF76')

    SetScenaFlags(ScenaFlag(0x0739, 1, 0x39C9))

    Jump('loc_1FF7E')

    def _loc_1FF7E(): pass

    label('loc_1FF7E')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x000081EF, 'loc_200D7'),
        (0x000081F0, 'loc_200F3'),
        (0x000081F1, 'loc_20112'),
        (0x000081F2, 'loc_2012E'),
        (0x000081F3, 'loc_2014D'),
        (0x000081F4, 'loc_20169'),
        (0x000081F5, 'loc_20188'),
        (0x000081F6, 'loc_201A4'),
        (0x000081F7, 'loc_201C0'),
        (0x000081F8, 'loc_201DC'),
        (0x000081F9, 'loc_201F8'),
        (0x000081FA, 'loc_20217'),
        (0x000081FB, 'loc_20233'),
        (0x000081FC, 'loc_2024F'),
        (0x000081FD, 'loc_2026B'),
        (0x000081FE, 'loc_20287'),
        (0x000081FF, 'loc_202A3'),
        (0x00008200, 'loc_202BF'),
        (0x00008201, 'loc_202DB'),
        (0x00008202, 'loc_202F7'),
        (0x00008203, 'loc_20313'),
        (0x00008204, 'loc_2032F'),
        (0x00008205, 'loc_2034B'),
        (0x00008206, 'loc_20367'),
        (0x00008207, 'loc_20386'),
        (0x00008208, 'loc_203A2'),
        (0x00008209, 'loc_203C1'),
        (0x0000820A, 'loc_203DD'),
        (0x0000820B, 'loc_203F9'),
        (0x0000820C, 'loc_20415'),
        (0x0000820D, 'loc_20431'),
        (0x0000820E, 'loc_2044D'),
        (0x0000820F, 'loc_20469'),
        (0x00008210, 'loc_20485'),
        (0x00008211, 'loc_204A1'),
        (0x00008212, 'loc_204BD'),
        (0x00008213, 'loc_204D9'),
        (0x00008214, 'loc_204F5'),
        (0x00008215, 'loc_20511'),
        (0x00008216, 'loc_2052D'),
        (0x00008217, 'loc_20549'),
        (0x00008218, 'loc_20565'),
        (-1, 'loc_20581'),
    )

    def _loc_200D7(): pass

    label('loc_200D7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81EF, 0x0))

    Jump('loc_20586')

    def _loc_200F3(): pass

    label('loc_200F3')

    SetScenaFlags(ScenaFlag(0x0734, 4, 0x39A4))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F0, 0x0))

    Jump('loc_20586')

    def _loc_20112(): pass

    label('loc_20112')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F1, 0x0))

    Jump('loc_20586')

    def _loc_2012E(): pass

    label('loc_2012E')

    SetScenaFlags(ScenaFlag(0x0734, 6, 0x39A6))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F2, 0x0))

    Jump('loc_20586')

    def _loc_2014D(): pass

    label('loc_2014D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F3, 0x0))

    Jump('loc_20586')

    def _loc_20169(): pass

    label('loc_20169')

    SetScenaFlags(ScenaFlag(0x0735, 0, 0x39A8))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F4, 0x0))

    Jump('loc_20586')

    def _loc_20188(): pass

    label('loc_20188')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F5, 0x0))

    Jump('loc_20586')

    def _loc_201A4(): pass

    label('loc_201A4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F6, 0x0))

    Jump('loc_20586')

    def _loc_201C0(): pass

    label('loc_201C0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F7, 0x0))

    Jump('loc_20586')

    def _loc_201DC(): pass

    label('loc_201DC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F8, 0x0))

    Jump('loc_20586')

    def _loc_201F8(): pass

    label('loc_201F8')

    SetScenaFlags(ScenaFlag(0x0735, 5, 0x39AD))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81F9, 0x0))

    Jump('loc_20586')

    def _loc_20217(): pass

    label('loc_20217')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81FA, 0x0))

    Jump('loc_20586')

    def _loc_20233(): pass

    label('loc_20233')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81FB, 0x0))

    Jump('loc_20586')

    def _loc_2024F(): pass

    label('loc_2024F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81FC, 0x0))

    Jump('loc_20586')

    def _loc_2026B(): pass

    label('loc_2026B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81FD, 0x0))

    Jump('loc_20586')

    def _loc_20287(): pass

    label('loc_20287')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81FE, 0x0))

    Jump('loc_20586')

    def _loc_202A3(): pass

    label('loc_202A3')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x81FF, 0x0))

    Jump('loc_20586')

    def _loc_202BF(): pass

    label('loc_202BF')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8200, 0x0))

    Jump('loc_20586')

    def _loc_202DB(): pass

    label('loc_202DB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8201, 0x0))

    Jump('loc_20586')

    def _loc_202F7(): pass

    label('loc_202F7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8202, 0x0))

    Jump('loc_20586')

    def _loc_20313(): pass

    label('loc_20313')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8203, 0x0))

    Jump('loc_20586')

    def _loc_2032F(): pass

    label('loc_2032F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8204, 0x0))

    Jump('loc_20586')

    def _loc_2034B(): pass

    label('loc_2034B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8205, 0x0))

    Jump('loc_20586')

    def _loc_20367(): pass

    label('loc_20367')

    SetScenaFlags(ScenaFlag(0x0736, 4, 0x39B4))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8206, 0x0))

    Jump('loc_20586')

    def _loc_20386(): pass

    label('loc_20386')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8207, 0x0))

    Jump('loc_20586')

    def _loc_203A2(): pass

    label('loc_203A2')

    SetScenaFlags(ScenaFlag(0x0736, 6, 0x39B6))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8208, 0x0))

    Jump('loc_20586')

    def _loc_203C1(): pass

    label('loc_203C1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8209, 0x0))

    Jump('loc_20586')

    def _loc_203DD(): pass

    label('loc_203DD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x820A, 0x0))

    Jump('loc_20586')

    def _loc_203F9(): pass

    label('loc_203F9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x820B, 0x0))

    Jump('loc_20586')

    def _loc_20415(): pass

    label('loc_20415')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x820C, 0x0))

    Jump('loc_20586')

    def _loc_20431(): pass

    label('loc_20431')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x820D, 0x0))

    Jump('loc_20586')

    def _loc_2044D(): pass

    label('loc_2044D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x820E, 0x0))

    Jump('loc_20586')

    def _loc_20469(): pass

    label('loc_20469')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x820F, 0x0))

    Jump('loc_20586')

    def _loc_20485(): pass

    label('loc_20485')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8210, 0x0))

    Jump('loc_20586')

    def _loc_204A1(): pass

    label('loc_204A1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8211, 0x0))

    Jump('loc_20586')

    def _loc_204BD(): pass

    label('loc_204BD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8212, 0x0))

    Jump('loc_20586')

    def _loc_204D9(): pass

    label('loc_204D9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8213, 0x0))

    Jump('loc_20586')

    def _loc_204F5(): pass

    label('loc_204F5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8214, 0x0))

    Jump('loc_20586')

    def _loc_20511(): pass

    label('loc_20511')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8215, 0x0))

    Jump('loc_20586')

    def _loc_2052D(): pass

    label('loc_2052D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8216, 0x0))

    Jump('loc_20586')

    def _loc_20549(): pass

    label('loc_20549')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8217, 0x0))

    Jump('loc_20586')

    def _loc_20565(): pass

    label('loc_20565')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8218, 0x0))

    Jump('loc_20586')

    def _loc_20581(): pass

    label('loc_20581')

    Jump('loc_20586')

    def _loc_20586(): pass

    label('loc_20586')

    Jump('loc_1F10D')

    def _loc_2058B(): pass

    label('loc_2058B')

    Return()

# id: 0x008B offset: 0x2058C
@scena.Code('EV_Jump_SB_03A_00')
def EV_Jump_SB_03A_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_20595(): pass

    label('loc_20595')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2107E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_03A_00_00] [艦長席でオリビエ達と会話　　　]', 0x00008219)
    MenuCmd(0x01, 0x02, '[SB_03A_00_01] [艦長席でオリビエ達と会話２　　]', 0x0000821A)
    MenuCmd(0x01, 0x02, '[SB_03A_00_02] [オリヴァルト＆アルフィンと会話]', 0x0000821B)
    MenuCmd(0x01, 0x02, '[SB_03A_00_02B][シェラザード・追加任意イベント]', 0x00008280)
    MenuCmd(0x01, 0x02, '[SB_03A_00_02C][ＬＰ・アーティファクトを調べる]', 0x00008281)
    MenuCmd(0x01, 0x02, '[SB_03A_00_03] [シェラと会話　　　　　　　　　]', 0x0000821C)
    MenuCmd(0x01, 0x02, '[SB_03A_00_04] [４Ｆでミュラー＆クルトと会話　]', 0x0000821D)
    MenuCmd(0x01, 0x02, '[SB_03A_00_05] [ミュラーと会話　　　　　　　　]', 0x0000821E)
    MenuCmd(0x01, 0x02, '[SB_03A_00_06] [３階会議室でミハイル達と会話　]', 0x0000821F)
    MenuCmd(0x01, 0x02, '[SB_03A_00_07] [ミハイルと会話　　　　　　　　]', 0x00008220)
    MenuCmd(0x01, 0x02, '[SB_03A_00_08] [２Ｆでトヴァル＆サラと会話　　]', 0x00008221)
    MenuCmd(0x01, 0x02, '[SB_03A_00_09] [２Ｆ甲板でパトリック達と会話　]', 0x00008222)
    MenuCmd(0x01, 0x02, '[SB_03A_00_10] [２Ｆ甲板でパトリック達と会話２]', 0x00008223)
    MenuCmd(0x01, 0x02, '[SB_03A_00_11] [１Ｆでグエン達と会話　　　　　]', 0x00008224)
    MenuCmd(0x01, 0x02, '[SB_03A_00_12] [ラウラ＆デュバリィ　　　　　　]', 0x00008225)
    MenuCmd(0x01, 0x02, '[SB_03A_00_13] [食堂でアッシュ達との会話　　　]', 0x00008226)
    MenuCmd(0x01, 0x02, '[SB_03A_00_14] [医務室でヴィヴィ達との会話　　]', 0x00008227)
    MenuCmd(0x01, 0x02, '[SB_03A_00_15] [マルガリータ＆ドロテ＆ムンク　]', 0x00008228)
    MenuCmd(0x01, 0x02, '[SB_03A_00_16] [ベッキー＆レックス＆マキアス　]', 0x00008229)
    MenuCmd(0x01, 0x02, '[SB_03A_00_17] [ミント＆ケネス＆エリオット　　]', 0x0000822A)
    MenuCmd(0x01, 0x02, '[SB_03A_00_18] [オリビエからのアナウンス　　　]', 0x0000822B)
    MenuCmd(0x01, 0x02, '[SB_03A_00_19] [月霊窟に向かう　　　　　　　　]', 0x00008231)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008219, 'loc_20C7D'),
        (0x0000821A, 'loc_20C7D'),
        (0x0000821B, 'loc_20C7D'),
        (0x00008280, 'loc_20C7D'),
        (0x00008281, 'loc_20C7D'),
        (0x0000821C, 'loc_20C7D'),
        (0x0000821D, 'loc_20C7D'),
        (0x0000821E, 'loc_20C7D'),
        (0x0000821F, 'loc_20C7D'),
        (0x00008220, 'loc_20C7D'),
        (0x00008221, 'loc_20C7D'),
        (0x00008222, 'loc_20C7D'),
        (0x00008223, 'loc_20C7D'),
        (0x00008224, 'loc_20C7D'),
        (0x00008225, 'loc_20C7D'),
        (0x00008226, 'loc_20C7D'),
        (0x00008227, 'loc_20C7D'),
        (0x00008228, 'loc_20C7D'),
        (0x00008229, 'loc_20C7D'),
        (0x0000822A, 'loc_20C7D'),
        (0x0000822B, 'loc_20C7D'),
        (0x00008231, 'loc_20C7D'),
        (-1, 'loc_20C8B'),
    )

    def _loc_20C7D(): pass

    label('loc_20C7D')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x400D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_20C99')

    def _loc_20C8B(): pass

    label('loc_20C8B')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_20C99')

    def _loc_20C99(): pass

    label('loc_20C99')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20CD0',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_20CD0(): pass

    label('loc_20CD0')

    OP_71(0x00, 0x4580, 0x4582)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008231, 'loc_20D17'),
        (0x0000822B, 'loc_20D1D'),
        (0x0000821C, 'loc_20D31'),
        (0x00008281, 'loc_20D31'),
        (0x00008280, 'loc_20D34'),
        (0x0000821B, 'loc_20D3F'),
        (0x0000821A, 'loc_20D42'),
        (-1, 'loc_20D4A'),
    )

    def _loc_20D17(): pass

    label('loc_20D17')

    OP_71(0x00, 0x4396, 0x439B)

    def _loc_20D1D(): pass

    label('loc_20D1D')

    SetScenaFlags(ScenaFlag(0x0860, 1, 0x4301))
    OP_71(0x00, 0x4380, 0x438B)
    OP_71(0x00, 0x4390, 0x4395)

    Jump('loc_20D4A')

    def _loc_20D31(): pass

    label('loc_20D31')

    SetScenaFlags(ScenaFlag(0x0876, 0, 0x43B0))

    def _loc_20D34(): pass

    label('loc_20D34')

    SetScenaFlags(ScenaFlag(0x0870, 1, 0x4381))
    SetScenaFlags(ScenaFlag(0x0870, 0, 0x4380))

    Jump('loc_20D4A')

    def _loc_20D3F(): pass

    label('loc_20D3F')

    SetScenaFlags(ScenaFlag(0x0870, 1, 0x4381))

    def _loc_20D42(): pass

    label('loc_20D42')

    SetScenaFlags(ScenaFlag(0x0870, 0, 0x4380))

    Jump('loc_20D4A')

    def _loc_20D4A(): pass

    label('loc_20D4A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008219, 'loc_20E03'),
        (0x0000821A, 'loc_20E1F'),
        (0x0000821B, 'loc_20E3B'),
        (0x00008280, 'loc_20E57'),
        (0x00008281, 'loc_20E73'),
        (0x0000821C, 'loc_20E8F'),
        (0x0000821D, 'loc_20EAB'),
        (0x0000821E, 'loc_20EC7'),
        (0x0000821F, 'loc_20EE6'),
        (0x00008220, 'loc_20F02'),
        (0x00008221, 'loc_20F21'),
        (0x00008222, 'loc_20F3D'),
        (0x00008223, 'loc_20F59'),
        (0x00008224, 'loc_20F78'),
        (0x00008225, 'loc_20F94'),
        (0x00008226, 'loc_20FB0'),
        (0x00008227, 'loc_20FCC'),
        (0x00008228, 'loc_20FE8'),
        (0x00008229, 'loc_21004'),
        (0x0000822A, 'loc_21020'),
        (0x0000822B, 'loc_2103C'),
        (0x00008231, 'loc_21058'),
        (-1, 'loc_21074'),
    )

    def _loc_20E03(): pass

    label('loc_20E03')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8219, 0x0))

    Jump('loc_21079')

    def _loc_20E1F(): pass

    label('loc_20E1F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x821A, 0x0))

    Jump('loc_21079')

    def _loc_20E3B(): pass

    label('loc_20E3B')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x821B, 0x0))

    Jump('loc_21079')

    def _loc_20E57(): pass

    label('loc_20E57')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8280, 0x0))

    Jump('loc_21079')

    def _loc_20E73(): pass

    label('loc_20E73')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8281, 0x0))

    Jump('loc_21079')

    def _loc_20E8F(): pass

    label('loc_20E8F')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x821C, 0x0))

    Jump('loc_21079')

    def _loc_20EAB(): pass

    label('loc_20EAB')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x821D, 0x0))

    Jump('loc_21079')

    def _loc_20EC7(): pass

    label('loc_20EC7')

    SetScenaFlags(ScenaFlag(0x0870, 4, 0x4384))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x821E, 0x0))

    Jump('loc_21079')

    def _loc_20EE6(): pass

    label('loc_20EE6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x821F, 0x0))

    Jump('loc_21079')

    def _loc_20F02(): pass

    label('loc_20F02')

    SetScenaFlags(ScenaFlag(0x0870, 6, 0x4386))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8220, 0x0))

    Jump('loc_21079')

    def _loc_20F21(): pass

    label('loc_20F21')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8221, 0x0))

    Jump('loc_21079')

    def _loc_20F3D(): pass

    label('loc_20F3D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8222, 0x0))

    Jump('loc_21079')

    def _loc_20F59(): pass

    label('loc_20F59')

    SetScenaFlags(ScenaFlag(0x0871, 1, 0x4389))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8223, 0x0))

    Jump('loc_21079')

    def _loc_20F78(): pass

    label('loc_20F78')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8224, 0x0))

    Jump('loc_21079')

    def _loc_20F94(): pass

    label('loc_20F94')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8225, 0x0))

    Jump('loc_21079')

    def _loc_20FB0(): pass

    label('loc_20FB0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8226, 0x0))

    Jump('loc_21079')

    def _loc_20FCC(): pass

    label('loc_20FCC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8227, 0x0))

    Jump('loc_21079')

    def _loc_20FE8(): pass

    label('loc_20FE8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8228, 0x0))

    Jump('loc_21079')

    def _loc_21004(): pass

    label('loc_21004')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8229, 0x0))

    Jump('loc_21079')

    def _loc_21020(): pass

    label('loc_21020')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x822A, 0x0))

    Jump('loc_21079')

    def _loc_2103C(): pass

    label('loc_2103C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x822C, 0x0))

    Jump('loc_21079')

    def _loc_21058(): pass

    label('loc_21058')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8231, 0x0))

    Jump('loc_21079')

    def _loc_21074(): pass

    label('loc_21074')

    Jump('loc_21079')

    def _loc_21079(): pass

    label('loc_21079')

    Jump('loc_20595')

    def _loc_2107E(): pass

    label('loc_2107E')

    Return()

# id: 0x008C offset: 0x21080
@scena.Code('EV_Jump_SB_03B_00')
def EV_Jump_SB_03B_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_21089(): pass

    label('loc_21089')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2131B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_03B_00_00][リヴィエラコートを見る　　　　]', 0x00008232)
    MenuCmd(0x01, 0x02, '[SB_03B_00_01][エントランス・選択肢　　　　　]', 0x00008233)
    MenuCmd(0x01, 0x02, '[SB_03B_00_02][公爵家城館でプリシラと会話する]', 0x00008234)
    MenuCmd(0x01, 0x02, '[SB_03B_00_03][ハイアームズ達を見かける　　　]', 0x00008235)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008232, 'loc_211F1'),
        (0x00008233, 'loc_211F1'),
        (0x00008234, 'loc_211F1'),
        (0x00008235, 'loc_211F1'),
        (-1, 'loc_211FF'),
    )

    def _loc_211F1(): pass

    label('loc_211F1')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2120D')

    def _loc_211FF(): pass

    label('loc_211FF')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2120D')

    def _loc_2120D(): pass

    label('loc_2120D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21244',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_21244(): pass

    label('loc_21244')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008232, 'loc_2126D'),
        (0x00008233, 'loc_2126D'),
        (0x00008234, 'loc_2126D'),
        (0x00008235, 'loc_21270'),
        (-1, 'loc_21278'),
    )

    def _loc_2126D(): pass

    label('loc_2126D')

    SetScenaFlags(ScenaFlag(0x0873, 7, 0x439F))

    def _loc_21270(): pass

    label('loc_21270')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_21278')

    def _loc_21278(): pass

    label('loc_21278')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008232, 'loc_212A1'),
        (0x00008233, 'loc_212BD'),
        (0x00008234, 'loc_212D9'),
        (0x00008235, 'loc_212F5'),
        (-1, 'loc_21311'),
    )

    def _loc_212A1(): pass

    label('loc_212A1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8232, 0x0))

    Jump('loc_21316')

    def _loc_212BD(): pass

    label('loc_212BD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8233, 0x0))

    Jump('loc_21316')

    def _loc_212D9(): pass

    label('loc_212D9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8234, 0x0))

    Jump('loc_21316')

    def _loc_212F5(): pass

    label('loc_212F5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8235, 0x0))

    Jump('loc_21316')

    def _loc_21311(): pass

    label('loc_21311')

    Jump('loc_21316')

    def _loc_21316(): pass

    label('loc_21316')

    Jump('loc_21089')

    def _loc_2131B(): pass

    label('loc_2131B')

    Return()

# id: 0x008D offset: 0x2131C
@scena.Code('EV_Jump_SB_03D_00')
def EV_Jump_SB_03D_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_21325(): pass

    label('loc_21325')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2163B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_03D_00_00][病院へ向かうプリシラを見送る　]', 0x00008236)
    MenuCmd(0x01, 0x02, '[SB_03D_01_00][港湾区でレンが家族と会う　　　]', 0x00008237)
    MenuCmd(0x01, 0x02, '[SB_03D_01_01][モルジュにいるオスカーとロイド]', 0x00008238)
    MenuCmd(0x01, 0x02, '[SB_03D_01_02][黄昏ているベネットを見つける　]', 0x00008239)
    MenuCmd(0x01, 0x02, '[SB_03D_01_03][オスカーとベネットのパン勝負　]', 0x0000823A)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008236, 'loc_214DA'),
        (0x00008237, 'loc_214E8'),
        (0x00008238, 'loc_214E8'),
        (0x00008239, 'loc_214E8'),
        (0x0000823A, 'loc_214E8'),
        (-1, 'loc_214F6'),
    )

    def _loc_214DA(): pass

    label('loc_214DA')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_21504')

    def _loc_214E8(): pass

    label('loc_214E8')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4089),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_21504')

    def _loc_214F6(): pass

    label('loc_214F6')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_21504')

    def _loc_21504(): pass

    label('loc_21504')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2153B',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_2153B(): pass

    label('loc_2153B')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008236, 'loc_2156C'),
        (0x00008237, 'loc_2156C'),
        (0x00008238, 'loc_2156C'),
        (0x00008239, 'loc_2156C'),
        (0x0000823A, 'loc_2156C'),
        (-1, 'loc_21574'),
    )

    def _loc_2156C(): pass

    label('loc_2156C')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_21574')

    def _loc_21574(): pass

    label('loc_21574')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008236, 'loc_215A5'),
        (0x00008237, 'loc_215C1'),
        (0x00008238, 'loc_215DD'),
        (0x00008239, 'loc_215F9'),
        (0x0000823A, 'loc_21615'),
        (-1, 'loc_21631'),
    )

    def _loc_215A5(): pass

    label('loc_215A5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8236, 0x0))

    Jump('loc_21636')

    def _loc_215C1(): pass

    label('loc_215C1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8237, 0x0))

    Jump('loc_21636')

    def _loc_215DD(): pass

    label('loc_215DD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8238, 0x0))

    Jump('loc_21636')

    def _loc_215F9(): pass

    label('loc_215F9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8239, 0x0))

    Jump('loc_21636')

    def _loc_21615(): pass

    label('loc_21615')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x823A, 0x0))

    Jump('loc_21636')

    def _loc_21631(): pass

    label('loc_21631')

    Jump('loc_21636')

    def _loc_21636(): pass

    label('loc_21636')

    Jump('loc_21325')

    def _loc_2163B(): pass

    label('loc_2163B')

    Return()

# id: 0x008E offset: 0x2163C
@scena.Code('EV_Jump_SB_03E_00')
def EV_Jump_SB_03E_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_21645(): pass

    label('loc_21645')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21953',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_03E_00_00][ウルスラ病院の敷地に入る　　　]', 0x0000823C)
    MenuCmd(0x01, 0x02, '[SB_03E_00_01][プリシラとセシルとの会話　　　]', 0x0000823D)
    MenuCmd(0x01, 0x02, '[SB_03E_00_02][手術直前の皇帝を見舞う　　　　]', 0x0000823E)
    MenuCmd(0x01, 0x02, '[SB_03E_00_03][見舞い後の会話　　　　　　　　]', 0x0000823F)
    MenuCmd(0x01, 0x02, '[SB_03E_00_04][パティリーとカルゴの再会　　　]', 0x00008240)
    MenuCmd(0x06, 0x02, 0x0004)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000823C, 'loc_217FF'),
        (0x0000823D, 'loc_217FF'),
        (0x0000823E, 'loc_217FF'),
        (0x0000823F, 'loc_217FF'),
        (0x00008240, 'loc_217FF'),
        (-1, 'loc_2180D'),
    )

    def _loc_217FF(): pass

    label('loc_217FF')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x40B2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2181B')

    def _loc_2180D(): pass

    label('loc_2180D')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2181B')

    def _loc_2181B(): pass

    label('loc_2181B')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21852',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_21852(): pass

    label('loc_21852')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000823F, 'loc_2187B'),
        (0x0000823E, 'loc_2187E'),
        (0x0000823D, 'loc_21881'),
        (0x0000823C, 'loc_21884'),
        (-1, 'loc_2188C'),
    )

    def _loc_2187B(): pass

    label('loc_2187B')

    SetScenaFlags(ScenaFlag(0x0871, 6, 0x438E))

    def _loc_2187E(): pass

    label('loc_2187E')

    SetScenaFlags(ScenaFlag(0x0871, 5, 0x438D))

    def _loc_21881(): pass

    label('loc_21881')

    SetScenaFlags(ScenaFlag(0x0871, 4, 0x438C))

    def _loc_21884(): pass

    label('loc_21884')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_2188C')

    def _loc_2188C(): pass

    label('loc_2188C')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000823C, 'loc_218BD'),
        (0x0000823D, 'loc_218D9'),
        (0x0000823E, 'loc_218F5'),
        (0x0000823F, 'loc_21911'),
        (0x00008240, 'loc_2192D'),
        (-1, 'loc_21949'),
    )

    def _loc_218BD(): pass

    label('loc_218BD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x823C, 0x0))

    Jump('loc_2194E')

    def _loc_218D9(): pass

    label('loc_218D9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x823D, 0x0))

    Jump('loc_2194E')

    def _loc_218F5(): pass

    label('loc_218F5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x823E, 0x0))

    Jump('loc_2194E')

    def _loc_21911(): pass

    label('loc_21911')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x823F, 0x0))

    Jump('loc_2194E')

    def _loc_2192D(): pass

    label('loc_2192D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8240, 0x0))

    Jump('loc_2194E')

    def _loc_21949(): pass

    label('loc_21949')

    Jump('loc_2194E')

    def _loc_2194E(): pass

    label('loc_2194E')

    Jump('loc_21645')

    def _loc_21953(): pass

    label('loc_21953')

    Return()

# id: 0x008F offset: 0x21954
@scena.Code('EV_Jump_SB_03X_00')
def EV_Jump_SB_03X_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2195D(): pass

    label('loc_2195D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2243B',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_03X_00_00][ビーチ脇でユーシス達と会話　　]', 0x00008241)
    MenuCmd(0x01, 0x02, '[SB_03X_00_01][ミリアムと会話　　　　　　　　]', 0x00008242)
    MenuCmd(0x01, 0x02, '[SB_03X_00_02][観覧車前でジョルジュ達と会話　]', 0x00008243)
    MenuCmd(0x01, 0x02, '[SB_03X_00_03][観覧車前でジョルジュ達と会話２]', 0x00008244)
    MenuCmd(0x01, 0x02, '[SB_03X_00_04][カシウス＆アルゼイドと会話　　]', 0x00008245)
    MenuCmd(0x01, 0x02, '[SB_03X_00_05][カシウスと会話（ＶＭ）　　　　]', 0x00008246)
    MenuCmd(0x01, 0x02, '[SB_03X_00_06][カシウス＆アルゼイドと会話２　]', 0x00008247)
    MenuCmd(0x01, 0x02, '[SB_03X_00_07][奥伝を授かる・選択肢　　　　　]', 0x00008248)
    MenuCmd(0x01, 0x02, '[SB_03X_00_08][カシウスから奥伝を授かる　　　]', 0x00008249)
    MenuCmd(0x01, 0x02, '[SB_03X_00_09][最悪の鬼化リィン戦　　　　　　]戦', 0x0000824A)
    MenuCmd(0x01, 0x02, '[SB_03X_00_10][リィンが剣聖になる　　　　　　]', 0x0000824B)
    MenuCmd(0x01, 0x02, '[SB_03X_00_11][ミントがお節介を焼く　　　　　]', 0x0000824D)
    MenuCmd(0x01, 0x02, '[SB_03X_00_12][ヴァリマールとの会話１　　　　]', 0x00008276)
    MenuCmd(0x01, 0x02, '[SB_03X_00_13][ヴァリマールとの会話２　　　　]', 0x00008277)
    MenuCmd(0x01, 0x02, '[SB_03X_00_14][ヴァリマールとの会話３　　　　]', 0x00008278)
    MenuCmd(0x01, 0x02, '[SB_03X_00_15][アントンとシャロンのやり取り　]', 0x0000824E)
    MenuCmd(0x01, 0x02, '[SB_03X_00_16][ケネスとアナベルのやり取り　　]', 0x0000827A)
    MenuCmd(0x01, 0x02, '[SB_03X_00_17][みっしぃ＆メカみっしぃショー　]', 0x0000827F)
    MenuCmd(0x01, 0x02, '[SB_03X_01_00][謎の導力メールが届く　　　　　]', 0x0000824F)
    MenuCmd(0x01, 0x02, '[SB_03X_01_01][湿地帯出口・選択肢　　　　　　]', 0x00008250)
    MenuCmd(0x01, 0x02, '[SB_03X_01_02][湿地帯でクレアと会話　　　　　]', 0x00008251)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008241, 'loc_21FE5'),
        (0x00008242, 'loc_21FE5'),
        (0x00008243, 'loc_21FE5'),
        (0x00008244, 'loc_21FE5'),
        (0x00008245, 'loc_21FE5'),
        (0x00008246, 'loc_21FE5'),
        (0x00008247, 'loc_21FE5'),
        (0x00008248, 'loc_21FE5'),
        (0x00008249, 'loc_21FE5'),
        (0x0000824A, 'loc_21FE5'),
        (0x0000824B, 'loc_21FE5'),
        (0x0000824D, 'loc_21FE5'),
        (0x00008276, 'loc_21FE5'),
        (0x00008277, 'loc_21FE5'),
        (0x00008278, 'loc_21FE5'),
        (0x0000824E, 'loc_21FE5'),
        (0x0000827A, 'loc_21FE5'),
        (0x0000827F, 'loc_21FE5'),
        (0x0000824F, 'loc_21FF3'),
        (0x00008250, 'loc_21FF3'),
        (0x00008251, 'loc_21FF3'),
        (-1, 'loc_22001'),
    )

    def _loc_21FE5(): pass

    label('loc_21FE5')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2200F')

    def _loc_21FF3(): pass

    label('loc_21FF3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x5011),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2200F')

    def _loc_22001(): pass

    label('loc_22001')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2200F')

    def _loc_2200F(): pass

    label('loc_2200F')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22047',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03X')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_22047(): pass

    label('loc_22047')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008250, 'loc_220A0'),
        (0x0000824F, 'loc_220A3'),
        (0x0000824F, 'loc_220A6'),
        (0x0000824E, 'loc_220A6'),
        (0x0000824B, 'loc_220AF'),
        (0x0000824A, 'loc_220B2'),
        (0x00008249, 'loc_220B5'),
        (0x00008248, 'loc_220B8'),
        (0x00008247, 'loc_220CA'),
        (0x00008246, 'loc_220CD'),
        (-1, 'loc_220D5'),
    )

    def _loc_220A0(): pass

    label('loc_220A0')

    SetScenaFlags(ScenaFlag(0x0981, 5, 0x4C0D))

    def _loc_220A3(): pass

    label('loc_220A3')

    SetScenaFlags(ScenaFlag(0x0981, 4, 0x4C0C))

    def _loc_220A6(): pass

    label('loc_220A6')

    SetScenaFlags(ScenaFlag(0x0981, 2, 0x4C0A))
    SetScenaFlags(ScenaFlag(0x0B76, 3, 0x5BB3))
    SetScenaFlags(ScenaFlag(0x0B76, 4, 0x5BB4))

    def _loc_220AF(): pass

    label('loc_220AF')

    SetScenaFlags(ScenaFlag(0x0981, 1, 0x4C09))

    def _loc_220B2(): pass

    label('loc_220B2')

    SetScenaFlags(ScenaFlag(0x0981, 0, 0x4C08))

    def _loc_220B5(): pass

    label('loc_220B5')

    SetScenaFlags(ScenaFlag(0x0980, 7, 0x4C07))

    def _loc_220B8(): pass

    label('loc_220B8')

    SetScenaFlags(ScenaFlag(0x0980, 6, 0x4C06))
    SetScenaFlags(ScenaFlag(0x0982, 1, 0x4C11))
    SetScenaFlags(ScenaFlag(0x0B80, 0, 0x5C00))
    SetScenaFlags(ScenaFlag(0x0B80, 1, 0x5C01))
    SetScenaFlags(ScenaFlag(0x0B80, 2, 0x5C02))
    OP_88(0x0000)

    def _loc_220CA(): pass

    label('loc_220CA')

    SetScenaFlags(ScenaFlag(0x0980, 5, 0x4C05))

    def _loc_220CD(): pass

    label('loc_220CD')

    SetScenaFlags(ScenaFlag(0x0980, 4, 0x4C04))

    Jump('loc_220D5')

    def _loc_220D5(): pass

    label('loc_220D5')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008241, 'loc_22186'),
        (0x00008242, 'loc_221A2'),
        (0x00008243, 'loc_221C1'),
        (0x00008244, 'loc_221DD'),
        (0x00008245, 'loc_221FC'),
        (0x00008246, 'loc_22218'),
        (0x00008247, 'loc_22234'),
        (0x00008248, 'loc_22250'),
        (0x00008249, 'loc_2226C'),
        (0x0000824A, 'loc_22288'),
        (0x0000824B, 'loc_222A4'),
        (0x0000824D, 'loc_222C0'),
        (0x00008276, 'loc_222DC'),
        (0x00008277, 'loc_222F8'),
        (0x00008278, 'loc_22314'),
        (0x0000824E, 'loc_22330'),
        (0x0000827A, 'loc_2234C'),
        (0x0000827F, 'loc_22368'),
        (0x0000824F, 'loc_22384'),
        (0x00008250, 'loc_223F9'),
        (0x00008251, 'loc_22415'),
        (-1, 'loc_22431'),
    )

    def _loc_22186(): pass

    label('loc_22186')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8241, 0x0))

    Jump('loc_22436')

    def _loc_221A2(): pass

    label('loc_221A2')

    SetScenaFlags(ScenaFlag(0x0980, 0, 0x4C00))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8242, 0x0))

    Jump('loc_22436')

    def _loc_221C1(): pass

    label('loc_221C1')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8243, 0x0))

    Jump('loc_22436')

    def _loc_221DD(): pass

    label('loc_221DD')

    SetScenaFlags(ScenaFlag(0x0980, 2, 0x4C02))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8244, 0x0))

    Jump('loc_22436')

    def _loc_221FC(): pass

    label('loc_221FC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8245, 0x0))

    Jump('loc_22436')

    def _loc_22218(): pass

    label('loc_22218')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8246, 0x0))

    Jump('loc_22436')

    def _loc_22234(): pass

    label('loc_22234')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8247, 0x0))

    Jump('loc_22436')

    def _loc_22250(): pass

    label('loc_22250')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8248, 0x0))

    Jump('loc_22436')

    def _loc_2226C(): pass

    label('loc_2226C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8249, 0x0))

    Jump('loc_22436')

    def _loc_22288(): pass

    label('loc_22288')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x824A, 0x0))

    Jump('loc_22436')

    def _loc_222A4(): pass

    label('loc_222A4')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x824B, 0x0))

    Jump('loc_22436')

    def _loc_222C0(): pass

    label('loc_222C0')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x824D, 0x0))

    Jump('loc_22436')

    def _loc_222DC(): pass

    label('loc_222DC')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8276, 0x0))

    Jump('loc_22436')

    def _loc_222F8(): pass

    label('loc_222F8')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8277, 0x0))

    Jump('loc_22436')

    def _loc_22314(): pass

    label('loc_22314')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8278, 0x0))

    Jump('loc_22436')

    def _loc_22330(): pass

    label('loc_22330')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x824E, 0x0))

    Jump('loc_22436')

    def _loc_2234C(): pass

    label('loc_2234C')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x827A, 0x0))

    Jump('loc_22436')

    def _loc_22368(): pass

    label('loc_22368')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x827F, 0x0))

    Jump('loc_22436')

    def _loc_22384(): pass

    label('loc_22384')

    CreateChr(ChrTable['黎恩'], 'C_CHR000', 'リィン', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    Call(ScriptId.System4, 'SB_03X_01_00')
    OP_28((0xDD, 'f4010'), (0xDD, 'go_f4000'), 0x00)

    Jump('loc_22436')

    def _loc_223F9(): pass

    label('loc_223F9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8250, 0x0))

    Jump('loc_22436')

    def _loc_22415(): pass

    label('loc_22415')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8251, 0x0))

    Jump('loc_22436')

    def _loc_22431(): pass

    label('loc_22431')

    Jump('loc_22436')

    def _loc_22436(): pass

    label('loc_22436')

    Jump('loc_2195D')

    def _loc_2243B(): pass

    label('loc_2243B')

    Return()

# id: 0x0090 offset: 0x2243C
@scena.Code('EV_Jump_SB_04_00')
def EV_Jump_SB_04_00():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_22445(): pass

    label('loc_22445')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23218',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[SB_04_00_00][ＲＦビルでイリーナ達と会話　　]', 0x00008253)
    MenuCmd(0x01, 0x02, '[SB_04_00_01][ドレックノール要塞前での会話　]', 0x00008254)
    MenuCmd(0x01, 0x02, '[SB_04_00_02][要塞中庭の様子　　　　　　　　]', 0x00008255)
    MenuCmd(0x01, 0x02, '[SB_04_00_03][司令室でクレイグ達と会話　　　]', 0x00008256)
    MenuCmd(0x01, 0x02, '[SB_04_00_04][オリビエ＆シェラとの会話　　　]', 0x00008257)
    MenuCmd(0x01, 0x02, '[SB_04_00_05][オリビエ＆シェラとの会話２　　]', 0x00008258)
    MenuCmd(0x01, 0x02, '[SB_04_00_06][準備をするヨナ＆シュリ　　　　]', 0x00008259)
    MenuCmd(0x01, 0x02, '[SB_04_00_07][セイランド達から手術結果を聞く]', 0x0000825A)
    MenuCmd(0x01, 0x02, '[SB_04_00_08][手術後のユーゲント＆プリシラ　]', 0x0000825B)
    MenuCmd(0x01, 0x02, '[SB_04_00_09][鉄騎隊・ブルブランに遭遇　　　]', 0x00008275)
    MenuCmd(0x01, 0x02, '[SB_04_00_10][レンとハロルドが会う　　　　　]', 0x0000827B)
    MenuCmd(0x01, 0x02, '[SB_04_00_11][アークロイアル号との通信　　　]', 0x0000827C)
    MenuCmd(0x01, 0x02, '[SB_04_00_12][本校会議室でのトールズ作戦会議]', 0x0000827D)
    MenuCmd(0x01, 0x02, '[SB_04_00_13][v1.03ハーシェル家と友人たち]', 0x00008284)
    MenuCmd(0x01, 0x02, '[SB_04_01_00][小庭園でユウナ達と会話　　　　]', 0x0000825C)
    MenuCmd(0x01, 0x02, '[SB_04_01_01][クルトとの会話　　　　　　　　]', 0x0000825D)
    MenuCmd(0x01, 0x02, '[SB_04_01_02][フィーとの会話　　　　　　　　]', 0x0000825E)
    MenuCmd(0x01, 0x02, '[SB_04_01_03][アッシュとの会話　　　　　　　]', 0x0000825F)
    MenuCmd(0x01, 0x02, '[SB_04_01_04][ミリアムとの会話　　　　　　　]', 0x00008279)
    MenuCmd(0x01, 0x02, '[SB_04_02_00][サラとの会話　　　　　　　　　]', 0x00008260)
    MenuCmd(0x01, 0x02, '[SB_04_02_01][ユーシスとの会話　　　　　　　]', 0x00008261)
    MenuCmd(0x01, 0x02, '[SB_04_03_00][アリサとの会話　　　　　　　　]', 0x00008262)
    MenuCmd(0x01, 0x02, '[SB_04_04_00][ユーシス＆ミリアムとの会話　　]', 0x00008263)
    MenuCmd(0x01, 0x02, '[SB_04_05_00][エマ＆セリーヌとの会話　　　　]', 0x00008264)
    MenuCmd(0x01, 0x02, '[SB_04_05_01][ガイウスとの会話　　　　　　　]', 0x00008265)
    MenuCmd(0x01, 0x02, '[SB_04_05_02][クロウとの会話　　　　　　　　]', 0x00008266)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008253, 'loc_22C2A'),
        (0x00008254, 'loc_22C2A'),
        (0x00008255, 'loc_22C2A'),
        (0x00008256, 'loc_22C2A'),
        (0x00008257, 'loc_22C2A'),
        (0x00008258, 'loc_22C2A'),
        (0x00008259, 'loc_22C2A'),
        (0x0000825A, 'loc_22C2A'),
        (0x0000825B, 'loc_22C2A'),
        (0x00008275, 'loc_22C2A'),
        (0x0000827B, 'loc_22C2A'),
        (0x0000827C, 'loc_22C2A'),
        (0x0000827D, 'loc_22C2A'),
        (0x00008284, 'loc_22C2A'),
        (0x0000825C, 'loc_22C38'),
        (0x0000825D, 'loc_22C38'),
        (0x0000825E, 'loc_22C38'),
        (0x0000825F, 'loc_22C38'),
        (0x00008279, 'loc_22C38'),
        (0x00008260, 'loc_22C46'),
        (0x00008261, 'loc_22C46'),
        (0x00008262, 'loc_22C54'),
        (0x00008263, 'loc_22C62'),
        (0x00008264, 'loc_22C70'),
        (0x00008265, 'loc_22C70'),
        (0x00008266, 'loc_22C70'),
        (-1, 'loc_22C7E'),
    )

    def _loc_22C2A(): pass

    label('loc_22C2A')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22C8C')

    def _loc_22C38(): pass

    label('loc_22C38')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6059),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22C8C')

    def _loc_22C46(): pass

    label('loc_22C46')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6061),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22C8C')

    def _loc_22C54(): pass

    label('loc_22C54')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6066),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22C8C')

    def _loc_22C62(): pass

    label('loc_22C62')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x606E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22C8C')

    def _loc_22C70(): pass

    label('loc_22C70')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6075),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22C8C')

    def _loc_22C7E(): pass

    label('loc_22C7E')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22C8C')

    def _loc_22C8C(): pass

    label('loc_22C8C')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22CC3',
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_22CC3(): pass

    label('loc_22CC3')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008284, 'loc_22D84'),
        (0x0000827D, 'loc_22D84'),
        (0x0000827C, 'loc_22D84'),
        (0x0000827B, 'loc_22D84'),
        (0x0000825B, 'loc_22D84'),
        (0x0000825A, 'loc_22D87'),
        (0x00008259, 'loc_22D87'),
        (0x00008258, 'loc_22D8F'),
        (0x00008256, 'loc_22D97'),
        (0x00008255, 'loc_22D9A'),
        (0x00008254, 'loc_22D9D'),
        (0x0000825C, 'loc_22DA5'),
        (0x0000825D, 'loc_22DA5'),
        (0x0000825E, 'loc_22DA5'),
        (0x0000825F, 'loc_22DA5'),
        (0x00008279, 'loc_22DA5'),
        (0x00008260, 'loc_22DA5'),
        (0x00008261, 'loc_22DA5'),
        (0x00008262, 'loc_22DA5'),
        (0x00008263, 'loc_22DA5'),
        (0x00008264, 'loc_22DA5'),
        (0x00008265, 'loc_22DA5'),
        (0x00008266, 'loc_22DA5'),
        (-1, 'loc_22E5A'),
    )

    def _loc_22D84(): pass

    label('loc_22D84')

    SetScenaFlags(ScenaFlag(0x0A32, 2, 0x5192))

    def _loc_22D87(): pass

    label('loc_22D87')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_22E5A')

    def _loc_22D8F(): pass

    label('loc_22D8F')

    SetScenaFlags(ScenaFlag(0x0A31, 7, 0x518F))

    Jump('loc_22E5A')

    def _loc_22D97(): pass

    label('loc_22D97')

    SetScenaFlags(ScenaFlag(0x0A30, 2, 0x5182))

    def _loc_22D9A(): pass

    label('loc_22D9A')

    SetScenaFlags(ScenaFlag(0x0A30, 1, 0x5181))

    def _loc_22D9D(): pass

    label('loc_22D9D')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_22E5A')

    def _loc_22DA5(): pass

    label('loc_22DA5')

    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['妙婕'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克蕾雅少校'], 0x00000100)

    Jump('loc_22E5A')

    def _loc_22E5A(): pass

    label('loc_22E5A')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008253, 'loc_22F33'),
        (0x00008254, 'loc_22F52'),
        (0x00008255, 'loc_22F6E'),
        (0x00008256, 'loc_22F8A'),
        (0x00008257, 'loc_22FA6'),
        (0x00008258, 'loc_22FC2'),
        (0x00008259, 'loc_22FDE'),
        (0x0000825A, 'loc_22FFA'),
        (0x0000825B, 'loc_23016'),
        (0x00008275, 'loc_23032'),
        (0x0000827B, 'loc_2304E'),
        (0x0000827C, 'loc_2306A'),
        (0x0000827D, 'loc_23086'),
        (0x00008284, 'loc_230A2'),
        (0x0000825C, 'loc_230BE'),
        (0x0000825D, 'loc_230DA'),
        (0x0000825E, 'loc_230F6'),
        (0x0000825F, 'loc_23112'),
        (0x00008279, 'loc_2312E'),
        (0x00008260, 'loc_2314A'),
        (0x00008261, 'loc_23166'),
        (0x00008262, 'loc_23182'),
        (0x00008263, 'loc_2319E'),
        (0x00008264, 'loc_231BA'),
        (0x00008265, 'loc_231D6'),
        (0x00008266, 'loc_231F2'),
        (-1, 'loc_2320E'),
    )

    def _loc_22F33(): pass

    label('loc_22F33')

    FormationCtrl(0x1C, 0x01)
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8253, 0x0))

    Jump('loc_23213')

    def _loc_22F52(): pass

    label('loc_22F52')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8254, 0x0))

    Jump('loc_23213')

    def _loc_22F6E(): pass

    label('loc_22F6E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8255, 0x0))

    Jump('loc_23213')

    def _loc_22F8A(): pass

    label('loc_22F8A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8256, 0x0))

    Jump('loc_23213')

    def _loc_22FA6(): pass

    label('loc_22FA6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8257, 0x0))

    Jump('loc_23213')

    def _loc_22FC2(): pass

    label('loc_22FC2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8258, 0x0))

    Jump('loc_23213')

    def _loc_22FDE(): pass

    label('loc_22FDE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8259, 0x0))

    Jump('loc_23213')

    def _loc_22FFA(): pass

    label('loc_22FFA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x825A, 0x0))

    Jump('loc_23213')

    def _loc_23016(): pass

    label('loc_23016')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x825B, 0x0))

    Jump('loc_23213')

    def _loc_23032(): pass

    label('loc_23032')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8275, 0x0))

    Jump('loc_23213')

    def _loc_2304E(): pass

    label('loc_2304E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x827B, 0x0))

    Jump('loc_23213')

    def _loc_2306A(): pass

    label('loc_2306A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x827C, 0x0))

    Jump('loc_23213')

    def _loc_23086(): pass

    label('loc_23086')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x827D, 0x0))

    Jump('loc_23213')

    def _loc_230A2(): pass

    label('loc_230A2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8284, 0x0))

    Jump('loc_23213')

    def _loc_230BE(): pass

    label('loc_230BE')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x825C, 0x0))

    Jump('loc_23213')

    def _loc_230DA(): pass

    label('loc_230DA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x825D, 0x0))

    Jump('loc_23213')

    def _loc_230F6(): pass

    label('loc_230F6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x825E, 0x0))

    Jump('loc_23213')

    def _loc_23112(): pass

    label('loc_23112')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x825F, 0x0))

    Jump('loc_23213')

    def _loc_2312E(): pass

    label('loc_2312E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8279, 0x0))

    Jump('loc_23213')

    def _loc_2314A(): pass

    label('loc_2314A')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8260, 0x0))

    Jump('loc_23213')

    def _loc_23166(): pass

    label('loc_23166')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8261, 0x0))

    Jump('loc_23213')

    def _loc_23182(): pass

    label('loc_23182')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8262, 0x0))

    Jump('loc_23213')

    def _loc_2319E(): pass

    label('loc_2319E')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8263, 0x0))

    Jump('loc_23213')

    def _loc_231BA(): pass

    label('loc_231BA')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8264, 0x0))

    Jump('loc_23213')

    def _loc_231D6(): pass

    label('loc_231D6')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8265, 0x0))

    Jump('loc_23213')

    def _loc_231F2(): pass

    label('loc_231F2')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8266, 0x0))

    Jump('loc_23213')

    def _loc_2320E(): pass

    label('loc_2320E')

    Jump('loc_23213')

    def _loc_23213(): pass

    label('loc_23213')

    Jump('loc_22445')

    def _loc_23218(): pass

    label('loc_23218')

    Return()

# id: 0x0091 offset: 0x2321C
@scena.Code('EV_YarikomiJump')
def EV_YarikomiJump():
    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_23237(): pass

    label('loc_23237')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23344',
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2333F',
    )

    MenuCmd(0x01, 0x00, '温泉測試', 0x00000001)
    MenuCmd(0x01, 0x00, '钓鱼相关', 0x00000009)
    MenuCmd(0x01, 0x00, '全体人员瞬间胜利', 0x0000000D)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000001, 'loc_232E2'),
        (0x00000009, 'loc_232FA'),
        (0x0000000D, 'loc_23315'),
        (-1, 'loc_23328'),
    )

    def _loc_232E2(): pass

    label('loc_232E2')

    Call(ScriptId.Current, 'EV_Jump_YR_Bath')

    Jump('loc_23336')

    def _loc_232FA(): pass

    label('loc_232FA')

    Call(ScriptId.Current, 'EV_Jump_YR_Fishing')

    Jump('loc_23336')

    def _loc_23315(): pass

    label('loc_23315')

    Call(ScriptId.System4, 'YR_POM_Complete')

    def _loc_23328(): pass

    label('loc_23328')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_23336')

    def _loc_23336(): pass

    label('loc_23336')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2333F(): pass

    label('loc_2333F')

    Jump('loc_23237')

    def _loc_23344(): pass

    label('loc_23344')

    Return()

# id: 0x0092 offset: 0x23348
@scena.Code('EV_Jump_YR_Bath')
def EV_Jump_YR_Bath():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_23351(): pass

    label('loc_23351')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_244B3',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '[YR_BATH_02_00_00] [温泉イベント・第Ⅱ部00　　　　]', 0x00008640)
    MenuCmd(0x01, 0x02, '[YR_BATH_02_02_01] [温泉イベント・第Ⅱ部02オル編①]', 0x00008641)
    MenuCmd(0x01, 0x02, '[YR_BATH_02_03_01] [温泉イベント・第Ⅱ部03ドレ編①]', 0x00008642)
    MenuCmd(0x01, 0x02, '[YR_BATH_02_04_01] [温泉イベント・第Ⅱ部04リー編①]', 0x00008643)
    MenuCmd(0x01, 0x02, '[YR_BATH_02_05_01] [温泉イベント・第Ⅱ部05パン編①]', 0x00008644)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_00_00S][風呂イベント・第Ⅲ部00　　　　]', 0x00008645)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_00_00] [風呂イベント・第Ⅲ部00　　　　]', 0x00008646)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_02_01] [温泉イベント・第Ⅲ部02ガル編①]', 0x00008647)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_02_04S][風呂イベント・第Ⅲ部02ガル編④]', 0x00008648)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_02_04] [風呂イベント・第Ⅲ部02ガル編④]', 0x00008649)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_04_01] [温泉イベント・第Ⅲ部04裏オ編①]', 0x0000864A)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_05_01S][風呂イベント・第Ⅲ部05星霊編①]', 0x0000864B)
    MenuCmd(0x01, 0x02, '[YR_BATH_03_05_01] [風呂イベント・第Ⅲ部05星霊編①]', 0x0000864C)
    MenuCmd(0x01, 0x02, '[YR_BATH_04_00_00] [温泉イベント・最終幕00　　　　]', 0x0000864D)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008640, 'loc_237F3'),
        (0x00008641, 'loc_2382A'),
        (0x00008642, 'loc_238EA'),
        (0x00008643, 'loc_23A75'),
        (0x00008644, 'loc_23B35'),
        (0x00008645, 'loc_23BF2'),
        (0x00008646, 'loc_23BF2'),
        (0x00008647, 'loc_23C29'),
        (0x00008648, 'loc_23D16'),
        (0x00008649, 'loc_23D16'),
        (0x0000864A, 'loc_23D4D'),
        (0x0000864B, 'loc_23E15'),
        (0x0000864C, 'loc_23E15'),
        (0x0000864D, 'loc_23E4C'),
        (-1, 'loc_242A8'),
    )

    def _loc_237F3(): pass

    label('loc_237F3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    Jump('loc_242A8')

    def _loc_2382A(): pass

    label('loc_2382A')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3030),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    def _loc_23846(): pass

    label('loc_23846')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0017)"),
            Expr.Ez,
            (Expr.Eval, "FormationCtrl(0x05, 0x0023)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_238E5',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'クロウとデュバリィをパーティに入れて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    Jump('loc_23846')

    def _loc_238E5(): pass

    label('loc_238E5')

    Jump('loc_242A8')

    def _loc_238EA(): pass

    label('loc_238EA')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3062),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2390F(): pass

    label('loc_2390F')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0012)"),
            Expr.Ez,
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_23A70',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'アンゼリカと女子３名をパーティに入れて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x000A)"),
            Expr.Return,
        ),
        'loc_239CB',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_239CB(): pass

    label('loc_239CB')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x000C)"),
            Expr.Return,
        ),
        'loc_239DF',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_239DF(): pass

    label('loc_239DF')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x000D)"),
            Expr.Return,
        ),
        'loc_239F3',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_239F3(): pass

    label('loc_239F3')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0001)"),
            Expr.Return,
        ),
        'loc_23A07',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_23A07(): pass

    label('loc_23A07')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0003)"),
            Expr.Return,
        ),
        'loc_23A1B',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_23A1B(): pass

    label('loc_23A1B')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0005)"),
            Expr.Return,
        ),
        'loc_23A2F',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_23A2F(): pass

    label('loc_23A2F')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0007)"),
            Expr.Return,
        ),
        'loc_23A43',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_23A43(): pass

    label('loc_23A43')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x000F)"),
            Expr.Return,
        ),
        'loc_23A57',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_23A57(): pass

    label('loc_23A57')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0023)"),
            Expr.Return,
        ),
        'loc_23A6B',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_23A6B(): pass

    label('loc_23A6B')

    Jump('loc_2390F')

    def _loc_23A70(): pass

    label('loc_23A70')

    Jump('loc_242A8')

    def _loc_23A75(): pass

    label('loc_23A75')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x3092),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    def _loc_23A91(): pass

    label('loc_23A91')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0014)"),
            Expr.Ez,
            (Expr.Eval, "FormationCtrl(0x05, 0x0011)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_23B30',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ティータとアガットをパーティに入れて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    Jump('loc_23A91')

    def _loc_23B30(): pass

    label('loc_23B30')

    Jump('loc_242A8')

    def _loc_23B35(): pass

    label('loc_23B35')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x30D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_02')
    def _loc_23B51(): pass

    label('loc_23B51')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x001F)"),
            Expr.Ez,
            (Expr.Eval, "FormationCtrl(0x05, 0x0015)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_23BED',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'ランディとティオをパーティに入れて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    Jump('loc_23B51')

    def _loc_23BED(): pass

    label('loc_23BED')

    Jump('loc_242A8')

    def _loc_23BF2(): pass

    label('loc_23BF2')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x400D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    Jump('loc_242A8')

    def _loc_23C29(): pass

    label('loc_23C29')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4032),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    def _loc_23C45(): pass

    label('loc_23C45')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x0001)"),
            Expr.Ez,
            (Expr.Eval, "FormationCtrl(0x05, 0x0007)"),
            Expr.Ez,
            Expr.Or,
            (Expr.Eval, "FormationCtrl(0x05, 0x0005)"),
            Expr.Ez,
            Expr.Or,
            (Expr.Eval, "FormationCtrl(0x05, 0x0003)"),
            Expr.Ez,
            Expr.Or,
            (Expr.Eval, "FormationCtrl(0x05, 0x000F)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_23D11',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（デバッグ用）\n',
            'アリサ・フィー・エマ・ラウラ・サラをパーティに入れて下さい。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    Jump('loc_23C45')

    def _loc_23D11(): pass

    label('loc_23D11')

    Jump('loc_242A8')

    def _loc_23D16(): pass

    label('loc_23D16')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4060),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    Jump('loc_242A8')

    def _loc_23D4D(): pass

    label('loc_23D4D')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x4082),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    def _loc_23D69(): pass

    label('loc_23D69')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, 0x000A)"),
            Expr.Ez,
            (Expr.Eval, "FormationCtrl(0x05, 0x000D)"),
            Expr.Ez,
            Expr.Or,
            (Expr.Eval, "FormationCtrl(0x05, 0x000C)"),
            Expr.Ez,
            Expr.Or,
            (Expr.Eval, "FormationCtrl(0x05, 0x0014)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_23E10',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（用于调试）\n',
            '请把尤纳・穆洁・阿尔蒂娜・提坦放入队伍里。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    Jump('loc_23D69')

    def _loc_23E10(): pass

    label('loc_23E10')

    Jump('loc_242A8')

    def _loc_23E15(): pass

    label('loc_23E15')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x40B2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_03')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    Jump('loc_242A8')

    def _loc_23E4C(): pass

    label('loc_23E4C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, '最后的羁绊选择了尤娜', 0x00000001)
    OP_75(0x01, 0x00, '用最终的羁绊选择了阿尔蒂娜', 0x00000002)
    OP_75(0x01, 0x00, '最终的羁绊选择了缪洁', 0x00000003)
    OP_75(0x01, 0x00, '最终的羁绊选择了艾丽莎', 0x00000004)
    OP_75(0x01, 0x00, '最后的羁绊选择了劳拉', 0x00000005)
    OP_75(0x01, 0x00, '用最终的羁绊选择了艾玛', 0x00000006)
    OP_75(0x01, 0x00, '用最终的羁绊选择了菲', 0x00000007)
    OP_75(0x01, 0x00, '最后的羁绊选择了莎拉', 0x00000008)
    OP_75(0x01, 0x00, '最后的羁绊选择了托娃', 0x00000009)
    OP_75(0x01, 0x00, '最终的羁绊选择了阿尔芬', 0x0000000A)
    OP_75(0x01, 0x00, '最后的羁绊选择了艾丽谢', 0x0000000B)
    OP_75(0x02, 0x00, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF9)
    OP_75(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24089',
    )

    SetScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))

    Jump('loc_24160')

    def _loc_24089(): pass

    label('loc_24089')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2409F',
    )

    SetScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))

    Jump('loc_24160')

    def _loc_2409F(): pass

    label('loc_2409F')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_240B5',
    )

    SetScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))

    Jump('loc_24160')

    def _loc_240B5(): pass

    label('loc_240B5')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_240CB',
    )

    SetScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))

    Jump('loc_24160')

    def _loc_240CB(): pass

    label('loc_240CB')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_240E1',
    )

    SetScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))

    Jump('loc_24160')

    def _loc_240E1(): pass

    label('loc_240E1')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_240F7',
    )

    SetScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))

    Jump('loc_24160')

    def _loc_240F7(): pass

    label('loc_240F7')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2410D',
    )

    SetScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))

    Jump('loc_24160')

    def _loc_2410D(): pass

    label('loc_2410D')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24123',
    )

    SetScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))

    Jump('loc_24160')

    def _loc_24123(): pass

    label('loc_24123')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24139',
    )

    SetScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))

    Jump('loc_24160')

    def _loc_24139(): pass

    label('loc_24139')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2414F',
    )

    SetScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))

    Jump('loc_24160')

    def _loc_2414F(): pass

    label('loc_2414F')

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24160',
    )

    SetScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    def _loc_24160(): pass

    label('loc_24160')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B61, 2, 0x5B0A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0B64, 1, 0x5B21)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B65, 4, 0x5B2C)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B67, 3, 0x5B3B)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B68, 6, 0x5B46)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B6A, 7, 0x5B57)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B6C, 3, 0x5B63)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B6F, 0, 0x5B78)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2428D',
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2418E(): pass

    label('loc_2418E')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24288',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xF,
            '（用于调试）\n',
            '羁绊事件：请将在最终场景中选择的角色加入队伍。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    FormationCtrl(0x1C, 0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B61, 2, 0x5B0A)),
            (Expr.Eval, "FormationCtrl(0x05, 0x000A)"),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0B64, 1, 0x5B21)),
            (Expr.Eval, "FormationCtrl(0x05, 0x000C)"),
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B65, 4, 0x5B2C)),
            (Expr.Eval, "FormationCtrl(0x05, 0x000D)"),
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B67, 3, 0x5B3B)),
            (Expr.Eval, "FormationCtrl(0x05, 0x0001)"),
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B68, 6, 0x5B46)),
            (Expr.Eval, "FormationCtrl(0x05, 0x0003)"),
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B6A, 7, 0x5B57)),
            (Expr.Eval, "FormationCtrl(0x05, 0x0005)"),
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B6C, 3, 0x5B63)),
            (Expr.Eval, "FormationCtrl(0x05, 0x0007)"),
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0B6F, 0, 0x5B78)),
            (Expr.Eval, "FormationCtrl(0x05, 0x000F)"),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_24283',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_24283(): pass

    label('loc_24283')

    Jump('loc_2418E')

    def _loc_24288(): pass

    label('loc_24288')

    Jump('loc_242A3')

    def _loc_2428D(): pass

    label('loc_2428D')

    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))
    def _loc_242A3(): pass

    label('loc_242A3')

    Jump('loc_242A8')

    def _loc_242A8(): pass

    label('loc_242A8')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00008640, 'loc_24321'),
        (0x00008641, 'loc_2433D'),
        (0x00008642, 'loc_24359'),
        (0x00008643, 'loc_24375'),
        (0x00008644, 'loc_24391'),
        (0x00008645, 'loc_243AD'),
        (0x00008646, 'loc_243C9'),
        (0x00008647, 'loc_243E5'),
        (0x00008648, 'loc_24401'),
        (0x00008649, 'loc_2441D'),
        (0x0000864A, 'loc_24439'),
        (0x0000864B, 'loc_24455'),
        (0x0000864C, 'loc_24471'),
        (0x0000864D, 'loc_2448D'),
        (-1, 'loc_244A9'),
    )

    def _loc_24321(): pass

    label('loc_24321')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8640, 0x0))

    Jump('loc_244AE')

    def _loc_2433D(): pass

    label('loc_2433D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8641, 0x0))

    Jump('loc_244AE')

    def _loc_24359(): pass

    label('loc_24359')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8642, 0x0))

    Jump('loc_244AE')

    def _loc_24375(): pass

    label('loc_24375')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8643, 0x0))

    Jump('loc_244AE')

    def _loc_24391(): pass

    label('loc_24391')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8644, 0x0))

    Jump('loc_244AE')

    def _loc_243AD(): pass

    label('loc_243AD')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8645, 0x0))

    Jump('loc_244AE')

    def _loc_243C9(): pass

    label('loc_243C9')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8646, 0x0))

    Jump('loc_244AE')

    def _loc_243E5(): pass

    label('loc_243E5')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8647, 0x0))

    Jump('loc_244AE')

    def _loc_24401(): pass

    label('loc_24401')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8648, 0x0))

    Jump('loc_244AE')

    def _loc_2441D(): pass

    label('loc_2441D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x8649, 0x0))

    Jump('loc_244AE')

    def _loc_24439(): pass

    label('loc_24439')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x864A, 0x0))

    Jump('loc_244AE')

    def _loc_24455(): pass

    label('loc_24455')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x864B, 0x0))

    Jump('loc_244AE')

    def _loc_24471(): pass

    label('loc_24471')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x864C, 0x0))

    Jump('loc_244AE')

    def _loc_2448D(): pass

    label('loc_2448D')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x864D, 0x0))

    Jump('loc_244AE')

    def _loc_244A9(): pass

    label('loc_244A9')

    Jump('loc_244AE')

    def _loc_244AE(): pass

    label('loc_244AE')

    Jump('loc_23351')

    def _loc_244B3(): pass

    label('loc_244B3')

    Return()

# id: 0x0093 offset: 0x244B4
@scena.Code('EV_Jump_YR_Fishing')
def EV_Jump_YR_Fishing():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_244BD(): pass

    label('loc_244BD')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24635',
    )

    MenuCmd(0x00, 0x02, 0x0018, 40.0, 0x00000000)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24630',
    )

    MenuCmd(0x01, 0x02, '[▼釣り大会に遭遇する　　　　　　]', 0x0000860B)
    MenuCmd(0x01, 0x02, '[▼ヌシを釣った後のＥＶ　　　　　]', 0x0000860C)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_245AA',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))

    def _loc_245AA(): pass

    label('loc_245AA')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000860B, 'loc_245C3'),
        (0x0000860C, 'loc_245C3'),
        (-1, 'loc_245CE'),
    )

    def _loc_245C3(): pass

    label('loc_245C3')

    ClearScenaFlags(ScenaFlag(0x0BCE, 4, 0x5E74))
    ClearScenaFlags(ScenaFlag(0x0BCF, 1, 0x5E79))

    Jump('loc_245CE')

    def _loc_245CE(): pass

    label('loc_245CE')

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x0000860B, 'loc_245E7'),
        (0x0000860C, 'loc_24603'),
        (-1, 'loc_24622'),
    )

    def _loc_245E7(): pass

    label('loc_245E7')

    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x860B, 0x0))

    Jump('loc_24630')

    def _loc_24603(): pass

    label('loc_24603')

    SetScenaFlags(ScenaFlag(0x0BCE, 4, 0x5E74))
    Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x860C, 0x0))

    Jump('loc_24630')

    def _loc_24622(): pass

    label('loc_24622')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_24630')

    def _loc_24630(): pass

    label('loc_24630')

    Jump('loc_244BD')

    def _loc_24635(): pass

    label('loc_24635')

    Return()

# id: 0x0094 offset: 0x24638
@scena.Code('TK_System_Debug')
def TK_System_Debug():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    PlayBGM(922, 1.0, 0x0000, 0x00000000, 0x00)
    MenuCmd(0x00, 0x00, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '语音测试', 0x00000000)
    MenuCmd(0x01, 0x00, '图片显示测试', 0x00000001)
    MenuCmd(0x01, 0x00, '选项测试', 0x00000005)
    MenuCmd(0x01, 0x00, '文字测试', 0x00000006)
    MenuCmd(0x01, 0x00, '对话框测试', 0x0000000B)
    MenuCmd(0x01, 0x00, '脸部表情测试', 0x0000000C)
    MenuCmd(0x01, 0x00, 'AVG对话测试', 0x0000000D)
    MenuCmd(0x01, 0x00, '消息测试＞', 0x0000000F)
    MenuCmd(0x01, 0x00, '对话模式测试', 0x0000000E)
    MenuCmd(0x01, 0x00, '2D表情测试', 0x00000007)
    MenuCmd(0x01, 0x00, '黑屏开关', 0x00000008)
    MenuCmd(0x01, 0x00, '角色颜色变更测试', 0x00000009)
    MenuCmd(0x01, 0x00, '角色发色变更测试', 0x0000000A)
    MenuCmd(0x01, 0x00, '角色用光源方向变更测试', 0x00000013)
    MenuCmd(0x01, 0x00, '地图环境光变测试', 0x00000014)
    MenuCmd(0x01, 0x00, '地名测试', 0x00000010)
    MenuCmd(0x01, 0x00, '人名测试', 0x00000011)
    MenuCmd(0x01, 0x00, '其它名称测试', 0x00000012)
    MenuCmd(0x01, 0x00, '模糊测试', 0x00000015)
    MenuCmd(0x01, 0x00, '淡入淡出测试', 0x00000016)
    MenuCmd(0x01, 0x00, '画面振动测试', 0x00000018)
    MenuCmd(0x01, 0x00, '帮助菜单测试', 0x0000001A)
    MenuCmd(0x01, 0x00, '通知日志测试', 0x0000001C)
    MenuCmd(0x01, 0x00, '动作菜单测试>', 0x0000001E)
    MenuCmd(0x01, 0x00, '链接级别测试>', 0x0000001F)
    MenuCmd(0x01, 0x00, '好感度测试>', 0x00000020)
    MenuCmd(0x01, 0x00, '日历测试>', 0x00000021)
    MenuCmd(0x01, 0x00, '相机命令测试>', 0x00000022)
    MenuCmd(0x01, 0x00, '脑袋命令测试>（慎用）', 0x00000023)
    MenuCmd(0x01, 0x00, '活动TODO测试>（不知道啥用）', 0x00000024)
    MenuCmd(0x01, 0x00, '搭档振动测试>（也不知道啥用）', 0x00000025)
    MenuCmd(0x01, 0x00, '状态提升测试>', 0x00000026)
    MenuCmd(0x01, 0x00, '章间保存测试>', 0x00000027)
    MenuCmd(0x01, 0x00, 'S技测试>', 0x00000028)
    MenuCmd(0x01, 0x00, '标题测试>', 0x00000029)
    MenuCmd(0x01, 0x00, '队伍/团队编制测试>', 0x0000002A)
    MenuCmd(0x01, 0x00, '跟踪测试（后面队友）', 0x0000002B)
    MenuCmd(0x01, 0x00, 'BGM测试', 0x0000002C)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000000, 'loc_24BB6'),
        (0x00000001, 'loc_24BD5'),
        (0x00000005, 'loc_24BF6'),
        (0x00000006, 'loc_24C19'),
        (0x0000000E, 'loc_24C3D'),
        (0x00000008, 'loc_24C5E'),
        (0x00000009, 'loc_24C7F'),
        (0x0000000A, 'loc_24CA0'),
        (0x00000013, 'loc_24CC2'),
        (0x00000014, 'loc_24CEE'),
        (0x0000000B, 'loc_24D29'),
        (0x0000000C, 'loc_24D47'),
        (0x0000000D, 'loc_24D67'),
        (0x0000000F, 'loc_24D89'),
        (0x00000007, 'loc_24DA9'),
        (0x00000010, 'loc_24DC9'),
        (0x00000011, 'loc_24DFC'),
        (0x00000012, 'loc_24E1B'),
        (0x00000015, 'loc_24E3A'),
        (0x00000016, 'loc_24E5B'),
        (0x00000018, 'loc_24E7C'),
        (0x0000001A, 'loc_24EA0'),
        (0x0000001C, 'loc_24EAC'),
        (0x0000002A, 'loc_24EC6'),
        (0x0000002B, 'loc_24EDF'),
        (0x0000002C, 'loc_24EF5'),
        (0x0000001E, 'loc_24F09'),
        (0x0000001F, 'loc_24F21'),
        (0x00000020, 'loc_24F3B'),
        (0x00000021, 'loc_24F55'),
        (0x00000022, 'loc_24F6E'),
        (0x00000023, 'loc_24F8C'),
        (0x00000024, 'loc_24FA8'),
        (0x00000025, 'loc_24FC3'),
        (0x00000026, 'loc_24FDE'),
        (0x00000027, 'loc_24FF7'),
        (0x00000028, 'loc_25013'),
        (0x00000029, 'loc_2502D'),
        (-1, 'loc_25043'),
    )

    def _loc_24BB6(): pass

    label('loc_24BB6')

    Call(ScriptId.Current, 'TK_System_Debug_AVoice')

    Jump('loc_25043')

    def _loc_24BD5(): pass

    label('loc_24BD5')

    Call(ScriptId.Current, 'TK_System_Debug_Portrait')

    Jump('loc_25043')

    def _loc_24BF6(): pass

    label('loc_24BF6')

    Call(ScriptId.Current, 'TK_System_Debug_ButtonMenu')

    Jump('loc_25043')

    def _loc_24C19(): pass

    label('loc_24C19')

    Call(ScriptId.Current, 'TK_System_Debug_StringsTest')

    Jump('loc_25043')

    def _loc_24C3D(): pass

    label('loc_24C3D')

    Call(ScriptId.Current, 'TK_System_Debug_Bustshot')

    Jump('loc_25043')

    def _loc_24C5E(): pass

    label('loc_24C5E')

    Call(ScriptId.Current, 'TK_System_Debug_Monotone')

    Jump('loc_25043')

    def _loc_24C7F(): pass

    label('loc_24C7F')

    Call(ScriptId.Current, 'TK_System_Debug_ChrColor')

    Jump('loc_25043')

    def _loc_24CA0(): pass

    label('loc_24CA0')

    Call(ScriptId.Current, 'TK_System_Debug_HiarColor')

    Jump('loc_25043')

    def _loc_24CC2(): pass

    label('loc_24CC2')

    OP_6B(0x06, 0x0000, 0x0000, 90.0, 0x00000000, 0x00000000)
    Sleep(1000)

    OP_6B(0x07, 0x0000, 0x0000, 0.0, 0x00000000, 0x00000000)

    Jump('loc_25043')

    def _loc_24CEE(): pass

    label('loc_24CEE')

    OP_9A(0x0004, 0.0, 0.0, 0.0, 0x01F4)
    OP_9A(0x0006, 0.0, 0.0, 0.0, 0x01F4)
    Sleep(1000)

    OP_9A(0x0005, 0.0, 0.0, 0.0, 0x0000)

    Jump('loc_25043')

    def _loc_24D29(): pass

    label('loc_24D29')

    Call(ScriptId.Current, 'TK_System_Debug_popup')

    Jump('loc_25043')

    def _loc_24D47(): pass

    label('loc_24D47')

    Call(ScriptId.Current, 'TK_System_Debug_FaceCmd')

    Jump('loc_25043')

    def _loc_24D67(): pass

    label('loc_24D67')

    Call(ScriptId.Current, 'TK_System_Debug_CutinTest')

    Jump('loc_25043')

    def _loc_24D89(): pass

    label('loc_24D89')

    Call(ScriptId.Current, 'TK_System_Debug_Message')

    Jump('loc_25043')

    def _loc_24DA9(): pass

    label('loc_24DA9')

    Call(ScriptId.Current, 'TK_System_Debug_Emotest')

    Jump('loc_25043')

    def _loc_24DC9(): pass

    label('loc_24DC9')

    OP_5A(0x00, 0x03C0, 0x0384, 'I_PVIS_M1490', 0x0BB8)
    OP_5A(0x01)
    OP_5A(0x00, 0x03C0, 0x0384, 'I_PVIS_M9000', 0x0BB8)
    OP_5A(0x01)

    Jump('loc_25043')

    def _loc_24DFC(): pass

    label('loc_24DFC')

    OP_5A(0x00, 0x04B0, 0x0320, 'I_CVIS4_0025_01', 0x0BB8)
    OP_5A(0x01)

    Jump('loc_25043')

    def _loc_24E1B(): pass

    label('loc_24E1B')

    OP_5A(0x00, 0x04B0, 0x0320, 'I_CVIS4_0025_01', 0x0BB8)
    OP_5A(0x01)

    Jump('loc_25043')

    def _loc_24E3A(): pass

    label('loc_24E3A')

    Call(ScriptId.Current, 'TK_System_Debug_BlurTest')

    Jump('loc_25043')

    def _loc_24E5B(): pass

    label('loc_24E5B')

    Call(ScriptId.Current, 'TK_System_Debug_FadeTest')

    Jump('loc_25043')

    def _loc_24E7C(): pass

    label('loc_24E7C')

    Call(ScriptId.Current, 'TK_System_CameraVibrateTest')

    Jump('loc_25043')

    def _loc_24EA0(): pass

    label('loc_24EA0')

    Sleep(300)

    OP_C2(0x00)
    OP_C2(0x01)

    Jump('loc_25043')

    def _loc_24EAC(): pass

    label('loc_24EAC')

    Call(ScriptId.Current, 'TK_NoticeLog_Test')

    Jump('loc_25043')

    def _loc_24EC6(): pass

    label('loc_24EC6')

    Call(ScriptId.Current, 'TK_PartySel_Test')

    Jump('loc_25043')

    def _loc_24EDF(): pass

    label('loc_24EDF')

    Call(ScriptId.Current, 'TK_Train_Test')

    Jump('loc_25043')

    def _loc_24EF5(): pass

    label('loc_24EF5')

    Call(ScriptId.Current, 'TK_Bgm_Test')

    Jump('loc_25043')

    def _loc_24F09(): pass

    label('loc_24F09')

    Call(ScriptId.Current, 'TK_ActMenu_Test')

    Jump('loc_25043')

    def _loc_24F21(): pass

    label('loc_24F21')

    Call(ScriptId.Current, 'TK_LinkLevel_Test')

    Jump('loc_25043')

    def _loc_24F3B(): pass

    label('loc_24F3B')

    Call(ScriptId.Current, 'TK_LikeLevel_Test')

    Jump('loc_25043')

    def _loc_24F55(): pass

    label('loc_24F55')

    Call(ScriptId.Current, 'TK_Calendar_Test')

    Jump('loc_25043')

    def _loc_24F6E(): pass

    label('loc_24F6E')

    Call(ScriptId.Current, 'TK_CameraCommand_Test')

    Jump('loc_25043')

    def _loc_24F8C(): pass

    label('loc_24F8C')

    Call(ScriptId.Current, 'TK_LookCommand_Test')

    Jump('loc_25043')

    def _loc_24FA8(): pass

    label('loc_24FA8')

    Call(ScriptId.Current, 'TK_ActiveTodo_Test')

    Jump('loc_25043')

    def _loc_24FC3(): pass

    label('loc_24FC3')

    Call(ScriptId.Current, 'TK_VibratePad_Test')

    Jump('loc_25043')

    def _loc_24FDE(): pass

    label('loc_24FDE')

    Call(ScriptId.Current, 'TK_StatusUp_Test')

    Jump('loc_25043')

    def _loc_24FF7(): pass

    label('loc_24FF7')

    Call(ScriptId.Current, 'TK_ChapterSave_Test')

    Jump('loc_25043')

    def _loc_25013(): pass

    label('loc_25013')

    Call(ScriptId.Current, 'TK_GetSCraft_Test')

    Jump('loc_25043')

    def _loc_2502D(): pass

    label('loc_2502D')

    Call(ScriptId.Current, 'TK_Title_Test')

    Jump('loc_25043')

    def _loc_25043(): pass

    label('loc_25043')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))

    Return()

# id: 0x0095 offset: 0x25058
@scena.Code('TK_System_Debug_AVoice')
def TK_System_Debug_AVoice():
    MenuCmd(0x00, 0x00, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '简短的台词', 0x00000000)
    MenuCmd(0x01, 0x00, '长台词', 0x00000001)
    MenuCmd(0x01, 0x00, '全员检查1', 0x00000003)
    MenuCmd(0x01, 0x00, '全员检查2', 0x00000004)
    MenuCmd(0x01, 0x00, '全员检查3', 0x00000005)
    MenuCmd(0x01, 0x00, '全员检查4', 0x00000006)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000000, 'loc_2512A'),
        (0x00000001, 'loc_25137'),
        (0x00000003, 'loc_25144'),
        (0x00000004, 'loc_25154'),
        (0x00000005, 'loc_25164'),
        (0x00000006, 'loc_25174'),
        (-1, 'loc_25184'),
    )

    def _loc_2512A(): pass

    label('loc_2512A')

    OP_74(0x014A, 0x00, 0x00000000)

    Jump('loc_25184')

    def _loc_25137(): pass

    label('loc_25137')

    OP_74(0x015D, 0x00, 0x00000000)

    Jump('loc_25184')

    def _loc_25144(): pass

    label('loc_25144')

    ClearScenaFlags(ScenaFlag(0x0046, 0, 0x230))
    OP_74(0x03DE, 0x00, 0x00000000)

    Jump('loc_25184')

    def _loc_25154(): pass

    label('loc_25154')

    ClearScenaFlags(ScenaFlag(0x0046, 0, 0x230))
    OP_74(0x03DF, 0x00, 0x00000000)

    Jump('loc_25184')

    def _loc_25164(): pass

    label('loc_25164')

    ClearScenaFlags(ScenaFlag(0x0046, 0, 0x230))
    OP_74(0x03E0, 0x00, 0x00000000)

    Jump('loc_25184')

    def _loc_25174(): pass

    label('loc_25174')

    ClearScenaFlags(ScenaFlag(0x0046, 0, 0x230))
    OP_74(0x03E1, 0x00, 0x00000000)

    Jump('loc_25184')

    def _loc_25184(): pass

    label('loc_25184')

    Return()

# id: 0x0096 offset: 0x25188
@scena.Code('TK_System_Debug_Portrait')
def TK_System_Debug_Portrait():
    OP_55(0x00, 0x0000, 0x0000, 0x1000, 0x1000, 0x0000, 0x0000, 0x0000, 0x0000, 0x1000, 0x1000, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_MG08_CARD', '')
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    Sleep(1000)

    OP_62(0x071C, 0x03FC)
    OP_56(0x00, 0x01, 0x00, 0.3, 0.3, 0.0, 0.0, 300.0)
    Sleep(1000)

    OP_62(0x071C, 0x03FC)
    OP_58(0x00)
    OP_55(0x00, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_VIS999', '')
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    Sleep(1000)

    OP_62(0x071C, 0x03FC)
    OP_56(0x00, 0x00, 0x00, 0.0, 0.0, 0.0, 0.0, 0.0)
    OP_56(0x00, 0x00, 0x00, -1800.0, 0.0, 30000.0, 0.0, 0.0)
    OP_57(0x00, 0x03)
    OP_62(0x071C, 0x03FC)
    OP_58(0x00)
    OP_55(0x00, 0x0000, 0x0000, 0x0600, 0x0400, 0x0153, 0x003C, 0x0000, 0x0000, 0x0600, 0x0400, 1.0, 1.0, 1.0, 0.0, 0x01, 0x00, 'I_NOTE_HELP000', '')
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 500.0)
    OP_57(0x00, 0x03)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '手帳ヘルプ画像。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_62(0x058C, 0x0380)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 500.0)
    OP_57(0x00, 0x03)
    OP_58(0x00)
    OP_55(0x00, 0x0000, 0x0000, 0x0400, 0x0400, 0x0000, 0x0000, 0x0000, 0x0000, 0x0400, 0x0400, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_ICONS', 'I_SYSTEM')
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    OP_57(0x00, 0x03)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'I_SYSTEMからI_ICONSを読み込む。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_62(0x071C, 0x03FC)
    OP_58(0x00)
    OP_55(0x00, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x02, 'I_VIS9100', '')
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    Sleep(1000)

    OP_62(0x071C, 0x03FC)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 300.0)
    Sleep(300)

    OP_58(0x00)

    Return()

# id: 0x0097 offset: 0x25434
@scena.Code('TK_System_Debug_ButtonMenu')
def TK_System_Debug_ButtonMenu():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, '智障兽最爱公主', 0x00000001)
    OP_75(0x01, 0x00, '智障兽最爱3C哥', 0x00000002)
    OP_75(0x01, 0x00, '智障兽是自以为是的白痴（嗯？）', 0x00000003)
    OP_75(0x01, 0x00, '智障兽是恶心的家伙（[○･｀Д´･ ○]）', 0x00000004)
    OP_75(0x01, 0x00, '智障兽最爱姐姐的陪伴', 0x00000005)
    OP_75(0x07, 0x00, 0x0003)
    OP_75(0x07, 0x00, 0x0004)
    OP_75(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF7)
    OP_75(0x03, 0x00)

    Return()

# id: 0x0098 offset: 0x25538
@scena.Code('TK_System_Debug_StringsTest')
def TK_System_Debug_StringsTest():
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '#20s尺寸20（相当于16pixel）最爱公主！公主最高！\n',
            '#24s尺寸24（相当于18pixel）最爱公主！公主最高！\n',
            '#28s尺寸28（相当于21pixel）最爱公主！公主最高！\n',
            '#32s尺寸32（相当于24pixel）最爱公主！公主最高！\n',
            '#40s尺寸40（相当于30pixel）最爱公主！公主最高！\n',
            '#48s尺寸48（相当于36pixel）最爱公主！公主最高！\n',
            '#64s尺寸64（相当于48pixel）最爱公主！公主最高！',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '#0C色 ＃0C 最爱3C，3C超温柔\n',
            '#1C色 ＃1C 最爱3C，3C超温柔\n',
            '#2C色 ＃2C 最爱3C，3C超温柔\n',
            '#3C色 ＃3C 最爱3C，3C超温柔\n',
            '#4C色 ＃4C 最爱3C，3C超温柔\n',
            '#5C色 ＃5C 最爱3C，3C超温柔\n',
            '#6C色 ＃6C 最爱3C，3C超温柔\n',
            '#7C色 ＃7C 最爱3C，3C超温柔\n',
            '#8C色 ＃8C 最爱3C，3C超温柔\n',
            '#9C色 ＃9C 最爱3C，3C超温柔',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_27('㌃㌄㌅', 0xFFFF)

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '♥㍻㍼㊥───　───　━━━\n',
            ' ㌃㌄㌅(リィン)｜㌔㌘㌢㌣(ミリアム)｜㌦㌧㌶㍉㍑(アルグレス)',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0C①②③④⑤⑥⑦⑧⑨⑩\n',
            '#1C１２３４５６７８９０\n',
            '#2CⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ\n',
            '#3Cⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ\n',
            '#4C＋－＊・／「」【】『』',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            'abcdefghijklmnopqrstuvwxyz\n',
            'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ\n',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '*/+-\n',
            'AAAAAAACEEEEIIIIDNOOOOO×OU\n',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            'あ【あいう】あ『幻焔計画』\n',
            'あ「あいう」あ\n',
            'あ『あいう』あ',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            'メモリ\n',
            '#6Sメモリ',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '記#2Rメモリ#',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '米国#4Rステイツ#',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '記憶結晶#8Rメモリークオーツ#\n',
            '導力器#6Rオーブメント#',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            'ルビテスト#10Rルビテスト#\n',
            'ルビテスト#10Rルビテスト#\n',
            'ルビテスト#10Rルビテスト#',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '確認可能#6Rルビテスト#\n',
            '記憶結晶#8Rメモリークオーツ#\n',
            '剣──法剣#4Rテンプルソード#\n',
            '剣──法剣#4Rテンプル#',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '《叢雲#4Rむらくも#大社》',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '眼#2Rまなこ#',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            'ふふ、けっこう山間#4Rやまあい#まで',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#160I#161I#191I#174I#164I#166Iアイコンテスト',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#2S#160I#161I#191I#174Iアイコンテスト',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '報告の際にＡＰが規定値に達すると\n',
            'ランクアップし、特典が入手できるため、\n',
            'クエストを達成したら積極的に報告しましょう。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Return()

# id: 0x0099 offset: 0x25E70
@scena.Code('TK_System_Debug_Bustshot')
def TK_System_Debug_Bustshot():
    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    CreateChr(0x03FB, 'C_CHR999', 'アリサ', '', 0x00, 0x00000000, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, 'chr001', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    OP_38(0xF016, 0x00, 0x00, 'AniWait')
    OP_38(0x03FB, 0x00, 0x00, 'AniWait')
    OP_4F(0x00, 0xF016, 30.0, 0xFE3E, 0x0010, 0.0, -0.14)
    OP_4F(0x00, 0x03FB, -30.0, 0x01C2, 0x0010, 0.0, -0.13)
    OP_4F(0x03, 0xF016, 1.0, 1.0, 1.0, 0.0, 0x0000, 0x03)
    OP_4F(0x03, 0x03FB, 1.0, 1.0, 1.0, 0.0, 0x0000, 0x03)
    OP_4F(0x03, 0xF016, 1.0, 1.0, 1.0, 1.0, 0x03E8, 0x03)
    OP_4F(0x03, 0x03FB, 1.0, 1.0, 1.0, 1.0, 0x03E8, 0x03)
    Sleep(1000)

    OP_23(0x01, 0xFFFF, 0x02EE, 0x00, 0x0A)
    OP_23(0x02, 0x0384, 0x0104)
    OP_43(0x0A, 0x012C)
    OP_43(0x0C, 0x0000)
    SetChrFace(0x04, 0x03FB, '#E_I#M_0')

    ChrTalk(
        0x03FB,
        0x00000000,
        (
            '#K#0T──時坂君、私たちは\n',
            '“ただの”クラスメイトよ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#E[1]#M_0貴方に何を聞かれても、\n',
            '私が“あの夜”について\n',
            '答えることは絶対ない……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#E_0#M_0それは分かっているんでしょう？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    SetChrFace(0x04, 0xF016, '#E_F#M_9')

    ChrTalk(
        0xF016,
        0x00000001,
        (
            '#K#0T……ああ、\n',
            'ま、そうなんだろうな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#E[1]#M_0それについてはまだ\n',
            '納得したわけじゃねぇが……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#E_8#M_9──それ以前に、ちゃんと\n',
            '礼を言ってなかったと思ってな。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_4F(0x03, 0xF016, 1.0, 1.0, 1.0, 0.0, 0x03E8, 0x03)
    OP_4F(0x03, 0x03FB, 1.0, 1.0, 1.0, 0.0, 0x03E8, 0x03)
    Sleep(1000)

    OP_43(0x0B, 0x012C)
    OP_43(0x0C, 0x0000)
    OP_4F(0x01, 0xF016)
    OP_4F(0x01, 0x03FB)
    ReleaseChr(0x03FB)
    OP_21(0x00)

    Return()

# id: 0x009A offset: 0x261E0
@scena.Code('TK_System_Debug_Monotone')
def TK_System_Debug_Monotone():
    If(
        (
            (Expr.Eval, "OP_A8(0x80000000)"),
            Expr.Return,
        ),
        'loc_26262',
    )

    DebugLog(0x02, (0xDD, 'monotone: off'))
    OP_84(0x00, 0.5, 0.5, 0.5, 0.0)
    OP_14(0x80000000)
    OP_84(0x03, 0xF000, '', 0x01)
    OP_84(0x03, 0xF001, '', 0x01)
    OP_84(0x03, 0xF002, '', 0x01)
    SetChrFace(0x04, 0xF016, '#E_0#M_0')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#Kカラーフェイスです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_262C4')

    def _loc_26262(): pass

    label('loc_26262')

    DebugLog(0x02, (0xDD, 'monotone: on'))
    OP_13(0x80000000)
    OP_84(0x03, 0xF000, '', 0x02)
    OP_84(0x03, 0xF001, '', 0x02)
    OP_84(0x03, 0xF002, '', 0x02)
    SetChrFace(0x04, 0xF016, '#E_0#M_0')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            0x13,
            '#Kモノクロフェイスです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    def _loc_262C4(): pass

    label('loc_262C4')

    Return()

# id: 0x009B offset: 0x262C8
@scena.Code('TK_System_Debug_ChrColor')
def TK_System_Debug_ChrColor():
    If(
        (
            (Expr.GetChrWork, 0xF016, 0x10),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26305',
    )

    ChrSetRGBA(0xF016, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    OP_4C(0xF016, 0.0, 0.0, 0.0, 0x03E8, 0x03)

    Jump('loc_2632D')

    def _loc_26305(): pass

    label('loc_26305')

    ChrSetRGBA(0xF016, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    OP_4C(0xF016, 1.0, 1.0, 1.0, 0x03E8, 0x03)

    def _loc_2632D(): pass

    label('loc_2632D')

    Return()

# id: 0x009C offset: 0x26330
@scena.Code('TK_System_Debug_HiarColor')
def TK_System_Debug_HiarColor():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_26339(): pass

    label('loc_26339')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2653A',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'リィン：髪の毛色：初期     change_face_asset() ', 0x00000064)
    MenuCmd(0x01, 0x01, 'リィン：髪の毛色：金       change_face_asset() ', 0x00000065)
    MenuCmd(0x01, 0x01, 'ユウナ：髪の毛色：初期     set_equip() ', 0x0000006E)
    MenuCmd(0x01, 0x01, 'ユウナ：髪の毛色：金髪     set_equip() ', 0x0000006F)
    MenuCmd(0x01, 0x01, 'リィン：衣装変更           change_skin() ', 0x00000070)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000064, 'loc_264CE'),
        (0x00000065, 'loc_264D9'),
        (0x0000006E, 'loc_264F1'),
        (0x0000006F, 'loc_264FB'),
        (0x00000070, 'loc_26510'),
        (-1, 'loc_26527'),
    )

    def _loc_264CE(): pass

    label('loc_264CE')

    AnimeClipCtrl(0x0B, ChrTable['黎恩'], '', '')

    Jump('loc_26535')

    def _loc_264D9(): pass

    label('loc_264D9')

    AnimeClipCtrl(0x0B, ChrTable['黎恩'], 'FC_CHR000_C02', '')

    Jump('loc_26535')

    def _loc_264F1(): pass

    label('loc_264F1')

    OP_70(0x01, 0x000A, 0x09)

    Jump('loc_26535')

    def _loc_264FB(): pass

    label('loc_264FB')

    AddItem(0x00, 0x0444, 1)
    OP_70(0x00, 0x000A, 0x0444, 0xFF, 0x00)

    Jump('loc_26535')

    def _loc_26510(): pass

    label('loc_26510')

    AnimeClipChangeSkin(ChrTable['黎恩'], 'C_CHR000_C01')

    Jump('loc_26535')

    def _loc_26527(): pass

    label('loc_26527')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_26535')

    def _loc_26535(): pass

    label('loc_26535')

    Jump('loc_26339')

    def _loc_2653A(): pass

    label('loc_2653A')

    Return()

# id: 0x009D offset: 0x2653C
@scena.Code('TK_System_Debug_Message')
def TK_System_Debug_Message():
    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2655F(): pass

    label('loc_2655F')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_269DE',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '窗口大小可变', 0x00000064)
    MenuCmd(0x01, 0x00, '窗口大小固定', 0x00000065)
    MenuCmd(0x01, 0x00, '窗口位置固定', 0x00000066)
    MenuCmd(0x01, 0x00, '窗口位置变化', 0x00000067)
    MenuCmd(0x01, 0x00, '消息条', 0x00000068)
    MenuCmd(0x01, 0x00, '信息框', 0x00000069)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x00, 0xF7)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000064, 'loc_26656'),
        (0x00000065, 'loc_266E4'),
        (0x00000066, 'loc_267F1'),
        (0x00000067, 'loc_26845'),
        (0x00000068, 'loc_268B0'),
        (0x00000069, 'loc_26938'),
        (-1, 'loc_269CB'),
    )

    def _loc_26656(): pass

    label('loc_26656')

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '通常は\n',
            '#1CPAUSE#0Cごとにサイズが変化。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '①②③④⑤⑥⑦⑧⑨⑩①②③④⑤⑥⑦⑧⑨⑩①②③',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_269D9')

    def _loc_266E4(): pass

    label('loc_266E4')

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000001,
        (
            '#1CPW_FIXSIZE#0Cをつけると\n',
            '#1CPAUSE#0Cがあるpopupでもウィンドウサイズ固定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1CPAUSE#0C後のメッセージのほうが\n',
            '文字数多い場合にも対応。\n',
            '①②③④⑤⑥⑦⑧⑨⑩①②③④⑤⑥⑦⑧⑨⑩①②③',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_269D9')

    def _loc_267F1(): pass

    label('loc_267F1')

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '通常は\n',
            '初回のみウィンドウの座標計算を行う。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_269D9')

    def _loc_26845(): pass

    label('loc_26845')

    SetChrFace(0x04, 0xF016, 'M_0')

    ChrTalk(
        0xF016,
        0x00000002,
        (
            '#K#1CPW_UPDATEPOS#0Cをつけると\n',
            '常にウィンドウの座標計算を行う。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_269D9')

    def _loc_268B0(): pass

    label('loc_268B0')

    SetScenaFlags(ScenaFlag(0x0064, 6, 0x326))
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '縁取りがあるよ。\n',
            '解除し忘れると大変なことに！\n',
            'ちゃんとスキップ対策もしてね。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_269D9')

    def _loc_26938(): pass

    label('loc_26938')

    ClearScenaFlags(ScenaFlag(0x0064, 6, 0x326))
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '縁取り消えたよ。\n',
            'GF4_FUCHIDORI_MODEをresetするだけだよ。\n',
            '忘れずにスキップ対策しておいてね。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_269D9')

    def _loc_269CB(): pass

    label('loc_269CB')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_269D9')

    def _loc_269D9(): pass

    label('loc_269D9')

    Jump('loc_2655F')

    def _loc_269DE(): pass

    label('loc_269DE')

    OP_21(0x00)

    Return()

# id: 0x009E offset: 0x269E4
@scena.Code('TK_System_Debug_popup')
def TK_System_Debug_popup():
    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_45(0xF016, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xF016, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xF016, 0xFFFF, 0x0000)
    OP_23(0x01, 0x00F0, 0x020D, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_1P1()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x0276, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_1P2()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x0186, 0x01A4, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_1P3()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x01A4, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_1P4()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x00F0, 0x020D, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_2P1()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x0276, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_2P2()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x0186, 0x01A4, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_2P3()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x01A4, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_2P4()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x00F0, 0x0357, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_3P1()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x0357, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_3P2()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x0186, 0x03C0, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_3P3()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x03C0, 0x01, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_3P4()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x00F0, 0x0357, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_4P1()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x0357, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_4P2()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x0186, 0x03C0, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_4P3()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0x005A, 0x03C0, 0x02, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_4P4()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x00D2, 0x05, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C1L()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x014A, 0x05, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C2L()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x0276, 0x05, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C3L()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x02EE, 0x05, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C4L()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x00D2, 0x06, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C1R()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x014A, 0x06, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C2R()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x0276, 0x06, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C3R()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x02EE, 0x06, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K POPUPPOS_C4R()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_23(0x01, 0xFFFF, 0x02EE, 0x06, 0x0A)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K#F POPUPPOS_C4R()',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_21(0x00)

    Return()

# id: 0x009F offset: 0x26E1C
@scena.Code('TK_System_Debug_FaceCmd')
def TK_System_Debug_FaceCmd():
    SetChrFace(0x04, 0xFFFE, '#E_0#M_0#B_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#K＃E_0＃M_0＃B_0',
            TxtCtl.Enter,
            '#B[012345678]＃B[012345678]',
            TxtCtl.Enter,
            '#M[1,111,2,222,3,333]＃M[1,111,2,222,3,333]',
            TxtCtl.Enter,
            '#E[1,111,2,222,3,333,4,444]',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    SetChrFace(0x04, 0xFFFE, '#E_0#M_0#B_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#E[0]#e[5]#B[0](＃E[1]＃e[5]＃B[0])',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    SetScenaFlags(ScenaFlag(0x0066, 2, 0x332))
    SetChrFace(0x04, 0xF016, '#E_0#M_0#B_0')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K普通の角度',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_63(0xFFFF, 0x01)
    SetChrFace(0x04, 0xF016, '#E_0#M_0#B_0')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K#F正面ぽい',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_63(0xFFFF, 0x01)
    SetChrFace(0x04, 0xF016, '#E_0#M_0#B_0')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#K#2F角度強め',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Return()

# id: 0x00A0 offset: 0x26F84
@scena.Code('TK_System_Debug_CutinTest')
def TK_System_Debug_CutinTest():
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR033', '鋼のアリアンロード', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    OP_BC(0x01, 0x0000, (0xFF, 0x6E, 0x0), 0x00000000, 0.0, 0.03, 1.0, 1.0, 1.0, 1.0, 0.0, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x3F800000, 0x0000, 0x0003)
    OP_BC(0x01, 0x0000, (0xFF, 0x6E, 0x0), 0x00000001, 0.35, 0.03, 1.0, 1.0, 1.0, 1.0, 0.0, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x3F800000, 0x0000, 0x0003)
    OP_BC(0x01, 0x0000, (0xFF, 0x6E, 0x0), 0x00000002, 0.0, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x3F800000, 0x0000, 0x0003)
    OP_BC(0x01, 0x0000, (0xFF, 0x6E, 0x0), 0x00000003, 0.25, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x3F800000, 0x0000, 0x0003)
    OP_BC(0x09, 0x0000, (0xFF, 0x6E, 0x0), 0.0, -0.08, -12.0, 3.0, 0.0, 0.9, 0x0000, 3)
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    OP_BC(0x02, 0x0000, (0xFF, 0x6E, 0x0), 0x00)
    AttachEquip(0x006E, 'M_V4040', 'up_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x006E, '', 'up_point', 0x01)
    OP_76(ChrTable['剛毅艾奈絲'], 'up_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AnimeClipLoadMultiple(ChrTable['剛毅艾奈絲'], 0x00, 'AniEv45005', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEv45005', -1.0, 1.0, 0x00000000)
    OP_BC(0x09, 0x0000, (0xFF, 0x6E, 0x0), 0.0, -0.08, -12.0, -2.0, 0.0, 0.9, 0x0000, 3)
    OP_BC(0x04, 0x0000, (0xFF, 0x6E, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0x6E, 0x0))
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    OP_43(0x06, 0x012C)
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E[1]#M_0#B_0')

    ChrTalk(
        ChrTable['剛毅艾奈絲'],
        0x00000000,
        (
            '#K……フフ、カットインとは。\n',
            'ぶざまだな。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_44(0x006E, 0x01, 0.1, 0x0004, 0.0)
    Sleep(1000)

    OP_43(0x6A, 0x012C)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_43(0x6B, 0x012C)
    OP_BC(0x05, 0x0000, (0xFF, 0x6E, 0x0), 0x0190, 0x0003)
    Sleep(500)

    OP_BC(0x03, 0x0000, (0xFF, 0xFFFF, 0x0))
    ReleaseChr(ChrTable['剛毅艾奈絲'])

    Return()

# id: 0x00A1 offset: 0x272D8
@scena.Code('TK_System_Debug_Emotest')
def TK_System_Debug_Emotest():
    CameraCtrl(0x08, 0x00, 0x0000)
    CameraRotate(0x03, 0.0, 0.0, 0.0, 0, 0x01)
    CameraCtrl(0x12, 0x0004)
    CameraCtrl(0x12, 0x0010)
    CameraCtrl(0x12, 0x0040)
    ChrSetPhysicsFlags(0xFFFE, 0x00004000)

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2730C(): pass

    label('loc_2730C')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27746',
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '通常动作', 0x00000000)
    MenuCmd(0x01, 0x01, '胸围投影向右', 0x00000001)
    MenuCmd(0x01, 0x01, '胸围投影向左', 0x00000002)
    MenuCmd(0x01, 0x01, '在窗口中', 0x00000003)
    MenuCmd(0x01, 0x01, '身体向后', 0x0000000A)
    MenuCmd(0x01, 0x01, '身体向右', 0x0000000B)
    MenuCmd(0x01, 0x01, '身体向左转', 0x0000000C)
    MenuCmd(0x01, 0x01, '面向身体正面', 0x0000000D)
    MenuCmd(0x01, 0x01, '头向右', 0x00000014)
    MenuCmd(0x01, 0x01, '头朝左', 0x00000015)
    MenuCmd(0x01, 0x01, '头朝上向左', 0x00000016)
    MenuCmd(0x01, 0x01, '面向正前方', 0x00000017)
    MenuCmd(0x01, 0x01, '面对面', 0x00000018)
    MenuCmd(0x02, 0x01, 0x01, 0x0010, 0x0040, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27479',
    )

    Call(ScriptId.Current, 'SUB_EmotionTest')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2773D')

    def _loc_27479(): pass

    label('loc_27479')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_274BC',
    )

    OP_4F(0x00, 0xFFFE, 30.0, 0x00FA, 0x0010, 0.0, -0.1)
    Call(ScriptId.Current, 'SUB_EmotionTest')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2773D')

    def _loc_274BC(): pass

    label('loc_274BC')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_274FF',
    )

    OP_4F(0x00, 0xFFFE, -30.0, 0x00FA, 0x0010, 0.0, -0.1)
    Call(ScriptId.Current, 'SUB_EmotionTest')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2773D')

    def _loc_274FF(): pass

    label('loc_274FF')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x18),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_275BA',
    )

    Call(ScriptId.System, 'FC_BustShotCreateKizuna', (0xFF, 0x0, 0x0), (0xFF, 0xFFFE, 0x0))
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    Call(ScriptId.System, 'FC_BustShotShow', (0xFF, 0x0, 0x0), (0xFF, 0xFFFE, 0x0), (0xFF, 0xFFFF, 0x0), (0xFF, 0xFFFF, 0x0), (0xFF, 0xFFFF, 0x0), (0xFF, 0xFFFF, 0x0), (0xFF, 0xFFFF, 0x0), (0xFF, 0xFFFF, 0x0))
    Call(ScriptId.Current, 'SUB_EmotionTest')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_BC(0x06, 0x0000, (0xFF, 0xFFFF, 0x0))
    OP_BC(0x03, 0x0000, (0xFF, 0xFFFF, 0x0))

    Jump('loc_2773D')

    def _loc_275BA(): pass

    label('loc_275BA')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27618',
    )

    OP_44(0xFFFE, 0x00, 0.1, 0x0004, 0.0)
    SetChrFace(0x04, 0xFFFE, '#E_0#M_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kウィンドウテストですよ。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_2773D')

    def _loc_27618(): pass

    label('loc_27618')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2763F',
    )

    ChrClearPhysicsFlags(0xFFFE, 0x00002000)
    OP_3D(0xFFFE, 180.0, 10.0, 0x00)

    Jump('loc_2773D')

    def _loc_2763F(): pass

    label('loc_2763F')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2765E',
    )

    OP_3D(0xFFFE, -90.0, 10.0, 0x00)

    Jump('loc_2773D')

    def _loc_2765E(): pass

    label('loc_2765E')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2767D',
    )

    OP_3D(0xFFFE, 90.0, 10.0, 0x00)

    Jump('loc_2773D')

    def _loc_2767D(): pass

    label('loc_2767D')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2769C',
    )

    OP_3D(0xFFFE, 0.0, 10.0, 0x00)

    Jump('loc_2773D')

    def _loc_2769C(): pass

    label('loc_2769C')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x14),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_276C2',
    )

    OP_45(0xFFFE, -45.0, 0.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2773D')

    def _loc_276C2(): pass

    label('loc_276C2')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x15),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_276E8',
    )

    OP_45(0xFFFE, 45.0, 0.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2773D')

    def _loc_276E8(): pass

    label('loc_276E8')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x16),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2770E',
    )

    OP_45(0xFFFE, 0.0, 45.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2773D')

    def _loc_2770E(): pass

    label('loc_2770E')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x17),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27734',
    )

    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2773D')

    def _loc_27734(): pass

    label('loc_27734')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2773D(): pass

    label('loc_2773D')

    OP_4F(0x01, 0xFFFE)

    Jump('loc_2730C')

    def _loc_27746(): pass

    label('loc_27746')

    MenuCmd(0x03, 0x01)
    ChrClearPhysicsFlags(0xFFFE, 0x00004000)

    Return()

# id: 0x00A2 offset: 0x27754
@scena.Code('SUB_EmotionTest')
def SUB_EmotionTest():
    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2775D(): pass

    label('loc_2775D')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28608',
    )

    MenuCmd(0x00, 0x00, 0x0014, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '？', 0x00000001)
    MenuCmd(0x01, 0x00, '！', 0x00000002)
    MenuCmd(0x01, 0x00, '！？', 0x00000003)
    MenuCmd(0x01, 0x00, '！！', 0x00000004)
    MenuCmd(0x01, 0x00, '♪（心情）', 0x00000005)
    MenuCmd(0x01, 0x00, 'LOVE', 0x00000006)
    MenuCmd(0x01, 0x00, '生气', 0x00000007)
    MenuCmd(0x01, 0x00, '紊乱', 0x00000008)
    MenuCmd(0x01, 0x00, '冷汗', 0x00000009)
    MenuCmd(0x01, 0x00, '害怕', 0x0000000A)
    MenuCmd(0x01, 0x00, '・・・（循环）', 0x0000000B)
    MenuCmd(0x01, 0x00, '・・・', 0x0000000C)
    MenuCmd(0x01, 0x00, 'ZZZ（循环）', 0x0000000D)
    MenuCmd(0x01, 0x00, '灵光一闪', 0x0000000E)
    MenuCmd(0x01, 0x00, '起哄', 0x0000000F)
    MenuCmd(0x01, 0x00, 'ＰＡ', 0x00000010)
    MenuCmd(0x01, 0x00, '汗', 0x00000011)
    MenuCmd(0x01, 0x00, '汗水（循环）', 0x00000012)
    MenuCmd(0x01, 0x00, '混乱（循环）', 0x00000013)
    MenuCmd(0x01, 0x00, '眩晕（循环）', 0x00000014)
    MenuCmd(0x01, 0x00, '闪闪发光', 0x00000015)
    MenuCmd(0x01, 0x00, '惊讶', 0x00000016)
    MenuCmd(0x01, 0x00, '批量表情（连发）', 0x00000017)
    MenuCmd(0x02, 0x00, 0x01, 0x0020, 0x0064, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000001, 'loc_279E3'),
        (0x00000002, 'loc_279F6'),
        (0x00000003, 'loc_27A09'),
        (0x00000004, 'loc_27A1C'),
        (0x00000005, 'loc_27A2F'),
        (0x00000006, 'loc_27A42'),
        (0x00000007, 'loc_27A55'),
        (0x00000008, 'loc_27A68'),
        (0x00000009, 'loc_27A7B'),
        (0x0000000A, 'loc_27A8E'),
        (0x0000000B, 'loc_27AA1'),
        (0x0000000C, 'loc_27AB4'),
        (0x0000000D, 'loc_27AC7'),
        (0x0000000E, 'loc_27ADA'),
        (0x0000000F, 'loc_27AED'),
        (0x00000010, 'loc_27B00'),
        (0x00000011, 'loc_27B13'),
        (0x00000012, 'loc_27B26'),
        (0x00000013, 'loc_27B39'),
        (0x00000014, 'loc_27B4C'),
        (0x00000015, 'loc_27B5F'),
        (0x00000016, 'loc_27B72'),
        (0x00000017, 'loc_27B85'),
        (-1, 'loc_285FA'),
    )

    def _loc_279E3(): pass

    label('loc_279E3')

    OP_44(0xFFFE, 0x00, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_279F6(): pass

    label('loc_279F6')

    OP_44(0xFFFE, 0x01, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A09(): pass

    label('loc_27A09')

    OP_44(0xFFFE, 0x15, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A1C(): pass

    label('loc_27A1C')

    OP_44(0xFFFE, 0x11, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A2F(): pass

    label('loc_27A2F')

    OP_44(0xFFFE, 0x02, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A42(): pass

    label('loc_27A42')

    OP_44(0xFFFE, 0x03, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A55(): pass

    label('loc_27A55')

    OP_44(0xFFFE, 0x05, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A68(): pass

    label('loc_27A68')

    OP_44(0xFFFE, 0x06, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A7B(): pass

    label('loc_27A7B')

    OP_44(0xFFFE, 0x07, 0.0, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27A8E(): pass

    label('loc_27A8E')

    OP_44(0xFFFE, 0x08, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27AA1(): pass

    label('loc_27AA1')

    OP_44(0xFFFE, 0x09, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27AB4(): pass

    label('loc_27AB4')

    OP_44(0xFFFE, 0x0A, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27AC7(): pass

    label('loc_27AC7')

    OP_44(0xFFFE, 0x0B, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27ADA(): pass

    label('loc_27ADA')

    OP_44(0xFFFE, 0x0C, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27AED(): pass

    label('loc_27AED')

    OP_44(0xFFFE, 0x0D, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27B00(): pass

    label('loc_27B00')

    OP_44(0xFFFE, 0x0E, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27B13(): pass

    label('loc_27B13')

    OP_44(0xFFFE, 0x0F, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27B26(): pass

    label('loc_27B26')

    OP_44(0xFFFE, 0x10, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27B39(): pass

    label('loc_27B39')

    OP_44(0xFFFE, 0x12, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27B4C(): pass

    label('loc_27B4C')

    OP_44(0xFFFE, 0x13, 0.15, 0x0408, 0.0)

    Jump('loc_28603')

    def _loc_27B5F(): pass

    label('loc_27B5F')

    OP_44(0xFFFE, 0x14, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27B72(): pass

    label('loc_27B72')

    OP_44(0xFFFE, 0x16, 0.15, 0x0400, 0.0)

    Jump('loc_28603')

    def _loc_27B85(): pass

    label('loc_27B85')

    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)

    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)

    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)

    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)

    SetChrPos(ChrTable['黎恩'], -2.35, 0.0, 0.12, 352.7)
    SetChrPos(ChrTable['悠娜'], -1.72, 0.0, 0.21, 355.2)
    SetChrPos(ChrTable['庫爾特'], -1.15, 0.0, 0.14, 10.6)
    SetChrPos(ChrTable['亞爾緹娜'], -0.63, 0.0, 0.08, 2.4)
    OP_44(0xF000, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27C56',
    )

    OP_44(0xF001, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27C56(): pass

    label('loc_27C56')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27C76',
    )

    OP_44(0xF002, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27C76(): pass

    label('loc_27C76')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27C96',
    )

    OP_44(0xF003, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27C96(): pass

    label('loc_27C96')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27CB6',
    )

    OP_44(0xF004, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27CB6(): pass

    label('loc_27CB6')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x5),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27CD6',
    )

    OP_44(0xF005, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27CD6(): pass

    label('loc_27CD6')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x6),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27CF6',
    )

    OP_44(0xF006, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27CF6(): pass

    label('loc_27CF6')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x7),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27D16',
    )

    OP_44(0xF007, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27D16(): pass

    label('loc_27D16')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27D36',
    )

    OP_44(0xF008, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27D36(): pass

    label('loc_27D36')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x9),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27D56',
    )

    OP_44(0xF009, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27D56(): pass

    label('loc_27D56')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27D76',
    )

    OP_44(0xF00A, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27D76(): pass

    label('loc_27D76')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xB),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27D96',
    )

    OP_44(0xF00B, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27D96(): pass

    label('loc_27D96')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xC),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27DB6',
    )

    OP_44(0xF00C, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27DB6(): pass

    label('loc_27DB6')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xD),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27DD6',
    )

    OP_44(0xF00D, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27DD6(): pass

    label('loc_27DD6')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xE),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27DF6',
    )

    OP_44(0xF00E, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27DF6(): pass

    label('loc_27DF6')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xF),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27E16',
    )

    OP_44(0xF00F, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27E16(): pass

    label('loc_27E16')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x10),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27E36',
    )

    OP_44(0xF010, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27E36(): pass

    label('loc_27E36')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x11),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27E56',
    )

    OP_44(0xF011, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27E56(): pass

    label('loc_27E56')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x12),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27E76',
    )

    OP_44(0xF012, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27E76(): pass

    label('loc_27E76')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x13),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27E96',
    )

    OP_44(0xF013, 0x01, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27E96(): pass

    label('loc_27E96')

    Sleep(1000)

    OP_44(0xF000, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27ECA',
    )

    OP_44(0xF001, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27ECA(): pass

    label('loc_27ECA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27EEA',
    )

    OP_44(0xF002, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27EEA(): pass

    label('loc_27EEA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27F0A',
    )

    OP_44(0xF003, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27F0A(): pass

    label('loc_27F0A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27F2A',
    )

    OP_44(0xF004, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27F2A(): pass

    label('loc_27F2A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x5),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27F4A',
    )

    OP_44(0xF005, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27F4A(): pass

    label('loc_27F4A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x6),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27F6A',
    )

    OP_44(0xF006, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27F6A(): pass

    label('loc_27F6A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x7),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27F8A',
    )

    OP_44(0xF007, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27F8A(): pass

    label('loc_27F8A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27FAA',
    )

    OP_44(0xF008, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27FAA(): pass

    label('loc_27FAA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x9),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27FCA',
    )

    OP_44(0xF009, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27FCA(): pass

    label('loc_27FCA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27FEA',
    )

    OP_44(0xF00A, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_27FEA(): pass

    label('loc_27FEA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xB),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2800A',
    )

    OP_44(0xF00B, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2800A(): pass

    label('loc_2800A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xC),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2802A',
    )

    OP_44(0xF00C, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2802A(): pass

    label('loc_2802A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xD),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2804A',
    )

    OP_44(0xF00D, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2804A(): pass

    label('loc_2804A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xE),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2806A',
    )

    OP_44(0xF00E, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2806A(): pass

    label('loc_2806A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xF),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2808A',
    )

    OP_44(0xF00F, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2808A(): pass

    label('loc_2808A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x10),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_280AA',
    )

    OP_44(0xF010, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_280AA(): pass

    label('loc_280AA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x11),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_280CA',
    )

    OP_44(0xF011, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_280CA(): pass

    label('loc_280CA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x12),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_280EA',
    )

    OP_44(0xF012, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_280EA(): pass

    label('loc_280EA')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x13),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2810A',
    )

    OP_44(0xF013, 0x00, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2810A(): pass

    label('loc_2810A')

    Sleep(1000)

    OP_44(0xF000, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2813E',
    )

    OP_44(0xF001, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2813E(): pass

    label('loc_2813E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2815E',
    )

    OP_44(0xF002, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2815E(): pass

    label('loc_2815E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2817E',
    )

    OP_44(0xF003, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2817E(): pass

    label('loc_2817E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2819E',
    )

    OP_44(0xF004, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2819E(): pass

    label('loc_2819E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x5),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_281BE',
    )

    OP_44(0xF005, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_281BE(): pass

    label('loc_281BE')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x6),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_281DE',
    )

    OP_44(0xF006, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_281DE(): pass

    label('loc_281DE')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x7),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_281FE',
    )

    OP_44(0xF007, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_281FE(): pass

    label('loc_281FE')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2821E',
    )

    OP_44(0xF008, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2821E(): pass

    label('loc_2821E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x9),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2823E',
    )

    OP_44(0xF009, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2823E(): pass

    label('loc_2823E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2825E',
    )

    OP_44(0xF00A, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2825E(): pass

    label('loc_2825E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xB),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2827E',
    )

    OP_44(0xF00B, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2827E(): pass

    label('loc_2827E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xC),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2829E',
    )

    OP_44(0xF00C, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2829E(): pass

    label('loc_2829E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xD),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_282BE',
    )

    OP_44(0xF00D, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_282BE(): pass

    label('loc_282BE')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xE),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_282DE',
    )

    OP_44(0xF00E, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_282DE(): pass

    label('loc_282DE')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xF),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_282FE',
    )

    OP_44(0xF00F, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_282FE(): pass

    label('loc_282FE')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x10),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2831E',
    )

    OP_44(0xF010, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2831E(): pass

    label('loc_2831E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x11),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2833E',
    )

    OP_44(0xF011, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2833E(): pass

    label('loc_2833E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x12),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2835E',
    )

    OP_44(0xF012, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2835E(): pass

    label('loc_2835E')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x13),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2837E',
    )

    OP_44(0xF013, 0x02, 0.15, 0x0400, 0.0)
    Sleep(50)

    def _loc_2837E(): pass

    label('loc_2837E')

    Sleep(1000)

    OP_44(0xF000, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_283B2',
    )

    OP_44(0xF001, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_283B2(): pass

    label('loc_283B2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_283D2',
    )

    OP_44(0xF002, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_283D2(): pass

    label('loc_283D2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_283F2',
    )

    OP_44(0xF003, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_283F2(): pass

    label('loc_283F2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28412',
    )

    OP_44(0xF004, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28412(): pass

    label('loc_28412')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x5),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28432',
    )

    OP_44(0xF005, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28432(): pass

    label('loc_28432')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x6),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28452',
    )

    OP_44(0xF006, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28452(): pass

    label('loc_28452')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x7),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28472',
    )

    OP_44(0xF007, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28472(): pass

    label('loc_28472')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28492',
    )

    OP_44(0xF008, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28492(): pass

    label('loc_28492')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x9),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_284B2',
    )

    OP_44(0xF009, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_284B2(): pass

    label('loc_284B2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_284D2',
    )

    OP_44(0xF00A, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_284D2(): pass

    label('loc_284D2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xB),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_284F2',
    )

    OP_44(0xF00B, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_284F2(): pass

    label('loc_284F2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xC),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28512',
    )

    OP_44(0xF00C, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28512(): pass

    label('loc_28512')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xD),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28532',
    )

    OP_44(0xF00D, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28532(): pass

    label('loc_28532')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xE),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28552',
    )

    OP_44(0xF00E, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28552(): pass

    label('loc_28552')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0xF),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28572',
    )

    OP_44(0xF00F, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28572(): pass

    label('loc_28572')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x10),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28592',
    )

    OP_44(0xF010, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_28592(): pass

    label('loc_28592')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x11),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_285B2',
    )

    OP_44(0xF011, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_285B2(): pass

    label('loc_285B2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x12),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_285D2',
    )

    OP_44(0xF012, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_285D2(): pass

    label('loc_285D2')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x10)"),
            (Expr.PushLong, 0x13),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_285F2',
    )

    OP_44(0xF013, 0x07, 0.0, 0x0400, 0.0)
    Sleep(50)

    def _loc_285F2(): pass

    label('loc_285F2')

    Sleep(1000)

    Jump('loc_28603')

    def _loc_285FA(): pass

    label('loc_285FA')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28603(): pass

    label('loc_28603')

    Jump('loc_2775D')

    def _loc_28608(): pass

    label('loc_28608')

    OP_44(0xFFFE, 0xFF, 0.0, 0x0000, 0.0)
    MenuCmd(0x03, 0x00)

    Return()

# id: 0x00A3 offset: 0x2861C
@scena.Code('TK_System_Debug_BlurTest')
def TK_System_Debug_BlurTest():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28625(): pass

    label('loc_28625')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2889A',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '模糊测试（通常）※不动就没有效果', 0x00000001)
    MenuCmd(0x01, 0x01, '模糊测试（放大）', 0x00000002)
    MenuCmd(0x01, 0x01, '模糊测试（破折号用）', 0x00000003)
    MenuCmd(0x01, 0x01, '模糊测试（放大）', 0x00000004)
    MenuCmd(0x01, 0x01, '模糊测试（扩大中央透明）+（角色）', 0x00000005)
    MenuCmd(0x01, 0x01, '模糊测试（放大全画面）+（坐标2，1，0）', 0x00000006)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_287A8'),
        (0x00000002, 'loc_287CE'),
        (0x00000003, 'loc_287F4'),
        (0x00000004, 'loc_2881A'),
        (0x00000005, 'loc_28840'),
        (0x00000006, 'loc_28866'),
        (-1, 'loc_2888C'),
    )

    def _loc_287A8(): pass

    label('loc_287A8')

    OP_5E(0x00, 0x0000, 0.8, 0x00FA, 0x03E8, 0x00FA, 0x00000000, 0xFFFF, '', -9000.0, -9000.0, -9000.0)

    Jump('loc_28895')

    def _loc_287CE(): pass

    label('loc_287CE')

    OP_5E(0x00, 0x0002, 0.8, 0x00FA, 0x03E8, 0x00FA, 0x00000000, 0xFFFF, '', -9000.0, -9000.0, -9000.0)

    Jump('loc_28895')

    def _loc_287F4(): pass

    label('loc_287F4')

    OP_5E(0x00, 0x0001, 0.8, 0x00FA, 0x03E8, 0x00FA, 0x00000000, 0xFFFF, '', -9000.0, -9000.0, -9000.0)

    Jump('loc_28895')

    def _loc_2881A(): pass

    label('loc_2881A')

    OP_5E(0x00, 0x0003, 1.0, 0x00FA, 0x2710, 0x00FA, 0x3E4CCCCD, 0xFFFF, '', -9000.0, -9000.0, -9000.0)

    Jump('loc_28895')

    def _loc_28840(): pass

    label('loc_28840')

    OP_5E(0x00, 0x0004, 1.0, 0x00FA, 0x2710, 0x00FA, 0x3E4CCCCD, 0xF016, '', 0.0, 1.0, 0.0)

    Jump('loc_28895')

    def _loc_28866(): pass

    label('loc_28866')

    OP_5E(0x00, 0x0003, 1.0, 0x00FA, 0x2710, 0x00FA, 0x3E4CCCCD, 0xFFFF, '', 2.0, 0.0, 0.0)

    Jump('loc_28895')

    def _loc_2888C(): pass

    label('loc_2888C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28895(): pass

    label('loc_28895')

    Jump('loc_28625')

    def _loc_2889A(): pass

    label('loc_2889A')

    Return()

# id: 0x00A4 offset: 0x2889C
@scena.Code('TK_System_Debug_FadeTest')
def TK_System_Debug_FadeTest():
    OP_55(0x00, 0x0000, 0x0000, 0x0200, 0x0182, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_VIS4_0001', '')
    OP_55(0x01, 0x0000, 0x0000, 0x0200, 0x0182, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x01, 0x00, 'I_VIS4_0002', '')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2890F(): pass

    label('loc_2890F')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28CB0',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'FADE_LAYER_NORMAL', 0x00000001)
    MenuCmd(0x01, 0x01, 'FADE_LAYER_PREMES ', 0x00000002)
    MenuCmd(0x01, 0x01, 'FADE_LAYER_FRONT ', 0x00000003)
    MenuCmd(0x01, 0x01, 'FADETYPE_CROSS ', 0x00000004)
    MenuCmd(0x01, 0x01, 'ポートレート:DRAW0 ', 0x0000000A)
    MenuCmd(0x01, 0x01, 'ポートレート:DRAW1 ', 0x0000000B)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_28A21'),
        (0x00000002, 'loc_28A9B'),
        (0x00000003, 'loc_28B15'),
        (0x00000004, 'loc_28B8F'),
        (0x0000000A, 'loc_28C29'),
        (0x0000000B, 'loc_28C5E'),
        (-1, 'loc_28C93'),
    )

    def _loc_28A21(): pass

    label('loc_28A21')

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '表示順：\n',
            'FADE_NORMAL\n',
            'Portrait0\n',
            'FADE_PREMES\n',
            'mes\n',
            'Portrait1\n',
            'FADE_FRONT',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    OP_43(0x00, 0x03E8, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_43(0x64, 0x03E8, 1.0, 0x0000)

    Jump('loc_28C9C')

    def _loc_28A9B(): pass

    label('loc_28A9B')

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '表示順：\n',
            'FADE_NORMAL\n',
            'Portrait0\n',
            'FADE_PREMES\n',
            'mes\n',
            'Portrait1\n',
            'FADE_FRONT',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    OP_43(0x00, 0x03E8, 1.0, 0x0001)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_43(0x64, 0x03E8, 1.0, 0x0001)

    Jump('loc_28C9C')

    def _loc_28B15(): pass

    label('loc_28B15')

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '表示順：\n',
            'FADE_NORMAL\n',
            'Portrait0\n',
            'FADE_PREMES\n',
            'mes\n',
            'Portrait1\n',
            'FADE_FRONT',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    OP_43(0x00, 0x03E8, 1.0, 0x0002)
    OP_43(0xFF, 0x0000, 0x0002)
    OP_43(0x64, 0x03E8, 1.0, 0x0002)

    Jump('loc_28C9C')

    def _loc_28B8F(): pass

    label('loc_28B8F')

    OP_43(0x65, 0x07D0, 1.0, 0x0000)
    OP_43(0xFE, 0x0000)
    CameraCtrl(0x03, 0x03, 0x03EA, '', -0.03, 1.4, 0.09, 0x0000)
    CameraRotateByTarget(0x03EA, '', 0x03, 6.0, -17.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.36, 0)
    CameraCtrl(0x0B, 0x03, 40.0, 0x0000)
    Sleep(1000)

    OP_43(0x65, 0x07D0, 1.0, 0x0000)
    OP_43(0xFE, 0x0000)
    CameraCtrl(0x03, 0x03, 0x03EB, '', -0.21, 1.4, 0.55, 0x0000)
    CameraRotateByTarget(0x03EB, '', 0x03, 11.0, -2.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.06, 0)
    CameraCtrl(0x0B, 0x03, 40.0, 0x0000)

    Jump('loc_28C9C')

    def _loc_28C29(): pass

    label('loc_28C29')

    OP_56(0x00, 0x00, 0x00, 200.0, 200.0, 0.0, 0.0, 0.0)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 0.0)

    Jump('loc_28C9C')

    def _loc_28C5E(): pass

    label('loc_28C5E')

    OP_56(0x01, 0x00, 0x00, 1124.0, 200.0, 0.0, 0.0, 0.0)
    OP_56(0x01, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 0.0)

    Jump('loc_28C9C')

    def _loc_28C93(): pass

    label('loc_28C93')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28C9C(): pass

    label('loc_28C9C')

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Jump('loc_2890F')

    def _loc_28CB0(): pass

    label('loc_28CB0')

    OP_58(0xFF)

    Return()

# id: 0x00A5 offset: 0x28CB4
@scena.Code('TK_System_CameraVibrateTest')
def TK_System_CameraVibrateTest():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28CBD(): pass

    label('loc_28CBD')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28EEE',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '振动停止', 0x00000001)
    MenuCmd(0x01, 0x01, '弱振动：0.01f，time 0.15', 0x00000002)
    MenuCmd(0x01, 0x01, '强震：0.10f，time 0.50', 0x00000003)
    MenuCmd(0x01, 0x01, '地震发生～平息：0.10f，time500-1000-2000', 0x00000004)
    MenuCmd(0x01, 0x01, '接受了抢截：0.015f，time0-500-250qenduluum，cycle 250', 0x00000005)
    MenuCmd(0x01, 0x01, '飞行船坠落时：0.015f，time0-5000-0，qenduluum，cycle 500', 0x00000006)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_28E4D'),
        (0x00000002, 'loc_28E60'),
        (0x00000003, 'loc_28E73'),
        (0x00000004, 'loc_28E86'),
        (0x00000005, 'loc_28EA4'),
        (0x00000006, 'loc_28EC2'),
        (-1, 'loc_28EE0'),
    )

    def _loc_28E4D(): pass

    label('loc_28E4D')

    CameraCtrl(0x09, 0.0, 0.0, 0.0)

    Jump('loc_28EE9')

    def _loc_28E60(): pass

    label('loc_28E60')

    CameraCtrl(0x09, 0.01, 0.01, 0.15)

    Jump('loc_28EE9')

    def _loc_28E73(): pass

    label('loc_28E73')

    CameraCtrl(0x09, 0.05, 0.05, 0.5)

    Jump('loc_28EE9')

    def _loc_28E86(): pass

    label('loc_28E86')

    CameraCtrl(0x0A, 0.1, 0.1, 0.0, 0x01F4, 0x03E8, 0x07D0, 0x0000, 0x0000, 0x00)

    Jump('loc_28EE9')

    def _loc_28EA4(): pass

    label('loc_28EA4')

    CameraCtrl(0x0A, 0.015, 0.015, 0.0, 0x0000, 0x01F4, 0x00FA, 0x0001, 0x00FA, 0x00)

    Jump('loc_28EE9')

    def _loc_28EC2(): pass

    label('loc_28EC2')

    CameraCtrl(0x0A, 0.0075, 0.0075, 0.015, 0x0000, 0x1388, 0x0000, 0x0001, 0x01F4, 0x00)

    Jump('loc_28EE9')

    def _loc_28EE0(): pass

    label('loc_28EE0')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28EE9(): pass

    label('loc_28EE9')

    Jump('loc_28CBD')

    def _loc_28EEE(): pass

    label('loc_28EEE')

    Return()

# id: 0x00A6 offset: 0x28EF0
@scena.Code('TK_NoticeLog_Test')
def TK_NoticeLog_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28EF9(): pass

    label('loc_28EF9')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29518',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '清除日志（一瞬间）', 0x00000001)
    MenuCmd(0x01, 0x01, '清除日志（淡入淡出）', 0x00000002)
    MenuCmd(0x01, 0x01, '日志添加×1（人物手册）', 0x00000003)
    MenuCmd(0x01, 0x01, '日志添加×1（项目获取）', 0x00000004)
    MenuCmd(0x01, 0x01, '日志添加×３', 0x00000005)
    MenuCmd(0x01, 0x01, '日志添加×１０', 0x00000006)
    MenuCmd(0x01, 0x01, '日志添加×３５（maxover）', 0x00000007)
    MenuCmd(0x01, 0x01, '在事件中添加日志', 0x00000008)
    MenuCmd(0x01, 0x01, '中断事件', 0x00000009)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_290AB'),
        (0x00000002, 'loc_290B3'),
        (0x00000003, 'loc_290BB'),
        (0x00000004, 'loc_290EC'),
        (0x00000005, 'loc_290FC'),
        (0x00000006, 'loc_29122'),
        (0x00000007, 'loc_29195'),
        (0x00000008, 'loc_2931B'),
        (0x00000009, 'loc_2942B'),
        (-1, 'loc_2950A'),
    )

    def _loc_290AB(): pass

    label('loc_290AB')

    OP_C3(0x01, 0x00)

    Jump('loc_29513')

    def _loc_290B3(): pass

    label('loc_290B3')

    OP_C3(0x01, 0x01)

    Jump('loc_29513')

    def _loc_290BB(): pass

    label('loc_290BB')

    OP_C3(0x00, 0x00, 0x00000011, 0x00000001)
    OP_C3(0x00, 0x00, 0x00000011, 0x00000100)
    OP_C3(0x00, 0x00, 0x00000011, 0x00000200)
    OP_C3(0x00, 0x00, 0x00000011, 0x00000400)

    Jump('loc_29513')

    def _loc_290EC(): pass

    label('loc_290EC')

    OP_C3(0x00, 0x01, 0x00000000, 0x00000000)

    Jump('loc_29513')

    def _loc_290FC(): pass

    label('loc_290FC')

    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)

    Jump('loc_29513')

    def _loc_29122(): pass

    label('loc_29122')

    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)

    Jump('loc_29513')

    def _loc_29195(): pass

    label('loc_29195')

    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)
    OP_C3(0x00, 0x01, 0x00000005, 0x00000000)

    Jump('loc_29513')

    def _loc_2931B(): pass

    label('loc_2931B')

    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_43(0x00, 0x0064, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_43(0x05, 0x012C)
    OP_43(0x64, 0x0064, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_3B(0x00, (0xFF, 0x88C2, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            0xC,
            (TxtCtl.Item, 0x0),
            TxtCtl.SetColor,
            'を手に入れた。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    AddItem(0x00, 0x0000, 1)
    OP_43(0x00, 0x0064, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_43(0x69, 0x012C)
    OP_91(0x00, 0x0000, 0x00000001)
    OP_C3(0x00, 0x01, 0x00000000, 0x00000000)
    OP_43(0x64, 0x0064, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_21(0x00)

    Jump('loc_29513')

    def _loc_2942B(): pass

    label('loc_2942B')

    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_43(0x00, 0x01F4, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_43(0x05, 0x012C)
    OP_43(0x64, 0x01F4, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_27('ナイトハルトの声', 0xFFFF)
    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cフフ……\n',
            '見事だったぞ、シュバルツァー。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_27('', 0xFFFF)
    OP_63(0xFFFF, 0x01)
    OP_43(0x00, 0x01F4, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_43(0x69, 0x012C)
    OP_43(0x64, 0x01F4, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)
    OP_21(0x00)

    Jump('loc_29513')

    def _loc_2950A(): pass

    label('loc_2950A')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_29513(): pass

    label('loc_29513')

    Jump('loc_28EF9')

    def _loc_29518(): pass

    label('loc_29518')

    Return()

# id: 0x00A7 offset: 0x2951C
@scena.Code('TK_PartySel_Test')
def TK_PartySel_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_29525(): pass

    label('loc_29525')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A472',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '▼队伍组成菜单---------', 0x00000062)
    MenuCmd(0x01, 0x01, '【例】第I部（交替形式）', 0x00000001)
    MenuCmd(0x01, 0x01, '【例】第I部（填空形式）', 0x00000002)
    MenuCmd(0x01, 0x01, '【例】第Ⅲ部：星灵窟攻略（交换形式）', 0x00000003)
    MenuCmd(0x01, 0x01, '【例】最后一幕', 0x00000004)
    MenuCmd(0x01, 0x01, '▼团队编辑菜单', 0x00000063)
    MenuCmd(0x01, 0x01, '团队设置-飞行地图注册-JoinParty', 0x0000000A)
    MenuCmd(0x01, 0x01, '取消团队编辑模式', 0x0000000B)
    MenuCmd(0x01, 0x01, '现在的队伍号码和队伍数是？', 0x0000000C)
    MenuCmd(0x01, 0x01, '有提欧的队是？', 0x0000000D)
    MenuCmd(0x01, 0x01, '【例】第Ⅱ部：潘塔格里尔迎击战', 0x0000000E)
    MenuCmd(0x01, 0x01, '【例】终末BOSS战', 0x0000000F)
    MenuCmd(0x01, 0x01, '自动链接', 0x00000010)
    MenuCmd(0x01, 0x01, '▼一个人行动------------------', 0x00000063)
    MenuCmd(0x01, 0x01, '设为个人操作模式', 0x00000014)
    MenuCmd(0x01, 0x01, '取消个人操作模式并更新队伍', 0x00000015)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_2983B'),
        (0x00000002, 'loc_298C1'),
        (0x00000003, 'loc_29947'),
        (0x00000004, 'loc_29A29'),
        (0x0000000A, 'loc_29B71'),
        (0x0000000B, 'loc_29BE1'),
        (0x0000000C, 'loc_29BF9'),
        (0x0000000D, 'loc_29E1A'),
        (0x0000000E, 'loc_29F9B'),
        (0x0000000F, 'loc_2A227'),
        (0x00000010, 'loc_2A3E1'),
        (0x00000014, 'loc_2A3EA'),
        (0x00000015, 'loc_2A45C'),
        (-1, 'loc_2A464'),
    )

    def _loc_2983B(): pass

    label('loc_2983B')

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x0007)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x000F)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_69(0x14, 0x01, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')

    Jump('loc_2A46D')

    def _loc_298C1(): pass

    label('loc_298C1')

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x000F)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_69(0x14, 0x01, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')

    Jump('loc_2A46D')

    def _loc_29947(): pass

    label('loc_29947')

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x0023)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x0001)
    OP_C4(0x02, 0x00, 0x0002)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x001F)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x02, 0x0016)
    OP_C4(0x02, 0x02, 0x0012)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克蕾雅少校'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2D,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_69(0x14, 0x01, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')

    Jump('loc_2A46D')

    def _loc_29A29(): pass

    label('loc_29A29')

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x001A)
    OP_C4(0x02, 0x00, 0x001B)
    OP_C4(0x02, 0x00, 0x0011)
    OP_C4(0x02, 0x00, 0x0014)
    OP_C4(0x02, 0x00, 0x001C)
    OP_C4(0x02, 0x01, 0x001D)
    OP_C4(0x02, 0x01, 0x001E)
    OP_C4(0x02, 0x01, 0x0015)
    OP_C4(0x02, 0x01, 0x001F)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0021)
    OP_C4(0x02, 0x02, 0x0016)
    OP_C4(0x02, 0x02, 0x0020)
    OP_C4(0x02, 0x03, 0x0023)
    OP_C4(0x02, 0x03, 0x0024)
    OP_C4(0x02, 0x03, 0x0025)
    OP_C4(0x02, 0x03, 0x0026)
    OP_C4(0x02, 0x03, 0x0027)
    OP_C4(0x02, 0x04, 0x0010)
    OP_C4(0x02, 0x04, 0x0018)
    OP_C4(0x02, 0x04, 0x0022)
    OP_C4(0x02, 0x04, 0x0019)

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2D,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2E,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2F,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0072, 0, 0x390))
    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    OP_C4(0x04, 0x00, (0xDD, 'a0000'), 0.0, 0.0, 0.0, 180.0)
    OP_C4(0x04, 0x01, (0xDD, 'a0000'), 10.0, 0.0, 0.0, 180.0)
    OP_C4(0x04, 0x02, (0xDD, 'a0000'), 20.0, 0.0, 0.0, 180.0)
    OP_C4(0x04, 0x03, (0xDD, 'a0000'), 30.0, 0.0, 0.0, 180.0)
    OP_C4(0x04, 0x04, (0xDD, 'a0000'), 40.0, 0.0, 0.0, 180.0)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_69(0x14, 0x01, 0x00)

    Jump('loc_2A46D')

    def _loc_29B71(): pass

    label('loc_29B71')

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x01, 0x0000)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x04, 0x00, (0xDD, 'a0000'), -6.12, 0.0, -0.21, 183.0)
    OP_C4(0x04, 0x01, (0xDD, 'a0000'), -4.04, 0.0, 0.05, 88.6)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    Jump('loc_2A46D')

    def _loc_29BE1(): pass

    label('loc_29BE1')

    Call(ScriptId.System, 'FC_TSMenu_Reset')

    Jump('loc_2A46D')

    def _loc_29BF9(): pass

    label('loc_29BF9')

    If(
        (
            (Expr.Eval, "OP_C4(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29C37',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチームは無い',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29E15')

    def _loc_29C37(): pass

    label('loc_29C37')

    If(
        (
            (Expr.Eval, "OP_C4(0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29C73',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム数：4',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29D22')

    def _loc_29C73(): pass

    label('loc_29C73')

    If(
        (
            (Expr.Eval, "OP_C4(0x06)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29CAF',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム数：3',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29D22')

    def _loc_29CAF(): pass

    label('loc_29CAF')

    If(
        (
            (Expr.Eval, "OP_C4(0x06)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29CEB',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム数：2',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29D22')

    def _loc_29CEB(): pass

    label('loc_29CEB')

    If(
        (
            (Expr.Eval, "OP_C4(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29D22',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム数：1',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    def _loc_29D22(): pass

    label('loc_29D22')

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29D60',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム番号：D',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29E15')

    def _loc_29D60(): pass

    label('loc_29D60')

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29D9E',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム番号：C',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29E15')

    def _loc_29D9E(): pass

    label('loc_29D9E')

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29DDC',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム番号：B',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29E15')

    def _loc_29DDC(): pass

    label('loc_29DDC')

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29E15',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cチーム番号：A',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    def _loc_29E15(): pass

    label('loc_29E15')

    Jump('loc_2A46D')

    def _loc_29E1A(): pass

    label('loc_29E1A')

    If(
        (
            (Expr.Eval, "OP_C4(0x03, 0x0000)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29E6A',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4CチームAにリィンおります',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29F96')

    def _loc_29E6A(): pass

    label('loc_29E6A')

    If(
        (
            (Expr.Eval, "OP_C4(0x03, 0x0000)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29EBA',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4CチームBにリィンおります',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29F96')

    def _loc_29EBA(): pass

    label('loc_29EBA')

    If(
        (
            (Expr.Eval, "OP_C4(0x03, 0x0000)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29F0A',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4CチームCにリィンおります',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29F96')

    def _loc_29F0A(): pass

    label('loc_29F0A')

    If(
        (
            (Expr.Eval, "OP_C4(0x03, 0x0000)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29F5A',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4CチームDにリィンおります',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_29F96')

    def _loc_29F5A(): pass

    label('loc_29F5A')

    If(
        (
            (Expr.Eval, "OP_C4(0x03, 0x0000)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29F96',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cリィン無所属',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    def _loc_29F96(): pass

    label('loc_29F96')

    Jump('loc_2A46D')

    def _loc_29F9B(): pass

    label('loc_29F9B')

    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3CＡチームを編成してください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x001D)
    OP_C4(0x02, 0x00, 0x001B)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x05, 0x0002)
    OP_C4(0x02, 0x05, 0x0004)
    OP_C4(0x02, 0x05, 0x0006)
    OP_C4(0x02, 0x05, 0x0011)
    OP_C4(0x02, 0x05, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['湯瑪斯'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克蕾雅少校'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x30,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3CＢチームを編成してください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_C4(0x02, 0x01, 0x001A)
    OP_C4(0x02, 0x01, 0x001C)
    OP_C4(0x02, 0x01, 0x001E)
    OP_C4(0x02, 0x01, 0x0015)
    OP_C4(0x02, 0x01, 0x0023)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x05, 0x0001)
    OP_C4(0x02, 0x05, 0x0005)
    OP_C4(0x02, 0x05, 0x0007)
    OP_C4(0x02, 0x05, 0x0003)
    OP_C4(0x02, 0x05, 0x000F)
    OP_C4(0x02, 0x05, 0x0014)
    OP_C4(0x02, 0x05, 0x0012)
    MenuChrFlagCmd(0x00, ChrTable['派崔克'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x30,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    Jump('loc_2A46D')

    def _loc_2A227(): pass

    label('loc_2A227')

    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '#1C最後の戦いは３チームに分かれて戦います。\\n',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x00, 0xFF)
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x0010)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x01, 0x001A)
    OP_C4(0x02, 0x01, 0x001B)
    OP_C4(0x02, 0x01, 0x001C)
    OP_C4(0x02, 0x01, 0x0020)
    OP_C4(0x02, 0x02, 0x0003)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0004)
    OP_C4(0x02, 0x02, 0x0002)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x001D)
    OP_C4(0x02, 0x02, 0x001E)
    OP_C4(0x02, 0x02, 0x0022)
    OP_C4(0x02, 0x04, 0x001F)
    OP_C4(0x02, 0x04, 0x0015)
    OP_C4(0x02, 0x04, 0x0011)
    OP_C4(0x02, 0x04, 0x0014)
    OP_C4(0x02, 0x04, 0x0028)
    OP_C4(0x02, 0x04, 0x0016)
    OP_C4(0x02, 0x04, 0x0018)
    OP_C4(0x02, 0x04, 0x0019)
    OP_C4(0x02, 0x05, 0x0012)
    OP_C4(0x02, 0x05, 0x0021)
    OP_C4(0x02, 0x05, 0x0023)
    OP_C4(0x02, 0x05, 0x0024)
    OP_C4(0x02, 0x05, 0x0025)
    OP_C4(0x02, 0x05, 0x0026)
    OP_C4(0x02, 0x05, 0x0027)
    SetScenaFlags(ScenaFlag(0x0072, 2, 0x392))

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x2F,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x30,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)

    Jump('loc_2A46D')

    def _loc_2A3E1(): pass

    label('loc_2A3E1')

    OP_69(0x14, 0x01, 0x01)

    Jump('loc_2A46D')

    def _loc_2A3EA(): pass

    label('loc_2A3EA')

    FormationReset(0x00)
    FormationAddMember(ChrTable['悠娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['菲'])
    FormationSetLeader(ChrTable['悠娜'])
    OP_69(0x14, 0x01, 0x00)
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['悠娜'])
    FormationSetLeader(ChrTable['悠娜'])
    MenuChrFlagCmd(0x01, 0xFFFF, 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)

    Jump('loc_2A46D')

    def _loc_2A45C(): pass

    label('loc_2A45C')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_2A46D')

    def _loc_2A464(): pass

    label('loc_2A464')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A46D(): pass

    label('loc_2A46D')

    Jump('loc_29525')

    def _loc_2A472(): pass

    label('loc_2A472')

    Return()

# id: 0x00A8 offset: 0x2A474
@scena.Code('TK_Train_Test')
def TK_Train_Test():
    ModelCtrl(0x31, 0x00, 0x0000, 0x0028, 1.6, 0.25, 0x03, 0x00, 0x0000)
    OP_C9(0x0A, 0x0028, 'TK_celine2:tk_celine2')
    MenuChrFlagCmd(0x00, ChrTable['測試：恩奈雅'], 0x00000000)
    ChrPhysicsCtrl(0x0A, ChrTable['測試：恩奈雅'], 0x00000004)

    Return()

# id: 0x00A9 offset: 0x2A4B4
@scena.Code('TK_Bgm_Test')
def TK_Bgm_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A4BD(): pass

    label('loc_2A4BD')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A63B',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'play_bgm()', 0x00000064)
    MenuCmd(0x01, 0x01, 'stop_bgm()', 0x00000065)
    MenuCmd(0x01, 0x01, 'play_bgm() stop_bgm()  play_bgm()', 0x00000066)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000064, 'loc_2A55F'),
        (0x00000065, 'loc_2A593'),
        (0x00000066, 'loc_2A5BE'),
        (-1, 'loc_2A62D'),
    )

    def _loc_2A55F(): pass

    label('loc_2A55F')

    PlayBGM(922, 1.0, 0x0000, 0x00000000, 0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '新BGM播放',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2A636')

    def _loc_2A593(): pass

    label('loc_2A593')

    OP_3A(0x01, 0x00AB, 0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'stop_bgm(500)',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2A636')

    def _loc_2A5BE(): pass

    label('loc_2A5BE')

    PlayBGM(171, 1.0, 0x0000, 0x00000000, 0x00)
    OP_3A(0x01, 0x00AB, 0x00)
    PlayBGM(171, 1.0, 0x0000, 0x00000000, 0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'play_bgm(BGM_171)\\nstop_bgm(500)\\nplay_bgm(BGM_171)',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2A636')

    def _loc_2A62D(): pass

    label('loc_2A62D')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A636(): pass

    label('loc_2A636')

    Jump('loc_2A4BD')

    def _loc_2A63B(): pass

    label('loc_2A63B')

    Return()

# id: 0x00AA offset: 0x2A63C
@scena.Code('TK_ActMenu_Test')
def TK_ActMenu_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A645(): pass

    label('loc_2A645')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A92F',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 3, 0x39B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'アクションメニュー禁止', 0x00000001, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 1, 0x399)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'アクションメニューボタン禁止', 0x00000002, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr24, 0x400000),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'SYSTEM_FLAG_SHORTCUT_HORSE', 0x00000003, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 2, 0x39A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '選択肢：アークス起動', 0x00000004, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 1, 0x311)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '選択肢：バイク起動', 0x00000005, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '選択肢：馬起動', 0x00000006, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 5, 0x39D)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '選択肢：導力波測定器', 0x00000007, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 4, 0x394)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '選択肢：エマのペンダント', 0x00000008, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr24, 0x100),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'SYSTEM_FLAG_HORSE_GETON_DISABLE', 0x00000009, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_2A8D5'),
        (0x00000002, 'loc_2A8DD'),
        (0x00000003, 'loc_2A8E5'),
        (0x00000004, 'loc_2A8EF'),
        (0x00000005, 'loc_2A8F7'),
        (0x00000006, 'loc_2A8FF'),
        (0x00000007, 'loc_2A907'),
        (0x00000008, 'loc_2A90F'),
        (0x00000009, 'loc_2A917'),
        (-1, 'loc_2A921'),
    )

    def _loc_2A8D5(): pass

    label('loc_2A8D5')

    OP_12(0x039B)

    Jump('loc_2A92A')

    def _loc_2A8DD(): pass

    label('loc_2A8DD')

    OP_12(0x0399)

    Jump('loc_2A92A')

    def _loc_2A8E5(): pass

    label('loc_2A8E5')

    OP_15(0x00400000)

    Jump('loc_2A92A')

    def _loc_2A8EF(): pass

    label('loc_2A8EF')

    OP_12(0x039A)

    Jump('loc_2A92A')

    def _loc_2A8F7(): pass

    label('loc_2A8F7')

    OP_12(0x0311)

    Jump('loc_2A92A')

    def _loc_2A8FF(): pass

    label('loc_2A8FF')

    OP_12(0x0310)

    Jump('loc_2A92A')

    def _loc_2A907(): pass

    label('loc_2A907')

    OP_12(0x039D)

    Jump('loc_2A92A')

    def _loc_2A90F(): pass

    label('loc_2A90F')

    OP_12(0x0394)

    Jump('loc_2A92A')

    def _loc_2A917(): pass

    label('loc_2A917')

    OP_15(0x00000100)

    Jump('loc_2A92A')

    def _loc_2A921(): pass

    label('loc_2A921')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A92A(): pass

    label('loc_2A92A')

    Jump('loc_2A645')

    def _loc_2A92F(): pass

    label('loc_2A92F')

    Return()

# id: 0x00AB offset: 0x2A930
@scena.Code('EV_useChecker')
def EV_useChecker():
    OP_20(0x15, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    OP_3A(0x03, 1.0, 0x01F4, 0x00)
    SetChrFace(0x04, ChrTable['黎恩'], '#E0#M4')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            '#0T#3Kレベル３、か。\n',
            'ここは全く問題ないみたいだな。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_63(0xFFFF, 0x01)
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetChrFace(0x03, ChrTable['黎恩'], '0[autoE0]', '0[autoM0]', '', '#b', '0')
    OP_21(0x15)

    Return()

# id: 0x00AC offset: 0x2A9E8
@scena.Code('EV_useItemEmasPendant')
def EV_useItemEmasPendant():
    Return()

# id: 0x00AD offset: 0x2A9EC
@scena.Code('TK_LinkLevel_Test')
def TK_LinkLevel_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A9F5(): pass

    label('loc_2A9F5')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2ACEB',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '链接注册新老+嘉宾', 0x00000001)
    MenuCmd(0x01, 0x01, '链接EXP上升（一人）', 0x00000002)
    MenuCmd(0x01, 0x01, '链接EXP上升（多人）', 0x00000003)
    MenuCmd(0x01, 0x01, '链接EXP（LVUP之前）', 0x00000004)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_2AADA'),
        (0x00000002, 'loc_2AB97'),
        (0x00000003, 'loc_2ABB8'),
        (0x00000004, 'loc_2ABED'),
        (-1, 'loc_2ACDD'),
    )

    def _loc_2AADA(): pass

    label('loc_2AADA')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x00000002)
    MenuChrFlagCmd(0x01, 0xFFFF, 0x00000004)
    MenuChrFlagCmd(0x01, 0xFFFF, 0x00000008)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['妙婕'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['克蕾雅少校'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['測試：杜巴莉'], 0x00000008)
    MenuChrFlagCmd(0x00, ChrTable['測試：奧利維爾'], 0x00000008)
    MenuChrFlagCmd(0x00, ChrTable['測試：恩奈雅'], 0x00000008)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000008)

    Jump('loc_2ACE6')

    def _loc_2AB97(): pass

    label('loc_2AB97')

    OP_69(0x04, 0x0007)
    OP_69(0x06, 0x0000, 0x000A, 0x0258, 0x00000000)
    OP_69(0x07, 0x0000)
    OP_69(0x09, 0x0000)
    OP_69(0x08, 0x0000)

    Jump('loc_2ACE6')

    def _loc_2ABB8(): pass

    label('loc_2ABB8')

    OP_69(0x06, 0x0000, 0x000B, 0x012C, 0x00000000)
    OP_69(0x06, 0x000B, 0x000A, 0x012C, 0x00000000)
    OP_69(0x06, 0x000C, 0x000E, 0x012C, 0x00000000)
    OP_69(0x07, 0x0000)
    OP_69(0x09, 0x0000)
    OP_69(0x08, 0x0000)

    Jump('loc_2ACE6')

    def _loc_2ABED(): pass

    label('loc_2ABED')

    OP_69(0x05, 0x0000, 0x000B, 0x07CF)
    OP_69(0x05, 0x0000, 0x000A, 0x07CF)
    OP_69(0x05, 0x000B, 0x000A, 0x07CF)
    OP_69(0x05, 0x000B, 0x000C, 0x07CF)
    OP_69(0x05, 0x000C, 0x000E, 0x07CF)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'リィン - クルト、\\nリィン - ユウナ、\\nクルト - ユウナ、\\nクルト - アルティナ、\\nアルティナ - アッシュ\\nのLVEXPを1999にしました。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2ACE6')

    def _loc_2ACDD(): pass

    label('loc_2ACDD')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2ACE6(): pass

    label('loc_2ACE6')

    Jump('loc_2A9F5')

    def _loc_2ACEB(): pass

    label('loc_2ACEB')

    Return()

# id: 0x00AE offset: 0x2ACEC
@scena.Code('TK_LikeLevel_Test')
def TK_LikeLevel_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2ACF5(): pass

    label('loc_2ACF5')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BAA4',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '好感度全恢复', 0x0000000A)
    MenuCmd(0x01, 0x01, '好感度LV+1（一人）', 0x00000001)
    MenuCmd(0x01, 0x01, '好感度Lv+2（一人）', 0x00000002)
    MenuCmd(0x01, 0x01, '好感度Lv+1（很多人）', 0x00000003)
    MenuCmd(0x01, 0x01, '好感度exp+300（一个人）', 0x00000005)
    MenuCmd(0x01, 0x01, '好感度exp+200（一人）', 0x00000006)
    MenuCmd(0x01, 0x01, '好感度exp+1000（很多人）', 0x00000007)
    MenuCmd(0x01, 0x01, '好感度exp+1000（不显示人数和计量器）', 0x00000008)
    MenuCmd(0x01, 0x01, '库尔特的好感度LV是？', 0x00000014)
    MenuCmd(0x01, 0x01, '库尔特的好感度EXP是？', 0x00000015)
    MenuCmd(0x01, 0x01, '好感度最高的角色是？', 0x00000016)
    MenuCmd(0x01, 0x01, '好感度MAX', 0x00000017)
    MenuCmd(0x01, 0x01, '好感度极限', 0x00000018)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x0000000A, 'loc_2AF63'),
        (0x00000014, 'loc_2B000'),
        (0x00000015, 'loc_2B1BA'),
        (0x00000016, 'loc_2B340'),
        (0x00000017, 'loc_2B8B2'),
        (0x00000018, 'loc_2B920'),
        (0x00000001, 'loc_2B9CA'),
        (0x00000002, 'loc_2B9D9'),
        (0x00000003, 'loc_2B9E8'),
        (0x00000005, 'loc_2BA06'),
        (0x00000006, 'loc_2BA18'),
        (0x00000007, 'loc_2BA2A'),
        (0x00000008, 'loc_2BA54'),
        (-1, 'loc_2BA96'),
    )

    def _loc_2AF63(): pass

    label('loc_2AF63')

    OP_C6(0x04, 0x000A, 0x00000000)
    OP_C6(0x04, 0x000B, 0x00000000)
    OP_C6(0x04, 0x000C, 0x00000000)
    OP_C6(0x04, 0x000D, 0x00000000)
    OP_C6(0x04, 0x000E, 0x00000000)
    OP_C6(0x04, 0x002C, 0x00000000)
    OP_C6(0x04, 0x0009, 0x00000000)
    OP_C6(0x04, 0x0066, 0x00000000)
    OP_C6(0x04, 0x0003, 0x00000000)
    OP_C6(0x04, 0x0002, 0x00000000)
    OP_C6(0x04, 0x0004, 0x00000000)
    OP_C6(0x04, 0x0001, 0x00000000)
    OP_C6(0x04, 0x0016, 0x00000000)
    OP_C6(0x04, 0x0007, 0x00000000)
    OP_C6(0x04, 0x0006, 0x00000000)
    OP_C6(0x04, 0x0008, 0x00000000)
    OP_C6(0x04, 0x0005, 0x00000000)
    OP_C6(0x04, 0x0091, 0x00000000)
    OP_C6(0x04, 0x000F, 0x00000000)

    Jump('loc_2BA9F')

    def _loc_2B000(): pass

    label('loc_2B000')

    If(
        (
            (Expr.Eval, "OP_C6(0x06, 0x000B)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B039',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度０',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B1B4')

    def _loc_2B039(): pass

    label('loc_2B039')

    If(
        (
            (Expr.Eval, "OP_C6(0x06, 0x000B)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B072',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度１',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B1B4')

    def _loc_2B072(): pass

    label('loc_2B072')

    If(
        (
            (Expr.Eval, "OP_C6(0x06, 0x000B)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B0AB',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度２',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B1B4')

    def _loc_2B0AB(): pass

    label('loc_2B0AB')

    If(
        (
            (Expr.Eval, "OP_C6(0x06, 0x000B)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B0E4',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度３',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B1B4')

    def _loc_2B0E4(): pass

    label('loc_2B0E4')

    If(
        (
            (Expr.Eval, "OP_C6(0x06, 0x000B)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B11D',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度４',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B1B4')

    def _loc_2B11D(): pass

    label('loc_2B11D')

    If(
        (
            (Expr.Eval, "OP_C6(0x06, 0x000B)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B156',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度５',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B1B4')

    def _loc_2B156(): pass

    label('loc_2B156')

    If(
        (
            (Expr.Eval, "OP_C6(0x06, 0x000B)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B1B4',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度６は無いはずだよ。エラーだよ。',
            TxtCtl.Enter,
        ),
    )

    def _loc_2B1B4(): pass

    label('loc_2B1B4')

    WaitForMsg()

    Jump('loc_2BA9F')

    def _loc_2B1BA(): pass

    label('loc_2B1BA')

    If(
        (
            (Expr.Eval, "OP_C6(0x07, 0x000B)"),
            (Expr.PushLong, 0x64),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2B1FD',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度EXP 100以下',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B33A')

    def _loc_2B1FD(): pass

    label('loc_2B1FD')

    If(
        (
            (Expr.Eval, "OP_C6(0x07, 0x000B)"),
            (Expr.PushLong, 0x1F4),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2B240',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度EXP 500以下',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B33A')

    def _loc_2B240(): pass

    label('loc_2B240')

    If(
        (
            (Expr.Eval, "OP_C6(0x07, 0x000B)"),
            (Expr.PushLong, 0x3E8),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2B284',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度EXP 1000以下',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B33A')

    def _loc_2B284(): pass

    label('loc_2B284')

    If(
        (
            (Expr.Eval, "OP_C6(0x07, 0x000B)"),
            (Expr.PushLong, 0x5DC),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2B2C8',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度EXP 1500以下',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B33A')

    def _loc_2B2C8(): pass

    label('loc_2B2C8')

    If(
        (
            (Expr.Eval, "OP_C6(0x07, 0x000B)"),
            (Expr.PushLong, 0x7D0),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2B30C',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度EXP 2000以下',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B33A')

    def _loc_2B30C(): pass

    label('loc_2B30C')

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C好感度EXP 2000以上',
            TxtCtl.Enter,
        ),
    )

    def _loc_2B33A(): pass

    label('loc_2B33A')

    WaitForMsg()

    Jump('loc_2BA9F')

    def _loc_2B340(): pass

    label('loc_2B340')

    OP_A4(0x00, 0x00, 0x000A, 0x000B, 0x000C, 0x000D, 0x000E, 0x002C, 0x0009, 0x0066, 0x0003, 0x0002, 0x0004, 0x0001, 0x0016, 0x0007, 0x0006, 0x0008, 0x0005, 0x0091, 0x000F, 0xFFFF)

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B3AD',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cユウナといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B3AD(): pass

    label('loc_2B3AD')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B3EF',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cクルトといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B3EF(): pass

    label('loc_2B3EF')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B437',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cアルティナといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B437(): pass

    label('loc_2B437')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B479',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cミュゼといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B479(): pass

    label('loc_2B479')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B4BE',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cアッシュといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B4BE(): pass

    label('loc_2B4BE')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x2C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B4FD',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cトワといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B4FD(): pass

    label('loc_2B4FD')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B542',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cミリアムといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B542(): pass

    label('loc_2B542')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B584',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cクレアといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B584(): pass

    label('loc_2B584')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B5C6',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cラウラといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B5C6(): pass

    label('loc_2B5C6')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B60E',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cエリオットといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B60E(): pass

    label('loc_2B60E')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B653',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cマキアスといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B653(): pass

    label('loc_2B653')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B695',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cアリサといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B695(): pass

    label('loc_2B695')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x16),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B6DA',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cシャロンといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B6DA(): pass

    label('loc_2B6DA')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B71C',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cフィーといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B71C(): pass

    label('loc_2B71C')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B761',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cユーシスといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B761(): pass

    label('loc_2B761')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B7A6',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cガイウスといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B7A6(): pass

    label('loc_2B7A6')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B7E5',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cエマといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B7E5(): pass

    label('loc_2B7E5')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0x91),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B82A',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cセリーヌといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B82A(): pass

    label('loc_2B82A')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0xF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B869',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4Cサラといい感じ',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8AC')

    def _loc_2B869(): pass

    label('loc_2B869')

    If(
        (
            (Expr.Expr23, 0x1E),
            (Expr.PushLong, 0xFFFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B8AC',
    )

    SetChrFace(0x04, 0xF016, '')

    ChrTalk(
        0xF016,
        0x00000000,
        (
            '#0T#2P#4C誰ともいい感じでない',
            TxtCtl.Enter,
        ),
    )

    def _loc_2B8AC(): pass

    label('loc_2B8AC')

    WaitForMsg()

    Jump('loc_2BA9F')

    def _loc_2B8B2(): pass

    label('loc_2B8B2')

    OP_C6(0x03, 0x000A, 0x05)
    OP_C6(0x03, 0x000B, 0x05)
    OP_C6(0x03, 0x000C, 0x05)
    OP_C6(0x03, 0x000D, 0x05)
    OP_C6(0x03, 0x000E, 0x05)
    OP_C6(0x03, 0x002C, 0x05)
    OP_C6(0x03, 0x0001, 0x05)
    OP_C6(0x03, 0x0002, 0x05)
    OP_C6(0x03, 0x0003, 0x05)
    OP_C6(0x03, 0x0004, 0x05)
    OP_C6(0x03, 0x0005, 0x05)
    OP_C6(0x03, 0x0006, 0x05)
    OP_C6(0x03, 0x0007, 0x05)
    OP_C6(0x03, 0x0008, 0x05)
    OP_C6(0x03, 0x0023, 0x05)
    OP_C6(0x03, 0x000F, 0x05)
    OP_C6(0x03, 0x0091, 0x05)
    OP_C6(0x03, 0x002D, 0x05)
    OP_C6(0x03, 0x002E, 0x05)
    OP_C6(0x03, 0x0017, 0x05)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2B920(): pass

    label('loc_2B920')

    OP_C6(0x04, 0x000A, 0x00000384)
    OP_C6(0x04, 0x000B, 0x00000384)
    OP_C6(0x04, 0x000C, 0x00000384)
    OP_C6(0x04, 0x000D, 0x00000384)
    OP_C6(0x04, 0x000E, 0x00000384)
    OP_C6(0x04, 0x002C, 0x00000384)
    OP_C6(0x04, 0x0001, 0x00000384)
    OP_C6(0x04, 0x0002, 0x00000384)
    OP_C6(0x04, 0x0003, 0x00000384)
    OP_C6(0x04, 0x0004, 0x00000384)
    OP_C6(0x04, 0x0005, 0x00000384)
    OP_C6(0x04, 0x0006, 0x00000384)
    OP_C6(0x04, 0x0007, 0x00000384)
    OP_C6(0x04, 0x0008, 0x00000384)
    OP_C6(0x04, 0x0023, 0x00000384)
    OP_C6(0x04, 0x000F, 0x00000384)
    OP_C6(0x04, 0x0091, 0x00000384)
    OP_C6(0x04, 0x002D, 0x00000384)
    OP_C6(0x04, 0x002E, 0x00000384)
    OP_C6(0x04, 0x0017, 0x00000384)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2B9CA(): pass

    label('loc_2B9CA')

    OP_C6(0x03, 0x000B, 0x01)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2B9D9(): pass

    label('loc_2B9D9')

    OP_C6(0x03, 0x000D, 0x02)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2B9E8(): pass

    label('loc_2B9E8')

    OP_C6(0x03, 0x000B, 0x01)
    OP_C6(0x03, 0x000C, 0x01)
    OP_C6(0x03, 0x000E, 0x01)
    OP_C6(0x03, 0x0004, 0x01)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2BA06(): pass

    label('loc_2BA06')

    OP_C6(0x05, 0x000B, 0x0000012C)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2BA18(): pass

    label('loc_2BA18')

    OP_C6(0x05, 0x000D, 0x000007D0)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2BA2A(): pass

    label('loc_2BA2A')

    OP_C6(0x05, 0x002C, 0x000003E8)
    OP_C6(0x05, 0x002E, 0x000003E8)
    OP_C6(0x05, 0x002D, 0x000003E8)
    OP_C6(0x05, 0x0091, 0x000003E8)
    OP_C6(0x00, 0x00)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2BA54(): pass

    label('loc_2BA54')

    OP_C6(0x05, 0x000B, 0x000003E8)
    OP_C6(0x05, 0x000C, 0x000003E8)
    OP_C6(0x05, 0x000E, 0x000003E8)
    OP_C6(0x05, 0x0004, 0x000003E8)
    OP_C6(0x05, 0x0091, 0x000003E8)
    OP_C6(0x05, 0x0016, 0x000003E8)
    OP_C6(0x05, 0x0066, 0x000003E8)
    OP_C6(0x00, 0x01)
    OP_C6(0x01)

    Jump('loc_2BA9F')

    def _loc_2BA96(): pass

    label('loc_2BA96')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BA9F(): pass

    label('loc_2BA9F')

    Jump('loc_2ACF5')

    def _loc_2BAA4(): pass

    label('loc_2BAA4')

    Return()

# id: 0x00AF offset: 0x2BAA8
@scena.Code('LP_trialbox01')
def LP_trialbox01():
    OP_18(
        0x17,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_trialbox_open', (0xDD, 'TrialBox01'))

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BAFB',
    )

    Battle(0x00, 0x0000000A, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    def _loc_2BAFB(): pass

    label('loc_2BAFB')

    Return()

# id: 0x00B0 offset: 0x2BAFC
@scena.Code('LP_trialbox01_Get')
def LP_trialbox01_Get():
    Call(ScriptId.System, 'FC_trialbox_get', (0xDD, 'TrialBox01'))

    Return()

# id: 0x00B1 offset: 0x2BB1C
@scena.Code('TK_Calendar_Test')
def TK_Calendar_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BB25(): pass

    label('loc_2BB25')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C101',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '元旦／特別日無し／行動ポイント０', 0x00000001)
    MenuCmd(0x01, 0x01, '日付：12月23日(木)', 0x0000000A)
    MenuCmd(0x01, 0x01, '日付：1月23日(木)', 0x0000000B)
    MenuCmd(0x01, 0x01, '日付：12月2日(木)', 0x0000000C)
    MenuCmd(0x01, 0x01, '特別日切り替え', 0x00000003)
    MenuCmd(0x01, 0x01, '行動ポイント：３', 0x00000004)
    MenuCmd(0x01, 0x01, '行動ポイント：３６', 0x00000009)
    MenuCmd(0x01, 0x01, '行動ポイント：＋１', 0x00000005)
    MenuCmd(0x01, 0x01, '行動ポイント：－１', 0x00000006)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 4, 0x39C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'フラグ：カレンダー表示オフ', 0x00000007, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 7, 0x39F)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'フラグ：チケットモード', 0x00000008, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 6, 0x396)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'フラグ：勉強モード', 0x0000000F, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x01, 'イベントカレンダー１', 0x0000000D)
    MenuCmd(0x01, 0x01, 'イベントカレンダー２(全行事名付き)', 0x0000000E)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_2BE22'),
        (0x0000000A, 'loc_2BE4C'),
        (0x0000000B, 'loc_2BE6C'),
        (0x0000000C, 'loc_2BE8C'),
        (0x00000003, 'loc_2BEAC'),
        (0x00000004, 'loc_2BEF2'),
        (0x00000009, 'loc_2BEFA'),
        (0x00000005, 'loc_2BF02'),
        (0x00000006, 'loc_2BF0A'),
        (0x00000007, 'loc_2BF29'),
        (0x00000008, 'loc_2BF31'),
        (0x0000000F, 'loc_2BF39'),
        (0x0000000D, 'loc_2BF41'),
        (0x0000000E, 'loc_2BF9C'),
        (-1, 'loc_2C0F3'),
    )

    def _loc_2BE22(): pass

    label('loc_2BE22')

    OP_18(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x05,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x09,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A0()

    Jump('loc_2C0FC')

    def _loc_2BE4C(): pass

    label('loc_2BE4C')

    OP_18(
        0x04,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x05,
        (
            (Expr.PushLong, 0x17),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x09,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C0FC')

    def _loc_2BE6C(): pass

    label('loc_2BE6C')

    OP_18(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x05,
        (
            (Expr.PushLong, 0x17),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x09,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C0FC')

    def _loc_2BE8C(): pass

    label('loc_2BE8C')

    OP_18(
        0x04,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x05,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x09,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2C0FC')

    def _loc_2BEAC(): pass

    label('loc_2BEAC')

    If(
        (
            (Expr.Expr23, 0x6),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BEC8',
    )

    OP_18(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2BEED')

    def _loc_2BEC8(): pass

    label('loc_2BEC8')

    If(
        (
            (Expr.Expr23, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BEE4',
    )

    OP_18(
        0x06,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2BEED')

    def _loc_2BEE4(): pass

    label('loc_2BEE4')

    OP_18(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BEED(): pass

    label('loc_2BEED')

    Jump('loc_2C0FC')

    def _loc_2BEF2(): pass

    label('loc_2BEF2')

    OP_88(0x0003)

    Jump('loc_2C0FC')

    def _loc_2BEFA(): pass

    label('loc_2BEFA')

    OP_88(0x0024)

    Jump('loc_2C0FC')

    def _loc_2BF02(): pass

    label('loc_2BF02')

    OP_89(0x0001)

    Jump('loc_2C0FC')

    def _loc_2BF0A(): pass

    label('loc_2BF0A')

    If(
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BF24',
    )

    OP_18(
        0x0A,
        (
            (Expr.Expr23, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BF24(): pass

    label('loc_2BF24')

    Jump('loc_2C0FC')

    def _loc_2BF29(): pass

    label('loc_2BF29')

    OP_12(0x039C)

    Jump('loc_2C0FC')

    def _loc_2BF31(): pass

    label('loc_2BF31')

    OP_12(0x039F)

    Jump('loc_2C0FC')

    def _loc_2BF39(): pass

    label('loc_2BF39')

    OP_12(0x0396)

    Jump('loc_2C0FC')

    def _loc_2BF41(): pass

    label('loc_2BF41')

    OP_43(0x00, 0x00C8, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)
    OP_8E(0x0001, 0x000A, 0xFFFF, 0x0001, 0x000A, 0xFFFF, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0009, 0x0001, 0xFFFF, 0x0009, 0x0009, 0xFFFF, 0x0000, 0x04B6)
    OP_8F()
    OP_8E(0x0009, 0x0001, 0xFFFF, 0x0009, 0x0014, 0xFFFF, 0x0000, 0x04B6)
    OP_8F()
    OP_43(0x64, 0x00C8, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)

    Jump('loc_2C0FC')

    def _loc_2BF9C(): pass

    label('loc_2BF9C')

    OP_43(0x00, 0x00C8, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)
    OP_8E(0x0001, 0x0001, 0xFFFF, 0x0001, 0x0002, 0x0000, 0x0001, 0x04B5)
    OP_8F()
    OP_8E(0x0004, 0x0010, 0x0000, 0x0004, 0x0011, 0x000B, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0004, 0x0011, 0x0001, 0x0004, 0x0015, 0x0002, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0004, 0x0015, 0x0002, 0x0004, 0x0016, 0x0003, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0004, 0x0016, 0x0003, 0x0004, 0x0017, 0x0004, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0006, 0x0004, 0x0007, 0x0007, 0x0005, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0007, 0x0005, 0x0007, 0x0008, 0x0006, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0004, 0x0006, 0x0007, 0x0005, 0x0007, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0001, 0x000A, 0x0007, 0x0001, 0x000A, 0x0008, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0001, 0x000A, 0x0008, 0x0001, 0x000A, 0x0009, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0001, 0x000A, 0x0009, 0x0001, 0x000A, 0x000A, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0009, 0x000A, 0x0007, 0x000C, 0x000B, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0010, 0x000B, 0x0007, 0x0011, 0x000C, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0011, 0x000C, 0x0007, 0x0012, 0x000D, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0012, 0x000D, 0x0007, 0x0013, 0x000E, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0013, 0x000E, 0x0007, 0x0014, 0x000F, 0x0000, 0x04B5)
    OP_8F()
    OP_8E(0x0007, 0x0014, 0x000F, 0x0007, 0x0015, 0x0010, 0x0000, 0x04B5)
    OP_8F()
    OP_43(0x64, 0x00C8, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)

    Jump('loc_2C0FC')

    def _loc_2C0F3(): pass

    label('loc_2C0F3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C0FC(): pass

    label('loc_2C0FC')

    Jump('loc_2BB25')

    def _loc_2C101(): pass

    label('loc_2C101')

    Return()

# id: 0x00B2 offset: 0x2C104
@scena.Code('TK_CameraCommand_Test')
def TK_CameraCommand_Test():
    Call(ScriptId.System, 'FC_TalkEnd_NoCamMove')
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x0, 0x0))
    CameraRotate(0x03, 0.0, 0.0, 0.0, 0, 0x01)
    OP_43(0x64, 0x012C, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x00FF)

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C15E(): pass

    label('loc_2C15E')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C50E',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '  0度に回転(角度差小さい方に回転)', 0x00000064)
    MenuCmd(0x01, 0x01, ' 45度に回転(角度差小さい方に回転)', 0x00000065)
    MenuCmd(0x01, 0x01, '-45度に回転(角度差小さい方に回転)', 0x00000066)
    MenuCmd(0x01, 0x01, '315度に回転(角度差小さい方に回転)', 0x00000067)
    MenuCmd(0x01, 0x01, ' 45度に回転(線形補完回転)', 0x00000068)
    MenuCmd(0x01, 0x01, '-45度に回転(線形補完回転)', 0x00000069)
    MenuCmd(0x01, 0x01, '315度に回転(線形補完回転)', 0x0000006A)
    MenuCmd(0x01, 0x01, '360度にリセット', 0x0000006E)
    MenuCmd(0x01, 0x01, '315度 ⇒ 15度(角度差小さい方に回転)', 0x0000006F)
    MenuCmd(0x01, 0x01, '315度 ⇒ 15度(線形補完回転)', 0x00000070)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000064, 'loc_2C3C9'),
        (0x00000065, 'loc_2C3E4'),
        (0x00000066, 'loc_2C3FF'),
        (0x00000067, 'loc_2C41A'),
        (0x00000068, 'loc_2C435'),
        (0x00000069, 'loc_2C450'),
        (0x0000006A, 'loc_2C46B'),
        (0x0000006E, 'loc_2C486'),
        (0x0000006F, 'loc_2C4A0'),
        (0x00000070, 'loc_2C4D0'),
        (-1, 'loc_2C500'),
    )

    def _loc_2C3C9(): pass

    label('loc_2C3C9')

    CameraRotate(0x03, 0.0, 0.0, 0.0, 1000, 0x01)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C3E4(): pass

    label('loc_2C3E4')

    CameraRotate(0x03, 0.0, 45.0, 0.0, 1000, 0x01)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C3FF(): pass

    label('loc_2C3FF')

    CameraRotate(0x03, 0.0, -45.0, 0.0, 1000, 0x01)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C41A(): pass

    label('loc_2C41A')

    CameraRotate(0x03, 0.0, 315.0, 0.0, 1000, 0x01)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C435(): pass

    label('loc_2C435')

    CameraRotate(0x03, 0.0, 45.0, 0.0, 1000, 0x00)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C450(): pass

    label('loc_2C450')

    CameraRotate(0x03, 0.0, -45.0, 0.0, 1000, 0x00)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C46B(): pass

    label('loc_2C46B')

    CameraRotate(0x03, 0.0, 315.0, 0.0, 1000, 0x00)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C486(): pass

    label('loc_2C486')

    CameraRotate(0x03, 0.0, 360.0, 0.0, 0, 0x01)
    Sleep(1000)

    Jump('loc_2C509')

    def _loc_2C4A0(): pass

    label('loc_2C4A0')

    CameraRotate(0x03, 0.0, 315.0, 0.0, 0, 0x01)
    Sleep(500)

    CameraRotate(0x03, 0.0, 15.0, 0.0, 1000, 0x01)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C4D0(): pass

    label('loc_2C4D0')

    CameraRotate(0x03, 0.0, 315.0, 0.0, 0, 0x01)
    Sleep(500)

    CameraRotate(0x03, 0.0, 15.0, 0.0, 1000, 0x00)
    CameraCtrl(0x07, 0x00BF)

    Jump('loc_2C509')

    def _loc_2C500(): pass

    label('loc_2C500')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C509(): pass

    label('loc_2C509')

    Jump('loc_2C15E')

    def _loc_2C50E(): pass

    label('loc_2C50E')

    Call(ScriptId.System, 'FC_EventEnd', (0xFF, 0x0, 0x0))
    OP_14(0x04000000)

    Return()

# id: 0x00B3 offset: 0x2C52C
@scena.Code('TK_LookCommand_Test')
def TK_LookCommand_Test():
    OP_45(0xF016, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xF016, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xF016, 0xFFFF, 0x0000)

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C563(): pass

    label('loc_2C563')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CCC1',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '上     look_dir(  0.f, 45.f,  0.f )', 0x00000064)
    MenuCmd(0x01, 0x01, '下     look_dir(  0.f,-45.f,  0.f )', 0x00000065)
    MenuCmd(0x01, 0x01, '左     look_dir( 45.f,  0.f,  0.f )', 0x00000066)
    MenuCmd(0x01, 0x01, '右     look_dir(-45.f,  0.f,  0.f )', 0x00000067)
    MenuCmd(0x01, 0x01, '左Roll look_dir(  0.f,  0.f, 45.f )', 0x00000079)
    MenuCmd(0x01, 0x01, '右Roll look_dir(  0.f,  0.f,-45.f )', 0x0000007A)
    MenuCmd(0x01, 0x01, 'リセット', 0x00000078)
    MenuCmd(0x01, 0x01, 'HEAD_YES', 0x00000068)
    MenuCmd(0x01, 0x01, 'HEAD_NO', 0x00000069)
    MenuCmd(0x01, 0x01, '首だけ動く', 0x0000006A)
    MenuCmd(0x01, 0x01, '目だけ動く', 0x0000006B)
    MenuCmd(0x01, 0x01, '目と首の比率戻す', 0x0000006C)
    MenuCmd(0x01, 0x01, 'look_chr(player, キャンプテストさん)', 0x0000006E)
    MenuCmd(0x01, 0x01, 'look_chr(player, キャンプテストさん,0)', 0x0000006F)
    MenuCmd(0x01, 0x01, 'look_chr(player, キャンプテストさん,100)', 0x00000070)
    MenuCmd(0x01, 0x01, 'look_chr(player, null, 4000)', 0x00000071)
    MenuCmd(0x01, 0x01, 'プレイヤー位置を変更', 0x000000C8)
    MenuCmd(0x01, 0x01, '*回転後にアニメテスト(TSPEED_DEF)', 0x0000012C)
    MenuCmd(0x01, 0x01, '*回転後にアニメテスト(TSPEED_SLOW)', 0x0000012D)
    MenuCmd(0x01, 0x01, '*回転後にアニメテスト(TSPEED_VSLOW)', 0x0000012E)
    MenuCmd(0x01, 0x01, 'アニメテスト', 0x0000012F)
    MenuCmd(0x02, 0x01, 0x01, 0x0032, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)
    MenuCmd(0x10, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000064, 'loc_2C981'),
        (0x00000065, 'loc_2C999'),
        (0x00000066, 'loc_2C9B1'),
        (0x00000067, 'loc_2C9C9'),
        (0x00000079, 'loc_2C9E1'),
        (0x0000007A, 'loc_2C9F9'),
        (0x00000078, 'loc_2CA11'),
        (0x00000068, 'loc_2CA44'),
        (0x00000069, 'loc_2CA5E'),
        (0x0000006A, 'loc_2CA77'),
        (0x0000006B, 'loc_2CA89'),
        (0x0000006C, 'loc_2CA9B'),
        (0x0000006E, 'loc_2CAAD'),
        (0x0000006F, 'loc_2CABD'),
        (0x00000070, 'loc_2CACD'),
        (0x00000071, 'loc_2CADD'),
        (0x000000C8, 'loc_2CAED'),
        (0x000000C9, 'loc_2CB09'),
        (0x0000012C, 'loc_2CB25'),
        (0x0000012D, 'loc_2CB94'),
        (0x0000012E, 'loc_2CC03'),
        (0x0000012F, 'loc_2CC72'),
        (-1, 'loc_2CCB3'),
    )

    def _loc_2C981(): pass

    label('loc_2C981')

    OP_45(0xF016, 0.0, 45.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2CCBC')

    def _loc_2C999(): pass

    label('loc_2C999')

    OP_45(0xF016, 0.0, -45.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2CCBC')

    def _loc_2C9B1(): pass

    label('loc_2C9B1')

    OP_45(0xF016, 45.0, 0.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2CCBC')

    def _loc_2C9C9(): pass

    label('loc_2C9C9')

    OP_45(0xF016, -45.0, 0.0, 0.0, 0x012C, 0x0000)

    Jump('loc_2CCBC')

    def _loc_2C9E1(): pass

    label('loc_2C9E1')

    OP_45(0xF016, 0.0, 0.0, 45.0, 0x012C, 0x0000)

    Jump('loc_2CCBC')

    def _loc_2C9F9(): pass

    label('loc_2C9F9')

    OP_45(0xF016, 0.0, 0.0, -45.0, 0x012C, 0x0000)

    Jump('loc_2CCBC')

    def _loc_2CA11(): pass

    label('loc_2CA11')

    OP_45(0xF016, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xF016, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xF016, 0xFFFF, 0x0000)

    Jump('loc_2CCBC')

    def _loc_2CA44(): pass

    label('loc_2CA44')

    CreateThread(0xF016, 0x02, ScriptId.System, 'FC_look_dir_Yes')

    Jump('loc_2CCBC')

    def _loc_2CA5E(): pass

    label('loc_2CA5E')

    CreateThread(0xF016, 0x02, ScriptId.System, 'FC_look_dir_No')

    Jump('loc_2CCBC')

    def _loc_2CA77(): pass

    label('loc_2CA77')

    OP_46(0x03, 0xF016, 0xFFFF, 0x03E8, 0.0, 0x03)

    Jump('loc_2CCBC')

    def _loc_2CA89(): pass

    label('loc_2CA89')

    OP_46(0x03, 0xF016, 0xFFFF, 0x03E8, 1.0, 0x03)

    Jump('loc_2CCBC')

    def _loc_2CA9B(): pass

    label('loc_2CA9B')

    OP_46(0x03, 0xF016, 0xFFFF, 0x01D0, 0.5, 0x03)

    Jump('loc_2CCBC')

    def _loc_2CAAD(): pass

    label('loc_2CAAD')

    OP_46(0x00, 0xF016, 0x03ED, 0x03E8)
    Sleep(500)

    Jump('loc_2CCBC')

    def _loc_2CABD(): pass

    label('loc_2CABD')

    OP_46(0x00, 0xF016, 0x03ED, 0x0000)
    Sleep(500)

    Jump('loc_2CCBC')

    def _loc_2CACD(): pass

    label('loc_2CACD')

    OP_46(0x00, 0xF016, 0x03ED, 0x0064)
    Sleep(2000)

    Jump('loc_2CCBC')

    def _loc_2CADD(): pass

    label('loc_2CADD')

    OP_46(0x00, 0xF016, 0xFFFF, 0x0FA0)
    Sleep(2000)

    Jump('loc_2CCBC')

    def _loc_2CAED(): pass

    label('loc_2CAED')

    ModelCtrl(0x3A, 0xF016, 0x03EB, 0.0, 0.0, 1.0, 180.0, 0x01)

    Jump('loc_2CCBC')

    def _loc_2CB09(): pass

    label('loc_2CB09')

    ModelCtrl(0x3A, 0xF016, 0x03EB, 0.0, 0.0, 1.5, 180.0, 0x01)

    Jump('loc_2CCBC')

    def _loc_2CB25(): pass

    label('loc_2CB25')

    AnimeClipLoadMultiple(0xF016, 0x00, 'AniEvByeWalk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ModelCtrl(0x3A, 0xF016, 0x03EB, 0.0, 0.0, 1.0, 0.0, 0x01)
    Sleep(500)

    OP_3D(0xF016, 180.0, 10.0, 0x00)
    OP_3F(0xF016)
    SetChrAniFunction(0xF016, 0x00, 'AniEvByeWalk', -1.0, 1.0, 0x00000000)
    Sleep(1000)

    Jump('loc_2CCBC')

    def _loc_2CB94(): pass

    label('loc_2CB94')

    AnimeClipLoadMultiple(0xF016, 0x00, 'AniEvByeWalk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ModelCtrl(0x3A, 0xF016, 0x03EB, 0.0, 0.0, 1.0, 0.0, 0x01)
    Sleep(500)

    OP_3D(0xF016, 180.0, 5.0, 0x00)
    OP_3F(0xF016)
    SetChrAniFunction(0xF016, 0x00, 'AniEvByeWalk', -1.0, 1.0, 0x00000000)
    Sleep(1000)

    Jump('loc_2CCBC')

    def _loc_2CC03(): pass

    label('loc_2CC03')

    AnimeClipLoadMultiple(0xF016, 0x00, 'AniEvByeWalk', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ModelCtrl(0x3A, 0xF016, 0x03EB, 0.0, 0.0, 1.0, 0.0, 0x01)
    Sleep(500)

    OP_3D(0xF016, 180.0, 2.5, 0x00)
    OP_3F(0xF016)
    SetChrAniFunction(0xF016, 0x00, 'AniEvByeWalk', -1.0, 1.0, 0x00000000)
    Sleep(1000)

    Jump('loc_2CCBC')

    def _loc_2CC72(): pass

    label('loc_2CC72')

    AnimeClipLoadMultiple(0xF016, 0x00, 'AniEv00040a', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(0xF016, 0x00, 'AniEv00040a', -1.0, 1.0, 0x00000000)

    Jump('loc_2CCBC')

    def _loc_2CCB3(): pass

    label('loc_2CCB3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CCBC(): pass

    label('loc_2CCBC')

    Jump('loc_2C563')

    def _loc_2CCC1(): pass

    label('loc_2CCC1')

    Return()

# id: 0x00B4 offset: 0x2CCC4
@scena.Code('TK_ActiveTodo_Test')
def TK_ActiveTodo_Test():
    Return()

# id: 0x00B5 offset: 0x2CCC8
@scena.Code('TK_VibratePad_Test')
def TK_VibratePad_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CCD1(): pass

    label('loc_2CCD1')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CE44',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '鈍い振動    （左モーターのみ）', 0x00000000)
    MenuCmd(0x01, 0x01, '小刻みな振動（右モーターのみ）', 0x00000001)
    MenuCmd(0x01, 0x01, '銃', 0x00000002)
    MenuCmd(0x01, 0x01, 'ダメージ', 0x00000003)
    MenuCmd(0x01, 0x01, 'パワーアップ', 0x00000004)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_2CDD7'),
        (0x00000001, 'loc_2CDEA'),
        (0x00000002, 'loc_2CDFD'),
        (0x00000003, 'loc_2CE10'),
        (0x00000004, 'loc_2CE23'),
        (-1, 'loc_2CE36'),
    )

    def _loc_2CDD7(): pass

    label('loc_2CDD7')

    OP_3B(0xFF, 0.7, 0.0, 0.2)

    Jump('loc_2CE3F')

    def _loc_2CDEA(): pass

    label('loc_2CDEA')

    OP_3B(0xFF, 0.0, 0.7, 0.2)

    Jump('loc_2CE3F')

    def _loc_2CDFD(): pass

    label('loc_2CDFD')

    OP_3B(0xFF, 0.2, 0.4, 0.1)

    Jump('loc_2CE3F')

    def _loc_2CE10(): pass

    label('loc_2CE10')

    OP_3B(0xFF, 0.4, 0.4, 0.1)

    Jump('loc_2CE3F')

    def _loc_2CE23(): pass

    label('loc_2CE23')

    OP_3B(0xFF, 0.5, 0.5, 0.3)

    Jump('loc_2CE3F')

    def _loc_2CE36(): pass

    label('loc_2CE36')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CE3F(): pass

    label('loc_2CE3F')

    Jump('loc_2CCD1')

    def _loc_2CE44(): pass

    label('loc_2CE44')

    Return()

# id: 0x00B6 offset: 0x2CE48
@scena.Code('TK_StatusUp_Test')
def TK_StatusUp_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CE51(): pass

    label('loc_2CE51')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D11D',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'MaxHP +1000', 0x00000000)
    MenuCmd(0x01, 0x01, 'STR   +100', 0x00000001)
    MenuCmd(0x01, 0x01, 'DEF   +100', 0x00000002)
    MenuCmd(0x01, 0x01, 'ATS   +100', 0x00000003)
    MenuCmd(0x01, 0x01, 'ADF   +100', 0x00000004)
    MenuCmd(0x01, 0x01, 'LEVEL +10 (差分の経験値維持)', 0x00000005)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_2CF45'),
        (0x00000001, 'loc_2CF93'),
        (0x00000002, 'loc_2CFDE'),
        (0x00000003, 'loc_2D029'),
        (0x00000004, 'loc_2D074'),
        (0x00000005, 'loc_2D0BF'),
        (-1, 'loc_2D10F'),
    )

    def _loc_2CF45(): pass

    label('loc_2CF45')

    OP_48(0x00, 0x0000, 0x0064, 0x03E8)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'リィンのMaxHPが#3C1000#2C上がった！',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2D118')

    def _loc_2CF93(): pass

    label('loc_2CF93')

    OP_48(0x00, 0x0000, 0x0065, 0x0064)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'リィンのSTRが#3C100#2C上がった！',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2D118')

    def _loc_2CFDE(): pass

    label('loc_2CFDE')

    OP_48(0x00, 0x0000, 0x0066, 0x0064)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'リィンのDEFが#3C100#2C上がった！',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2D118')

    def _loc_2D029(): pass

    label('loc_2D029')

    OP_48(0x00, 0x0000, 0x0067, 0x0064)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'リィンのATSが#3C100#2C上がった！',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2D118')

    def _loc_2D074(): pass

    label('loc_2D074')

    OP_48(0x00, 0x0000, 0x0068, 0x0064)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'リィンのDEFが#3C100#2C上がった！',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2D118')

    def _loc_2D0BF(): pass

    label('loc_2D0BF')

    OP_48(0x00, 0x0000, 0x0002, 0x000A)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'リィンのレベルが#3C10#2C上がった！',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_2D118')

    def _loc_2D10F(): pass

    label('loc_2D10F')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D118(): pass

    label('loc_2D118')

    Jump('loc_2CE51')

    def _loc_2D11D(): pass

    label('loc_2D11D')

    Return()

# id: 0x00B7 offset: 0x2D120
@scena.Code('TK_ChapterSave_Test')
def TK_ChapterSave_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D129(): pass

    label('loc_2D129')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D558',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '章間セーブ', 0x00000000)
    MenuCmd(0x01, 0x01, 'クリアセーブ', 0x00000001)
    MenuCmd(0x01, 0x01, 'set_system_save_flag(SF4_TEST)', 0x00000002)
    MenuCmd(0x01, 0x01, 'reset_system_save_flag(SF4_TEST)', 0x00000003)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_2D205'),
        (0x00000001, 'loc_2D2D3'),
        (0x00000002, 'loc_2D4A5'),
        (0x00000003, 'loc_2D4F7'),
        (-1, 'loc_2D54A'),
    )

    def _loc_2D205(): pass

    label('loc_2D205')

    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_55(0x00, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0400, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_VIS1000', '')
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 500.0)
    OP_57(0x00, 0x03)
    Sleep(0)

    OP_AF(0x00)
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    OP_90('current', 0x00000014)
    OP_93(0x00, 0x00)
    OP_93(0x01)
    ClearScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    ClearScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    OP_AF(0x01)
    OP_43(0x00, 0x0000, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 500.0)
    OP_57(0x00, 0x03)
    OP_58(0xFF)
    SetScenaFlags(ScenaFlag(0x052F, 7, 0x297F))

    OP_18(
        0x03,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    Jump('loc_2D553')

    def _loc_2D2D3(): pass

    label('loc_2D2D3')

    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_55(0x00, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0400, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_VIS1000', '')
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 500.0)
    OP_57(0x00, 0x03)
    OP_23(0x05, 0xFFFF, 0x00DC, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '　　　 ～　クリアデータのセーブについて　～\n',
            'クリアデータを作成し、タイトル画面からロードすると\n',
            '各種データを引き継いだまま２周目を開始できます。',
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)

    Sleep(0)

    OP_AF(0x00)
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    OP_90('current', 0x0000001C)
    OP_93(0x00, 0x02)
    OP_93(0x01)
    ClearScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    ClearScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    OP_AF(0x01)
    OP_25(0x00)
    OP_43(0x00, 0x0000, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 500.0)
    OP_57(0x00, 0x03)
    OP_58(0xFF)
    Call(ScriptId.System, 'FC_EventEndMapChange', (0xDD, 'title'), (0xDD, ''))
    OP_14(0x04000000)

    Jump('loc_2D553')

    def _loc_2D4A5(): pass

    label('loc_2D4A5')

    OP_19(0x00, 0x0001)

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0001)"),
            Expr.Return,
        ),
        'loc_2D4F2',
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'システムセーブフラグを立てた',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    def _loc_2D4F2(): pass

    label('loc_2D4F2')

    Jump('loc_2D553')

    def _loc_2D4F7(): pass

    label('loc_2D4F7')

    OP_19(0x01, 0x0001)

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0001)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D545',
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'システムセーブフラグを下した',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    def _loc_2D545(): pass

    label('loc_2D545')

    Jump('loc_2D553')

    def _loc_2D54A(): pass

    label('loc_2D54A')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D553(): pass

    label('loc_2D553')

    Jump('loc_2D129')

    def _loc_2D558(): pass

    label('loc_2D558')

    Return()

# id: 0x00B8 offset: 0x2D55C
@scena.Code('EV_Test_Evsave_Load')
def EV_Test_Evsave_Load():
    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_43(0x00, 0x0000, 1.0, 0x0000)
    FormationCtrl(0x07)
    OP_3A(0x04, 0x0002, 1.0, 0x0000, 0x00000000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    OP_AF(0x01)
    ClearScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x052F, 7, 0x297F))

    OP_18(
        0x03,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3A(0x05, 0x0001, 0x0001)
    OP_3A(0x06, 0x0001)

    Return()

# id: 0x00B9 offset: 0x2D5B0
@scena.Code('TK_GetSCraft_Test')
def TK_GetSCraft_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D5B9(): pass

    label('loc_2D5B9')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D68F',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, 'クラフトクリア', 0x00000000)
    MenuCmd(0x01, 0x00, 'SC：七之太刀・落叶', 0x00000001)
    MenuCmd(0x01, 0x00, 'SC：七之太刀·刻叶', 0x00000002)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x00, 0xF7)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_2D66E'),
        (0x00000001, 'loc_2D677'),
        (0x00000002, 'loc_2D67C'),
        (-1, 'loc_2D681'),
    )

    def _loc_2D66E(): pass

    label('loc_2D66E')

    CraftCtrl(0x03, 0x0000)

    Jump('loc_2D68A')

    def _loc_2D677(): pass

    label('loc_2D677')

    Jump('loc_2D68A')

    def _loc_2D67C(): pass

    label('loc_2D67C')

    Jump('loc_2D68A')

    def _loc_2D681(): pass

    label('loc_2D681')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D68A(): pass

    label('loc_2D68A')

    Jump('loc_2D5B9')

    def _loc_2D68F(): pass

    label('loc_2D68F')

    Return()

# id: 0x00BA offset: 0x2D690
@scena.Code('TK_Title_Test')
def TK_Title_Test():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D699(): pass

    label('loc_2D699')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DCE9',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x000A, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'ゲーム開始時', 0x00000000)
    MenuCmd(0x01, 0x01, 'Ⅰ部①', 0x00000001)
    MenuCmd(0x01, 0x01, 'Ⅰ部②', 0x00000002)
    MenuCmd(0x01, 0x01, 'Ⅰ部③', 0x00000003)
    MenuCmd(0x01, 0x01, '断章前半', 0x00000004)
    MenuCmd(0x01, 0x01, '断章後半', 0x00000005)
    MenuCmd(0x01, 0x01, 'Ⅱ部前半', 0x00000006)
    MenuCmd(0x01, 0x01, 'Ⅱ部後半', 0x00000007)
    MenuCmd(0x01, 0x01, 'Ⅱ部パンタグリュエル編', 0x00000008)
    MenuCmd(0x01, 0x01, 'Ⅲ部', 0x00000009)
    MenuCmd(0x01, 0x01, '前日譚', 0x0000000A)
    MenuCmd(0x01, 0x01, '最終幕', 0x0000000B)
    MenuCmd(0x01, 0x01, 'クリア直後', 0x0000000C)
    MenuCmd(0x01, 0x01, 'クリアした', 0x0000000D)
    MenuCmd(0x01, 0x01, 'Ⅱ部アリサ・エマ', 0x0000000E)
    MenuCmd(0x01, 0x01, 'Ⅱ部エリオット・ガイウス', 0x0000000F)
    MenuCmd(0x01, 0x01, 'Ⅱ部フィー・ラウラ', 0x00000010)
    MenuCmd(0x01, 0x01, 'Ⅱ部ユーシス・マキアス', 0x00000011)
    MenuCmd(0x01, 0x01, 'Ⅱ部リィン・クロウ', 0x00000012)
    MenuCmd(0x01, 0x01, 'Ⅲ部クロスベル組', 0x00000013)
    MenuCmd(0x01, 0x01, 'Ⅲ部エリゼ・アルフィン・トワ', 0x00000014)
    MenuCmd(0x01, 0x01, 'Ⅲ部リベール組', 0x00000015)
    MenuCmd(0x01, 0x01, 'Ⅲ部結社', 0x00000016)
    MenuCmd(0x01, 0x01, 'Ⅲ部遊撃士', 0x00000017)
    MenuCmd(0x01, 0x01, 'Ⅲ部魔女', 0x00000018)
    MenuCmd(0x01, 0x01, 'Ⅲ部軌跡主人公s', 0x00000019)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_2DA51'),
        (0x00000001, 'loc_2DA6A'),
        (0x00000002, 'loc_2DA83'),
        (0x00000003, 'loc_2DA9C'),
        (0x00000004, 'loc_2DAB5'),
        (0x00000005, 'loc_2DACE'),
        (0x00000006, 'loc_2DAE7'),
        (0x00000007, 'loc_2DB00'),
        (0x00000008, 'loc_2DB19'),
        (0x00000009, 'loc_2DB32'),
        (0x0000000A, 'loc_2DB4B'),
        (0x0000000B, 'loc_2DB64'),
        (0x0000000C, 'loc_2DB7D'),
        (0x0000000D, 'loc_2DB96'),
        (0x0000000E, 'loc_2DBAF'),
        (0x0000000F, 'loc_2DBC8'),
        (0x00000010, 'loc_2DBE1'),
        (0x00000011, 'loc_2DBFA'),
        (0x00000012, 'loc_2DC13'),
        (0x00000013, 'loc_2DC2C'),
        (0x00000014, 'loc_2DC45'),
        (0x00000015, 'loc_2DC5E'),
        (0x00000016, 'loc_2DC77'),
        (0x00000017, 'loc_2DC90'),
        (0x00000018, 'loc_2DCA9'),
        (0x00000019, 'loc_2DCC2'),
        (-1, 'loc_2DCDB'),
    )

    def _loc_2DA51(): pass

    label('loc_2DA51')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DA6A(): pass

    label('loc_2DA6A')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DA83(): pass

    label('loc_2DA83')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DA9C(): pass

    label('loc_2DA9C')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DAB5(): pass

    label('loc_2DAB5')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DACE(): pass

    label('loc_2DACE')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DAE7(): pass

    label('loc_2DAE7')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DB00(): pass

    label('loc_2DB00')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DB19(): pass

    label('loc_2DB19')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DB32(): pass

    label('loc_2DB32')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DB4B(): pass

    label('loc_2DB4B')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DB64(): pass

    label('loc_2DB64')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DB7D(): pass

    label('loc_2DB7D')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DB96(): pass

    label('loc_2DB96')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DBAF(): pass

    label('loc_2DBAF')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DBC8(): pass

    label('loc_2DBC8')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DBE1(): pass

    label('loc_2DBE1')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DBFA(): pass

    label('loc_2DBFA')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DC13(): pass

    label('loc_2DC13')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x12),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DC2C(): pass

    label('loc_2DC2C')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x13),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DC45(): pass

    label('loc_2DC45')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x14),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DC5E(): pass

    label('loc_2DC5E')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x15),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DC77(): pass

    label('loc_2DC77')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x16),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DC90(): pass

    label('loc_2DC90')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x17),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DCA9(): pass

    label('loc_2DCA9')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DCC2(): pass

    label('loc_2DCC2')

    OP_08(
        0x09,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_2DCE4')

    def _loc_2DCDB(): pass

    label('loc_2DCDB')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2DCE4(): pass

    label('loc_2DCE4')

    Jump('loc_2D699')

    def _loc_2DCE9(): pass

    label('loc_2DCE9')

    Return()

# id: 0x00BB offset: 0x2DCEC
@scena.Code('TK_MiniGame_Debug_CardGame')
def TK_MiniGame_Debug_CardGame():
    Call(ScriptId.System4, 'FC_CardGame_joshua')

    Return()

# id: 0x00BC offset: 0x2DD04
@scena.Code('TK_MiniGame_Debug')
def TK_MiniGame_Debug():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2DD29(): pass

    label('loc_2DD29')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EEDF',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '迷你游戏01（钓鱼）', 0x00000001)
    MenuCmd(0x01, 0x00, '迷你游戏07', 0x00000007)
    MenuCmd(0x01, 0x00, '迷你游戏08', 0x00000008)
    MenuCmd(0x01, 0x00, '迷你游戏09（黑杰克）', 0x00000009)
    MenuCmd(0x01, 0x00, '迷你游戏10（扑克）', 0x0000000A)
    MenuCmd(0x01, 0x00, '迷你游戏11（恐怖过山车羁绊）', 0x0000000B)
    MenuCmd(0x01, 0x00, '迷你游戏11（恐怖过山车）', 0x0000000C)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000001, 'loc_2DE97'),
        (0x00000003, 'loc_2E88D'),
        (0x00000007, 'loc_2E8AA'),
        (0x00000008, 'loc_2EDC5'),
        (0x00000009, 'loc_2EDF3'),
        (0x0000000A, 'loc_2EE2C'),
        (0x0000000B, 'loc_2EE65'),
        (0x0000000C, 'loc_2EEA9'),
        (-1, 'loc_2EECC'),
    )

    def _loc_2DE97(): pass

    label('loc_2DE97')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['悠娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['妙婕'])
    FormationAddMember(ChrTable['亞修'])
    FormationSetLeader(ChrTable['黎恩'])

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 't5000　\x09エリン\x09\x09\x09\x09\x09\x09', 0x00000000)
    MenuCmd(0x01, 0x01, 'm0600　\x09大森林\x09\x09\x09\x09\x09\x09', 0x00000001)
    MenuCmd(0x01, 0x01, 'r0000　\x09南街道①\x09\x09\x09\x09\x09', 0x00000002)
    MenuCmd(0x01, 0x01, 'r0010　\x09南街道②\x09\x09\x09\x09\x09', 0x00000003)
    MenuCmd(0x01, 0x01, 't2000　\x09紡績町パルム\x09\x09\x09\x09', 0x00000004)
    MenuCmd(0x01, 0x01, 'r1000　\x09アグリア旧道\x09\x09\x09\x09', 0x00000005)
    MenuCmd(0x01, 0x01, 'r1200　\x09パルム間道①\x09\x09\x09\x09', 0x00000006)
    MenuCmd(0x01, 0x01, 'r1210　\x09パルム間道②\x09\x09\x09\x09', 0x00000007)
    MenuCmd(0x01, 0x01, 'r1400　\x09ハーメル廃道①\x09\x09\x09\x09', 0x00000008)
    MenuCmd(0x01, 0x01, 'r1410　\x09ハーメル廃道②\x09\x09\x09\x09', 0x00000009)
    MenuCmd(0x01, 0x01, 'm0630　\x09魔の森Ｃ\x09\x09\x09\x09\x09', 0x0000000A)
    MenuCmd(0x01, 0x01, 'r5200　\x09ガラ湖周遊道・前半\x09\x09\x09', 0x0000000B)
    MenuCmd(0x01, 0x01, 'r3450　\x09北ラングドック峡谷道②\x09\x09', 0x0000000C)
    MenuCmd(0x01, 0x01, 'r7000　\x09ラマール旧道①\x09\x09\x09\x09', 0x0000000D)
    MenuCmd(0x01, 0x01, 'r2420　\x09東クロスベル街道③\x09\x09\x09', 0x0000000E)
    MenuCmd(0x01, 0x01, 'r2410　\x09東クロスベル街道②\x09\x09\x09', 0x0000000F)
    MenuCmd(0x01, 0x01, 'c0800　\x09クロスベル港湾区\x09\x09\x09', 0x00000010)
    MenuCmd(0x01, 0x01, 'r2200　\x09ウルスラ間道①\x09\x09\x09\x09', 0x00000011)
    MenuCmd(0x01, 0x01, 'r2210　\x09ウルスラ間道②\x09\x09\x09\x09', 0x00000012)
    MenuCmd(0x01, 0x01, 'r2220　\x09ウルスラ間道③\x09\x09\x09\x09', 0x00000013)
    MenuCmd(0x01, 0x01, 'f4000　\x09ミシュラム(波止場orビーチ)\x09', 0x00000014)
    MenuCmd(0x01, 0x01, 'r2610　\x09湿地帯②\x09\x09\x09\x09\x09', 0x00000015)
    MenuCmd(0x01, 0x01, 'r3600　\x09ブリオニア島浜辺\x09\x09\x09', 0x00000016)
    MenuCmd(0x01, 0x01, 'r3600　\x09ブリオニア島滝前\x09\x09\x09', 0x00000017)
    MenuCmd(0x01, 0x01, 'r3600　\x09ブリオニア島埠頭\x09\x09\x09', 0x00000018)
    MenuCmd(0x01, 0x01, 't3600　\x09オルディス港湾区\x09\x09\x09', 0x00000019)
    MenuCmd(0x01, 0x01, 'm6500　\x09海都地下水道？\x09\x09\x09\x09', 0x0000001A)
    MenuCmd(0x01, 0x01, 'r0210　\x09北サザーラント街道②\x09\x09', 0x0000001B)
    MenuCmd(0x01, 0x01, 'r5200　\x09ガラ湖周遊道・後半\x09\x09\x09', 0x0000001C)
    MenuCmd(0x01, 0x01, 't0000　\x09リーヴスの川\x09\x09\x09\x09', 0x0000001D)
    MenuCmd(0x01, 0x01, 'r3200　\x09アウロス海岸道①浜辺\x09\x09', 0x0000001E)
    MenuCmd(0x01, 0x01, 'r3210　\x09アウロス海岸道②浜辺\x09\x09', 0x0000001F)
    MenuCmd(0x01, 0x01, 'r6000　\x09エイボン丘陵・後半？\x09\x09', 0x00000020)
    MenuCmd(0x01, 0x01, 'r2600　\x09湿地帯①\x09\x09\x09\x09\x09', 0x00000021)
    MenuCmd(0x01, 0x01, 'f4200　\x09ミシュラムビーチ(ヌシ用)\x09', 0x00000022)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_2E5CC'),
        (0x00000001, 'loc_2E5E0'),
        (0x00000002, 'loc_2E5F4'),
        (0x00000003, 'loc_2E608'),
        (0x00000004, 'loc_2E61C'),
        (0x00000005, 'loc_2E630'),
        (0x00000006, 'loc_2E644'),
        (0x00000007, 'loc_2E658'),
        (0x00000008, 'loc_2E66C'),
        (0x00000009, 'loc_2E680'),
        (0x0000000A, 'loc_2E694'),
        (0x0000000B, 'loc_2E6A8'),
        (0x0000000C, 'loc_2E6BC'),
        (0x0000000D, 'loc_2E6D0'),
        (0x0000000E, 'loc_2E6E4'),
        (0x0000000F, 'loc_2E6F8'),
        (0x00000010, 'loc_2E70C'),
        (0x00000011, 'loc_2E720'),
        (0x00000012, 'loc_2E734'),
        (0x00000013, 'loc_2E748'),
        (0x00000014, 'loc_2E75C'),
        (0x00000015, 'loc_2E770'),
        (0x00000016, 'loc_2E784'),
        (0x00000017, 'loc_2E798'),
        (0x00000018, 'loc_2E7AC'),
        (0x00000019, 'loc_2E7C0'),
        (0x0000001A, 'loc_2E7D4'),
        (0x0000001B, 'loc_2E7E8'),
        (0x0000001C, 'loc_2E7FC'),
        (0x0000001D, 'loc_2E810'),
        (0x0000001E, 'loc_2E824'),
        (0x0000001F, 'loc_2E838'),
        (0x00000020, 'loc_2E84C'),
        (0x00000021, 'loc_2E860'),
        (0x00000022, 'loc_2E874'),
        (-1, 'loc_2E888'),
    )

    def _loc_2E5CC(): pass

    label('loc_2E5CC')

    OP_28((0xDD, 't5000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E5E0(): pass

    label('loc_2E5E0')

    OP_28((0xDD, 'm0600'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E5F4(): pass

    label('loc_2E5F4')

    OP_28((0xDD, 'r0000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E608(): pass

    label('loc_2E608')

    OP_28((0xDD, 'r0010'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E61C(): pass

    label('loc_2E61C')

    OP_28((0xDD, 't2000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E630(): pass

    label('loc_2E630')

    OP_28((0xDD, 'r1000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E644(): pass

    label('loc_2E644')

    OP_28((0xDD, 'r1200'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E658(): pass

    label('loc_2E658')

    OP_28((0xDD, 'r1210'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E66C(): pass

    label('loc_2E66C')

    OP_28((0xDD, 'r1400'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E680(): pass

    label('loc_2E680')

    OP_28((0xDD, 'r1410'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E694(): pass

    label('loc_2E694')

    OP_28((0xDD, 'm0630'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E6A8(): pass

    label('loc_2E6A8')

    OP_28((0xDD, 'r5200'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E6BC(): pass

    label('loc_2E6BC')

    OP_28((0xDD, 'r3450'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E6D0(): pass

    label('loc_2E6D0')

    OP_28((0xDD, 'r7000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E6E4(): pass

    label('loc_2E6E4')

    OP_28((0xDD, 'r2420'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E6F8(): pass

    label('loc_2E6F8')

    OP_28((0xDD, 'r2410'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E70C(): pass

    label('loc_2E70C')

    OP_28((0xDD, 'c0800'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E720(): pass

    label('loc_2E720')

    OP_28((0xDD, 'r2200'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E734(): pass

    label('loc_2E734')

    OP_28((0xDD, 'r2210'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E748(): pass

    label('loc_2E748')

    OP_28((0xDD, 'r2220'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E75C(): pass

    label('loc_2E75C')

    OP_28((0xDD, 'f4000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E770(): pass

    label('loc_2E770')

    OP_28((0xDD, 'r2610'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E784(): pass

    label('loc_2E784')

    OP_28((0xDD, 'r3600'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E798(): pass

    label('loc_2E798')

    OP_28((0xDD, 'r3600'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E7AC(): pass

    label('loc_2E7AC')

    OP_28((0xDD, 'r3600'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E7C0(): pass

    label('loc_2E7C0')

    OP_28((0xDD, 't3600'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E7D4(): pass

    label('loc_2E7D4')

    OP_28((0xDD, 'm6500'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E7E8(): pass

    label('loc_2E7E8')

    OP_28((0xDD, 'r0210'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E7FC(): pass

    label('loc_2E7FC')

    OP_28((0xDD, 'r5200'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E810(): pass

    label('loc_2E810')

    OP_28((0xDD, 't0000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E824(): pass

    label('loc_2E824')

    OP_28((0xDD, 'r3200'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E838(): pass

    label('loc_2E838')

    OP_28((0xDD, 'r3210'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E84C(): pass

    label('loc_2E84C')

    OP_28((0xDD, 'r6000'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E860(): pass

    label('loc_2E860')

    OP_28((0xDD, 'r2600'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E874(): pass

    label('loc_2E874')

    OP_28((0xDD, 'f4200'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2E888')

    def _loc_2E888(): pass

    label('loc_2E888')

    Jump('loc_2EEDA')

    def _loc_2E88D(): pass

    label('loc_2E88D')

    OP_18(
        0x24,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'c3210'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2EEDA')

    def _loc_2E8AA(): pass

    label('loc_2E8AA')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E8B3(): pass

    label('loc_2E8B3')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EDB7',
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'ゲーム起動', 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0588, 7, 0x2C47)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'アークスに登録', 0x00000001, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x01, '対戦相手のオン・オフ', 0x00000002)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_2E96D'),
        (0x00000001, 'loc_2E9A4'),
        (0x00000002, 'loc_2E9AF'),
        (-1, 'loc_2EDA3'),
    )

    def _loc_2E96D(): pass

    label('loc_2E96D')

    OP_43(0x00, 0x012C, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)
    ModelCtrl(0x6B, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Jump('loc_2EDB2')

    def _loc_2E9A4(): pass

    label('loc_2E9A4')

    OP_12(0x2C47)
    SetScenaFlags(ScenaFlag(0x0073, 2, 0x39A))

    Jump('loc_2EDB2')

    def _loc_2E9AF(): pass

    label('loc_2E9AF')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E9B8(): pass

    label('loc_2E9B8')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2ED9E',
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 0, 0x5FA0)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ヨナ', 0x00000000, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 1, 0x5FA1)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'エステル', 0x00000001, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 2, 0x5FA2)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'マキアス', 0x00000002, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 3, 0x5FA3)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ユウナ', 0x00000003, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 4, 0x5FA4)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'クルト', 0x00000004, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 5, 0x5FA5)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'エリィ', 0x00000005, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 6, 0x5FA6)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'アッシュ', 0x00000006, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF4, 7, 0x5FA7)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'クローゼ', 0x00000007, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 0, 0x5FA8)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'エマ', 0x00000008, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 1, 0x5FA9)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ティータ', 0x00000009, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 2, 0x5FAA)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ガイウス', 0x0000000A, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 3, 0x5FAB)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'アルティナ', 0x0000000B, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 4, 0x5FAC)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'オリビエ', 0x0000000C, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 5, 0x5FAD)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'レン', 0x0000000D, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 6, 0x5FAE)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ミュゼ', 0x0000000E, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0BF5, 7, 0x5FAF)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'ティオ', 0x0000000F, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x02, '全員', 0x00000010)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000000, 'loc_2ECD5'),
        (0x00000001, 'loc_2ECDD'),
        (0x00000002, 'loc_2ECE5'),
        (0x00000003, 'loc_2ECED'),
        (0x00000004, 'loc_2ECF5'),
        (0x00000005, 'loc_2ECFD'),
        (0x00000006, 'loc_2ED05'),
        (0x00000007, 'loc_2ED0D'),
        (0x00000008, 'loc_2ED15'),
        (0x00000009, 'loc_2ED1D'),
        (0x0000000A, 'loc_2ED25'),
        (0x0000000B, 'loc_2ED2D'),
        (0x0000000C, 'loc_2ED35'),
        (0x0000000D, 'loc_2ED3D'),
        (0x0000000E, 'loc_2ED45'),
        (0x0000000F, 'loc_2ED4D'),
        (0x00000010, 'loc_2ED55'),
        (-1, 'loc_2ED8A'),
    )

    def _loc_2ECD5(): pass

    label('loc_2ECD5')

    OP_12(0x5FA0)

    Jump('loc_2ED99')

    def _loc_2ECDD(): pass

    label('loc_2ECDD')

    OP_12(0x5FA1)

    Jump('loc_2ED99')

    def _loc_2ECE5(): pass

    label('loc_2ECE5')

    OP_12(0x5FA2)

    Jump('loc_2ED99')

    def _loc_2ECED(): pass

    label('loc_2ECED')

    OP_12(0x5FA3)

    Jump('loc_2ED99')

    def _loc_2ECF5(): pass

    label('loc_2ECF5')

    OP_12(0x5FA4)

    Jump('loc_2ED99')

    def _loc_2ECFD(): pass

    label('loc_2ECFD')

    OP_12(0x5FA5)

    Jump('loc_2ED99')

    def _loc_2ED05(): pass

    label('loc_2ED05')

    OP_12(0x5FA6)

    Jump('loc_2ED99')

    def _loc_2ED0D(): pass

    label('loc_2ED0D')

    OP_12(0x5FA7)

    Jump('loc_2ED99')

    def _loc_2ED15(): pass

    label('loc_2ED15')

    OP_12(0x5FA8)

    Jump('loc_2ED99')

    def _loc_2ED1D(): pass

    label('loc_2ED1D')

    OP_12(0x5FA9)

    Jump('loc_2ED99')

    def _loc_2ED25(): pass

    label('loc_2ED25')

    OP_12(0x5FAA)

    Jump('loc_2ED99')

    def _loc_2ED2D(): pass

    label('loc_2ED2D')

    OP_12(0x5FAB)

    Jump('loc_2ED99')

    def _loc_2ED35(): pass

    label('loc_2ED35')

    OP_12(0x5FAC)

    Jump('loc_2ED99')

    def _loc_2ED3D(): pass

    label('loc_2ED3D')

    OP_12(0x5FAD)

    Jump('loc_2ED99')

    def _loc_2ED45(): pass

    label('loc_2ED45')

    OP_12(0x5FAE)

    Jump('loc_2ED99')

    def _loc_2ED4D(): pass

    label('loc_2ED4D')

    OP_12(0x5FAF)

    Jump('loc_2ED99')

    def _loc_2ED55(): pass

    label('loc_2ED55')

    OP_12(0x5FA0)
    OP_12(0x5FA1)
    OP_12(0x5FA2)
    OP_12(0x5FA3)
    OP_12(0x5FA4)
    OP_12(0x5FA5)
    OP_12(0x5FA6)
    OP_12(0x5FA7)
    OP_12(0x5FA8)
    OP_12(0x5FA9)
    OP_12(0x5FAA)
    OP_12(0x5FAB)
    OP_12(0x5FAC)
    OP_12(0x5FAD)
    OP_12(0x5FAE)
    OP_12(0x5FAF)

    Jump('loc_2ED99')

    def _loc_2ED8A(): pass

    label('loc_2ED8A')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2ED99')

    def _loc_2ED99(): pass

    label('loc_2ED99')

    Jump('loc_2E9B8')

    def _loc_2ED9E(): pass

    label('loc_2ED9E')

    Jump('loc_2EDB2')

    def _loc_2EDA3(): pass

    label('loc_2EDA3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2EDB2')

    def _loc_2EDB2(): pass

    label('loc_2EDB2')

    Jump('loc_2E8B3')

    def _loc_2EDB7(): pass

    label('loc_2EDB7')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2EEDA')

    def _loc_2EDC5(): pass

    label('loc_2EDC5')

    Call(ScriptId.Current, 'TK_MiniGame_Debug_Mg08_Start')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2EEDA')

    def _loc_2EDF3(): pass

    label('loc_2EDF3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    OP_28((0xDD, 't4060'), (0xFF, 0x0, 0x0), 0x00)

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2EEDA')

    def _loc_2EE2C(): pass

    label('loc_2EE2C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x6006),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Debug, 'EV_DoJumpSet_04')
    OP_28((0xDD, 'c1220'), (0xFF, 0x0, 0x0), 0x00)

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2EEDA')

    def _loc_2EE65(): pass

    label('loc_2EE65')

    OP_18(
        0x25,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Expr23, 0x25),
            (Expr.PushLong, 0x8),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2EE8C',
    )

    OP_18(
        0x25,
        (
            (Expr.PushLong, 0x8),
            Expr.Not,
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_2EE8C(): pass

    label('loc_2EE8C')

    OP_18(
        0x25,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'f4460'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2EEDA')

    def _loc_2EEA9(): pass

    label('loc_2EEA9')

    OP_18(
        0x25,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_28((0xDD, 'f4460'), (0xFF, 0x0, 0x0), 0x00)

    Jump('loc_2EEDA')

    def _loc_2EECC(): pass

    label('loc_2EECC')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2EEDA')

    def _loc_2EEDA(): pass

    label('loc_2EEDA')

    Jump('loc_2DD29')

    def _loc_2EEDF(): pass

    label('loc_2EEDF')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))

    Return()

# id: 0x00BD offset: 0x2EEF4
@scena.Code('TK_MiniGame_Debug_Mg08_Start')
def TK_MiniGame_Debug_Mg08_Start():
    OP_18(
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x21,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "AddItem(0x02, 0x0870, 1)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EF43',
    )

    Call(ScriptId.Current, 'TK_MiniGame_Debug_Mg08_Cardset', (0xFF, 0x0, 0x0))

    def _loc_2EF43(): pass

    label('loc_2EF43')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2EF4D(): pass

    label('loc_2EF4D')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F42E',
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '対戦開始（相手を選択）', 0x00000006)
    MenuCmd(0x01, 0x01, '全部カードを入手', 0x00000003)
    MenuCmd(0x01, 0x01, '初期カードにする', 0x00000004)
    MenuCmd(0x01, 0x01, 'チュートリアル', 0x00000002)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000003, 'loc_2F037'),
        (0x00000004, 'loc_2F123'),
        (0x00000006, 'loc_2F20F'),
        (0x00000000, 'loc_2F23D'),
        (0x00000001, 'loc_2F247'),
        (0x00000002, 'loc_2F32E'),
        (-1, 'loc_2F420'),
    )

    def _loc_2F037(): pass

    label('loc_2F037')

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_3B(0x00, (0xFF, 0x88BA, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Talk(
        0xFFFF,
        (
            '全部カードを入手しました。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    Call(ScriptId.Current, 'TK_MiniGame_Debug_Mg08_Cardset', (0xFF, 0x2, 0x0))
    Call(ScriptId.Current, 'TK_MiniGame_Debug_Mg08_Cardset', (0xFF, 0x1, 0x0))

    Jump('loc_2F429')

    def _loc_2F123(): pass

    label('loc_2F123')

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    OP_3B(0x00, (0xFF, 0x88BA, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Talk(
        0xFFFF,
        (
            '初期カードを入手しました。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    Call(ScriptId.Current, 'TK_MiniGame_Debug_Mg08_Cardset', (0xFF, 0x2, 0x0))
    Call(ScriptId.Current, 'TK_MiniGame_Debug_Mg08_Cardset', (0xFF, 0x0, 0x0))

    Jump('loc_2F429')

    def _loc_2F20F(): pass

    label('loc_2F20F')

    Call(ScriptId.Current, 'TK_MiniGame_Debug_Mg08_Enemy')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2F429')

    def _loc_2F23D(): pass

    label('loc_2F23D')

    OP_9E(0x0F, 0x00)
    OP_9E(0x10)

    Jump('loc_2F429')

    def _loc_2F247(): pass

    label('loc_2F247')

    OP_9E(0x0F, 0x01)
    OP_9E(0x10)

    If(
        (
            (Expr.Expr23, 0x20),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F329',
    )

    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_43(0x00, 0x012C, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)
    ModelCtrl(0x6C, 0x0000009C, 0x00000000, 0x00000021, 0x00000022, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_43(0x64, 0x012C, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)

    If(
        (
            (Expr.Expr23, 0x21),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F2D9',
    )

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            'かち',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_2F320')

    def _loc_2F2D9(): pass

    label('loc_2F2D9')

    If(
        (
            (Expr.Expr23, 0x21),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F2FC',
    )

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            'まけ',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_2F320')

    def _loc_2F2FC(): pass

    label('loc_2F2FC')

    If(
        (
            (Expr.Expr23, 0x21),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F320',
    )

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            'ひきわけ',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    def _loc_2F320(): pass

    label('loc_2F320')

    OP_18(
        0x21,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2F329(): pass

    label('loc_2F329')

    Jump('loc_2F429')

    def _loc_2F32E(): pass

    label('loc_2F32E')

    Call(ScriptId.System4, 'FC_CardGameResetTutorialFlags')
    OP_9E(0x12, 0x00, 0x00)
    OP_9E(0x0F, 0x01)
    OP_9E(0x10)

    If(
        (
            (Expr.Expr23, 0x20),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F41B',
    )

    OP_43(0x00, 0x012C, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)
    ModelCtrl(0x6C, 0x0000009C, 0x00000000, 0x00000021, 0x00000022, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_43(0x64, 0x012C, 1.0, 0x0000)
    OP_43(0xFF, 0x0000, 0x0000)

    If(
        (
            (Expr.Expr23, 0x21),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F3CB',
    )

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            'かち',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_2F412')

    def _loc_2F3CB(): pass

    label('loc_2F3CB')

    If(
        (
            (Expr.Expr23, 0x21),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F3EE',
    )

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            'まけ',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_2F412')

    def _loc_2F3EE(): pass

    label('loc_2F3EE')

    If(
        (
            (Expr.Expr23, 0x21),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F412',
    )

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            'ひきわけ',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    def _loc_2F412(): pass

    label('loc_2F412')

    OP_18(
        0x21,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2F41B(): pass

    label('loc_2F41B')

    Jump('loc_2F429')

    def _loc_2F420(): pass

    label('loc_2F420')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2F429(): pass

    label('loc_2F429')

    Jump('loc_2EF4D')

    def _loc_2F42E(): pass

    label('loc_2F42E')

    Return()

# id: 0x00BE offset: 0x2F430
@scena.Code('TK_MiniGame_Debug_Mg08_Enemy')
def TK_MiniGame_Debug_Mg08_Enemy():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0018, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '・パブロ', 0x00000190)
    MenuCmd(0x01, 0x01, '・★エリオット', 0x00000191)
    MenuCmd(0x01, 0x01, '・シスター・ｵﾙﾌｧ', 0x00000192)
    MenuCmd(0x01, 0x01, '・ティーリア', 0x00000193)
    MenuCmd(0x01, 0x01, '・★フィー', 0x000001A0)
    MenuCmd(0x01, 0x01, '・サンサン', 0x00000195)
    MenuCmd(0x01, 0x01, '・みっしぃ', 0x00000196)
    MenuCmd(0x01, 0x01, '・キーア', 0x00000197)
    MenuCmd(0x01, 0x01, '・ローゼリア', 0x00000198)
    MenuCmd(0x01, 0x01, '・★ラウラ', 0x00000199)
    MenuCmd(0x01, 0x01, '・アントン', 0x0000019A)
    MenuCmd(0x01, 0x01, '・☆ユウナ', 0x0000019B)
    MenuCmd(0x01, 0x01, '・ヴィンセント', 0x0000019C)
    MenuCmd(0x01, 0x01, '・★アンゼリカ', 0x0000019D)
    MenuCmd(0x01, 0x01, '・☆クルト', 0x000001A3)
    MenuCmd(0x01, 0x01, '・バラット侯', 0x0000019F)
    MenuCmd(0x01, 0x01, '・★アリサ', 0x00000194)
    MenuCmd(0x01, 0x01, '・ジョゼット', 0x000001A1)
    MenuCmd(0x01, 0x01, '・セリーヌ', 0x000001A2)
    MenuCmd(0x01, 0x01, '・セリーヌ・ネコ', 0x000001B8)
    MenuCmd(0x01, 0x01, '・☆アッシュ', 0x0000019E)
    MenuCmd(0x01, 0x01, '・ロイド', 0x000001A4)
    MenuCmd(0x01, 0x01, '・デュバリィ', 0x000001A5)
    MenuCmd(0x01, 0x01, '・★ユーシス', 0x000001A6)
    MenuCmd(0x01, 0x01, '・シェラザード', 0x000001A7)
    MenuCmd(0x01, 0x01, '・カエラ', 0x000001A8)
    MenuCmd(0x01, 0x01, '・★サラ', 0x000001A9)
    MenuCmd(0x01, 0x01, '・シャロン', 0x000001AA)
    MenuCmd(0x01, 0x01, '・ツァオ', 0x000001AB)
    MenuCmd(0x01, 0x01, '・★クロウ', 0x000001AC)
    MenuCmd(0x01, 0x01, '・☆アルティナ', 0x000001AD)
    MenuCmd(0x01, 0x01, '・カシウス①', 0x000001AE)
    MenuCmd(0x01, 0x01, '・ミリアム', 0x000001B0)
    MenuCmd(0x01, 0x01, '・トヴァル', 0x000001B1)
    MenuCmd(0x01, 0x01, '・ヨシュア', 0x000001B2)
    MenuCmd(0x01, 0x01, '・☆ミュゼ', 0x000001B3)
    MenuCmd(0x01, 0x01, '・アルゼイド①', 0x000001B4)
    MenuCmd(0x01, 0x01, '・★クロウ（イベント', 0x000001B7)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000190, 'loc_2F942'),
        (0x00000191, 'loc_2F970'),
        (0x00000192, 'loc_2F99E'),
        (0x00000193, 'loc_2F9CB'),
        (0x00000194, 'loc_2F9F9'),
        (0x00000195, 'loc_2FA27'),
        (0x00000196, 'loc_2FA56'),
        (0x00000197, 'loc_2FA84'),
        (0x00000198, 'loc_2FAB0'),
        (0x00000199, 'loc_2FAE0'),
        (0x0000019A, 'loc_2FB0E'),
        (0x0000019B, 'loc_2FB3D'),
        (0x0000019C, 'loc_2FB6A'),
        (0x0000019D, 'loc_2FB9A'),
        (0x0000019E, 'loc_2FBCB'),
        (0x0000019F, 'loc_2FBF7'),
        (0x000001A0, 'loc_2FC26'),
        (0x000001A1, 'loc_2FC52'),
        (0x000001A2, 'loc_2FC80'),
        (0x000001A3, 'loc_2FCB1'),
        (0x000001A4, 'loc_2FCDE'),
        (0x000001A5, 'loc_2FD0B'),
        (0x000001A6, 'loc_2FD3B'),
        (0x000001A7, 'loc_2FD69'),
        (0x000001A8, 'loc_2FD98'),
        (0x000001A9, 'loc_2FDC6'),
        (0x000001AA, 'loc_2FDF3'),
        (0x000001AB, 'loc_2FE22'),
        (0x000001AC, 'loc_2FE4E'),
        (0x000001AD, 'loc_2FE7B'),
        (0x000001AE, 'loc_2FEAA'),
        (0x000001B0, 'loc_2FEDA'),
        (0x000001B1, 'loc_2FF0A'),
        (0x000001B2, 'loc_2FF38'),
        (0x000001B3, 'loc_2FF67'),
        (0x000001B4, 'loc_2FF95'),
        (0x000001B8, 'loc_2FFC4'),
        (-1, 'loc_2FFF4'),
    )

    def _loc_2F942(): pass

    label('loc_2F942')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_pablo')

    Jump('loc_2FFF4')

    def _loc_2F970(): pass

    label('loc_2F970')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_eliot')

    Jump('loc_2FFF4')

    def _loc_2F99E(): pass

    label('loc_2F99E')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_olfa')

    Jump('loc_2FFF4')

    def _loc_2F9CB(): pass

    label('loc_2F9CB')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_tilia')

    Jump('loc_2FFF4')

    def _loc_2F9F9(): pass

    label('loc_2F9F9')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_alisa')

    Jump('loc_2FFF4')

    def _loc_2FA27(): pass

    label('loc_2FA27')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_sansan')

    Jump('loc_2FFF4')

    def _loc_2FA56(): pass

    label('loc_2FA56')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_missy')

    Jump('loc_2FFF4')

    def _loc_2FA84(): pass

    label('loc_2FA84')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_kea')

    Jump('loc_2FFF4')

    def _loc_2FAB0(): pass

    label('loc_2FAB0')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_roselia')

    Jump('loc_2FFF4')

    def _loc_2FAE0(): pass

    label('loc_2FAE0')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_laura')

    Jump('loc_2FFF4')

    def _loc_2FB0E(): pass

    label('loc_2FB0E')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_antone')

    Jump('loc_2FFF4')

    def _loc_2FB3D(): pass

    label('loc_2FB3D')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_juna')

    Jump('loc_2FFF4')

    def _loc_2FB6A(): pass

    label('loc_2FB6A')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_vincent')

    Jump('loc_2FFF4')

    def _loc_2FB9A(): pass

    label('loc_2FB9A')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_angelica')

    Jump('loc_2FFF4')

    def _loc_2FBCB(): pass

    label('loc_2FBCB')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_ash')

    Jump('loc_2FFF4')

    def _loc_2FBF7(): pass

    label('loc_2FBF7')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_barrad')

    Jump('loc_2FFF4')

    def _loc_2FC26(): pass

    label('loc_2FC26')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_fie')

    Jump('loc_2FFF4')

    def _loc_2FC52(): pass

    label('loc_2FC52')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_jozet')

    Jump('loc_2FFF4')

    def _loc_2FC80(): pass

    label('loc_2FC80')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_celine_h')

    Jump('loc_2FFF4')

    def _loc_2FCB1(): pass

    label('loc_2FCB1')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_kurt')

    Jump('loc_2FFF4')

    def _loc_2FCDE(): pass

    label('loc_2FCDE')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_roid')

    Jump('loc_2FFF4')

    def _loc_2FD0B(): pass

    label('loc_2FD0B')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_dubarry')

    Jump('loc_2FFF4')

    def _loc_2FD3B(): pass

    label('loc_2FD3B')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_jusis')

    Jump('loc_2FFF4')

    def _loc_2FD69(): pass

    label('loc_2FD69')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_schera')

    Jump('loc_2FFF4')

    def _loc_2FD98(): pass

    label('loc_2FD98')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_kaela')

    Jump('loc_2FFF4')

    def _loc_2FDC6(): pass

    label('loc_2FDC6')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_sara')

    Jump('loc_2FFF4')

    def _loc_2FDF3(): pass

    label('loc_2FDF3')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_sharon')

    Jump('loc_2FFF4')

    def _loc_2FE22(): pass

    label('loc_2FE22')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_cao')

    Jump('loc_2FFF4')

    def _loc_2FE4E(): pass

    label('loc_2FE4E')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_crow')

    Jump('loc_2FFF4')

    def _loc_2FE7B(): pass

    label('loc_2FE7B')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_altina')

    Jump('loc_2FFF4')

    def _loc_2FEAA(): pass

    label('loc_2FEAA')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_cassius')

    Jump('loc_2FFF4')

    def _loc_2FEDA(): pass

    label('loc_2FEDA')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_millium')

    Jump('loc_2FFF4')

    def _loc_2FF0A(): pass

    label('loc_2FF0A')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_tovar')

    Jump('loc_2FFF4')

    def _loc_2FF38(): pass

    label('loc_2FF38')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_joshua')

    Jump('loc_2FFF4')

    def _loc_2FF67(): pass

    label('loc_2FF67')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_musse')

    Jump('loc_2FFF4')

    def _loc_2FF95(): pass

    label('loc_2FF95')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_arseid')

    Jump('loc_2FFF4')

    def _loc_2FFC4(): pass

    label('loc_2FFC4')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))
    Call(ScriptId.System4, 'FC_CardGame_celine2')

    Jump('loc_2FFF4')

    def _loc_2FFF4(): pass

    label('loc_2FFF4')

    Return()

# id: 0x00BF offset: 0x2FFF8
@scena.Code('TK_MiniGame_Debug_Mg08_Cardset')
def TK_MiniGame_Debug_Mg08_Cardset():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3005B',
    )

    AddItem(0x00, 0x0893, 1)
    AddItem(0x00, 0x0870, 3)
    AddItem(0x00, 0x0872, 3)
    AddItem(0x00, 0x0878, 3)
    AddItem(0x00, 0x087C, 3)
    AddItem(0x00, 0x0882, 3)
    AddItem(0x00, 0x0883, 3)
    AddItem(0x00, 0x0888, 3)
    AddItem(0x00, 0x0889, 3)

    Jump('loc_3037E')

    def _loc_3005B(): pass

    label('loc_3005B')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_301EF',
    )

    AddItem(0x00, 0x0870, 3)
    AddItem(0x00, 0x0871, 3)
    AddItem(0x00, 0x0872, 3)
    AddItem(0x00, 0x0873, 3)
    AddItem(0x00, 0x0874, 3)
    AddItem(0x00, 0x0875, 3)
    AddItem(0x00, 0x0876, 3)
    AddItem(0x00, 0x0877, 3)
    AddItem(0x00, 0x0878, 3)
    AddItem(0x00, 0x0879, 3)
    AddItem(0x00, 0x087A, 3)
    AddItem(0x00, 0x087B, 3)
    AddItem(0x00, 0x087C, 3)
    AddItem(0x00, 0x087D, 3)
    AddItem(0x00, 0x087E, 3)
    AddItem(0x00, 0x087F, 3)
    AddItem(0x00, 0x0880, 3)
    AddItem(0x00, 0x0881, 3)
    AddItem(0x00, 0x0882, 3)
    AddItem(0x00, 0x0883, 3)
    AddItem(0x00, 0x0884, 3)
    AddItem(0x00, 0x0885, 3)
    AddItem(0x00, 0x0886, 3)
    AddItem(0x00, 0x0887, 3)
    AddItem(0x00, 0x0888, 3)
    AddItem(0x00, 0x0889, 3)
    AddItem(0x00, 0x088A, 3)
    AddItem(0x00, 0x088B, 3)
    AddItem(0x00, 0x088C, 3)
    AddItem(0x00, 0x088D, 3)
    AddItem(0x00, 0x088E, 3)
    AddItem(0x00, 0x088F, 3)
    AddItem(0x00, 0x0890, 3)
    AddItem(0x00, 0x0891, 3)
    AddItem(0x00, 0x0892, 1)
    AddItem(0x00, 0x0893, 1)
    AddItem(0x00, 0x0894, 1)
    AddItem(0x00, 0x0895, 1)
    AddItem(0x00, 0x0896, 1)
    AddItem(0x00, 0x0897, 1)
    AddItem(0x00, 0x0898, 1)
    AddItem(0x00, 0x0899, 1)
    AddItem(0x00, 0x089A, 1)
    AddItem(0x00, 0x089B, 1)
    AddItem(0x00, 0x089C, 1)
    AddItem(0x00, 0x089D, 1)
    AddItem(0x00, 0x089E, 1)
    AddItem(0x00, 0x089F, 1)

    Jump('loc_3037E')

    def _loc_301EF(): pass

    label('loc_301EF')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3037E',
    )

    AddItem(0x01, 0x0870, 99)
    AddItem(0x01, 0x0871, 99)
    AddItem(0x01, 0x0872, 99)
    AddItem(0x01, 0x0873, 99)
    AddItem(0x01, 0x0874, 99)
    AddItem(0x01, 0x0875, 99)
    AddItem(0x01, 0x0876, 99)
    AddItem(0x01, 0x0877, 99)
    AddItem(0x01, 0x0878, 99)
    AddItem(0x01, 0x0879, 99)
    AddItem(0x01, 0x087A, 99)
    AddItem(0x01, 0x087B, 99)
    AddItem(0x01, 0x087C, 99)
    AddItem(0x01, 0x087D, 99)
    AddItem(0x01, 0x087E, 99)
    AddItem(0x01, 0x087F, 99)
    AddItem(0x01, 0x0880, 99)
    AddItem(0x01, 0x0881, 99)
    AddItem(0x01, 0x0882, 99)
    AddItem(0x01, 0x0883, 99)
    AddItem(0x01, 0x0884, 99)
    AddItem(0x01, 0x0885, 99)
    AddItem(0x01, 0x0886, 99)
    AddItem(0x01, 0x0887, 99)
    AddItem(0x01, 0x0888, 99)
    AddItem(0x01, 0x0889, 99)
    AddItem(0x01, 0x088A, 99)
    AddItem(0x01, 0x088B, 99)
    AddItem(0x01, 0x088C, 99)
    AddItem(0x01, 0x088D, 99)
    AddItem(0x01, 0x088E, 99)
    AddItem(0x01, 0x088F, 99)
    AddItem(0x01, 0x0890, 99)
    AddItem(0x01, 0x0891, 99)
    AddItem(0x01, 0x0892, 99)
    AddItem(0x01, 0x0893, 99)
    AddItem(0x01, 0x0894, 99)
    AddItem(0x01, 0x0895, 99)
    AddItem(0x01, 0x0896, 99)
    AddItem(0x01, 0x0897, 99)
    AddItem(0x01, 0x0898, 99)
    AddItem(0x01, 0x0899, 99)
    AddItem(0x01, 0x089A, 99)
    AddItem(0x01, 0x089B, 99)
    AddItem(0x01, 0x089C, 99)
    AddItem(0x01, 0x089D, 99)
    AddItem(0x01, 0x089E, 99)
    AddItem(0x01, 0x089F, 99)

    def _loc_3037E(): pass

    label('loc_3037E')

    Return()

# id: 0x00C0 offset: 0x30380
@scena.Code('TK_Shop_Debug')
def TK_Shop_Debug():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_303A5(): pass

    label('loc_303A5')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_307C7',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '武器店', 0x000003E8)
    MenuCmd(0x01, 0x00, '武器店', 0x000003F2)
    MenuCmd(0x01, 0x00, '工房', 0x000003E9)
    MenuCmd(0x01, 0x00, '工房（换碎片）', 0x000003F3)
    MenuCmd(0x01, 0x00, '工房（换耀金石）', 0x000003F4)
    MenuCmd(0x01, 0x00, '工房（购买核心回路）', 0x000003EA)
    MenuCmd(0x01, 0x00, '※掘り出し物セット', 0x000003F5)
    MenuCmd(0x01, 0x00, '露天商店', 0x000003F6)
    MenuCmd(0x01, 0x00, '住宿', 0x000003EB)
    MenuCmd(0x01, 0x00, '交换物', 0x000003EC)
    MenuCmd(0x01, 0x00, '改造厂', 0x000003ED)
    MenuCmd(0x01, 0x00, '回路制作', 0x000003EF)
    MenuCmd(0x01, 0x00, '筹码交换（赌场）', 0x00000400)
    MenuCmd(0x01, 0x00, '想要无限米拉', 0x000003F0)
    MenuCmd(0x01, 0x00, '米拉添加测试', 0x000003F1)
    MenuCmd(0x01, 0x00, '★店铺清单', 0x000003FF)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x000003E8, 'loc_305DB'),
        (0x000003F2, 'loc_305E7'),
        (0x000003E9, 'loc_305F3'),
        (0x000003F3, 'loc_305FF'),
        (0x000003F4, 'loc_3060B'),
        (0x000003EA, 'loc_30617'),
        (0x000003F5, 'loc_30623'),
        (0x000003F6, 'loc_3065E'),
        (0x000003EB, 'loc_3066A'),
        (0x000003EC, 'loc_30676'),
        (0x000003ED, 'loc_30682'),
        (0x000003EF, 'loc_3068E'),
        (0x000003F0, 'loc_3069A'),
        (0x000003F1, 'loc_306EF'),
        (0x00000400, 'loc_30794'),
        (0x000003FF, 'loc_307A0'),
        (-1, 'loc_307B4'),
    )

    def _loc_305DB(): pass

    label('loc_305DB')

    OP_7D(0x0000, 0x00018F9C)

    Jump('loc_307C2')

    def _loc_305E7(): pass

    label('loc_305E7')

    OP_7D(0x0384, 0x00018F9C)

    Jump('loc_307C2')

    def _loc_305F3(): pass

    label('loc_305F3')

    OP_7D(0x0001, 0x00124F80)

    Jump('loc_307C2')

    def _loc_305FF(): pass

    label('loc_305FF')

    OP_7D(0x0385, 0x00124F80)

    Jump('loc_307C2')

    def _loc_3060B(): pass

    label('loc_3060B')

    OP_7D(0x0386, 0x00124F80)

    Jump('loc_307C2')

    def _loc_30617(): pass

    label('loc_30617')

    OP_7D(0x0010, 0x00124F96)

    Jump('loc_307C2')

    def _loc_30623(): pass

    label('loc_30623')

    OP_83(0xFFFF, 0x0000, 0x0000, 0x0000)
    OP_83(0x0000, 0x0004, 0x270F, 0x0317)
    OP_83(0x0001, 0x0004, 0x270F, 0x0318)
    OP_83(0x0002, 0x0004, 0x270F, 0x0319)
    OP_83(0x0003, 0x0004, 0x270F, 0x031A)
    OP_83(0x0004, 0x0004, 0x270F, 0x031B)

    Jump('loc_307C2')

    def _loc_3065E(): pass

    label('loc_3065E')

    OP_7D(0x0004, 0x00124F80)

    Jump('loc_307C2')

    def _loc_3066A(): pass

    label('loc_3066A')

    OP_7D(0x0003, 0x00124F80)

    Jump('loc_307C2')

    def _loc_30676(): pass

    label('loc_30676')

    OP_7D(0x0005, 0x00124F80)

    Jump('loc_307C2')

    def _loc_30682(): pass

    label('loc_30682')

    OP_7D(0x0006, 0x00124F80)

    Jump('loc_307C2')

    def _loc_3068E(): pass

    label('loc_3068E')

    OP_7D(0x0009, 0x00124F80)

    Jump('loc_307C2')

    def _loc_3069A(): pass

    label('loc_3069A')

    AddItem(0x04, 0x0000, 8000000)
    AddItem(0x07, 0x00F1, 1000)
    AddItem(0x07, 0x00F2, 1000)
    AddItem(0x07, 0x00F3, 1000)
    AddItem(0x07, 0x00F4, 1000)
    AddItem(0x07, 0x00F5, 1000)
    AddItem(0x07, 0x00F6, 1000)
    AddItem(0x07, 0x00F7, 1000)
    AddItem(0x07, 0x00F8, 1000)
    AddItem(0x18, 0x0000, 500)

    Jump('loc_307C2')

    def _loc_306EF(): pass

    label('loc_306EF')

    AddItem(0x04, 0x0000, 900)
    AddItem(0x07, 0x00F1, 100)
    AddItem(0x07, 0x00F2, 100)
    AddItem(0x07, 0x00F3, 100)
    AddItem(0x07, 0x00F4, 100)
    AddItem(0x07, 0x00F5, 100)
    AddItem(0x07, 0x00F6, 100)
    AddItem(0x07, 0x00F7, 100)
    AddItem(0x07, 0x00F8, 100)
    AddItem(0x0F, 0x0081, 1)
    AddItem(0x0F, 0x008C, 1)
    AddItem(0x0F, 0x00BE, 1)
    AddItem(0x0F, 0x00BF, 1)
    AddItem(0x0F, 0x00C0, 1)
    AddItem(0x0F, 0x00C8, 1)
    AddItem(0x00, 0x0000, 25)
    AddItem(0x00, 0x0005, 50)
    AddItem(0x00, 0x000A, 75)
    AddItem(0x00, 0x003C, 9)
    AddItem(0x18, 0x0000, 200)

    Jump('loc_307C2')

    def _loc_30794(): pass

    label('loc_30794')

    OP_7D(0x0008, 0x00124F80)

    Jump('loc_307C2')

    def _loc_307A0(): pass

    label('loc_307A0')

    Call(ScriptId.Current, 'FC_ShopList')

    Jump('loc_307C2')

    def _loc_307B4(): pass

    label('loc_307B4')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_307C2')

    def _loc_307C2(): pass

    label('loc_307C2')

    Jump('loc_303A5')

    def _loc_307C7(): pass

    label('loc_307C7')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))

    Return()

# id: 0x00C1 offset: 0x307DC
@scena.Code('FC_ShopList')
def FC_ShopList():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_307E5(): pass

    label('loc_307E5')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30A11',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'メルカバ・カレイジャス', 0x00000001)
    MenuCmd(0x01, 0x01, 'リーブス・ミルサンテ', 0x00000002)
    MenuCmd(0x01, 0x01, 'エリン・セントアーク・パルム', 0x00000003)
    MenuCmd(0x01, 0x01, 'クロスベル・ミシュラム・ウルスラ医科大学', 0x00000004)
    MenuCmd(0x01, 0x01, 'オルディス・ラクウェル・アルスター', 0x00000005)
    MenuCmd(0x01, 0x01, '★ショップ開封フラグ', 0x0000000A)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_30978'),
        (0x00000002, 'loc_3098E'),
        (0x00000003, 'loc_309A4'),
        (0x00000004, 'loc_309BA'),
        (0x00000005, 'loc_309D0'),
        (0x0000000A, 'loc_309E6'),
        (-1, 'loc_309FE'),
    )

    def _loc_30978(): pass

    label('loc_30978')

    Call(ScriptId.Current, 'FC_ShopList01')

    Jump('loc_30A0C')

    def _loc_3098E(): pass

    label('loc_3098E')

    Call(ScriptId.Current, 'FC_ShopList02')

    Jump('loc_30A0C')

    def _loc_309A4(): pass

    label('loc_309A4')

    Call(ScriptId.Current, 'FC_ShopList03')

    Jump('loc_30A0C')

    def _loc_309BA(): pass

    label('loc_309BA')

    Call(ScriptId.Current, 'FC_ShopList04')

    Jump('loc_30A0C')

    def _loc_309D0(): pass

    label('loc_309D0')

    Call(ScriptId.Current, 'FC_ShopList05')

    Jump('loc_30A0C')

    def _loc_309E6(): pass

    label('loc_309E6')

    Call(ScriptId.Current, 'FC_ShopListFlag')

    Jump('loc_30A0C')

    def _loc_309FE(): pass

    label('loc_309FE')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_30A0C')

    def _loc_30A0C(): pass

    label('loc_30A0C')

    Jump('loc_307E5')

    def _loc_30A11(): pass

    label('loc_30A11')

    Return()

# id: 0x00C2 offset: 0x30A14
@scena.Code('FC_ShopListFlag')
def FC_ShopListFlag():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_30A1D(): pass

    label('loc_30A1D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30D91',
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '初期　　リセット', 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0565, 7, 0x2B2F)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅰ－①　セントアーク', 0x00000001, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0572, 3, 0x2B93)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅰ－②　エリンの里', 0x00000002, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0574, 5, 0x2BA5)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅰ－②　ミルサンテ', 0x00000003, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x057E, 3, 0x2BF3)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅰ－③　エリンの里', 0x00000004, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0582, 1, 0x2C11)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅰ－③　クロスベル', 0x00000005, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06A1, 7, 0x350F)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, '断章　　エリンの里', 0x00000006, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06E7, 1, 0x3739)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅱ－②　メルカバ', 0x00000007, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0700, 0, 0x3800)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅱ－④　メルカバ', 0x00000008, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0820, 0, 0x4100)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅲ－０　カレイジャス', 0x00000009, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0838, 0, 0x41C0)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, 'Ⅲ－④　カレイジャス', 0x0000000A, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x09E0, 0, 0x4F00)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x02, '最終話　カレイジャス', 0x0000000B, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000000, 'loc_30D32'),
        (0x0000000B, 'loc_30D58'),
        (0x0000000A, 'loc_30D5B'),
        (0x00000009, 'loc_30D5E'),
        (0x00000008, 'loc_30D61'),
        (0x00000007, 'loc_30D64'),
        (0x00000006, 'loc_30D67'),
        (0x00000005, 'loc_30D6A'),
        (0x00000004, 'loc_30D6D'),
        (0x00000003, 'loc_30D70'),
        (0x00000002, 'loc_30D73'),
        (0x00000001, 'loc_30D76'),
        (-1, 'loc_30D7E'),
    )

    def _loc_30D32(): pass

    label('loc_30D32')

    ClearScenaFlags(ScenaFlag(0x0565, 7, 0x2B2F))
    ClearScenaFlags(ScenaFlag(0x0572, 3, 0x2B93))
    ClearScenaFlags(ScenaFlag(0x0574, 5, 0x2BA5))
    ClearScenaFlags(ScenaFlag(0x057E, 3, 0x2BF3))
    ClearScenaFlags(ScenaFlag(0x0582, 1, 0x2C11))
    ClearScenaFlags(ScenaFlag(0x06A1, 7, 0x350F))
    ClearScenaFlags(ScenaFlag(0x06E7, 1, 0x3739))
    ClearScenaFlags(ScenaFlag(0x0700, 0, 0x3800))
    ClearScenaFlags(ScenaFlag(0x0820, 0, 0x4100))
    ClearScenaFlags(ScenaFlag(0x0838, 0, 0x41C0))
    ClearScenaFlags(ScenaFlag(0x09E0, 0, 0x4F00))

    Jump('loc_30D8C')

    def _loc_30D58(): pass

    label('loc_30D58')

    SetScenaFlags(ScenaFlag(0x09E0, 0, 0x4F00))

    def _loc_30D5B(): pass

    label('loc_30D5B')

    SetScenaFlags(ScenaFlag(0x0838, 0, 0x41C0))

    def _loc_30D5E(): pass

    label('loc_30D5E')

    SetScenaFlags(ScenaFlag(0x0820, 0, 0x4100))

    def _loc_30D61(): pass

    label('loc_30D61')

    SetScenaFlags(ScenaFlag(0x0700, 0, 0x3800))

    def _loc_30D64(): pass

    label('loc_30D64')

    SetScenaFlags(ScenaFlag(0x06E7, 1, 0x3739))

    def _loc_30D67(): pass

    label('loc_30D67')

    SetScenaFlags(ScenaFlag(0x06A1, 7, 0x350F))

    def _loc_30D6A(): pass

    label('loc_30D6A')

    SetScenaFlags(ScenaFlag(0x0582, 1, 0x2C11))

    def _loc_30D6D(): pass

    label('loc_30D6D')

    SetScenaFlags(ScenaFlag(0x057E, 3, 0x2BF3))

    def _loc_30D70(): pass

    label('loc_30D70')

    SetScenaFlags(ScenaFlag(0x0574, 5, 0x2BA5))

    def _loc_30D73(): pass

    label('loc_30D73')

    SetScenaFlags(ScenaFlag(0x0572, 3, 0x2B93))

    def _loc_30D76(): pass

    label('loc_30D76')

    SetScenaFlags(ScenaFlag(0x0565, 7, 0x2B2F))

    Jump('loc_30D8C')

    def _loc_30D7E(): pass

    label('loc_30D7E')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_30D8C')

    def _loc_30D8C(): pass

    label('loc_30D8C')

    Jump('loc_30A1D')

    def _loc_30D91(): pass

    label('loc_30D91')

    Return()

# id: 0x00C3 offset: 0x30D94
@scena.Code('FC_ShopList01')
def FC_ShopList01():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_30D9D(): pass

    label('loc_30D9D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_311A5',
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, 'メルカバ・メルカバ工房', 0x00000001)
    MenuCmd(0x01, 0x02, 'メルカバ・メルカバ補給所', 0x00000002)
    MenuCmd(0x01, 0x02, 'カレイジャス・技術班ティータ・オーブメント調整', 0x00000003)
    MenuCmd(0x01, 0x02, 'カレイジャス・技術班ティータ・武器・クオーツを強化', 0x00000004)
    MenuCmd(0x01, 0x02, 'カレイジャス・技術班ティータ・買い物', 0x00000005)
    MenuCmd(0x01, 0x02, 'カレイジャス・技術班ティータ・ＥＸオーブを作成する', 0x00000006)
    MenuCmd(0x01, 0x02, 'カレイジャス・技術班ティータ・ＥＸオーブを組み込む', 0x00000007)
    MenuCmd(0x01, 0x02, 'カレイジャス・研修医リンデ・買い物', 0x00000008)
    MenuCmd(0x01, 0x02, 'カレイジャス・商人ベッキー・買い物', 0x00000009)
    MenuCmd(0x01, 0x02, 'カレイジャス・補給班スターク・買い物', 0x0000000A)
    MenuCmd(0x01, 0x02, 'カレイジャス・炊事班サンディ・買い物', 0x0000000B)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000001, 'loc_310FD'),
        (0x00000002, 'loc_31109'),
        (0x00000003, 'loc_31115'),
        (0x00000004, 'loc_31121'),
        (0x00000005, 'loc_3112D'),
        (0x00000006, 'loc_31139'),
        (0x00000007, 'loc_31145'),
        (0x00000008, 'loc_31162'),
        (0x00000009, 'loc_3116E'),
        (0x0000000A, 'loc_3117A'),
        (0x0000000B, 'loc_31186'),
        (-1, 'loc_31192'),
    )

    def _loc_310FD(): pass

    label('loc_310FD')

    OP_7D(0x0014, 0x00124F94)

    Jump('loc_311A0')

    def _loc_31109(): pass

    label('loc_31109')

    OP_7D(0x0015, 0x00124F95)

    Jump('loc_311A0')

    def _loc_31115(): pass

    label('loc_31115')

    OP_7D(0x0016, 0x00124F96)

    Jump('loc_311A0')

    def _loc_31121(): pass

    label('loc_31121')

    OP_7D(0x000B, 0x00124F96)

    Jump('loc_311A0')

    def _loc_3112D(): pass

    label('loc_3112D')

    OP_7D(0x0017, 0x00124F96)

    Jump('loc_311A0')

    def _loc_31139(): pass

    label('loc_31139')

    OP_7D(0x0012, 0x00124F96)

    Jump('loc_311A0')

    def _loc_31145(): pass

    label('loc_31145')

    Call(ScriptId.System, 'FC_ExOrb_SetInit')
    OP_BA(0x0A)
    OP_BA(0x0B)

    Jump('loc_311A0')

    def _loc_31162(): pass

    label('loc_31162')

    OP_7D(0x0018, 0x00124F99)

    Jump('loc_311A0')

    def _loc_3116E(): pass

    label('loc_3116E')

    OP_7D(0x0019, 0x00124F9B)

    Jump('loc_311A0')

    def _loc_3117A(): pass

    label('loc_3117A')

    OP_7D(0x001A, 0x00124F9C)

    Jump('loc_311A0')

    def _loc_31186(): pass

    label('loc_31186')

    OP_7D(0x001B, 0x00124F9D)

    Jump('loc_311A0')

    def _loc_31192(): pass

    label('loc_31192')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_311A0')

    def _loc_311A0(): pass

    label('loc_311A0')

    Jump('loc_30D9D')

    def _loc_311A5(): pass

    label('loc_311A5')

    Return()

# id: 0x00C4 offset: 0x311A8
@scena.Code('FC_ShopList02')
def FC_ShopList02():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_311B1(): pass

    label('loc_311B1')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_316DE',
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, 'リーブス・本・遊具《カーネギー書房》・買い物', 0x00000001)
    MenuCmd(0x01, 0x02, 'リーブス・ブティック《ラパン》・買い物', 0x00000002)
    MenuCmd(0x01, 0x02, 'リーブス・食材・雑貨《如水庵》・買い物', 0x00000003)
    MenuCmd(0x01, 0x02, 'リーブス・武器・交換屋《ナインヴァリ》・買い物', 0x00000004)
    MenuCmd(0x01, 0x02, 'リーブス・武器・交換屋《ナインヴァリ》・交換', 0x00000005)
    MenuCmd(0x01, 0x02, 'リーブス・武器・交換屋《ナインヴァリ》・掘り出し物', 0x00000006)
    MenuCmd(0x01, 0x02, '■《ナインヴァリ》・掘り出し物セット■', 0x000003F5)
    MenuCmd(0x01, 0x02, 'リーブス・宿酒場《バーニーズ》・買い物・宿泊', 0x00000007)
    MenuCmd(0x01, 0x02, 'リーブス・ベーカリーカフェ《ルセット》・買い物', 0x00000008)
    MenuCmd(0x01, 0x02, '分校・学生食堂・買い物', 0x00000009)
    MenuCmd(0x01, 0x02, 'ミルサンテ・武器・雑貨《○○○》・買い物（武器関連）', 0x0000000A)
    MenuCmd(0x01, 0x02, 'ミルサンテ・武器・雑貨《○○○》・買い物（雑貨関連）', 0x0000000B)
    MenuCmd(0x01, 0x02, 'ミルサンテ・宿酒場《○○○》・買い物・宿泊', 0x0000000C)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000001, 'loc_31600'),
        (0x00000002, 'loc_3160C'),
        (0x00000003, 'loc_31618'),
        (0x00000004, 'loc_31624'),
        (0x00000005, 'loc_31630'),
        (0x00000006, 'loc_3163C'),
        (0x00000007, 'loc_31648'),
        (0x00000008, 'loc_31654'),
        (0x00000009, 'loc_31660'),
        (0x0000000A, 'loc_3166C'),
        (0x0000000B, 'loc_31678'),
        (0x0000000C, 'loc_31684'),
        (0x000003F5, 'loc_31690'),
        (-1, 'loc_316CB'),
    )

    def _loc_31600(): pass

    label('loc_31600')

    OP_7D(0x001E, 0x00124FA8)

    Jump('loc_316D9')

    def _loc_3160C(): pass

    label('loc_3160C')

    OP_7D(0x001F, 0x00124FA9)

    Jump('loc_316D9')

    def _loc_31618(): pass

    label('loc_31618')

    OP_7D(0x0020, 0x00124FAA)

    Jump('loc_316D9')

    def _loc_31624(): pass

    label('loc_31624')

    OP_7D(0x0023, 0x00124FAB)

    Jump('loc_316D9')

    def _loc_31630(): pass

    label('loc_31630')

    OP_7D(0x0024, 0x00124FAB)

    Jump('loc_316D9')

    def _loc_3163C(): pass

    label('loc_3163C')

    OP_7D(0x0025, 0x00124FAB)

    Jump('loc_316D9')

    def _loc_31648(): pass

    label('loc_31648')

    OP_7D(0x0026, 0x00124FAC)

    Jump('loc_316D9')

    def _loc_31654(): pass

    label('loc_31654')

    OP_7D(0x0027, 0x00124FAD)

    Jump('loc_316D9')

    def _loc_31660(): pass

    label('loc_31660')

    OP_7D(0x0028, 0x00124FAE)

    Jump('loc_316D9')

    def _loc_3166C(): pass

    label('loc_3166C')

    OP_7D(0x002D, 0x00124FB2)

    Jump('loc_316D9')

    def _loc_31678(): pass

    label('loc_31678')

    OP_7D(0x002E, 0x00124FB2)

    Jump('loc_316D9')

    def _loc_31684(): pass

    label('loc_31684')

    OP_7D(0x002F, 0x00124FB3)

    Jump('loc_316D9')

    def _loc_31690(): pass

    label('loc_31690')

    OP_83(0xFFFF, 0x0000, 0x0000, 0x0000)
    OP_83(0x0000, 0x0025, 0x270F, 0x0317)
    OP_83(0x0001, 0x0025, 0x270F, 0x0318)
    OP_83(0x0002, 0x0025, 0x270F, 0x0319)
    OP_83(0x0003, 0x0025, 0x270F, 0x031A)
    OP_83(0x0004, 0x0025, 0x270F, 0x031B)

    Jump('loc_316D9')

    def _loc_316CB(): pass

    label('loc_316CB')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_316D9')

    def _loc_316D9(): pass

    label('loc_316D9')

    Jump('loc_311B1')

    def _loc_316DE(): pass

    label('loc_316DE')

    Return()

# id: 0x00C5 offset: 0x316E0
@scena.Code('FC_ShopList03')
def FC_ShopList03():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_316E9(): pass

    label('loc_316E9')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31CD9',
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x02, 0x000F, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, 'エリン・武具・工房《○○》', 0x00000001)
    MenuCmd(0x01, 0x02, 'エリン・雑貨屋《○○○○》', 0x00000002)
    MenuCmd(0x01, 0x02, 'エリン・薬師○○○', 0x00000003)
    MenuCmd(0x01, 0x02, 'エリン・宿酒場《○○》', 0x00000004)
    MenuCmd(0x01, 0x02, 'セントアーク・《チェンバーズ工房》・オーブメント調整', 0x0000000A)
    MenuCmd(0x01, 0x02, 'セントアーク・《チェンバーズ工房》・買い物', 0x0000000B)
    MenuCmd(0x01, 0x02, 'セントアーク・武具・甲冑《シュプリンガー》', 0x0000000C)
    MenuCmd(0x01, 0x02, 'セントアーク・高級食材《ステリーファーム》', 0x0000000D)
    MenuCmd(0x01, 0x02, 'セントアーク・ブティック《シャルダン》', 0x0000000E)
    MenuCmd(0x01, 0x02, 'セントアーク・古書・雑貨《エルヌール書房》', 0x0000000F)
    MenuCmd(0x01, 0x02, 'セントアーク・交換・古董品《デメテル》', 0x00000010)
    MenuCmd(0x01, 0x02, 'セントアーク・《ホテル・オーガスタ》', 0x00000011)
    MenuCmd(0x01, 0x02, 'セントアーク・カフェ・宿泊《エイプリル》', 0x00000012)
    MenuCmd(0x01, 0x02, 'セントアーク・ジューススタンド《ダイナ》', 0x00000013)
    MenuCmd(0x01, 0x02, 'パルム・武具・工房《ドワイト商会》', 0x00000014)
    MenuCmd(0x01, 0x02, 'パルム・雑貨・仕立て屋《ジェローム》', 0x00000015)
    MenuCmd(0x01, 0x02, 'パルム・イリスの土産屋', 0x00000016)
    MenuCmd(0x01, 0x02, 'パルム・宿酒場《白の小道亭》', 0x00000017)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000001, 'loc_31BEE'),
        (0x00000002, 'loc_31BFA'),
        (0x00000003, 'loc_31C06'),
        (0x00000004, 'loc_31C12'),
        (0x0000000A, 'loc_31C1E'),
        (0x0000000B, 'loc_31C2A'),
        (0x0000000C, 'loc_31C36'),
        (0x0000000D, 'loc_31C42'),
        (0x0000000E, 'loc_31C4E'),
        (0x0000000F, 'loc_31C5A'),
        (0x00000010, 'loc_31C66'),
        (0x00000011, 'loc_31C72'),
        (0x00000012, 'loc_31C7E'),
        (0x00000013, 'loc_31C8A'),
        (0x00000014, 'loc_31C96'),
        (0x00000015, 'loc_31CA2'),
        (0x00000016, 'loc_31CAE'),
        (0x00000017, 'loc_31CBA'),
        (-1, 'loc_31CC6'),
    )

    def _loc_31BEE(): pass

    label('loc_31BEE')

    OP_7D(0x0032, 0x00124FB7)

    Jump('loc_31CD4')

    def _loc_31BFA(): pass

    label('loc_31BFA')

    OP_7D(0x0033, 0x00124FB8)

    Jump('loc_31CD4')

    def _loc_31C06(): pass

    label('loc_31C06')

    OP_7D(0x0034, 0x00124FB9)

    Jump('loc_31CD4')

    def _loc_31C12(): pass

    label('loc_31C12')

    OP_7D(0x0035, 0x00124FBA)

    Jump('loc_31CD4')

    def _loc_31C1E(): pass

    label('loc_31C1E')

    OP_7D(0x000A, 0x00124F8F)

    Jump('loc_31CD4')

    def _loc_31C2A(): pass

    label('loc_31C2A')

    OP_7D(0x003C, 0x00124F8F)

    Jump('loc_31CD4')

    def _loc_31C36(): pass

    label('loc_31C36')

    OP_7D(0x003D, 0x00124FBC)

    Jump('loc_31CD4')

    def _loc_31C42(): pass

    label('loc_31C42')

    OP_7D(0x003E, 0x00124FBD)

    Jump('loc_31CD4')

    def _loc_31C4E(): pass

    label('loc_31C4E')

    OP_7D(0x003F, 0x00124FBE)

    Jump('loc_31CD4')

    def _loc_31C5A(): pass

    label('loc_31C5A')

    OP_7D(0x0040, 0x00124FBF)

    Jump('loc_31CD4')

    def _loc_31C66(): pass

    label('loc_31C66')

    OP_7D(0x0041, 0x00124FC0)

    Jump('loc_31CD4')

    def _loc_31C72(): pass

    label('loc_31C72')

    OP_7D(0x0042, 0x00124FC1)

    Jump('loc_31CD4')

    def _loc_31C7E(): pass

    label('loc_31C7E')

    OP_7D(0x0043, 0x00124FBA)

    Jump('loc_31CD4')

    def _loc_31C8A(): pass

    label('loc_31C8A')

    OP_7D(0x0044, 0x00124FBA)

    Jump('loc_31CD4')

    def _loc_31C96(): pass

    label('loc_31C96')

    OP_7D(0x0046, 0x00124F90)

    Jump('loc_31CD4')

    def _loc_31CA2(): pass

    label('loc_31CA2')

    OP_7D(0x0047, 0x00124FD0)

    Jump('loc_31CD4')

    def _loc_31CAE(): pass

    label('loc_31CAE')

    OP_7D(0x0048, 0x00124FD2)

    Jump('loc_31CD4')

    def _loc_31CBA(): pass

    label('loc_31CBA')

    OP_7D(0x0049, 0x00124FD1)

    Jump('loc_31CD4')

    def _loc_31CC6(): pass

    label('loc_31CC6')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_31CD4')

    def _loc_31CD4(): pass

    label('loc_31CD4')

    Jump('loc_316E9')

    def _loc_31CD9(): pass

    label('loc_31CD9')

    Return()

# id: 0x00C6 offset: 0x31CDC
@scena.Code('FC_ShopList04')
def FC_ShopList04():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_31CE5(): pass

    label('loc_31CE5')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_324E1',
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x02, 0x000F, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, 'クロスベル・オーバルストア《ゲンテン》', 0x00000001)
    MenuCmd(0x01, 0x02, 'クロスベル・《リジョンフード》', 0x00000002)
    MenuCmd(0x01, 0x02, 'クロスベル・雑貨コーナー《サザーク》', 0x00000003)
    MenuCmd(0x01, 0x02, 'クロスベル・ブティック《ルッカ》', 0x00000004)
    MenuCmd(0x01, 0x02, 'クロスベル・《ストレガーショップ》', 0x00000005)
    MenuCmd(0x01, 0x02, 'クロスベル・アクセサリ《ベイカー》', 0x00000006)
    MenuCmd(0x01, 0x02, 'クロスベル・《ジロンド武器商会》', 0x00000007)
    MenuCmd(0x01, 0x02, 'クロスベル・クロスベル商工組合', 0x00000008)
    MenuCmd(0x01, 0x02, 'クロスベル・食品・雑貨《タリーズ商店》', 0x00000009)
    MenuCmd(0x01, 0x02, 'クロスベル・野菜屋タッカー', 0x0000000A)
    MenuCmd(0x01, 0x02, 'クロスベル・魚屋マルテ', 0x0000000B)
    MenuCmd(0x01, 0x02, 'クロスベル・Ｐ＆Ｒ商会', 0x0000000C)
    MenuCmd(0x01, 0x02, 'クロスベル・ＩＢＣカウンター', 0x0000000D)
    MenuCmd(0x01, 0x02, 'クロスベル・アンティーク屋《イメルダ》', 0x0000000E)
    MenuCmd(0x01, 0x02, 'クロスベル・カフェレストラン《ヴァンセット》', 0x0000000F)
    MenuCmd(0x01, 0x02, 'クロスベル・ベーカリー《モルジュ》', 0x00000010)
    MenuCmd(0x01, 0x02, 'クロスベル・宿酒場《龍老飯店》', 0x00000011)
    MenuCmd(0x01, 0x02, 'クロスベル・麺処《オーゼル》', 0x00000012)
    MenuCmd(0x01, 0x02, 'クロスベル・交換屋《ナインヴァリ》', 0x00000013)
    MenuCmd(0x01, 0x02, 'ウルスラ医科大学・ビュッフェ《レクチュ》', 0x0000001E)
    MenuCmd(0x01, 0x02, 'ミシュラム\x09ブティック《コルセリカ》', 0x0000001F)
    MenuCmd(0x01, 0x02, 'ミシュラム\x09ジュエリー＆ドール《○○○》', 0x00000020)
    MenuCmd(0x01, 0x02, 'ミシュラム\x09パーク内ショップ', 0x00000021)
    MenuCmd(0x01, 0x02, 'ミシュラム\x09肉屋台', 0x00000022)
    MenuCmd(0x01, 0x02, 'ミシュラム\x09アイス屋台', 0x00000023)
    MenuCmd(0x01, 0x02, 'ミシュラム\x09レストラン《フォルトゥナ》', 0x00000024)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000001, 'loc_32396'),
        (0x00000002, 'loc_323A2'),
        (0x00000003, 'loc_323AE'),
        (0x00000004, 'loc_323BA'),
        (0x00000005, 'loc_323C6'),
        (0x00000006, 'loc_323D2'),
        (0x00000007, 'loc_323DE'),
        (0x00000008, 'loc_323EA'),
        (0x00000009, 'loc_323F6'),
        (0x0000000A, 'loc_32402'),
        (0x0000000B, 'loc_3240E'),
        (0x0000000C, 'loc_3241A'),
        (0x0000000D, 'loc_32426'),
        (0x0000000E, 'loc_32432'),
        (0x0000000F, 'loc_3243E'),
        (0x00000010, 'loc_3244A'),
        (0x00000011, 'loc_32456'),
        (0x00000012, 'loc_32462'),
        (0x00000013, 'loc_3246E'),
        (0x0000001E, 'loc_3247A'),
        (0x0000001F, 'loc_32486'),
        (0x00000020, 'loc_32492'),
        (0x00000021, 'loc_3249E'),
        (0x00000022, 'loc_324AA'),
        (0x00000023, 'loc_324B6'),
        (0x00000024, 'loc_324C2'),
        (-1, 'loc_324CE'),
    )

    def _loc_32396(): pass

    label('loc_32396')

    OP_7D(0x0050, 0x00124FDA)

    Jump('loc_324DC')

    def _loc_323A2(): pass

    label('loc_323A2')

    OP_7D(0x0051, 0x00124FDB)

    Jump('loc_324DC')

    def _loc_323AE(): pass

    label('loc_323AE')

    OP_7D(0x0052, 0x00124FDC)

    Jump('loc_324DC')

    def _loc_323BA(): pass

    label('loc_323BA')

    OP_7D(0x0053, 0x00124FDD)

    Jump('loc_324DC')

    def _loc_323C6(): pass

    label('loc_323C6')

    OP_7D(0x0054, 0x00124FDE)

    Jump('loc_324DC')

    def _loc_323D2(): pass

    label('loc_323D2')

    OP_7D(0x0055, 0x00124FDF)

    Jump('loc_324DC')

    def _loc_323DE(): pass

    label('loc_323DE')

    OP_7D(0x0056, 0x00124FE0)

    Jump('loc_324DC')

    def _loc_323EA(): pass

    label('loc_323EA')

    OP_7D(0x0057, 0x00124FE1)

    Jump('loc_324DC')

    def _loc_323F6(): pass

    label('loc_323F6')

    OP_7D(0x0058, 0x00124FE2)

    Jump('loc_324DC')

    def _loc_32402(): pass

    label('loc_32402')

    OP_7D(0x005A, 0x00124FE3)

    Jump('loc_324DC')

    def _loc_3240E(): pass

    label('loc_3240E')

    OP_7D(0x005B, 0x00124FE4)

    Jump('loc_324DC')

    def _loc_3241A(): pass

    label('loc_3241A')

    OP_7D(0x005C, 0x00124FE5)

    Jump('loc_324DC')

    def _loc_32426(): pass

    label('loc_32426')

    OP_7D(0x005D, 0x00124FE6)

    Jump('loc_324DC')

    def _loc_32432(): pass

    label('loc_32432')

    OP_7D(0x005E, 0x00124FE7)

    Jump('loc_324DC')

    def _loc_3243E(): pass

    label('loc_3243E')

    OP_7D(0x005F, 0x00124FE8)

    Jump('loc_324DC')

    def _loc_3244A(): pass

    label('loc_3244A')

    OP_7D(0x0060, 0x00124FE9)

    Jump('loc_324DC')

    def _loc_32456(): pass

    label('loc_32456')

    OP_7D(0x0061, 0x00124FEA)

    Jump('loc_324DC')

    def _loc_32462(): pass

    label('loc_32462')

    OP_7D(0x0062, 0x00124FEB)

    Jump('loc_324DC')

    def _loc_3246E(): pass

    label('loc_3246E')

    OP_7D(0x0063, 0x00124FEC)

    Jump('loc_324DC')

    def _loc_3247A(): pass

    label('loc_3247A')

    OP_7D(0x0064, 0x00124FEE)

    Jump('loc_324DC')

    def _loc_32486(): pass

    label('loc_32486')

    OP_7D(0x0066, 0x00124FEF)

    Jump('loc_324DC')

    def _loc_32492(): pass

    label('loc_32492')

    OP_7D(0x0067, 0x00124FF0)

    Jump('loc_324DC')

    def _loc_3249E(): pass

    label('loc_3249E')

    OP_7D(0x0068, 0x00124FF1)

    Jump('loc_324DC')

    def _loc_324AA(): pass

    label('loc_324AA')

    OP_7D(0x0069, 0x00124FF2)

    Jump('loc_324DC')

    def _loc_324B6(): pass

    label('loc_324B6')

    OP_7D(0x006A, 0x00124FF3)

    Jump('loc_324DC')

    def _loc_324C2(): pass

    label('loc_324C2')

    OP_7D(0x006B, 0x00124FF4)

    Jump('loc_324DC')

    def _loc_324CE(): pass

    label('loc_324CE')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_324DC')

    def _loc_324DC(): pass

    label('loc_324DC')

    Jump('loc_31CE5')

    def _loc_324E1(): pass

    label('loc_324E1')

    Return()

# id: 0x00C7 offset: 0x324E4
@scena.Code('FC_ShopList05')
def FC_ShopList05():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_324ED(): pass

    label('loc_324ED')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32AC8',
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x02, 0x000F, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, 'オルディス・《シュトラウス工房》\x09', 0x00000001)
    MenuCmd(0x01, 0x02, 'オルディス・リヴィエラコート', 0x00000002)
    MenuCmd(0x01, 0x02, 'オルディス・《ＲＦストア》', 0x00000003)
    MenuCmd(0x01, 0x02, 'オルディス・輸入食材《ケンドール》', 0x00000004)
    MenuCmd(0x01, 0x02, 'オルディス・《マニスター書房》', 0x00000005)
    MenuCmd(0x01, 0x02, 'オルディス・《グリシーヌ生花店》', 0x00000006)
    MenuCmd(0x01, 0x02, 'オルディス・アイス屋ジャクリーン\x09', 0x00000007)
    MenuCmd(0x01, 0x02, 'オルディス・宿酒場《海風亭》', 0x00000008)
    MenuCmd(0x01, 0x02, 'オルディス・船員酒場《ミランダ》', 0x00000009)
    MenuCmd(0x01, 0x02, 'オルディス・肉屋台バルトロ', 0x0000000A)
    MenuCmd(0x01, 0x02, 'オルディス・《ホテル・オルテンシア》', 0x0000000B)
    MenuCmd(0x01, 0x02, 'ラクウェル・《イカロス・マート》※武具・工房', 0x0000000C)
    MenuCmd(0x01, 0x02, 'ラクウェル・《イカロス・マート》※雑貨', 0x0000000D)
    MenuCmd(0x01, 0x02, 'ラクウェル・パブ・宿泊《ハーミット》', 0x0000000E)
    MenuCmd(0x01, 0x02, 'ラクウェル・パブ・食堂《デッケン》', 0x0000000F)
    MenuCmd(0x01, 0x02, 'アルスター・工房《○○○○○》', 0x00000010)
    MenuCmd(0x01, 0x02, 'アルスター・《○○○○○》', 0x00000011)
    MenuCmd(0x01, 0x02, 'アルスター・◆露店', 0x00000012)
    MenuCmd(0x01, 0x02, 'アルスター・宿酒場《○○○》', 0x00000013)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000001, 'loc_329D1'),
        (0x00000002, 'loc_329DD'),
        (0x00000003, 'loc_329E9'),
        (0x00000004, 'loc_329F5'),
        (0x00000005, 'loc_32A01'),
        (0x00000006, 'loc_32A0D'),
        (0x00000007, 'loc_32A19'),
        (0x00000008, 'loc_32A25'),
        (0x00000009, 'loc_32A31'),
        (0x0000000A, 'loc_32A3D'),
        (0x0000000B, 'loc_32A49'),
        (0x0000000C, 'loc_32A55'),
        (0x0000000D, 'loc_32A61'),
        (0x0000000E, 'loc_32A6D'),
        (0x0000000F, 'loc_32A79'),
        (0x00000010, 'loc_32A85'),
        (0x00000011, 'loc_32A91'),
        (0x00000012, 'loc_32A9D'),
        (0x00000013, 'loc_32AA9'),
        (-1, 'loc_32AB5'),
    )

    def _loc_329D1(): pass

    label('loc_329D1')

    OP_7D(0x006E, 0x00124F91)

    Jump('loc_32AC3')

    def _loc_329DD(): pass

    label('loc_329DD')

    OP_7D(0x006F, 0x00124FF8)

    Jump('loc_32AC3')

    def _loc_329E9(): pass

    label('loc_329E9')

    OP_7D(0x0070, 0x00124FF9)

    Jump('loc_32AC3')

    def _loc_329F5(): pass

    label('loc_329F5')

    OP_7D(0x0071, 0x00124FFA)

    Jump('loc_32AC3')

    def _loc_32A01(): pass

    label('loc_32A01')

    OP_7D(0x0072, 0x00124FFB)

    Jump('loc_32AC3')

    def _loc_32A0D(): pass

    label('loc_32A0D')

    OP_7D(0x0073, 0x00124FFC)

    Jump('loc_32AC3')

    def _loc_32A19(): pass

    label('loc_32A19')

    OP_7D(0x0074, 0x00125007)

    Jump('loc_32AC3')

    def _loc_32A25(): pass

    label('loc_32A25')

    OP_7D(0x0075, 0x00124FFE)

    Jump('loc_32AC3')

    def _loc_32A31(): pass

    label('loc_32A31')

    OP_7D(0x0076, 0x00124FFF)

    Jump('loc_32AC3')

    def _loc_32A3D(): pass

    label('loc_32A3D')

    OP_7D(0x0077, 0x00125000)

    Jump('loc_32AC3')

    def _loc_32A49(): pass

    label('loc_32A49')

    OP_7D(0x0078, 0x00125001)

    Jump('loc_32AC3')

    def _loc_32A55(): pass

    label('loc_32A55')

    OP_7D(0x007D, 0x0012500C)

    Jump('loc_32AC3')

    def _loc_32A61(): pass

    label('loc_32A61')

    OP_7D(0x007E, 0x0012500C)

    Jump('loc_32AC3')

    def _loc_32A6D(): pass

    label('loc_32A6D')

    OP_7D(0x007F, 0x0012500D)

    Jump('loc_32AC3')

    def _loc_32A79(): pass

    label('loc_32A79')

    OP_7D(0x0080, 0x0012500E)

    Jump('loc_32AC3')

    def _loc_32A85(): pass

    label('loc_32A85')

    OP_7D(0x0082, 0x00125016)

    Jump('loc_32AC3')

    def _loc_32A91(): pass

    label('loc_32A91')

    OP_7D(0x0083, 0x00125017)

    Jump('loc_32AC3')

    def _loc_32A9D(): pass

    label('loc_32A9D')

    OP_7D(0x0084, 0x00125018)

    Jump('loc_32AC3')

    def _loc_32AA9(): pass

    label('loc_32AA9')

    OP_7D(0x0085, 0x00125019)

    Jump('loc_32AC3')

    def _loc_32AB5(): pass

    label('loc_32AB5')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_32AC3')

    def _loc_32AC3(): pass

    label('loc_32AC3')

    Jump('loc_324ED')

    def _loc_32AC8(): pass

    label('loc_32AC8')

    Return()

# id: 0x00C8 offset: 0x32ACC
@scena.Code('TK_Note_Debug')
def TK_Note_Debug():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_32AF1(): pass

    label('loc_32AF1')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_333D1',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0016, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '记事本全登记', 0x00000000)
    MenuCmd(0x01, 0x00, '|导航全部登录', 0x0000000A)
    MenuCmd(0x01, 0x00, '任务全部登录', 0x00000014)
    MenuCmd(0x01, 0x00, '|全程', 0x00000015)
    MenuCmd(0x01, 0x00, '达成全部', 0x00000016)
    MenuCmd(0x01, 0x00, '|全部报告', 0x00000017)
    MenuCmd(0x01, 0x00, '|战斗全登录', 0x0000001E)
    MenuCmd(0x01, 0x00, '|所有信息', 0x0000001F)
    MenuCmd(0x01, 0x00, '|人物全部登录', 0x00000028)
    MenuCmd(0x01, 0x00, '|所有信息', 0x00000029)
    MenuCmd(0x01, 0x00, '|测试>', 0x0000002A)
    MenuCmd(0x01, 0x00, '|测试2>', 0x0000002B)
    MenuCmd(0x01, 0x00, '|料理全部登录', 0x00000032)
    MenuCmd(0x01, 0x00, '获取食材', 0x00000033)
    MenuCmd(0x01, 0x00, '料理情报', 0x00000034)
    MenuCmd(0x01, 0x00, '获得“我的料理”系列', 0x00000035)
    MenuCmd(0x01, 0x00, '|料理初始化', 0x00000036)
    MenuCmd(0x01, 0x00, '|厨师黎恩', 0x00000037)
    MenuCmd(0x01, 0x00, '|厨师新Ⅶ组', 0x00000038)
    MenuCmd(0x01, 0x00, '|厨师旧Ⅶ组', 0x00000039)
    MenuCmd(0x01, 0x00, '厨师及其他', 0x0000003A)
    MenuCmd(0x01, 0x00, '|厨师艾琳①', 0x0000003B)
    MenuCmd(0x01, 0x00, '|钓鱼全登录', 0x0000003C)
    MenuCmd(0x01, 0x00, '|卡片全部登录', 0x00000046)
    MenuCmd(0x01, 0x00, '|书籍全部登录', 0x00000050)
    MenuCmd(0x01, 0x00, '日志测试', 0x0000005A)
    MenuCmd(0x01, 0x00, '全开放', 0x00000064)
    MenuCmd(0x01, 0x00, '情节全面开放', 0x00000065)
    MenuCmd(0x01, 0x00, '事件簿', 0x00000066)
    MenuCmd(0x01, 0x00, '手册登录数取得测试>', 0x00000067)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000000, 'loc_32EDA'),
        (0x0000000A, 'loc_32F64'),
        (0x00000014, 'loc_32F6D'),
        (0x00000015, 'loc_32F89'),
        (0x00000016, 'loc_32FA5'),
        (0x00000017, 'loc_32FC1'),
        (0x0000001E, 'loc_32FDD'),
        (0x0000001F, 'loc_32FFA'),
        (0x00000028, 'loc_33017'),
        (0x00000029, 'loc_33034'),
        (0x0000002A, 'loc_33051'),
        (0x0000002B, 'loc_3306E'),
        (0x00000032, 'loc_3308B'),
        (0x00000033, 'loc_33098'),
        (0x00000034, 'loc_330A5'),
        (0x00000036, 'loc_331DA'),
        (0x00000037, 'loc_331E7'),
        (0x00000038, 'loc_331F4'),
        (0x00000039, 'loc_33221'),
        (0x0000003A, 'loc_33276'),
        (0x0000003B, 'loc_332BB'),
        (0x00000035, 'loc_332F8'),
        (0x0000003C, 'loc_33305'),
        (0x00000046, 'loc_3331A'),
        (0x0000005A, 'loc_33327'),
        (0x00000064, 'loc_3333E'),
        (0x00000050, 'loc_33346'),
        (0x00000065, 'loc_33365'),
        (0x00000066, 'loc_33382'),
        (0x00000067, 'loc_333A3'),
        (-1, 'loc_333BE'),
    )

    def _loc_32EDA(): pass

    label('loc_32EDA')

    Call(ScriptId.Current, 'EV_Note_Quest', (0xFF, 0x3, 0x0))
    Call(ScriptId.Current, 'EV_Note_Battle', (0xFF, 0x1, 0x0))
    Call(ScriptId.Current, 'EV_Note_Person', (0xFF, 0x1, 0x0))
    Call(ScriptId.Current, 'EV_Note_OpenBook', (0xFF, 0x1, 0x0))
    OP_97(0x00, 0xFFFF, 0x00000701)
    OP_91(0x05, 0xFFFF, 0x00000001)
    AddItem(0x0F, 0x0086, 1)
    AddItem(0x0F, 0x00DD, 1)
    OP_79(0x08, 0xFFFF)

    Jump('loc_333CC')

    def _loc_32F64(): pass

    label('loc_32F64')

    OP_79(0x08, 0xFFFF)

    Jump('loc_333CC')

    def _loc_32F6D(): pass

    label('loc_32F6D')

    Call(ScriptId.Current, 'EV_Note_Quest', (0xFF, 0x0, 0x0))

    Jump('loc_333CC')

    def _loc_32F89(): pass

    label('loc_32F89')

    Call(ScriptId.Current, 'EV_Note_Quest', (0xFF, 0x1, 0x0))

    Jump('loc_333CC')

    def _loc_32FA5(): pass

    label('loc_32FA5')

    Call(ScriptId.Current, 'EV_Note_Quest', (0xFF, 0x2, 0x0))

    Jump('loc_333CC')

    def _loc_32FC1(): pass

    label('loc_32FC1')

    Call(ScriptId.Current, 'EV_Note_Quest', (0xFF, 0x3, 0x0))

    Jump('loc_333CC')

    def _loc_32FDD(): pass

    label('loc_32FDD')

    Call(ScriptId.Current, 'EV_Note_Battle', (0xFF, 0x0, 0x0))

    Jump('loc_333CC')

    def _loc_32FFA(): pass

    label('loc_32FFA')

    Call(ScriptId.Current, 'EV_Note_Battle', (0xFF, 0x1, 0x0))

    Jump('loc_333CC')

    def _loc_33017(): pass

    label('loc_33017')

    Call(ScriptId.Current, 'EV_Note_Person', (0xFF, 0x0, 0x0))

    Jump('loc_333CC')

    def _loc_33034(): pass

    label('loc_33034')

    Call(ScriptId.Current, 'EV_Note_Person', (0xFF, 0x1, 0x0))

    Jump('loc_333CC')

    def _loc_33051(): pass

    label('loc_33051')

    Call(ScriptId.Current, 'EV_Note_Person', (0xFF, 0x2, 0x0))

    Jump('loc_333CC')

    def _loc_3306E(): pass

    label('loc_3306E')

    Call(ScriptId.Current, 'EV_Note_Person', (0xFF, 0x3, 0x0))

    Jump('loc_333CC')

    def _loc_3308B(): pass

    label('loc_3308B')

    OP_97(0x00, 0xFFFF, 0x00000001)

    Jump('loc_333CC')

    def _loc_33098(): pass

    label('loc_33098')

    AddItem(0x0F, 0x00D2, 99)

    Jump('loc_333CC')

    def _loc_330A5(): pass

    label('loc_330A5')

    OP_97(0x00, 0x0000, 0x00000701)
    OP_97(0x00, 0x0001, 0x00000701)
    OP_97(0x00, 0x0002, 0x00000701)
    OP_97(0x00, 0x0003, 0x00000701)
    OP_97(0x00, 0x0004, 0x00000701)
    OP_97(0x00, 0x0005, 0x00000701)
    OP_97(0x00, 0x0006, 0x00000701)
    OP_97(0x00, 0x0007, 0x00000701)
    OP_97(0x00, 0x0008, 0x00000701)
    OP_97(0x00, 0x0009, 0x00000701)
    OP_97(0x00, 0x000A, 0x00000701)
    OP_97(0x00, 0x000B, 0x00000701)
    OP_97(0x00, 0x000C, 0x00000701)
    OP_97(0x00, 0x000D, 0x00000701)
    OP_97(0x00, 0x000E, 0x00000701)
    OP_97(0x00, 0x000F, 0x00000701)
    OP_97(0x00, 0x0010, 0x00000701)
    OP_97(0x00, 0x0011, 0x00000701)
    OP_97(0x00, 0x0012, 0x00000701)
    OP_97(0x00, 0x0013, 0x00000701)
    OP_97(0x00, 0x0014, 0x00000701)
    OP_97(0x00, 0x0015, 0x00000701)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['妙婕'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['米莉亞姆'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000200)

    Jump('loc_333CC')

    def _loc_331DA(): pass

    label('loc_331DA')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x00000200)

    Jump('loc_333CC')

    def _loc_331E7(): pass

    label('loc_331E7')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000200)

    Jump('loc_333CC')

    def _loc_331F4(): pass

    label('loc_331F4')

    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['妙婕'], 0x00000200)

    Jump('loc_333CC')

    def _loc_33221(): pass

    label('loc_33221')

    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['克蕾雅少校'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000200)

    Jump('loc_333CC')

    def _loc_33276(): pass

    label('loc_33276')

    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['測試：妙婕制服測試'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['測試：奧利維爾'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['測試：杜巴莉'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['緹妲'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000200)

    Jump('loc_333CC')

    def _loc_332BB(): pass

    label('loc_332BB')

    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000200)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000200)

    Jump('loc_333CC')

    def _loc_332F8(): pass

    label('loc_332F8')

    AddItem(0x0F, 0x0085, 1)

    Jump('loc_333CC')

    def _loc_33305(): pass

    label('loc_33305')

    OP_91(0x05, 0xFFFF, 0x00000001)
    AddItem(0x0F, 0x00DD, 1)

    Jump('loc_333CC')

    def _loc_3331A(): pass

    label('loc_3331A')

    AddItem(0x0F, 0x0086, 1)

    Jump('loc_333CC')

    def _loc_33327(): pass

    label('loc_33327')

    Call(ScriptId.Current, 'EV_Note_AVoice')

    Jump('loc_333CC')

    def _loc_3333E(): pass

    label('loc_3333E')

    OP_99(0xFFFF)

    Jump('loc_333CC')

    def _loc_33346(): pass

    label('loc_33346')

    Call(ScriptId.Current, 'EV_Note_OpenBook', (0xFF, 0x1, 0x0))

    Jump('loc_333CC')

    def _loc_33365(): pass

    label('loc_33365')

    Call(ScriptId.Current, 'EV_Note_OpenSynopsis')

    Jump('loc_333CC')

    def _loc_33382(): pass

    label('loc_33382')

    Sleep(300)

    OP_95(0x00, 'book01', 'BookData02', 0x00, 0x0000)
    OP_95(0x01)

    Jump('loc_333CC')

    def _loc_333A3(): pass

    label('loc_333A3')

    Call(ScriptId.Current, 'EV_Note_CountTests')

    Jump('loc_333CC')

    def _loc_333BE(): pass

    label('loc_333BE')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_333CC')

    def _loc_333CC(): pass

    label('loc_333CC')

    Jump('loc_32AF1')

    def _loc_333D1(): pass

    label('loc_333D1')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))

    Return()

# id: 0x00C9 offset: 0x333E8
@scena.Code('EV_Note_Quest')
def EV_Note_Quest():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3340B',
    )

    QuestCtrl(0x270E, 0x01, 0x001F, 0x02)
    QuestCtrl(0x270E, 0x03, 0x01, 0x02)

    def _loc_3340B(): pass

    label('loc_3340B')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33436',
    )

    QuestCtrl(0x270E, 0x01, 0x001F, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0000, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0001, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0002, 0x02)

    def _loc_33436(): pass

    label('loc_33436')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33524',
    )

    QuestCtrl(0x270E, 0x01, 0x001F, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0000, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0001, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0002, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0003, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0004, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0005, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0006, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0007, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0008, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0009, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000A, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000B, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000C, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000D, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000E, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000F, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0010, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0011, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0012, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0013, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0014, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0015, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0016, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0017, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0018, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0019, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001A, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001B, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001C, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001D, 0x02)
    QuestCtrl(0x270E, 0x03, 0x02, 0x02)

    def _loc_33524(): pass

    label('loc_33524')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33618',
    )

    QuestCtrl(0x270E, 0x01, 0x001F, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0000, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0001, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0002, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0003, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0004, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0005, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0006, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0007, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0008, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0009, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000A, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000B, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000C, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000D, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000E, 0x02)
    QuestCtrl(0x270E, 0x01, 0x000F, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0010, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0011, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0012, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0013, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0014, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0015, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0016, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0017, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0018, 0x02)
    QuestCtrl(0x270E, 0x01, 0x0019, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001A, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001B, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001C, 0x02)
    QuestCtrl(0x270E, 0x01, 0x001D, 0x02)
    QuestCtrl(0x270E, 0x03, 0x02, 0x02)
    QuestCtrl(0x270E, 0x03, 0x04, 0x02)

    def _loc_33618(): pass

    label('loc_33618')

    Return()

# id: 0x00CA offset: 0x3361C
@scena.Code('EV_Note_AVoice')
def EV_Note_AVoice():
    OP_74(0x0001, 0x16)
    OP_74(0x0002, 0x16)
    OP_74(0x0003, 0x16)

    Return()

# id: 0x00CB offset: 0x3362C
@scena.Code('EV_Note_Battle')
def EV_Note_Battle():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3364E',
    )

    OP_91(0x02, 'all', 0x01)

    Jump('loc_33655')

    def _loc_3364E(): pass

    label('loc_3364E')

    OP_91(0x02, 'all', 0x7F)

    def _loc_33655(): pass

    label('loc_33655')

    Return()

# id: 0x00CC offset: 0x33658
@scena.Code('EV_Note_Person')
def EV_Note_Person():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3367B',
    )

    OP_91(0x00, 0xFFFF, 0x00000001)

    Jump('loc_33C08')

    def _loc_3367B(): pass

    label('loc_3367B')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3369F',
    )

    OP_91(0x00, 0xFFFF, 0x00001F00)
    OP_91(0x00, 0xFFFF, 0x00002000)

    Jump('loc_33C08')

    def _loc_3369F(): pass

    label('loc_3369F')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_336BB',
    )

    OP_91(0x00, 0xFFFF, 0xFFFFFFFF)

    Jump('loc_33C08')

    def _loc_336BB(): pass

    label('loc_336BB')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_338C6',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_336D3(): pass

    label('loc_336D3')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_338C1',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '全キャラUPDATE1', 0x00000001)
    MenuCmd(0x01, 0x01, '全キャラUPDATE1/OFF', 0x00000002)
    MenuCmd(0x01, 0x01, '全キャラ画像更新    (※scenaフラグ変更)', 0x00000003)
    MenuCmd(0x01, 0x01, '全キャラ画像更新/OFF(※scenaフラグ変更)', 0x00000004)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_337F2'),
        (0x00000002, 'loc_33837'),
        (0x00000003, 'loc_3387C'),
        (0x00000004, 'loc_3389C'),
        (-1, 'loc_337E4'),
    )

    def _loc_337E4(): pass

    label('loc_337E4')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_338BC')

    def _loc_337F2(): pass

    label('loc_337F2')

    OP_91(0x00, 0x0012, 0x00002000)
    OP_91(0x00, 0x0021, 0x00002000)
    OP_91(0x00, 0x00BD, 0x00002000)
    OP_91(0x00, 0x00EF, 0x00002000)
    OP_91(0x00, 0x0016, 0x00002000)
    OP_91(0x00, 0x0022, 0x00002000)
    OP_91(0x00, 0x0161, 0x00002000)
    OP_91(0x00, 0x0162, 0x00002000)

    Jump('loc_338BC')

    def _loc_33837(): pass

    label('loc_33837')

    OP_91(0x01, 0x0012, 0x00002000)
    OP_91(0x01, 0x0021, 0x00002000)
    OP_91(0x01, 0x00BD, 0x00002000)
    OP_91(0x01, 0x00EF, 0x00002000)
    OP_91(0x01, 0x0016, 0x00002000)
    OP_91(0x01, 0x0022, 0x00002000)
    OP_91(0x01, 0x0161, 0x00002000)
    OP_91(0x01, 0x0162, 0x00002000)

    Jump('loc_338BC')

    def _loc_3387C(): pass

    label('loc_3387C')

    SetScenaFlags(ScenaFlag(0x06E1, 3, 0x370B))
    SetScenaFlags(ScenaFlag(0x0564, 3, 0x2B23))
    SetScenaFlags(ScenaFlag(0x0564, 3, 0x2B23))
    SetScenaFlags(ScenaFlag(0x0564, 3, 0x2B23))
    SetScenaFlags(ScenaFlag(0x057E, 3, 0x2BF3))
    SetScenaFlags(ScenaFlag(0x0572, 3, 0x2B93))
    SetScenaFlags(ScenaFlag(0x06E7, 1, 0x3739))
    SetScenaFlags(ScenaFlag(0x06A6, 1, 0x3531))
    SetScenaFlags(ScenaFlag(0x06E7, 1, 0x3739))

    Jump('loc_338BC')

    def _loc_3389C(): pass

    label('loc_3389C')

    ClearScenaFlags(ScenaFlag(0x06E1, 3, 0x370B))
    ClearScenaFlags(ScenaFlag(0x0564, 3, 0x2B23))
    ClearScenaFlags(ScenaFlag(0x0564, 3, 0x2B23))
    ClearScenaFlags(ScenaFlag(0x0564, 3, 0x2B23))
    ClearScenaFlags(ScenaFlag(0x057E, 3, 0x2BF3))
    ClearScenaFlags(ScenaFlag(0x0572, 3, 0x2B93))
    ClearScenaFlags(ScenaFlag(0x06E7, 1, 0x3739))
    ClearScenaFlags(ScenaFlag(0x06A6, 1, 0x3531))
    ClearScenaFlags(ScenaFlag(0x06E7, 1, 0x3739))

    Jump('loc_338BC')

    def _loc_338BC(): pass

    label('loc_338BC')

    Jump('loc_336D3')

    def _loc_338C1(): pass

    label('loc_338C1')

    Jump('loc_33C08')

    def _loc_338C6(): pass

    label('loc_338C6')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_338CF(): pass

    label('loc_338CF')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33C08',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'リィン①', 0x00000001)
    MenuCmd(0x01, 0x01, 'リィン②', 0x00000002)
    MenuCmd(0x01, 0x01, 'リィン③', 0x00000003)
    MenuCmd(0x01, 0x01, 'リィン④', 0x00000004)
    MenuCmd(0x01, 0x01, 'アッシュ①', 0x0000000A)
    MenuCmd(0x01, 0x01, 'アッシュ②', 0x0000000B)
    MenuCmd(0x01, 0x01, 'アッシュ③', 0x0000000C)
    MenuCmd(0x01, 0x01, 'アッシュ④', 0x0000000D)
    MenuCmd(0x01, 0x01, 'アッシュ UPDATE1', 0x0000000C)
    MenuCmd(0x01, 0x01, 'ミュゼ①', 0x00000014)
    MenuCmd(0x01, 0x01, 'ミュゼ②', 0x00000015)
    MenuCmd(0x01, 0x01, 'ミュゼ③', 0x00000016)
    MenuCmd(0x01, 0x01, 'ミュゼ④', 0x00000017)
    MenuCmd(0x01, 0x01, 'ミュゼ UPDATE1', 0x00000018)
    MenuCmd(0x01, 0x01, 'ローゼリア①', 0x0000001E)
    MenuCmd(0x01, 0x01, 'ローゼリア②', 0x0000001F)
    MenuCmd(0x01, 0x01, 'ローゼリア UPDATE1', 0x00000020)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_33B26'),
        (0x00000002, 'loc_33B33'),
        (0x00000003, 'loc_33B40'),
        (0x00000004, 'loc_33B4D'),
        (0x0000000A, 'loc_33B5A'),
        (0x0000000B, 'loc_33B67'),
        (0x0000000C, 'loc_33B74'),
        (0x0000000D, 'loc_33B81'),
        (0x0000000E, 'loc_33B8E'),
        (0x00000014, 'loc_33B9B'),
        (0x00000015, 'loc_33BA8'),
        (0x00000016, 'loc_33BB5'),
        (0x00000017, 'loc_33BC2'),
        (0x00000018, 'loc_33BCF'),
        (0x0000001E, 'loc_33BDC'),
        (0x0000001F, 'loc_33BE9'),
        (0x00000020, 'loc_33BF6'),
        (-1, 'loc_33B18'),
    )

    def _loc_33B18(): pass

    label('loc_33B18')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_33C03')

    def _loc_33B26(): pass

    label('loc_33B26')

    OP_91(0x00, 0x0000, 0x00000100)

    Jump('loc_33C03')

    def _loc_33B33(): pass

    label('loc_33B33')

    OP_91(0x00, 0x0000, 0x00000200)

    Jump('loc_33C03')

    def _loc_33B40(): pass

    label('loc_33B40')

    OP_91(0x00, 0x0000, 0x00000400)

    Jump('loc_33C03')

    def _loc_33B4D(): pass

    label('loc_33B4D')

    OP_91(0x00, 0x0000, 0x00000800)

    Jump('loc_33C03')

    def _loc_33B5A(): pass

    label('loc_33B5A')

    OP_91(0x00, 0x000E, 0x00000100)

    Jump('loc_33C03')

    def _loc_33B67(): pass

    label('loc_33B67')

    OP_91(0x00, 0x000E, 0x00000200)

    Jump('loc_33C03')

    def _loc_33B74(): pass

    label('loc_33B74')

    OP_91(0x00, 0x000E, 0x00000400)

    Jump('loc_33C03')

    def _loc_33B81(): pass

    label('loc_33B81')

    OP_91(0x00, 0x000E, 0x00000800)

    Jump('loc_33C03')

    def _loc_33B8E(): pass

    label('loc_33B8E')

    OP_91(0x00, 0x000E, 0x00002000)

    Jump('loc_33C03')

    def _loc_33B9B(): pass

    label('loc_33B9B')

    OP_91(0x00, 0x000D, 0x00000100)

    Jump('loc_33C03')

    def _loc_33BA8(): pass

    label('loc_33BA8')

    OP_91(0x00, 0x000D, 0x00000200)

    Jump('loc_33C03')

    def _loc_33BB5(): pass

    label('loc_33BB5')

    OP_91(0x00, 0x000D, 0x00000400)

    Jump('loc_33C03')

    def _loc_33BC2(): pass

    label('loc_33BC2')

    OP_91(0x00, 0x000D, 0x00000800)

    Jump('loc_33C03')

    def _loc_33BCF(): pass

    label('loc_33BCF')

    OP_91(0x00, 0x000D, 0x00002000)

    Jump('loc_33C03')

    def _loc_33BDC(): pass

    label('loc_33BDC')

    OP_91(0x00, 0x0020, 0x00000100)

    Jump('loc_33C03')

    def _loc_33BE9(): pass

    label('loc_33BE9')

    OP_91(0x00, 0x0020, 0x00000200)

    Jump('loc_33C03')

    def _loc_33BF6(): pass

    label('loc_33BF6')

    OP_91(0x00, 0x0020, 0x00002000)

    Jump('loc_33C03')

    def _loc_33C03(): pass

    label('loc_33C03')

    Jump('loc_338CF')

    def _loc_33C08(): pass

    label('loc_33C08')

    Return()

# id: 0x00CD offset: 0x33C0C
@scena.Code('EV_Note_OpenBook')
def EV_Note_OpenBook():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)
    AddItem(0x00, 0x0122, 1)
    AddItem(0x00, 0x0123, 1)
    AddItem(0x00, 0x0124, 1)
    AddItem(0x00, 0x0125, 1)
    AddItem(0x00, 0x0126, 1)
    AddItem(0x00, 0x0127, 1)
    AddItem(0x00, 0x0128, 1)
    AddItem(0x00, 0x0129, 1)
    AddItem(0x00, 0x012A, 1)
    AddItem(0x00, 0x012B, 1)
    AddItem(0x00, 0x012C, 1)
    AddItem(0x00, 0x0168, 1)
    AddItem(0x00, 0x0169, 1)
    AddItem(0x00, 0x016A, 1)
    AddItem(0x00, 0x016B, 1)
    AddItem(0x00, 0x016C, 1)
    AddItem(0x00, 0x016D, 1)
    AddItem(0x00, 0x016E, 1)
    AddItem(0x00, 0x016F, 1)
    AddItem(0x00, 0x0170, 1)
    AddItem(0x00, 0x0190, 1)
    AddItem(0x00, 0x0191, 1)
    AddItem(0x00, 0x0192, 1)
    AddItem(0x00, 0x0193, 1)
    AddItem(0x00, 0x0194, 1)
    AddItem(0x00, 0x0195, 1)
    AddItem(0x00, 0x0196, 1)
    AddItem(0x00, 0x0197, 1)
    AddItem(0x00, 0x0198, 1)
    AddItem(0x00, 0x0199, 1)
    AddItem(0x00, 0x019A, 1)
    AddItem(0x00, 0x019B, 1)
    AddItem(0x00, 0x019C, 1)
    AddItem(0x00, 0x0139, 1)
    AddItem(0x00, 0x013A, 1)
    AddItem(0x00, 0x013B, 1)
    AddItem(0x00, 0x013C, 1)
    AddItem(0x00, 0x013D, 1)
    AddItem(0x00, 0x0159, 1)
    AddItem(0x00, 0x015A, 1)
    AddItem(0x00, 0x015B, 1)
    AddItem(0x00, 0x015C, 1)
    AddItem(0x00, 0x015D, 1)
    AddItem(0x00, 0x015E, 1)
    AddItem(0x00, 0x015F, 1)
    AddItem(0x00, 0x0160, 1)
    AddItem(0x00, 0x0161, 1)
    AddItem(0x00, 0x0162, 1)
    AddItem(0x00, 0x0171, 1)
    AddItem(0x00, 0x0172, 1)
    AddItem(0x00, 0x0173, 1)
    AddItem(0x00, 0x0174, 1)
    AddItem(0x00, 0x0175, 1)
    AddItem(0x00, 0x0176, 1)
    AddItem(0x00, 0x0177, 1)
    AddItem(0x00, 0x0178, 1)
    AddItem(0x00, 0x0179, 1)
    AddItem(0x00, 0x017C, 1)
    AddItem(0x00, 0x017D, 1)
    AddItem(0x00, 0x017E, 1)
    AddItem(0x00, 0x017F, 1)
    AddItem(0x00, 0x0180, 1)
    AddItem(0x00, 0x0181, 1)
    AddItem(0x00, 0x0182, 1)
    AddItem(0x00, 0x0183, 1)
    AddItem(0x00, 0x0184, 1)
    AddItem(0x00, 0x0185, 1)

    Return()

# id: 0x00CE offset: 0x33E2C
@scena.Code('EV_Note_OpenSynopsis')
def EV_Note_OpenSynopsis():
    AddItem(0x0F, 0x00DF, 1)

    Return()

# id: 0x00CF offset: 0x33E38
@scena.Code('EV_Note_CountTests')
def EV_Note_CountTests():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_33E41(): pass

    label('loc_33E41')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_340BC',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '战斗：魔兽的登录数', 0x00000001)
    MenuCmd(0x01, 0x00, '人物：人物信息登记数', 0x0000000A)
    MenuCmd(0x01, 0x00, '料理：料理的食谱数量', 0x00000014)
    MenuCmd(0x01, 0x00, '书籍：书籍的登录数', 0x0000001E)
    MenuCmd(0x01, 0x00, '钓鱼：鱼的登记数', 0x00000028)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF7)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_33F58'),
        (0x0000000A, 'loc_33F93'),
        (0x00000014, 'loc_33FD4'),
        (0x0000001E, 'loc_34024'),
        (0x00000028, 'loc_34068'),
        (-1, 'loc_340A9'),
    )

    def _loc_33F58(): pass

    label('loc_33F58')

    OP_18(
        0x00,
        (
            (Expr.Eval, "OP_A9(0x00)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '魔獣の登録数：#1C#0G',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_340B7')

    def _loc_33F93(): pass

    label('loc_33F93')

    OP_18(
        0x00,
        (
            (Expr.Eval, "OP_A9(0x0A)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '人物の情報登録数：#1C#0G',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_340B7')

    def _loc_33FD4(): pass

    label('loc_33FD4')

    OP_18(
        0x00,
        (
            (Expr.Eval, "OP_A9(0x14)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '料理：料理のレシピコンプ数：#1C#0G',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_340B7')

    def _loc_34024(): pass

    label('loc_34024')

    OP_18(
        0x00,
        (
            (Expr.Eval, "OP_A9(0x1E)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '書物：書物の登録数：#1C#0G',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_340B7')

    def _loc_34068(): pass

    label('loc_34068')

    OP_18(
        0x00,
        (
            (Expr.Eval, "OP_A9(0x28)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            '釣り：魚の登録数：#1C#0G',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_340B7')

    def _loc_340A9(): pass

    label('loc_340A9')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_340B7')

    def _loc_340B7(): pass

    label('loc_340B7')

    Jump('loc_33E41')

    def _loc_340BC(): pass

    label('loc_340BC')

    Return()

# id: 0x00D0 offset: 0x340C0
@scena.Code('TK_Camp_Debug')
def TK_Camp_Debug():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_340E5(): pass

    label('loc_340E5')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3431F',
    )

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '整体：禁止测试>', 0x0000044C)
    MenuCmd(0x01, 0x00, '整体：其他测试>', 0x0000044E)
    MenuCmd(0x01, 0x00, '编组：队伍测试>', 0x0000044F)
    MenuCmd(0x01, 0x00, '导力器控制>', 0x00000450)
    MenuCmd(0x01, 0x00, '核心回路>', 0x00000451)
    MenuCmd(0x01, 0x00, '链接测试>', 0x00000452)
    MenuCmd(0x01, 0x00, '未知的测试>', 0x00000453)
    MenuCmd(0x01, 0x00, '部分道具禁止测试>', 0x00000454)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x0000044C, 'loc_34237'),
        (0x0000044E, 'loc_34253'),
        (0x0000044F, 'loc_34271'),
        (0x00000450, 'loc_3428B'),
        (0x00000451, 'loc_342A3'),
        (0x00000452, 'loc_342C1'),
        (0x00000453, 'loc_342D6'),
        (0x00000454, 'loc_342F0'),
        (-1, 'loc_3430C'),
    )

    def _loc_34237(): pass

    label('loc_34237')

    Call(ScriptId.Current, 'TK_Camp_ChrFlagTest')

    Jump('loc_3431A')

    def _loc_34253(): pass

    label('loc_34253')

    Call(ScriptId.Current, 'TK_Camp_OtherFlagTest')

    Jump('loc_3431A')

    def _loc_34271(): pass

    label('loc_34271')

    Call(ScriptId.Current, 'TK_Camp_PartyTest')

    Jump('loc_3431A')

    def _loc_3428B(): pass

    label('loc_3428B')

    Call(ScriptId.Current, 'TK_Camp_Orbment')

    Jump('loc_3431A')

    def _loc_342A3(): pass

    label('loc_342A3')

    Call(ScriptId.Current, 'TK_Camp_MQuartz', (0xFF, 0x0, 0x0))

    Jump('loc_3431A')

    def _loc_342C1(): pass

    label('loc_342C1')

    Call(ScriptId.Current, 'TK_Camp_Link')

    Jump('loc_3431A')

    def _loc_342D6(): pass

    label('loc_342D6')

    Call(ScriptId.Current, 'TK_Camp_Formation')

    Jump('loc_3431A')

    def _loc_342F0(): pass

    label('loc_342F0')

    Call(ScriptId.Current, 'TK_Camp_CantUseItem')

    Jump('loc_3431A')

    def _loc_3430C(): pass

    label('loc_3430C')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3431A')

    def _loc_3431A(): pass

    label('loc_3431A')

    Jump('loc_340E5')

    def _loc_3431F(): pass

    label('loc_3431F')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))

    Return()

# id: 0x00D1 offset: 0x34334
@scena.Code('TK_Battle_Debug')
def TK_Battle_Debug():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    AddItem(0x0F, 0x0081, 10)
    AddItem(0x0F, 0x00D7, 10)
    AddItem(0x0F, 0x00D3, 10)
    AddItem(0x0F, 0x00D4, 10)
    AddItem(0x0F, 0x00D5, 10)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x14),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3441B',
    )

    CreateThread(0x03E8, 0x03, ScriptId.Current, 'FC_SetMegane')
    CreateThread(0x03E9, 0x03, ScriptId.Current, 'FC_SetMegane')
    CreateThread(0x03EA, 0x03, ScriptId.Current, 'FC_SetMegane')
    CreateThread(0x03EB, 0x03, ScriptId.Current, 'FC_SetMegane')
    CreateThread(0x03EC, 0x03, ScriptId.Current, 'FC_SetMegane')
    CreateThread(0x03ED, 0x03, ScriptId.Current, 'FC_SetMegane')
    CreateThread(0x03EE, 0x03, ScriptId.Current, 'FC_SetMegane')
    CreateThread(0x03EF, 0x03, ScriptId.Current, 'FC_SetMegane')

    def _loc_3441B(): pass

    label('loc_3441B')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_34424(): pass

    label('loc_34424')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34BEE',
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '战斗测试', 0x00000000)
    MenuCmd(0x01, 0x00, '战斗测试（战斗区域）', 0x00000001)
    MenuCmd(0x01, 0x00, '战斗测试（实际地图）', 0x00000002)
    MenuCmd(0x01, 0x00, '战斗测试（强敌杂鱼）', 0x00000003)
    MenuCmd(0x01, 0x00, '战斗测试（敌人8体）', 0x00000004)
    MenuCmd(0x01, 0x00, '战斗测试（幻兽）', 0x00000005)
    MenuCmd(0x01, 0x00, '战斗测试（暗转）', 0x00000006)
    MenuCmd(0x01, 0x00, '战斗队伍', 0x00000007)
    MenuCmd(0x01, 0x00, '用于确认战斗队伍', 0x00000009)
    MenuCmd(0x01, 0x00, '用于确认战斗等级提升', 0x0000000A)
    MenuCmd(0x01, 0x00, '用于确认战斗链接升级', 0x0000000B)
    MenuCmd(0x01, 0x00, '战斗AT奖金测试用', 0x0000000C)
    MenuCmd(0x01, 0x00, '骑神战配置测试（请变更BTLSET1000）', 0x00000017)
    MenuCmd(0x01, 0x00, '骑神战测试>', 0x00000016)
    MenuCmd(0x01, 0x00, '战斗活动>', 0x0000000F)
    MenuCmd(0x01, 0x00, '获得勇气指令>', 0x00000010)
    MenuCmd(0x01, 0x00, '------------------------------------', 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 6, 0x406)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x00, '无战斗背景音乐', 0x00000014, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x00, '选择战斗对手的数量>', 0x00000015)
    MenuCmd(0x01, 0x00, '选择战斗对手（有AT伯纳斯）>', 0x00000012)
    MenuCmd(0x01, 0x00, '选择战斗对象（梯度图）>', 0x00000013)
    MenuCmd(0x01, 0x00, '选择战斗对手＞', 0x00000011)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000000, 'loc_347FD'),
        (0x00000001, 'loc_34842'),
        (0x00000002, 'loc_34863'),
        (0x00000003, 'loc_3489F'),
        (0x00000004, 'loc_348C0'),
        (0x00000005, 'loc_348E1'),
        (0x00000006, 'loc_3490B'),
        (0x00000007, 'loc_3492C'),
        (0x00000009, 'loc_34947'),
        (0x0000000A, 'loc_349C7'),
        (0x0000000B, 'loc_349E8'),
        (0x0000000C, 'loc_34A21'),
        (0x0000000F, 'loc_34A42'),
        (0x00000010, 'loc_34A59'),
        (0x00000011, 'loc_34A66'),
        (0x00000012, 'loc_34A87'),
        (0x00000013, 'loc_34AA8'),
        (0x00000014, 'loc_34AC9'),
        (0x00000015, 'loc_34AD1'),
        (0x00000016, 'loc_34AED'),
        (0x00000017, 'loc_34AFD'),
        (-1, 'loc_34BDB'),
    )

    def _loc_347FD(): pass

    label('loc_347FD')

    SetScenaFlags(ScenaFlag(0x0080, 0, 0x400))
    SetScenaFlags(ScenaFlag(0x0080, 1, 0x401))
    SetScenaFlags(ScenaFlag(0x0080, 2, 0x402))
    Call(ScriptId.System, 'FC_EVENT_BATTLE_FADEOUT')
    Battle(0x00, 0x00000001, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34842(): pass

    label('loc_34842')

    Battle(0x00, 0x00000002, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34863(): pass

    label('loc_34863')

    Call(ScriptId.System, 'FC_EVENT_BATTLE_FADEOUT')
    Battle(0x00, 0x00000004, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_3489F(): pass

    label('loc_3489F')

    Battle(0x00, 0x00000003, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_348C0(): pass

    label('loc_348C0')

    Battle(0x00, 0x00000006, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_348E1(): pass

    label('loc_348E1')

    Battle(0x00, 0x00000007, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_3490B(): pass

    label('loc_3490B')

    Battle(0x00, 0x00000008, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_3492C(): pass

    label('loc_3492C')

    Call(ScriptId.Debug, 'FC_BattleTestParty')

    Jump('loc_34BE9')

    def _loc_34947(): pass

    label('loc_34947')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['緹妲'])
    FormationSetLeader(ChrTable['緹妲'])
    AddItem(0x00, 0x0001, 15)
    AddItem(0x00, 0x0006, 15)
    AddItem(0x00, 0x027A, 15)
    OP_70(0x00, 0x0014, 0x027A, 0x03, 0x00)
    CraftCtrl(0x00, 0x0014, 0x0BEA)
    CraftCtrl(0x00, 0x0014, 0x0BEB)
    CraftCtrl(0x00, 0x0014, 0x0869)
    CraftCtrl(0x00, 0x0014, 0x0BFE)
    CraftCtrl(0x00, 0x0014, 0x087A)
    OP_48(0x00, 0x0014, 0x0001, 0x0028)
    SetScenaFlags(ScenaFlag(0x0080, 0, 0x400))
    SetScenaFlags(ScenaFlag(0x0080, 1, 0x401))
    SetScenaFlags(ScenaFlag(0x0080, 2, 0x402))
    OP_69(0x04, 0x0007)
    OP_69(0x02, 0x0000, 0xFFFF, 0x0003)
    OP_69(0x02, 0x0014, 0xFFFF, 0x0003)
    OP_69(0x00, 0x0000, 0x0014, 0xFF, 0x00, 0x00)

    Jump('loc_34BE9')

    def _loc_349C7(): pass

    label('loc_349C7')

    Battle(0x00, 0x00000005, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_349E8(): pass

    label('loc_349E8')

    OP_69(0x05, 0x0000, 0x000B, 0x07CF)
    OP_69(0x05, 0x000B, 0x000A, 0x07CF)
    OP_69(0x05, 0x000C, 0x0009, 0x07CF)
    Battle(0x00, 0x00000001, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34A21(): pass

    label('loc_34A21')

    Battle(0x00, 0x00000009, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34A42(): pass

    label('loc_34A42')

    Call(ScriptId.Current, 'TK_BattleEvent')

    Jump('loc_34BE9')

    def _loc_34A59(): pass

    label('loc_34A59')

    CraftCtrl(0x0B, 0xFFFF, 0x00000000)

    Jump('loc_34BE9')

    def _loc_34A66(): pass

    label('loc_34A66')

    Battle(0x00, 0x0000000B, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34A87(): pass

    label('loc_34A87')

    Battle(0x00, 0x0000000C, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34AA8(): pass

    label('loc_34AA8')

    Battle(0x00, 0x0000000D, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34AC9(): pass

    label('loc_34AC9')

    OP_12(0x0406)

    Jump('loc_34BE9')

    def _loc_34AD1(): pass

    label('loc_34AD1')

    Call(ScriptId.Current, 'FC_SelectEnemyCount')

    Jump('loc_34BE9')

    def _loc_34AED(): pass

    label('loc_34AED')

    OP_28((0xDD, 'a1004'), (0xDD, ''), 0x00)

    Jump('loc_34BE9')

    def _loc_34AFD(): pass

    label('loc_34AFD')

    Call(ScriptId.System, 'DebugGetKisinItem_2')
    Call(ScriptId.System, 'DebugGetKisinOrb')
    SetScenaFlags(ScenaFlag(0x0087, 1, 0x439))
    OP_48(0x00, 0x0000, 0x0001, 0x0022)
    OP_48(0x00, 0x000A, 0x0001, 0x001D)
    OP_48(0x00, 0x000B, 0x0001, 0x001D)

    OP_18(
        0x31,
        (
            (Expr.PushLong, 0x1C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_B8(0x03, (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    OP_B8(0x00, (0xFF, 0x0, 0x0), (0xFF, 0xC4E, 0x0))
    OP_B8(0x00, (0xFF, 0x1, 0x0), (0xFF, 0xC57, 0x0))
    FormationCtrl(0x18)
    FormationCtrl(0x16, 0x0000, 0x0001)
    FormationCtrl(0x16, 0x000A, 0x0005)
    FormationCtrl(0x16, 0x000B, 0x0004)
    OP_B7(0x03, 0x0001)
    OP_B7(0x03, 0x0002)
    OP_B7(0x03, 0x0003)
    OP_B7(0x03, 0x0004)
    OP_B7(0x03, 0x0005)
    OP_B7(0x03, 0x0006)
    OP_B7(0x03, 0x0007)
    OP_B7(0x03, 0x0008)
    OP_B7(0x03, 0x0009)
    OP_B7(0x03, 0x000F)
    OP_B7(0x03, 0x000C)
    OP_B7(0x03, 0x000E)
    Battle(0x00, 0x00000025, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_34BE9')

    def _loc_34BDB(): pass

    label('loc_34BDB')

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34BE9')

    def _loc_34BE9(): pass

    label('loc_34BE9')

    Jump('loc_34424')

    def _loc_34BEE(): pass

    label('loc_34BEE')

    Call(ScriptId.System, 'FC_TalkEnd', (0xFF, 0x0, 0x0))

    Return()

# id: 0x00D2 offset: 0x34C04
@scena.Code('FC_SelectEnemyCount')
def FC_SelectEnemyCount():
    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_34C0D(): pass

    label('loc_34C0D')

    If(
        (
            (Expr.Expr23, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34DB9',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00BA, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '現在は#0Gです。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    MenuCmd(0x00, 0x02, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x02, '　１　', 0x00000001)
    MenuCmd(0x01, 0x02, '　２　', 0x00000002)
    MenuCmd(0x01, 0x02, '　３　', 0x00000003)
    MenuCmd(0x01, 0x02, '　４　', 0x00000004)
    MenuCmd(0x01, 0x02, '　５　', 0x00000005)
    MenuCmd(0x01, 0x02, '　６　', 0x00000006)
    MenuCmd(0x01, 0x02, '　７　', 0x00000007)
    MenuCmd(0x01, 0x02, '　８　', 0x00000008)
    MenuCmd(0x02, 0x02, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x02, 0xF8)
    MenuCmd(0x03, 0x02)

    Switch(
        (
            (Expr.Expr23, 0xF8),
            Expr.Return,
        ),
        (0x00000001, 'loc_34D30'),
        (0x00000002, 'loc_34D3E'),
        (0x00000003, 'loc_34D4C'),
        (0x00000004, 'loc_34D5A'),
        (0x00000005, 'loc_34D68'),
        (0x00000006, 'loc_34D76'),
        (0x00000007, 'loc_34D84'),
        (0x00000008, 'loc_34D92'),
        (-1, 'loc_34DA0'),
    )

    def _loc_34D30(): pass

    label('loc_34D30')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34D3E(): pass

    label('loc_34D3E')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34D4C(): pass

    label('loc_34D4C')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34D5A(): pass

    label('loc_34D5A')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34D68(): pass

    label('loc_34D68')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34D76(): pass

    label('loc_34D76')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34D84(): pass

    label('loc_34D84')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34D92(): pass

    label('loc_34D92')

    OP_08(
        0x14,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34DA0(): pass

    label('loc_34DA0')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34DAE')

    def _loc_34DAE(): pass

    label('loc_34DAE')

    OP_18(
        0x00,
        (
            (Expr.PushValueByIndex, 0x14),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_34C0D')

    def _loc_34DB9(): pass

    label('loc_34DB9')

    OP_25(0x00)

    Return()

# id: 0x00D3 offset: 0x34DBC
@scena.Code('FC_SetMegane')
def FC_SetMegane():
    LoadAsset('C_EQU350_C02')
    AttachEquip(0xFFFE, 'C_EQU350_C02', 'megane_point', 0.0, 0.0, -0.04, 0.0, 0.0, 0.0, 1.4, 1.4, 1.4)
    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x01)

    Return()

# id: 0x00D4 offset: 0x34E24
@scena.Code('TK_BattleEvent')
def TK_BattleEvent():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_34E2D(): pass

    label('loc_34E2D')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35946',
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '閃４[条件テスト]', 0x000007D1)
    MenuCmd(0x01, 0x01, '[QS343_02][ゼシカ＆ウェインがラウラ＆デュバリィとの手合わせ]', 0x0000240C)
    MenuCmd(0x01, 0x01, '[EV_02E_10_00]ガレス率いる赤い星座部隊との中ボス戦', 0x0000250C)
    MenuCmd(0x01, 0x01, '[EV_03B_04_00]アリサ・アンゼリカＶＳエミリー・テレジアのイベント戦闘', 0x0000260C)
    MenuCmd(0x01, 0x01, '[EV_01B_29_02]ルトガー＆ゼノ＆レオニダスとのボス戦②', 0x0000270C)
    MenuCmd(0x01, 0x01, '[EV_01C_26_00]セドリック・エイダ・フリッツ・シャーリィとのボス戦①', 0x0000290C)
    MenuCmd(0x01, 0x01, '[EV_01D_43_00]カンパネルラ・レクター・シャロンとの戦闘', 0x00002A0C)
    MenuCmd(0x01, 0x01, '[EV_01X_09_00]リンクした状態のＯＺミラージュ紅＆蒼とのボス戦', 0x00002B0C)
    MenuCmd(0x01, 0x01, '[EV_01X_14_05]リィンたち４名ＶＳ魔人マクバーン、アイネス、エンネア', 0x00002C0C)
    MenuCmd(0x01, 0x01, '[EV_01X_15_09]オズボーン＆アリアンロードとの大ボス戦', 0x00002D0C)
    MenuCmd(0x01, 0x01, '[EV_02B_12_01]クレア＆ロスヴァイセとの人間ボス戦', 0x00002E0C)
    MenuCmd(0x01, 0x01, '[EV_02C_12_00]クレイグ＆ナイトハルトとのボス戦', 0x00002F0C)
    MenuCmd(0x01, 0x01, '[EV_02E_12_00]Ａチーム②（ＶＳレクター／ゼノ／レオニダス）', 0x0000300C)
    MenuCmd(0x01, 0x01, '[EV_02E_12_02]Ｂチーム①（ＶＳマリアベル／シャーリィ／カンパネルラ）', 0x0000310C)
    MenuCmd(0x01, 0x01, '[EV_02D_22_00]ミハイル・エイダ・フリッツ・本校男子２・女子１と戦闘', 0x0000330C)
    MenuCmd(0x01, 0x01, '[EV_04_20_00]マリアベル＆カンパネルラとの大ボス戦', 0x0000340C)
    MenuCmd(0x01, 0x01, '[EV_04_23_00]ルーファス＆アルベリヒとの最終決戦', 0x0000350C)
    MenuCmd(0x01, 0x01, '[EV_05_00_04B]≪巨イナルー≫との最終決戦 本体', 0x000001F4)
    MenuCmd(0x01, 0x01, '[EV_05_00_04B]≪巨イナルー≫との最終決戦 巨人', 0x000001F5)
    MenuCmd(0x01, 0x01, '[EV_05_00_04B]≪巨イナルー≫との最終決戦 鳥', 0x000001F6)
    MenuCmd(0x01, 0x01, '閃４[手配魔獣、４チェインバトル] モモイロヒツジンズ', 0x000007D0)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x0000240C, 'loc_355AB'),
        (0x0000250C, 'loc_35610'),
        (0x0000260C, 'loc_35631'),
        (0x0000270C, 'loc_35652'),
        (0x0000290C, 'loc_35673'),
        (0x00002A0C, 'loc_35694'),
        (0x00002B0C, 'loc_356B5'),
        (0x00002C0C, 'loc_356D6'),
        (0x00002E0C, 'loc_356F7'),
        (0x00002D0C, 'loc_35718'),
        (0x00002F0C, 'loc_35739'),
        (0x0000300C, 'loc_3575A'),
        (0x0000310C, 'loc_3577B'),
        (0x0000330C, 'loc_3579C'),
        (0x0000340C, 'loc_357BD'),
        (0x0000350C, 'loc_357DE'),
        (0x000001F4, 'loc_357FF'),
        (0x000001F5, 'loc_358AF'),
        (0x000001F6, 'loc_358D0'),
        (0x000007D0, 'loc_358F1'),
        (0x000007D1, 'loc_35912'),
        (-1, 'loc_35933'),
    )

    def _loc_355AB(): pass

    label('loc_355AB')

    FormationCtrl(0x18)
    FormationCtrl(0x11, 0x0032)
    FormationCtrl(0x11, 0x0033)
    OP_70(0x00, 0x0032, 0x064A, 0xFF, 0x01)
    OP_70(0x00, 0x0033, 0x064B, 0xFF, 0x01)
    OP_70(0x03, 0x0032, 0x0CE4, 0x02, 0x01, 0x01)
    OP_70(0x03, 0x0033, 0x0D16, 0x02, 0x01, 0x01)
    OP_48(0x00, 0x0032, 0x002F, 0x0000)
    OP_48(0x00, 0x0033, 0x002F, 0x0000)
    OP_69(0x02, 0x0032, 0x0033, 0x0006)
    Battle(0x00, 0x0000000E, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35610(): pass

    label('loc_35610')

    Battle(0x00, 0x0000000F, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35631(): pass

    label('loc_35631')

    Battle(0x00, 0x00000010, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35652(): pass

    label('loc_35652')

    Battle(0x00, 0x00000011, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35673(): pass

    label('loc_35673')

    Battle(0x00, 0x00000013, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35694(): pass

    label('loc_35694')

    Battle(0x00, 0x00000014, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_356B5(): pass

    label('loc_356B5')

    Battle(0x00, 0x00000015, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_356D6(): pass

    label('loc_356D6')

    Battle(0x00, 0x00000016, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_356F7(): pass

    label('loc_356F7')

    Battle(0x00, 0x00000018, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35718(): pass

    label('loc_35718')

    Battle(0x00, 0x00000017, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35739(): pass

    label('loc_35739')

    Battle(0x00, 0x00000019, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_3575A(): pass

    label('loc_3575A')

    Battle(0x00, 0x0000001A, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_3577B(): pass

    label('loc_3577B')

    Battle(0x00, 0x0000001B, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_3579C(): pass

    label('loc_3579C')

    Battle(0x00, 0x0000001D, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_357BD(): pass

    label('loc_357BD')

    Battle(0x00, 0x0000001E, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_357DE(): pass

    label('loc_357DE')

    Battle(0x00, 0x0000001F, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_357FF(): pass

    label('loc_357FF')

    OP_C4(0x00, 0xFF)
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x00, 0x0014)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x01, 0x000F)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0024)
    OP_C4(0x02, 0x02, 0x0025)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0021)
    OP_C4(0x02, 0x02, 0x0018)
    OP_C4(0x02, 0x02, 0x0026)
    OP_C4(0x02, 0x02, 0x0027)
    FormationCtrl(0x18)
    FormationCtrl(0x1D, 0x00)
    FormationCtrl(0x1D, 0x01)
    FormationCtrl(0x1D, 0x02)

    OP_18(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00, 0x00000020, 0x00, 0x00, 0x00000021, 0x00, 0x00000022, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_358AF(): pass

    label('loc_358AF')

    Battle(0x00, 0x00000021, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_358D0(): pass

    label('loc_358D0')

    Battle(0x00, 0x00000022, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_358F1(): pass

    label('loc_358F1')

    Battle(0x00, 0x00000024, 0x00, 0x00, 0x00000024, 0x01, 0x00000024, 0x02, 0x00000024, 0x03, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35912(): pass

    label('loc_35912')

    Battle(0x00, 0x00000023, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Jump('loc_35941')

    def _loc_35933(): pass

    label('loc_35933')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_35941')

    def _loc_35941(): pass

    label('loc_35941')

    Jump('loc_34E2D')

    def _loc_35946(): pass

    label('loc_35946')

    Return()

# id: 0x00D5 offset: 0x35948
@scena.Code('TK_Camp_ChrFlagTest')
def TK_Camp_ChrFlagTest():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_35951(): pass

    label('loc_35951')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35E6A',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.Expr24, 0x800000),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止菜单', 0x00000009, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止保存', 0x0000000A, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 1, 0x351)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止载入', 0x0000000B, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 6, 0x39E)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止暂停菜单', 0x0000000C, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x051F, 3, 0x28FB)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止地图菜单', 0x0000000D, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 2, 0x352)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '装备菜单禁止', 0x0000000E, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 3, 0x353)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止导力器菜单', 0x0000000F, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 4, 0x354)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '道具菜单禁止', 0x00000010, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 5, 0x355)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '状态菜单', 0x00000011, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 6, 0x356)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '链接菜单', 0x00000012, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 7, 0x357)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止操作菜单', 0x00000013, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 2, 0x35A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止服装菜单', 0x00000014, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 1, 0x359)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止系统菜单', 0x00000015, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '顶部显示其他队伍', 0x00000016, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x051F, 7, 0x28FF)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止地图传送', 0x00000017, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0074, 0, 0x3A0)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止A组切换按钮', 0x00000018, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0074, 1, 0x3A1)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '禁止B组切换按钮', 0x00000019, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0074, 2, 0x3A2)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '队伍C转换按钮禁止', 0x0000001A, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x01, '禁止装备变更：武器', 0x0000001E)
    MenuCmd(0x01, 0x01, '禁止更改装备：解除武器', 0x0000001F)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000009, 'loc_35DA0'),
        (0x0000000A, 'loc_35DAA'),
        (0x0000000B, 'loc_35DB2'),
        (0x0000000C, 'loc_35DBA'),
        (0x0000000D, 'loc_35DC2'),
        (0x0000000E, 'loc_35DCA'),
        (0x0000000F, 'loc_35DD2'),
        (0x00000010, 'loc_35DDA'),
        (0x00000011, 'loc_35DE2'),
        (0x00000012, 'loc_35DEA'),
        (0x00000013, 'loc_35DF2'),
        (0x00000014, 'loc_35DFA'),
        (0x00000015, 'loc_35E02'),
        (0x00000016, 'loc_35E0A'),
        (0x00000017, 'loc_35E12'),
        (0x00000018, 'loc_35E1A'),
        (0x00000019, 'loc_35E22'),
        (0x0000001A, 'loc_35E2A'),
        (0x0000001E, 'loc_35E32'),
        (0x0000001F, 'loc_35E47'),
        (-1, 'loc_35E5C'),
    )

    def _loc_35DA0(): pass

    label('loc_35DA0')

    OP_15(0x00800000)

    Jump('loc_35E65')

    def _loc_35DAA(): pass

    label('loc_35DAA')

    OP_12(0x0350)

    Jump('loc_35E65')

    def _loc_35DB2(): pass

    label('loc_35DB2')

    OP_12(0x0351)

    Jump('loc_35E65')

    def _loc_35DBA(): pass

    label('loc_35DBA')

    OP_12(0x039E)

    Jump('loc_35E65')

    def _loc_35DC2(): pass

    label('loc_35DC2')

    OP_12(0x28FB)

    Jump('loc_35E65')

    def _loc_35DCA(): pass

    label('loc_35DCA')

    OP_12(0x0352)

    Jump('loc_35E65')

    def _loc_35DD2(): pass

    label('loc_35DD2')

    OP_12(0x0353)

    Jump('loc_35E65')

    def _loc_35DDA(): pass

    label('loc_35DDA')

    OP_12(0x0354)

    Jump('loc_35E65')

    def _loc_35DE2(): pass

    label('loc_35DE2')

    OP_12(0x0355)

    Jump('loc_35E65')

    def _loc_35DEA(): pass

    label('loc_35DEA')

    OP_12(0x0356)

    Jump('loc_35E65')

    def _loc_35DF2(): pass

    label('loc_35DF2')

    OP_12(0x0357)

    Jump('loc_35E65')

    def _loc_35DFA(): pass

    label('loc_35DFA')

    OP_12(0x035A)

    Jump('loc_35E65')

    def _loc_35E02(): pass

    label('loc_35E02')

    OP_12(0x0359)

    Jump('loc_35E65')

    def _loc_35E0A(): pass

    label('loc_35E0A')

    OP_12(0x035C)

    Jump('loc_35E65')

    def _loc_35E12(): pass

    label('loc_35E12')

    OP_12(0x28FF)

    Jump('loc_35E65')

    def _loc_35E1A(): pass

    label('loc_35E1A')

    OP_12(0x03A0)

    Jump('loc_35E65')

    def _loc_35E22(): pass

    label('loc_35E22')

    OP_12(0x03A1)

    Jump('loc_35E65')

    def _loc_35E2A(): pass

    label('loc_35E2A')

    OP_12(0x03A2)

    Jump('loc_35E65')

    def _loc_35E32(): pass

    label('loc_35E32')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00200000)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00400000)

    Jump('loc_35E65')

    def _loc_35E47(): pass

    label('loc_35E47')

    MenuChrFlagCmd(0x01, ChrTable['黎恩'], 0x00200000)
    MenuChrFlagCmd(0x01, ChrTable['黎恩'], 0x00400000)

    Jump('loc_35E65')

    def _loc_35E5C(): pass

    label('loc_35E5C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_35E65(): pass

    label('loc_35E65')

    Jump('loc_35951')

    def _loc_35E6A(): pass

    label('loc_35E6A')

    Return()

# id: 0x00D6 offset: 0x35E6C
@scena.Code('TK_Camp_OtherFlagTest')
def TK_Camp_OtherFlagTest():
    Return()

# id: 0x00D7 offset: 0x35E70
@scena.Code('TK_Camp_PartyTest')
def TK_Camp_PartyTest():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_35E79(): pass

    label('loc_35E79')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3627A',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '黎恩一人', 0x00000001)
    MenuCmd(0x01, 0x01, '添加空白角色', 0x00000014)
    MenuCmd(0x01, 0x01, '追加尤娜', 0x00000015)
    MenuCmd(0x01, 0x01, '添加库鲁特', 0x00000016)
    MenuCmd(0x01, 0x01, '追加阿尔蒂娜', 0x00000017)
    MenuCmd(0x01, 0x01, '添加穆洁', 0x00000018)
    MenuCmd(0x01, 0x01, '添加亚修', 0x00000019)
    MenuCmd(0x01, 0x01, '4人（ATTACK）', 0x00000002)
    MenuCmd(0x01, 0x01, '6人（ATTACK+SUPPORT）', 0x00000003)
    MenuCmd(0x01, 0x01, '8人（ATTACK+SUPPORT+劳拉·菲）', 0x00000004)
    MenuCmd(0x01, 0x01, '最多预定13人（新7组+旧7组）', 0x00000005)
    MenuCmd(0x01, 0x01, '角色标志：全部复位', 0x0000000A)
    MenuCmd(0x01, 0x01, '角色标志：装备→沙拉', 0x0000000B)
    MenuCmd(0x01, 0x01, '角色标志：服装→沙拉', 0x0000000C)
    MenuCmd(0x01, 0x01, 'NPC：没有', 0x0000001E)
    MenuCmd(0x01, 0x01, 'NPC1', 0x0000001F)
    MenuCmd(0x01, 0x01, 'NPC2', 0x00000020)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_36106'),
        (0x00000002, 'loc_36116'),
        (0x00000003, 'loc_36132'),
        (0x00000004, 'loc_36156'),
        (0x00000005, 'loc_36182'),
        (0x00000014, 'loc_361C2'),
        (0x00000015, 'loc_361D3'),
        (0x00000016, 'loc_361DC'),
        (0x00000017, 'loc_361E5'),
        (0x00000018, 'loc_361EE'),
        (0x00000019, 'loc_361F7'),
        (0x0000001E, 'loc_36200'),
        (0x0000001F, 'loc_36217'),
        (0x00000020, 'loc_3622E'),
        (0x0000000A, 'loc_36245'),
        (0x0000000B, 'loc_36252'),
        (0x0000000C, 'loc_3625F'),
        (-1, 'loc_3626C'),
    )

    def _loc_36106(): pass

    label('loc_36106')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    Jump('loc_36275')

    def _loc_36116(): pass

    label('loc_36116')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    FormationAddMember(ChrTable['悠娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])

    Jump('loc_36275')

    def _loc_36132(): pass

    label('loc_36132')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    FormationAddMember(ChrTable['悠娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['妙婕'])
    FormationAddMember(ChrTable['亞修'])

    Jump('loc_36275')

    def _loc_36156(): pass

    label('loc_36156')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    FormationAddMember(ChrTable['悠娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['妙婕'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['菲'])

    Jump('loc_36275')

    def _loc_36182(): pass

    label('loc_36182')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    FormationAddMember(ChrTable['悠娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['妙婕'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationAddMember(ChrTable['莎拉'])

    Jump('loc_36275')

    def _loc_361C2(): pass

    label('loc_361C2')

    FormationAddMember(ChrTable['？？？'])
    MenuChrFlagCmd(0x00, ChrTable['？？？'], 0x01000000)

    Jump('loc_36275')

    def _loc_361D3(): pass

    label('loc_361D3')

    FormationAddMember(ChrTable['悠娜'])

    Jump('loc_36275')

    def _loc_361DC(): pass

    label('loc_361DC')

    FormationAddMember(ChrTable['庫爾特'])

    Jump('loc_36275')

    def _loc_361E5(): pass

    label('loc_361E5')

    FormationAddMember(ChrTable['亞爾緹娜'])

    Jump('loc_36275')

    def _loc_361EE(): pass

    label('loc_361EE')

    FormationAddMember(ChrTable['妙婕'])

    Jump('loc_36275')

    def _loc_361F7(): pass

    label('loc_361F7')

    FormationAddMember(ChrTable['亞修'])

    Jump('loc_36275')

    def _loc_36200(): pass

    label('loc_36200')

    OP_18(
        0x27,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_36275')

    def _loc_36217(): pass

    label('loc_36217')

    OP_18(
        0x27,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_36275')

    def _loc_3622E(): pass

    label('loc_3622E')

    OP_18(
        0x27,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0x28,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_36275')

    def _loc_36245(): pass

    label('loc_36245')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x03000001)

    Jump('loc_36275')

    def _loc_36252(): pass

    label('loc_36252')

    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000001)

    Jump('loc_36275')

    def _loc_3625F(): pass

    label('loc_3625F')

    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x02000000)

    Jump('loc_36275')

    def _loc_3626C(): pass

    label('loc_3626C')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_36275(): pass

    label('loc_36275')

    Jump('loc_35E79')

    def _loc_3627A(): pass

    label('loc_3627A')

    Return()

# id: 0x00D8 offset: 0x3627C
@scena.Code('ClearLF_TEMP')
def ClearLF_TEMP():
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Return()

# id: 0x00D9 offset: 0x36290
@scena.Code('TK_Camp_Orbment')
def TK_Camp_Orbment():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_36299(): pass

    label('loc_36299')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36561',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ClearLF_TEMP')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['黎恩'], 0x00200000)"),
            Expr.Return,
        ),
        'loc_362D2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_362D2(): pass

    label('loc_362D2')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['黎恩'], 0x00400000)"),
            Expr.Return,
        ),
        'loc_362E4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_362E4(): pass

    label('loc_362E4')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['黎恩'], 0x00800000)"),
            Expr.Return,
        ),
        'loc_362F6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_362F6(): pass

    label('loc_362F6')

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, '所有槽强化初始化', 0x00000002)
    MenuCmd(0x01, 0x01, '所有槽强化（LV1）', 0x00000004)
    MenuCmd(0x01, 0x01, '所有槽最大强化（LV2）', 0x00000005)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '锁定核心回路', 0x0000000A, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '锁定：黎恩的核心回路', 0x0000000B, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '锁定：导力器的所有回路', 0x0000000C, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x01, '封面更换测试', 0x00000064)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_36486'),
        (0x00000002, 'loc_36493'),
        (0x00000003, 'loc_364A0'),
        (0x00000004, 'loc_364AD'),
        (0x00000005, 'loc_364BA'),
        (0x0000000A, 'loc_364C7'),
        (0x0000000B, 'loc_364D4'),
        (0x0000000C, 'loc_364E1'),
        (0x00000064, 'loc_364EE'),
        (-1, 'loc_36553'),
    )

    def _loc_36486(): pass

    label('loc_36486')

    OP_70(0x06, 0xFFFF, 0xFF, 0x01, 0x00, 0x01)

    Jump('loc_3655C')

    def _loc_36493(): pass

    label('loc_36493')

    OP_70(0x06, 0xFFFF, 0xFF, 0x01, 0x01, 0x01)

    Jump('loc_3655C')

    def _loc_364A0(): pass

    label('loc_364A0')

    OP_70(0x06, 0xFFFF, 0x01, 0x01, 0x00, 0x01)

    Jump('loc_3655C')

    def _loc_364AD(): pass

    label('loc_364AD')

    OP_70(0x06, 0xFFFF, 0xFF, 0x02, 0x01, 0x01)

    Jump('loc_3655C')

    def _loc_364BA(): pass

    label('loc_364BA')

    OP_70(0x06, 0xFFFF, 0xFF, 0x03, 0x01, 0x01)

    Jump('loc_3655C')

    def _loc_364C7(): pass

    label('loc_364C7')

    MenuChrFlagCmd(0x02, ChrTable['黎恩'], 0x00200000)

    Jump('loc_3655C')

    def _loc_364D4(): pass

    label('loc_364D4')

    MenuChrFlagCmd(0x02, ChrTable['黎恩'], 0x00400000)

    Jump('loc_3655C')

    def _loc_364E1(): pass

    label('loc_364E1')

    MenuChrFlagCmd(0x02, ChrTable['黎恩'], 0x00800000)

    Jump('loc_3655C')

    def _loc_364EE(): pass

    label('loc_364EE')

    OP_A3(0x000A, 0x0E75)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'ユウナのアークスカバーを ITM_COVER_BASE2 にしました。',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_3655C')

    def _loc_36553(): pass

    label('loc_36553')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3655C(): pass

    label('loc_3655C')

    Jump('loc_36299')

    def _loc_36561(): pass

    label('loc_36561')

    Call(ScriptId.Current, 'ClearLF_TEMP')

    Return()

# id: 0x00DA offset: 0x36574
@scena.Code('TK_Camp_MQuartz')
def TK_Camp_MQuartz():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_36584(): pass

    label('loc_36584')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36E67',
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x00, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x00, '全部获得', 0x00000001)
    MenuCmd(0x01, 0x00, '全核心回路LV2', 0x00000002)
    MenuCmd(0x01, 0x00, '全核心回路LV3', 0x00000003)
    MenuCmd(0x01, 0x00, '全部核心回路LV4', 0x00000004)
    MenuCmd(0x01, 0x00, '全核心回路LVMAX', 0x00000005)
    MenuCmd(0x01, 0x00, '装备客人专用核心回路', 0x0000000A)
    MenuCmd(0x01, 0x00, '检查是否配备了特定的核心回路', 0x0000000B)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x00, 0xF7)
    MenuCmd(0x03, 0x00)

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_366B4',
    )

    AddItem(0x0F, 0x00C9, 1)
    AddItem(0x0F, 0x00C8, 3)

    Jump('loc_36E62')

    def _loc_366B4(): pass

    label('loc_366B4')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3683B',
    )

    OP_70(0x0A, 0x0C9D, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C9C, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C9B, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C9A, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C99, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C98, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C97, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C96, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C95, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C94, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C93, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C92, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C91, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C90, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C8F, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C8E, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C8D, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C8C, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C8B, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C8A, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C89, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C88, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C87, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C86, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C85, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C84, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C83, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C82, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C81, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x000006A3, 0x00000001)

    Jump('loc_36E62')

    def _loc_3683B(): pass

    label('loc_3683B')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_369C2',
    )

    OP_70(0x0A, 0x0C9D, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C9C, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C9B, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C9A, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C99, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C98, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C97, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C96, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C95, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C94, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C93, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C92, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C91, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C90, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8F, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8E, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8D, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8C, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8B, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8A, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C89, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C88, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C87, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C86, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C85, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C84, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C83, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C82, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C81, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x00001837, 0x00000001)

    Jump('loc_36E62')

    def _loc_369C2(): pass

    label('loc_369C2')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36B49',
    )

    OP_70(0x0A, 0x0C9D, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C9C, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C9B, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C9A, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C99, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C98, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C97, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C96, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C95, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C94, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C93, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C92, 0x000006A3, 0x00000001)
    OP_70(0x0A, 0x0C91, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C90, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8F, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8E, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8D, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8C, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8B, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C8A, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C89, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C88, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C87, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C86, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C85, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C84, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C83, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C82, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C81, 0x00001837, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x00001837, 0x00000001)

    Jump('loc_36E62')

    def _loc_36B49(): pass

    label('loc_36B49')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36CD0',
    )

    OP_70(0x0A, 0x0C9D, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C9C, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C9B, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C9A, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C99, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C98, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C97, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C96, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C95, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C94, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C93, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C92, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C91, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C90, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C8F, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C8E, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C8D, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C8C, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C8B, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C8A, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C89, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C88, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C87, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C86, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C85, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C84, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C83, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C82, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C81, 0x00061A80, 0x00000001)
    OP_70(0x0A, 0x0C80, 0x00061A80, 0x00000001)

    Jump('loc_36E62')

    def _loc_36CD0(): pass

    label('loc_36CD0')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36D64',
    )

    AddItem(0x00, 0x0CAF, 1)
    OP_70(0x03, 0x000A, 0x0CAF, 0x00, 0x00, 0x01)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00200000)
    AddItem(0x0F, 0x00C9, 1)
    OP_70(0x03, 0x000A, 0x0CB0, 0x01, 0x00, 0x01)
    AddItem(0x0F, 0x0CB0, 1)
    OP_70(0x06, 0x000A, 0x01, 0x01, 0x00, 0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'ユウナにマスタークオーツＥｘを装備',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_36E62')

    def _loc_36D64(): pass

    label('loc_36D64')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36E59',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x05, 0xFFFF, 0x0C81, 0x01, 0x01)"),
            Expr.Return,
        ),
        'loc_36DED',
    )

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'サブスロットに「スクルド」装備者あり(全ての味方キャラ内)',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    Jump('loc_36E54')

    def _loc_36DED(): pass

    label('loc_36DED')

    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    Talk(
        0xFFFF,
        (
            'サブスロットに「スクルド」装備者なし(全ての味方キャラ内)',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)

    def _loc_36E54(): pass

    label('loc_36E54')

    Jump('loc_36E62')

    def _loc_36E59(): pass

    label('loc_36E59')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_36E62(): pass

    label('loc_36E62')

    Jump('loc_36584')

    def _loc_36E67(): pass

    label('loc_36E67')

    Return()

# id: 0x00DB offset: 0x36E68
@scena.Code('TK_Camp_Link')
def TK_Camp_Link():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'リンクをそれっぽくしてみる', 0x00000001)
    MenuCmd(0x01, 0x01, '新老Ⅶ组', 0x00000002)
    MenuCmd(0x01, 0x01, '历代轨迹组', 0x00000003)
    MenuCmd(0x01, 0x01, '利贝尔（嘉宾）组', 0x00000004)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_36F31'),
        (0x00000002, 'loc_36FB0'),
        (0x00000003, 'loc_3703D'),
        (0x00000004, 'loc_370B2'),
        (-1, 'loc_37107'),
    )

    def _loc_36F31(): pass

    label('loc_36F31')

    OP_69(0x00, 0x0000, 0x000A, 0xFF, 0x00, 0x00)
    OP_69(0x00, 0x000B, 0x000C, 0xFF, 0x00, 0x00)
    OP_69(0x02, 0x0000, 0x000A, 0x0005)
    OP_69(0x02, 0x0000, 0x000B, 0x0004)
    OP_69(0x02, 0x0000, 0x000C, 0x0003)
    OP_69(0x02, 0x0000, 0x000D, 0x0002)
    OP_69(0x02, 0x0000, 0x000E, 0x0001)
    OP_69(0x05, 0x0000, 0x0001, 0x03E8)
    OP_69(0x05, 0x0000, 0x0002, 0x05DC)
    OP_69(0x05, 0x0000, 0x0003, 0x07D0)
    OP_69(0x05, 0x0000, 0x0004, 0x09C4)
    OP_69(0x05, 0x0000, 0x0005, 0x0BB8)
    OP_69(0x05, 0x0000, 0x000F, 0x0DAC)
    OP_69(0x05, 0x0000, 0x0009, 0x0FA0)
    OP_69(0x05, 0x0000, 0x0008, 0x1194)

    Jump('loc_37110')

    def _loc_36FB0(): pass

    label('loc_36FB0')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x0000000E)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['悠娜'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['妙婕'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['克蕾雅少校'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000004)

    Jump('loc_37110')

    def _loc_3703D(): pass

    label('loc_3703D')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x0000000E)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['緹妲'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['緋之羅賽莉亞'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['雷克多少校'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['派崔克'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['湯瑪斯'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000004)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000004)

    Jump('loc_37110')

    def _loc_370B2(): pass

    label('loc_370B2')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x0000000E)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['奧蕾莉亞分校長'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['喬治'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['亞爾賽德子爵'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['剛毅艾奈絲'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['魔弓恩奈雅'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['陷阱師傑諾'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['破壞獸雷歐尼達斯'], 0x00000002)
    MenuChrFlagCmd(0x00, ChrTable['測試：恩奈雅'], 0x00000002)

    Jump('loc_37110')

    def _loc_37107(): pass

    label('loc_37107')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_37110(): pass

    label('loc_37110')

    Return()

# id: 0x00DC offset: 0x37114
@scena.Code('TK_Camp_Formation')
def TK_Camp_Formation():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)
    MenuCmd(0x01, 0x01, 'リィン、ユウナ、クルト、アルティナ、アッシュ、ミュゼの戦闘フォーメーション', 0x00000001)
    MenuCmd(0x01, 0x01, 'リィン、ユウナ、クルト、アルティナ、アッシュ、ミュゼの同座標配置テスト１', 0x00000002)
    MenuCmd(0x01, 0x01, 'リィン、ユウナ、クルト、アルティナ、アッシュ、ミュゼの同座標配置テスト２', 0x00000003)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000001, 'loc_372BA'),
        (0x00000002, 'loc_3730D'),
        (0x00000003, 'loc_37360'),
        (-1, 'loc_373B3'),
    )

    def _loc_372BA(): pass

    label('loc_372BA')

    FormationCtrl(0x08, 0x0000, -1.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000A, 1.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000B, -2.0, 1.0, 0x00)
    FormationCtrl(0x08, 0x000C, 2.0, 1.0, 0x00)
    FormationCtrl(0x08, 0x000E, -1.0, 2.0, 0x00)
    FormationCtrl(0x08, 0x000D, 1.0, 2.0, 0x00)

    Jump('loc_373BC')

    def _loc_3730D(): pass

    label('loc_3730D')

    FormationCtrl(0x08, 0x0000, -1.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000A, -1.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000B, -1.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000C, -1.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000E, -1.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000D, -1.0, 0.0, 0x00)

    Jump('loc_373BC')

    def _loc_37360(): pass

    label('loc_37360')

    FormationCtrl(0x08, 0x0000, -2.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000A, -2.0, 0.0, 0x00)
    FormationCtrl(0x08, 0x000B, -0.25, 1.0, 0x00)
    FormationCtrl(0x08, 0x000C, 0.25, 1.0, 0x00)
    FormationCtrl(0x08, 0x000E, 2.0, 3.0, 0x00)
    FormationCtrl(0x08, 0x000D, 2.0, 3.0, 0x00)

    Jump('loc_373BC')

    def _loc_373B3(): pass

    label('loc_373B3')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_373BC(): pass

    label('loc_373BC')

    Return()

# id: 0x00DD offset: 0x373C0
@scena.Code('TK_Camp_CantUseItem')
def TK_Camp_CantUseItem():
    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_373D2(): pass

    label('loc_373D2')

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_375F5',
    )

    Call(ScriptId.Current, 'ClearLF_TEMP')

    If(
        (
            (Expr.Eval, "AddItem(0x17, 0x0000, 0)"),
            Expr.Return,
        ),
        'loc_37402',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_37402(): pass

    label('loc_37402')

    If(
        (
            (Expr.Eval, "AddItem(0x17, 0x000A, 0)"),
            Expr.Return,
        ),
        'loc_37414',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_37414(): pass

    label('loc_37414')

    If(
        (
            (Expr.Eval, "AddItem(0x17, 0x0032, 0)"),
            Expr.Return,
        ),
        'loc_37426',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_37426(): pass

    label('loc_37426')

    If(
        (
            (Expr.Eval, "AddItem(0x17, 0x0028, 0)"),
            Expr.Return,
        ),
        'loc_37438',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_37438(): pass

    label('loc_37438')

    MenuCmd(0x00, 0x01, 0x0000, 40.0, 0x00000000)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'ティアの薬 を使用禁止する', 0x00000000, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'セラスの薬 を使用禁止する', 0x0000000A, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, '命の雫 を使用禁止する', 0x00000032, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0x01, 'パワーポーション を使用禁止する', 0x00000028, (0x11, 0x0, 0x0), (0xFF, 0x1, 0x0))
    MenuCmd(0x01, 0x01, '全使用禁止解除', 0x000003E7)
    MenuCmd(0x02, 0x01, 0x01, 0xFFFF, 0xFFFF, 0x00)
    MenuCmd(0x04, 0x01, 0xF7)
    MenuCmd(0x03, 0x01)

    Switch(
        (
            (Expr.Expr23, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_375A6'),
        (0x0000000A, 'loc_375B3'),
        (0x00000032, 'loc_375C0'),
        (0x00000028, 'loc_375CD'),
        (0x000003E7, 'loc_375DA'),
        (-1, 'loc_375E7'),
    )

    def _loc_375A6(): pass

    label('loc_375A6')

    AddItem(0x16, 0x0000, 0)

    Jump('loc_375F0')

    def _loc_375B3(): pass

    label('loc_375B3')

    AddItem(0x16, 0x000A, 0)

    Jump('loc_375F0')

    def _loc_375C0(): pass

    label('loc_375C0')

    AddItem(0x16, 0x0032, 0)

    Jump('loc_375F0')

    def _loc_375CD(): pass

    label('loc_375CD')

    AddItem(0x16, 0x0028, 0)

    Jump('loc_375F0')

    def _loc_375DA(): pass

    label('loc_375DA')

    AddItem(0x15, 0x270F, 0)

    Jump('loc_375F0')

    def _loc_375E7(): pass

    label('loc_375E7')

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_375F0(): pass

    label('loc_375F0')

    Jump('loc_373D2')

    def _loc_375F5(): pass

    label('loc_375F5')

    Call(ScriptId.Current, 'ClearLF_TEMP')

    Return()

# id: 0x00DE offset: 0x37608
@scena.Code('TK_Jump_Tmp')
def TK_Jump_Tmp():
    OP_04(0x14, 'EV_DoJump_04')

    Return()

# id: 0x00DF offset: 0x37618
@scena.Code('TK_EV_Jump')
def TK_EV_Jump():
    Call(ScriptId.System, 'FC_TalkBegin', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    OP_C9(0x02)

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_37651(): pass

    label('loc_37651')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37ECF',
    )

    MenuCmd(0x00, 0x00, 0x0018, 40.0, 0x00000000)

    If(
        (
            (Expr.Expr23, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37ECA',
    )

    MenuCmd(0x01, 0x00, '[00_00]  序', 0x00000001)
    MenuCmd(0x01, 0x00, '[01A_00] 第Ⅰ部　０サングラール迷宮', 0x00000002)
    MenuCmd(0x01, 0x00, '[01B_00] 第Ⅰ部　①サザーラント方面', 0x00000003)
    MenuCmd(0x01, 0x00, '[01C_00] 第Ⅰ部　②ラマール方面', 0x00000004)
    MenuCmd(0x01, 0x00, '[01D_00] 第Ⅰ部　③クロスベル方面', 0x00000005)
    MenuCmd(0x01, 0x00, '[01X_00] 断章', 0x00000006)
    MenuCmd(0x01, 0x00, '[02A_00] 第Ⅱ部　０これからについて', 0x00000007)
    MenuCmd(0x01, 0x00, '[02A_04] 第Ⅱ部　①ブリオニア編', 0x00000008)
    MenuCmd(0x01, 0x00, '[02B_00] 第Ⅱ部　②オルディス編', 0x00000009)
    MenuCmd(0x01, 0x00, '[02C_00] 第Ⅱ部　③ドレックノール編', 0x0000000A)
    MenuCmd(0x01, 0x00, '[02D_00] 第Ⅱ部　④リーヴス～士官学校編', 0x0000000B)
    MenuCmd(0x01, 0x00, '[02E_00] 第Ⅱ部　⑤パンタグリュエル編', 0x0000000C)
    MenuCmd(0x01, 0x00, '[03A_00] 第Ⅲ部　０カレイジャスⅡ始動', 0x0000000D)
    MenuCmd(0x01, 0x00, '[03A_02] 第Ⅲ部　①月の霊場編', 0x0000000E)
    MenuCmd(0x01, 0x00, '[03B_00] 第Ⅲ部　②ガルガンチュア編', 0x0000000F)
    MenuCmd(0x01, 0x00, '[03C_00] 第Ⅲ部　③龍の霊場編', 0x00000010)
    MenuCmd(0x01, 0x00, '[03D_00] 第Ⅲ部　④裏オルキスタワー編', 0x00000011)
    MenuCmd(0x01, 0x00, '[03E_00] 第Ⅲ部　⑤星の霊場編', 0x00000012)
    MenuCmd(0x01, 0x00, '[03X_00] 前日譚', 0x00000013)
    MenuCmd(0x01, 0x00, '[04_00]  最終幕　０作戦開始前～最終行動タイミング', 0x00000014)
    MenuCmd(0x01, 0x00, '[04_02]  最終幕　①ヨルムンガンド作戦開始～《杭》', 0x00000015)
    MenuCmd(0x01, 0x00, '[04_07]  最終幕　②《幻想機動要トゥアハ＝デ＝ダナーン》攻略', 0x00000016)
    MenuCmd(0x01, 0x00, '[05_00]  大団円　①《巨イナル一》との戦い～決着', 0x00000017)
    MenuCmd(0x01, 0x00, '[05_02]  大団円　②それから～トゥルーエンド', 0x00000018)
    MenuCmd(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x01)
    MenuCmd(0x04, 0x00, 0xF6)
    MenuCmd(0x03, 0x00)

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.Expr23, 0xF6),
            Expr.Return,
        ),
        (0x00000001, 'loc_37C8C'),
        (0x00000002, 'loc_37CA2'),
        (0x00000003, 'loc_37CB9'),
        (0x00000004, 'loc_37CD0'),
        (0x00000005, 'loc_37CE7'),
        (0x00000006, 'loc_37CFE'),
        (0x00000007, 'loc_37D15'),
        (0x00000008, 'loc_37D2C'),
        (0x00000009, 'loc_37D43'),
        (0x0000000A, 'loc_37D5A'),
        (0x0000000B, 'loc_37D71'),
        (0x0000000C, 'loc_37D88'),
        (0x0000000D, 'loc_37D9F'),
        (0x0000000E, 'loc_37DB6'),
        (0x0000000F, 'loc_37DCD'),
        (0x00000010, 'loc_37DE4'),
        (0x00000011, 'loc_37DFB'),
        (0x00000012, 'loc_37E12'),
        (0x00000013, 'loc_37E29'),
        (0x00000014, 'loc_37E40'),
        (0x00000015, 'loc_37E56'),
        (0x00000016, 'loc_37E6C'),
        (0x00000017, 'loc_37E82'),
        (0x00000018, 'loc_37E98'),
    )





