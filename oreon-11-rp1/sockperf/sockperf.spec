%global source0_hash 5373385e78921ba7156e03629daa0a2243b388d4c2b0c8ff99218d2a3e3be7a1
Name:           sockperf
Version:        3.10
Release:        1%{?dist}
Summary:        Network benchmarking utility for testing latency and throughput
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/Mellanox/%{name}
Source0:        https://github.com/Mellanox/%{name}/archive/%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
sockperf is a network benchmarking utility over socket API that was designed
for testing performance (latency and throughput) of high-performance systems
(it is also good for testing performance of regular networking systems as
well). It covers most of the socket API calls and options.

Specifically, in addition to the standard throughput tests, sockperf, does the
following:

* Measure latency of each discrete packet at sub-nanosecond resolution (using
  TSC register that counts CPU ticks with very low overhead).

* Does the above for both ping-pong mode and for latency under load mode. This
  means that we measure latency of single packets even under load of millions
  Packets Per Second (without waiting for reply of packet before sending
  subsequent packet on time)

* Enable spike analysis by providing histogram, with various percentiles of the
  packets’ latencies (for example: median, min, max, 99%% percentile, and more),
  (this is in addition to average and standard deviation). Also, sockperf
  provides full log with all packet’s tx/rx times that can be further analyzed
  with external tools, such as MS-Excel or matplotlib - All this without
  affecting the benchmark itself.

* Support MANY optional settings for good coverage of socket API and network
  configurations, while still keeping very low overhead in the fast path to
  allow cleanest results.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
export CXXFLAGS='%{optflags} -O3'
%configure --enable-doc
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
