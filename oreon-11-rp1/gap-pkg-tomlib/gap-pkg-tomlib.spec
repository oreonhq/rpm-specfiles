%global source0_hash none
%global gap_pkgname tomlib
%global giturl      https://github.com/gap-packages/tomlib
Name:           gap-pkg-%{gap_pkgname}
Version:        1.2.11
Release:        1%{?dist}
Summary:        GAP Table of Marks package
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/tomlib/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data gap htm tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-atlasrep
Recommends:     gap-pkg-ctbllib
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  parallel
# /oreon:deps
%description
This package provides access to several hundred tables of marks of almost
simple groups and their maximal subgroups.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Table of Marks documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

%autosetup -n %{gap_upname}-%{version}

%build -a

parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.tom
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-tomlib-doc -f %{oreon_filedir}/gap-pkg-tomlib-doc.list

%changelog

%autochangelog
