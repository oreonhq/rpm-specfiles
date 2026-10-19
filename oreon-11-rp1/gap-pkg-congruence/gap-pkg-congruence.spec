%global source0_hash 980799e39b1d5884d0dcf2be24aa75e541430f8988e47873a92ba3e8bd4e9ee5
%global gap_pkgname congruence
%global giturl      https://github.com/gap-packages/congruence
Name:           gap-pkg-%{gap_pkgname}
Version:        1.2.7
Release:        1%{?dist}
Summary:        Congruence subgroups of SL(2,Integers)
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/congruence/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
# /oreon:deps
%description
The Congruence package provides functions to construct several types of
canonical congruence subgroups in SL_2(Z), and also intersections of a finite
number of such subgroups.  Furthermore, it implements the algorithm for
generating Farey symbols for congruence subgroups and using them to produce a
system of independent generators for these subgroups.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Congruence documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-congruence-doc -f %{oreon_filedir}/gap-pkg-congruence-doc.list

%changelog

%autochangelog
