#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Print the bytes information
 *
 * @p: Python Object
 * Return: There is no return.
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, a, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (a = 0; a < limit; a++)
		if (string[a] >= 0)
			printf(" %02x", string[a]);
		else
			printf(" %02x", 256 + string[a]);

	printf("\n");
}

/**
 * print_python_list - Prints the list information
 *
 * @p: Python Object
 * Return: There is no return
 */
void print_python_list(PyObject *p)
{
	long int size, b;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (b = 0; b < size; b++)
	{
		obj = ((PyListObject *)p)->ob_item[b];
		printf("Element %ld: %s\n", b, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
