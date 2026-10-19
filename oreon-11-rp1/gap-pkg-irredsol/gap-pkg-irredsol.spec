%global source0_hash none
%global gap_pkgname irredsol
%global giturl      https://github.com/bh11/irredsol
Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.4
Release:        1%{?dist}
Summary:        Irreducible soluble linear groups over finite fields
License:        BSD-2-Clause
URL:            http://www.icm.tu-bs.de/~bhoeflin/irredsol/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/IRREDSOL-%{version}/%{gap_pkgname}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data fp htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
Recommends:     gap-pkg-crisp
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-crisp-doc
BuildRequires:  gap-pkg-primgrp-doc
BuildRequires:  perl-interpreter
BuildRequires:  tth
# /oreon:deps
%description
IRREDSOL is a GAP package which provides a library of all irreducible soluble
subgroups of GL(n, q), up to conjugacy, where n is a positive integer and q a
prime power satisfying q^n <= 2000000, and a library of all primitive soluble
groups of degree at most 2000000.

%package doc
License:        BSD-2-Clause AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        IRREDSOL documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-crisp-doc
Requires:       gap-pkg-primgrp-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

%autosetup -n %{gap_upname}-%{version}

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg ../../pkg
ln -s %{gap_libdir}/pkg/crisp ..
ln -s %{gap_libdir}/pkg/primgrp ..
pushd doc
pdftex manual
makeindex manual
pdftex manual
pdftex manual
rm -f ../htm/*
perl %{gap_libdir}/etc/convert.pl -t -c -n IRREDSOL . ../htm
popd
rm -f ../../{doc,etc,pkg} ../crisp
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-irredsol-doc -f %{oreon_filedir}/gap-pkg-irredsol-doc.list

%changelog

%autochangelog
