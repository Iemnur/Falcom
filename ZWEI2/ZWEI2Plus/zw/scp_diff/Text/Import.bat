:: ����ȡ���ı�д�ؽű��С�

@FOR %%i in (EV*.txt) DO @(
	Title Importing %%~nxi
	ZWEI2Scp.exe -i "MES_%%~nxi" "%%~nxi"
)