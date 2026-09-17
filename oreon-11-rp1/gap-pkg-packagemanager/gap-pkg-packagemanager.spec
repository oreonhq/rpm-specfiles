%global source0_hash b4ffe9ea66b5d6fda6b5ebaf6b96f59e4d8ef30f6f387b02b6e15e039775655b

%global gap_pkgname packagemanager
%global gap_upname  PackageManager
%global giturl      https://github.com/gap-packages/PackageManager

Name:           gap-pkg-%{gap_pkgname}
Version:        1.6.3
Release:        %autorelease
Summary:        Basic package manager for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/PackageManager/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): binder etc gap tst

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-curlinterface

Requires:       gap-core

Recommends:     gap-pkg-curlinterface

%description
PackageManager is a basic collection of simple functions for installing and
removing GAP packages, with the eventual aim of becoming a full pip-style
package manager for the GAP system.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
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
# Tests cannot be run due to network use, so leave this empty

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/binder/
%{gap_libdir}/pkg/%{gap_upname}/etc/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
