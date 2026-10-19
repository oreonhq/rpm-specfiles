%global source0_hash 26661a569a7def45a2e97fbbd09e0dc5bbb2f8ab1b41250c19e795559eec6fb2
Name:           libaec
Version:        1.1.7
Release:        1%{?dist}
Summary:        Adaptive Entropy Coding library
License:        LicenseRef-Callaway-BSD
Url:            https://gitlab.dkrz.de/k202009/libaec
Source0:        https://github.com/MathisRosenhauer/libaec/archive/v%{version}/libaec-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
%description
Libaec provides fast loss-less compression of 1 up to 32 bit wide
signed or unsigned integers (samples). The library achieves best
results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate
simulations. While floating point representations are not directly
supported, they can also be efficiently coded by grouping exponents
and mantissa.

Libaec implements Golomb Rice coding as defined in the Space Data
System Standard documents 121.0-B-2 and 120.0-G-2.

Libaec includes a free drop-in replacement for the SZIP
library (http://www.hdfgroup.org/doc_resource/SZIP).

%package devel
Summary:        Devel package for libaec (Adaptive Entropy Coding library)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Devel files for libaec (Adaptive Entropy Coding library).

%package static
Summary:        Static variant of libaec (Adaptive Entropy Coding library)
Requires:       %{name}-devel = %{version}-%{release}
%description static
Static variant of libaec (Adaptive Entropy Coding library).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{cmake} -DBUILD_TESTING=ON -DBUILD_STATIC_LIBS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libaec-devel -f %{oreon_filedir}/libaec-devel.list
%files -n libaec-static -f %{oreon_filedir}/libaec-static.list

%changelog

%autochangelog
