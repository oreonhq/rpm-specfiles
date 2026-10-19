%global source0_hash 44ab0d1ee1caf0e537dd81c0325e40d40c67081627212cc0fdf02b8d9556906e
%global gap_pkgname ferret
%global giturl      https://github.com/gap-packages/ferret
Name:           gap-pkg-%{gap_pkgname}
Version:        1.0.17
Release:        1%{?dist}
Summary:        Backtracking search in permutation groups
License:        MPL-2.0
URL:            https://gap-packages.github.io/ferret/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Ferret is a reimplementation of parts of Jeffery Leon's Partition Backtrack
framework in C++, with extensions including:

- Ability to intersect many groups simultaneously.
- Improved refiners based on orbital graphs.

This package currently supports:

- Group intersection.
- Stabilizing many structures including sets, sets of sets, graphs, sets of
  tuples and tuples of sets.

This package can be used by users in two ways:

- When the package is loaded many built-in GAP functions such as
  'Intersection' and 'Stabilizer' are replaced with more optimized
  implementations.  This requires no changes to existing code.

- The function 'Solve' provides a unified interface to accessing all the
  functionality of the package directly.

%package doc
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Ferret documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%build -p

%configure --with-gaproot=%{gap_archdir}
%make_build
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-ferret-doc -f %{oreon_filedir}/gap-pkg-ferret-doc.list

%changelog

%autochangelog
