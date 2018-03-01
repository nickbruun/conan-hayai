#include <hayai/hayai.hpp>

#ifdef _WIN32
#ifndef NOMINMAX
#define NOMINMAX
#endif
#include <windows.h>

inline void msleep(unsigned int duration)
{
    Sleep(duration);
}

#else
#include <unistd.h>

inline void msleep(unsigned int duration)
{
    usleep(duration * 1000);
}
#endif

BENCHMARK(SomeSleep, Sleep10ms, 5, 10)
{
    msleep(10);
}
