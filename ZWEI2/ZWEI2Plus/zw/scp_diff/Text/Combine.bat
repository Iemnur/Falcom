:: ��MES_*.txt��ϳ�Tran.txt�������޸ġ�

@ECHO OFF&SETLOCAL ENABLEDELAYEDEXPANSION
CD/D "%~dp0"
FOR %%i IN (MES_*.txt) DO (
	Set File=%%i
	ECHO [FILENAME] %~dp0!File:~4!>>Tran.txt
	Type %%i>>Tran.txt
)