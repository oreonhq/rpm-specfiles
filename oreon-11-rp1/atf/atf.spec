%global source0_hash 0a6ecdbd2081079f16d0f43be08765edbaeab660febb2da2ce336b9f881a469b
Summary:        Automated Testing Framework
Name:    atf
Version: 0.26
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL:     https://github.com/freebsd/atf
Source0:        https://github.com/freebsd/atf/archive/refs/tags/atf-%{version}.tar.gz#/atf-%{version}.tar.gz
Source1: README.Fedora
%global _testsdir %{_libexecdir}/atf/tests
%global common_description The Automated Testing Framework (ATF) is a collection of libraries to \
implement test programs in a variety of languages.  At the moment, ATF \
offers C, C++ and POSIX shell bindings with which to implement tests. \
These bindings all offer a similar set of functionality and any test \
program written with them exposes a consistent user interface. \
\
ATF-based test programs rely on a separate runtime engine to execute them. \
The runtime engine is in charge of isolating the test programs from the \
rest of the system to ensure that their results are deterministic and that \
they cannot affect the running system.  The runtime engine is also \
responsible for gathering the results of all tests and composing reports. \
The current runtime of choice is Kyua.
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
There is no main package being built here.  This is unused.

# Ideally, we would ship one tests package for every component, namely
# libatf-c-tests, libatf-c++-tests and libatf-sh-tests.  However, the test
# suite of ATF has not been written with this in mind, and the tests of one
# component often have dependencies on the rest of the components.  It is
# much easier to ship a single package with the whole test suite rather
# than attempting to fight this fact.
%package tests
Summary: Automated Testing Framework - Test suite
Requires: libatf-c = %{version}-%{release}
Requires: libatf-c++ = %{version}-%{release}
Requires: libatf-sh = %{version}-%{release}
Requires: libatf-c-devel = %{version}-%{release}
Requires: libatf-c++-devel = %{version}-%{release}
Requires: libatf-sh-devel = %{version}-%{release}
%description tests
%{common_description}

This package installs the run-time tests for all the components of ATF, which
include tests for the C, C++ and POSIX shell libraries and the run-time tools.
Please see the README.Fedora file in the documentation directory for further
details on how to run the installed tests.

%package -n libatf-c
Summary: Automated Testing Framework - C bindings
%description -n libatf-c
%{common_description}

This package provides the run-time libraries to run tests that use the
ATF C bindings.

%package -n libatf-c-devel
Summary: Automated Testing Framework - C bindings (headers)
Requires: libatf-c = %{version}-%{release}
%description -n libatf-c-devel
%{common_description}

This package provides the libraries, header files and documentation to
develop tests that use the ATF C bindings.

%package -n libatf-c++
Summary: Automated Testing Framework - C++ bindings
%description -n libatf-c++
%{common_description}

This package provides the run-time libraries to run tests that use the
ATF C++ bindings.

%package -n libatf-c++-devel
Summary: Automated Testing Framework - C++ bindings (headers)
Requires: libatf-c = %{version}-%{release}
Requires: libatf-c-devel = %{version}-%{release}
Requires: libatf-c++ = %{version}-%{release}
%description -n libatf-c++-devel
%{common_description}

This package provides the libraries, header files and documentation to
develop applications that use the ATF C++ bindings.

%package -n libatf-sh
Summary: Automated Testing Framework - POSIX shell bindings
Requires: libatf-c++ = %{version}-%{release}
%description -n libatf-sh
%{common_description}

This package provides the run-time libraries to run tests that use the
ATF POSIX shell bindings.

%package -n libatf-sh-devel
Summary: Automated Testing Framework - POSIX shell bindings (headers)
Requires: libatf-sh = %{version}-%{release}
%description -n libatf-sh-devel
%{common_description}

This package provides the supporting files and documentation to develop
applications that use the ATF POSIX shell bindings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{name}-%{version}

# Put the README.Fedora file in the top-level directory of the source tree so
# that the %doc call below can pick it up.
cp -p %{SOURCE1} README.Fedora

%build

autoreconf -is
%configure INSTALL="/usr/bin/install -p" --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build pkgtestsdir=%{_testsdir} testsdir=%{_testsdir}
%check

make check
%install
%make_install doc_DATA= \
             pkgtestsdir=%{_testsdir} testsdir=%{_pkgtestsdir}
rm %{buildroot}%{_libdir}/libatf*.la
%oreon_autofiles atf-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libatf-c usr/*/lib*.so.*
%oreon_autofiles libatf-c-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libatf-sh usr/*/lib*.so.*
%oreon_autofiles libatf-sh-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n atf-tests -f %{oreon_filedir}/atf-tests.list
%files -n libatf-c -f %{oreon_filedir}/libatf-c.list
%files -n libatf-c-devel -f %{oreon_filedir}/libatf-c-devel.list
%files -n libatf-sh -f %{oreon_filedir}/libatf-sh.list
%files -n libatf-sh-devel -f %{oreon_filedir}/libatf-sh-devel.list

%changelog

%autochangelog
