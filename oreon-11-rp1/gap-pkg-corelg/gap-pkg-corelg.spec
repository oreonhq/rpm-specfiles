%global source0_hash f87443c2c3d74b8fdc78e7e77267dd757e3372063b8e2369e7dfd0384b701750
%global gap_pkgname corelg
%global giturl      https://github.com/gap-packages/corelg
Name:           gap-pkg-%{gap_pkgname}
Version:        1.57
Release:        1%{?dist}
Summary:        Computation with real Lie groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/corelg/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-sla
Recommends:     gap-pkg-singular
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-singular
BuildRequires:  gap-pkg-sla
# /oreon:deps
%description
The main object of the CoReLG package is to provide functionality for
computing with real (semi-)simple Lie algebras.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        CoReLG documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-corelg-doc -f %{oreon_filedir}/gap-pkg-corelg-doc.list

%changelog

%autochangelog
