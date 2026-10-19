%global source0_hash 11456e65b805d094147f92158222dce98f26fd74f2f1c85595c13fab7dfa8685
%global gap_pkgname singular
%global giturl      https://github.com/gap-packages/singular
Name:           gap-pkg-%{gap_pkgname}
Version:        2026.05.05
Release:        1%{?dist}
Summary:        GAP interface to Singular
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/singular/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): contrib gap lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core
Requires:       Singular
# oreon:deps
BuildRequires:  Singular
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-guava-doc
# /oreon:deps
%description
This package contains a GAP interface to the computer algebra system Singular.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Singular documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-guava-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-singular-doc -f %{oreon_filedir}/gap-pkg-singular-doc.list

%changelog

%autochangelog
