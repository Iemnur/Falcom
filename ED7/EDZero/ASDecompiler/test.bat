@ECHO OFF
cd/d "%~dp0"

call cl.bat as00500.asm
move /y as04540.dat J:\Falcom\ED_Zero\patch\battle\dat\as04540.dat

IF [%1] == [1] start "" "E:\Desktop\Ӣ�۴�˵ ��֮�켣.lnk"