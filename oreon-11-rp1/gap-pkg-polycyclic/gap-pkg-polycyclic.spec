%global source0_hash 0d82a709155db7a0d3db7dd7ce96a50c7e7f4bd07dd0085eb0009de01f1e2ca1
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname    polycyclic
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/polycyclic
Name:           gap-pkg-%{gap_pkgname}
Version:        2.18
Release:        1%{?dist}
Summary:        Algorithms on polycylic groups for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/polycyclic/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
%if %{without bootstrap}
Requires:       gap-pkg-alnuth
%endif
Requires:       gap-pkg-autpgrp
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-alnuth
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
# /oreon:deps
%description
This package provides algorithms for working with polycyclic groups.  The
features of this package include:
- creating a polycyclic group from a polycyclic presentation
- arithmetic in a polycyclic group
- computation with subgroups and factor groups of a polycyclic group
- computation of standard subgroup series such as the derived series, the
  lower central series
- computation of the first and second cohomology
- computation of group extensions
- computation of normalizers and centralizers
- solutions to the conjugacy problems for elements and subgroups
- computation of Torsion and various finite subgroups
- computation of various subgroups of finite index
- computation of the Schur multiplicator, the non-abelian exterior square and
  the non-abelian tensor square

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polycyclic groups documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix character encodings
for fil in gap/basic/colcom.gi; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-polycyclic-doc -f %{oreon_filedir}/gap-pkg-polycyclic-doc.list

%changelog

%autochangelog
