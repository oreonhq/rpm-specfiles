%global source0_hash none
%global gap_pkgname smallsemi
%global giturl      https://github.com/gap-packages/smallsemi
Name:           gap-pkg-%{gap_pkgname}
Version:        0.7.2
Release:        1%{?dist}
Summary:        GAP library of small semigroups
License:        GPL-3.0-or-later
URL:            https://gap-packages.github.io/smallsemi/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data gap tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
The Smallsemi package is a data library of semigroups of small size.  It
provides all semigroups with at most 8 elements as well as information of
various kinds about these objects.

%package doc
License:        GFDL-1.1-no-invariants-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Small semigroups documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-smallsemi-doc -f %{oreon_filedir}/gap-pkg-smallsemi-doc.list

%changelog

%autochangelog
