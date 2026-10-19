%global source0_hash cd7f173d7122b1e72a1f8ae3131e7685cd586dd362bd7efd21fe542fac5411c3
%global gap_pkgname sophus
%global giturl      https://github.com/gap-packages/sophus
Name:           gap-pkg-%{gap_pkgname}
Version:        1.27
Release:        1%{?dist}
Summary:        Computing in nilpotent Lie algebras
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/sophus/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-autpgrp
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
# /oreon:deps
%description
The Sophus package is written to compute with nilpotent Lie algebras over
finite prime fields.  Using this package, you can compute the cover, the list
of immediate descendants, and the automorphism group of such Lie algebras.
You can also test if two such Lie algebras are isomorphic.

The immediate descendant function of the package can be used to classify
small-dimensional nilpotent Lie algebras over a given field.  For instance,
the package author obtained a classification of nilpotent Lie algebras with
dimension at most 9 over F_2; see
http://www.sztaki.hu/~schneider/Research/SmallLie.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Sophus documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-sophus-doc -f %{oreon_filedir}/gap-pkg-sophus-doc.list

%changelog

%autochangelog
