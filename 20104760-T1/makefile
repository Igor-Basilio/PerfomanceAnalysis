
CC = g++
CFLAGS = -Wall -O3 -std=c++20

EXECUTAVEL=ord
FONTES=20104760.cpp
OBJETOS=$(FONTES:.cpp=.o)

$(EXECUTAVEL): $(OBJETOS)
	$(CC) $(CFLAGS) -o $@ $^ 

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

run: $(EXECUTAVEL)
	./$(EXECUTAVEL) $(TAMANHO)

clean:
	rm -f ${OBJETOS} ${EXECUTAVEL}

.PHONY: run clean

