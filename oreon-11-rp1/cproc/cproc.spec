%global source0_hash 0998a6bfac3c1f1719151fb9e772a4a6a90c775c1332d0b02dcbadeca31e5b9b

%global         commit      f66a661359a39e10af01508ad02429517b8460e3
%global         shortcommit  %(c=%{commit}; echo ${c:0:8})

Name:           cproc
Version:        0.0^20240428.f66a6613
Release:        %{autorelease}
Summary:        A C11 compiler using QBE as a backend

# Main code is under ISC license
# tree.c is under MIT license
# tests are under Unlicense, but not distributed
License:        ISC AND MIT
URL:            https://git.sr.ht/~mcf/cproc/
Source:         %{url}/archive/%{commit}.tar.gz
# https://lists.sr.ht/~mcf/cproc/patches/56032
Patch:          redhat-linux-configure.patch
# Compiler has not been ported to other architectures
ExclusiveArch:  aarch64 riscv64 x86_64

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  qbe

%description
cproc is a C11 compiler using QBE as a backend. It is released under the ISC
license.

Some C23 features and GNU C extensions are also implemented.

There is still much to do, but it currently implements most of the language and
is capable of building software including itself, mcpp, gcc 4.7, binutils, and
more.

It was inspired by several other small C compilers including 8cc, c, lacc, and
scc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p 1

%build
# Fedora specific commands not used
./configure
%make_build all

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 cproc %{buildroot}%{_bindir}
install -m 755 cproc-qbe %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 cproc.1 %{buildroot}%{_mandir}/man1/

%check
make check

%files
%license LICENSE
%doc README.md
%doc doc/*.md
%{_bindir}/cproc
%{_bindir}/cproc-qbe
%{_mandir}/man1/cproc.1*

%changelog
%autochangelog
