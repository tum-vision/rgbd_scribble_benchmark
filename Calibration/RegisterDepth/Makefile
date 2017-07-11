CC = clang++
CFLAGS = `pkg-config --cflags opencv`
CFLAGS += -g -Wall -Wextra
LIBS = `pkg-config --libs opencv`

registerDepth : registerDepth.cpp
	$(CC) $(CFLAGS) $(LIBS) -o $@ $<

clean:
	rm registerDepth
