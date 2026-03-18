Name:           libaec
Version:        1.1.6
Release:        1%{?dist}
Summary:        Adaptive Entropy Coding library
License:        LicenseRef-Callaway-BSD
Url:            https://gitlab.dkrz.de/k202009/libaec
Source0:        https://gitlab.dkrz.de/k202009/libaec/-/archive/v%{version}/libaec-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake >= 3.1

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
%autosetup -p1 -n %{name}-v%{version}

%build
%{cmake} -DBUILD_TESTING=ON -DBUILD_STATIC_LIBS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/cmake/%{name}
%exclude %{_libdir}/cmake/%{name}/*_static*

%files static
%{_libdir}/lib*.a
%{_libdir}/cmake/%{name}/*_static*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-1
- Prepare for Oreon 11 (RP1)
