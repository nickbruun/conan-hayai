VERSION := 1.0.2

all: clean build package export test

clean:
	rm -rf build package

build:
	conan build .

package:
	conan package .

export:
	conan export . hayai/${VERSION}

test:
	conan create . dev/testing

.PHONY: all clean build package export test
