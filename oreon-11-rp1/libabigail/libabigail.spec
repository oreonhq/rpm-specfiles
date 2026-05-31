%global source0_hash b4b86baa3105a28ada25091f1ef0535e7a60616d3d5d4cb1ee2aceaba341d738

# dependencies are not available in RHEL
%bcond abidb %{undefined rhel}

%global tarball_revision 1
%global tarball_name %{name}-%{version}

Name: libabigail
Version: 2.9
Release: 2%{?dist}
Summary: Set of ABI analysis tools

License: Apache-2.0 WITH LLVM-exception
URL: https://sourceware.org/libabigail/
Source0:        http://mirrors.kernel.org/sourceware/libabigail/%{tarball_name}.tar.xz

BuildRequires: git
BuildRequires: libbpf-devel
BuildRequires: binutils-devel
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: elfutils-devel
BuildRequires: libxml2-devel
BuildRequires: xxhash-devel
BuildRequires: xz-devel >= 5.2.0
BuildRequires: doxygen
BuildRequires: python3-sphinx
BuildRequires: texinfo
%if %{with abidb}
BuildRequires: python3-GitPython
BuildRequires: python3-libarchive-c
Requires: python3-GitPython
Requires: python3-libarchive-c
%endif
%if 0%{?fedora} || 0%{?epel}
BuildRequires: dpkg
BuildRequires: koji
BuildRequires: python3-koji
%endif
BuildRequires: wget

%description
The libabigail package comprises seven command line utilities:
abidiff, kmidiff, abipkgdiff, abicompat, abidw, and abilint.
The abidiff command line tool compares the ABI of two
ELF shared libraries and emits meaningful textual reports about
changes impacting exported functions, variables and their types.
Simarly, the kmidiff compares the kernel module interface of two Linux
kernels.  abipkgdiff compares the ABIs of ELF binaries contained in
two packages.  abicompat checks if a subsequent version of a shared
library is still compatible with an application that is linked against
it.  abidw emits an XML representation of the ABI of a given ELF
shared library. abilint checks that a given XML representation of the
ABI of a shared library is correct.

Install libabigail if you need to compare the ABI of ELF shared
libraries.

%package devel
Summary: Shared library and header files to write ABI analysis tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains a shared library and the associated header files
that are necessary to develop applications that use the C++ Libabigail
library.  The library provides facilities to analyze and compare
application binary interfaces of shared libraries in the ELF format.


%package doc
Summary: Man pages, texinfo files and html manuals of libabigail

%description doc
This package contains documentation for the libabigail tools in the
form of man pages, texinfo documentation and API documentation in html
format.

%if 0%{?fedora} || 0%{?epel}
%package fedora
Summary: Utility to compare the ABI of Fedora packages
BuildRequires: python3-devel
BuildRequires: python3-koji
BuildRequires: python3-rpm
BuildRequires: python3-pyxdg
#For x-rpm mimetype definition!
BuildRequires: mailcap
BuildRequires: make
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: curl
Requires: koji
Requires: python3 >= 3.6
Requires: python3-koji
Requires: python3-pyxdg
Requires: python3-rpm
#For x-rpm mimetype definition!
Requires: mailcap

%description fedora
This package contains the fedabipkgdiff command line utility, which
interacts with the Fedora Build System over the internet to let the
user compare the ABI of Fedora packages without having to download
them manually.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git

%build
%configure %{?with_abidb:--enable-abidb} --enable-ctf --enable-btf --disable-silent-rules --disable-zip-archive --disable-static
make %{?_smp_mflags}
pushd doc
make html-doc
pushd manuals
make html-doc
make man
make info
popd
popd

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Install man and texinfo files as they are not installed by the
# default 'install' target of the makefile.
make -C doc/manuals install-man-and-info-doc DESTDIR=%{buildroot}

%if 0%{?fedora} || 0%{?epel}
# Explicitly use Python 3 as the interpreter
%py3_shebang_fix %{buildroot}%{_bindir}/fedabipkgdiff
%endif

%check
time make %{?_smp_mflags} check check-self-compare || (cat tests/test-suite.log && exit 2)

%ldconfig_scriptlets

%files
%{_bindir}/abicompat
%{_bindir}/abidiff
%{_bindir}/abidw
%{_bindir}/abilint
%{_bindir}/abipkgdiff
%{_bindir}/kmidiff
%if %{with abidb}
%{_bindir}/abidb
%endif
%{_libdir}/libabigail.so.8
%{_libdir}/libabigail.so.8.0.0
%{_libdir}/libabigail/default.abignore
%doc README AUTHORS ChangeLog
%license LICENSE.txt license-change-2020.txt
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_infodir}/abigail.info*

%files devel
%{_libdir}/libabigail.so
%{_libdir}/pkgconfig/libabigail.pc
%{_includedir}/*
%{_datadir}/aclocal/abigail.m4

%files doc
%license LICENSE.txt license-change-2020.txt
%doc doc/manuals/html/*

%if 0%{?fedora} || 0%{?epel}
%files fedora
%{_bindir}/fedabipkgdiff
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9-2
- Prepare for Oreon 11 (RP1)
