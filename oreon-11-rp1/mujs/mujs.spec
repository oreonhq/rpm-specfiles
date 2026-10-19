%global source0_hash 6e36c15dbb84ff859320297c900852f241b131a7b6ddaea669ac9a65bd75571c
%global unicodedir  /usr/share/unicode
%global ucddir      %{unicodedir}/ucd
Name:           mujs
Version:        1.3.10
Release:        1%{?dist}
Summary:        An embeddable Javascript interpreter
License:        ISC
URL:            https://mujs.com/
Source0:        https://mujs.com/downloads/%{name}-%{version}.tar.gz
Patch:          set-library-soname-version.patch
Patch:          downstream-soname-version.patch
Patch:          remove-curl-from-Makefile.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  unicode-ucd
# /oreon:deps
%description
MuJS is a lightweight Javascript interpreter designed for embedding in
other software to extend them with scripting capabilities.

%package devel
Summary:        MuJS development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the MuJS shared library.

%package static
Summary:        MuJS development files using static lib
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
This package provides the MuJS static library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod a-x -v docs/*
ln -sf %{ucddir}/UnicodeData.txt
ln -sf %{ucddir}/SpecialCasing.txt

%build

%make_build release prefix="%{_prefix}" libdir="%{_libdir}" CFLAGS="%{build_cflags} %{build_ldflags}"
%install
%make_install prefix="%{_prefix}" libdir="%{_libdir}"
%{__make} install-shared DESTDIR=%{?buildroot} INSTALL="%{__install} -p" prefix="%{_prefix}" libdir="%{_libdir}"
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n mujs-devel -f %{oreon_filedir}/mujs-devel.list
%files -n mujs-static -f %{oreon_filedir}/mujs-static.list

%changelog

%autochangelog
