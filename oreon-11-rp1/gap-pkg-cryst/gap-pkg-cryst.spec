%global source0_hash d563ee3bda1e8b4bdff2c5b03d8d6be9a127011490dbad298bf4d2a15d0afc0e
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname    cryst
%global gap_skip_check %{?with_bootstrap}
Name:           gap-pkg-%{gap_pkgname}
Version:        4.1.32
Release:        1%{?dist}
Summary:        GAP support for crystallographic groups
License:        GPL-2.0-or-later
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
VCS:            git:https://github.com/gap-packages/cryst.git
Source0:        https://www.math.uni-bielefeld.de/~gaehler/gap/Cryst/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap grp htm tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       gap-pkg-caratinterface
Requires:       gap-pkg-polenta
Requires:       gap-pkg-polycyclic
Suggests:       xgap
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-caratinterface
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-polenta
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  tth
# /oreon:deps
%description
The GAP 4 package Cryst, previously known as CrystGAP, is the successor of the
CrystGAP package for GAP 3.  During the porting process to GAP 4, large parts
of the code have been rewritten, and the functionality has been extended
considerably.  Cryst provides a rich set of methods to compute with affine
crystallographic groups, in particular space groups.  In contrast to the GAP 3
version, affine crystallographic groups are now fully supported both in the
representation acting from the right and in the representation acting from the
left.  The latter representation is the one preferred by crystallographers.
There are also functions to determine representatives of all space group types
of a given dimension.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Cryst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-cryst-doc -f %{oreon_filedir}/gap-pkg-cryst-doc.list

%changelog

%autochangelog
