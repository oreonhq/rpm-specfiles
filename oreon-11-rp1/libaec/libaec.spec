Name:           libaec
Version:        1.1.6
Release:        1%{?dist}
Summary:        Adaptive Entropy Coding library
License:        LicenseRef-Callaway-BSD
Url:            https://gitlab.dkrz.de/k202009/libaec
Source0:        https://gitlab.dkrz.de/k202009/libaec/-/archive/v%{version}/libaec-v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 e50f323418eb451587891102b6014730e1aa936e763c47f2ae166a4745d1bed2
%global source0_file libaec-v1.1.6.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libaec-v1.1.6.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e50f323418eb451587891102b6014730e1aa936e763c47f2ae166a4745d1bed2" || { echo "oreon: Source0 SHA256 mismatch for libaec-v1.1.6.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
