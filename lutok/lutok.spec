Summary: Lightweight C++ API library for Lua
Name: lutok
Version: 0.6.2
Release: 1%{?dist}
License: BSD-3-Clause
URL: https://github.com/freebsd/lutok
Source0:https://github.com/freebsd/lutok/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1: README.Fedora
Requires: lua >= 5.2
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: libatf-c++-devel >= 0.21
BuildRequires: libatf-sh-devel >= 0.21
BuildRequires: lua-devel >= 5.2
BuildRequires: make

%define _testsdir %{_libexecdir}/lutok/tests

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
%setup -q

# Put the README.Fedora file in the top-level directory of the source tree so
# that the %doc call below can pick it up.
cp -p %{SOURCE1} README.Fedora

%build
%configure --docdir=%{_defaultdocdir}/lutok-doc-%{version} \
           --disable-static \
           --htmldir=%{_defaultdocdir}/lutok-doc-%{version}/html \
           --without-doxygen --enable-atf
# Drop the default RPATH
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/#_beware_of_rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} testsdir=%{_testsdir}

%check
# In order to enable this, we need to add a BuildRequires on kyua-cli.  The
# problem is that kyua-cli depends on lutok.  Introducing a circular dependency
# for this minor benefit does not seem like the best move.  After all, we can
# always install lutok-tests later and run the tests post-install.
#make check testsdir=%{_testsdir}

%install
make install DESTDIR=%{buildroot} doc_DATA= testsdir=%{_testsdir}
rm %{buildroot}%{_libdir}/liblutok.la

%files
%doc AUTHORS COPYING NEWS README.md
%{_libdir}/liblutok.so.3
%{_libdir}/liblutok.so.3.0.0

%ldconfig_scriptlets

%package devel
Summary: Libraries and header files for Lutok development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lua-devel >= 5.1

%description devel
Provides the libraries and header files to develop applications that
use the Lutok C++ API to Lua.

%files devel
%{_includedir}/lutok
%{_libdir}/liblutok.so
%{_libdir}/pkgconfig/lutok.pc

%package doc
Summary: API documentation of the Lutok library and example programs
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Provides HTML documentation describing the API of the Lutok library
and a collection of sample source programs to demonstrate the use
of the library.

%files doc
%{_defaultdocdir}/lutok-doc-%{version}

%package tests
Summary: Run-time tests of the Lutok library
Requires: %{name} = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: libatf-c++ >= 0.20

%description tests
This package installs the run-time tests for the Lutok library.
Please see the README.Fedora file in the documentation directory for further
details on how to run the installed tests.

%files tests
%doc README.Fedora
%{_testsdir}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2-1
- Prepare for Oreon 11 (RP1)
