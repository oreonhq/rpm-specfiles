%global source0_hash 928b94314330e139b52cb16f7dd0175062e2b621dc5687f2db24a0f8ebee90cc
%global gap_pkgname loops
%global giturl      https://github.com/gap-packages/loops
Name:           gap-pkg-%{gap_pkgname}
Version:        3.4.5
Release:        1%{?dist}
Summary:        Computing with quasigroups and loops
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/loops/
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
The LOOPS package provides researchers in nonassociative algebra with a
computational tool that integrates standard notions of loop theory with
libraries of loops and group-theoretical algorithms of GAP.  The package also
expands GAP toward nonassociative structures.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        LOOPS documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-loops-doc -f %{oreon_filedir}/gap-pkg-loops-doc.list

%changelog

%autochangelog
