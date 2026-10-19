%global source0_hash 3cc7fd0da3c258371f41b15718212ade864d1ddc7dcc28a0b3e82cf8316db4bd
%global gap_pkgname toric
%global gap_upname  Toric
%global giturl      https://github.com/gap-packages/toric
Name:           gap-pkg-%{gap_pkgname}
Version:        1.9.6
Release:        1%{?dist}
Summary:        Computations with toric varieties in GAP
License:        MIT
URL:            https://gap-packages.github.io/toric/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
Toric implements some computations related to toric varieties and
combinatorial geometry in GAP.  Affine toric varieties can be created and
related information about them can be calculated.

%package doc
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Toric documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-toric-doc -f %{oreon_filedir}/gap-pkg-toric-doc.list

%changelog

%autochangelog
