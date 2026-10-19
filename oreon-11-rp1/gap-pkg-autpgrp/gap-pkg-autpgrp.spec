%global source0_hash d13725a9eadcc289160b88e96492965d19d968c80111ecd79a0b5953fa815966
%global gap_pkgname autpgrp
%global giturl      https://github.com/gap-packages/autpgrp
Name:           gap-pkg-%{gap_pkgname}
Version:        1.13.0
Release:        1%{?dist}
Summary:        Compute the automorphism group of a p-Group in GAP
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/autpgrp/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap htm tst
BuildOption(check): tst/testall.g
Requires:       gap-core
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  tth
# /oreon:deps
%description
The AutPGrp package introduces a new function to compute the automorphism
group of a finite p-group.  The underlying algorithm is a refinement of the
methods described in O'Brien (1995).  In particular, this implementation is
more efficient in both time and space requirements and hence has a wider range
of applications than the ANUPQ method.  Our package is written in GAP code and
it makes use of a number of methods from the GAP library such as the MeatAxe
for matrix groups and permutation group functions.  We have compared our
method to the others available in GAP.  Our package usually out-performs all
but the method designed for finite abelian groups.  We note that our method
uses the small groups library in certain cases and hence our algorithm is more
effective if the small groups library is installed.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Automorphism group documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%conf
# Use the system GAP macro file instead of the bundled version
rm -f doc/gapmacro.tex
ln -s %{gap_libdir}/doc/gapmacro.tex doc

%build

ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-autpgrp-doc -f %{oreon_filedir}/gap-pkg-autpgrp-doc.list

%changelog

%autochangelog
