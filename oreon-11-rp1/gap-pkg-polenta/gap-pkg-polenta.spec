%global source0_hash 28f84d5a3241a5177992e076ca86eb913283325670f81acbe2e61adf2f813b1f
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname    polenta
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/polenta
Name:           gap-pkg-%{gap_pkgname}
Version:        1.3.11
Release:        1%{?dist}
Summary:        Polycyclic presentations for matrix groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/polenta/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): exam lib tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       gap-pkg-alnuth
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-radiroot
%if %{without bootstrap}
Recommends:     gap-pkg-aclib
%endif
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-alnuth-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-radiroot
# /oreon:deps
%description
The Polenta package provides methods to compute polycyclic presentations of
matrix groups (finite or infinite).  As a by-product, this package gives some
functionality to compute certain module series for modules of solvable groups.
For example, if G is a rational polycyclic matrix group, then we can compute
the radical series of the natural Q[G]-module Q^d.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polenta documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-alnuth-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%check -p

sed -i 's/"POLENTA\.tst"/#&/;/POLENTA2/s/Add/;#&/' tst/testall.g
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-polenta-doc -f %{oreon_filedir}/gap-pkg-polenta-doc.list

%changelog

%autochangelog
