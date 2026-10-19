%global source0_hash 15e9a18bb0d5c3c5093444a9003471c2d25ab611b4219ef1064f598668723681
Name:		sfsexp
%global libname	libsexp
Version:	1.4.1
%global soname	1
%global sominor	0.0
Release:        1%{?dist}
Summary:        Small Fast S-Expression Library
License:	LGPL-2.1-or-later
URL:		https://github.com/mjsottile/sfsexp
Source0:        https://github.com/mjsottile/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This library is intended for developers who wish to manipulate (read,
parse, modify, and create) symbolic expressions (s-expressions)from C
or C++ programs.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure --disable-static
%make_build
%check

pushd tests
/bin/sh dotests.sh
popd
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sfsexp-devel -f %{oreon_filedir}/sfsexp-devel.list

%changelog

%autochangelog
