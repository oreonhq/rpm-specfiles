%global source0_hash 37aa5341f2b51ffee245db3456d9bc25f718ca12beb7b990dc16d686890115e3

Summary: Automated Testing Framework
Name:    atf
Version: 0.23
Release: 4%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/freebsd/atf
Source0:        https://github.com/freebsd/atf/archive/atf-0.23/atf-0.23.tar.gz
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

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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


%files tests
%doc README.Fedora
%{_testsdir}
%{_mandir}/man7/atf.7.gz

%files -n libatf-c
%{_libdir}/libatf-c.so.1
%{_libdir}/libatf-c.so.1.0.0
%{_datadir}/man/man1/atf-test-program.1.gz
%{_datadir}/man/man4/atf-test-case.4.gz
%{_mandir}/man3/atf-c.3.gz

%files -n libatf-c-devel
%{_datadir}/aclocal/atf-c.m4
%{_datadir}/aclocal/atf-common.m4
%{_includedir}/atf-c.h
%{_includedir}/atf-c
%{_libdir}/libatf-c.so
%{_libdir}/pkgconfig/atf-c.pc

%files -n libatf-c++
%{_libdir}/libatf-c++.so.2
%{_libdir}/libatf-c++.so.2.0.0
%{_mandir}/man3/atf-c++.3.gz

%files -n libatf-c++-devel
%{_datadir}/aclocal/atf-c++.m4
%{_includedir}/atf-c++.hpp
%{_includedir}/atf-c++
%{_libdir}/libatf-c++.so
%{_libdir}/pkgconfig/atf-c++.pc

%files -n libatf-sh
%{_bindir}/atf-sh
# Cheat a bit: While this directory should be supposedly owned by the main
# 'atf' package, 'atf' depends on libatf-sh.  Therefore, it's easier to handle
# ownership here.
%{_datadir}/atf
%{_libexecdir}/atf-check
%{_mandir}/man1/atf-sh.1.gz
%{_mandir}/man3/atf-sh.3.gz

%files -n libatf-sh-devel
%{_datadir}/aclocal/atf-sh.m4
%{_libdir}/pkgconfig/atf-sh.pc
%{_mandir}/man1/atf-check.1.gz


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.23-4
- Prepare for Oreon 11 (RP1)
