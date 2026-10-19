%global source0_hash e5997fa5546317b258454c3d578ad3fc36e239e600eb0a82c0b99347d07bf66a
%global gap_pkgname wpe
%global gap_upname  WPE
%global giturl      https://github.com/gap-packages/WPE
Name:           gap-pkg-%{gap_pkgname}
Version:        0.8
Release:        1%{?dist}
Summary:        Efficient methods for working with wreath product elements
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/WPE/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
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
WPE provides efficient methods for working with Wreath Product Elements in GAP.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        WPE documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-wpe-doc -f %{oreon_filedir}/gap-pkg-wpe-doc.list

%changelog

%autochangelog
