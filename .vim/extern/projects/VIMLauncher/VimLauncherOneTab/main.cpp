#include "stdafx.h"

//
// Entry point for the console application.
//
int _tmain(int argc, _TCHAR* argv[])
{
	char * pgVimExe = "C:\\Users\\sbenner\\AppData\\Roaming\\Vim\\vim72\\gvim.exe";
/*
	pgVimExe = std::getenv ("GVIM_EXECUTABLE");
	bool bError = false;
	if (pgVimExe == NULL)
	{
		std::cout << "Error: Cannot find environment variable GVIM_EXECUTABLE";
		bError = true;
	}
	else if (argc < 2)
	{
		std::cout << "Error: Invalid number of argument.";
		bError = true;
	}
	if (bError)
	{
		return 1;
	}
*/
	std::string sCall("start \"\" \"");
	sCall += pgVimExe;
	sCall += "\" --remote-silent";
	for (int i=1; i<argc; ++i)
	{
		sCall += " \"";
		sCall += argv[i];
		sCall += "\"";
	}

#ifdef _DEBUG
	std::cout << "Calling " << sCall.c_str() << "...";
	std::cout << "\n";
	std::system("pause");
#endif

	// call system command
	std::system(sCall.c_str());

	return 0;
}

