%global source0_hash ec8cffca7e543662c522f0f6412cf994dc5fbe439d333f5f11e22923655b9c4e
%global gap_pkgname mapclass
%global gap_upname  MapClass
%global giturl      https://github.com/gap-packages/MapClass
Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.6
Release:        1%{?dist}
Summary:        Calculate mapping class group orbits for a finite group
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/MapClass/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
# /oreon:deps
%description
The MapClass package calculates the mapping class group orbits for a given
finite group.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        MapClass documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-mapclass-doc -f %{oreon_filedir}/gap-pkg-mapclass-doc.list

%changelog

%autochangelog
