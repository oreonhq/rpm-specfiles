%global source0_hash 8920965473a74800237c7d57bcc7b52f1af118c5ef438b064d04ca333ac28827
%global gap_pkgname primgrp
%global giturl      https://github.com/gap-packages/primgrp
Name:           gap-pkg-%{gap_pkgname}
Version:        4.0.3
Release:        1%{?dist}
Summary:        Primitive permutation groups library
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/primgrp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --bare
BuildOption(install): data lib tst
BuildOption(check): --bare tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
The PrimGrp package provides the library of primitive permutation groups which
includes, up to permutation isomorphism (i.e., up to conjugacy in the
corresponding symmetric group), all primitive permutation groups of degree
less than 4096.  Groups of degree 4096 to 8191 must be downloaded separately
from https://doi.org/10.5281/zenodo.10411366 and then installed by following
the instructions given there.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Primitive permutation groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-primgrp-doc -f %{oreon_filedir}/gap-pkg-primgrp-doc.list

%changelog

%autochangelog
