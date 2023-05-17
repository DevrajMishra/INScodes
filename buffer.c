#include <stdio.h>

int main() {
        struct {
                char text[5];
                short int code;
        } local;
        local.code = 0;
        gets(local.text);
        puts(local.code);
        if (local.code == 97) {
                puts("Buffer overflow successful");
        } else {
                puts("Buffer overflow unsuccessful");
        }
        return 0;
}