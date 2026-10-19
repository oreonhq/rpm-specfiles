%global source0_hash 93941f85a1e7bd593fa94f299233cb5dfc91cd144fd9a78a6ceb75001c5b03be
Name:           libpsl
Version:        0.23.3
Release:        1%{?dist}
Summary:        C library for the Publix Suffix List
License:        MIT
URL:            https://rockdaboot.github.io/libpsl
Source0:        https://github.com/rockdaboot/libpsl/releases/download/%{version}/libpsl-%{version}.tar.gz
Requires:       publicsuffix-list-dafsa
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libicu-devel
BuildRequires:  libidn2-devel
BuildRequires:  libunistring-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  publicsuffix-list
BuildRequires:  python3-devel
# /oreon:deps
%description
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       publicsuffix-list
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package -n     psl
Summary:        Commandline utility to explore the Public Suffix List
%description -n psl
This package contains a commandline utility to explore the Public Suffix List,
for example it checks if domains are public suffixes, checks if cookie-domain
is acceptable for domains and so on.

%package -n     psl-make-dafsa
Summary:        Compiles the Public Suffix List into DAFSA form
BuildArch:      noarch
%description -n psl-make-dafsa
This script produces C/C++ code or an architecture-independent binary object
which represents a Deterministic Acyclic Finite State Automaton (DAFSA)
from a plain text Public Suffix List.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
rm -frv list
ln -sv %{_datadir}/publicsuffix list
%py3_shebang_fix src/psl-make-dafsa

%build

%configure --disable-silent-rules \
           --disable-static       \
           --enable-man           \
           --enable-gtk-doc       \
           --enable-builtin=libicu \
           --enable-runtime=libidn2 \
           --with-psl-distfile=%{_datadir}/publicsuffix/public_suffix_list.dafsa  \
           --with-psl-file=%{_datadir}/publicsuffix/effective_tld_names.dat       \
           --with-psl-testfile=%{_datadir}/publicsuffix/test_psl.txt
sed -i libtool \
    -e 's|^\(runpath_var=\).*$|\1|' \
    -e 's|^\(hardcode_libdir_flag_spec=\).*$|\1|'
%make_build
%install
%make_install
%oreon_autofiles psl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles psl-make-dafsa usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check || cat tests/test-suite.log
%files -f %{oreon_filedir}/main.list
%files -n libpsl-devel -f %{oreon_filedir}/libpsl-devel.list
%files -n psl -f %{oreon_filedir}/psl.list
%files -n psl-make-dafsa -f %{oreon_filedir}/psl-make-dafsa.list

%changelog

%autochangelog
