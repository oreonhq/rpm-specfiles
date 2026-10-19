%global source0_hash b474c879dcf28023a80608c1354974337e2e598287e5a81ded5ef5ba3e7d63ca
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname    alnuth
%global gap_skip_check %{?with_bootstrap}
%global giturl         https://github.com/gap-packages/alnuth
Name:           gap-pkg-%{gap_pkgname}
Version:        4.0.2
Release:        1%{?dist}
Summary:        Algebraic number theory for GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/alnuth/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): exam gap gp htm tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       gap-pkg-polycyclic
Requires:       pari-gp
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-radiroot
BuildRequires:  pari-gp
BuildRequires:  tth
# /oreon:deps
%description
Alnuth is an extension for the computer algebra system GAP and forms part of a
standard installation.  The functionality of Alnuth lies in ALgebraic NUmber
THeory.  It provides an interface from GAP to certain number theoretic
functions from the computer algebra system PARI/GP.  Most computations with
Alnuth rely on this interface.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Alnuth documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-alnuth-doc -f %{oreon_filedir}/gap-pkg-alnuth-doc.list

%changelog

%autochangelog
