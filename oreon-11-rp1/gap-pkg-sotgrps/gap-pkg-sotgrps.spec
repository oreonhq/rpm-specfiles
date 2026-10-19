%global source0_hash 2229d10bf599dd673a20359430a619ed6ac7bdb0d85bea02e8a6162512054df1
%global gap_pkgname sotgrps
%global giturl      https://github.com/gap-packages/sotgrps
Name:           gap-pkg-%{gap_pkgname}
Version:        1.4
Release:        1%{?dist}
Summary:        Construct and identify groups of small order type
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/sotgrps/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
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
The SOTGrps GAP package contains methods to construct the groups of a small
order type up to isomorphism.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SOTGrps documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-sotgrps-doc -f %{oreon_filedir}/gap-pkg-sotgrps-doc.list

%changelog

%autochangelog
