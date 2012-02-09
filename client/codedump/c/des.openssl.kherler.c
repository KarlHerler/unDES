#include <stdio.h>      /* fprintf */
#include <stdlib.h>     /* malloc, free, exit */ 
#include <unistd.h>
#include <string.h>     /* strerror */
#include <signal.h>
#include <openssl/des.h>

static long long unsigned nrkeys = 0; // performance counter

char *
Encrypt( char *Key, char *Msg, int size)
{
        static char*    Res;
        free(Res);
        int             n=0;
        DES_cblock      Key2;
        DES_key_schedule schedule;
        Res = ( char * ) malloc( size );
        /* Prepare the key for use with DES_ecb_encrypt */
        memcpy( Key2, Key,8);
        DES_set_odd_parity( &Key2 );
        DES_set_key_checked( &Key2, &schedule );
        /* Encryption occurs here */
        DES_ecb_encrypt( ( unsigned char (*) [8] ) Msg, ( unsigned char (*) [8] ) Res,
                           &schedule, DES_ENCRYPT );
         return (Res);
}

char *
Decrypt( char *Key, char *Msg, int size)
{
        static char*    Res;
        free(Res);
        int             n=0;
        DES_cblock      Key2;
        DES_key_schedule schedule;
        Res = ( char * ) malloc( size );
        /* Prepare the key for use with DES_ecb_encrypt */
        memcpy( Key2, Key,8);
        DES_set_odd_parity( &Key2 );
        DES_set_key_checked( &Key2, &schedule );
        /* Decryption occurs here */
        DES_ecb_encrypt( ( unsigned char (*) [8]) Msg, ( unsigned char (*) [8]) Res,
                           &schedule, DES_DECRYPT );
        return (Res);
}

void ex_program(int sig);

int main(int argc, char const *argv[])
{
    (void) signal(SIGINT, ex_program);

    FILE *f, *g; 
    int counter, i, prime = 0, len = 8; 
    char cbuff[8], mbuff[8];
    char letters[] = "02468ACEGIKMOQSUWYZacegikmoqsuwyz"; 
    //char letters[] = "86421"; 
    int nbletters = sizeof(letters)-1;
    int entry[len];
    char *password, *decrypted, *plain;


    if (argv[1]) {
        prime = atoi(argv[1]);   
    }

    f = fopen("encrypt6.dat", "rb");
    if(!f) {
        printf("Unable to open the file\n");
        return 1;
    }
    for (counter = 0; counter < 8; counter ++) cbuff[counter] = fgetc(f);
    fclose(f);


    g = fopen("plain6.txt", "r");
    if(!g) {
        printf("Unable to open the file\n");
        return 1;
    }
    for (counter = 0; counter < 8; counter ++) mbuff[counter] = fgetc(g);
    fclose(g);
    plain = malloc(8);
    memcpy(plain, mbuff, 8);


    for(i=0 ; i<len ; i++) entry[i] = 0;
    entry[len-1] = prime;

    password = malloc(8);
    decrypted = malloc(8);

    do {
        
        //getting key
        for(i=0 ; i<len ; i++) password[i] = letters[entry[i]];
        nrkeys++;

        //UI output
        if(nrkeys % 10000000 == 0) {
            printf("Current key: %s\n", password);
        }

        //decrypting and grabbing the first 8 bytes.
        memcpy(decrypted,Decrypt(password,cbuff,8), 8);

        
        //exitpoint if found
        if (strcmp(plain, decrypted) == 0)
        {
            printf("We've got it! The key is: %s\n", password);
            printf("%lld keys searched", nrkeys);
            free(plain);
            free(password);
            free(decrypted);
            exit(0);
        }

        //next key
        for(i=0 ; i<len && ++entry[i] == nbletters; i++) entry[i] = 0;
    } while(i<len);

    free(password);
    free(decrypted);

    fprintf(stderr, "Nothing found. \n");
    free(plain);
    return 0;
}

void ex_program(int sig) {
 printf("\n\nProgram terminated %lld keys searched.\n", nrkeys);
 (void) signal(SIGINT, SIG_DFL);
 exit(0);
}