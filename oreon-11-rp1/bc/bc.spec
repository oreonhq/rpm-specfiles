# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ae470fec429775653e042015edc928d07c8c3b2fc59765172a330d3d87785f86

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:        GNU's bc (a numeric processing language) and dc (a calculator)
Name:           bc
Version:        1.08.2
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/bc/
Source0:        https://ftp.gnu.org/gnu/bc/bc-%{version}.tar.gz
Source1:        bc-1.08.2.tar.gz.sig
Source2:        kevin_pizzini.asc
Patch1:         bc-1.06-dc_ibase.patch
Patch2:         bc-1.06.95-doc.patch
Patch3:         bc-1.07.1-readline-echo-empty.diff

BuildRequires:  oreon-rpm-macros
BuildRequires:  bison
BuildRequires:  ed
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  texinfo

%description
The bc package includes bc and dc. Bc is an arbitrary precision
numeric processing arithmetic language. Dc is an interactive
arbitrary precision stack based calculator, which can be used as a
text mode calculator.

Install the bc package if you need its number handling capabilities or
if you would like to use its text mode calculator.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure --with-readline
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%check
%make_build check
test "$(echo '2^10' | ./bc/bc)" = 1024
test "$(./dc/dc -e '16o 255p')" = FF

%files
%license COPYING COPYING.LIB
%doc FAQ AUTHORS NEWS README Examples/
%{_bindir}/dc
%{_bindir}/bc
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*
%{_infodir}/bc.info*
%{_infodir}/dc.info*

%changelog
%autochangelog
