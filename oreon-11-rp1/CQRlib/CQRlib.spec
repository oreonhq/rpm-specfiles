%global source0_hash af3cf2402974579f3c6efc6a6174a5da52786db4bfee9d38d504d93bc42410fd
Name:           CQRlib
Version:        1.1.2
Release:        36%{?dist}
Summary:        ANSI C API for quaternion arithmetic and rotation
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://cqrlib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/cqrlib/cqrlib/CQRlib-%{version}/CQRlib-%{version}.tar.gz
Patch0:         CQRlib-1.0.6-dynamic.patch
Patch1:         CQRlib-1.1.2-tag.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
CQRlib is an ANSI C implementation of a utility library for quaternion
arithmetic and quaternion rotation math.

%package devel
Summary:        Development tools for compiling programs using CQRlib
Requires:       %{name} = %{version}-%{release}
%description devel
The CQRlib-devel package includes the header and library files for
developing applications that use CQRlib.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1 -b .dynamic
%patch -P1 -p1 -b .tag
%if "%{_lib}" == "lib64"
sed -i -e 's,$(INSTALLDIR)/lib,$(INSTALLDIR)/lib64,' -e 's,$(ROOT)/lib,$(ROOT)/lib64,' Makefile
%endif

%build

make all CFLAGS="%{optflags}" %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install CFLAGS="%{optflags}" INSTALLDIR="%{buildroot}%{_prefix}"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%oreon_autofiles CQRlib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make tests
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n CQRlib-devel -f %{oreon_filedir}/CQRlib-devel.list

%changelog

%autochangelog
