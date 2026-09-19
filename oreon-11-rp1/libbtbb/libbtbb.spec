%global source0_hash 9478bb51a38222921b5b1d7accce86acd98ed37dbccb068b38d60efa64c5231f

%global POSTYEAR 2020
%global POSTMONTH 12
%global POSTNUM 1

Name:           libbtbb
Version:        %{POSTYEAR}.%{POSTMONTH}.R%{POSTNUM}
Release:        16%{?dist}
Summary:        A Bluetooth baseband decoding library
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/greatscottgadgets/libbtbb
Source0:        https://github.com/greatscottgadgets/libbtbb/archive/%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}.tar.gz

Patch0:         %{name}-0001-Update-CMake-version-requirement.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  make

%description
This is the Bluetooth baseband decoding library, forked from the GR-Bluetooth
project. It can be used to extract Bluetooth packet and piconet information
from Ubertooth devices as well as GR-Bluetooth/USRP.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{POSTYEAR}-%{POSTMONTH}-R%{POSTNUM}

%build
# TODO: Please submit an issue to upstream (rhbz#2380708)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DENABLE_PYTHON=OFF -B . -S .
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
