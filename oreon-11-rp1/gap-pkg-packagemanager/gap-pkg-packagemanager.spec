%global source0_hash b4ffe9ea66b5d6fda6b5ebaf6b96f59e4d8ef30f6f387b02b6e15e039775655b
%global gap_pkgname packagemanager
%global gap_upname  PackageManager
%global giturl      https://github.com/gap-packages/PackageManager
Name:           gap-pkg-%{gap_pkgname}
Version:        1.6.4
Release:        1%{?dist}
Summary:        Basic package manager for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/PackageManager/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): binder etc gap tst
Requires:       gap-core
Recommends:     gap-pkg-curlinterface
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-curlinterface
# /oreon:deps
%description
PackageManager is a basic collection of simple functions for installing and
removing GAP packages, with the eventual aim of becoming a full pip-style
package manager for the GAP system.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs AND GPL-1.0-or-later
Summary:        Block design documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%check

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-packagemanager-doc -f %{oreon_filedir}/gap-pkg-packagemanager-doc.list

%changelog

%autochangelog
