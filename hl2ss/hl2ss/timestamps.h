
#pragma once

#include <winrt/Windows.Perception.h>

#define HNS_BASE (10ULL * 1000ULL * 1000ULL)

UINT64 QPCTickstoQPCTimestamp(LARGE_INTEGER const& pc);
UINT64 FTToU64(FILETIME const& ft);
UINT64 GetCurrentQPCTimestamp();
UINT64 GetCurrentUTCTimestamp();
UINT64 GetQPCToUTCOffset();
winrt::Windows::Perception::PerceptionTimestamp QPCTimestampToPerceptionTimestamp(LONGLONG qpctime);
