%global source0_hash 05c31c30ece36dbc97649307cba58d74c764b0c849e27b9b4fc60cee00ea54d3
%global gap_pkgname quagroup
%global giturl      https://github.com/gap-packages/quagroup
Name:           gap-pkg-%{gap_pkgname}
Version:        1.8.4
Release:        1%{?dist}
Summary:        Computations with quantum groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/quagroup/
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
QuaGroup provides functionality for computing in quantized enveloping algebras
of finite-dimensional semisimple Lie algebras.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        QuaGroup documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-quagroup-doc -f %{oreon_filedir}/gap-pkg-quagroup-doc.list

%changelog

%autochangelog
