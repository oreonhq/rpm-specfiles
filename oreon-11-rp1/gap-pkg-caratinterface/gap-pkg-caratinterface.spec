%global source0_hash fdbc0f86befd8bf575c93475b33f58329ce99fe2ef97ba69af1478bc8664059c
%global gap_pkgname caratinterface
%global gap_upname  CaratInterface
Name:           gap-pkg-%{gap_pkgname}
Version:        2.3.7
Release:        1%{?dist}
Summary:        GAP interface to CARAT
License:        GPL-2.0-or-later
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
VCS:            git:https://github.com/gap-packages/CaratInterface.git
Source0:        https://www.math.uni-bielefeld.de/~gaehler/gap/%{gap_upname}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap htm tst
BuildOption(check): tst/testall.g
Requires:       carat
Requires:       gap-pkg-io
Suggests:       gap-pkg-cryst
# oreon:deps
BuildRequires:  carat
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-io
BuildRequires:  tth
# /oreon:deps
%description
This package provides GAP interface routines to some of the standalone
programs of the package CARAT, developed by J. Opgenorth, W. Plesken, and T.
Schulz at Lehrstuhl B für Mathematik, RWTH Aachen.  CARAT is a package for
computation with crystallographic groups.

CARAT is to a large extent complementary to the GAP 4 package Cryst.  In
particular, it provides routines for the computation of normalizers and
conjugators of finite unimodular groups in GL(n,Z), and routines for the
computation of Bravais groups, which are all missing in Cryst.  Furthermore,
it provides a catalog of Bravais groups up to dimension 6.  Cryst
automatically loads Carat when it is available, and makes use of its functions
where necessary.  The Carat package thereby extends the functionality of the
package Cryst considerably.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        CARAT documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}

%build

rm -f carat*.tgz
for f in read.g PackageInfo.g; do
  sed -i.orig 's,DirectoriesPackagePrograms( "%{gap_upname}" ),Directory( "%{_libexecdir}/carat" ),' $f
  touch -r ${f}.orig $f
  rm -f ${f}.orig
done
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-caratinterface-doc -f %{oreon_filedir}/gap-pkg-caratinterface-doc.list

%changelog

%autochangelog
