%global source0_hash 161585d1369e92ee12722320bb8eda055325e20ab7e0915c7a45ecb599cec32c
%global gap_pkgname laguna
%global giturl      https://github.com/gap-packages/laguna
Name:           gap-pkg-%{gap_pkgname}
Version:        3.10.1
Release:        1%{?dist}
Summary:        Lie AlGebras and UNits of group Algebras
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/laguna/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
Recommends:     gap-pkg-sophus
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-sophus
# /oreon:deps
%description
The LAGUNA package replaces the LAG package and provides functionality for
calculation of the normalized unit group of the modular group algebra of the
finite p-group and for investigation of Lie algebra associated with group
algebras and other associative algebras.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        LAGUNA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix end of line encodings
sed -i 's/\r/\n/g' doc/theory.xml

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-laguna-doc -f %{oreon_filedir}/gap-pkg-laguna-doc.list

%changelog

%autochangelog
