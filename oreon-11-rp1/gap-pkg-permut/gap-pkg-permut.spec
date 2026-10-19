%global source0_hash 4e8565fd74a34d55ec686bc80beda013a9f4050fb0176455fccbfe0eac72caec
%global gap_pkgname permut
%global giturl      https://github.com/gap-packages/permut
Name:           gap-pkg-%{gap_pkgname}
Version:        2.0.7
Release:        1%{?dist}
Summary:        Permutability in finite groups for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/permut/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-format
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-format-doc
# /oreon:deps
%description
The package permut contains some functions to deal with permutability in
finite groups.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Permut documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       gap-pkg-format-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-permut-doc -f %{oreon_filedir}/gap-pkg-permut-doc.list

%changelog

%autochangelog
