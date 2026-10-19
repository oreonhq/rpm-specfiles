%global source0_hash efcfb86635f2f3e81afdd3a053023b58d79cee871140f0699b53172974dbe866
%global gap_pkgname sla
%global giturl      https://github.com/gap-packages/sla
Name:           gap-pkg-%{gap_pkgname}
Version:        1.6.2
Release:        1%{?dist}
Summary:        Computing with simple Lie algebras
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/sla/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-quagroup
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-quagroup
# /oreon:deps
%description
This package contains diverse functions for working with simple Lie algebras
in GAP (base fields are of characteristic 0).

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SLA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-sla-doc -f %{oreon_filedir}/gap-pkg-sla-doc.list

%changelog

%autochangelog
