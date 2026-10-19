%global source0_hash 700b55f0b00b5578e2de014b286b815777644dde605c60f2095c8555eb508587
%global gap_pkgname spinsym
%global giturl      https://github.com/gap-packages/spinsym
Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.2
Release:        1%{?dist}
Summary:        GAP package for Brauer tables of spin-symmetric groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/spinsym/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap symdata tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-ctbllib
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
# /oreon:deps
%description
This package contains some p-modular character tables of Schur covers of
symmetric and alternating groups.  It also provides some more functionalities
related to these groups, for example, a method to construct character tables
of their maximal Young subgroups.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SpinSym documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-spinsym-doc -f %{oreon_filedir}/gap-pkg-spinsym-doc.list

%changelog

%autochangelog
