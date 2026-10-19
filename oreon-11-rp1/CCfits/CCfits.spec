%global source0_hash f63546d2feecbf732cc08aaaa80a2eb5334ada37fb2530181b7363a5dbdeb01a
Name: CCfits
Version: 2.7
Release:        4%{?dist}
Summary:        A C++ interface for cfitsio
License: CFITSIO
URL: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits
Source0:        https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/ccfits/v2.7/CCfits-2.7.tar.gz
Patch0: CCfits-removerpath.patch
Patch1: cfitsio-path.patch
# oreon:deps
BuildRequires:  cfitsio-devel
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
CCfits is an object oriented interface to the cfitsio library. It is designed 
to make the capabilities of cfitsio available to programmers working in C++. 
It is written in ANSI C++ and implemented using the C++ Standard Library 
with namespaces, exception handling, and member template functions.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: cfitsio-devel >= 3.280
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%package doc
Summary: Documentation for %{name}, includes full API docs
BuildArch: noarch
%description doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --with-cfitsio=%{_prefix} --with-cfitsio-include=%{_includedir}/cfitsio
make %{?_smp_mflags}
%install
make %{?_smp_mflags}  install DESTDIR=%{buildroot}
rm %{buildroot}/usr/bin/cookbook
%ldconfig_scriptlets
%oreon_autofiles CCfits-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles CCfits-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n CCfits-devel -f %{oreon_filedir}/CCfits-devel.list
%files -n CCfits-doc -f %{oreon_filedir}/CCfits-doc.list

%changelog

%autochangelog
