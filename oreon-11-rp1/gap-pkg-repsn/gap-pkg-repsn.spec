%global source0_hash 48f354e5e06e38c23c47bb6f87df9d15238f9943b1bc3115429484b676ff288c
%global gap_pkgname repsn
%global giturl      https://github.com/gap-packages/repsn
Name:           gap-pkg-%{gap_pkgname}
Version:        3.1.3
Release:        1%{?dist}
Summary:        Representations of finite groups
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/repsn/
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
This package is for computing matrix representations in characteristic zero of
finite groups.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        REPSN documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-repsn-doc -f %{oreon_filedir}/gap-pkg-repsn-doc.list

%changelog

%autochangelog
