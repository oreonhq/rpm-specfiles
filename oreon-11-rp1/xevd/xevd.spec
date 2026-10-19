%global source0_hash febfdb532819bbf36b1b04e74d3ef328ad0f0f2db6224ddb7640fce6bd0014f4
Name:           xevd
Version:        0.7.0
Release:        1%{?dist}
Summary:        Reference MPEG-5 Part 1 (EVC) decoder
License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xevd
Source0:        https://github.com/mpeg5/xevd/archive/v%{version}/xevd-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
%description
The eXtra-fast Essential Video Decoder (XEVD) is an open source MPEG-5 EVC
decoder baseline profile implementation.

%package libs
Summary:        Library files for %{name}
%description libs
Library files for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
rm -rf src_main
echo "v%{version}" > version.txt

%build

%cmake -DSET_PROF=BASE
%cmake_build
%install
%cmake_install
rm -rfv %{buildroot}%{_libdir}/%{name}*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xevd-libs -f %{oreon_filedir}/xevd-libs.list
%files -n xevd-devel -f %{oreon_filedir}/xevd-devel.list

%changelog

%autochangelog
