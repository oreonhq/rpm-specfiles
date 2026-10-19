%global source0_hash 6492b2beb26c3179cdd19abc90dc47a685be471c594d5ab664283e1d3586acdc
%{!?release_func:%global release_func() %1%%{?release_date:.%%release_date}%%{?dist}}
%define version_number 1.0.3
Name:           CVector
Version:        %{version_number}.1
Release:        36%{?dist}
Summary:        ANSI C API for Dynamic Arrays
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://cvector.sourceforge.net/
%if 0%{?release_date:1}
Source0:        http://downloads.sourceforge.net/project/cvector/cvector/%{name}-1.0.3/%{name}-%{version}.tar.gz
%else
Source0:        http://downloads.sourceforge.net/project/cvector/cvector/%{name}-1.0.3/%{name}-%{version}.tar.gz
%endif
Patch0:         CVector-1.0.3.1-dynamic.patch
Patch1:         CVector-1.0.3-lib64.patch
# oreon:deps
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
CVector is an ANSI C implementation of dynamic arrays to provide a
crude approximation to the C++ vector class.

%package devel
Summary:        Development tools for compiling programs using CVector
Requires:       %{name} = %{version}-%{release}
%description devel
The CVector-devel package includes the header and library files for
developing applications that use CVector.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .dynamic
%if "%{_lib}" == "lib64"
%patch -P1 -p1 -b .lib64
%endif

%build

make CFLAGS="%{optflags}" %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install CFLAGS="%{optflags}" INSTALL_PREFIX="%{buildroot}%{_prefix}"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%oreon_autofiles CVector-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make tests
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n CVector-devel -f %{oreon_filedir}/CVector-devel.list

%changelog

%autochangelog
