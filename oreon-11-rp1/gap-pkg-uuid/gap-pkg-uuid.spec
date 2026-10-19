%global source0_hash 30d83223fde65db8be8a496428347416816a296ea63605cc9d54bca4e4f9436c
%global gap_pkgname uuid
%global giturl      https://github.com/gap-packages/uuid
Name:           gap-pkg-%{gap_pkgname}
Version:        0.7
Release:        1%{?dist}
Summary:        RFC 4122 UUIDs for GAP
License:        BSD-3-Clause
URL:            https://gap-packages.github.io/uuid/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
This package provides functionality to create, query, and manipulate RFC 4122
UUIDs.

%package doc
License:        BSD-3-Clause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        UUID for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-uuid-doc -f %{oreon_filedir}/gap-pkg-uuid-doc.list

%changelog

%autochangelog
