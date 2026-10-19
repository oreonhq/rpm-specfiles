%global source0_hash d6564259fd52522de11149569bdceed7b0a14d39aeff3ea068840fb9686377ad
%global gap_pkgname crystcat
Name:           gap-pkg-%{gap_pkgname}
Version:        1.1.13
Release:        1%{?dist}
Summary:        Crystallographic groups catalog
License:        GPL-2.0-or-later
URL:            https://www.math.uni-bielefeld.de/~gaehler/gap/packages.php
VCS:            git:https://github.com/gap-packages/crystcat.git
Source0:        https://www.math.uni-bielefeld.de/~gaehler/gap/CrystCat/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): grp htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-cryst
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-cryst-doc
BuildRequires:  tth
# /oreon:deps
%description
The GAP 4 package CrystCat provides a catalog of crystallographic groups of
dimensions 2, 3, and 4 which covers most of the data contained in the book
"Crystallographic groups of four-dimensional space" by H. Brown, R. Bülow, J.
Neubüser, H. Wondratschek, and H. Zassenhaus (John Wiley, New York, 1978).
This catalog was previously available in the library of GAP 3.  The present
version for GAP 4 has been moved into a separate package, because it requires
the package Cryst, which is loaded automatically by CrystCat.  The benefit of
this is that space groups extracted from the catalog now have the rich set of
methods provided by Cryst at their disposal, and are no longer dumb lists of
generators.  Moreover, space groups are now fully supported in both the
representation acting from the left and the representation acting from the
right.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        CrystCat documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-cryst-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg/cryst ..
pushd doc
./make_doc
popd
rm -f ../../{doc,etc} ../cryst
gzip --best grp/crystcat.grp
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-crystcat-doc -f %{oreon_filedir}/gap-pkg-crystcat-doc.list

%changelog

%autochangelog
