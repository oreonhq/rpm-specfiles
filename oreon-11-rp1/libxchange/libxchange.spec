%global source0_hash e59a9edbe37988d48d8098acb22eab517486e2b51120faf70df51c6566ce0ed3
%global upstream_version        1.3.0
Name:                   libxchange
Version:                1.3.0
Release:        1%{?dist}
Summary:        Structured data representation and JSON support for C/C++
License:                Unlicense
URL:                    https://sigmyne.github.io/xchange
Source0:        https://github.com/Sigmyne/xchange/archive/refs/tags/v%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  sed
# /oreon:deps
%description

The xchange library provides a free framework for structured data 
representation in C/C++ (C99 or later), and includes JSON parsing and 
emitting functions. It is free to use, in any way you like, without 
licensing restrictions.

%package devel
Summary:                C development files for the xchange C/C++ library
Requires:               %{name}%{_isa} = %{version}-%{release}
%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the xchange C/C++ library.

%package doc
Summary:                Documentation for the xchange C/C++ library
BuildArch:              noarch
%description doc
This package provides HTML documentation and examples for the xchange C/C++ 
library. The HTML API documentation can also be used with the Eclipse IDE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n xchange-%{upstream_version}

%build

make %{?_smp_mflags}
%check

make test
%install
make PACKAGE_NAME=%{name} DESTDIR=%{buildroot} libdir=%{_libdir} install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libxchange-devel -f %{oreon_filedir}/libxchange-devel.list
%files -n libxchange-doc -f %{oreon_filedir}/libxchange-doc.list

%changelog

%autochangelog
