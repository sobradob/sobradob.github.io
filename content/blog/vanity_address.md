---
title: How to generate a Bitcoin vanity address using a Mac
description: Generating a vanity address
toc: true
tags:
categories:
series: hacking
date: '2018-08-11T13:11:22+08:00'
featuredImage:
draft: false

---

A bitcoin vanity address is an address that starts in a particular way. Here is an example:

Once I saw these addresses exist, I obviously wanted one. There are many websites that help you generate a vanity address, however it involves a trusted third party. Nick Szabo doesn't like [trusted third parties](https://nakamotoinstitute.org/trusted-third-parties/).

There are [clear, up to date instructions](https://99bitcoins.com/how-to-get-a-custom-bitcoin-address/) on how to do this on Windows. The only thing I found on Mac was [this](http://www.stanley-adams.co.uk/2013/12/custom-vanity-bitcoin-address/) blogpost from 2013. I thought I'd write slightly more up to date version of what worked for me. I'd like to point out that I'm merely following instructions and stumbling through things, so do not think of this as an authoritative source.

I already had homebrew installed, so I simply ran:

```
brew install pcre pcre++ openssl

```

This first updated homebrew and installed the missing dependencies, with the exception of "pcre++". I then checked the version of 'openssl', which looked fine given how old the Github of the vanity gen software was. I ignored all the other bits regarding paths, assuming it would work without it. It did.

Next I ran

```
git clone https://github.com/samr7/vanitygen.git

```

Then, following instructions I opened `pattern.h` and change the line "#define INLINE inline" to "#define INLINE". Subsequently I opened Makefile in TextEdit, and removed the following lines:

```
LIBS=-lpcre -lcrypto -lm -lpthread
CFLAGS=-ggdb -o3 -Wall

```

Replacing them with:

```
LIBS= -lpcre -lcrypto -lm -lpthread
INCPATHS=-I$(shell brew --prefix)/include -I$(shell brew --prefix openssl)/include
LIBPATHS=-L$(shell brew --prefix)/lib -L$(shell brew --prefix openssl)/lib
CFLAGS=-ggdb -O3 -Wall -Qunused-arguments $(INCPATHS) $(LIBPATHS)

```

Then I stepped into terminal, into the source file where all the cloned files were and ran `make all`. The next step was simply to run:

```
./vanitygen 1Boaz

Difficulty: 264104224
ERROR: could not determine processor count
Pattern: 1boaz
Address: 1boazgdG5CUdH2FxgqQjs9YCS81eWvdLZ
Privkey: 5Jai5QTiq3UQCfkLYqhQQVvzJC711tm44SxgqkzkvCHNFpkeyek

```

Next, I decided to try to generate it using my GPU so it would go faster. I stumbled around a little with the exact way of doing it, because while I understood I needed to run `oclvanitygen`, I could not get past this:

```
Difficulty: 4476342
Available OpenCL platforms:
0: [Apple] Apple
  0: [Intel] Intel(R) Core(TM) i5-7267U CPU @ 3.10GHz
  1: [Intel Inc.] Intel(R) Iris(TM) Graphics 650

```

In the end this seems to have worked to select the GPU:

```
./oclvanitygen -D 0:0 0:1 1Boaz
```
