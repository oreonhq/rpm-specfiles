%global source0_hash 8c7de16c0d4092418463b45ba160c9a592708c4eb20c7785fc9c009733683774
%global gap_pkgname fining
%global giturl      https://github.com/gap-packages/FinInG
Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.6
Release:        1%{?dist}
Summary:        Finite incidence geometry
License:        GPL-2.0-or-later
URL:            https://www.fining.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-cvec
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-grape
Requires:       gap-pkg-orb
Recommends:     gap-pkg-design
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-cvec
BuildRequires:  gap-pkg-design
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-orb
BuildRequires:  tex(makecell.sty)
# /oreon:deps
%description
FinInG is a GAP package for computation in Finite Incidence Geometry developed
by John Bamberg, Anton Betten, Philippe Cara, Jan De Beule, Michel Lavrauw and
Max Neunhoeffer.  It provides functionality:
- to create and explore finite incidence structures, such as finite projective
  spaces, finite classical polar spaces, generalized polygons, coset
  geometries, finite affine spaces, and many more;
- to explore algebraic varieties in finite projective and finite affine
  spaces;
- that deals with the automorphism groups of incidence structures, and
  functionality integrating these automorphism groups with the group
  theoretical capabilities of GAP;
- to explore various morphisms between finite incidence structures.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LPPL-1.3a
Summary:        FinInG documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-fining-doc -f %{oreon_filedir}/gap-pkg-fining-doc.list

%changelog

%autochangelog
