%global source0_hash 5f048ba8b62283de5ce3b2aeaae87338d9c89f4e74e59618bc5d546b77faf877
%global gap_pkgname hecke
%global giturl      https://github.com/gap-packages/hecke
Name:           gap-pkg-%{gap_pkgname}
Version:        1.6.0
Release:        1%{?dist}
Summary:        Calculating decomposition matrices of Hecke algebras
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/hecke/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
This package contains functions for computing the decomposition matrices for
Iwahori-Hecke algebras of the symmetric groups.  As the (modular)
representation theory of these algebras closely resembles that of the
(modular) representation theory of the symmetric groups (indeed, the latter is
a special case of the former) many of the combinatorial tools from the
representation theory of the symmetric group are included in the package.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Hecke documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-hecke-doc -f %{oreon_filedir}/gap-pkg-hecke-doc.list

%changelog

%autochangelog
