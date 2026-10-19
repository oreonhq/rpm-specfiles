%global source0_hash 3a87c9df2245b9f2d5ac90999e7276dbb6890c2aad0f23f3411dd5881174debf
%global gap_pkgname normalizinterface
%global gap_upname  NormalizInterface
%global giturl      https://github.com/gap-packages/NormalizInterface
Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.1
Release:        1%{?dist}
Summary:        GAP wrapper for Normaliz
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/NormalizInterface/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.bz2
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin etc examples lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc-c++
BuildRequires:  libnormaliz-devel
BuildRequires:  make
# /oreon:deps
%description
Normaliz is software for computations with rational cones and affine monoids.
It pursues two main computational goals: finding the Hilbert basis, a minimal
generating system of the monoid of lattice points of a cone; and counting
elements degree-wise in a generating function, the Hilbert series.

As a recent extension, Normaliz can handle unbounded polyhedra.  The Hilbert
basis computation can be considered as solving a linear diophantine system of
inhomogeneous equations, inequalities and congruences.

This package allows creating libnormaliz cone objects from within GAP, and
gives access to it in the GAP environment.  In this way GAP can be used as an
interactive interface to libnormaliz.

%package doc
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP %{gap_upname} package
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%conf
# Defeat attempts to set an rpath
sed -i 's/\(NORMALIZ_RPATH_EXTRA=\)"-.*"/\1""/' configure

%build -p

sed -i '/GMP_PREFIX/s,-none,-%{_prefix},' configure
%configure --with-gaproot=%{gap_archdir}
%make_build
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-normalizinterface-doc -f %{oreon_filedir}/gap-pkg-normalizinterface-doc.list

%changelog

%autochangelog
