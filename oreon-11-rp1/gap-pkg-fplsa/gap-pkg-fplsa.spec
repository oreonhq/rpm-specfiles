%global source0_hash 87e75b2bb464cc457999a4ab239ca6c4309e0a28eb4683be0ae0649bd862f8fc
%global gap_pkgname fplsa
%global gap_upname  FPLSA
%global giturl      https://github.com/gap-packages/FPLSA
Name:           gap-pkg-%{gap_pkgname}
Version:        1.2.8
Release:        1%{?dist}
Summary:        Finitely presented Lie algebras
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/FPLSA/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz
Patch:          %{name}-ini.patch
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap lib tst
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
# /oreon:deps
%description
When K is a finitely-presented Lie algebra, the GAP operation
IsomorphismSCTableAlgebra can be used to make the structure of K explicit, in
the form of an isomorphic algebra given by structure constants, which is much
more amenable to further computations.

This GAP package installs an alternative method for this operation, which
calls an external C program (fplsa version 4.0) to do the hard part of the
computation.  This speeds up the calculation and permits larger problems to be
attempted.  The external program has much additional functionality which is
not used by the present version of the package.

%package doc
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        FPLSA documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%build -p

./configure --with-gaproot=%{gap_archdir}
%make_build
%install -a
mkdir -p %{buildroot}%{_sysconfdir}
cp -p src/fplsa4.ini %{buildroot}%{_sysconfdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-fplsa-doc -f %{oreon_filedir}/gap-pkg-fplsa-doc.list

%changelog

%autochangelog
