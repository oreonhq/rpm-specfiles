%global source0_hash d237d9874c6e8b0ccf7758daa8286a6e825528b13ce3b2bca56eb1f73cddbc2c
Name:           chez-scheme
Summary:        Scheme incremental optimizing compiler
Version:        10.3.0
Release:        1%{?dist}
URL:            https://cisco.github.io/ChezScheme
License:        Apache-2.0 AND MIT
Source0:        https://github.com/cisco/ChezScheme/releases/download/v%{version}/csv%{version}.tar.gz
Patch0:         https://github.com/cisco/ChezScheme/pull/989.patch
Patch1:         https://github.com/cisco/ChezScheme/pull/990.patch
%ifarch ppc64le s390x
%endif
Provides:       bundled(nanopass)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Chez Scheme is both a programming language and an implementation of
that language, with supporting tools and documentation.

As a superset of the language described in the Revised6 Report on the
Algorithmic Language Scheme (R6RS), Chez Scheme supports all standard
features of Scheme, including first-class procedures, proper treatment
of tail calls, continuations, user-defined records, libraries,
exceptions, and hygienic macro expansion.

Chez Scheme also includes extensive support for interfacing with C and
other languages, support for multiple threads possibly running on
multiple cores, non-blocking I/O, and many other features.

The Chez Scheme implementation consists of a compiler, run-time
system, and programming environment. Although an interpreter is
available, all code is compiled by default. Source code is compiled
on-the-fly when loaded from a source file or entered via the shell. A
source file can also be precompiled into a stored binary form and
automatically recompiled when its dependencies change. Whether
compiling on the fly or precompiling, the compiler produces optimized
machine code, with some optimization across separately compiled
library boundaries. The compiler can also be directed to perform
whole-program compilation, which does full cross-library optimization
and also reduces a program and the libraries upon which it depends to
a single binary.

The run-time system interfaces with the operating system and supports,
among other things, binary and textual (Unicode) I/O, automatic
storage management (dynamic memory allocation and generational garbage
collection), library management, and exception handling. By default,
the compiler is included in the run-time system, allowing programs to
be generated and compiled at run time, and storage for dynamically
compiled code, just like any other dynamically allocated storage, is
automatically reclaimed by the garbage collector.

The programming environment includes a source-level debugger, a
mechanism for producing HTML displays of profile counts and program
"hot spots" when profiling is enabled during compilation, tools for
inspecting memory usage, and an interactive shell interface (the
expression editor, or "expeditor" for short) that supports multi-line
expression editing.

%package examples
Summary:        Chez-Scheme examples files
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description examples
The package provides the examples files from Chez-Scheme.

# see https://github.com/cisco/ChezScheme/issues/836 for upstream discussion
%package devel
Summary:        Chez-Scheme development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%ifarch ppc64le s390x
Requires:       libffi-devel
%endif
Provides:       %{name}-static = %{version}-%{release}
%description devel
The package provides extra development files for Chez-Scheme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n csv%{version} -p1
# use system libs
rm -r lz4 zlib

%build

case %{_arch} in
     x86_64) MACHINE=-m=ta6le ;;
     i386) MACHINE=-m=ti3le ;;
     aarch64) MACHINE=-m=tarm64le ;;
     riscv64) MACHINE=-m=trv64le ;;
     ppc64le) MACHINE="-m=tpb64l --enable-libffi" ;;
     s390x) MACHINE="-m=tpb64b --enable-libffi" ;;
esac
./configure --installbin=%{_bindir} --installlib=%{_libdir} --installman=%{_mandir} --temproot=%{buildroot} --threads $MACHINE ZLIB=-lz LZ4=-llz4
make ZUO_JOBS=$RPM_BUILD_NCPUS
%install
%make_install
chmod u+w %{buildroot}%{_libdir}/csv%{version}/*/{main.o,petite,scheme,scheme-script,lib*.a}
rm -rf %{buildroot}%{_libdir}/csv%{version}/examples
%oreon_autofiles chez-scheme-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles chez-scheme-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make ZUO_JOBS=$RPM_BUILD_NCPUS test-some-fast
%files -f %{oreon_filedir}/main.list
%files -n chez-scheme-examples -f %{oreon_filedir}/chez-scheme-examples.list
%files -n chez-scheme-devel -f %{oreon_filedir}/chez-scheme-devel.list

%changelog

%autochangelog
