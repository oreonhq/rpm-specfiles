%global source0_hash 1cf012cdc8445cab0efc445064ef9b2d3f46ed0165dae803c40fe3d2b23fdaad
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:             ledger
Version:          3.4.1
Release:        1%{?dist}
Summary:        A powerful command-line double-entry accounting system
License:          BSD-3-Clause
URL:              https://ledger-cli.org/
Source0:        https://github.com/ledger/ledger/archive/v%{version}.tar.gz
Patch0:           ledger-boost190.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  libedit-devel
BuildRequires:  man2html
BuildRequires:  mpfr-devel
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-ec
BuildRequires:  texlive-eurosym
BuildRequires:  utf8cpp-devel
# /oreon:deps
%description
Ledger is a powerful, double-entry accounting system that is accessed
from the UNIX command-line. This may put off some users — as there is
no flashy UI — but for those who want unparalleled reporting access to
their data, there really is no alternative.

%package devel
Summary: Libraries and header files for %{name} development
Requires: %{name} = %{version}-%{release}
%description devel
Libraries and header files for %{name} development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
# Avoid texinfo errors on EL7.
rm -r lib/utfcpp

%build

%cmake \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_SKIP_RPATH:BOOL=ON \
       -DUSE_PYTHON:BOOL=OFF \
       -DUSE_DOXYGEN:BOOL=ON \
       -DBUILD_WEB_DOCS:BOOL=ON
%cmake_build
%cmake_build -t doc
%install
%cmake_install
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -p -m0644 contrib/ledger-completion.bash \
    %{buildroot}%{_sysconfdir}/bash_completion.d/ledger
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_infodir}/*
cp -p %{__cmake_builddir}/doc/ledger3.info* %{buildroot}%{_infodir}
mkdir -p %{buildroot}%{_pkgdocdir}/contrib
for i in bal bal-huquq compilation-ledger.el entry getquote.pl getquote-uk.py ledger-du README repl.sh report tc ti to trend; do
    install -p -m0644 contrib/${i} %{buildroot}%{_pkgdocdir}/contrib/${i}
done
mkdir -p %{buildroot}%{_pkgdocdir}/samples
for i in demo.ledger divzero.dat drewr3.dat drewr.dat sample.dat standard.dat transfer.dat wow.dat; do
    install -p -m0644 test/input/${i} %{buildroot}%{_pkgdocdir}/samples/${i}
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ledger-devel -f %{oreon_filedir}/ledger-devel.list

%changelog

%autochangelog
