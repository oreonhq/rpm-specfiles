%global source0_hash d6bfae0d62ccace262f8efccd39e9fc000b44745ee8a4dac83a4adab3b152804
%global gap_pkgname xmod
%global gap_upname  XMod
%global giturl      https://github.com/gap-packages/xmod
Name:           gap-pkg-%{gap_pkgname}
Version:        2.99
Release:        1%{?dist}
Summary:        Crossed Modules and Cat1-Groups for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/xmod/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples lib tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-autpgrp
Requires:       gap-pkg-groupoids
Requires:       gap-pkg-hap
Requires:       gap-pkg-smallgrp
Requires:       gap-pkg-utils
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-groupoids
BuildRequires:  gap-pkg-hap
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polymaking
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  gap-pkg-utils
BuildRequires:  tex(xy.sty)
# /oreon:deps
%description
This package allows for computation with crossed modules, cat1-groups,
morphisms of these structures, derivations of crossed modules and the
corresponding sections of cat1-groups.  Experimental functions for crossed
squares are now included.  In October 2015 a new section on isoclinism of
crossed modules was added.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        XMod documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-xmod-doc -f %{oreon_filedir}/gap-pkg-xmod-doc.list

%changelog

%autochangelog
