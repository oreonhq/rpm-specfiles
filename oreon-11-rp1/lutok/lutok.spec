%global source0_hash 2cec51efa0c8d65ace8b21eaa08384b77abc5087b46e785f78de1c21fb754cd5
Summary:        Lightweight C++ API library for Lua
Name: lutok
Version: 0.4
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL: http://code.google.com/p/lutok/
Source0:        https://github.com/jmmv/lutok/releases/download/lutok-%{version}/lutok-%{version}.tar.gz
Source1:        README.Fedora
Requires: lua >= 5.2
%define _testsdir %{_libexecdir}/lutok/tests
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libatf-c++-devel
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
%description
Lutok provides thin C++ wrappers around the Lua C API to ease the
interaction between C++ and Lua.  These wrappers make intensive use of
RAII to prevent resource leakage, expose C++-friendly data types, report
errors by means of exceptions and ensure that the Lua stack is always
left untouched in the face of errors.  The library also provides a small
subset of miscellaneous utility functions built on top of the wrappers.

Lutok focuses on providing a clean and safe C++ interface; the drawback
is that it is not suitable for performance-critical environments.  In
order to implement error-safe C++ wrappers on top of a Lua C binary
library, Lutok adds several layers or abstraction and error checking
that go against the original spirit of the Lua C API and thus degrade
performance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

# Put the README.Fedora file in the top-level directory of the source tree so
# that the %doc call below can pick it up.
cp -p %{SOURCE1} README.Fedora

%build

%configure --docdir=%{_defaultdocdir}/lutok-doc-%{version} \
           --disable-static \
           --htmldir=%{_defaultdocdir}/lutok-doc-%{version}/html \
           --without-doxygen
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} testsdir=%{_testsdir}
%check

%install
make install DESTDIR=%{buildroot} doc_DATA= testsdir=%{_testsdir}
rm %{buildroot}%{_libdir}/liblutok.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package devel
Summary: Libraries and header files for Lutok development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lua-devel >= 5.1
%description devel
Provides the libraries and header files to develop applications that
use the Lutok C++ API to Lua.

%package doc
Summary: API documentation of the Lutok library and example programs
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Provides HTML documentation describing the API of the Lutok library
and a collection of sample source programs to demonstrate the use
of the library.

%package tests
Summary: Run-time tests of the Lutok library
Requires: %{name} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: libatf-c++ >= 0.20
%description tests
This package installs the run-time tests for the Lutok library.
Please see the README.Fedora file in the documentation directory for further
details on how to run the installed tests.

%files -f %{oreon_filedir}/main.list
%files -n lutok-devel -f %{oreon_filedir}/lutok-devel.list
%files -n lutok-doc -f %{oreon_filedir}/lutok-doc.list
%files -n lutok-tests -f %{oreon_filedir}/lutok-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4-31
- Import
