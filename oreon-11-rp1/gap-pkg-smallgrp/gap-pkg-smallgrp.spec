%global source0_hash none
%global gap_pkgname smallgrp
%global giturl      https://github.com/gap-packages/smallgrp
Name:           gap-pkg-%{gap_pkgname}
Version:        1.7.0
Release:        1%{?dist}
Summary:        Small groups library
License:        Artistic-2.0
URL:            https://gap-packages.github.io/smallgrp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --bare
BuildOption(install): gap id* small* tst
BuildOption(check): --bare tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  parallel
# /oreon:deps
%description
The Small Groups library gives access to all groups of certain "small" orders.
The groups are sorted by their orders and they are listed up to isomorphism;
that is, for each of the available orders a complete and irredundant list of
isomorphism type representatives of groups is given.

%package doc
License:        Artistic-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Small groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

%autosetup -n %{gap_upname}-%{version}

%conf
# Fix permissions
chmod a-x id9/idgrp9.g id10/idgrp10.g

%build -a

parallel %{?_smp_mflags} --no-notice gzip --best -f ::: id*/* small*/*
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-smallgrp-doc -f %{oreon_filedir}/gap-pkg-smallgrp-doc.list

%changelog

%autochangelog
