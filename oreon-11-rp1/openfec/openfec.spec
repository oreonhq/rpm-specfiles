%global source0_hash 3397f58c8fff945ece8ea19e7859040c98a5c6497e5d791397794094e15e5873
Name:		openfec
Version:	1.4.2.12
Release:        1%{?dist}
Summary:        Application-Level Forward Erasure Correction codes
License:	CeCILL-C and GPLv2+ and BSD
URL:		https://github.com/roc-streaming/openfec
Source0:        https://github.com/roc-streaming/%{name}/archive/v%{version}/%{name}_%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
# /oreon:deps
%description
Application-Level Forward Erasure Correction codes, or AL-FEC (also called
UL-FEC, for Upper-Layers FEC). The idea, in one line, is to add redundancy
in order to be able to recover from erasures. Because of their position in
the communication stack, these codes are implemented as software codecs,
and they find many applications in robust transmission and distrituted
storage systems.

%package devel
Summary: Development libraries for openfec
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The openfec-devel package contains header files necessary for
developing programs using openfec.

%package utils
Summary: Utilities for openfec
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Utilities for openfec.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DOPTIMIZE=DEFAULT -DINSTALL_DEVTOOLS=ON
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_includedir}/%{name}
pushd src
find -name '*.h' -type f -exec install -pDm 0644 '{}' %{buildroot}%{_includedir}/%{name}/'{}' \;
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n openfec-devel -f %{oreon_filedir}/openfec-devel.list
%files -n openfec-utils -f %{oreon_filedir}/openfec-utils.list

%changelog

%autochangelog
