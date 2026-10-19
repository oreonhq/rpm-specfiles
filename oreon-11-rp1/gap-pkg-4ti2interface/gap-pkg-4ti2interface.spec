%global source0_hash 90a4120af58b2245116191aa774ddab3131ff8a809831aa09de968328bd8b9f0
%global gap_pkgname 4ti2interface
%global gap_upname  4ti2Interface
%global upver       2025.12-01
%global giturl      https://github.com/homalg-project/homalg_project
Name:           gap-pkg-%{gap_pkgname}
Version:        %(tr - . <<< %{upver})
Release:        1%{?dist}
Summary:        GAP interface to 4ti2
License:        GPL-2.0-or-later
URL:            https://homalg-project.github.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{gap_upname}-%{upver}.tar.gz
Patch:          %{name}-binaries.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples gap tst
BuildOption(check): tst/testall.g
Requires:       4ti2
Requires:       gap-pkg-io
# oreon:deps
BuildRequires:  4ti2
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
# /oreon:deps
%description
This package is a GAP interface to 4ti2.

%package doc
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP 4ti2Interface package
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n homalg_project-%{gap_upname}-%{upver}/%{gap_upname} -p1

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-4ti2interface-doc -f %{oreon_filedir}/gap-pkg-4ti2interface-doc.list

%changelog

%autochangelog
