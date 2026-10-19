%global source0_hash 7123e4100f1340a791d20bca1a8d9e6d9f09fe74a1c5fb15f1723899a1bb4553
%global gap_pkgname ace
%global giturl      https://github.com/gap-packages/ace
Name:           gap-pkg-%{gap_pkgname}
Version:        5.7.0
Release:        1%{?dist}
Summary:        Advanced Coset Enumerator
License:        MIT
URL:            https://gap-packages.github.io/ace/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples gap htm res-examples tst VERSION
BuildOption(check): tst/testall.g
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  tth
# /oreon:deps
%description
The ACE package provides a mechanism to replace GAP's usual Todd-Coxeter coset
enumerator by ACE, so that functions that behind the scenes use coset
enumeration will use the ACE enumerator.  The ACE enumerator may also be used
explicitly; both non-interactively and interactively.  However the package is
used, a plethora of options and strategies are available to assist the user in
avoiding incomplete coset enumerations.

%package doc
License:        MIT AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        Advanced Coset Enumerator documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{gap_upname}-%{version}

%build

./configure %{gap_archdir}
%make_build
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/etc ../../etc
make doc
rm -f ../../{doc,etc}
pushd standalone-doc
ps2pdf ace3001.ps ace3001.pdf
popd
%install -a
rm %{buildroot}%{gap_archdir}/pkg/%{gap_upname}/gap/CHANGES
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-ace-doc -f %{oreon_filedir}/gap-pkg-ace-doc.list

%changelog

%autochangelog
