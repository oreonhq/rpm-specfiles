%global source0_hash 28d309525ca1d9fe2ad9ce076d1608099c9987a1fa96bf990321b5dbc1b6537f

%global gap_pkgname fga
%global giturl      https://github.com/gap-packages/fga

Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.0
Release:        %autorelease
Summary:        Free group algorithms for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/fga/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
The FGA package provides methods for computations with finitely generated
subgroups of free groups.

It allows you to (constructively) test membership and conjugacy, and to
compute free generators, the rank, the index, normalizers, centralizers, and
intersections where the groups involved are finitely generated subgroups of
free groups.

In addition, it provides generators and a finite presentation for the
automorphism group of a finitely generated free group and enables writing any
such automorphism as word in these generators.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        FGA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files
%doc README.md
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
