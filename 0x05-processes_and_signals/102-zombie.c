#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


/**
 * infinite_while - loop forever
 *
 * Return: Never
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - spawn zombie processes
 *
 * Return: Never
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (!pid)
			return (EXIT_SUCCESS);
		printf("Zombie process created, PID: %d\n", pid);
	}
	return (infinite_while());
}
