%global source0_hash 9a14209632490ab1149022165c2936f57cb7044293ffb2aef0580b3d4085eb8a
%global gap_pkgname radiroot
%global giturl      https://github.com/gap-packages/radiroot
Name:           gap-pkg-%{gap_pkgname}
Version:        2.10
Release:        1%{?dist}
Summary:        Compute radicals for roots of solvable rational polynomials
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/radiroot/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
Patch:          %{name}-example.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): htm lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-alnuth
# oreon:deps
BuildRequires:  GAPDoc-doc
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-alnuth
BuildRequires:  tth
# /oreon:deps
%description
This package can compute and display an expression by radicals for the roots
of a solvable, rational polynomial.  Related to this it is possible to create
the Galois group and the splitting field of a rational polynomial.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        Radiroot documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{gap_upname}-%{version}

%conf
# Fix link to main GAP bibliography file
sed -i 's,/doc/manual,&bib.xml,' doc/manual.tex

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg/GAPDoc ../gapdoc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc} ../gapdoc
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-radiroot-doc -f %{oreon_filedir}/gap-pkg-radiroot-doc.list

%changelog

%autochangelog
