#include "interface.h"

int main(void) {
	char buffer[5] = {0};
	in(buffer, 5);
	int output = out(buffer);
	if(output > 4){
		char buffer2[5];
		in(buffer2, 6);
		out(buffer2);
	}
	
    	return 0;
}
